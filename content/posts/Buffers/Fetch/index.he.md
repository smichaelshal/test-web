+++
Sources = [
"https://developer.arm.com/documentation/den0042/a/Caches",
"http://infolab.stanford.edu/pub/cstr/reports/csl/tr/95/685/CSL-TR-95-685.pdf",
"https://www.amd.com/content/dam/amd/en/documents/processor-tech-docs/programmer-references/24593.pdf",
"https://lwn.net/Articles/255364/",
"https://dl.acm.org/doi/pdf/10.1145/3524059.3532396",
"https://en.wikichip.org/wiki/intel/microarchitectures/skylake_(client)",
"https://pages.cs.wisc.edu/~markhill/papers/primer2020_2nd_edition.pdf",
"https://developer.arm.com/documentation/den0024/a/Caches/Cache-maintenance",
"https://developer.arm.com/documentation/ddi0487/latest/",
"https://inria.hal.science/hal-02509910/document",
"https://developer.arm.com/documentation/102336/0100/Data-Synchronization-Barrier",
"https://mariokartwii.com/armv8/ch30.html",
"http://www.rdrop.com/users/paulmck/scalability/paper/whymb.2010.07.23a.pdf",
"https://lwn.net/Articles/252125/",

]
authors = [
"Michael Shalitin",

]
math = true
date = "2025-01-11"
categories = [

]
series = [

]
title = "Fetch"
+++

# מבוא
## שליפה מוקדמת

מטרת השליפה המוקדמת היא להפחית את זמן ההשהיה של גישה לזיכרון. למרות שה-pipeline של ההוראות ויכולת הביצוע מחוץ לסדר (out-of-order) של מעבדים מודרניים יכולים להפחית חלק מהשהיית הזיכרון, זה מוגבל בעיקר לגישות שהן cache hit. כדי לכסות את כל זמן האחזור של גישה לזיכרון הראשי, ה-pipeline היה צריך להיות ארוך מאוד, מה שלא פרקטי. חלק מהמעבדים שאינם תומכים בביצוע מחוץ לסדר מנסים לפצות על כך באמצעות הגדלת מספר הליבות, אך זה יעיל רק אם כל הקוד יכול לפעול במקביל.

מנגנון ה-Prefetching יכול להסתיר את ה-latency בצורה נוספת. המעבד יכול לבצע Prefetching בעצמו כשהוא מופעל על ידי אירועים מסוימים (שליפה מוקדמת בחומרה) או כשהתוכנית מבקשת זאת במפורש (שליפה מוקדמת בתוכנה).

זרימת התוכנית נוטה להיות הרבה יותר צפויה מאשר דפוסי הגישה לנתונים. המעבדים המודרניים מצטיינים בזיהוי דפוסים, מה שמסייע בשיפור היעילות של prefetching.
#### שליפה מוקדמת בחומרה

שליפה מוקדמת בחומרה מופעלת בדרך כלל על ידי רצף של שתי cache miss או יותר בדפוס מסוים. החמצות אלה יכולות להתרחש בשורות cache עוקבות. בעבר, מנגנוני השליפה המוקדמת זיהו רק החמצות cache בשורות סמוכות, אך בחומרה עכשווית, הם מזהים גם דפוסים של דילוג על מספר קבוע של שורות cache ומתאימים את עצמם לכך.

אחת החולשות המרכזיות של השליפה המוקדמת היא שאינה יכולה לחצות גבולות page-ים, בגלל תמיכת המעבדים ב-demand paging. אם השליפה הייתה יכולה לחצות גבולות page-ים, היא הייתה עלולה להפעיל אירוע מערכת הפעלה כדי להעלות page לזיכרון, וזה עשוי לפגוע בביצועים.

לכן, גם אם השליפה המוקדמת מצליחה לנבא את הדפוסים בצורה מדויקת, התוכנית עדיין תחווה החמצות cache בגבולות page-ים, אלא אם תבצע שליפה מוקדמת או קריאה מפורשת מה-page החדש.

