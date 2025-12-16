# הוראות לעדכון הטופס החדש

## שינויים נדרשים בקוד החדש שנתת:

### 1. עדכון תגית HTML
בשורה הראשונה, שנה מ:
```html
<html lang="he"  class="supernova ">
```
ל:
```html
<html lang="he" dir="rtl" class="supernova ">
```

### 2. עדכון תגית body
חפש את `<body>` ושנה ל:
```html
<body dir="rtl">
```

### 3. הוספת CSS מותאם אישית
אחרי השורה:
```html
<style type="text/css">@media print{...}</style>
```

הוסף את הקוד הבא:
```html
<style type="text/css" id="form-designer-style">
    /* Injected CSS Code */
    .form-label.form-label-auto {
        display: inline-block;
        float: right;
        text-align: right;
    }

    /* RTL Support */
    html[dir="rtl"],
    html[dir="rtl"] body,
    html[dir="rtl"] .form-all,
    html[dir="rtl"] .form-line {
        direction: rtl;
    }
    
    html[dir="rtl"] .form-label,
    html[dir="rtl"] .form-label.form-label-auto {
        float: right;
        text-align: right;
        margin-left: 10px;
        margin-right: 0;
    }
    
    html[dir="rtl"] .form-input {
        float: right;
        text-align: right;
    }
    
    html[dir="rtl"] input[type="text"],
    html[dir="rtl"] input[type="number"],
    html[dir="rtl"] input[type="email"],
    html[dir="rtl"] input[type="tel"] {
        text-align: right;
        direction: rtl;
    }
    
    html[dir="rtl"] .form-buttons-wrapper {
        text-align: center;
    }
    
    html[dir="rtl"] #form-status-message {
        text-align: center;
        direction: rtl;
    }
    
    /* סימון שדות עם שגיאה */
    .field-error {
        border: 2px solid #d32f2f !important;
        background-color: #ffebee !important;
        box-shadow: 0 0 5px rgba(211, 47, 47, 0.3) !important;
    }
    
    .field-error:focus {
        outline: none;
        border-color: #d32f2f !important;
        box-shadow: 0 0 8px rgba(211, 47, 47, 0.5) !important;
    }
    
    /* סימון חתימה עם שגיאה */
    .signature-error {
        border: 2px solid #d32f2f !important;
        background-color: #ffebee !important;
    }
    
    /* מסתיר את הנקודה בשדה מספר אשראי */
    #input_40 {
        color: #000;
    }
</style>
```

### 4. הוספת JavaScript לאימות שדות
אחרי תגית `</form>` (לפני `</body>`), הוסף את כל הקוד מ-index.html שורות 816-2682, אבל עם התאמות למזהי השדות החדשים:

#### התאמות מזהי השדות:
- במקום `input_66` → `input_57` (תעודת זהות)
- במקום `input_7` → `input_8` (שם פרטי)
- במקום `input_9` → `input_7` (שם משפחה)
- במקום `input_12` → `input_9` (שנת לידה)
- במקום `input_15` → `input_16` (עיר)
- במקום `input_24` → `input_15` (רחוב)
- במקום `input_18` → `input_18_full` (טלפון) - אבל צריך לבדוק שזה השדה הנכון
- במקום `input_69` → `input_22` (חתימה)
- במקום `input_72` → `input_61` (תוקף אשראי)
- במקום `input_44` → `input_42` (שם בעל הכרטיס)
- במקום `input_74` → `input_62` (תעודת זהות בעל הכרטיס)
- במקום `input_73` → `input_44` (חתימה אמצעי תשלום)
- במקום `input_42` → `input_40` (מספר אשראי)
- במקום `input_33` → `input_60` (תז בת/בן זוג)
- במקום `input_26` → `input_25` (שם פרטי בת/בן זוג)
- במקום `input_27` → `input_24` (שם משפחה בת/בן זוג)
- במקום `input_32` → `input_26` (שנת לידה בת/בן זוג)
- במקום `input_35` → `input_33_full` (טלפון בת/בן זוג)
- במקום `input_71` → `input_37` (חתימה בת/בן זוג)
- במקום `input_70` → `input_30` (שם האב בת/בן זוג)

### 5. עדכון קוד ביטול מיסוך מספר אשראי
בקוד ה-JavaScript, כל מקום שמתייחס ל-`input_42` (מספר אשראי) צריך להיות `input_40`, וכל מקום שמתייחס ל-`"42"` (ID של השדה) צריך להיות `"40"`.

### 6. הערות חשובות:
- בטופס החדש שדה הטלפון הוא `input_18_full` ולא `input_18` - צריך לבדוק את זה בקוד
- בטופס החדש שדה הטלפון של בת/בן זוג הוא `input_33_full` ולא `input_33`
- צריך להתאים את כל הפונקציות לאימות שדות למזהי השדות החדשים

## קובץ הקוד המלא
אני יכול ליצור את הקובץ המלא המעודכן אם תרצה - פשוט תגיד לי ואני אכין אותו בדיוק עם כל השינויים האלה.

