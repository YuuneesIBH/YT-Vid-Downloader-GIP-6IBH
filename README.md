# Pytube Backup Tool – GIP 

Een educatieve toepassing ontwikkeld als onderdeel van het GIP project (Geïntegreerde Proef 6de middelbaar) die demonstreert hoe de `pytube`-bibliotheek gebruikt kan worden voor het downloaden van YouTube-video's.

## 📚 Over dit project

Dit project is gemaakt als praktische demonstratie voor mijn geïntegreerde proef in het zesde middelbaar. Het toont de implementatie van Python-bibliotheken voor mediaverwerkingstaken en illustreert concepten zoals API-gebruik, bestandsbeheer en command-line interfaces.

## ⚠️ Belangrijke disclaimer

**Deze software is uitsluitend bedoeld voor educatief en experimenteel gebruik.**

- Niet geschikt voor commerciële of grootschalige toepassing
- De ontwikkelaar is niet verantwoordelijk voor misbruik van deze tool
- Respecteer altijd de gebruiksvoorwaarden van YouTube en geldende copyrightwetgeving
- Gebruik alleen voor content waarvoor je toestemming hebt of die onder fair use valt

## ✨ Functionaliteiten

- Download individuele YouTube-video's
- Ondersteuning voor het downloaden van complete playlists
- Gebruiksvriendelijke command-line interface (CLI)
- Automatische organisatie van gedownloade bestanden in lokale mapstructuur
- Kwaliteitsselectie voor video-downloads

## 🛠️ Installatie

### Vereisten
- Python 3.7 of hoger
- Internetverbinding

### Stappen
1. Clone of download dit project naar je lokale machine
2. Installeer de benodigde dependencies:
```bash
pip install pytube
```

## 🚀 Gebruik

### Basis gebruik
```bash
python main.py
```

### Video downloaden
1. Start de applicatie
2. Voer de YouTube-URL in wanneer daarom gevraagd wordt
3. Selecteer de gewenste kwaliteit
4. Wacht tot de download voltooid is

### Playlist downloaden
1. Voer een playlist-URL in plaats van een individuele video-URL in
2. De tool zal automatisch alle video's in de playlist detecteren en downloaden

## 📁 Projectstructuur

```
pytube-backup-tool/
├── main.py              # Hoofdapplicatie
├── README.md            # Dit bestand
├── requirements.txt     # Python dependencies
└── downloads/           # Map voor gedownloade bestanden
```

## 🔧 Technische details

Dit project maakt gebruik van:
- **pytube**: Python-bibliotheek voor YouTube-video downloads
- **Command-line interface**: Voor gebruikersinteractie
- **Bestandsbeheer**: Georganiseerde opslag van gedownloade content

## 📖 Educatieve doeleinden

Dit project demonstreert:
- Gebruik van externe Python-bibliotheken
- API-integratie met online platforms
- Bestandsverwerking en -organisatie
- Command-line applicatieontwikkeling
- Foutafhandeling en gebruikerservaring

## 🤝 Bijdragen

Dit is een educatief project ontwikkeld voor schooldoeleinden. Suggesties en feedback zijn welkom voor leerdoeleinden.

## 📝 Licentie

Dit project is ontwikkeld voor educatieve doeleinden als onderdeel van een schoolproject. Gebruik op eigen risico en respecteer alle geldende wetten en gebruiksvoorwaarden.

## 👨‍🎓 Over de ontwikkelaar

Ontwikkeld door een leerling van het zesde middelbaar als onderdeel van de Geïntegreerde Proef 2 (GIP 2), met focus op praktische toepassing van programmeertechnieken en bibliotheekintegratie.

---

**Let op**: Dit project is puur educatief. Zorg ervoor dat je gebruik in overeenstemming is met YouTube's gebruiksvoorwaarden en lokale wetgeving betreffende auteursrechten.