### שליפה מוקדמת - ספקולציה

היכולת של מעבד לבצע הוראות מחוץ לסדר מאפשרת להעביר הוראות קדימה אם אין התנגשויות ביניהן.
אמנם לא ניתן להשתמש בערך ישירות, אך המעבד יכול להתחיל לעבד אותו.
ה-load הספקולטיבי עושה את עבודתו והשהיית ה-load מוסתרת.

ל-loads ספקולטיביים יש יתרון נוסף בכך שהם טוענים את הערך ישירות לתוך הרגיסטר ולא לשורת ה-cache, שם הוא עלול להימחק שוב, למשל התיזמון (scheduling) של ה-thread מופסק.


## תיאור טכניקת האחזור המוקדם

שליפה מוקדמת (prefetching) יכולה להיות מסווגת לפי האם היא מחייבת או לא, והאם היא מבוצעת על ידי חומרה או תוכנה.
בשליפה מחייבת, הערך שמועבר קשור בזמן שבו נעשתה השליפה. לכן, שליפה מחייבת יכולה להיתקל במגבלות אם מעבד אחר משנה את המיקום בזיכרון בזמן שבין השליפה המוקדמת לקריאה בפועל, מה שעלול לגרום לערך שנשמר להתיישן. לעומת זאת, בשליפה לא מחייבת, הנתונים מועברים למיקום קרוב למעבד, כמו ל-cache, ומוחזקים שם עד לשימושם בפועל, תוך שמירה על קוהרנטיות. בשליפה לא מחייבת מבוססת חומרה, אין השפעה על מודלי עקביות הזיכרון, והיא יכולה לשמש לשיפור הביצועים בלבד.

שליפה אוטומטית מראש יכולה לשפר ביצועים על ידי קיצור זמן ההמתנה של פעולות קריאה שמתעכבות עקב סדר ההוראות בתוכנית. במקרים כאלה, הנתונים נכנסים ל-cache במצב נקי בזמן שהקריאה מתעכבת. מכיוון שהשליפה המוקדמת אינה מחייבת, מובטח שהקריאה תשיב את הערך הנכון ברגע שהפעולה תורשה להסתיים.

 
במקרה של כתיבה, ניתן להשתמש בשליפה בלעדית לקריאה כדי להשיג בעלות על השורה בזיכרון, מה שמאפשר לפעולת הכתיבה להתרחש במהירות ברגע שהיא מורשית. שליפה כזו מתאימה לפרוטוקולי invalidate, אך אינה מתאימה לפרוטוקולי עדכון שבהם קשה לשמור על עקביות בזמן פעולת הכתיבה. כמו בשליפה המוקדמת לקריאה, השורה שנשלפה מתבטלת או מתעדכנת אם מתבצעת כתיבה למיקום זה על ידי מעבד אחר בזמן שבין השליפה לכתיבה בפועל.

### יישום טכניקת האחזור מראש

הדרך הנפוצה לאכוף סדר בתוכנית היא לעכב את הנפקת הפעולה עד להשלמת פעולות קודמות. שליפה מוקדמת יכולה להשתלב במסגרת זו כאשר החומרה מנפיקה באופן אוטומטי שליפות מוקדמות (לקריאה או לכתיבה) עבור פעולות שמתעכבות עקב אילוצי סדר.

בקשת שליפה מוקדמת פועלת בדומה לבקשת קריאה או כתיבה רגילה מהזיכרון. בתחילה, נבדק אם השורה קיימת כבר ב-cache. אם כן, הבקשה מתבטלת, ואם לא, הבקשה מועברת לזיכרון. התשובה מהזיכרון ממוקמת ב-cache. אם יש בקשות נוספות לאותה שורה, הן משולבות בבקשת השליפה המוקדמת כדי למנוע כפילות.

אחת הבעיות בשליפה מוקדמת היא שה-cache עשוי להיות עמוס יותר, שכן הנתונים נגישים פעמיים – פעם אחת בשליפה המוקדמת ופעם נוספת בקריאה בפועל. עם זאת, מכיוון ששליפות מוקדמות מתבצעות רק כשפעולות רגילות מתעכבות, לא צפויה בעיה משמעותית בעומס ה-cache.

