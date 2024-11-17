# Comunicación UDP simple

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

Ejemplo simple de comunicación cliente-servidor utilizando sockets UDP. Consta de dos scripts de cliente y un script de servidor que ilustran el flujo básico de envío y recepción de mensajes mediante UDP.

## Archivos

- **cliente1.py** y **cliente2.py**: Scripts de cliente que envían un mensaje al servidor.
- **servidor.py**: Script de servidor que recibe los mensajes de los clientes y responde.

## Ejecución

1. Iniciar el servidor:

```bash
python servidor.py
```

2. Ejecutar los scripts de cliente en terminales separadas:

```bash
python cliente1.py
python cliente2.py
```

El servidor recibirá los mensajes de los clientes y enviará una respuesta.
