class BotMessage:
    def __init__(self):
        self.test_msg_channel = "Test msg channel uniquement réussi!"
        fail_msg_welcome = [
            "Tu n'as mentionné personne!",
            "Réessaie en tapant la commande suivante:",
            "`!bienvenue @pseudo`"
            ]
        self.welcome_msg_failed = "\n".join(fail_msg_welcome)
        msg_clear = [
            "Tu n'as pas précis un nombre de message à néttoyer",
            "Réessaie en tapant la commande suivante:",
            "`!clear 10`"
            ]
        self.clear_msg = "\n".join(msg_clear)
        self.clear_msg_failed = "Tu n'as pas la permission `Gérer les messages`."
        url_emoji = [
            "Voici le lien du site d'émoji:",
            "https://emojikeyboard.top/fr/"
            ]
        self.emoji_url = "\n".join(url_emoji)
        all_commands = [
            "!bienvenue + @pseudo",
            "!clear + nombre(exemple: 5)"
            "/test",
            "/warnguy + pseudo",
            "/banguy + pseudo",
            "/emoji"
            ]
        self.all_commands_msg = "\n".join(all_commands)
        self.all_commands_msg_failed = ""

    def start_bot_msg(self, bot_user: str) -> str:
        return f"Bot allumé ! Connecté en tant que {bot_user}"

    def welcome_msg(self, pseudo: str) -> str:
        return f"Bienvenue à toi: {pseudo} 🥳"
