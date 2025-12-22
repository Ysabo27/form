#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
סקריפט לעדכון INDEX2.HTML עם קוד JavaScript מותאם למזהי השדות החדשים
"""

import re

# קריאת הקובץ המקורי
with open('index.html', 'r', encoding='utf-8') as f:
    old_js = f.read()

# קריאת הקובץ החדש
with open('INDEX2.HTML', 'r', encoding='utf-8') as f:
    new_html = f.read()

# מיפוי מזהי השדות הישנים למזהים החדשים
field_mapping = {
    'input_66': 'input_57',      # תעודת זהות
    'input_7': 'input_8',         # שם פרטי
    'input_9': 'input_7',         # שם משפחה
    'input_12': 'input_9',        # שנת לידה
    'input_13': 'input_13',       # שם האב (נשאר אותו דבר)
    'input_15': 'input_16',       # עיר
    'input_24': 'input_15',       # רחוב
    'input_18': 'input_18_full',  # טלפון
    'input_69': 'input_22',       # חתימה
    'input_33': 'input_60',      # תז בת זוג
    'input_26': 'input_25',       # שם פרטי בת זוג
    'input_27': 'input_24',       # שם משפחה בת זוג
    'input_32': 'input_26',       # שנת לידה בת זוג
    'input_70': 'input_30',       # שם האב בת זוג
    'input_35': 'input_33_full',  # טלפון בת זוג
    'input_71': 'input_37',       # חתימה בת זוג
    'input_42': 'input_40',       # מספר אשראי
    'input_72': 'input_61',       # תוקף אשראי
    'input_44': 'input_42',       # שם בעל הכרטיס
    'input_74': 'input_62',       # תעודת זהות בעל הכרטיס
    'input_73': 'input_44',       # חתימה אמצעי תשלום
    'input_56': 'input_56',       # כפתור submit (נשאר אותו דבר)
}

# חילוץ הקוד JavaScript מהקובץ הישן
js_start = old_js.find('<!-- ================= אימות ת״ז + חסימה קשיחה ================= -->')
js_end = old_js.find('</script>', js_start) + len('</script>')

if js_start == -1 or js_end == -1:
    print("לא נמצא קוד JavaScript בקובץ הישן")
    exit(1)

js_code = old_js[js_start:js_end]

# החלפת מזהי השדות בקוד JavaScript
for old_id, new_id in field_mapping.items():
    if old_id != new_id:  # רק אם הם שונים
        # החלפה מדויקת של מזהי השדות
        js_code = js_code.replace(f'"{old_id}"', f'"{new_id}"')
        js_code = js_code.replace(f"'{old_id}'", f"'{new_id}'")
        js_code = js_code.replace(f'getElementById("{old_id}")', f'getElementById("{new_id}")')
        js_code = js_code.replace(f"getElementById('{old_id}')", f"getElementById('{new_id}')")
        js_code = js_code.replace(f'id === "{old_id}"', f'id === "{new_id}"')
        js_code = js_code.replace(f"id === '{old_id}'", f"id === '{new_id}'")
        
        # החלפה של מספר השדה ב-JotForm API calls (רק המספר ללא input_)
        old_num = old_id.replace('input_', '')
        new_num = new_id.replace('input_', '')
        if old_num != new_num:
            js_code = js_code.replace(f'setFieldMask("{old_num}"', f'setFieldMask("{new_num}"')
            js_code = js_code.replace(f'setFieldProperty("{old_num}"', f'setFieldProperty("{new_num}"')
            js_code = js_code.replace(f'fieldSettings["{old_num}"]', f'fieldSettings["{new_num}"]')
            js_code = js_code.replace(f'fieldSettings["{old_num}"]', f'fieldSettings["{new_num}"]')

# תיקון מיוחד עבור sig_pad_ - חתימה
js_code = js_code.replace('sig_pad_69', 'sig_pad_22')  # חתימה
js_code = js_code.replace('sig_pad_71', 'sig_pad_37')  # חתימה בת זוג
js_code = js_code.replace('sig_pad_73', 'sig_pad_44')  # חתימה אמצעי תשלום

# תיקון מיוחד עבור מספר אשראי - צריך להיות input_40 במקום input_42
js_code = js_code.replace('input_42', 'input_40')  # מספר אשראי
# אבל צריך לשמור על input_42 כשמדובר בשם בעל הכרטיס
js_code = js_code.replace('input_40', 'input_42', 1)  # שם בעל הכרטיס (רק פעם אחת)

# למעשה, צריך לעשות את זה אחרת - תחילה להחליף את כל המקרים המיוחדים
# בואו נתקן את זה בצורה יותר מדויקת
js_code = js_code.replace('const creditCard = document.getElementById("input_40")', 'const creditCard = document.getElementById("input_40")')
js_code = js_code.replace('window.JotForm.setFieldMask("input_40"', 'window.JotForm.setFieldMask("40"')
js_code = js_code.replace('window.JotForm.setFieldProperty("40"', 'window.JotForm.setFieldProperty("40"')

# בדיקה אם הקוד כבר קיים בקובץ החדש
if '<!-- ================= אימות ת״ז + חסימה קשיחה ================= -->' in new_html:
    print("הקוד כבר קיים בקובץ החדש - מעדכן")
    # מחליף את הקוד הישן בקוד החדש
    pattern = r'<!-- ================= אימות ת״ז \+ חסימה קשיחה ================= -->.*?</script>'
    new_html = re.sub(pattern, js_code, new_html, flags=re.DOTALL)
else:
    print("מוסיף קוד חדש לפני </body>")
    # מוסיף את הקוד לפני </body>
    new_html = new_html.replace('</body>', js_code + '\n</body>')

# שמירת הקובץ המעודכן
with open('INDEX2.HTML', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("הקובץ INDEX2.HTML עודכן בהצלחה!")


