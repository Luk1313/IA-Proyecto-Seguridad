# 🔐 CGSA-Seguridad — Sistema de Seguridad Inteligente para Cajeros Automáticos

> Monitoreo inteligente en tiempo real con visión por computadora, alertas automáticas y análisis de riesgo mediante Python y OpenCV.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![Automatización](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-brightgreen)

---

## 📸 Descripción del Proyecto

**CGSA-Seguridad** es un sistema automatizado diseñado para:
- Monitorear cámaras de seguridad en tiempo real.
- Detectar movimiento anómalo, obstrucción y manipulación del cajero.
- Evaluar el nivel de riesgo de los eventos.
- Activar alarmas y grabaciones automáticamente.
- Notificar al equipo de seguridad y autoridades mediante alertas.

---

## 🚀 Tecnologías Utilizadas

| Tecnología | Uso |
|-----------|-----|
| `Python 3.9+` | Lenguaje principal del sistema |
| `OpenCV` | Procesamiento de video y visión por computadora |
| `Threading` | Manejo de múltiples cámaras en paralelo |
| `GitHub Actions` | CI/CD automatizado para pruebas y despliegue |
| `Unittest` | Pruebas automatizadas del sistema |

---

## 🧠 Arquitectura General

```
Cámaras IP ──▶ [CGSA-Seguridad] ──▶ Evaluación de Riesgo ──▶ Acciones:
                              ├── Grabar Video
                              ├── Activar Alarma
                              └── Enviar Alerta
```

---

## 📂 Estructura del Repositorio

```
.
├── CGSA-Seguridad.py        # Código principal del sistema
├── tests/                   # Carpeta para pruebas unitarias
│   └── test_seguridad.py
├── .github/
│   └── workflows/
│       └── python-package.yml  # Flujo CI/CD en GitHub Actions
├── requirements.txt         # Dependencias
├── README.md                # Este archivo
└── Evolución_Acciones.ipynb # Análisis de mejoras y evolución
```

---

## ⚙️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Luk1313/CGSA-Seguridad.git
cd CGSA-Seguridad
```

2. Crea un entorno virtual e instala dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows

pip install -r requirements.txt
```

---

## ▶️ Uso

```bash
python CGSA-Seguridad.py
```

El sistema comenzará a monitorear las cámaras configuradas y aplicará evaluación de riesgo en tiempo real.

---

## 🧪 Pruebas

Para ejecutar las pruebas unitarias:

```bash
python -m unittest discover -s tests
```

---

## 📦 Automatización CI/CD

Este proyecto utiliza **GitHub Actions** para automatizar:
- Instalación de dependencias
- Pruebas en distintas versiones de Python
- Simulación de despliegue

Archivo de flujo: `.github/workflows/python-package.yml`

---

## 📈 Evolución del Proyecto

- [x] Detección de movimiento
- [x] Evaluación de riesgo bajo/medio/alto
- [x] Activación de alarma y grabación
- [x] Alerta automática
- [ ] Integración con sistema de alertas por WhatsApp/Email
- [ ] Dashboard con monitoreo en tiempo real
- [ ] Despliegue en Streamlit / servidor cloud

---

## 👨‍💻 Autor

**Lucas Rapiman Huican**  
Analista en Ciberseguridad | Estudiante de Ingeniería en Informática  
GitHub: [@Luk1313](https://github.com/Luk1313)

---

## 🔐 Licencia

Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente, citando la autoría.

---

## 💬 Contacto

Si deseas colaborar o implementar este sistema en tu organización, contáctame por [LinkedIn](https://linkedin.com) o correo electrónico.
