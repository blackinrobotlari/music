# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from DaisyXMusic.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "**Salam 🤓 [{}](tg://user?id={})!**\n\n🤖 Mən Telegram Qrupları və Kanallarının səsli söhbətlərində musiqi oxumaq üçün yaradılmış təkmil botam.\n\n✅ Əlavə məlumat üçün mənə /help'yazın 🤓"
    HELP_MSG = [
        ".",
        f"""
**Salam 🤓 Yenidən xoş gəlmisiniz {PROJECT_NAME}

🤓 {PROJECT_NAME} qrupunuzun səsli söhbətində, eləcə də kanal səsli söhbətlərində musiqi oxuya bilər

🤓 Assistanın adı >> @{ASSISTANT_NAME}\n\nC təlimatlar üçün növbətiyə keçin**
""",
        f"""
**🤓Ayarlar**

1) Bot admini olun (cplay istifadə edirsinizsə qrupda və kanalda)
2) Səsli söhbətə başlayın
3) İlk dəfə admin tərəfindən [mahnı adı] oynamağa cəhd edin
*) İstifadəçi robotu qoşulubsa, musiqidən həzz alın, yoxsa əlavə edin @{ASSISTANT_NAME} qrupunuza daxil olun və yenidən cəhd edin

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group
""",
        f"""
**🤓Əmirlər**

**🤓 Mahnı Ayarları **

- /play: İstədiyiniz mahnını səsləndirin
- /play [yt url] : Verilmiş yt url-ni çalın
- /play [reply yo audio]: Cavab verilmiş audionu oxudun
- /splay: Jio saavn vasitəsilə mahnı oxuyun
- /ytplay: Youtube Music vasitəsilə birbaşa mahnı oxuyun

**🤓 Oynatma**

- /player: Pleyerin Parametrlər menyusunu açın
- /skip: Cari treki keçir
- /pause: Trası dayandırın
- /resume: Dayandırılmış treki davam etdirir
- /end: Media oxutmağı dayandırır
- /mute: səssiz mahnı ifa
- /unmute: mahnının səsini açın
- /current: Cari ifa olunan treki göstərir
- /playlist: Pleylist göstərir

*Player cmd və /play istisna olmaqla, bütün digər cmdlər, /current  və /playlist  yalnız qrupun adminləri üçündür.
""",
        f"""
**=>> Kanal Musiqi Oynamaq 🛠**

🤓 For linked group admins only:

- /cplay [song name] - play song you requested
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /cmute - mute song play
- /mute - mute song play
- /unmute - mute song play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

🤓 Əlaqəli qrupda oynamaq istəmirsinizsə:

1) Kanal ID-nizi əldə edin.
2) Başlığı olan qrup yaradın: Kanal Musiqisi: kanal identifikatorunuz
3) Botu tam icazələrlə Kanal admini olaraq əlavə edin
4) Eklə @{ASSISTANT_NAME} kanala admin kimi.
5) Qrupunuzda sadəcə əmrlər göndərin. (əvəzinə /ytplay /play istifadə etməyi unutmayın)
""",
        f"""
**🤓 Daha çox alət**

- /musicplayer [on/off]: Musiqi pleyeri aktivləşdirin/deaktiv edin
- /admincache: Qrupunuzun admin məlumatını yeniləyir. Əgər bot admini tanımırsa, cəhd edin
- /userbotjoin: dəvət et @{ASSISTANT_NAME} Söhbətinizə istifadəçi robotu
""",
        f"""
**🤓 Mahnı Yüklə**

- /video [mahnı mame]: Youtube-dan video mahnı yükləyin
- /song [mahnının adı]: Youtube-dan audio mahnı yükləyin
- /saavn [mahnının adı]: Saavn-dan mahnı yükləmək
- /deezer [mahnının adı]: Deezer-dən mahnı yükləmək

**🤓 Axtarış alətləri**

- /search [mahnı adı]: mahnıları youtube-da axtarın
- /lyrics [mahnı adı]: mahnı sözlərini əldə edin
""",
        f"""
**🤓 Sudo İstifadəçiləri üçün əmrlər**

 - /userbotleaveall - köməkçini bütün söhbətlərdən çıxarın
 - /broadcast <mesaja cavab vermək> - bütün çatlara qlobal yayımlanan cavab mesajı
 - /pmpermit [on/off] - pmpermit mesajını aktivləşdir/deaktiv et
*Sudo İstifadəçiləri istənilən qrupda istənilən əmri yerinə yetirə bilərlər

""",
    ]
