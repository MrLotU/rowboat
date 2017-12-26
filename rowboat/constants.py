import re
from disco.types.user import GameType, Status

# Emojis
GREEN_TICK_EMOJI_ID = 347005603828334592
RED_TICK_EMOJI_ID = 347004829723525130
GREEN_TICK_EMOJI = 'green_tick:{}'.format(GREEN_TICK_EMOJI_ID)
RED_TICK_EMOJI = 'red_tick:{}'.format(RED_TICK_EMOJI_ID)
STAR_EMOJI = u'\U00002B50'
STATUS_EMOJI = {
    Status.ONLINE: ':status_online:346247554188574720',
    Status.IDLE: ':status_idle:346247554104557569',
    Status.DND: ':status_dnd:346247553773469697',
    Status.OFFLINE: ':status_offline:346247554167603220',
    GameType.STREAMING: ':status_streaming:347004585329688576',
}


# Regexes
INVITE_LINK_RE = re.compile(r'(discordapp.com/invite|discord.me|discord.gg)(?:/#)?(?:/invite)?/([a-z0-9\-]+)', re.I)
URL_RE = re.compile(r'(https?://[^\s]+)')
USER_MENTION_RE = re.compile('<@!?([0-9]+)>')

# IDs and such
ROWBOAT_GUILD_ID = 311878403986817026
ROWBOAT_USER_ROLE_ID = 351381732345511937

# Discord Error codes
ERR_UNKNOWN_MESSAGE = 10008

# Etc
YEAR_IN_SEC = 60 * 60 * 24 * 365
CDN_URL = 'https://twemoji.maxcdn.com/2/72x72/{}.png'

# Loaded from files
with open('data/badwords.txt', 'r') as f:
    BAD_WORDS = f.readlines()
