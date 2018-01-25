import os
from pitman import Document


TEST_URLS = [
    'https://www.theguardian.com/world/2017/oct/01/dozens-injured-as-riot-police-storm-catalan-ref-polling-stations',
    'http://www.independent.co.uk/news/business/news/coca-cola-bottles-plastic-increase-coke-total-number-world-yearly-a7981561.html'
]
TEST_RESULTS = [
    {
        'language': 'en',
        'title': 'Catalan referendum: preliminary results show 90% in favour of independence | World news | The Guardian',
        'short_title': 'Catalan referendum: preliminary results show 90% in favour of independence'
    },
    {
        'language': 'en',
        'title': "Coca-Cola 'increases production of plastic bottles by a billion' | The Independent",
        'short_title': "Coca-Cola 'increases production of plastic bottles by a billion'"
    }
]


def test_document(capsys):
    with capsys.disabled():
        for i, test_url in enumerate(TEST_URLS):
            result = TEST_RESULTS[i]
            document = Document(test_url)
            assert document.title == result['title']
            assert document.short_title == result['short_title']
            assert document.language == result['language']
            translation = document.translate('it')
            assert translation.detect_language() == 'it'

