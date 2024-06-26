# 🎥 Çoklu İstemci Video İşleme Sunucusu ve İstemci 🖥️

Bu proje, Python kullanarak çoklu istemci video işleme sunucusu ve istemcisini oluşturur. Sunucu, istemcilerden video akışı alır, işler (örneğin, görüntüyü döndürme) ve işlenmiş görüntüyü geri gönderir.

![image](https://github.com/bogac124/G-r-nt-aktar-m-/assets/69991160/ded374d7-dceb-475c-b339-33f5a793ab15)

## 📄 İçindekiler

- [Nasıl Çalışır?](#-nasıl-çalışır)
- [Kullanım](#-kullanım)
- [Katılım](#-katılım)

## 🚀 Nasıl Çalışır?

- **Sunucu**: `server.py` dosyası, video işleme sunucusunu temsil eder. Sunucu, belirli bir port üzerinden istemci bağlantılarını dinler. Her bağlantı için yeni bir iş parçacığı oluşturur ve video akışlarını işler.

- **İstemci**: `client.py` dosyası, video işleme istemcisini temsil eder. İstemci, video akışını sunucuya gönderir ve işlenmiş video akışını alır.

## 📝 Kullanım

1. **Sunucuyu Başlatma**:
    - Sunucuyu başlatmak için terminal veya komut istemcisinde `python server.py` komutunu çalıştırın.
    - Sunucu, belirtilen port üzerinden istemci bağlantılarını dinlemeye başlar.

2. **İstemciyi Başlatma**:
    - İstemciyi başlatmak için ayrı bir terminal veya komut istemcisinde `python client.py` komutunu çalıştırın.
    - İstemci, sunucuya bağlanır ve kameradan video akışını alarak sunucuya gönderir.
    - Sunucu, aldığı video akışını işler (örneğin, görüntüyü yatay olarak çevirir) ve işlenmiş videoyu geri gönderir.
    - İstemci, işlenmiş videoyu alır ve ekranda görüntüler.

## 🤝 Katılım

- Bu depoyu çatallayın (fork) ve geliştirmelerinizi yapın.
- Yeni özellikler eklemek veya hataları düzeltmek için Pull Talepler (Pull Requests) gönderin.
- Hataları bildirmek veya önerilerde bulunmak için konu (issue) açın.