בנוסף, מבט קדימה בזרם ההוראות יכול לסייע בטכניקות של שליפה מוקדמת הנשלטות על ידי חומרה, במיוחד במעבדים התומכים בתזמון דינמי, חיזוי branch-ים וביצוע ספקולטיבי. מבט קדימה זה מאפשר לשליפה מראש לחפוף עם פעולות זיכרון המתעכבות, ולשפר את ביצועי המערכת.

יש כל מיני פרמטרים שמבדילים בין סוגי שליפה מקודמת:
- פעולות השליפה המוקדמת מתבצעות באופן אוטומטי על ידי החומרה או שהקומפיילר או המתכנת חייבים להפעיל אותן דרך תוכנה.
- האם הנתונים שנשלפים מראש הם עותק משותף או עותק בלעדי, בהתאמה לקריאה רגילה או לשליפה מוקדמת בלעדית לקריאה.
- ישנם שני סוגים של שליפה מוקדמת: ביוזמת הצרכן, שבו המעבד שמבצע את השליפה הוא הצרכן של הנתונים, וביוזמת היצרן, שבו מעבד אחד דוחף את הנתונים לכיוון מעבד אחר שצפוי לצרוך אותם.

### ביטול שליפות מוקדמות מיותרות

כדי למנוע שליפות מוקדמות מיותרות, יש לבדוק את הנתונים בהיררכיית ה-cache של המעבד לפני שהן נשלחות לזיכרון. בנוסף, חשוב לעקוב אחר פעולות שליפה מוקדמת פעולות כדי לאפשר מיזוג של שליפות מוקדמות עוקבות או פעולות רגילות לאותו שורת cache. דרך פשוטה להשיג זאת היא להתייחס לשליפות מוקדמות כאל פעולות קריאה וכתיבה רגילות בהיררכיית cache ללא נעילה. מעקב אחר שליפות מוקדמות קל יותר ממעקב אחר פעולות קריאה או כתיבה, כיוון שאין צורך לעקוב אחרי רגיסטר יעד או נתוני כתיבה. בנוסף, מכיוון שניתן לבטל שליפות מוקדמות, המעבד לא חייב לעצור אם חסרים משאבים למעקב אחריהן.

### סדר פעולות בשליפות מוקדמות לא מחייבות ביוזמת הצרכן

אין צורך לעכב שליפות קריאה מוקדמות בגלל פעולות קודמות, וגם אין צורך לעכב פעולות עתידיות כדי להמתין להשלמת השליפה המוקדמת. באופן דומה, אין מגבלות סדר עבור שליפות מוקדמות בלעדיות לקריאה אם מערכת הזיכרון מתמודדת עם השליפות הללו באמצעות תשובות בלעדיות מושהות. בחלק מהעיצובים ניתן להשתמש ב-buffer נפרד לשליפות מוקדמות, מה שעשוי לגרום לשינויים בסדר שלהן ביחס לפעולות אחרות. עם זאת, אילוצי סדר הופכים חשובים יותר אם מערכת הזיכרון משתמשת בתשובות בלעדיות נלהבות (eager), כיוון שתשובה נלהבת עשויה לאפשר לכתיבה שלאחר מכן לשורת הזיכרון להיות מטופלת על ידי ה-cache, אף על פי שעדיין יש צורך ב-invalidation acknowledgement. פתרון אפשרי לכך הוא להגדיל את ספירת הכתיבות הפעולות בשליפה מוקדמת בלעדית לקריאה, כך שפעולות עוקבות שמחכות להשלמת כתיבה ימתינו גם להשלמת השליפה המוקדמת.

### התייחסות לשליפות מוקדמות במערכת הזיכרון

