import discord
import time
from discord.ext import commands as cmd
import asyncio
import myModule
import functools
import itertools
import math
import random
import youtube_dl
from async_timeout import timeout

"""#prerequisite code for voice functions
class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass

class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)"""

insultList = ["I???ve never, ever, ever met someone I believe in as little as you!",
"This fish is so raw it's still trying to find Nemo!",
"There???s enough garlic in here to kill every vampire in Europe!",
"Why did the chicken cross the road? Cause thats how it escaped out of this restaurant, thats how fucking raw this is!",
"You cook like old people fuck!",
"This crab is so undercooked I can still hear it singing 'Under the Sea'!",
"You're a first class cunt",
"This lamb is so underdone a skilled vetrinarian could still save it!",
"I wouldn???t trust you running a bath, let alone a fucking restaurant!",
"You're a fucking disgrace...",
"This has so much oil in it America wants to invade the fucking plate!",
"You wanna see my asshole? You can watch me walk out of the door of this fucking dump!",
"Chimichanga? More like chimi-chuck-it-in-the-bin!",
"You fucking donut!",
"It's not as if you're the captain of the Titanic... You're the fucking iceberg!",
"This beef is so frozen it is singing 'Let It Go'!",
"You put so much ginger in this it???s a Weasley!",
"You fucking donkey",
"Fuck off you piece of fucking yankie dankie doodle shite, fuck off will you please yeah?",
"Right, well I???ll get you your pumpkin, and I???ll ram it up your fucking ass, would you like it whole or diced?",
"Don???t whistle at me I???m not your fucking dog, you look like more of a dog than I do!",
"This bread pudding tastes like I already threw it up out of my arse!",
"Is your brains in your fucking arse? Is your brains in your fucking arse?",
"That looks like it had a thousand buffaloes walk over it!",
"You stuck up precious little bitch...",
"My Gran could do it better, and she???s dead!",
"THIS SQUID IS SO RAW I CAN STILL HEAR IT TELLING SPONGEBOB TO FUCK OFF!",
"Your breaded cod tastes more like a breaded condom!",
"For what we are about to eat, may the Lord make us truly not vomit",
"This pasta is more limp than my grandfather???s dick!"]

recipieList = ["https://www.gordonramsay.com/gr/recipes/pork-stuffed-with-manchego-and-membrillo/",
"https://www.gordonramsay.com/gr/recipes/roast-beef-with-caramelised-onion-gravy/",
"https://www.gordonramsay.com/gr/recipes/bakedchickenwings/",
"https://www.gordonramsay.com/gr/recipes/stuffed-lamb-with-spinach-and-pine-nuts/",
"https://www.gordonramsay.com/gr/recipes/candiedchickpeasnackmix/",
"https://www.gordonramsay.com/gr/recipes/frenchlentilswithlabneh/",
"https://www.gordonramsay.com/gr/recipes/harissatoast/",
"https://www.gordonramsay.com/gr/recipes/barleyrisotto/",
"https://www.gordonramsay.com/gr/recipes/buttermilkbiscuit/",
"https://www.gordonramsay.com/gr/recipes/mojochickenquinoabowl/",
"https://www.gordonramsay.com/gr/recipes/gingerbreadbundtcake/",
"https://www.gordonramsay.com/gr/recipes/holidaystuffing/",
"https://www.gordonramsay.com/gr/recipes/stickytoffee-pudding/",
"***You are not worthy!***"
]

PolishCow1 = """Tylko jedno w g??owie mam
koksu pi???? gram odlecie?? sam
W krain?? za zapomnienia
W g??owie my??li mam
kiedy sko??czy si?? ten stan
Gdy ju?? nie b??d?? sam
Bo wjedzie bia??y w??gorz

Tylko jedno w g??owie mam
koksu pi???? gram odlecie?? sam
W krain?? za zapomnienia
W g??owie my??li mam
kiedy sko??czy si?? ten stan
Gdy ju?? nie b??d?? sam
Bo wjedzie bia??y w??gorz

Ja pierdole mam zjazd
nie chwytam gwiazd
jak k??oda le??e
nie wierze co si?? dzieje
jak kura z g??odu pieje
jak wilko??ak do ksi????yca
W g??owie dziury jak ulica
przed twoj?? chat??
rozpuszczam si?? jak baton
kt??ry le??y na blacie
zej???? jest jak nie wci??gacie
bracie kurwa ryj mi krzywi
w g??owie burdel jak w TV
Mnie nie dziwi taki stan
brak towar,w my??lach ??pam
rade dam albo nie dam
wszystko kurwa z chaty sprzedam
w sumie mam ju?? przejebane
wszystko jednak jest sprzedane
Ja pierdole same d??ugi
kinol jak u tabalugi
dzie?? drugi bez walenia
gdzie jest w???? ? bia??a chemia.
Jebane zej??cie tak wyka??cza
jak by w chuja dziab??a ci?? szara??cza

Tylko jedno w g??owie mam
koksu pi???? gram odlecie?? sam
W krain?? za zapomnienia
W g??owie my??li mam
kiedy sko??czy si?? ten stan
Gdy ju?? nie b??d?? sam
Bo wjedzie bia??y w??gorz"""

