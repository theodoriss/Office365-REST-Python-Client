from office365.onedrive.sites.site import Site
from tests.graph_case import GraphTestCase


class TestSite(GraphTestCase):
    """OneDrive specific test case base class"""
    target_site = None  # type: Site

    @classmethod
    def setUpClass(cls):
        super(TestSite, cls).setUpClass()
        cls.target_site = cls.client.sites.root
        cls.followed_sites_count = None
        assert cls.target_site.resource_path is not None

    @classmethod
    def tearDownClass(cls):
        pass

    def test1_get_root_site(self):
        root_site = self.target_site.get().execute_query()
        assert root_site.id is not None

    def test2_get_site_by_path(self):
        pass

    def test3_get_activities_by_interval(self):
        col = self.target_site.get_activities_by_interval().execute_query()
        self.assertIsNotNone(col)

    def test4_list_followed_sites(self):
        sites = self.client.me.followed_sites.get().execute_query()
        self.followed_sites_count = len(sites)

    def test5_follow(self):
        pass

    def test6_unfollow(self):
        pass
