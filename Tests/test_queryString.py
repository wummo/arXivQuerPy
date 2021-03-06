import unittest
from queryString import *


class test_queryString(unittest.TestCase):
    def setUp(self):
        self.queryString = QueryString()

    def tearDown(self):
        self.queryString = None


class test_emptyQueryString(test_queryString):
    def test_strEmpty(self):
        with self.assertRaises(EmptyQueryException):
            str(self.queryString)

    def test_getSearchStringEmpty(self):
        self.assertRaises(EmptyQueryException,
                          self.queryString.getSearchString)

    def test_getAllAuthorQueriesEmpty(self):
        self.assertEqual(self.queryString.getAllAuthorQueries(), [])

    def test_getAllTitleQueriesEmpty(self):
        self.assertEqual(self.queryString.getAllTitleQueries(), [])

    def test_getAllAuthorQueriesEmpty(self):
        self.assertEqual(self.queryString.getAllAbstractQueries(), [])

    def test_getAllCategoriesEmpty(self):
        self.assertEqual(self.queryString.getAllCategories(), [])


class test_addingRemovingCategories(test_queryString):
    def test_addingValidCategories(self):
        self.queryString.addCategory("cond-mat")
        self.queryString.addCategory("cond-mat.soft")
        self.assertEqual(self.queryString.getAllCategories(),
                         ["cond-mat", "cond-mat.soft"])

    def test_addingValidCategoryTwice(self):
        self.queryString.addCategory("cond-mat")
        self.queryString.addCategory("cond-mat")
        self.assertEqual(self.queryString.getAllCategories(), ["cond-mat"])

    def test_addingEmptyCategory(self):
        with self.assertRaises(InvalidCategoryException):
            self.queryString.addCategory("")

    def test_addingUnknownCategory(self):
        with self.assertRaises(InvalidCategoryException):
            self.queryString.addCategory("definetlyInvalid")

    def test_removeExistingCategory(self):
        self.queryString.addCategory("cond-mat")
        self.queryString.addCategory("cond-mat.soft")
        self.queryString.removeCategory("cond-mat")
        self.assertEqual(self.queryString.getAllCategories(),
                         ["cond-mat.soft"])

    def test_removeInvalidCategory(self):
        with self.assertRaises(InvalidCategoryException):
            self.queryString.removeCategory("definetlyInvalid")

    def test_removeNotExistingCategory(self):
        self.queryString.addCategory("cond-mat.soft")
        with self.assertRaises(NotInQueryException):
            self.queryString.removeCategory("cond-mat")


