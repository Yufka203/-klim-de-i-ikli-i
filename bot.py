import discord
from discord.ext import commands
import random
import os


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name="Bana_bir_fikir_ver")
async def Bana_bir_fikir_ver(ctx):
         Fikirler = [
        "Evde Sıfır Atık Projeleri: Plastik kullanımını azaltmaya yönelik DIY projeler.",
        "Kompost Yapımı: Evde kolayca kompost yapma rehberi.",
        "Geri Dönüşüm Doğruları ve Mitleri: Geri dönüşümde yapılan hatalar.",
        "Enerji Verimliliği: Elektrik ve su tasarrufu için ipuçları.",
        "Minimalist Yaşam: Daha az tüketerek çevreye nasıl katkı sağlanır?",
        "Plastik Alternatifleri: Günlük hayatta plastik yerine kullanılabilecek ürünler.",
        "Evde Organik Ürünler Yetiştirme: Balkon veya küçük bahçelerde bitki yetiştirme.",
        "Doğal Temizlik Ürünleri Yapımı: Kimyasal içermeyen temizlik malzemeleri hazırlama.",
        "Kapsül Gardırop Oluşturma: Daha az kıyafetle sürdürülebilir bir stil yaratma.",
        "Toplu Taşıma Kullanımı: Karbon ayak izini azaltmak için etkili yollar.",
        "Eko-Turizm: Çevre dostu seyahat rehberi.",
        "İklim Krizi Hakkında Bilgi: Basit ve anlaşılır şekilde küresel ısınma.",
        "Çevreci Girişimcilerle Röportajlar: İlham veren hikayeler.",
        "Yenilenebilir Enerji Kaynakları: Güneş panelleri ve rüzgar türbinleri nasıl çalışır?",
        "Kendi Sabununuzu Yapın: Evde doğal sabun yapımı.",
        "İkinci El Alışveriş: Neden ve nasıl yapılmalı?",
        "Doğal Güzellik Ürünleri: Cilt bakımında kimyasallardan kaçınma.",
        "Su Tasarrufu Teknikleri: Musluklardan damlayan damlaları nasıl önleriz?",
        "Karbon Ayak İzini Ölçme: Pratik bir rehber.",
        "Plastik Poşet Alternatifleri: Kumaş çanta yapımı.",
        "Yerel Pazarlardan Alışveriş: Hem çevre dostu hem de ekonomik.",
        "Doğal Çocuk Oyuncakları Yapımı: Evde geri dönüştürülebilir malzemelerle.",
        "Bisiklet Kullanımı: Çevreye etkisi ve faydaları.",
        "Eko-Evler ve Mimarisi: Enerji verimli evlerin avantajları.",
        "Sürdürülebilir Balık Tüketimi: Deniz kaynaklarını koruma yolları."
    ]
 await ctx.send(f"İşte bir el işi fikri: {random.choice(Fikirler)}")

@bot.event
async def on_ready():
    print(f'{bot.user} a giriş yapıldı!')


@bot.command(name="Bana_bir_mem_yarat")
async def Bana_bir_mem_yarat(ctx):
    try:
        img_name = random.choice(os.listdir('images'))
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)  
    except FileNotFoundError:
        await ctx.send("Görseller için 'images' klasörünü bulamadım!")
    except Exception as e:
        await ctx.send(f"Bir hata oluştu: {e}")

bot.run("token")
