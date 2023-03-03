import requests,os,random
from time import sleep
from datetime import date
from datetime import datetime
from pystyle import Colors, Colorate, Write, Center, Add, Box
from colorama import init, Fore, Back, Style
class apifb:
  def __init__(self, cookie) -> None:
    self.headfb={
      'authority': 'www.facebook.com',
      'accept': '*/*',
      'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
      # Requests sorts cookies= alphabetically
      'cookie': cookie,
      'origin': 'https://www.facebook.com',
      'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
      'sec-ch-prefers-color-scheme': 'dark',
      'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
      'viewport-width': '979',
      'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
      'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }
      
    find_data = requests.get("https://mbasic.facebook.com/", headers=self.headfb).text
    self.fb_dtsg=find_data.split('fb_dtsg" value="')[1].split('"')[0]
    self.jazoest=find_data.split('jazoest" value="')[1].split('"')[0]
    self.id_acc=cookie.split('c_user=')[1].split(';')[0]
    #self.jazoest=find_data.split('jazoest", "')[1].split('"')[0]
    #self.fb_dtsg=find_data.split('"initDtsg":"')[1].split('"')[0]
    #self.id_acc=cookie.split('c_user=')[1].split(';')[0]
    
    
  def camxuc(self,cmfb,uid):
    if cmfb == 'LIKE':
      camxuc='1'
    if cmfb == 'LOVE':
      camxuc = '2'
    if cmfb == 'CARE':
      camxuc = '16'
    if cmfb == 'HAHA':
      camxuc = '4'
    if cmfb == 'WOW':
      camxuc = '3'
    if cmfb == 'SAD':
      camxuc = '7'
    if cmfb == 'ANGRY':
      camxuc = '8'
    if '_' in uid:
      uid=uid.split('_')[1]
    data = {
          'reaction_type':camxuc,
  
          'ft_ent_identifier':uid,
  
          'fb_dtsg':self.fb_dtsg,
  
          'jazoest':self.jazoest,
     }
  
    response = requests.post(f'https://m.facebook.com/ufi/reaction/?ft_ent_identifier={uid}',headers=self.headfb, data=data)
  def share(self,uid):
  
    uri = requests.get(f'https://mbasic.facebook.com/{uid}').url
    cc=requests.get(uri,headers=self.headfb).text
    eev = cc.split('eav=')[1].split('&')[0]
    data = {
    'fb_dtsg':self.fb_dtsg,
    'jazoest':self.jazoest,
    'comment':'',
    'privacyx':'300645083384735',
    'm':'self',
    'sid':uid,
    'fs':'8',
    'im':'self',
    'session_id':'8b87032f-9152-44f3-9e51-dca90a7c7872',
    'app_id':'966242223397117'
    }
  
    response = requests.post(f'https://m.facebook.com/a/sharer.php?shouldRedirectToPermalink=1&usedialogwithselector=1&isthrowbackpost&eav={eev}&paipv=0',headers=self.headfb, data=data)
  def follow (self,uid):
  
    data = {
  
          'subject_id':uid,
  
          'fb_dtsg':self.fb_dtsg,
  
          'jazoest':self.jazoest,
  
          '__user': self.id_acc,
  
      }
    data1={
      'av':self.id_acc,
      '__user':self.id_acc,
      '__a':'1',
      '__dyn':'7AzHJ16U9ob8ng5K8G6EjBWo2nDwAxu13wsongS3q2ibwyzE5S3O2Saxa1NwJwpUe8hwaG0Z82_CxS320om78bbwto88422y11xmfz83WwgEcHzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUy2a0SEuBwJCwLyESE2KwwwOg2cwMwhF8-4UdUcobUak1xwJwxw',
      '__csr':'g8YIBgJklstOnvTNGt8YnvuoD4razqN1a8Dd9_AiRQWsijLAHWCQ-Q6njpF8BeHFbVepUgUyuC74iaGQuHF6GiULZ3-KdBCx-5ohK4kp4XyWAxit7AAzS4FqDwCzHK4FoCum5qxq78pyE-fxa8gap4i3Ocwzxyax24EbEnwKy8gxG4o-ewiocUsAwXwGwsEdU5i7oS8y8lwyxO9xm0x89ppE5aawwwhUy1hwyQ2qbwjE0cLE0z206S9o1Fo02RNw288S0Uo0how7hw8m0b-g044u1Sa023m0ji03Bi0eyg9o2vw2dU3hw1ku1uw-w',
      '__req':'27',
      '__hs':'19324.HYP:comet_pkg.2.1.0.2.1',
      'dpr':'2',
      '__ccg':'EXCELLENT',
      '__rev':'1006638951',
      '__s':'fi0bg0:mys0n8:kibtlv',
      '__hsi':'7170981203729397430',
      '__comet_req':'15',
      'fb_dtsg':self.fb_dtsg,
      'jazoest':self.jazoest,
      'lsd':'AGxqXZ4bEd4uBgz2k5BEBM',
      '__aaid':'3346513562278209',
      '__spin_r':'1006638951',
      '__spin_b':'trunk',
      '__spin_t':'1669624169',
      'fb_api_caller_class':'RelayModern',
      'fb_api_req_friendly_name':'FriendingCometFriendRequestSendMutation',
      'variables':'{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1669624170450,479235,190055527696468,","friend_requestee_ids":["'+uid+'"],"refs":[null],"source":"profile_button","warn_ack_for_ids":[],"actor_id":"'+self.id_acc+'","client_mutation_id":"6"},"scale":2}',
      'server_timestamps':'true',
      'doc_id':'8495827540457782',
      }
    response = requests.post('https://m.facebook.com/a/subscriptions/add',headers=self.headfb, data=data)
    cc=requests.post('https://www.facebook.com/api/graphql/',headers=self.headfb,data=data1)
  def cmt(self,uid,ndcmt):
    uri = requests.get(f'https://mbasic.facebook.com/{uid}').url
    cc=requests.get(uri,headers=self.headfb).text
    try:
      story_fbid = cc.split('story_fbid=')[1].split('&')[0]
    
      eav = cc.split('eav=')[1].split('&')[0]
    except:
      pass
    data = {
    'comment_text':ndcmt,
    
    'conversation_guide_session_id': '',
    
    'conversation_guide_shown': 'none',
    
    'waterfall_source': 'photo_comment',
    
    'submit': 'Đăng',
    
    'fb_dtsg':self.fb_dtsg,
    
    'jazoest':self.jazoest,
    
    '__user':self.id_acc,
    
            }
    response = requests.post(f'https://m.facebook.com/a/comment.php?fscomment_logging&ft_ent_identifier={story_fbid}&eav={eav}', headers=self.headfb, data=data)
  def joingr(self,uid):
    data = {
                'av':self.id_acc,
                '__user':self.id_acc,
                'fb_dtsg':self.fb_dtsg,
                'jazoest':self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'ModernForumJoinMutation',
                'variables': '{"input":{"client_mutation_id":"1","actor_id":"'+self.id_acc+'","group_id":"'+uid+'","source":"mobile_group_join","group_share_tracking_params":null}}',
                'server_timestamps': 'true',
                'doc_id': '3879455072179463',
            }
    response = requests.post('https://m.facebook.com/api/graphql/', headers=self.headfb, data=data) 
  def likepage(self,uid):
    data = {

            'av': self.id_acc,

            '__user': self.id_acc,

            'fb_dtsg': self.fb_dtsg,

            'jazoest': self.jazoest,

            'fb_api_caller_class': 'RelayModern',

            'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',

            'variables': '{"input":{"page_id":"'+uid+'","source":null,"actor_id":"'+self.id_acc+'","client_mutation_id":"1"},"scale":1}',

            'server_timestamps': 'true',

            'doc_id': '4867271226642619',

        }

    response = requests.post('https://www.facebook.com/api/graphql/',headers=self.headfb, data=data)
  def cmm(self,type,id):
    id1=id.split('_')[0]
    id2=id.split('_')[1]
    uri = requests.get(f'https://mbasic.facebook.com/{id1}').url
    cc=requests.get(uri,headers=self.headfb).text
    story_fbid = cc.split('story_fbid=')[1].split('&')[0]
    
    eav = cc.split('eav=')[1].split('&')[0]
    data={
      'fb_dtsg':self.fb_dtsg,
      'jazoest':self.jazoest,
      'lsd':'lpg_Kt97B9rrMkLeNsuciL',
      '__dyn':'1KQEGiEiwgVU-4UpwGzVQ2mml3onxG6UmwHwAxu3-UcodUbEdEc8uK0AUlxK4o3PwqEhwem0Joeoe852q1ew65xO0FE6S1QzU1vrzo5q0hK1gwwyo36w9yq3q0H8-0KU6i0N85G0zE5W0HUvwww5NyES0gq0Lo4K2e1FwLw8O',
      '__csr':'',
      '__req':'7',
      '__a':'AYlLV02koTgzzMQavdKl8FFtY8EyTFC4Efa9caGK9c7iQT3XsOXXkS_n7RvVTfzOEutp0VAGm_K1VgJyqhYPTIHG2xjqO62lYk2El3ggB-yzMA',
      '__user':self.id_acc,

    }
    if type=="LIKE":
      camxuc="1"
    if type=="LOVE":
      camxuc="2"
    if type =="WOW":
      camxuc="3"
    if type=="HAHA":
      camxuc="4"
    if type=="SAD":
      camxuc="7"
    if type=="ANGRY":
      camxuc="8"
    if type=="CARE":
      camxuc="16"
    d=requests.post(f"https://m.facebook.com/a/comment.php?parent_redirect_comment_token={id}&reaction_comment_id={id2}&viewer_reaction={camxuc}&snowflake&ft_ent_identifier={story_fbid}&eav={eav}&gfid=AQDqjHvmviN_vLEaql8&paipv=0&fs=8&__tn__=R-R&client_id=1671023558652%3A2276991652&session_id=e6cc3840-7523-4af7-8b8a-d280a1dbb746",headers=self.headfb,data=data)
   
def thanhdai():
  x="="*70
  print(Colorate.Horizontal(Colors.green_to_white,x))
barnv=f'''
┌──────────────────────────────────────────┐
│  STT  │       Nhiệm Vụ       │  Xu Nhận  │
├──────────────────────────────────────────┤
│   1   │ LIKE                 │  300 Xu   │
├──────────────────────────────────────────┤
│   2   │ Cảm Xúc              │  400 Xu   │             
├──────────────────────────────────────────┤
│   3   │ Bình Luận            │  800 Xu   │
├──────────────────────────────────────────┤
│   4   │ Theo Dõi             │  900 Xu   │
├──────────────────────────────────────────┤
│   5   │ Like Page            │  900 Xu   │
├──────────────────────────────────────────┤
│   6   │ Tham Gia Nhóm        │  1400 Xu  │
├──────────────────────────────────────────┤
│   7   │ Cảm Xúc Bình Luận    │  600 Xu   │
├──────────────────────────────────────────┤
│   8   │ Chia Sẻ              │  800 Xu   │
├──────────────────────────────────────────┤
│Lưu Ý: Chọn Nhiều Nhiệm Vụ Thì Sử Dụng "+"│
│Ví Dụ: 1+2+3+2+2+4+5+...                  │
└──────────────────────────────────────────┘'''

def log(tk,mk):
  try:
    data={
    'username':tk,
    'password':mk,
    }
    logck=requests.post('https://traodoisub.com/scr/login.php',data=data).cookies
    m=logck['PHPSESSID']
    cktds='PHPSESSID='+m
    headlog = {
    'user-agent':'Mozilla/5.0 (Linux; Android 12; vivo 2019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'cookie':cktds
    }
    gettk=requests.get('https://traodoisub.com/view/setting/load.php', headers=headlog).json()
    token=gettk['tokentds']
    head={'Host':'traodoisub.com','accept':'application/json, text/javascript, */*; q=0.01','user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36','x-requested-with':'XMLHttpRequest','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://traodoisub.com/view/cauhinh','accept-encoding':'gzip, deflate','accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7','Cookie':cktds,}
    
    check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
    head_job={
      
      'referer':'https://traodoisub.com/ex/reaction/',
      'user-agent':'Mozilla/5.0 (Linux; Android 12; vivo 2019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'cookie':cktds,}
    return {"token":token,"head_job":head_job}
  except:
    return {"token":"sai"}
def idelay(dl):
  for demtg in range(dl, -1, -1):
    print(Colorate.Horizontal(Colors.green_to_white,f'Làm Nhiệm Vụ Tiếp Theo Sau:{demtg} Giây'),end='\r')
    sleep(0.9)
filetkmk='tdssieuvippro.txt'
checktk=os.path.isfile(filetkmk)
def tuandat(text:str):
  text=int(input(f"{Fore.GREEN}[{Fore.YELLOW}●{Fore.GREEN}] {text}{Fore.WHITE}"))
  return text
def text(text:str):
  text=str(input(f"{Fore.GREEN}[{Fore.YELLOW}●{Fore.GREEN}] {text}{Fore.WHITE}"))
  return text
if checktk == False:
  while True:
    os.system('clear')
    tk=text('Nhập Tài Khoản TDS: ')
    mk=text('Nhập Mật Khẩu TDS: ')
    c1=log(tk,mk)
    token=c1['token']
    if token != 'sai':
      head=c1['head_job']
      zzz=f"{tk}|{mk}"
      open(filetkmk,'w').write(zzz)
      tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
      ten=tttds['data']['user']
      xu=tttds['data']['xu']
      os.system('clear')
      print(f'{Fore.GREEN}[{Fore.YELLOW}●{Fore.GREEN}] Đăng Nhập Thành Công')
      print(f'{Fore.GREEN}[{Fore.YELLOW}●{Fore.GREEN}] Tài Khoản:{Fore.RED}{ten}{Fore.GREEN}|Xu:{Fore.RED}{xu}')
      break
    else:
      print(f'{Fore.RED} Sai Tài Khoản Hoặc Mật Khẩu')
      sleep(1)
if checktk == True:
  doc=open(filetkmk,'r').read()
  try:
    tk=doc.split('|')[0]
    mk=doc.split('|')[1]
    c1=log(tk,mk)
    token=c1['token']
    if token != 'sai':
      head=c1['head_job']
      os.system('clear')
      tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
      ten=tttds['data']['user']
      xu=tttds['data']['xu']
      print(f'{Fore.GREEN}[{Fore.YELLOW}●{Fore.GREEN}] Tài Khoản:{Fore.RED}{ten}{Fore.GREEN}|Xu:{Fore.RED}{xu}')
      lcc=text('Bạn Có Muốn Tiếp Tục Sử Dụng Tài Khoản Trên Không(y/n): ')
      
      if lcc =='n':
        while True:
          os.system('clear')
          tk=text('Nhập Tài Khoản TDS: ')
          mk=text('Nhập Mật Khẩu TDS: ')
          c1=log(tk,mk)
          token=c1['token']
          if token != 'sai':
            head=c1['head_job']
            zzz=f"{tk}|{mk}"
            open(filetkmk,'w').write(zzz)
            tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
            ten=tttds['data']['user']
            xu=tttds['data']['xu']
            break
          else:
            print(f'{Fore.RED} Sai Tài Khoản Hoặc Mật Khẩu')
            sleep(1)
    elif token =='sai':
      while True:
        os.system('clear')
        tk=text('Nhập Tài Khoản TDS: ')
        mk=text('Nhập Mật Khẩu TDS: ')
        c1=log(tk,mk)
        token=c1['token']
        if token != 'sai':
          head=c1['head_job']
          zzz=f"{tk}|{mk}"
          open(filetkmk,'w').write(zzz)
          tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
          ten=tttds['data']['user']
          xu=tttds['data']['xu']
          break
        else:
          print(f'{Fore.RED} Sai Tài Khoản Hoặc Mật Khẩu')
          sleep(1)
  except:
    while True:
      os.system('clear')
      tk=text('Nhập Tài Khoản TDS: ')
      mk=text('Nhập Mật Khẩu TDS: ')
      c1=log(tk,mk)
      token=c1['token']
      if token != 'sai':
        head=c1['head_job']
        zzz=f"{tk}|{mk}"
        open(filetkmk,'w').write(zzz)
        tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
        ten=tttds['data']['user']
        xu=tttds['data']['xu']
        break
      else:
        print(f'{Fore.RED} Sai Tài Khoản Hoặc Mật Khẩu')
        sleep(1)
listck=[]
slck=1
os.system('clear')
thanhdai()
print(f'{Fore.GREEN}[{Fore.YELLOW}●{Fore.GREEN}] Đăng Nhập Thành Công')
print(f'{Fore.GREEN}[{Fore.YELLOW}●{Fore.GREEN}] Tài Khoản:{Fore.RED}{ten}{Fore.GREEN}|Xu:{Fore.RED}{xu}')
thanhdai()
while True:
  ck_fb=text(f'Nhập Cookie Thứ {slck}: ')
  if ck_fb =='':
    if len(listck) == 0:
      print(f'{Fore.RED}Vui Lòng Nhập Ít Nhất 1 Cookie',end='\r')
      sleep(1)
    else:
      break
  
  u_check='https://mbasic.facebook.com/profile.php'
  h={'cookie':ck_fb}
  check=requests.get(url=u_check,headers=h).text
  try:
    name=check.split('<title>')[1].split('</title>')[0]
    id_fb=check.split('><a href="/profile.php?lst=')[1].split('%')[0]
    chfb=requests.get(f'https://traodoisub.com/api/?fields=run&id={id_fb}&access_token={token}').json()
    if 'success' in chfb:
      thanhdai()
      print(Colorate.Horizontal(Colors.red_to_yellow,f'Cấu Hình Thành Công|Name:{name}|Uid:{id_fb}'))
      thanhdai()
      listck.append(ck_fb)
      slck+=1
    else:
      print(f'{Fore.RED}Có Vẻ Như Name:{name}|Uid:{id_fb} Chưa Được Cấu Hình\n',end='\r')
      sleep(2)
  except:
    print(f'{Fore.RED}COOKIE FACEBOOKDIE',end='\r')
    sleep(2)
os.system('clear')
print(Colorate.Horizontal(Colors.yellow_to_red,
Center.XCenter('─────────────{Name:Bùi Tuấn Đạt|Zalo:0363006167}─────────────')))
print(Colorate.Horizontal(Colors.green_to_white,Center.XCenter(barnv)))
listjobb=[]
lcjob=text('Vui Lòng Nhập Lựa Chọn: ')
xuka=0
for job in lcjob.split('+'):
  if job =="1":  job ="like"
  if job =="2":  job="reaction"
  if job =="3":  job="comment"
  if job =="4":  job="follow"
  if job =="5":  job="fanpage"
  if job =="6":  job="group"
  if job =="7":  job="reactioncmt"
  if job =="8":  job="share"
  listjobb.append(job)
dl=tuandat('Nhập Delay Làm Nhiệm Vụ: ')
  
sl=1
while True:
  for i in range(len(listck)):
    ck=listck[i]
    try:
      h={'cookie':ck}
      check=requests.get('https://mbasic.facebook.com/profile.php',headers=h).text
      name=check.split('<title>')[1].split('</title>')[0]
      id_fb=check.split('><a href="/profile.php?lst=')[1].split('%')[0]
      chfb=requests.get(f'https://traodoisub.com/api/?fields=run&id={id_fb}&access_token={token}').json()
      thanhdai()
      print(Colorate.Horizontal(Colors.green_to_white,f'|COOKIE:{len(listck)}|CẤU HÌNH THÀNH CÔNG|Name:{name}|Uid:{id_fb}|'))
      thanhdai()
      DoiNick=0
      HetJob=0
      JobLoi=0
      run=apifb(ck)
    except:
      listck.remove(ckk)
      break
    while True:
      if DoiNick>=10 or JobLoi>=5:
        break
      rdnv=random.choice(listjobb)
      if rdnv=="reaction":
        getjob=requests.get(f'https://traodoisub.com/ex/{rdnv}/load.php',headers=head).json()
        try:
          for gj in getjob['data']:
            id=gj['id']
            type=gj['type']
            run.camxuc(type,id)
            nhantien=requests.post(f'https://traodoisub.com/ex/{rdnv}/nhantien.php',headers=head,data={'id':id, 'type': type}).text
            if '2' in nhantien:
              xudc=400
              xuka=xuka+xudc
              x = datetime.now().strftime("%H:%M:%S")
              tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
              xu=tttds['data']['xu']
              print(Colorate.Horizontal(Colors.green_to_white,f'[{sl}] [{x}] [{type}] [{id}] [400] [{xuka}] [{xu}]'))
              sl=sl+1
              DoiNick=DoiNick+1
              HetJob=0
              JobLoi=0
              if DoiNick>=10:  break
              idelay(dl)
            else:
              JobLoi=JobLoi+1
              if JobLoi>=5:
                break
        except:
          print(Colorate.Horizontal(Colors.green_to_white,f'Hết Nhiệm Vụ {rdnv}'),end='\r')
          HetJob=HetJob+1
          if HetJob>=10:  break
      if rdnv=="like":
        getjob=requests.get(f'https://traodoisub.com/ex/{rdnv}/load.php',headers=head).json()
        try:
          for gj in getjob['data']:
            id=gj['id']
            run.camxuc('LIKE',id)
            nhantien=requests.post(f'https://traodoisub.com/ex/{rdnv}/nhantien.php',headers=head,data={'id':id,
            'type':'like'}).text
            if '2' in nhantien:
              xudc=300
              xuka=xuka+xudc
              x = datetime.now().strftime("%H:%M:%S")
              tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
              xu=tttds['data']['xu']
              if '_' in id:
                id=id.split('_')[1]
              print(Colorate.Horizontal(Colors.green_to_white,f'[{sl}] [{x}] [LIKE] [{id}] [300] [{xuka}] [{xu}]'))
              sl=sl+1
              DoiNick=DoiNick+1
              HetJob=0
              JobLoi=0
              if DoiNick>=10:  break
              idelay(dl)
            else:
              JobLoi=JobLoi+1
              if JobLoi>=5:
                break
        except:
          print(Colorate.Horizontal(Colors.green_to_white,f'Hết Nhiệm Vụ {rdnv}'),end='\r')
          HetJob=HetJob+1
          if HetJob>=10:  break
      if rdnv=="comment":
        getjob=requests.get(f'https://traodoisub.com/ex/{rdnv}/load.php',headers=head).json()
        try:
          for gj in getjob['data']:
            id=gj['id']
            type=gj['msg']
            run.cmt(id,type)
            nhantien=requests.post(f'https://traodoisub.com/ex/{rdnv}/nhantien.php',headers=head,data={'id':id, 'type': 'comment'}).text
            if '2' in nhantien:
              xudc=800
              xuka=xuka+xudc
              x = datetime.now().strftime("%H:%M:%S")
              tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
              xu=tttds['data']['xu']
              print(Colorate.Horizontal(Colors.green_to_white,f'[{sl}] [{x}] [CMT] [{id}] [800] [{xuka}] [{xu}]'))
              sl=sl+1
              DoiNick=DoiNick+1
              HetJob=0
              JobLoi=0
              if DoiNick>=10:  break
              idelay(dl)
            else:
              JobLoi=JobLoi+1
              if JobLoi>=5:
                break
        except:
          print(Colorate.Horizontal(Colors.green_to_white,f'Hết Nhiệm Vụ {rdnv}'),end='\r')
          HetJob=HetJob+1
          if HetJob>=10:  break
      if rdnv=="follow":
        getjob=requests.get(f'https://traodoisub.com/ex/{rdnv}/load.php',headers=head).json()
        try:
          for gj in getjob['data']:
            id=gj['id']
            run.follow(id)
            nhantien=requests.post(f'https://traodoisub.com/ex/{rdnv}/nhantien.php',headers=head,data={'id':id, 'type': 'follow'}).text
            if '2' in nhantien:
              xudc=900
              xuka=xuka+xudc
              x = datetime.now().strftime("%H:%M:%S")
              tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
              xu=tttds['data']['xu']
              print(Colorate.Horizontal(Colors.green_to_white,f'[{sl}] [{x}] [FOLLOW] [{id}] [900] [{xuka}] [{xu}]'))
              sl=sl+1
              DoiNick=DoiNick+1
              HetJob=0
              JobLoi=0
              if DoiNick>=10:  break
              idelay(dl)
            else:
              JobLoi=JobLoi+1
              if JobLoi>=5:
                break
        except:
          print(Colorate.Horizontal(Colors.green_to_white,f'Hết Nhiệm Vụ {rdnv}'),end='\r')
          HetJob=HetJob+1
          if HetJob>=10:  break
      if rdnv=="fanpage":
        getjob=requests.get(f'https://traodoisub.com/ex/{rdnv}/load.php',headers=head).json()
        try:
          for gj in getjob['data']:
            id=gj['id']
            run.likepage(id)
            nhantien=requests.post(f'https://traodoisub.com/ex/{rdnv}/nhantien.php',headers=head,data={'id':id,'type': 'fanpage'}).text
            if '2' in nhantien:
              xudc=900
              xuka=xuka+xudc
              x = datetime.now().strftime("%H:%M:%S")
              tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
              xu=tttds['data']['xu']
              print(Colorate.Horizontal(Colors.green_to_white,f'[{sl}] [{x}] [LIKEPAGE] [{id}] [900] [{xuka}] [{xu}]'))
              sl=sl+1
              DoiNick=DoiNick+1
              HetJob=0
              JobLoi=0
              if DoiNick>=10:  break
              idelay(dl)
            else:
              JobLoi=JobLoi+1
              if JobLoi>=5:
                break
        except:
          print(Colorate.Horizontal(Colors.green_to_white,f'Hết Nhiệm Vụ {rdnv}'),end='\r')
          HetJob=HetJob+1
          if HetJob>=10:  break
      if rdnv=="group":
        getjob=requests.get(f'https://traodoisub.com/ex/{rdnv}/load.php',headers=head).json()
        try:
          for gj in getjob['data']:
            id=gj['id']
            run.joingr(id)
            nhantien=requests.post(f'https://traodoisub.com/ex/{rdnv}/nhantien.php',headers=head,data={'id':id,'type':'group'}).text
            if '2' in nhantien:
              xudc=1400
              xuka=xuka+xudc
              x = datetime.now().strftime("%H:%M:%S")
              tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
              xu=tttds['data']['xu']
              print(Colorate.Horizontal(Colors.green_to_white,f'[{sl}] [{x}] [GROUP] [{id}] [1400] [{xuka}] [{xu}]'))
              sl=sl+1
              DoiNick=DoiNick+1
              HetJob=0
              JobLoi=0
              if DoiNick>=10:  break
              idelay(dl)
            else:
              JobLoi=JobLoi+1
              if JobLoi>=5:
                break
        except:
          print(Colorate.Horizontal(Colors.green_to_white,f'Hết Nhiệm Vụ {rdnv}'),end='\r')
          HetJob=HetJob+1
          if HetJob>=10:  break
      if rdnv=="reactioncmt":
        getjob=requests.get(f'https://traodoisub.com/ex/{rdnv}/load.php',headers=head).json()
        try:
          for gj in getjob['data']:
            id=gj['id']
            type=gj['type']
            run.cmm(type,id)
            nhantien=requests.post(f'https://traodoisub.com/ex/{rdnv}/nhantien.php',headers=head,data={'id':id, 'type': type}).text
            if '2' in nhantien:
              xudc=600
              xuka=xuka+xudc
              x = datetime.now().strftime("%H:%M:%S")
              tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
              xu=tttds['data']['xu']
              if '_' in id:
                id=id.split('_')[1]
              print(Colorate.Horizontal(Colors.green_to_white,f'[{sl}] [{x}] [{type}CMT] [{id}] [600] [{xuka}] [{xu}]'))
              sl=sl+1
              DoiNick=DoiNick+1
              HetJob=0
              JobLoi=0
              if DoiNick>=10:  break
              idelay(dl)
            else:
              JobLoi=JobLoi+1
              if JobLoi>=5:
                break
        except:
          print(Colorate.Horizontal(Colors.green_to_white,f'Hết Nhiệm Vụ {rdnv}'),end='\r')
          HetJob=HetJob+1
          if HetJob>=10:  break
      if rdnv=="share":
        getjob=requests.get(f'https://traodoisub.com/ex/{rdnv}/load.php',headers=head).json()
        try:
          for gj in getjob['data']:
            id=gj['id']
            run.share(id)
            sleep(1)
            nhantien=requests.post(f'https://traodoisub.com/ex/{rdnv}/nhantien.php',headers=head,data={'id':id,'type': 'share'}).text
            if '2' in nhantien:
              xudc=800
              xuka=xuka+xudc
              x = datetime.now().strftime("%H:%M:%S")
              tttds=requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
              xu=tttds['data']['xu']
              print(Colorate.Horizontal(Colors.green_to_white,f'[{sl}] [{x}] [SHARE] [{id}] [800] [{xuka}] [{xu}]'))
              sl=sl+1
              DoiNick=DoiNick+1
              HetJob=0
              JobLoi=0
              if DoiNick>=10:  break
              idelay(dl)
            else:
              JobLoi=JobLoi+1
              if JobLoi>=5:
                break
        except:
          print(Colorate.Horizontal(Colors.green_to_white,f'Hết Nhiệm Vụ {rdnv}'),end='\r')
          HetJob=HetJob+1
          if HetJob>=10:  break