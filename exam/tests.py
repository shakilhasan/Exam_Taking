from django.test import TestCase
from exam.models import Question
from django.utils import timezone
from django.urls import reverse
from exam.forms import QuestionForm

# models test
class QuestionTest(TestCase):

    def create_question(self, name="only a test", select=True):
        return Question.objects.create(name=name, select=select)

    def test_question_creation(self):
        w = self.create_question()
        self.assertTrue(isinstance(w, Question))
        self.assertEqual(w.__str__(), w.name)

# forms
    def test_invalid_form(self):
        w = Question.objects.create(name='Foo', select=True)
        data = {'name': w.name, 'select': w.select,}
        form = QuestionForm(data=data)
        self.assertFalse(form.is_valid())

if __name__ == '__main__':
    unittest.main()




# model mommy
from model_mommy import mommy

class QuestionTestMommy(TestCase):

	def test_book_info_creation_mommy(self):
		question = mommy.make(Question)
		self.assertTrue(isinstance(question, Question))
		self.assertEqual(question.__str__(), question.name)
