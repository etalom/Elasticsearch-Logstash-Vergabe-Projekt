# Elasticsearch-Logstash-Vergabe-Projekt
### Elasticsearch • Logstash • Kibana • Jupyter Notebook

Dieses Repository enthält ein vollständiges Setup zur **Analyse von Vergaberechts‑Dokumenten** des Landes Rheinland‑Pfalz.  
Es kombiniert:

- **Elasticsearch** zur Volltextsuche  
- **Logstash** zur automatischen PDF‑Extraktion  
- **Kibana** für Dashboards & Visualisierungen  
- **Jupyter Notebooks** zur Auswertung und KI‑Vorverarbeitung  

Die Grundlage bilden die folgenden Originaldokumente (PDF):  
UVgO, VgV, GWB, VV Öffentliches Auftragswesen, VV Öffentliches Beschaffungswesen, Rundschreiben, LHO usw.  
(Die Inhalte wurden mit Logstash automatisch extrahiert und in das Feld `attachment.content` indexiert.) 

---

## 🚀 Funktionen

- Automatische **Extraktion von Text & Metadaten** aus PDF‑Rechtsdokumenten  
- Volltextsuche über `attachment.content`  
- Fertiges **Kibana‑Dashboard** (User‑Story‑orientiert)  
- Analyse & Matching in **Jupyter Notebook**  
- Vollständig dockerisiert (lokal lauffähig)  
- Grundlage für einen eigenen **Vergabe‑Chatbot** oder eine RLP‑Vergabe‑Wissensdatenbank

---

## 📦 Voraussetzungen

- Docker & Docker Compose  
- Git  
- PDF‑Dateien in `data/` (dieser Ordner wird nicht versioniert)

---

## 📁 Projektstruktur
