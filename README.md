# IAW - Despliegue de Aplicación Flask con Docker y Git

Este repositorio contiene el desarrollo y despliegue de las prácticas 6.2 y 6.3 del módulo **Implantación de Aplicaciones Web**.

## Práctica 6.2: Creación de Imágenes Propias y Persistencia
En esta fase se trabajó sobre una aplicación **Flask** y su despliegue mediante contenedores, cumpliendo los siguientes requisitos:

* **Refactorización de la App:** Se adaptó la aplicación para que la base de datos SQLite3 resida en un directorio independiente (`/sqlite3-db`) de la aplicación principal.
* **Dockerfile Personalizado:** Creación de una imagen propia basada en Python. Siguiendo principios de inmutabilidad, la base de datos no se incorpora a la imagen para garantizar que el contenedor sea efímero y sin estado.
* **Orquestación con Docker Compose:** * Automatización del levantamiento del servicio.
    * Publicación de puertos para acceso externo.
    * **Gestión de Volúmenes:** Uso de volúmenes para mapear la base de datos local y asegurar la persistencia de los datos.
* **Distribución en Docker Hub:** La imagen final ha sido subida al registro oficial de Docker bajo el perfil de usuario correspondiente.

## Práctica 6.3: Control de Versiones con GitHub
En la actual práctica 6.3, se ha procedido a la creación de este repositorio en GitHub para gestionar el código fuente y la configuración del proyecto.

**Operaciones realizadas:**
1.  Vinculación de la cuenta corporativa `@iesgrancapitan.org`.
2.  Inicialización de Git local y configuración de identidad.
3.  Sincronización del directorio de trabajo con este repositorio remoto.
4.  Gestión de ramas y resolución de conflictos de subida.

---
**Tecnologías utilizadas:**
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

*Jesús Díaz Mata - 2º ASIR*