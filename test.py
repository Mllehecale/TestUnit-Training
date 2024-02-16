import pytest
from main import add
def test_add_two_positive_numbers():
    assert add(5, 10) == 15

def test_add_two_letters():
    assert add("a", "b") == "ab"

def test_add_two_none():
    with pytest.raises(TypeError):
        add(None, None)
        """test vérifie si la fonction add lève une exception de type TypeError 
            lorsque des arguments de type None sont passés à la fonction, ici le test fonctionne bien"""

# main()  # permet d'exécuter test  ( dans terminal, python test.py - v)

# utilisation du module unittest pour exécuter test  ( dans  terminal, python -m unittest test , unittest a importer)

# installation coverage ( dans terminal, coverage run -m unittest test)
# dans terminal ,coverage html ,  pour voir la couverture des test   commande à regénérer pour mise a jour

#utilisation pytest pip install pytest    pip install pytest-htm  ( dans terminal, pytest test.py -v )
# créer rapport HTML avec pytest  ( dans terminal, pytest test.py -v --html=index.html)