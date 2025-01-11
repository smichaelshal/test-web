תסכם לי בפרוט את הקטעים הבאים למאמר מופרט:

# נושאים (תגים)

## כללי
#tearing 
#formal 
#out_of_order 
herd7
#barrier 
#speculation 
#atomic 
#buffer 
#coherence_protocol 
#store_release 
#acquire_release 



## כל הארכיטקטורות
#store_buffer 
#cache 
#cacheline 
data cache
instruction cache


## חלק הארכיטקטורות

#lock 
#ll/cs 
#line_fill_buffer 
#rob 
#μop
#cumulative 
#propagate 
#cache_maintenance / ניהול מטמון


לבדוק אם כדי להתחיל לכתוב במאמר דבר ראשון על מצבי פרוטוקלי קורנטיות של cache (כלומר ,משפחת MESI או AMBA CHI ) #coherence_protocol 


כשאני מציג את CHI אפשר להציג אותו על ידי הצגה של תרשים זרימה (כמו Figure B2.3) ודרך ההסבר הזה להסביר על הסוגי טרנזקציות ועל הפרוטוקול עצמו בכלליות ולהסביר רק מה שקשור לתרשים, וככה אפשר להציג בצורה יחסית ממוקדת חלק מהפרוטוקול ושאם הקוראים רוצים להבין עוד פרטים על CHI הם יכולים לקרוא את התיעוד הרשמי ואני לא יהיה צריך להסביר את כל הפרוטוקול כי הוא גדול מידי כדי שאני אסביר אותו. #CHI


---

