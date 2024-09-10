# Sistema de Sockets para Envío de Texto

Este repositorio contiene un sistema básico de comunicación por sockets que permite el envío de texto entre un cliente y un servidor. El sistema está disponible en tres versiones:

1. **Plano**: Comunicación sin cifrado.
2. **Encriptado con Salsa20**: Comunicación cifrada utilizando el algoritmo de cifrado Salsa20.
3. **Encriptado con AES256**: Comunicación cifrada utilizando el algoritmo de cifrado AES256.

## Requisitos

- Python 3.7 o superior
- Paquetes Python necesarios:
  - `pycriptodome` (para la versión encriptada)

## Instalación

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install pycriptodome
