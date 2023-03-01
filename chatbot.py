import bot, user_input


print('Welcome to ' + bot.program_name)

print('Type "STOP" to end. ')
 
user_input.ask_question('How was your day?')



while True:
    bot_response = bot.general_computer_response()
    response = user_input.ask_question(bot_response)
    if response.upper() == 'STOP':
        break

print(' Thank for the intersting conversation! ')