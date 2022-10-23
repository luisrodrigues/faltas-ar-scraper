# faltas-ar-scraper
Web scraping project to obtain and summarize portuguese national parliament attendance numbers.

## Requirements

  * Python 3.9+
  * Installed packages (see `requirements.txt`)
  * .env file with configs (see `.env-example`)

## Sample Execution & Output

```
python main.py
```

The following messages will be displayed:

```
rodrilui$ python main.py
Checking the absence list...
Page exists.
Not working with files. Sending BID: 299295.
Scraping new data...
Page exists.
Producing social media post...
🗓️21/10/2022
📝Reunião Plenária Ordinária
➡️Nº de faltas por grupo parlamentar:
PS ❌ : 11/120 (9%)
PSD ❌ : 8/77 (10%)
IL ❌ : 2/8 (25%)
CH ❌ : 1/12 (8%)
PCP ❌ : 1/6 (17%)
BE ❌ : 1/5 (20%)
PAN ✅ : 0/1 (0%)
L ✅ : 0/1 (0%)
🔗https://www.parlamento.pt/DeputadoGP/Paginas/DetalheReuniaoPlenaria.aspx?BID=299295
Not posting on Twitter...
```
---
### Heads Up
* After the script runs, the "post" string is copied to the clipboard for ease of use.
* Some parts of the code can be run separately
* Please check `settings.py` to change script behaviour
* When working with files, a `data` folder will be created to save scraped data and avoid re-connecting

### Roadmap
* Twitter postage is not yet automated
* The script should be turned into a function and triggered via cron job.