import discord 
from discord.ext import commands
import random
import aiohttp  # Librería para realizar peticiones HTTP de forma asíncrona
import json

description = '''An example bot to showcase the discord.ext.commands extension
module.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content: str):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

# @bot.command()
# async def catfact(ctx):
#     """Consulta la API de catfact.ninja y envía un dato curioso de gatos."""
#     url = "https://catfact.ninja/fact"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             if response.status == 200:
#                 # Parseamos la respuesta en JSON
#                 data = await response.json()
#                 fact = data.get("fact", "No se encontró dato alguno.")
#                 await ctx.send(f"🐱 Dato curioso: {fact}")
#             else:
#                 await ctx.send("❌ Ocurrió un error al consultar la API.")

@bot.command()
async def elige_agente(ctx, member: discord.Member):
    """
    Consulta la API de agentes de Valorant y la de playercards para seleccionar:
      - Un agente aleatorio.
      - Una imagen aleatoria de playercards.
    Envía un embed humorístico con la información.
    """
    async with aiohttp.ClientSession() as session:
        # Consulta la API de agentes
        agents_url = "https://valorant-api.com/v1/agents"
        async with session.get(agents_url) as response:
            if response.status != 200:
                await ctx.send("❌ Error al obtener la lista de agentes.")
                return
            try:
                data_agents = await response.json()
            except Exception as e:
                await ctx.send("❌ Error al parsear los datos de agentes.")
                return
        agents = data_agents.get("data", [])
        if not agents:
            await ctx.send("❌ No se encontraron agentes en la respuesta.")
            return
        chosen_agent = random.choice(agents)
        agent_name = chosen_agent.get("displayName", "Agente desconocido")
        
        # Consulta la API de playercards
        playercards_url = "https://valorant-api.com/v1/playercards"
        async with session.get(playercards_url) as response:
            if response.status != 200:
                await ctx.send("❌ Error al obtener las playercards.")
                return
            try:
                # Ignoramos el content_type para forzar el parseo a JSON
                data_cards = await response.json(content_type=None)
            except json.decoder.JSONDecodeError:
                text = await response.text()
                if not text.strip():
                    await ctx.send("❌ La API de playercards no devolvió ningún contenido.")
                else:
                    await ctx.send("❌ Error parseando JSON de playercards: " + text)
                return
        # Se asume que la respuesta tiene la lista en la clave "data"
        playercards = data_cards.get("data", [])
        if not playercards:
            await ctx.send("❌ No se encontraron playercards en la respuesta.")
            return
        chosen_card = random.choice(playercards)
        # Se intenta obtener la URL de la imagen de la card (priorizando largeArt, sino displayIcon)
        image_url = chosen_card.get("largeArt") or chosen_card.get("displayIcon")
    
    # Mensajes humorísticos para el embed
    mensajes = [
        f"¡Atención {member.mention}! Hoy te toca jugar como **{agent_name}**. ¡El destino ha hablado!",
        f"{member.mention}, los dioses del juego han decidido que tu héroe sea **{agent_name}**. ¡A romperla!",
        f"Por arte del azar, {member.mention} deberá tomar las riendas de **{agent_name}**. ¡Que comience la épica!",
        f"¡Sorpresa! {member.mention} juega de **{agent_name}** hoy. ¡Prepárate para la acción!"
    ]
    mensaje = random.choice(mensajes)
    
    embed = discord.Embed(
        title="Asignación de Agente",
        description=mensaje,
        color=discord.Color.blue()
    )
    if image_url:
        embed.set_image(url=image_url)
    else:
        embed.add_field(name="PlayerCard", value="No se encontró imagen de playercard.", inline=False)
    embed.set_footer(text="¡Buena suerte en la partida!")
    
    await ctx.send(embed=embed)


@bot.command()
async def para_karne(ctx):
    """
    Envía un embed expresivo y delicado, con un poema y una imagen de margaritas.
    """
    # Poema proporcionado
    poema = (
        "Siento que no hay palabras, para que expresen el que tanto me has tocado, "
        "no hablo físicamente, sino emocionalmente una parte de mí se siente tan feliz de conocerte, "
        "de saber que existes en el mismo momento que yo, de saber que estás en algún lugar de este pequeño planeta, "
        "riendo, sonriendo, siendo tú con esa actitud que me dejó loco desde el primer instante en que te conocí, "
        "es raro, porque aún sin besarte, viéndote distante, te siento cercana, te siento conectada a mí, "
        "eres cómo ese destino y propósito que debo cumplir, porque sin ti no habría sentido, "
        "qué razón tendría yo de vivir? Qué razón tendría yo de tener a alguien más? "
        "Si la persona que tanto he buscado ya la encontré."
    )
    
    # Crear el embed con tono delicado y color verde
    embed = discord.Embed(
        title="Versos del Alma",
        description=poema,
        color=0x32CD32  # Verde lima
    )
    embed.set_footer(text="Que cada palabra te acerque a la esencia del amor.")
    
    # Establece la imagen usando el enlace proporcionado
    embed.set_image(url="https://plus.unsplash.com/premium_photo-1667867937010-77fd5161cf8d?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    
    await ctx.send(embed=embed)




bot.run('')