from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt

# Create your tests here.


class EditorTestClass(TestCase):

    # set up method
    def setUp(self):
        self.ray = Editor(first_name='ray', last_name='yego',
                          email='ray@django.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.ray, Editor))

    # Testing save method

    def test_save_method(self):
        self.ray.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete_method(self):
        self.ray.save_editor()
        self.test = Editor(first_name='test',
                           last_name='delete', email='delete@test.com')
        self.test.save_editor()
        self.ray.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 1)


class ArticleTestclass(TestCase):
    def setUp(self):
        # creating a new editor and saving it
        self.ray = Editor(first_name='ray', last_name='yego',
                          email='ray@django.com')
        self.ray.save_editor()

        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(
            title='Test Article', post='This is a random test Post', editor=self.ray)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def teardown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2019-08-05'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
