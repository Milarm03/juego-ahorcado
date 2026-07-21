# juego-ahorcado

El ahorcado de toda la vida, en la terminal. Dibujo ASCII, 25 palabras y contador de partidas.

Solo librería estándar de Python.

```
  EL AHORCADO
  Palabra de 7 letras.

     +---+
     O   |
    /|   |
         |
        ===

  c o n _ o _ a

  Falladas: e i
  Te quedan 4 intentos.

  Letra:
```

> De cuando empecé con Python. Acabo de abrir GitHub y estoy subiendo lo que tenía en local.

## Jugar

```bash
python3 ahorcado.py
```

Seis fallos y pierdes. Al terminar puedes seguir jugando y lleva la cuenta de cuántas has ganado.

## Cosas que aprendí haciéndolo

**El muñeco es una lista, no un `if`.** La primera versión que hice tenía un `if fallos == 1: ... elif fallos == 2: ...`. Guardando los dibujos en una lista, el índice *es* el número de fallos:

```python
print(MUNECO[len(falladas)])
```

Seis líneas menos y añadir una fase nueva es meter un elemento más.

**Las tildes y la eñe dan guerra.** Si la palabra es "montaña" y el jugador teclea `n`, no coincide. Y escribir `ñ` en algunos teclados es incómodo.

La solución es normalizar antes de comparar:

```python
sin_tildes = unicodedata.normalize("NFD", texto)
return "".join(c for c in sin_tildes if unicodedata.category(c) != "Mn")
```

`NFD` separa la letra base de su acento (`ñ` pasa a ser `n` + tilde), y luego se descarta todo lo que sea categoría `Mn` (marcas diacríticas). Queda `montana` y se juega sin problema.

**Los conjuntos encajan aquí.** Las letras acertadas y falladas son `set`, no listas: no admiten duplicados por definición y comprobar si una letra ya se dijo es instantáneo. Además `acertadas | falladas` da todas las usadas en una línea.

**Validar la entrada da más trabajo que el juego.** El bucle de `pedir_letra` rechaza cadenas vacías, palabras enteras, números, símbolos y letras repetidas. Es más código que la lógica de acertar o fallar.

## Cómo se detecta la victoria

```python
if all(l in acertadas for l in palabra):
```

`all()` con un generador: en cuanto encuentra una letra que falta, para y devuelve `False`. No recorre el resto.

## Pendiente

- [ ] Leer las palabras de un archivo
- [ ] Niveles de dificultad por longitud
- [ ] Guardar récord entre sesiones
- [ ] Pistas (categoría de la palabra)

---

Milagrosa Rivero · [github.com/Milarm03](https://github.com/Milarm03)
