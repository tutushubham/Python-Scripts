from random import randint
#------------------------------Part1--------------------------------
Marvel_LIST = ["Ant Man","War Machine"]
Marvel_BIOGRAPHY = {"ant man":"Ant-Man is a legacy super-hero name, primarily associated with the ability to shrink in size. Former thief Scott Lang once stole an advanced size-altering suit in order to aid his ailing daughter, only to discover that the stolen tech belonged to the world-renowned Dr. Hank Pym. Seeing the heroic potential within him, Dr. Pym allowed Scott to continue using the suit, as well as the identity Pym once battled evil under. As the Astonishing Ant-Man, Scott now handles the jobs too small for any other Super Hero.",
"war machine" : "Colonel James Rupert Rhodes, commonly known as Rhodey, is the officer of the United States Air Force. He is the best friend of Tony Stark and the liaison between Stark Industries and the military in the Department of Acquisitions."}
Marvel_FACT = {"ant man":["When Paul Rudd told his nine-year old son that he was playing the titular character in Ant-Man, he responded with, Wow, I can’t wait to see how stupid that’ll be.","Rudd got in such good shape that they had to alter the Ant-Man costume to account for his new physique.","In the comics, Hank Pym is actually the one who creates Ultron. Of course, Tony Stark does so in the movies because, y’know, drama."],
"war machine":["IN AN EARLY DRAFT OF THE FIRST IRON MAN MOVIE, TONY'S FATHER HOWARD STARK WAS THE MAIN VILLAIN, CALLING HIMSELF WAR MACHINE","DON CHEADLE TOOK ANTI-ANXIETY MEDICATION TO WEAR THE WAR MACHINE SUIT","JAMES RHODES ORIGINALLY MET TONY STARK DURING THE VIETNAM WAR"]
}
#------------------------------Part2--------------------------------
def lambda_handler(event, context):
    if event['session']['new']:
        on_start()
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event)
    elif event['request']['type'] == "IntentRequest":
        return intent_scheme(event)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_end()
#------------------------------Part3--------------------------------
def on_start():
    print("Session Started.")
def on_launch(event):
    onlunch_MSG = "Hi, welcome to the Alexa Skill. My favourite marvel characters are: " + ', '.join(map(str, Marvel_LIST)) + ". "\
    "If you would like to hear more about a particular character or a fact related to it, you could say for example: tell me about Ant Man? or give me a fact on Ant Man "
    reprompt_MSG = "Do you want to hear more about a particular marvel character?"
    card_TEXT = "Pick a marvel."
    card_TITLE = "Choose a marvel."
    return output_json_builder_with_reprompt_and_card(onlunch_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
def on_end():
    print("Session Ended.")
#-----------------------------Part3.1-------------------------------
def intent_scheme(event):
    
    intent_name = event['request']['intent']['name']
    if intent_name == "marvelBio":
        return marvel_bio(event) 
    elif intent_name == "marvelFacts":
        return marvel_fact(event) 
    elif intent_name in ["AMAZON.NoIntent", "AMAZON.StopIntent", "AMAZON.CancelIntent"]:
        return stop_the_skill(event)
    elif intent_name == "AMAZON.HelpIntent":
        return assistance(event)
    elif intent_name == "AMAZON.FallbackIntent":
        return fallback_call(event)
#---------------------------Part3.1.1-------------------------------
def marvel_bio(event):
    name=event['request']['intent']['slots']['marvel']['value']
    marvel_list_lower=[w.lower() for w in Marvel_LIST]
    if name.lower() in marvel_list_lower:
        reprompt_MSG = "Do you want to hear more about a particular character?"
        card_TEXT = "You've picked " + name.lower()
        card_TITLE = "You've picked " + name.lower()
        return output_json_builder_with_reprompt_and_card(Marvel_BIOGRAPHY[name.lower()], card_TEXT, card_TITLE, reprompt_MSG, False)
    else:
        wrongname_MSG = "I cannot help you with that. If you have forgotten which characters you can pick say Help."
        reprompt_MSG = "Do you want to hear more about a particular ?"
        card_TEXT = "Use the full name."
        card_TITLE = "Wrong name."
        return output_json_builder_with_reprompt_and_card(wrongname_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
        
def marvel_fact(event):
    name=event['request']['intent']['slots']['marvel']['value']
    marvel_list_lower=[w.lower() for w in Marvel_LIST]
    if name.lower() in marvel_list_lower:
        reprompt_MSG = "Do you want to hear a fact on a particular character?"
        card_TEXT = "You've picked " + name.lower()
        card_TITLE = "You've picked " + name.lower()
        return output_json_builder_with_reprompt_and_card(Marvel_FACT[name.lower()][randint(0, 2)], card_TEXT, card_TITLE, reprompt_MSG, False)
    else:
        wrongname_MSG = "I cannot help you with that. If you have forgotten which characters you can pick say Help."
        reprompt_MSG = "Do you want to hear more about a particular ?"
        card_TEXT = "Use the full name."
        card_TITLE = "Wrong name."
        return output_json_builder_with_reprompt_and_card(wrongname_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
        
def stop_the_skill(event):
    stop_MSG = "Thank you. Bye!"
    reprompt_MSG = ""
    card_TEXT = "Bye."
    card_TITLE = "Bye Bye."
    return output_json_builder_with_reprompt_and_card(stop_MSG, card_TEXT, card_TITLE, reprompt_MSG, True)
    
def assistance(event):
    assistance_MSG = "You can choose among these marvels: " + ', '.join(map(str, Marvel_LIST)) + ". Be sure to use the full name when asking about the character."
    reprompt_MSG = "Do you want to hear more about a particular marvel character?"
    card_TEXT = "You've asked for help."
    card_TITLE = "Help"
    return output_json_builder_with_reprompt_and_card(assistance_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
def fallback_call(event):
    fallback_MSG = "I can't help you with that, try rephrasing the question or ask for help by saying HELP."
    reprompt_MSG = "Do you want to hear more about a particular marvel character?"
    card_TEXT = "You've asked a wrong question."
    card_TITLE = "Wrong question."
    return output_json_builder_with_reprompt_and_card(fallback_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
#------------------------------Part4--------------------------------
def plain_text_builder(text_body):
    text_dict = {}
    text_dict['type'] = 'PlainText'
    text_dict['text'] = text_body
    return text_dict
def reprompt_builder(repr_text):
    reprompt_dict = {}
    reprompt_dict['outputSpeech'] = plain_text_builder(repr_text)
    return reprompt_dict
    
def card_builder(c_text, c_title):
    card_dict = {}
    card_dict['type'] = "Simple"
    card_dict['title'] = c_title
    card_dict['content'] = c_text
    return card_dict
def response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    speech_dict = {}
    speech_dict['outputSpeech'] = plain_text_builder(outputSpeach_text)
    speech_dict['card'] = card_builder(card_text, card_title)
    speech_dict['reprompt'] = reprompt_builder(reprompt_text)
    speech_dict['shouldEndSession'] = value
    return speech_dict
def output_json_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    response_dict = {}
    response_dict['version'] = '1.0'
    response_dict['response'] = response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value)
    return response_dict