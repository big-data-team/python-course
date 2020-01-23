from wikipedia_app import app

def test_can_response_to_root():
    with app.test_client() as client:
        response = client.get('/')
        #from pdb import set_trace; set_trace()
        #b'Welcome to MailWikipedia Search Engine'
        assert 'Welcome to MailWikipedia Search Engine' in response.data.decode(response.charset)