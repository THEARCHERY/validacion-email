import unittest
from emails.validator import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.validator = EmailValidator()

    # Correos válidos
    def test_email_valido(self):
        email = "usuario.ejemplo@gmail.com"
        self.assertTrue(self.validator.validar(email))

    def test_email_valido_con_guiones(self):
        email = "usuario-ejemplo@gmail.com"
        self.assertTrue(self.validator.validar(email))

    def test_email_valido_con_numeros(self):
        email = "usuario123@gmail.com"
        self.assertTrue(self.validator.validar(email))

    # Correos inválidos
    def test_email_invalido_sin_arroba(self):
        email = "usuarioejemplo.com"
        self.assertFalse(self.validator.validar(email))

    def test_email_invalido_sin_dominio(self):
        email = "usuario@"
        self.assertFalse(self.validator.validar(email))

    def test_email_con_guion_al_inicio_dominio(self):
        email = "usuario@-gmail.com"
        self.assertFalse(self.validator.validar(email))

    def test_email_con_guion_al_final_dominio(self):
        email = "usuario@gmail-.com"
        self.assertFalse(self.validator.validar(email))

    def test_email_excede_longitud(self):
        email = f"{'a'*310}@gmail.com"
        self.assertFalse(self.validator.validar(email))

    def test_email_solo_espacios(self):
        email = "   "
        self.assertFalse(self.validator.validar(email))

    def test_email_con_espacios_internos(self):
        email = "usuario @gmail.com"
        self.assertFalse(self.validator.validar(email))

    def test_tipo_incorrecto(self):
        email = 12345
        self.assertFalse(self.validator.validar(email))

    def test_email_vacio(self):
        email = ""
        self.assertFalse(self.validator.validar(email))

    # Casos con caracteres especiales
    def test_email_invalido_con_caracteres_especiales(self):
        email = "usuario!@gmail.com"
        self.assertFalse(self.validator.validar(email))

    def test_email_valido_con_puntos(self):
        email = "usuario.ejemplo@gmail.com"
        self.assertTrue(self.validator.validar(email))

if __name__ == "__main__":
    unittest.main()