במערכת הזיכרון, ניתן להתייחס לשליפות מוקדמות ביוזמת הצרכן כמו לפעולות קריאה או פעולות בלעדיות לקריאה, מה שמבטיח שהנתונים שנשלפו מראש יישמרו קוהרנטיים. למשל, אילוצי סדר חלים גם על שליפות מוקדמות. באופן דומה, יש לטפל בתשובות לשליפות מוקדמות כמו בתשובות רגילות במערכות שמיישמות ביטול תוקף מוקדם או אישורי עדכון. לכן, רוב המערכות אינן מבדילות בין שליפות מוקדמות לפעולות רגילות ברגע שהן יוצאות מתחום המעבד.

# שליפה מוקדמת בתוכנה

יש 2 אספקטים שיש ל-prefetching בתוכנה:
- רמזים שאנחנו רוצים לתת לקומפיילר ולמעבד לביצועים טובים יותר
- התמודדות וסנכרון עם prefetching שמתרחש בחומרה.

## prefetch hints

תוכניות יכולות לבצע שליפה מוקדמת באופן ישיר למשל ב-c באמצעות ההוראה `_mm_prefetch` עבור כל מצביע בתוכנית.


ב-x86 הוראות השליפה המוקדמות (`PREFETCH`) מספקות לתוכנה את האפשרות לרמוז למעבד כי הנתונים המסוימים עשויים להידרש בקרוב. בתגובה, המעבד יכול לטעון מראש את שורת ה-cache שבה נמצאים הנתונים, מתוך ציפייה לשימוש עתידי בהם. ההוראה `PREFETCH` מרמזת לכך שיש לקרוא את הנתונים, בעוד שההוראה `PREFETCHW` מציינת כי הנתונים עומדים להיכתב. אם השורה נטענת מראש באמצעות `PREFETCHW`, המעבד עשוי לסמן אותה כ-modified (בפרוטוקול MESI).


ארכיטקטורת ARM מספקת רמזים למערכת הזיכרון, כולל `PRFM`, `RPRFM`, `LDNP` ו-`STNP`, אשר יכולים לשמש את התוכנה כדי להעביר לחומרה את הציפיות לגבי השימוש במיקומי זיכרון. המערכת יכולה להגיב על ידי נקיטת פעולות שמיועדות להאיץ את הגישה לזיכרון, אם היא מתרחשת, כגון טעינה מראש של הכתובת שצוינה לתוך cache אחד או יותר, בהתאם ליעד רמת ה-cache הפנימי וזרם הרמז.

ב-ARM הוראות טעינה מראש הן רמזים בלבד, ולכן התוכנה יכולה להתייחס אליהן כאל NOPs מבלי להשפיע על ההתנהגות הפונקציונלית של המכשיר. הוראות אלו אינן יוצרות exception של synchronous Data Abort, אך פעולות מערכת הזיכרון שנעשות כתוצאה מהן עשויות, במקרים חריגים, ליצור asynchronous External abort, המתבצע באמצעות SError interrupt exception.

הוראות ה-prefetch hint מגדירות את סוגי הרמזים לשליפה מראש. ההוראה מאותת למערכת הזיכרון שסביר להניח שגישה לזיכרון מסוג רמז לכתובת שצוינה או ממנה תתרחש בעתיד הקרוב. מערכת הזיכרון עשויה לנקוט פעולה כדי להאיץ את הגישה לזיכרון, כגון טעינה מראש של הכתובת שצוינה לתוך cache אחד או יותר.

עוד דוגמה לפעולה דומה לרמז ל-prefetch היא ההוראה `DC ZVA` לאיפוס שורת ה-cache ב-ARM בכך שהיא מספק רמז למעבד על סבירות השימוש העתידי בכתובות מסוימות. עם זאת, פעולת האיפוס עשויה להיות מהירה יותר משמעותית, מכיוון שהיא לא דורשת המתנה להשלמת גישה לזיכרון חיצוני. במקום לקרוא נתונים מהזיכרון לתוך ה-cache, השורות ב-cache מאופסות באופן ישיר. פעולה זו מאפשרת למעבד לדעת שהקוד ישנה לחלוטין את תוכן שורת ה-cache, ובכך מבטלת את הצורך בקריאה ראשונית של הנתונים.

