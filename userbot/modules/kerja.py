import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern='^.unredflag(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("UNTUK DI INGAT SAJA\nBUAT YANG BLM TAU BERAPA LAMA PROSES UNREDFLAG ."
f"\n\nBIASANYA PALING CEPAT ADALAH 1 MALAM DAN PALING LAMA ADALAH 1 - 3 HARI\nTHANKS BOSQU")

@register(outgoing=True, pattern='^.whm(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Berikut Adalah List Harga dari **WHM** \n"
			 f"Whm Mini      : **30.000 / 1 Month**\n"
			 f"Whm Medium : **40.000 / 1 Month**\n"
			 f"Whm Extra     : **50.000 / 1 Month**\n"
			 f"Whm Extra     : **60.000 / 1 Month**\n"
			 f"Dukung saya dengan cara join di channel saya! [klik disini](http://t.me/Jejakcheat14)")
	
@register(outgoing=True, pattern='^.proses(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("OK, Saya Akan Mengirimkan result dengan cara LIVE. Jadi nnti kalau sudah proses atau sudah giliranmu akan saya beritahu ~ Terimakasih \n"
			 f"Info Lebih Lanjut! [klik disini](http://t.me/Jejakcheat14)")

@register(outgoing=True, pattern='^.result(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Berikut Adalah List Harga dari **LIVE RESULT** \n"
			 f"100.000 => Mendapatkan **20 Result**\n"
			 f"150.000 => Mendapatkan **30 Result**\n"
			 f"200.000 => Mendapatkan **50 Result**\n"
			 f"400.000 => Mendapatkan **100 Result**\n"
			 f"Info Lebih Lanjut! [klik disini](http://t.me/Jejakcheat14)")


@register(outgoing=True, pattern='^.full(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Mohon Maaf, Untuk sekarang result live **FULL** \n"
			 f"Info Lebih Lanjut! [klik disini](http://t.me/Jejakcheat14)")


@register(outgoing=True, pattern='^.jual(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("OPEN WEBSITE PHISING\n"
			f"M.WHM, WHM, CPANEL\n"
			 f"\n\n`Send email lancar\nada SSL atau gembok ijo\nBisa request tampilan\nDan masih banyak lagi!!`\n\nHarga?\n\nDomain : Rp. 150.000 `Bisa Request Nama Web`"
			 f"Domain : Rp. 70.000 `Tidak bisa request nama web alias yang nentuin penjual`\n"
			 f"Subdomain : Rp. 20.000 `Tidak bisa request apapun kecuali request tampilan website`\n\n"
			 f"Payment via : BCA, OVO, TELKOMSEL\n"
			 f"Mau lihat tampilan web ? Yuk ke demo [klik di sini](https://senturypanel.com/)\n\n"
			 f"Chat ? [Jefanya Efandchris](http://t.me/Jejakcheat)\n"
			 f"Join channel telegram yuk! [klik disini](http://t.me/Jejakcheat14)")


@register(outgoing=True, pattern='^.demo(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Untuk melihat tampilan yang di inginkan\n Silahkan cek`\n [Disini](https://senturypanel.com) \n#SenturyBot")


# Create by myself @JejakCheat

@register(outgoing=True, pattern='^.sibuk(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Sebentar Ya Gan`")
	sleep(2)
	await typew.edit("`Masih Ngecek`")
	sleep(1)
	await typew.edit("`Oh Ternyata Jefa Masih sibuk... Tunggu sebentar nanti akan dibaca \n#SenturyBot`")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.o(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Maaf baru online, ada apa bos?` \n#SenturyBot")
	
	# Create by myself @JejakCheat


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.perbedaan(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Saya jelaskan untuk perbedaan domain dan subdomain .\n\nDomain (pubg.com) *langsung tidak ada tambahan sama sekali\n\nSubdomain ( blablabla.pubg.com ) *ada Tambahan di depan domainnya .\n\nBot By : [#Jefanya](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.bca(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`BCA : `0901316839 `A/N PILU EFENDI` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.tsel(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`TELKOMSEL : `082247870713 `A/N -` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.bni(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`BNI : `0830301026 `A/N Jefanya Efandchris` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.ovo(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`OVO : `082247870713 `A/N NI KETUT SUERTI` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")

# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.danaj(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`DANA : `085320064310 `A/N Sutri nanda` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")

# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.bcaj(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`BCA : `3030634780 `A/N Sutri nanda` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \n[#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.dana(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`DANA : `082247870713` A/N Jefanya Efandchris` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.data(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Kirim Email + Tampilan yang sudah di request di atas` (Sesuai nama di demo.senturypanel.xyz) \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.harga(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`UPDATE HARGA HARI INI` \n\nDOMAIN : 150.000 (Bisa Request Nama Web)\nSUBDOMAIN : 20.000 (SELAIN PULSA) \nSUBDOMAIN : 25.000 (Via Pulsa) \n\nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.bug(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`JIKA ADA ERROR ATAU BUG DI TAMPILAN PHISING KALIAN TINGGAL SURUH TEMAN KALIAN UNTUK MEMBUKA WEB KALIAN ITU \n\nSyarat : \n1. BEDA HP \n2. BEDA SINYAL \n3. BELUM PERNAH BUKA WEB ITU`\nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.exp(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("**EXP TIME !!** \nMaaf bos, phising saya matikan atau saya alihkan ke `exp.senturypanel.xyz` \nDikarenakan Sudah melewati tanggal kadaluarsa \nDan jika mau perpanjang silahkan balas pesan ini dengan **Yes** \nDan jika tidak mau perpanjang silahkan balas **No** \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
CMD_HELP.update({
    "done":
    "`.domainanim` = `DOMAIN` PUBG Mobile Season 12 `Animation Version`\n"
    "`.domaintourney` = `DOMAIN` PUBG Mobile Season 12 `Tournament`\n"
    "`.subdomainanim` = `SUBDOMAIN` PUBG Mobile Season 12 `Animation Version`"
    "`.subdomaintourney` = `SUBDOMAIN` PUBG Mobile Season 12 `Tournament`"
    "`.subdomainbokep1` = `SUBDOMAIN` Facebok Bokep `V1`"
    
})

