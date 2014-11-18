card = json.loads(
    storage['card_create']['response']
)

card_holds_uri = card['links']['cards.card_holds'].replace('{cards.id}', card['cards'][0]['id'])

order = json.loads(
    storage['order_create']['response']
)['orders'][0]


request = {
    'uri': card_holds_uri,
    'payload': {
        'amount': 5000,
        'order': order['href'],
        'description': 'Some descriptive text for the debit in the dashboard'
    },
    'card_href': card['cards'][0]['href'],
    'order_href': order['href'],
}