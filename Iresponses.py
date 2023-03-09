import random, string
import MemePy

def handle_response(message) -> str:
    p_message = message.lower()

    packs = ('stop','ask me who ligma is','you will never get to to see the milk :(','You like school so much boy the only reason you go to school everyday is because Tyler the Creator is your lunch lady','Yo dog got sponsored by Gfuel nigwga', 'are you adopted?', 'i get it you want see your father again isnt it')
    
    if p_message == 'hi':
        return 'hello.'
    
    if p_message == 'dice':
        return str(random.randint(1,69))
    
    if p_message == 'ihelp':
        return "`hi, dice, im depressed, amogus, /roast`"
    
    if p_message == 'im depressed':
        return 'i know how to fix it! KYS!! 🤗'
    
    if p_message == 'amogus' or p_message == 'amongus':
        return 'STOP SAYING AMOGUS ITS NOT FUNNY'
    
    if p_message == '<@483253937814896657>':
        return str(random.choice(packs))
    if p_message == 'roast':
        return str(random.choice(packs))
    if p_message == 'meme':
        return MemePy.MemeGenerator
    