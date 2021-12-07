from py_conversations.ops.scrape_googlenews import scrape_googlenews

def test_scrape_googlenews():
    response = scrape_googlenews()
    assert isinstance(response, list), "returned object should be of type 'list'"
    assert isinstance(response[0], dict), "list items should be of type 'dict'"