## התמודדות עם prefetch בחומרה


במקרים מסוימים, שליפת הוראות מראש עלולה ליצור מצבים שבהם טיפול בפרוטוקול קוהרנטיות הזיכרון הופך לבלתי אפשרי. במצבים כאלה, יש צורך שהתוכנה תשתמש בהוראות להסדרת קוהרנטיות ו/או הוראות לניקוי ה-cache כדי להבטיח שקבלת הגישה לנתונים לאחר מכן תהיה קוהרנטית.

דוגמה למצב כזה היא עדכון טבלת עמודים, ואחריו גישה לדפים הפיזיים שאליהם מתייחסים הטבלאות המעודכנות. להלן רצף האירועים האפשרי כאשר התוכנה משנה את התרגום של דף וירטואלי A מעמוד פיזי M לדף פיזי N:

1. התוכנה מבטלת את ערך ב-TLB. הטבלאות המתרגמות את הדף הווירטואלי A לדף הפיזי M נשמרות כעת רק בזיכרון הראשי ואינן נמצאות ב-cache ה-TLB.

2. התוכנה משנה את ערך טבלת הדפים בזיכרון הראשי עבור הדף הווירטואלי A, כך שהוא מצביע על הדף הפיזי N במקום הדף הפיזי M.

3. התוכנה ניגשת לנתונים בדף הווירטואלי A.

בשלב 3, התוכנה מצפה מהמעבד לגשת לנתונים מהדף הפיזי N. עם זאת, המעבד עלול להביא מראש את הנתונים מהדף הפיזי M לפני שנעשה עדכון טבלת הדפים בשלב 2. זאת כיוון שההפניות לזיכרון הפיזי של טבלאות הדפים שונות מההפניות לזיכרון הפיזי של הנתונים, ולכן המעבד אינו מזהה את הצורך לבדוק קוהרנטיות ומניח שהבאת הנתונים מהדף הפיזי M בטוחה. התנהגות דומה יכולה להתרחש גם כאשר הוראות נשלפות מראש מעבר לעדכון טבלת הדפים.

כדי למנוע בעיה זו, התוכנה צריכה להשתמש בהוראת `INVLPG` או ב-`MOV CR3` מיד לאחר עדכון טבלת העמודים. כך מבטיחים שאחזור ההוראות והגישה לנתונים לאחר מכן ישתמשו בתרגום הנכון של דף וירטואלי לדף פיזי. אין צורך לבצע פעולת ניקוי TLB לפני עדכון הטבלה.

עוד מקרה נפוץ שצריך לטפל ב-prefetch בחומרה הוא כשמשתמשים ב-self-modifying-code. 

 הבעיה נגרמת כשכותבים ערכים חדשים להוראות לביצוע והוראות מיושנות עשויות להימצא ב-Instruction Queue וב-Instruction cache, ולכן התוכנית צריכה להסיר אותן לפני שתמשיך.  

פעולות כאלו עלולות לדרוש ניקוי או ביטול cache-ים. קוד המעורב בהעתקת זיכרון משתמש בהוראות טעינה ואחסון, הפועלות בצד הנתונים של המעבד. אם cache הנתונים משתמש במדיניות write-back באזור שבו נכתב הקוד, יש לנקות את הנתונים מה-cache לפני הפעלת הקוד החדש. זאת כדי להבטיח שהנתונים שנכתבו יוצאים מה-cache ומועברים לזיכרון הראשי, ואז יהיו זמינים ללוגיקת שליפת הפקודות. בנוסף, אם האזור שאליו נכתב הקוד שימש קודם לכן לתוכנה אחרת, cache ההוראות עלול להכיל קוד ישן שלא הוסר מהזיכרון הראשי. לכן, ייתכן שיהיה צורך גם לנקות את cache ההוראות לפני הסתעפות לקוד החדש שהועתק.

