#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nIam MusicPlayer 2.0 which plays music in Channels and Groups 24*7</b>"
HELP = """

<b>Thêm bot và tài khoản Người dùng trong Nhóm của bạn với quyền quản trị.

Bắt đầu trò chuyện thoại.

Sử dụng /play <song name> hoặc dùng /play dưới dạng phản hồi cho tệp âm thanh hoặc liên kết youtube.

/cplay <channel username or channel id> to play music from a telegram channel.</b>

**Common Commands**:

**/play** Trả lời tệp âm thanh hoặc liên kết YouTube để phát hoặc sử dụng /play <song name>.
**/player**  Show current playing song.
**/help** Show help for commands
**/playlist** Shows the playlist.

**Admin Commands**:
**/skip** [n] ...  Skip current or n where n >= 2
**/join**  Join voice chat.
**/leave**  Leave current voice chat
**/shuffle** Shuffle Playlist.
**/cplay** Play music from a channel's music files.
**/vc**  Check which VC is joined.
**/stop**  Stop playing.
**/radio** Start Radio.
**/stopradio** Stops Radio Stream.
**/clearplaylist** Clear the playlist.
**/replay**  Play from the beginning.
**/clean** Remove unused RAW PCM files.
**/pause** Pause playing.
**/resume** Resume playing.
**/volume** Change volume(0-200).
**/off**  Mute in VC.
**/on**  Unmute in VC.
**/restart**  Update and restarts the Bot.
"""




@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
#        [
#        InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/subin_works'),
#        InlineKeyboardButton('🤖 Other Bots', url='https://t.me/subin_works/122'),
#    ],
    [
        InlineKeyboardButton('👨🏼‍💻 Admin', url='https://t.me/owohub'),
    ],
    [
        InlineKeyboardButton('👨🏼‍🦯 Help', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
 #       [
 #           InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/subin_works'),
  #          InlineKeyboardButton('🤖 Other Bots', url='https://t.me/subin_works/122'),
 #       ],
        [
 #           InlineKeyboardButton('👨🏼‍💻 Developer', url='https://t.me/subinps'),
          InlineKeyboardButton('👨🏼‍💻 Admin', url='https://t.me/owohub'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await mp.delete(message)
