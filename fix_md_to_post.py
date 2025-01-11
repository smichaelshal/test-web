import os
import re
import yaml
import toml
import shutil
from datetime import datetime
from pathlib import Path
import argparse
from typing import Dict, List, Union

all_sources = set()

PATTERN_TAGS = r'(?<!\S)#[\w/]+'
PATTERN_COMMENTS = r'%%[\s\S]*?%%'
PATTERN_IMAGE = r'!\[\[(.+?)\]\]'
PATTERN_OBSIDIAN_LINK = r'\[([^\]]+)\]\(obsidian://open\?vault=[^\)]+\)'
PATTERN_IMAEG_MD = r'!\[.*?\]\(([^()]+(?:\([^()]*\)[^()]*)*)\)'

languages_map = {
    'litmus':'c',
    'cat': 'ocaml',
    'bell': 'ocaml',
}

NOT_TRANSLATED_MSG = 'The page has not been translated yet.'

patterns_to_clean = [PATTERN_TAGS, PATTERN_COMMENTS]

default_config = dict(
    authors=['Michael Shalitin'],
    math=True,
    date=datetime.now().strftime('%Y-%m-%d'),
    tags=list(),
    categories=list(),
    series=list(),
)


class FixRegex:

    def __init__(self, data: str):
        self.data = data

    def fix(self) -> str:
        for pattern in patterns_to_clean:
            self.data = self.clean_by_regex(pattern)
            self.data = self.fix_image()
    
        self.data = self.replace_obsidian_links('https://smichaelshal.github.io')

        self.data = self.replace_languages()

        self.data = self.add_linenos_to_codeblocks()
        
        return self.data


    def replace_language(self, src_language: str, dst_language: str) -> str:
        PATTERN_LANGUAGE = '```{language}'
        return re.sub(PATTERN_LANGUAGE.format(language=src_language), PATTERN_LANGUAGE.format(language=dst_language), self.data)

    def add_linenos_to_codeblocks(self) -> str:
        PATTERN_LINENOS = r'```(\w+)\n'
        replacement = r'```\1 {linenos=inline}\n'
        return re.sub(PATTERN_LINENOS, replacement, self.data)

    def clean_by_regex(self, regex: str) -> str:
        return re.sub(regex, '', self.data)
    
    def fix_image(self) -> str:
        def replace_match(match: re.Match) -> str:
            filename = match.group(1)
            return f'![]({filename})'
        return re.sub(PATTERN_IMAGE, replace_match, self.data)
    
    def replace_obsidian_links(self, url: str) -> str:
        def replacement(match):
            text = match.group(1)
            return f'[{text}]({url})'
        
        updated_text = re.sub(PATTERN_OBSIDIAN_LINK, replacement, self.data)
        return updated_text
    
    def replace_languages(self) -> str:
        for src_language in languages_map:
            self.data = self.replace_language(src_language, languages_map[src_language])
        return self.data


class YamlToToml:

    def __init__(self, data: str, title: str):
        self.data = data
        self.config = None
        self.title = title

    def clean_unknow_fields(self) -> None:
        keys_to_delete = list()
        for key in self.config:
            if self.config[key] == '???' or key == 'cssclasses':
                keys_to_delete.append(key)
        
        for key in keys_to_delete:
            del self.config[key]

    def add_default_keys(self, default_config: Dict[str, str]) -> Dict[str, str]:
        for key in default_config:
            if key not in self.config:
                self.config[key] = default_config[key]
        
        if 'title' not in self.config:
            self.config['title'] = self.title
        return self.config

    def format_toml_list_multiline(self, toml_data: str) -> str:
        lines = []
        for line in toml_data.splitlines():
            if ' = [' in line and ']' in line:  # Detect TOML lists
                key, values = line.split('=', 1)
                key = key.strip()
                values = values.strip()[1:-1]  # Remove [ ]
                items = [v.strip() for v in values.split(',')]
                formatted_list = f'{key} = [\n' + ',\n'.join(f'{item}' for item in items) + '\n]'
                lines.append(formatted_list)
            else:
                lines.append(line)
        return '\n'.join(lines)

    def convert_yaml_to_toml(self) -> str:
            # Find the YAML frontmatter block
            yaml_match = re.match(r'^---\n(.*?)\n---\n(.*)', self.data, re.DOTALL)
            if not yaml_match:
                return FixMarkdown.create_default_file(self.title, self.data)
            

            yaml_block = yaml_match.group(1)
            remaining_content = yaml_match.group(2)

            # Convert YAML to Python dictionary
            self.config = yaml.safe_load(yaml_block)

            if 'Sources' in self.config.keys():
                all_sources.update(self.config['Sources'])
           
            self.clean_unknow_fields()
            
            self.add_default_keys(default_config)
                
            # Convert Python dictionary to TOML
            toml_data = toml.dumps(self.config)

            # Format TOML lists to be multiline
            toml_data = self.format_toml_list_multiline(toml_data)

            # Replace YAML block with TOML block
            toml_block = YamlToToml.warp_toml(toml_data)
            new_content = f'{toml_block}{remaining_content}'
            return new_content
    
    @staticmethod
    def warp_toml(data: str) -> str:
        return f'+++\n{data}\n+++\n'


