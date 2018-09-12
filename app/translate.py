import json
import requests
from flask_babel import _
from flask import current_app


def translate(text, source_language, dest_language):
    # TODO: Pass API Key in with HTTP header.
    if 'YANDEX_API_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['YANDEX_API_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    # auth = {'Ocp-Apim-Subscription-Key': app.config['YANDEX_API_TRANSLATOR_KEY']}
    api_key = current_app.config['YANDEX_API_TRANSLATOR_KEY']
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?lang={}-{}&text={}'
                     '&key={}'.format(source_language, dest_language, text, api_key))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
