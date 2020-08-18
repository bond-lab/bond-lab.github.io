#  -*- coding: utf-8 -*-   
# bad joke generator
#
# Copyright: Francis Bond, 2018
# License: Attribution 4.0 International (CC BY 4.0)
#          https://creativecommons.org/licenses/by/4.0/
#
###
### generate jokes of the form: 
### "when is an X not an X, when it is an AX"  iff AX is not a hyponym of X
###

from nltk.corpus import wordnet as wn
prep=dict()
prep['eng'] = "in on of after under over to".split()

def give_head (phrase, lang, pos):
    """Return the head of a phrase"""
    words = phrase.split()
    ### we could be more sophisticated :-)
    if lang=='eng':
        if pos in ('n'):
            ### if not species name
            if any(w in prep['eng'] for w in words):
                ## PPs
                ## fixme -return word before prep
                return None
            elif any(w in ['and', 'or'] for w in words):
                ## conjunction --- non-headed
                return None
            else:
                return words[-1]
        if pos in ('v', 'p'):
            return words[0]
        else:
            return None ### could do better
        
    elif lang=='jpn': ### Head final it is
        return words[-1]
    elif lang=='cmn': ### Head final it is
        if  pos=='n':
            if len(phrase)==4:
                return words[2:]
            elif len(phrase)==4:
                return words[1:]
            else:
                return  None 
        else:
            return  None 
    else:  ### if we are not sure, don't guess
        return  None

# def printwhen(lang, hotdog, dog):
#     if lang==eng:
#         print(u"""
# When is a %s not a %s?
#    When it is a %s
# """ % (dog, dog, hotdog))
#     elif lang==cmn:
#         print(u"""
# 什麼 %s 不是 %s？ 
#    %s"
# """ % (dog, dog, hotdog))

### escape the word
def link_word(word, format):
    if format == 'html':
        link = "<a href='http://compling.hss.ntu.edu.sg/omw/cgi-bin/wn-gridx.cgi?usrname=&gridmode=grid&lemma={0}'>{0}</a>".format(word)
    else:
        link= word
    return link

for s in wn.all_synsets('n'):
    wp = s.pos()
    for l in s.lemmas():
        words = l.name().split('_')
        lem = " ".join(words)
        if len(words) > 1 and lem[0].islower():  ### only non-Name MWEs
            head=give_head(lem,'eng', wp)
            if head:
                lem_is_head = False
                #print ("{}\t{}".format(head, lem))
                for p in s.hypernym_paths():
                    for ss in p:
                    #print p
                    #print [ss.lemmas for ss in p]
                        for ll in ss.lemmas():
                            if head == ll.name():
                                #print "%s is a %s" % (lem, head)
                                lem_is_head=True
                if not lem_is_head:
                    print ("""\
<p>When is a <i>{}</i> not a <i>{}</i>?
<br>&nbsp;&nbsp;&nbsp;&nbsp;When it is a <i>{}</i>!
""".format(head,
           link_word(head,'html'), 
           link_word(lem,'html')))
                    
