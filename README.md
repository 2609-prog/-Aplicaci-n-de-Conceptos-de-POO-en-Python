# -Aplicaci-n-de-Conceptos-de-POO-en-Python


Desarrollar un programa en Python que aplique los fundamentos de la Programación Orientada a Objetos (POO), incluyendo **clases**, **herencia**, **encapsulación** y **polimorfismo**
---

# ¿Por qué usar una clase `Animal`?

Se eligió la clase `Animal` como clase base porque representa una **estructura común para cualquier tipo de animal** dentro del programa. Esto permite definir atributos y comportamientos generales (como `nombre`, `hacer_sonido()` o `alimentar()`) que **todas las subclases pueden heredar y personalizar**.

Este diseño es típico en POO cuando se quiere trabajar con jerarquías. De esta forma se evita repetir código y se favorece la **reutilización y extensión**.

---

## Clases implementadas

- **Animal** (clase base):
  - Atributo encapsulado `__alimentado` para controlar su estado.
  - Métodos comunes como `alimentar()` y `hacer_sonido()`.

- **León**:
  - Hereda de `Animal`.
  - Agrega un atributo `edad` y sobrescribe `hacer_sonido()` con un rugido.

- **Pájaro**:
  - Hereda de `Animal`.
  - Agrega un atributo `puede_volar` y sobrescribe `hacer_sonido()` con un canto.

---

## Conceptos de POO utilizados

| Concepto         | Implementación                                                                 

**Clase y objeto**   Se definen clases (`Animal`, `Leon`, `Pajaro`) y se crean objetos (`Luke`, `Piolin`). 
**Herencia**         `Leon` y `Pajaro` heredan de `Animal` para reutilizar código.              
**Encapsulación**    El atributo `__alimentado` está oculto y solo accesible con métodos públicos. 
**Polimorfismo**     Cada clase redefine `hacer_sonido()` para comportarse distinto.             



## Ejecución

El programa puede ejecutarse directamente con Python, mostrando:

- El sonido específico de cada animal.
- El uso del método `alimentar()`.
- Comprobación del estado del animal.

---

## Autor

- Estudiante: Lisseth Puco
- Universidad Estatal Amazónica
