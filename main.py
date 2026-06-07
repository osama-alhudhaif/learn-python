# تحويل بين وحدات التخزين

# تحويل بين وحدات التخزين

# كل وحدة كم bit تساوي (الأساس = bit)
units = {
    "bit": 1,
    "byte": 8,
    "kb": 8 * 1024,
    "mb": 8 * 1024 ** 2,
    "gb": 8 * 1024 ** 3,
    "tb": 8 * 1024 ** 4,
    "pb": 8 * 1024 ** 5,
    "eb": 8 * 1024 ** 6,
    "zb": 8 * 1024 ** 7,
    "yb": 8 * 1024 ** 8,
}

from_unit = input("من أي وحدة؟ (bit, byte, kb, mb, gb, tb, pb, eb, zb, yb): ")
to_unit = input("إلى أي وحدة؟ (bit, byte, kb, mb, gb, tb, pb, eb, zb, yb): ")
value = float(input("ادخل القيمة المراد تحويلها: "))

# 1) حوّل للأساس (bit)
value_in_bits = value * units[from_unit]
# 2) من الأساس للوحدة الهدف
result = value_in_bits / units[to_unit]

print(f"القيمة المدخلة: {value} {from_unit}")
print(f"القيمة المحوّلة: {result} {to_unit}")