ב-ARM הוראת `isb` מיועדת למטרה זו. היא מטהרת את כל ההוראות בתור ההוראות וממתינה להשלמה של כל הוראות הביצוע הנוכחיות (הוראות שכבר עברו את שלב התור). לאחר מכן, אחזור ההוראות (fetching) יתחיל מחדש.

הוראת `isb` מבטיחה שכל הוראות הביצוע הושלמו, אך מדובר בהשלמה רק של ה-pipeline של ההוראות. כלומר, פעולות הקשורות ל-load/store (כגון גישה לזיכרון, cache, TLBs ויחידות אחרות שקוראות זיכרון) עשויות לא להיות מושלמות.


עוד הוראה נפוצה ב-ARM לפתרון של הבעיות האלו היא ההוראה `IC IVAU,Xn`  שמבטלת את הערכים השמורים ב-cache ההוראות עבור הכתובת שניתנת, בכל הליבות. זה מאלץ כל fetch עתידי של הוראות מאותה כתובת לקבל miss ב-cache ההוראות ולקרוא את הערכים החדשים ישירות מהיררכיית זיכרון הנתונים. בנוסף, ההוראה משפיעה גם על ה-fetch queue, כך שהיא נוגעת במכונות הקשורות ל-fetching הוראות.

עוד דגש קטן שצריך לזכור ב-ARM כשהוראת DSB מתבצעת, כל הוראה המופיעה בסדר התוכנית לאחר ה-DSB לא יכולה לשנות מצב של המערכת או לבצע פונקציות כלשהן עד שה-DSB יושלם. החריגים הם פעולות פנימיות של המעבד, כמו שליפה מהזיכרון ופענוח.

שליפה מוקדמת מהזיכרון יכולה להתבצע עד למרחק מסוים מהנקודה הנוכחית של הביצוע. שליפה מוקדמת כזו עשויה לכלול מספר קבוע או משתנה של הוראות, ויכולה לעקוב אחרי כל נתיב ביצוע עתידי אפשרי. לגבי כל סוגי הזיכרון:

- ה-PE (Processing Element) יכול לשלוף הוראות מהזיכרון בכל עת מאז אירוע סינכרון ההקשר האחרון באותו PE.
- הוראות שנשלפו בדרך זו עשויות להתבצע מספר פעמים אם נדרש על פי ביצוע התוכנית, מבלי להחזיר אותן מהזיכרון. בהעדר אירוע סינכרון הקשר, אין הגבלה על מספר הפעמים שבהן הוראה עשויה להתבצע מבלי לבצע fetch מהזיכרון.


# שליפה מוקדמת בחומרה

לפני שניתן לבצע הוראה היא נשלפת (fetched) וממוקמת במה שנקרא Instruction queue. התור הוא חלק מסביבה גדולה יותר הידועה בשם Instruction pipeline. ה-pipeline כולל שליפה, פענוח, ביצוע, השלמה ופרישה (retirement) של ההוראות.


רכיבים המכונים fetch buffers, יכולים לשמש בתהליכי קריאה במערכות מסוימות. לדוגמה, ליבות עיבוד לרוב כוללות prefetch buffers שמבצעים קריאה מוקדמת של הוראות מהזיכרון לפני שהן מוזנות ל-pipeline. באופן כללי, buffers אלו פועלים מאחורי הקלעים ואינם נראים לעין המשתמש. עם זאת, יש לקחת בחשבון סיכונים פוטנציאליים הקשורים בהם כאשר דנים בכללי סדר הזיכרון.

## עקביות במודל הזיכרון

### ב-AMD

כאשר מתבצע מעבר מצב ב-cache בעקבות פעולות קריאה, בדיקה לקריאה או בדיקה לכתיבה, ייתכן שהמעבר ייגרם כתוצאה משליפה מוקדמת או ביצוע ספקולטיבי.

