## 📞 Twilio AlarmServer / Alarm Server
🇩🇪 Notrufsystem für kleine und mittelständische Unternehmen | 🇬🇧 Emergency Alert System for SMEs

---

## 🔔 Projektbeschreibung (🇩🇪)

Ein schlanker, kostengünstiger Alarmserver für kleine und mittelständische Unternehmen, Vereine oder Organisationen.  
Ermöglicht automatisierte Notrufe per Anruf und SMS an vordefinierte Kontakte – ausgelöst durch einen Anruf bei Twilio oder eine API-Anfrage.



## 🔔 Project Description (🇬🇧)

A lightweight, cost-effective alarm server for small and medium-sized businesses, clubs, or organizations.  
Supports automated emergency notifications via call and SMS to predefined contacts – triggered by a Twilio call or an API request.

---

## ✅ Funktionen (🇩🇪)

- Reaktion auf eingehende Anrufe bei Twilio (automatischer Alarmversand)
- Manuelles Auslösen per API (HTTP POST)
- API antwortet zurück an Twilio
- Alarm per Anruf und SMS an mehrere Empfänger gleichzeitig
- Trennung von Kontakten und Code (Best Practice)



## ✅ Features (🇬🇧)

- Responds to incoming calls on Twilio (automated alert sending)
- Manual trigger via API (HTTP POST)
- API replies back to Twilio
- Alerts via call and SMS to multiple recipients simultaneously
- Separation of contacts (in text file) and logic (best practice)

---

## 📌 Twilio Flow Sample

![Logo](Twilio_Flow_Sample.png) "Twilio Flow Sample"

---

## 🚀 Installation & Setup

### 🇩🇪 Voraussetzungen / 🇬🇧 Requirements

- Python 3.x  
- Twilio-Konto mit aktivierter Telefonnummer / Twilio account with active number  
- Server mit offenem Port 8830 / Server with open port 8830

### 🖥️ Installation

```bash
git clone https://github.com/Twilio_AlarmServer/twilio-alarmserver.git
cd Twilio-AlarmServer
pip install -r requirements.txt

## 📞 Twilio Dokumentation

- [Twilio Studio Flow](https://www.twilio.com/docs/studio/)
