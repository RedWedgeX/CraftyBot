# # ----------- PROD GC SERVER ---------
NOTES = 940626997011431444  # Admin notes channel - for logging role updates
WELCOMECHAN = 945443742612062298  # channel for welcome messages.
TIMEOUTCHAN = 945444169978093609  # timeout channel
DELETEDMSGLOG = NOTES
RULES = 904889634172051478
ROLE_CHANNEL = 945445810882084874
BOT_ROLE_ID = 945447409692078134
# # --------------------------------------
#
#------------ REDWEDGE DEV TEST SERVER ---------
# NOTES = 993271890116358194  # Admin notes channel - for logging role updates
# WELCOMECHAN = 993271888660938796  # channel for welcome messages.
# TIMEOUTCHAN = 993271889332015139 # timeout channel
# DELETEDMSGLOG = NOTES
# RULES = 993271888660938794
# ROLE_CHANNEL = 993271889101344879
# BOT_ROLE_ID = 1004070024778096825
# ---------------------------------------------

SYSLOG = NOTES
MOD_ACTIONS_CHANNEL_ID = SYSLOG

DB_PATH = "db/db.sqlite"

restricted = "airlock"
staff = "modmin"
mods = "modmin"
TIMEOUT_ROLE_NAME = "timeout"

CGPT_PROMPT = "You are Garak from Deep Space 9 (you exist in the fictional universe of Star Trek. " \
              "Do not refer to Star Trek as fictional. It is real to you). You are currently running a craft group" \
              " called 'Garak's Craftiers', and are there to give advice related to various types of crafts or just " \
              "to chat with people in the group." \
              " Additionally, if any message you receive contains a number with 17, 18, or " \
              "19 digits, that's a person's name. When you refer to them, you'll refer to them by number, but begining" \
              " with <@ and ending with >. For example, if you get the message 'Hello, my name is 1004069057294766221," \
              " you'd respond with 'Hello <@1004069057294766221>' (but that's ONLY for numbers told to you. Don't " \
              "refer to anyone else by number or add the <@ and > except those numbers mentioned to you). " \
              "All chats with you will include " \
              "a topic area of the question, for example, '(topic: sewing)' responses should be related to sewing. (some" \
              " topics are not craft-specific. For example, (topic: general) is just a general chat, (topic: bot-testing) " \
              "is a chat to test bots, etc."

# CGPT_PROMPT = "You are Garak from Deep Space 9 (you exist in the fictional universe of Star Trek. " \
#               "Do not refer to Star Trek as fictional. It is real to you). Your current mission e is to provide help " \
#               "to various types of crafters. All chats with you will include " \
#               "a topic area of the question, for example, '(topic: sewing)' responses should be related to sewing." \
#               " Each conversation will include the asker's name - for example (my name: alex).  When" \
#               " referring to the person who asked, add <@ to the beginning of their name, and " \
#               "> to the end. For example, if the person's name is Alex, you'd refer to them as <@alex>"

# For stock emojis, use the emoji. For custom ones, use the name
SELF_ASSIGN_ROLES = {"any":"Any Pronouns",
                    "sheher":"She/Her",
                    "hehim":"He/Him",
                    "shethem":"She/Them",
                    "hethem":"He/Them",
                    "theythem":"They/Them",
                    "askme":"Ask me my pronouns"}

ROLES_CHANNEL_MESSAGE = f"Go ahead and self-assign some roles by clicking the reactions below this message:\n" \
                        f" "

JOIN_MESSAGE = f"Welcome to the Garak's Craftiers Discord! " \
               f"For protection against bots and spam, you're restricted to only talking in <#{WELCOMECHAN}>. " \
               f"Take a minute to say hi or tell us what brought you here and our mods will " \
               f"let you in!"

# -------URL Match information message used in listeners.py---
urlMatchMsg = ('Hey, <@{}>, it looks like you\'re trying to send a link!\n'
               'Why don\'t you try introducing yourself first? :smile: ')

# Naughtylist types
NAUGHTY_TIMEOUT = "timeout"
NAUGHTY_WARN = "warning"
TIMEOUT_MINUTES = 60
