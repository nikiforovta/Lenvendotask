from base import BaseApi


class TestSearch(BaseApi):
    def test_search_alcatel(self):
        result = self.api_client.get_results(search='Alcatel', sort_field='name')
        assert all('Alcatel' in item.name for item in result)
        assert result == sorted(result)
