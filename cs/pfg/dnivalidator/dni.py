from zope.interface import implements
from Products.validation.interfaces.IValidator import IValidator
from Products.validation import validation

class Dni:
    """ Validates a String field to contain a Spanish ID card number
    and letter.

    The verification algorithm is described here:
      http://es.wikibooks.org/wiki/Algoritmo_para_obtener_la_letra_del_NIF

    """
    implements(IValidator)

    name = 'Dni'

    def __init__(self, name, title='', description=''):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kwargs):
        if value[0] not in ['0','1','2','3','4','5','6','7','8','9']:
            value=value[1:]
        let = value[-1:].upper()
	number = value[:-1]
	number = int(number)
	number = number % 23
	letters = 'TRWAGMYFPDXBNJZSQVHLCKET'
	letter = letters[number:number + 1]
	if let == letter:
            return 1
        return ("Validation failed(%s): must be checked." % self.name)

validation.register(Dni('dni')) 
