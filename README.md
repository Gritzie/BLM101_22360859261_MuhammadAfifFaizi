BLM101 Dönem Projesi

Ad Soyad: Muhammad Afif Faizi
Öğrenci Numarası: 22360859261
Bölüm: Bilgisayar Mühendisliği

Proje Konusu
  RLE Sıkıştırma Algoritması

Açıklama
Bu projeyi, metinleri sıkıştırmak için Run Length Encoding (RLE) yöntemini uygular

Main Functions
1. rle_encode(text) 
   Converts a string into RLE format
2. rle_decode(text)  
   Converts RLE text back to original string
3. compression_ratio(original, compressed)  
   Calculates the compression ratio in percentage

Logic
1. rle_encode ardışık karakterleri sayar ve "sayı + karakter" formatında yeni bir string oluşturur
2. rle_decode sayıları okuyarak ilgili karakteri tekrar ederek orijinal metni oluşturur
3. compression_ratio orijinal ve sıkıştırılmış metin uzunluklarını karşılaştırarak oranı hesaplar
