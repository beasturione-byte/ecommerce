# E-Commerce MVP - Entrega Portafolio

Este proyecto es una plataforma de e-commerce desarrollada con Django, diseñada para demostrar un flujo completo de compras: desde la visualización del catálogo hasta la confirmación de la orden, incluyendo roles de usuario y persistencia de datos.

## Características Principales (Alcance)
- **Catálogo de Productos:** Mostrado desde la base de datos mediante el ORM de Django.
- **Roles de Usuario:**
  - *Cliente:* Puede iniciar sesión, explorar productos, gestionar su carrito y confirmar compras.
  - *Administrador:* Acceso al panel de control para crear, editar y eliminar productos.
- **Carrito de Compras:** Funcionalidad basada en sesiones (agregar, quitar, actualizar cantidades y cálculo de subtotales).
- **Validaciones:** Restricciones de base de datos y formularios para evitar precios o cantidades negativas.
- **Interfaz:** Construida con HTML5 y Bootstrap 5 para una navegación fluida y responsiva.

---

## Requisitos e Instalación

1. **Clonar el repositorio o descomprimir el proyecto:**
   ```bash
   # Si usas GitHub:
   git clone [ENLACE_A_TU_REPOSITORIO_AQUI]
   cd [NOMBRE_DE_LA_CARPETA]