# 🤖 Discord Bot Valorant & Más

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.0%2B-blueviolet?logo=discord)](https://discordpy.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/)

---

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/5968/5968756.png" width="100" alt="Discord Icon"/>
</p>

## ✨ Descripción

Este bot de Discord está diseñado para entretener y ayudar en servidores de juegos, especialmente para fans de Valorant. Incluye comandos para lanzar dados, repetir mensajes, asignar agentes aleatorios de Valorant y enviar mensajes poéticos personalizados.

---

## ⚡ Comandos principales

- 🎲 **`?roll NdN`** — Lanza dados en formato NdN (ejemplo: `?roll 2d6`).
- 🔁 **`?repeat <veces> <mensaje>`** — Repite un mensaje varias veces.
- 🎮 **`?elige_agente @usuario`** — Asigna un agente aleatorio de Valorant y una playercard con un mensaje divertido.
- 🌼 **`?para_karne`** — Envía un poema romántico con una imagen de margaritas.

---

## 🚀 Instalación rápida

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tuusuario/discord-bot.git
   cd discord-bot
   ```
2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configura tu archivo `.env`:**
   Crea un archivo `.env` con tu token de Discord:
   ```env
   discord-secret=TU_TOKEN_AQUI
   ```
4. **Ejecuta el bot:**
   ```bash
   python main.py
   ```

---

## 🛡️ Seguridad

> **¡Importante!** Nunca subas tu token de Discord a GitHub ni lo compartas públicamente. Usa siempre variables de entorno y asegúrate de que `.env` está en tu `.gitignore`.

---

## 📝 Explicación temporal del código

- El bot utiliza `discord.py` y comandos asíncronos.
- Los tokens y claves sensibles se cargan desde `.env` (usa la librería `python-dotenv`).
- Incluye ejemplos de uso de APIs externas (Valorant, playercards).
- El comando `para_karne` es un ejemplo de cómo enviar mensajes personalizados y embellecidos con imágenes.

---

## 💡 Mejoras futuras

- Añadir más comandos personalizados.
- Mejorar la gestión de errores y mensajes.
- Integrar más APIs de juegos.

---

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/5968/5968756.png" width="40"/>
  <b>¡Disfruta programando y jugando!</b>
</p>
