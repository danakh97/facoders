'''
 اكتبي لعبة تطبع اسم اللعبة أولا
Numbers from 1 to 10
 ثم تطلب من المستخدم أن يحزر الرقم
"Guess the number: "

 إذا المستخدم لم يدخل الرقم الصحيح ستبقى اللعبة تسأله للأبد، إذا قام بإدخال الرقم الصحيح، يظهر للمستخدم:
"Great! You did it!"

 لا تنسي أن تقومي بتخزين رقم من اختيارك ليكون هو الرقم الصحيح وتخزينه في متغير.
 الرقم يجب أن يكون بين 1 و10

'''

print ('Numbers from 1 to 10')
x = 4
while True:
    num = int(input('Guess the number: '))
    if num >= 1 and num <= 10:
        if num == x:
            print('Great! You did it!')
            break
        else:
            continue
    else:
        continue
