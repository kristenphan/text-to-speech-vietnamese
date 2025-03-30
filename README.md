# Text-to-speech Vietnamese
Creating a Vietnamese audio book from an English PDF book.

## How to run
```shell
# 1. Open Docker Desktop

# 2. Build and run text-to-speec container
# See: https://github.com/phatjkk/vits-tts-vietnamese/blob/main/README.md
cd vits_tts_vietnamese
docker build  ./ -f .Dockerfile -t vits-tts-vi:v1.0
docker run -d -p 5004:8888 vits-tts-vi:v1.0

# 3. Run main.py to convert English ebook to Viet ebook and Viet audio book
cd text-to-speech-vietnamese
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# In main.py: Replace {api-key} with key to call Google Cloud Translation API
python3 main.py
```

## Resources
- Viet tech-to-speed: https://github.com/phatjkk/vits-tts-vietnamese/blob/main/README.md
- Eng-Viet translation: [Google Cloud Translation API](https://cloud.google.com/translate?utm_source=google&utm_medium=cpc&utm_campaign=emea-nl-all-en-dr-skws-all-all-trial-e-gcp-1707574&utm_content=text-ad-none-any-dev_c-cre_574628516095-adgp_Hybrid+%7C+SKWS+-+EXA+%7C+Txt+-+AI+And+Machine+Learning+-+Translation+AI+-+v1-kwid_43700067787181231-kwd-30693959751-userloc_9065081&utm_term=kw_translate+api-net_g-plac_&&gad_source=1&gclid=Cj0KCQjw16O_BhDNARIsAC3i2GBP0Ae4oDsTxKN5ljkn7oTeHsUZVj4agmNzCdJW8tHqenMBwpaAVbUaAgykEALw_wcB&gclsrc=aw.ds&hl=en)
- Viet book: https://docs.google.com/document/d/1OaZFrgtk6GSpMbkUTZ7Q4N2ET6REzoNx/edit?