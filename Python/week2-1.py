'''
اكتبي برنامج يقوم بالطلب من المستخدم بإدخال رقم
 "Enter a number: "
 ثم يعيد له إن كان الرقم زوجي
 "Number is even"
 إذا كان فردي
 "Number is odd"
'''

num = int(input('Enter a number: '))
if num % 2 == 0 :
    print ('Number is even')
elif num % 2 != 0 :
    print ('Number is odd')