במעבדי AMD החל מסדרה 17h, המעבר למצב Modified אינו מתרחש באופן ספקולטיבי, אם כי ה-cache עדיין יכול לקבל נתונים שנכתבו מ-cache אחר באופן ספקולטיבי, מה שגורם לשורה להיכנס למצב Dirty. יישומים מסוימים עשויים לתמוך רק בתת-קבוצה של מצבי MOESDIF. הפעולה הספציפית של אותות וטרנזקציות bus חיצוני והאופן שבו הם משפיעים על מצב MOESDIF של cache תלויים במימוש. לדוגמה, יישום עשוי להמיר פספוס כתיבה בסוג זיכרון write-back לשני שינויים נפרדים במצב MOESDIF: הראשון, פספוס קריאה שיכניס את שורת ה-cache למצב Exclusive, ולאחר מכן hit כתיבה על השורה הזו שתשנה את מצב השורה ל-Modified.

### ב-ARM

ארכיטקטורת Arm מתירה שליפת הוראות מראש, כולל אפשרות של שליפה ספקולטיבית:

 "כמה רחוק מנקודת הביצוע הנוכחית נשלפים הוראות יישום מוגדר. שליפה מוקדמת כזו יכולה להיות מספר קבוע או משתנה דינמית של הוראות, ויכול לעקוב אחר כל נתיב ביצוע עתידי אפשרי או אחר. עבור כל סוגי הזיכרון, ייתכן שה-PE היה מביא את ההוראות מהזיכרון בכל עת מאז אירוע סנכרון ההקשר האחרון באותו PE." 

עם זאת, שליפת פקודות אחת עשויה להיות לא עקבית עם שליפות קודמות לפי סדר התוכנית, מה שעלול להוביל לנתונים ולזרמי הוראות שאינם מסונכרנים זה עם זה.

ארכיטקטורת Arm אינה מבטיחה עקביות בין שליפות מאותו מיקום זיכרון: שליפת פקודה אינה מבטיחה ששליפה מאוחרת יותר מאותו מיקום לא תחשוף הוראה ישנה יותר.


### שליפה Prefetching לא מחייבת

שליפה מוקדמת לא מחייבת לבלוק B היא בקשה למערכת הזיכרון הקוהרנטי לשנות את מצב הקוהרנטיות של B באחד או יותר מה-cache-ים. מימושים של שליפות מוקדמות לא מחייבות יכולים להתבצע מבלי להשפיע על מודל עקביות הזיכרון, מה שהופך אותן לשימושיות עבור שליפת cache פנימית מראש (למשל, דרך stream buffers) וגם עבור ליבות עם ביצועים אגרסיביים יותר.

כאשר מבצעים פעולות ספקולטיביות של load או store שמבוטלות בהמשך (נמעכות), הן עשויות להיראות כמו שליפות מוקדמות לא מחייבות, מה שמאפשר לספקולציה זו להתקיים מבלי להשפיע על מודל עקביות זיכרון חזק כמו SC. אם ה-load נמעך, הליבה מוחקת את עדכון הרגיסטר ומסירה כל השפעה פונקציונלית של הפעולה, כאילו היא לא התבצעה כלל.

במקרה של שליפות מוקדמות לא מחייבות, אין צורך לבטל אותן כאשר מדובר ב-cache, מכיוון שאחזור מוקדם של הבלוק עשוי לשפר את הביצועים אם ה-load תבוצע מחדש. עבור store, הליבה עשויה להוציא בקשה לקבלת הבלוק במצב modified לא מחייבת מוקדמת, אך היא לא תשלים את הפעולה עד שה-store תהיה מובטחת להתחייב.

במערכת בה הליבה מתוזמנת באופן דינמי, ייתכן ש-loads ו-stores יתבצעו בסדר שאינו עוקב אחר סדר התוכנית (program order). מודל ה-SC אינו מושפע מסדר השליפות המוקדמות הלא מחייבות, כיוון ש-SC דורש רק שה-loads וה-stores של ליבה מסוימת ייגשו ל-cache שלה לפי סדר התוכנית. קוהרנטיות הזיכרון מחייבת שבלוקי ה-cache יהיו במצבים המתאימים כדי לקבל פעולות load ו-store. חשוב לציין, ש-SC (או כל מודל עקביות זיכרון אחר):