# נושאים (מתוך מאמרים)
## Memory Barriers: a Hardware View for Software Hackers
[מתוך](https://www.puppetmastertrading.com/images/hwViewForSwHackers.pdf)

1 Cache Structure

2 Cache-Coherence Protocols
	2.1 MESI States
	2.2 MESI Protocol Messages
	2.3 MESI State Diagram
	2.4 MESI Protocol Example
	
3 Stores Result in Unnecessary Stalls
	3.1 Store Buffers
	3.2 Store Forwarding
	3.3 Store Buffers and Memory Barriers
	
4 Store Sequences Result in Unnecessary Stalls
	4.1 Invalidate Queues
	4.2 Invalidate Queues and Invalidate Acknowledge
	4.3 Invalidate Queues and Memory Barriers
	
5 Read and Write Memory Barriers

6 Example Memory-Barrier Sequences
	6.1 Ordering-Hostile Architecture
	6.2 Example 1
	6.3 Example 2
	6.4 Example 3
	
7 Memory-Barrier Instructions For Specific CPUs
	7.1 Alpha
	7.2 AMD64
	7.3 ARMv7-A/R
	7.4 IA64
	7.5 PA-RISC
	7.6 POWER / Power PC
	7.7 SPARC RMO, PSO, and TSO
	7.8 x86
	7.9 zSeries
	
8 Are Memory Barriers Forever?

9 Advice to Hardware Designers



## Is Parallel Programming Hard, And, If So, What Can You Do About It?


[מתוך](file:///Users/michael/Desktop/1/%D7%AA%D7%9B%D7%A0%D7%95%D7%AA/kernel/files/perfbook-1c.2023.06.11a.pdf)

3 Hardware and its Habits 37
	3.1 Overview
		3.1.1 Pipelined CPUs
		3.1.2 Memory References
		3.1.3 Atomic Operations
		3.1.4 Memory Barriers
		3.1.5 Thermal Throttling
		3.1.6 Cache Misses
		3.1.7 I/O Operations
	3.2 Overheads
		3.2.1 Hardware System Architecture
		3.2.2 Costs of Operations
		3.2.3 Hardware Optimizations
	3.3 Hardware Free Lunch?
		3.3.1 3D Integration
		3.3.2 Novel Materials and Processes
		3.3.3 Light, Not Electrons
		3.3.4 Special-Purpose Accelerators
		3.3.5 Existing Parallel Software
	3.4 Software Design Implications


15 Advanced Synchronization: Memory Ordering 497
	15.1 Ordering: Why and How?
		15.1.1 Why Hardware Misordering?
		15.1.2 How to Force Ordering?
		15.1.3 Basic Rules of Thumb
	15.2 Tricks and Traps
		15.2.1 Variables With Multiple Values
		15.2.2 Memory-Reference Reordering
		15.2.3 Address Dependencies
		15.2.4 Data Dependencies
		15.2.5 Control Dependencies
		15.2.6 Cache Coherence
		15.2.7 Multicopy Atomicity
		15.2.8 A Counter-Intuitive Case Study
	15.3 Compile-Time Consternation
		15.3.1 Memory-Reference Restrictions
		15.3.2 Address- and Data-Dependency Difficulties
		15.3.3 Control-Dependency Calamities
	15.4 Higher-Level Primitives
		15.4.1 Memory Allocation
		15.4.2 Locking
		15.4.3 RCU
		15.4.4 Higher-Level Primitives: Discussion
	15.5 Hardware Specifics
		15.5.1 Alpha
		15.5.2 Armv7-A/R
		15.5.3 Armv8
		15.5.4 Itanium 
		15.5.5 MIPS
		15.5.6 POWER / PowerPC
		15.5.7 SPARC TSO
		15.5.8 x86
		15.5.9 z Systems
		15.5.10 Hardware Specifics: Discussion
	15.6 Memory-Model Intuitions
		15.6.1 Transitive Intuitions
		15.6.2 Rules of Thumb

C Why Memory Barriers? 673
	C.1 Cache Structure
	C.2 Cache-Coherence Protocols
		C.2.1 MESI States
		C.2.2 MESI Protocol Messages
		C.2.3 MESI State Diagram
		C.2.4 MESI Protocol Example
	C.3 Stores Result in Unnecessary Stalls
		C.3.1 Store Buffers
		C.3.2 Store Forwarding
		C.3.3 Store Buffers and Memory Barriers
	C.4 Store Sequences Result in Unnecessary Stalls
		C.4.1 Invalidate Queues
		C.4.2 Invalidate Queues and Invalidate Acknowledge
		C.4.3 Invalidate Queues and Memory Barriers
	C.5 Read and Write Memory Barriers
	C.6 Example Memory-Barrier Sequences
		C.6.1 Ordering-Hostile Architecture
		C.6.2 Example 1
		C.6.3 Example 2
		C.6.4 Example 3
	C.7 Are Memory Barriers Forever?
	C.8 Advice to Hardware Designers

## memory-barriers

[מתוך](file:///Users/michael/Desktop/1/%D7%AA%D7%9B%D7%A0%D7%95%D7%AA/kernel/files/memory-barriers.txt)


Abstract memory access model.
	Device operations.
	Guarantees.

What are memory barriers?
	Varieties of memory barrier.
	What may not be assumed about memory barriers?
	Address-dependency barriers (historical).
	Control dependencies.
	SMP barrier pairing.
	Examples of memory barrier sequences.
	Read memory barriers vs load speculation.
	Multicopy atomicity.

Explicit kernel barriers.
	Compiler barrier.
	CPU memory barriers.

Implicit kernel memory barriers.
	Lock acquisition functions.
	Interrupt disabling functions.
	Sleep and wake-up functions.
	Miscellaneous functions.

Inter-CPU acquiring barrier effects.
	Acquires vs memory accesses.

Where are memory barriers needed?
	Interprocessor interaction.
	Atomic operations.
	Accessing devices.
	Interrupts.

Kernel I/O barrier effects.

Assumed minimum execution ordering model.

The effects of the cpu cache.
	Cache coherency.
	Cache coherency vs DMA.
	Cache coherency vs MMIO.

The things CPUs get up to.
	And then there's the Alpha.
	Virtual Machine Guests.

Example uses.
	Circular buffers.

References.



---
%%

סדרי זיכרון
חומרה
פיזיקה
פילוסופיה
פורמליזציה
רעיונות כללים
שימוש בכלים
קרנל

%%

# מטרות

- [ ] לתת לעצמי שם (שיווק עצמי)
- [ ] לפוצץ תמוח לקרואים (להראות דברים כמו iriw)
- [ ] להראות שהעולם "גדול" (כלומר אפילו פעולה שנראית ברורה כמו גישה לזיכרון היא הופכת להרבה יותר מורכבת משאפשר בכלל לדמיין)
- [ ] ללמד חומר
- [ ] לגרום לקוראים לחקור ולהרחיב את הידע בנושאים האלה
- [ ] לכתוב מאמר בעברית על נושאים מתקדמים (כרגע אני לא מכיר שיש כאלה רלוונטים לנושא בעברית)
- [ ] מטרת המאמר היא הכרה והבהרת הנושא והוא לא מכיל תוכן "חדש" אין בו רעיונות שלא היו קודם.
- [ ] לגרום לעצמי להבין יותר טוב את החומר



- [ ] ללמד על סדרי זיכרון
- [ ] ללמד על ארכיטקטורות ספציפיות
- [ ] ללמד על הקרנל
- [ ] ללמד על חומרה
- [ ] לגעת בקטנה בפיזיקה
- [ ] לגעת בקטנה בפילוספיה


## קהל יעד
הערה:
	כרגע הקהל יעד הוא דובר עברית.

- מתכנתי קרנל
- מתכנתי low-level
- מתכנתים רגילים (עם רקע בסיסי)
- חובבי מחשבים (בלי ידע קודם)

- חברות מחשבים
- אנשים מהקהיליה

## סביבית קריאה (ה-context)
הערה:
	כרגע המאמרים נכתבים ב-markdown בעברית (לבדוק אם יש תמיכה)
	
- ב-github (בתוך github.io או gitbook)
- ב-pdf
- ב-word (אולי רק חלקים ספציפים שאני רוצה להציג ב-digitalwhisper)

- אולי ב-hackmd
- אולי ב-medium
- אולי ב-linkedin
- המבואות ידרשו סביבה רגילה (לא יהיה צרוך בריכוז גבוה במיוחד)
- הפרקים המתקדמים ידרשו סביבה שקטה (נצרך ריכוז גבוה)

## מה הקורא ירוויח מהקריאה
- ידע ארכיטקטוני חומרתי
- הבנה איך מחשבים מודרנים עובדים
- שיפור ההבנה איך מערכות הפעלה עובדות
- פתיחת המחשבה לכיוונים חדשים
- שבירת קונספציה על דברים שנראים פשוטים
- הכרת עולם המקביליות
- ידע בכתיבת קוד מקבילי ברמה גבוהה
- כניסה "רכה" למקביליות בקרנל (כמו מנגנון rcu)


## סוג המאמר
- הפרקים של המבואות יהיו לקריאה חד פעמית (שאמור להיות מספיק לקרוא אותם פעם אחת בלבד, ויהיה אפשר לקרוא אותם בצורה רציפה).
- הפרקים המתקדמים יהיו בסגנון "תנך", כלומר הקריאה לא אמורה להיות רציפה, וקריאת הפרק תיהיה ממוקדת לצורך ספציפי (כמו הסגנון של ה-understanding linux kernel שמצפה שיגשו אליו לפי הצורך)
- המאמר יהיה מחולק לפרקים שכל פרק יכיל תוכן חצי עצמאי (כלומר הוא יתבסס על פרקים קודמים, אבל לא כל הפרקים הקודמים יהיו רלוונטים לכל הפרקים הבאים).
- קריאת המאמר המלא תיהיה בצורה של גישה בכל פעם לפרק רלוונטי אחר (כי יכול להיות כמה סדרים לקריאה, למשל אם מישהו רק רוצה לקרוא על ARM אני לא צריך להכריח אותו לקרוא על x86 או על הקרנל)


## הערות ודגשים לעצמי
%% חשוב !!! %%

- לא לחזור על דברים שנאמרו כבר במאמר
- לא להכריח את הקורא לקרוא חומר לא רלוונטי
- להביא קישור לחומר שאני מתבסס עליו (הכוונה לחומר שאני מצפה שהקורא יקיר מראש).

#### מהמיילים של אפיק קסטיאל

לנסות לייצר "סיפור" או 'קו עלילתי" במאמר. %% חשוב !!! %%

לפני שניגשים לתוכן עצמו, שווה להסביר לקורא על מה הוא הולך לקרוא ולמה שווה לו להשקיע עכשיו את הזמן בקריאה, מה הוא יקבל מהמאמר בסוף וכו'.

לאחר מכן, שווה להציג את הטכנולוגיה, איזה בעיה היא באה לפתור? למה היא קיימת? למה אותי בתור קורא (או אותך בתור כותב) מעניין לקרוא/לכתוב דווקא עליה?

לאחר מכן אפשר להמשיך את הסקירה על הטכנולוגיה על ידי הצגת הפיצ'רים שבה או להחליט שמציגים 2-3 דוגמאות לשימוש בה ואז תור כדי הצגת הדוגמאות לסקור אותה.

בסוף שווה להכניס סיכום (אם המאמר ארוך אפשר להציג סיכומי ביניים במהלך המאמר) וסוג של Recap קצר.

## לבדוק
%% חשוב !!! %%

- לבדוק על המרת פורמטים (הכוונה מ-markdown ל-word או latex...)
- לבדוק אם המאמר צריך תצוגה של סרטון או gif להבהרה של הסבר
- לבדוק אם המאמר צריך להיות אינטרקטיבי (עם שאלות כמו של פול, או שהמאמר ימליץ על הרצת קוד מסויים, או הרצה של מבחן, או אפילו כתיבה על נייר (כמו שאני עושה לעצמי)).
- לבדוק אם כדאי לתת כמה הסברים חוזרים על נושא מסויים מכיוונים שונים לצורך הבהרת הנושא או שזה יגרום לקרוא להתעצבן בגלל החזרה המיותרת.
- לחשוב אם צורת המאמר צריכה להיות בסגנון סולם יעקוב (סגנון ספירילי - דיאלקטיקה הגליאנית), כלומר בכל פעם חוזרים על הנושאים אבל מעמיקים בהם יותר ויותר. (כמו הצורה שאני למדתי את החומר, וכמו הצורה שהקפיטל כתוב בה (לפי יפתח גולדמן)).
- לחשוב אם צריך לתת נקודות להארה של נושא מסויים או כיוון מחשבה שאני מצפה שהקרוא יחשוב (הכוונה היא כמו שהשאלות שפול עשה במאמרים שלו).
- לחשוב באיזה גוף כדאי להשתמש (הכוונה גוף ראשון, שני או שלישי).
- לחשוב אם המאמר יצפה שתוך כדי קריאה הקורא יצטרך לגשת לחומרים חיצוניים
- לחשוב אם המאמר יתעדכן או שהוא סטטי (כלומר האם יתוקן במקרה של טעות או למשל אם יתווסף לו עוד תוכן)
- לבדוק לגבי תרגום המאמר עצמו לאנגלית
- לחשוב אם כדאי שהמאמר יהיה open source וגם אחרים יכולו לשנות אותו או לפתוח issues ב-github למשל.
- לחשוב אם המאמר צריך להיות פתוח להרחבות (open closed principle)

### סביבת קריאה
- לבדוק אם כדאי לנסות לבנות את המאמר לקריאה במחשב או גם בטלפון
- לבדוק כמה זמן קריאה יהיה לכל קטע במאמר
- לבדוק אם אפשר להתאים את המאמר גם ל-light mode וגם ל-dark mode.

### סגנון השפה
לבדוק אם להכניס:

- מילים גבוהות
- מילים "עממיות"
- מילים צהליות (של היחידה)
- ביטויים ישראליים
- ביטויים באנגלית


## הנחות יסוד
- הקורא יכיר או יקרא על נושאים שאני מזכיר ומתבסס עליהם ואני לא מסביר אותם.
- הקריאה תתבצע בעתיד הקרוב (תווך של 20 שנים), (עד שתוכן המאמר לא יהיה רלוונטי), (הכוונה היא שכל עוד יש מחשבים שעובדים כמתואר - למשל מחשבים קוונטים כנראה לא יהיו רלוונטים).

---

# נושאים

## חומרה
### ה-caches
- איך ה-cache בנוי
- ריבוי מטמונים (גם כמה סוגים וגם כמה רמות)
- פיספוס cache
- פגיעת cache
### ה-buffers
- ה-store buffer
- ה-load buffer
- ה-forward buffer
- ה-combined buffer
- ה-fetch buffer
- ה-reorder buffer
- ה-line fill buffer

### ריבוי רכיבים
- ריבוי מעבדים
- ריבוי ליבות
- ריבוי threads

### טכניקות יעול
- ה-pipeline
- סכנות (hazard) במעבד
- ה-scheduler של המעבד
- ספקולציות (גם בהוראות וגם במידע)
- שינוי שם (Register renaming)

### אחר
- נעילת bus (קידומת lock למשל או כמו פעם ב-arm)

-  ה-multi copy atomic ו-non multi copy atomic ו-other multi copy atomic
- ה-single copy atomic

- ה-early write acknowledgment 

- גישות לזיכרון

- מירוצי נתונים
-  תור Invalidate

- ה-domain ב-arm
- ה-lor (region) ב-arm

- ה-decoder (של הוראות) (אולי רק ב-x86 ???)
- ה-uops (אולי רק ב-x86 ???)


## סדרי זיכרון
- סדר sc
- סדר tso (x86-tso)
- סדר רגוע
- מחוץ לסדר (out of order)

## מודלי זיכרון
- מודל armv7
- מודל armv8
- מודל x86-tso
- מודל ppc
- מודל lkmm

## פעולות אטומיות
- הסבר כללי על מה זה אטומי
- בלעדי
- פעולות rmw
- פעולות cas
- פעולות בלעדיות (גם ll/cs)

## מחסומי זיכרון
- מחסום מלא - mb
- מחסום חלקי rmw
- מחסום חלקי wmb
- מחסום חד כיווני acquire
- מחסום חד כיווני acquirePC
- מחסום חד כיווני release

## תלויות
- תלות מידע
- תלות בקרה
- תלות כתובת

```c
aaaaa
```

## פורמליזציה
- הכלי herd
- כלי diy ???
- שפת cat
- שפת bell
- מבחני litmus
- מתמטיקה
- דוגמאות ???
- מבחנים נפוצים ???

## קוהרנטיות
- למה צריך קוהרנטיות cache
- משפחת פרוטוקלי MESI (אולי להסביר על הכי מורחב MOESDIF)
- פרוטוקולי AMBA
- הצטברות (cumulative)
- התפשטות (propagate)
- פעולות snoop
- פעולות directory
- פעולות תחזוקת (maintenance) מטמון

## שימושים
- מנעולים
- קוד שינוי עצמי (self modifying code)

## קומפיילר
- ה-gcc
 - ה-volatile
 - אופטימיזציות
 - מודל של c11 ???
 - כתיבת אסמבלי inline
 - בנייה נכונה של structs (הכוונה לבניה עם המנעות מבעיות כמו false sharing ו-cahce bouncing...)
 -  מירוצי שפה

## אחר
- פיזיקה של סיבתיות
- פילוסופיה של סיבתיות
- ה-Out-Of-Thin-Air

## בעיות ידועות
- בעיית ABA
- בעיית false sharing
- בעיית cache bouncing
- קריעת זיכרון (גם קומפיילר וגם המעבד בגישות לא מיושרות וגישות לא בגודל מתאים)

---


[מתוך](https://www.linkedin.com/pulse/step-by-step-guide-writing-effective-technical-articles-majed-khalaf)

הימנע משימוש בז'רגון או במונחים טכניים שאולי הקהל שלך לא מכיר.

השתמש במשפטים ופסקאות קצרות כדי לפצל את הטקסט ולהפוך אותו לקריאה יותר.

חתוך מילים מיותרות: חפש דרכים לקצץ את הכתיבה שלך ולבטל כל מילים או ביטויים מיותרים.


---

מ-GPT

סיים בשאלה מעוררת מחשבה, קריאה לפעולה או תחזית הקשורה לעתיד הטכנולוגיה.

הבע את הקול והדעה שלך כאשר אתה מדבר על טכנולוגיה. נקודת המבט הייחודית שלך חשובה, אבל חשוב להבין את הנושא שלך לעומק לפני שאתה כותב עליו

---

- [ ] לבדוק אם הרעיון של invalid queue הוא כמו Early Write Acknowledgment

---

# סידורי זיכרון בהשקה לקרנל
%% Memory ordering with kernel touch %%

## מבוא (הצגת הבעיה)
להציג קטעי קוד בקרנל ואת הבעיות שיש להם בריצה מקבילה ללא טיפול מתאים

## גורמים לבעיה
פירוט על הרכיבים ועל הטכניקות שיכולות לגרום לסידור מחדש:

### ה-caches
- איך ה-cache בנוי
- ריבוי מטמונים (גם כמה סוגים וגם כמה רמות)
- פיספוס ו-פגיעת cache
#### קוהרנטיות caches
- למה צריך קוהרנטיות cache
- משפחת פרוטוקלי MESI (אולי להסביר על הכי מורחב MOESDIF)
- פרוטוקולי AMBA
- הצטברות (cumulative)
- התפשטות (propagate)
- פעולות snoop (לבדוק אם להדגים עם AMBA CHI)
- פעולות directory ??? 
- פעולות תחזוקת (maintenance) מטמון (לבדוק אם להדגים עם AMBA CHI)

### קומפיילר
 - אופטימיזציות
 -  מירוצי שפה ???

### ה-buffers
- ה-store buffer
- ה-load buffer
- ה-forward buffer
- ה-combined buffer
- ה-fetch buffer
- ה-reorder buffer
- ה-line fill buffer
- ה-decoder (של הוראות) (אולי רק ב-x86 ???)
- ה-uops (אולי רק ב-x86 ???)

### טכניקות יעול
- ה-pipeline
- סכנות (hazard) במעבד
- ה-scheduler של המעבד ???
- ספקולציות (גם בהוראות וגם במידע)
- שינוי שם (Register renaming)

### אחר
- פיזיקה של סיבתיות
- פילוסופיה של סיבתיות
- ה-Out-Of-Thin-Air
## דרכי התמודדות
### כללי
תיאור כללי של הרעיון של מחסומים ופעולות אטומיות:
#### מחסומי זיכרון
- מחסום מלא mb
- מחסום חלקי rmb
- מחסום חלקי wmb
- מחסום חד כיווני acquire
- מחסום חד כיווני acquirePC
- מחסום חד כיווני release

#### פעולות אטומיות
- הסבר כללי על מה זה אטומי
- בלעדי
- פעולות rmw
- פעולות cas
- פעולות בלעדיות (גם ll/cs)

#### בעיות ידועות
- בעיית false sharing
- בעיית cache bouncing
- קריעת זיכרון (גם קומפיילר וגם המעבד בגישות לא מיושרות וגישות לא בגודל מתאים)

#### תלויות
- תלות מידע
- תלות בקרה
- תלות כתובת

### מודלי זיכרון
#### כלי diy
- שפת cat
- שפת bell
- הכלי herd7
- מבחני litmus
- מתמטיקה
#### פירוט על מודלים
- LKMM
	- arch ???
	- formal model
- PPC
	- arch
	- formal model
- ARMv(7/8)
	- arch
	- formal model
- x86 (TSO) ???


%% לפצל לקבצים לפי כל נושא ולהוסיף Properties לכל קובץ %%

מאפיינים:
- רמת קושי
- רמת חשיבות
- רמת הערך המוסף שלי (כמה ערך מוסף התיאור שלי מביא על פני מאמרים אחרים)
- אורך משוער
- רמת העיניין שלי
- מקורות מידע

תגים:
- ארכיטקטורות
- נושאים שעליהם מתבסס הקובץ


---

- [x] ה-store buffer ++
- [ ] ה-load buffer ???
- [x] ה-forward buffer
- [x] ה-combined buffer ---
- [x] ה-fetch buffer <<< +

- [x]  ה-line fill buffer +
- [x] ה-invalidate queue ++ <<

- [x] ה-reorder buffer
- [x] ה-decoder (של הוראות) +
- [x] ה-uops +
- [x] ה-Register renaming +


- [x] ספקולציות ++

- [x] ה-Pipeline & Hazard +

- [x] אופטימיזציות בקומפיילר ++

- [x] אטומי
- [x] פעולות cas
- [x] בלעדי (גם ll/cs)
- [x]  פעולות rmw (???)

- [x] מחסום מלא mb
- [x] מחסום חלקי rmb
- [x] מחסום חלקי wmb
- [x] מחסום חד כיווני acquire
- [x] מחסום חד כיווני acquirePC
- [x] מחסום חד כיווני release

- [x] פעולות תחזוקת (maintenance) מטמון (לבדוק אם להדגים עם AMBA CHI)
- [x] הצטברות (cumulative)
- [x] התפשטות (propagate)


%% 

אתר אינדוקס קרנל - https://elixir.bootlin.com/linux/v6.10.6/source

תנסח מחדש את הקטעים הבאים בפירוט:
%%

%%
בנושאים גדולים אפשר לעשות חיפוש עם תגים וגם עם כותרות <<<

```
grep -irE "^#+ .*(קוהרנט|coheren)" . > ~/Desktop/out_search
```
%%

---

- [x] פעולות תחזוקת (maintenance) מטמון (לבדוק אם להדגים עם AMBA CHI)

- [x] cache 
- [x] cache maintenance
- [x] snoop
- [x] Multi-copy atomicity
- [x] AMBA CHI
- [x] AMBA CHI - ordering
- [x] AMBA CHI - טרנזקציות

- [x] domain
- [x] Early Write Acknowledgment  ???

- [x] סיבתיות (פיזיקה + פילוסופיה) ???
- [x] herd7 (cat + bell + diytools?) <<<<
- [x] formal (בסיס) יחסי בסיס (po, co, rf, fr, ext, int), אופרטורים מתמטים

- [x] ordering <<<
- [x] out of order

%% - [ ] cache coherence (לא גמור) %%

- [x] hardware  (כמו דומיינים ב-arm) ???


- [x] מבנה כללי של מערכת (דומיינים, socket-ים) (אולי עם ARM ו-ACE)

- [x] propagate (לא גמור)
- [x] cumulative (לא גמור)
- [x] lkmm barrier <<<

- [x] מחסום מלא mb
- [x] מחסום חלקי rmb
- [x] מחסום חלקי wmb
- [x] מחסום חד כיווני acquire
- [x] מחסום חד כיווני acquirePC
- [x] מחסום חד כיווני release


- [x] AMBA ACE Barrier ??? (סוכם)

- [x] models (sc, tso, xc) <<<

- [x] מחסומי תלות בסיס (תלות מידע, תלות כתובת, תלות שליטה)


- [x] lkmm math
- [x] lkmm litmus
- [x] lkmm code
- [ ] lkmm formal
- [ ] מחסומי תלות בסיס פורמלי ???

- [ ] formal (מתקדם) ???
- [ ] arm model ???
- [ ] ppc model ???

- [ ] לבדוק על `membarrier(2)` ה-syscall

- [ ] LORegion (acquire + release) ???
- [ ] טרנזקציות עם קוד ???
- [ ] הסבר קטן על ערוצים ב-AMBA CHI ???

- [ ] הדגמה של Early Write Acknowledgment (אולי עם ARM)

- [ ] מנגנוני ack-ים (לבדוק אם כדאי להסביר את זה עם ACE או אולי עם PPC)

- [ ] הדגמה של non-multi copy atomic (לא עם CHI אולי עם PPC או ARMv7 ו-ACE)

- [ ] לעשות מיפוי של MOESI ל-AMBA CHI (כולל סוגי טרנזקציות והתנהגות כללית ומתי כל טרנזקציה מתרחשת... (התאמה בין הפרוטוקול שיש בספר [A Primer on Memory Consistency and Cache Coherence ](https://pages.cs.wisc.edu/~markhill/papers/primer2020_2nd_edition.pdf)לבין AMBA CHI))



%% 
!!! חשוב
רעיון לפרוייקט:
אפשר לעשות מערכת שפועלת בצורה מבוזרת בין מחשבים עם זיכרון מבוזר ושכל פעם שיש page fault לאזור זיכרון שמוגדר מבוזר אז המערכת תביא את ה-page מהרשת.
הרעיון הוא לעשות משהו דומה למה ש-Ivy עושה (זה מתואר [במאמר](http://infolab.stanford.edu/pub/cstr/reports/csl/tr/95/685/CSL-TR-95-685.pdf))
אולי צריך לבדוק איך smb ו-nfs עובדים  ואולי לחפש גם מימושים אחרים של דברים כאלה.


לבדוק איך vscode מתעדכן בזמן אמת על שינויים בקבצים

%%

https://diy.inria.fr/www/#

---

וירטואליזציה (vmm) - לבדוק על SSDT וגם על EPT

---

רפואה מרחוק 035304040

---

https://github.com/torvalds/linux/blob/master/tools/memory-model/linux-kernel.cat

https://github.com/torvalds/linux/blob/master/tools/memory-model/linux-kernel.bell


לחזור על `## Adjustments for ARM`


#code

לחזור על [בתיעוד שלי של memory-barriers.txt](obsidian://open?vault=Linux%20Kernel%20Docs%20v2&file=memory%20model%2FLINUX%20KERNEL%20MEMORY%20BARRIERS): %% חשוב !!! #article  %%
```
### מחסומי זיכרון מעבד
## מחסומי זיכרון מרומזים בקרנל
## השפעות מחסום ACQUIRING בין-מעבדים
### אינטראקציה בין-מעבד
### INTERRUPTS

774 + 1298 + 190 + 457 + 253 = 2972 מילים
```


- [ ] לבדוק לגבי תעתיק באנגלית של פורמליזציה [מהמאמר על המודל של arm](http://www0.cs.ucl.ac.uk/staff/j.alglave/papers/toplas21.pdf), וזה מופיע[ אצלי בחלק](obsidian://open?vault=Linux%20Kernel%20Docs%20v2&file=memory%20model%2Fnote) של `"# הגדרות תעתיק אנגלית"`  %% חשוב !!! #article  %%

- [ ] לבדוק לגבי קוד עם מחסומי זיכרון ב-Circular Buffers של הקרנל ([סיכום שלי](obsidian://open?vault=Linux%20Kernel%20Docs%20v2&file=other%2FCircular%20Buffers))
- [ ] לבדוק אם כדאי לעשות במאמר חלק על self-modifying-code 




---


- [ ] לבדוק אם thread-ים באותו core משתמשים באותו cache L1 ולבדוק אם הם אמורים להשתמש בפרוטוקול קוהרנטיות אחר מ-MOESI כי זה כל אלה פרוטוקולי cache והם צריכים לתקשר אפילו בלי cache.
- [ ] לבדוק אם רכיבים שהם תת-מערכת (למשל כמו thread-ים במעבד) שהם לא משתתפים בעצמם בפרוטוקול הקוהרנטיות הם דוגמה למקום שיכול להיות בו השפעת קצב התפשטות המידע (כי הפרוטוקול קוהרנטיות שם אחר)
- [ ] לבדוק מה הפרוטוקול קוהרנטיות של ppc
- [ ] לבדוק אם כדאי לחזור על החלק של סיפוק קריאה ב-[StrongModel](https://mirrors.edge.kernel.org/pub/linux/kernel/people/paulmck/LWNLinuxMM/StrongModel.html#Design%20of%20the%20Strong%20Model) בסעיף Processor-Local Ordering Requirements (נמצא אצלי [במאמר](obsidian://open?vault=Linux%20Kernel%20Docs%20v2&file=memory%20model%2Fnote)), וגם לבדוק אם החלק של סיפוק קריאה קשור לפרק [נספח O: אישור מוקדם בבקשות ביטול ועדכון](obsidian://open?vault=Linux%20Kernel%20Docs%20v2&file=memory%20model%2FMEMORY%20CONSISTENCY%20MODELS%20FOR%20SHARED-MEMORY%20MULTIPROCESSORS) (עם הדיאגרמות עם העיגולים)


- [ ] לבדוק אם ארכיטקטורות שמספקות multi copy atomic לא צריכות בכלל מחסומים, ארכיטקטורות שמספקות other multi copy atomic צריכות לספק מחסומים פנימיים למעבד (ללא הפצה) וארכיטקטורות שלא מספקות multi copy atomic בכלל צריכות מחסומים מתפשטים. ???

- [ ] לבדוק ב-ARMv8 מה הדומיין הברירת מחדל בפעולות תחזוקת cache כי אפשר להוסיף להוראות אפשרות להיות בדומיין inner או בכלל לא לציין דומיין. ולתקן בהתאם את [המאמר על תחזוקת cach e](obsidian://open?vault=Linux%20Kernel%20Docs%20v2&file=memory%20model%2FArticle%2FCache%2FCache%20maintenance)

- [ ] ללמוד לעומק על selinux
- [ ] ללמוד על RTOS בקרנל ובכללי
- [ ] ללמוד על cgroup ועל namespace-ים בכללי
- [ ] ללמוד על LXC לעומת Docker
- [ ] ללמוד לעומק על PREEMPT בקרנל וב-RTOS
- [ ] לבדוק על CONFIG_REFCOUNT_FULL
- [ ] לבדוק אם יש ספר שכדאי לקרוא ב-oreilly
- [ ] לנסות להתחיל לתרום קוד או לפתור באגים בקרנל
- [ ] ללמוד לעומק על poll ו-select
- [ ] ללמוד על inotify
- [ ] ללמוד על quota בקרנל
- [ ] ללמוד על ebpf
- [ ] ללמוד על crypto בקרנל ([קישור](https://docs.kernel.org/crypto/intro.html))


---


Arm
Atomic
Barriers
Buffers
Cache
Compiler
Models
Optimization techniques



- Arm:
    - [x] Domains.md
    - [x] Early Write Acknowledgment.md

- Atomic:
    - [x] Atomic.md <<<
    - [x] Exclusive.md <<<
    - [x] x86 Lock.md <<<

- Barriers:
    - [x] mb.md <<<
    - [x] Acquire Release.md <<<
    - [ ] AMBA ACE Barrier.md ?


- Buffers:
    - [x] Combined buffer.md <=
    - [x] Decoder.md
    - [x] Fetch.md <<<
    - [x] Invalidate queue.md <<<
    - [x] Line fill buffer.md
    - [x] Reorder buffer.md
    - [x] Store buffer.md <<<
    - [x] Uops.md <=


- Cache:

    - [x] Cache coherence.md <=
    - [x] Cache maintenance.md <=
    - [x] Cache.md
    - [x] Multi-copy atomicity.md <=
    - [x] Snoop & Directory.md <=

    - Coherence protocol:
		- [x] AMBA CHI. <=

		- [x] MOESI ?.md <=

- Compiler:
    - [x] Optimizations.md <<<

    - [x] GCC ?.md

- Models:
    - [x] Base Formal.md
    - [x] Dependency.md
    - [x] Herd7.md
    - [x] LKMM Code Examples.md
    - [x] LKMM.md
    - [x] Models.md
    - [x] Ordering.md

- Optimization techniques:
    - [x] Pipeline & Hazard.md <<<
    - [x] Register renaming.md <<<
    - [x] Speculation.md <<<

- [x] Causal & Physics.md <=



---

- [ ] במאמר של AMBA CHI לחבר את קטע על `WriteUniqueZero` להוראה `ZVA` ב-ARM


- [ ] לבדוק בכל מקום שאני מתייחס לטרנזקציית AMBA CHI שההמרה בין MOESI ל-CHI באמת נכונה (לבדוק לפי הטבלה table6 [ב-primer2020_2nd_edition](obsidian://open?vault=Linux%20Kernel%20Docs%20v2&file=memory%20model%2Fprimer2020_2nd_edition))





%% 
2700+ 3400 + 1600+ 4800 + 10000 +1800
%%


לעשות שהמאמר ל-digitalwhisper יהיה סיפור "רקום" סביב המאמרים שקיימים, כלומר לספר סיפור שהוא יהיה מסע כדי להבין איך ולמה קוד להדגמה (אולי הקוד של ה-buffer המעגלי) נראה ככה, וכל פרק יגע לא רק בחומר שקשור ישירות לסיפור אלה לכל הנושא, למשל אם בקוד יש רק מחסום smp_store_release אני עדיין אספר על כל סוגי המחסומים וההתנהגיות שלהם.
ואולי צריך לעשות בתחילת הסיפור חלק מנותק מהסיפור כי אני לא בטוח שאני אוכל להכניס בצורה כזאת נושאים כמו AMBA CHI 




---

```c

WRITE_ONCE(X, 1)
						READ_ONCE(X)
```


- Compiler:
    - [ ] Optimizations.md

- Optimization techniques:
    - [ ] Pipeline
    
Pipeline & Hazard.md
Register renaming.md

- Buffers:
    - [ ] Fetch.md
    - [ ] Store buffer.md
    - [ ] Invalidate queue.md
	- [ ] Domains.md

Early Write Acknowledgment.md
 Combined buffer.md
 Uops.md
 Decoder.md
Reorder buffer.md

- [ ] Speculation.md

- [ ] Ordering.md

- Cache:
    - [ ] Cache.md
    - [ ] Cache coherence.md
    - [ ] Snoop & Directory.md
    - [ ] Cache maintenance.md
    - [ ] Multi-copy atomicity.md

- Coherence protocol:
	- [ ] AMBA CHI.md
	- [ ] MOESI ?.md
	- [ ] Causal & Physics.md

- Barriers:
    - [ ] mb.md
    - [ ] Acquire Release.md

- Atomic:
    - [ ] Atomic.md
    - [ ] Exclusive.md
    - [ ] x86 Lock.md

- Models:
    - [ ] Models.md
    - [ ] Herd7.md
    - [ ] Base Formal.md
    - [ ] Dependency.md
    - [ ] LKMM.md
    - [ ] LKMM Code Examples.md



%% 
GCC ?.md
%%

https://docusaurus.io/docs/markdown-features/math-equations



```
npm run swizzle @docusaurus/theme-classic prism-include-languages

npm run swizzle @docusaurus/theme-search-algolia SearchBar
```


https://github.com/PrismJS/prism/blob/master/components/prism-ocaml.js%% 


---

### coder

add:

`themes/hugo-coder/assets/scss/css/normalize.css`
```css
.highlight {
	direction: ltr;
}
```


add:
`themes/hugo-coder/assets/scss/css/normalize.css`
```css
p code {
  direction: ltr;
  unicode-bidi: embed;
}
```


delete:
`themes/hugo-coder/assets/scss/_content.scss`
```css
p {
	text-align: justify;
}
```


delete:

`themes/hugo-coder/layouts/_default/baseof.html`
```html

before:
<body class="preload-transitions {{ $csClass }}{{ if .Site.Params.rtl }} rtl{{ end }}">

{{ partial "float" . }}

after:
<body class="preload-transitions {{ $csClass }}">
```

```html
before:
<html lang="{{ .Site.Language.Lang }}">

after:
<html lang="{{ site.Language }}" dir="rtl">


`{{ .Language.LanguageDirection }} `
```

add:
`themes/hugo-coder/layouts/partials/posts/math.html`
```html
<style>
.katex {
	direction: ltr;
	display: inline-flex;
	flex-direction: row-reverse;
	#unicode-bidi: embed;
}
</style>
```




add:
`themes/hugo-coder/layouts/posts/single.html`
```html
{{ partial "sources.html" . }}

Before:
<footer>
	{{ partial "posts/series.html" . }}
	{{ partial "posts/disqus.html" . }}
	{{ partial "posts/commento.html" . }}
	{{ partial "posts/utterances.html" . }}
	{{ partial "posts/giscus.html" . }}
	{{ partial "posts/mastodon.html" . }}
	{{ partial "posts/telegram.html" . }}
	{{ partial "posts/cusdis.html" . }}
</footer>

After:
<footer>
	{{ partial "sources.html" . }}
	{{ partial "posts/series.html" . }}
	{{ partial "posts/disqus.html" . }}
	{{ partial "posts/commento.html" . }}
	{{ partial "posts/utterances.html" . }}
	{{ partial "posts/giscus.html" . }}
	{{ partial "posts/mastodon.html" . }}
	{{ partial "posts/telegram.html" . }}
	{{ partial "posts/cusdis.html" . }}
</footer>
```

add: (create file)
`themes/hugo-coder/layouts/partials/sources.html`
```html
{{ if .Params.Sources }}
  <h3 dir="{{ .Language.LanguageDirection }}">
    {{ i18n "sources.sources" | default "Sources" }}
  </h3>
  <ul dir="ltr">
  {{ range .Params.Sources }}
    <li>
      <a href="{{ .}}">{{ . }}</a>
    </li>
  {{ end }}
{{ end }}
```


add:
`themes/hugo-coder/i18n/he.toml`
```toml
[sources]
sources = "מקורות"
```

add:
`themes/hugo-coder/assets/scss/_navigation.scss`
```css
float: left;

Before:
.navigation-title {
	letter-spacing: 0.1rem;
	text-transform: uppercase;
}

After:
.navigation-title {
	letter-spacing: 0.1rem;
	text-transform: uppercase;
	float: left;
}
```


add:
`themes/hugo-coder/layouts/posts/single.html`

```html
<span class="reading-time">
<i class="fa-solid fa-newspaper" aria-hidden="true"></i>
	{{ i18n "word_count.words" . }}
</span>

```

add:
`themes/hugo-coder/i18n/he.toml`
```toml
[word_count]
words = "{{ .WordCount }} מילים"
```


add:
`themes/hugo-coder/i18n/en.toml`
```toml
[sources]
sources = "sources"

[word_count]
words = "{{ .WordCount }} words"
```

delete:
`themes/hugo-coder/layouts/posts/single.html`
```html
<span class="reading-time">
	<i class="fa-solid fa-clock" aria-hidden="true"></i>
	{{ i18n "reading_time" .ReadingTime }}
</span>
```


delete:
`themes/hugo-coder/assets/scss/_base.scss`
```css
display: inline-block;

Before:
code {
	display: inline-block;
	background-color: inherit;
	color: inherit;
}

After:
code {
	background-color: inherit;
	color: inherit;
}
```

delete:
`themes/hugo-coder/layouts/partials/home.html`
```html
{{ partialCached "home/avatar.html" . }}
```

add: (create file)

`layouts/_default/_markup/render-image.html`
```html
{{- $pageDir := urlize .Page.Path -}}
{{- $imageName := printf "%s" .Destination -}}
{{- $imagePath := printf "%s/%s" $pageDir $imageName -}}

{{- if .IsBlock -}}
  <figure>
    <img src="{{ $imagePath | safeURL }}"
      {{- with .PlainText }} alt="{{ . }}"{{ end -}}
        class="dark-image"
    >
    {{- with .Title }}<figcaption>{{ . }}</figcaption>{{ end -}}
  </figure>
{{- else -}}
  <img src="{{ $imagePath | safeURL}}"
    {{- with .PlainText }} alt="{{ . }}"{{ end -}}
    {{- with .Title }} title="{{ . }}"{{ end -}}
    class="dark-image"
  >
{{- end -}}

<style>
  .dark-image {
    background-color: white;
  }
</style>
```

---

```
font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;
```

----


```css
p code {
  direction: ltr;
  display: inline-flex;
  flex-direction: row-reverse; 
}
```



```sh
python3 "/Users/michael/Desktop/fix md scripts/fix_md_to_post.py" -d "/Users/michael/Desktop/smichaelshal-web/a/test-web/content/posts" -i "/Users/michael/Documents/Linux Kernel Docs v2"
```

- [x] לתקן את החלק של המחיקת תגים בסקריפט במקרה של תג עם סלש כמו: #litmus/MP 


```html
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "316bf5f2576c4cb68b54c0b2a91cb739"}'></script><!-- End Cloudflare Web Analytics -->
```



```css
table {
	margin-left: auto;  
	margin-right: auto;
}
```