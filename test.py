from main import parse_mentions

print(parse_mentions({'message_id': 108, 'date': 1537364826, 'chat': {'id': -300366502, 'type': 'group', 'title': 'Split with Bot TEST', 'all_members_are_administrators': True}, 'text': '/add пицца 800 @rkhozinov @bronfirstring', 'entities': [{'type': 'bot_command', 'offset': 0, 'length': 4}, {'type': 'mention', 'offset': 15, 'length': 10}, {'type': 'mention', 'offset': 26, 'length': 14}], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 80166687, 'first_name': 'Никита', 'is_bot': False, 'last_name': 'Белоногов', 'username': 'meowmeowmeowpewpewpew', 'language_code': 'en-RU'}}))