class test_addingRemovingSearchQueries(test_queryString):
    def test_addAuthors(self):
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.addAuthorQuery("Mustermann_M")
        self.assertEqual(self.queryString.getAllAuthorQueries(),
                         ["Testfrau_T", "Mustermann_M"])

    def test_addAbstracts(self):
        self.queryString.addAbstractQuery("Awesome")
        self.queryString.addAbstractQuery("Stuff")
        self.assertEqual(self.queryString.getAllAbstractQueries(),
                         ["Awesome", "Stuff"])

    def test_addTitles(self):
        self.queryString.addTitleQuery("Awesome")
        self.queryString.addTitleQuery("Stuff")
        self.assertEqual(self.queryString.getAllTitleQueries(),
                         ["Awesome", "Stuff"])

    def test_addExistingAuthors(self):
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.addAuthorQuery("Testfrau_T")
        self.assertEqual(self.queryString.getAllAuthorQueries(),
                         ["Testfrau_T"])

    def test_addExistingAbstracts(self):
        self.queryString.addAbstractQuery("Awesome")
        self.queryString.addAbstractQuery("Awesome")
        self.assertEqual(self.queryString.getAllAbstractQueries(), ["Awesome"])

    def test_addExistingTitles(self):
        self.queryString.addTitleQuery("Awesome")
        self.queryString.addTitleQuery("Awesome")
        self.assertEqual(self.queryString.getAllTitleQueries(), ["Awesome"])

    def test_removeExistingAuthors(self):
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.addAuthorQuery("Mustermann_M")
        self.queryString.removeAuthorQuery("Testfrau_T")
        self.assertEqual(self.queryString.getAllAuthorQueries(),
                         ["Mustermann_M"])

    def test_removeExistingAbstracts(self):
        self.queryString.addAbstractQuery("Awesome")
        self.queryString.addAbstractQuery("Stuff")
        self.queryString.removeAbstractQuery("Awesome")
        self.assertEqual(self.queryString.getAllAbstractQueries(),
                         ["Stuff"])

    def test_removeExistingTitles(self):
        self.queryString.addTitleQuery("Awesome")
        self.queryString.addTitleQuery("Stuff")
        self.queryString.removeTitleQuery("Awesome")
        self.assertEqual(self.queryString.getAllTitleQueries(),
                         ["Stuff"])

    def test_removeNotExistingAuthors(self):
        self.queryString.addAuthorQuery("Mustermann_M")
        with self.assertRaises(NotInQueryException):
            self.queryString.removeAuthorQuery("Testfrau_T")

    def test_removeNotExistingAbstracts(self):
        self.queryString.addAbstractQuery("Stuff")
        with self.assertRaises(NotInQueryException):
            self.queryString.removeAbstractQuery("Awesome")

    def test_removeNotExistingTitles(self):
        self.queryString.addTitleQuery("Stuff")
        with self.assertRaises(NotInQueryException):
            self.queryString.removeTitleQuery("Awesome")

    def test_removeAllExistingAuthors(self):
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.addAuthorQuery("Mustermann_M")
        self.queryString.removeAllAuthorQueries()
        self.assertEqual(self.queryString.getAllAuthorQueries(),
                         [])

    def test_removeAllExistingAbstracts(self):
        self.queryString.addAbstractQuery("Awesome")
        self.queryString.addAbstractQuery("Stuff")
        self.queryString.removeAllAbstractQueries()
        self.assertEqual(self.queryString.getAllAbstractQueries(),
                         [])

    def test_removeAllExistingTitles(self):
        self.queryString.addTitleQuery("Awesome")
        self.queryString.addTitleQuery("Stuff")
        self.queryString.removeAllTitleQueries()
        self.assertEqual(self.queryString.getAllTitleQueries(),
                         [])

    def test_removeEmptyAuthors(self):
        self.queryString.removeAllAuthorQueries()
        self.assertEqual(self.queryString.getAllAuthorQueries(),
                         [])

    def test_removeEmptyAbstracts(self):
        self.queryString.removeAllAbstractQueries()
        self.assertEqual(self.queryString.getAllAbstractQueries(),
                         [])

    def test_removeEmptyTitles(self):
        self.queryString.removeAllTitleQueries()
        self.assertEqual(self.queryString.getAllTitleQueries(),
                         [])


