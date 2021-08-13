### standard
import streamlit as st
from core.Page import Page
### custom
from urllib import request
import json
from annotated_text import annotated_text, annotation
###
import os
import sys
import core.stInfrastructure as infra

################
### Useful functions
################

def display_state_values():

    st.write("## All data")
    st.write("Debug setting:", st.session_state.debug)
    st.write("---")

    # debug check
    if st.session_state.debug:
        st.write("### Debug is on")

    # check page info. defined
    if "Broom Cupboard" in [i for i in st.session_state.keys()]:
        if st.session_state.debug: st.write("st.session_state['Broom Cupboard'] defined")
    else:
        st.session_state['Broom Cupboard']={}

    myKeys=[x for x in st.session_state.keys()]
    st.write(myKeys)
    for mk in myKeys:
        if mk=="debug": continue
        st.write(f"**{mk}** information")
        infra.ToggleButton(st.session_state['Broom Cupboard'],'show_'+mk,f"Show *{mk}* information")
        if st.session_state['Broom Cupboard']['show_'+mk]:
            st.write(st.session_state[mk])


### get API response from endpoint
def GetResponse(endStr):
    api_endpoint = endStr
    api_response = json.load(request.urlopen(api_endpoint))
    return api_response


def EasterEgg():
    ### wee bit of fun
    if st.session_state.debug:
        st.write(":egg: Easter Egg")
        if st.button("Get a quote"):
            quote=GetResponse("https://favqs.com/api/qotd")
            if quote:
                annotated_text(
                (quote['quote']['body'],"","#8ef"),
                "\n",
                (quote['quote']['author'],"","#afa"),
                )

#####################
### main part
#####################

class Pagex(Page):
    def __init__(self):
        super().__init__("Broom Cupboard", ":wrench: Broom Cupboard", ['nothing to report'])

    def main(self):
        super().main()

        display_state_values()

        st.write("## :exclamation: Clear all state settings")
        if st.button("Clear state"):
            for mk in [x for x in st.session_state.keys()]:
                if mk=="debug": continue
                try:
                    state.__delattr__(mk)
                except AttributeError:
                    pass

        EasterEgg()