PolishCow2 = """Chemia party chce na narty
do dilera a nie w alpy.
O ??esz kurwa chyba fikn??
jak w nochala nic nie psike.
Tak bardzo chce dotyka?? gwiazd
ale nic z tego bo mam zjazd
totalne kurwa mega zej??cie
a marzy mi si?? smoka wej??cie.
Masz hajsy ? ci te?? zalegam ?
no to chuj dzi?? ju?? nie biegam.
Chce mie?? kopa jak pantera
w krech?? nie ma u dilera.
ju?? nie na pewno nie
chyba ??mier?? rozk??ada mnie.
Nic nie prze??kn?? mam dreszcze
kurwa ma?? ile jeszcze ?
b??dzie trwa?? ten stan
??ni?? mi si?? koksu van
i hery gram tak do smaku
chce si?? wozi?? w cadillacu
My??lami po znajomych biegam
lecz ka??demu co?? zalegam
odpada opcja po??yczki
bo przycinam jak no??yczki.

Tylko jedno w g??owie mam
koksu pi???? gram odlecie?? sam
W krain?? za zapomnienia
W g??owie my??li mam
kiedy sko??czy si?? ten stan
Gdy ju?? nie b??d?? sam
Bo wjedzie bia??y w??gorz"""

PolishCow3 = """Syf jak na Discovery
chce wystrzeli?? jak z giwery
chce hery i inne bajery
w nosie pustak s??ycha?? szmery.
Macie numer do gargamela ?
mo??e u niego w kotle jest hera ?
wiem g??upoty pierdole
ale nie ma nic na stole
a kieszeni jebana pustka
przyda??a by si?? w totka sz??stka
albo chocia?? jaka?? czw??rka
i bym lecia?? jak jask????ka
jak pszcz????ka maja
do ucha ??piewa??a by mi kaja
to s?? jaj no nie wierze
wygi??ty le??e jak zdech??e zwierze
Gor??czka w kurw?? si?? nasila
poharatany jak dupa fakira
jak zdzira wymi??tolony
le??e kurwa rozpalony.
hej Johny chcia??bym posypa??
i na ????ce jak kr??lik bryka??
Ale ca??y czas ten zjazd
usycham jak wyrwany chwast

Tylko jedno w g??owie mam
koksu pi???? gram odlecie?? sam
W krain?? za zapomnienia
W g??owie my??li mam
kiedy sko??czy si?? ten stan
Gdy ju?? nie b??d?? sam
Bo wjedzie bia??y w??gorz"""

#default prefix
client = cmd.Bot(command_prefix= "Hatta! ", case_insensitive=True)

#time at start
ordSuf = myModule.ordSuffix(time.strftime("%b"))
tijd = time.strftime("%A the %d" + ordSuf + " of %B, at %I:%M%p, GMT%z")

#ready message
@client.event
async def on_ready():
    #channel = client.get_channel(cmdBot)
    tijd = time.strftime("%A, %B %d, at %I:%M%p GMT%z")
    await client.change_presence(activity=discord.Game(name="Hatta!"))
    msg = str("Hatta came online on "+ tijd)
    #await channel.send(msg)
    print("Connection established on", tijd)


#uptime
@client.command(brief = "Shows time since application launch")
async def Uptime(ctx):
    msg = str("Bung, I've been awake since " + tijd)
    await ctx.send(msg)

#ping
@client.command(brief = "Shows ping between bot host and server")
async def Ping(ctx):
    lag = str(round(client.latency*100))
    msg = str("My ping is " + lag + "ms, bung")
    await ctx.send(msg)


#change prefix
@client.command(brief = "Changes bot prefix. WARNING, AFFECTS ALL SERVERS SERVED BY BOT")
async def newPrefix(ctx, prefix, brief):
    client.command_prefix = prefix
    await ctx.send(f"Your new prefix is ``{prefix}``, bung")

#new user role
"""@client.event
async def on_member_join():"""


"""#Do I x or y
@client.event
async def on_message(message):
    msg = "Hatta, do I ".casefold()
    if message.content.startswith(msg):
        channel = message.channel
        await channel.send("Test1")

        def check(m):
            return m.content == "hello" and m.channel == channel

        if myModule.randIntGen(end = 1) == 0:
            reply = "Yes"
        else:
            reply = "No"

        pLoad = await client.wait_for(reply, check=check)
        await channel.send(reply)"""

"""@classmethod
async def create_source (cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):"""

"xX_memelord69_Xx"
#Gordon Ramsay
@client.command(brief = "Commands to either roast or display a recipie. Use roast/insult or food/recipie after 'Gordon'")
async def Gordon(ctx, quoteInp, target = None):
    quote = quoteInp.casefold()

    #roasts
    if quote == "insult" or quote == "roast":
        lim = len(insultList)
        RNG = myModule.randIntGen(end = lim)
        #if target != null:
           # pass
        msg = str("***Gordon says:*** \n" + insultList[RNG])
        await ctx.send(msg)

    #recipies
    elif quote == "recipie" or quote == "recipies" or quote == 'food':
        lim = len(recipieList)
        RNG = myModule.randIntGen(end = lim)
        msg = str(recipieList[RNG])
        await ctx.send(msg)

    else:
        await ctx.send("**Gordon says: **You fucking mong, that isn't something you can ask me to do!")
#Speed meme
@client.command()
async def Alabama(ctx, message = "Sweet home *** A L A B A M A *** <@335529118240079872>"):
    await ctx.send(message)

@client.command()
async def torture(ctx, target, *msg):
    message = str(" ".join(msg[:])) + " " + target
    for count in range(200):
        await ctx.send(message)

#Polish cow
@client.command()
async def Kracow(ctx):
    await ctx.send(PolishCow1)
    await ctx.send(PolishCow2)
    await ctx.send(PolishCow3)


client.run("ODEwMTMyOTk2MjQ1OTQ2Mzc4.YCfNJQ.pn3VdQzWv942zGyohxV_20BJB10")