class test_queryStringProduction(test_queryString):
    def test_onlyAuthorNoCategory(self):
        self.queryString.addAuthorQuery("Testfrau_T")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T%29%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=10")

    def test_onlyAbstractNoCategory(self):
        self.queryString.addAbstractQuery("Awesome")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28abs:Awesome%29%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=10")

    def test_onlyTitleNoCategory(self):
        self.queryString.addTitleQuery("Awesome")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28ti:Awesome%29%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=10")

    def test_onlyTitleWithCategory(self):
        self.queryString.addTitleQuery("Awesome")
        self.queryString.addCategory("cond-mat")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28ti:Awesome%29%29"
                         r"+AND+%28cat:cond-mat%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=10")

    def test_onlyTitleWithTwoCategories(self):
        self.queryString.addTitleQuery("Awesome")
        self.queryString.addCategory("cond-mat")
        self.queryString.addCategory("cond-mat.soft")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28ti:Awesome%29%29"
                         r"+AND+%28cat:cond-mat+OR+cat:cond-mat.soft%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=10")

    def test_onlyAuthorsNoCategory(self):
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.addAuthorQuery("Mustermann_M")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T+OR+"
                         r"au:Mustermann_M%29%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=10")

    def test_onlyAbstractsNoCategory(self):
        self.queryString.addAbstractQuery("Awesome")
        self.queryString.addAbstractQuery("Stuff")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28abs:Awesome+OR+abs:Stuff%29%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=10")

    def test_onlyTitlesNoCategory(self):
        self.queryString.addTitleQuery("Awesome")
        self.queryString.addTitleQuery("Stuff")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28ti:Awesome+OR+ti:Stuff%29%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=10")

    def test_AuthorsTitlesAbstractsWithCategory(self):
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.addAuthorQuery("Mustermann_M")
        self.queryString.addTitleQuery("Awesome")
        self.queryString.addTitleQuery("Stuff")
        self.queryString.addAbstractQuery("Great")
        self.queryString.addAbstractQuery("Science")
        self.queryString.addCategory("cond-mat")
        self.queryString.addCategory("cond-mat.soft")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T+OR+"
                         r"au:Mustermann_M%29+OR+"
                         r"%28ti:Awesome+OR+ti:Stuff+OR+"
                         r"abs:Great+OR+abs:Science%29%29"
                         r"+AND+%28cat:cond-mat+OR+cat:cond-mat.soft%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=10")


class test_queryStringConstructor(unittest.TestCase):
    def test_onlyAuthorChangeN(self):
        self.queryString = QueryString(N=100)
        self.queryString.addAuthorQuery("Testfrau_T")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T%29%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=100")

    def test_onlyAuthorChangeStart(self):
        self.queryString = QueryString(start=100)
        self.queryString.addAuthorQuery("Testfrau_T")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T%29%29"
                         r"&sortBy=lastUpdatedDate&start=100&max_results=10")

    def test_onlyAuthorChangeStartAndN(self):
        self.queryString = QueryString(N=5, start=100)
        self.queryString.addAuthorQuery("Testfrau_T")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T%29%29"
                         r"&sortBy=lastUpdatedDate&start=100&max_results=5")

    def test_onlyAuthorUpdateN(self):
        self.queryString = QueryString()
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.nextNumberOfResults(15)
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T%29%29"
                         r"&sortBy=lastUpdatedDate&start=10&max_results=15")

    def test_onlyAuthorChangeUpdateN(self):
        self.queryString = QueryString(N=8, start=12)
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.nextNumberOfResults(15)
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T%29%29"
                         r"&sortBy=lastUpdatedDate&start=20&max_results=15")

    def test_invalidConnectorConstructor(self):
        with self.assertRaises(InvalidConnectorException):
            QueryString(connector="asdf")

    def test_invalidConnector(self):
        with self.assertRaises(InvalidConnectorException):
            QueryString().setConnector("asdf")

    def test_authorTitleAndConstructor(self):
        self.queryString = QueryString()
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.addTitleQuery("Awesome")
        self.queryString.setConnector("and")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T%29+AND+"
                         r"%28ti:Awesome%29%29&sortBy=lastUpdatedDate"
                         r"&start=0&max_results=10")

    def test_authorAbstractAndConstructor(self):
        self.queryString = QueryString()
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.addAbstractQuery("Awesome")
        self.queryString.setConnector("and")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T%29+AND+"
                         r"%28abs:Awesome%29%29&sortBy=lastUpdatedDate"
                         r"&start=0&max_results=10")

    def test_authorTitleAbstractAndConstructor(self):
        self.queryString = QueryString()
        self.queryString.addAuthorQuery("Testfrau_T")
        self.queryString.addTitleQuery("Awesome")
        self.queryString.addAbstractQuery("Stuff")
        self.queryString.setConnector("and")
        self.assertEqual(str(self.queryString),
                         r"http://export.arxiv.org/api/query?"
                         r"search_query=%28%28au:Testfrau_T%29+AND+"
                         r"%28ti:Awesome+OR+abs:Stuff%29%29"
                         r"&sortBy=lastUpdatedDate&start=0&max_results=10")


if __name__ == "__main__":
    unittest.main()
