from pymongo.collation import CollationAlternate
from py_conversations.ops.insert_items import insert_items


def test_insert_items():
    """
    Tests the insertion of items passed as a dictionary into a given database collection
    """
    result =  insert_items(
        collection_name='test_collection', 
        items=[
            {'a': 0, 'b': 1, 'c': 2}, 
            {'d': 3, 'e': 4, 'f': 5}])
    assert result.acknowledged == True
    assert len(result.inserted_ids) == 2
