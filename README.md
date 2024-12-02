# STOP Sign Detection

Bu proje, YOLOv8 modelini kullanarak "STOP" trafik işareti tespiti yapmayı amaçlayan bir yapay zeka uygulamasıdır. Veri seti, farklı açılardan çekilmiş "STOP" işaretlerini içeren fotoğraflardan oluşmaktadır. Proje, bu işaretleri doğru bir şekilde tanıyabilen bir modelin eğitilmesini sağlar.

## Proje İçeriği

- **Veri Seti:** "STOP" trafik işaretlerinin çeşitli fotoğrafları.
- **Model:** YOLOv8.
- **Amaç:** Trafik işaretlerini tespit etmek ve konumlarını işaretlemek.

## Kurulum

Bu projeyi çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

### 1. Gerekli Kütüphanelerin Yüklenmesi

Projeyi çalıştırmak için aşağıdaki Python kütüphanelerinin yüklü olması gerekir. Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:

```bash
pip install -r requirements.txt