- מכתיב את הסדר שבו פעולות load ו-store מיושמות על זיכרון קוהרנטי.
- אינו מכתיב את סדר פעילות הקוהרנטיות.

## מעבדי intel

במעבדי Skylake של intel, בהתחלה הוראות נשלפות מה-cache L2 לתוך ה-cache L1. cache ה-L1 הוא cache אסוציאטיבי בגודל 32 KiB עם 8 ways, בדומה לדורות קודמים. אחזור ההוראות מתבצע בחלון של 16 בתים, גודל שלא השתנה במשך מספר דורות. בכל מחזור, ניתן להביא עד 16 בתים של קוד, אך יש לזכור שהמשאב הזה מתחלק באופן שווה בין שני ה-thread-ים, כך שכל thread מקבל כל מחזור אחר. בשלב זה, ההוראות עדיין מוגדרות כ-macro-ops (כלומר, הוראות ארכיטקטוניות באורך משתנה של x86) ונכנסות ל-pre-decode buffer להכנה ראשונית.

הוראות x86 הן מורכבות, בעלות אורך משתנה, קידוד לא עקבי, ויכולות לכלול מספר פעולות. ב-pre-decode buffer, מזוהים ומסומנים גבולות ההוראות. זיהוי הגבולות הוא משימה מאתגרת, וקביעת האורך דורשת בדיקה של מספר בתים של ההוראה. בנוסף לסימון הגבולות, מתבצע פענוח של קידומות ובדיקה של מאפיינים שונים, כמו branch-ים. בדומה למיקרו-ארכיטקטורות קודמות, ל-pre-decode יש תפוקה של 6 macro-ops למחזור או עד שכל 16 הבתים נצרכים, מה שיקרה קודם.

אם ה-predecoder אינו מצליח לנצל את כל הבלוק של 16 בתים, תפוקת ההוראות עלולה להיות נמוכה משמעותית. לדוגמה, אם בלוק חדש מכיל 7 הוראות, 6 מהן יעובדו במחזור הראשון, אך המחזור השני יתבזבז כולו על ההוראה האחרונה, מה שיוביל לתפוקה נמוכה של 3.5 הוראות למחזור. במצב דומה, אם בלוק מכיל 4 הוראות מלאות ובית אחד מההוראה החמישית, 4 ההוראות הראשונות יעובדו במחזור הראשון, והמחזור השני יידרש עבור ההוראה האחרונה, מה שיוביל לתפוקה ממוצעת של 2.5 הוראות למחזור. מקרים מיוחדים, כמו הוראות עם קידומת שינוי אורך (LCP), יכולים לגרום לעיכובים נוספים.

תהליך זה עובד בשיתוף עם יחידת חיזוי ה-branch-ים, שמנסה לנחש את זרימת ההוראות. ב-Skylake, מנגנון חיזוי הbranch-ים שופר, והחיזוי השגוי של יעד קפיצה ישירה גורם כעת לפחות עונש בביצועים (זמן חביון נמוך יותר). כמו כן, המנבא (predictor) ב-Skylake יכול לנתח יותר נתונים בזרם הבייטים בהשוואה לארכיטקטורות קודמות, אם כי השיפורים המדויקים בחיזוי ה-branch-ים לא נחשפו על ידי אינטל.

ה-IDQ מבצע מספר אופטימיזציות נוספות בעת שמירת הוראות בתור. המנגנון בשם Loop Stream Detector (LSD) בתוך ה-IDQ מסוגל לזהות לולאות שמתאימות לשימוש ב-IDQ ולנעול אותן. ה-LSD מאפשר להזרים רצף של µOPs ישירות מה-IDQ ברציפות, מבלי צורך בשליפה, פענוח או ניצול cache-ים ומשאבים נוספים. תהליך הסטרימינג נמשך ללא הגבלת זמן עד שמתרחשת תחזית שגויה של branch. יש לציין כי במהלך פעילות ה-LSD, שאר החלקים של ה-front-end למעשה מושבתים.

