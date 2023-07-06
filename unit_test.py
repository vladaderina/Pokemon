from unittest import TestCase, main
from itog import GetInfo

class CalcTest(TestCase):
    def test_posit(self):
        self.assertEqual(GetInfo("56"), "Имя покемона: mankey, его способности: ['vital-spirit', 'anger-point', 'defiant']")
    def test_notname(self):
        with self.assertRaises(Exception) as e:
            GetInfo("dd")
        self.assertEqual('Покемона с таким ID нет', e.exception.args[0])
if __name__ == '__main__':
    main() 