def rename_file(root, filename: str) -> str:
    name, ext = os.path.splitext(filename)

    new_filename = f'index.he{ext}'
    old_path = os.path.join(root, filename)
    new_path = os.path.join(root, os.path.join(name, new_filename))
    
    file_path = Path(new_path)
    file_path.parent.mkdir(exist_ok=True, parents=True)
  
    os.rename(old_path, new_path)
    return new_path


class FixImages:
      
    @staticmethod
    def find_images(path: str) -> List[str]:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        matches = re.findall(PATTERN_IMAEG_MD, content)
        return matches
    
    @staticmethod
    def copy_images(image_paths: str, source_dir: str, target_dir: str) -> None:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        for image_path in image_paths:
            source_path = os.path.join(source_dir, image_path)
            target_path = os.path.join(target_dir, image_path)

            # Ensure the target subdirectories exist
            os.makedirs(os.path.dirname(target_path), exist_ok=True)

            if os.path.exists(source_path):
                shutil.copy2(source_path, target_path)

    @staticmethod
    def copy_images_from_file(file_path: str, source_dir: str, target_dir: str) -> None:
        image_paths = FixImages.find_images(file_path)
        if image_paths:
            FixImages.copy_images(image_paths, source_dir, target_dir)


class FixMarkdown:
    
    @staticmethod
    def add_index_file(root: str, title: str, data: str) -> None:
        content = FixMarkdown.create_default_file(title, data)
        with open(os.path.join(root, 'index.md'), 'w') as file:
                file.write(content)
    
    @staticmethod
    def create_default_file(title: str, data: str) -> str:
        config = default_config.copy()
        config['title'] = title
        toml_data = YamlToToml.warp_toml(toml.dumps(config))
        return f'{toml_data}\n{data}'
    
    @staticmethod
    def fix_content(content: str, title: str) -> str:

        fix_regex = FixRegex(content)
        fix_data = fix_regex.fix()

        yaml_to_toml = YamlToToml(fix_data, title)
        return yaml_to_toml.convert_yaml_to_toml()
    
    @staticmethod
    def fix_file_content(path: str, filename: str) -> None:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = file.read()
        except FileNotFoundError as e:
            exit(e)

        new_data = FixMarkdown.fix_content(data, os.path.splitext(filename)[0])

        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_data)

    @staticmethod
    def fix_file(root: str, filename: str, images_src: Union[str, None]) -> None:
        file_path = os.path.join(root, filename)
        
        FixMarkdown.fix_file_content(file_path, filename)
        new_path = rename_file(root, filename)
        new_root, _ = os.path.split(new_path)

        name, _ = os.path.splitext(filename)
        FixMarkdown.add_index_file(new_root, name, NOT_TRANSLATED_MSG)
        
        if images_src:
            FixImages.copy_images_from_file(new_path, images_src, new_root)
        

    @staticmethod
    def fix_directory(path: str, images_src: Union[str, None]) -> None:
        for root, _, files in os.walk(path):
            for filename in files:
                if filename.startswith('.') or filename.startswith('index'):
                    continue
                
                FixMarkdown.fix_file(root, filename, images_src)

    @staticmethod
    def fix_single_file(path: str, images_src: Union[str, None]):
        root, filename = os.path.split(path)
        FixMarkdown.fix_file(root, filename, images_src)


def run_cli():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--directory', '-d', help='Path to the directory markdown files')
    group.add_argument('--file', '-f', help='Path to the Obsidian markdown file')
    parser.add_argument('--images', '-i', help='Path to the Obsidian images directory')
    args = parser.parse_args()

    if args.directory:
        FixMarkdown.fix_directory(args.directory, args.images)
    elif args.file:
        FixMarkdown.fix_single_file(args.file, args.images)
    

def main():
    run_cli()
    print(all_sources)
    
    # path = r'/Users/michael/Desktop/smichaelshal-web/a/test-web/content/posts'
    # images_src = r'/Users/michael/Documents/Linux Kernel Docs v2'
    # fix_directory(path, images_src)
    # path = r'/Users/michael/Desktop/smichaelshal-web/a/test-web/content/posts/mb.md'
    # fix_single_file(path, images_src)

    # src = r'/Users/michael/Desktop/smichaelshal-web/a/test-web/content/posts/Models/Base Formal/fr.png'
    # dst = r'/Users/michael/Desktop/old/new_fr.png'
    # convert_image_to_white_background(src, src)

    # path = r'/Users/michael/Desktop/smichaelshal-web/a/test-web/content/posts/Barriers/mb/index.he.md'
    # root = r'/Users/michael/Desktop/smichaelshal-web/a/test-web/content/posts/Barriers/mb'
    # copy_images_from_file(path, images_src, root)


if __name__ == '__main__':
    main()

