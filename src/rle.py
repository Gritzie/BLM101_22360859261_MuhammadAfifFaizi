def rle_encode(text):
    if text == "":
        return ""

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += str(count) + text[i - 1]
            count = 1

    result += str(count) + text[-1]
    return result


def rle_decode(text):
    result = ""
    number = ""

    for ch in text:
        if ch.isdigit():
            number += ch
        else:
            result += ch * int(number)
            number = ""

    return result


def compression_ratio(original, compressed):
    if len(original) == 0:
        return 0

    return (1 - len(compressed) / len(original)) * 100


print("RLE Compressor")

data = input("Masukkan teks: ")

encoded = rle_encode(data)
decoded = rle_decode(encoded)
ratio = compression_ratio(data, encoded)

print("Encoding Result:", encoded)
print("Decoding Result:", decoded)
print("Kompresion Result: {:.2f}%".format(ratio))
