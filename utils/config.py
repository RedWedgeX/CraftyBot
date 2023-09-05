# # ----------- PROD GC SERVER ---------
# NOTES = 940626997011431444  # Admin notes channel - for logging role updates
# WELCOMECHAN = 945443742612062298  # channel for welcome messages.
# TIMEOUTCHAN = 945444169978093609  # timeout channel
# DELETEDMSGLOG = NOTES
# RULES = 904889634172051478
# ROLE_CHANNEL = 945445810882084874
# # --------------------------------------
#
#------------ REDWEDGE DEV TEST SERVER ---------
NOTES = 993271890116358194  # Admin notes channel - for logging role updates
WELCOMECHAN = 993271888660938796  # channel for welcome messages.
TIMEOUTCHAN = 993271889332015139 # timeout channel
DELETEDMSGLOG = NOTES
RULES = 993271888660938794
ROLE_CHANNEL = 993271889101344879
# ---------------------------------------------

SYSLOG = NOTES
MOD_ACTIONS_CHANNEL_ID = SYSLOG

DB_PATH = "db/db.sqlite"

restricted = "airlock"
staff = "modmin"
mods = "modmin"
TIMEOUT_ROLE_NAME = "timeout"

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
