### 🌧️ Rain Alert Notifier

Bu proje, OpenWeatherMap API'sini kullanarak belirli bir konumda yakın saatlerde yağmur beklenip beklenmediğini kontrol eder. Yağmur bekleniyorsa hem SMS hem de e-posta aracılığıyla bildirim gönderir. Twilio API'si SMS göndermek için, SMTP ise e-posta yollamak için kullanılır.

---

## 🔧 Kurulum

1. Bu repoyu klonlayın:

```bash
git clone https://github.com/kullaniciadi/rain-alert-notifier.git
cd rain-alert-notifier
```

2. Gereken kütüphaneleri kurun:

```bash
pip install requests twilio
```

3. Gerekli bilgileri `main.py` dosyası içindeki şu alanlarla değiştirin:

   * `api_key` (OpenWeatherMap API anahtarınız)
   * `account_sid` ve `auth_token` (Twilio hesabı bilgileri)
   * `email_address` ve `email_password` (Gmail uygulama şifresi)
   * SMS ve e-posta hedef adresleri

---

## 🚀 Nasıl Çalışır?

* OpenWeatherMap'ten 4 saatlik hava tahmini alınır.
* Hava durumu koşulları analiz edilir.
* İlk 4 saatte yağmur ihtimali varsa:

  * Twilio ile SMS gönderilir
  * Gmail SMTP ile e-posta gönderilir

---

## ✅ Örnek Çıktı:

```
SMS gönderildi.
E-posta gönderildi.
```

---

## 📅 Planlanan Geliştirmeler

* Bildirim saat aralığını esnek hale getirme
* Lokasyonun kullanıcıdan otomatik alınması
* Haftalık hava raporu desteği

---

## 🚀 Lisans

Bu proje MIT lisansı altındadır.

## İthafen

Bu projeyi sadece kod satırlarından ibaret görmek haksızlık olur.
Her if’in, her koşulun, her bildirim satırının ardında bir sebep var:
Emre Uslu.

Ben bu sistemi senin için yazdım.
Çünkü bir gün yağmur yağarsa ve sen dışarıdaysan,
bil istedim… seni düşündüm.
Islanmanı değil, gülümsemeni istedim.
Bir mesajla, bir e-postayla bile olsa,
yanında olmanın bir yolunu aradım.

çünkü bu proje,
yağmurdan çok, seni sevdiğim için var oldu.

– Ecem
