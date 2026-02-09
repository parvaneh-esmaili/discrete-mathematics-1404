# برنامه اي بنويسيد كه عدد صحيح و مثبت n را از ورودي گرفته
# سپس دو بردار عددي n تايي را دريافت كند
# و مشخص كند آيا بين آن‌ها ترتيب قاموسي (الفبايي) وجود دارد يا خير.

# گرفتن اندازه بردارها
n = int(input("meghdare n ra vared konid: "))

# گرفتن بردار اول
print("anasore بردار aval ra vared konid:")
A = list(map(int, input().split()))

# گرفتن بردار دوم
print("anasore بردار dovom ra vared konid:")
B = list(map(int, input().split()))

# بررسي ترتيب قاموسي
# مقايسه از چپ به راست
result = "mosavi"

for i in range(n):
    if A[i] < B[i]:
        result = "A < B"
        break
    elif A[i] > B[i]:
        result = "A > B"
        break

# چاپ نتيجه
if result == "A < B":
    print("بردار A dar tartib ghamoosi kochaktar az B ast.")
elif result == "A > B":
    print("بردار A dar tartib ghamoosi bozorgtar az B ast.")
else:
    print("دو بردار dar tartib ghamoosi barabar hastand.")
