import re
import logging

class EmailValidator:
    def __init__(self):
        self.regex = re.compile(r'([A-Za-z]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    def validar(self, correo: str):
        try:
            # Verificar si la entrada es una cadena
            if not isinstance(correo, str):
                raise TypeError("El correo debe ser una cadena de texto")

            # Verificar si está vacío
            if correo.strip() == "":
                raise ValueError("El correo no puede estar vacío")

            # Verificar el formato general con regex
            if not re.fullmatch(self.regex, correo):
                return False

            # Verificar longitud del correo
            if len(correo) > 320:  # Longitud máxima estándar para un correo
                raise ValueError("El correo excede la longitud máxima permitida (320 caracteres)")

            # Verificar que el dominio no contenga caracteres no permitidos
            domain = correo.split('@')[-1]
            if domain.startswith('-') or domain.endswith('-'):
                raise ValueError("El dominio no puede empezar ni terminar con un guion (-)")

            return True

        except TypeError as e:
            logging.error(f"Error de tipo: {e}")
            return False

        except ValueError as e:
            logging.error(f"Error de valor: {e}")
            return False

        except Exception as e:
            logging.error(f"Error inesperado: {e}")
            return False
