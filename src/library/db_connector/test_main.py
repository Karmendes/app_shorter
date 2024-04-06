from unittest import mock
from datetime import datetime
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.library.db_connector.models import ShortURL
from src.library.db_connector.main import RepositoryShortURL
from src.library.utils.main import create_record_short_code

class ConnectionHandlerMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(data =
                [
                    (   [
                        mock.call.query(ShortURL),
                        mock.call.filter(ShortURL.short_code == "abcdef")
                        ],
                        [ShortURL(
                                id = 2,
                                short_code = "abcdef",
                                url = "www.google.com",
                                created = datetime.now().isoformat(),
                                lastredirect=datetime.now().isoformat(),
                                redirectcount = 1
                            )
                        ]
                    )
                ]
        )


def test_read_by_short_code():
    db_connector = RepositoryShortURL(ConnectionHandlerMock())
    response = db_connector.read_by_short_code('abcdef')
    assert isinstance(response,ShortURL)
    assert response.short_code == 'abcdef'
    assert response.url == "www.google.com"

def test_insert_by_dict():
    db_connector = RepositoryShortURL(ConnectionHandlerMock())
    data = create_record_short_code('www.google.com','abcedf')
    response = db_connector.insert_by_dict(data)
    print(response)

def test_update_use_short_code():
    db_connector = RepositoryShortURL(ConnectionHandlerMock())
    response = db_connector.update_use_short_code('abcdef')
    print(response)
