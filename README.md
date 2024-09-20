# FastApi
```bash
fastapi dev main.py
```
- En la nueva organización
```bash
fastapi run src
```
## Conectarse a la consola de postgresql
```bash
psql
```
## Crear base de datos
```bash
CREATE DATABASE bookly_db;
```
## Conectarse a base de datos
```bash
\c bookly_db
```
## Listar tablas
```bash
\dt
```
## Ver columnas de tabla
```bash
\d books
```
## Eliminar tabla
```bash
DROP TABLE books;
```
## Alembic
```bash
alembic init -t async migrations
```
### Creamos migraciones
```bash
alembic revision --autogenerate -m "init"
```
### Ejecutamos las migraciones
```bash
alembic upgrade head
```
### Al cambiar una columna de un modelo
```bash
alembic revision --autogenerate -m "add password hash"
```