from unittest import TestCase, main
from main import add


class TestCalculatrice(TestCase):  # ne pas oublier de commencer par Test,test.
    def test_add_two_positive_numbers(self):
        self.assertEqual(add(5, 10), 15)

    def test_add_two_letters(self):
        self.assertEqual(add("a", "b"), "ab")

    def test_add_two_none(self):
        with self.assertRaises(TypeError):
            add(None, None)
            """test vérifie si la fonction add lève une exception de type TypeError 
            lorsque des arguments de type None sont passés à la fonction, ici le test fonctionne bien"""

# main()  # permet d'exécuter test  ( dans terminal, python test.py - v)

# utilisation du module unittest pour exécuter test  ( dans  terminal, python -m unittest test)

# installation coverage ( dans terminal, coverage run -m unittest test)
# dans terminal ,coverage html ,  pour voir la couverture des test   commande à regénérer pour mise a jour