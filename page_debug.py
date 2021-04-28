import streamlit as st
###
from urllib import request
import json
from annotated_text import annotated_text, annotation
###
import stInfrastructure as infra

#####################
### Check state page
#####################
def display_state_values(state):

    st.write("## All data")
    st.write("Debug setting:", state.debug)
    st.write("---")

    # debug check
    if state.debug:
        st.write("### Debug is on")

    # check page info. defined
    if "broom" in [i for i in state.__dict__.keys() if i[:1] != '_']:
        if state.debug: st.write("state.broom defined")
    else:
        state.broom={}

    # st.write(dir(state))
    myatts=[x for x in dir(state) if "__" not in x]
    st.write(myatts)
    for ma in myatts:
        #if ma=="broom": continue
        st.write(f"**{ma}** information")
        infra.ToggleButton(state.broom,'show_'+ma,f"Show *{ma}* information")
        if state.broom['show_'+ma]:
            st.write(state.__getattribute__(ma))



### get API response from endpoint
def GetResponse(endStr):
    api_endpoint = endStr
    api_response = json.load(request.urlopen(api_endpoint))
    return api_response


def EasterEgg(state):
    ### wee bit of fun
    if state.debug:
        st.write(":egg: Easter Egg")
        if st.button("Get a quote"):
            quote=GetResponse("https://favqs.com/api/qotd")
            if quote:
                annotated_text(
                (quote['quote']['body'],"","#8ef"),
                "\n",
                (quote['quote']['author'],"","#afa"),
                )


def main_part(state):
    st.title(":wrench: Broom cupboard")
    st.write("---")
    st.write("## Bits and bobs for maintainance")
    st.write("---")

    display_state_values(state)

    st.write("## :exclamation: Clear all state settings")
    if st.button("Clear state"):
        for ma in [x for x in dir(state) if "__" not in x]:
            if ma=="debug": continue
            try:
                state.__delattr__(ma)
            except AttributeError:
                pass


    EasterEgg(state)
