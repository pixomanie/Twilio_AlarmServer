# Twilio_AlarmServer

# 📞 Twilio Alarmserver – Notrufsystem für kleine und mittelständische Unternehmen

## 🔔 Projektbeschreibung

Dieses Projekt ermöglicht es, automatisiert Notrufe per Anruf und SMS an definierte Kontaktpersonen zu senden – ausgelöst durch einen eingehenden Anruf bei Twilio oder eine API-Anfrage.  
Gedacht ist das Skript als einfacher, kostengünstiger Alarmserver für kleine bis mittelständische Unternehmen, Vereine oder andere Organisationen, die im Ernstfall schnell informieren müssen (z. B. Evakuierung, technische Störungen, Notfallereignisse).

Die Umsetzung erfolgt mit [Twilio](https://www.twilio.com/), einem Cloud-Kommunikationsdienstleister, über den sowohl Sprachanrufe als auch SMS realisiert werden.

---

## ✅ Funktionen

- Reaktion auf eingehende Anrufe (automatischer Alarmversand)
- Manuelles Auslösen des Alarms per API (HTTP POST)
- Versand von Alarmmeldungen per Anruf und SMS an mehrere Personen gleichzeitig
- Trennung von Kontakten (Textdatei) und Code (Best Practice)
- Webhook-ready (kompatibel mit Twilio-Konsole)

---
## 📞 Twilio Lösung über

- Twilio Studio Flow [Twilio](https://www.twilio.com/docs/studio/)

---

## 💡 Warum ist das Projekt sinnvoll?

In Firmen, Vereinen oder kleinen Organisationen fehlt oft ein einfaches, zentral steuerbares Notrufsystem.  
Mit diesem Projekt können Verantwortliche schnell und zuverlässig einen festgelegten Personenkreis alarmieren – ohne teure Infrastruktur oder komplexe Systeme.

---

## 🚀 Projekt starten

### Voraussetzungen

- Python 3.x
- Twilio-Konto mit aktivierter Telefonnummer
- Server mit Port 8830 (Firewall die eingestellt ist)

### Installation

```bash
git clone https://github.com/Twilio_AlarmServer/twilio-alarmserver.git
cd twilio-alarmserver
pip install -r requirements.txt
