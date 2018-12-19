from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url
from store import *
import json
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_name(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '名字'
        return False

    def is_going_to_category(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '分類'
        return False
    
    def is_going_to_special(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'special'
        return False
    
    def on_enter_name(self, event):
        print("entering name")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "今天想看哪位女優？")

    def on_exit_name(self,event):
        print('Leaving name')

    def on_enter_special(self, event):
        print("entering special")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "輸入密碼後可以看到作者的個人推薦")

    def on_exit_special(self,event):
        print('Leaving special')

    def is_going_to_congrats(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '狗幹大爆射'
        return False

    def on_enter_congrats(self, event):
        print("entering congrats")

        sender_id = event['sender']['id']
        send_image_url(sender_id,"https://i.imgur.com/PTpXXdq.gif")
        response = send_text_message(sender_id, "SIRO-3346\nJUFD-868\nSNIS-923\n200GANA-1120\nFC2PPV-835964\nMIDE-565\nMIDE-502\nFC2PPV-879718\n300MAAN-236\n200GANA-1802\nCarib-072018-712\n300MIUM-283\n300MIUM-161\nSDMU-866\nMIDE-580\nFSET-784\nHND-576\nHND-573\nCarib-101918-776\n261ARA-331\n300MAAN-276\nFC2PPV-962880\nKMHR-052\nABP-789\n300MAAN-313\n300MIUM-349\nTEK-097\nCaribbeancom 121418-810\nFC2PPV-884748")
        self.go_back()

    def on_exit_congrats(self):
        print('Leaving congrats')

    def on_enter_category(self, event):
        print("entering category")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "選一個喜歡的分類吧")

    def on_exit_category(self,event):
        print('Leaving category')

    def is_going_to_bigtits(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '巨乳'
        return False
        
    def on_enter_bigtits(self, event):
        print("entering bigtits")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "MIDE-540\nABP-532\nHUNTA-331\nIPX-043\nSNIS-774\nPPPD-682\nIPX-155\nSSNI-283\nYRH-149\nKMHR-052") 
        self.go_back()
        
    def on_exit_bigtits(self):
        print('Leaving bigtits')               

    def is_going_to_uncensored(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '無碼'
        return False

    def on_enter_uncensored(self, event):
        print("entering uncensored")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "Caribbeancompr 102816_005\n鈴村あいり流出\nCaribbeancom 081116-227\nあやみ旬果　無修正\nCaribbeancom 071415-920\nCarib-121914-760\nFC2-PPV 980413\nCaribbeancom 081117-477\nheydouga 4017-216-1\nCaribbeancompr 082616_002") 
        self.go_back()
        
    def on_exit_uncensored(self):
        print('Leaving uncensored')        

    def is_going_to_amateur(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '素人'
        return False
        
    def on_enter_amateur(self, event):
        print("entering amateur")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,"FC2-PPV 962880\n261ARA-331\nFC2-PPV 872873\nFC2-PPV 734790\nAVOP-335\n300MAAN-276\nFC2-PPV 967926\nFC2-PPV 419201\nFC2-PPV 739415\nGachinco gachi1151") 
        self.go_back()        

    def on_exit_amateur(self):
        print('Leaving amateur') 

    def is_going_to_wife(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '人妻'
        return False

    def on_enter_wife(self, event):
        print("entering wife")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,"SDMU-787\nSTAR-813\nSSPD-137\nEYAN-092\nSGA-093\nTIKB-015\nJUY-641\nJUFD-767\nJUY-260\nADN-187") 
        self.go_back()        

    def on_exit_wife(self):
        print('Leaving wife')

    def is_going_to_schoolgirl(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '女子校生'
        return False

    def on_enter_schoolgirl(self, event):
        print("entering schoolgirl")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,"SSNI-025\nSSNI-024\nSSNI-058\nRTP-101\nREAL-628\nSDMU-656\nDVDMS-263\nMIAE-131\nPRED-116\nMDB-847") 
        self.go_back()
        
    def on_exit_schoolgirl(self):
        print('Leaving schoolgirl')

    def is_going_to_takahashishouko(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '高橋聖子'
        return False

    def on_enter_takahashishouko(self, event):
        print("in shouko")

        sender_id = event['sender']['id']
        send_image_url(sender_id,"https://i.imgur.com/jMnjR8h.jpg")
        response = send_text_message(sender_id,"名字:Takahashi Shouko\n年齡:25\n身高:161cm\nBHW:88-59-86cm\n罩杯:G\n經紀公司:MOODYZ\n推薦番號:MIDE-551,TEK-077")

    def on_exit_takahashishouko(self,event):
        print('Leaving shouko')

    def is_going_to_takahashishouko_rand(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '隨機選片'
        return False

    def on_enter_takahashishouko_rand(self, event):
        print("in shoukorand")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,random.choice(store.takahashishouko_index))
        self.go_back()        

    def on_exit_takahashishouko_rand(self):
        print('Leaving shoukorand')

    def is_going_to_sakuramomo(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '櫻空桃'
        return False

    def on_enter_sakuramomo(self,event):
        print("in momo")
        
        sender_id = event['sender']['id']
        send_image_url(sender_id,"https://i.imgur.com/HJwBEkV.jpg")
        response = send_text_message(sender_id,"名字:Sakura Momo\n年齡:22\n身高:160cm\nBHW:90-55-86cm\n罩杯:G\n經紀公司:IdeaPocket\n推薦番號:IPZ-995")
        
    def on_exit_sakuramomo(self,event):
        print('Leaving momo')

    def is_going_to_sakuramomo_rand(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '隨機選片'
        return False

    def on_enter_sakuramomo_rand(self, event):
        print("in momorand")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,random.choice(store.sakuramomo_index))
        self.go_back()

    def on_exit_sakuramomo_rand(self):
        print('Leaving momorand')

    def is_going_to_miurasakura(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '水卜櫻'
        return False
        
    def on_enter_miurasakura(self,event):
        print("in sakura")
        
        sender_id = event['sender']['id']
        send_image_url(sender_id,"https://i.imgur.com/6Ddn9QP.jpg")
        response = send_text_message(sender_id,"名字:Miura Sakura\n年齡:21\n身高:152cm\nBHW:79-52-78cm\n罩杯:G\n經紀公司:MOODYZ\n推薦番號:MIDE-580,MIDE-515")
     
    def on_exit_miurasakura(self,event):
        print('Leaving sakura')

    def is_going_to_miurasakura_rand(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '隨機選片'
        return False

    def on_enter_miurasakura_rand(self, event):
        print("in sakurarand")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,random.choice(store.miurasakura_index))
        self.go_back()

    def on_exit_miurasakura_rand(self):
        print('Leaving sakurarand')

    def is_going_to_shinodayuu(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '篠田優'
        return False
        
    def on_enter_shinodayuu(self,event):
        print("in yuu")
        
        sender_id = event['sender']['id']
        send_image_url(sender_id,"https://i.imgur.com/Sktrdux.jpg")
        response = send_text_message(sender_id,"名字:Shinoda Yuu\n年齡:27\n身高:155cm\nBHW:88-60-87cm\n罩杯:F\n經紀公司:T-POWERS\n推薦番號:ATID-305,PRED-054")
        
    def on_exit_shinodayuu(self,event):
        print('Leaving yuu')

    def is_going_to_shinodayuu_rand(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '隨機選片'
        return False

    def on_enter_shinodayuu_rand(self, event):
        print("in yuurand")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,random.choice(store.shinodayuu_index))
        self.go_back()

    def on_exit_shinodayuu_rand(self):
        print('Leaving yuurand')

    def is_going_to_hashimotoarina(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '橋本有菜'
        return False
        
    def on_enter_hashimotoarina(self,event):
        print("in arina")
        
        sender_id = event['sender']['id']
        send_image_url(sender_id,"https://i.imgur.com/VDBcGIA.jpg")
        response = send_text_message(sender_id,"名字:Hashimoto Arina\n年齡:21\n身高:166cm\nBHW:84-56-83cm\n罩杯:C\n經紀公司:S1\n推薦番號:SNIS-923,SSNI-209")        

    def on_exit_hashimotoarina(self,event):
        print('Leaving arina')

    def is_going_to_hashimotoarina_rand(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '隨機選片'
        return False

    def on_enter_hashimotoarina_rand(self, event):
        print("in arinarand")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,random.choice(store.hashimotoarina_index))
        self.go_back()
        
    def on_exit_hashimotoarina_rand(self):
        print('Leaving arinarand')

    def is_going_to_sonodamion(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '園田美櫻'
        return False
      
    def on_enter_sonodamion(self,event):
        print("in mion")
        
        sender_id = event['sender']['id']
        send_image_url(sender_id,"https://i.imgur.com/KPwGO5p.jpg")        
        response = send_text_message(sender_id,"名字:Sonoda Mion\n年齡:23\n身高:150cm\nBHW:90-58-88cm\n罩杯:G\n經紀公司:PRESTIGE\n推薦番號:ABP-721")
        
    def on_exit_sonodamion(self,event):
        print('Leaving mion')
        
    def is_going_to_sonodamion_rand(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '隨機選片'
        return False        

    def on_enter_sonodamion_rand(self, event):
        print("in mionrand")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,random.choice(store.sonodamion_index))
        self.go_back()

    def on_exit_sonodamion_rand(self):
        print('Leaving mionrand')

    def is_going_to_itochinami(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '伊東千奈美'
        return False

    def on_enter_itochinami(self,event):
        print("in chinami")
        
        sender_id = event['sender']['id']
        send_image_url(sender_id,"https://i.imgur.com/fpantsv.jpg")
        response = send_text_message(sender_id,"名字:Ito Chinami\n年齡:22\n身高:163cm\nBHW:87-57-86cm\n罩杯:E\n經紀公司:MOODYZ\n推薦番號:MIDE-468,MIDE-485")
        
    def on_exit_itochinami(self,event):
        print('Leaving chinami')

    def is_going_to_itochinami_rand(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '隨機選片'
        return False

    def on_enter_itochinami_rand(self, event):
        print("in chinamirand")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,random.choice(store.itochinami_index))
        self.go_back()

    def on_exit_itochinami_rand(self):
        print('Leaving chinamirand')

    def is_going_to_ayamishunka(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '彩美旬果'
        return False
      
    def on_enter_ayamishunka(self,event):
        print("in shunka")
        
        sender_id = event['sender']['id']
        send_image_url(sender_id,"https://i.imgur.com/TG3VWVB.jpg")
        response = send_text_message(sender_id,"名字:Ayami Shunka\n年齡:25\n身高:154cm\nBHW:85-58-83cm\n罩杯:D\n經紀公司:S1\n推薦番號:SSNI-227,abp-586")
    
    def on_exit_ayamishunka(self,event):
        print('Leaving shunka')

    def is_going_to_ayamishunka_rand(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '隨機選片'
        return False

    def on_enter_ayamishunka_rand(self, event):
        print("in shunkarand")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,random.choice(store.ayamishunka_index))
        self.go_back()

    def on_exit_ayamishunka_rand(self):
        print('Leaving shunkarand')

    def is_going_to_kogawaiori(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '古川伊織'
        return False
        
    def on_enter_kogawaiori(self,event):
        print("in iori")
        
        sender_id = event['sender']['id']
        send_image_url(sender_id,"https://i.imgur.com/Yui8Hng.jpg")
        response = send_text_message(sender_id,"名字:Kogawa Iori\n年齡:26\n身高:155cm\nBHW:88-58-86cm\n罩杯:F\n經紀公司:SOD\n推薦番號:Star-758")
        
    def on_exit_kogawaiori(self,event):
        print('Leaving iori')
        
    def is_going_to_kogawaiori_rand(self,event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == '隨機選片'
        return False        
        
    def on_enter_kogawaiori_rand(self, event):
        print("in iorirand")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id,random.choice(store.kogawaiori_index))
        self.go_back()   
        
    def on_exit_kogawaiori_rand(self):
        print('Leaving iorirand')             
