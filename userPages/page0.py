### standard
import streamlit as st
from core.Page import Page
### custom

#####################
### main part
#####################

class Page0(Page):
    def __init__(self):
        super().__init__("Page0", "Zeroth Page", ['nothing to report'])

    def main(self):
        super().main()

        #pageDict=st.session_state[self.name]

        st.write("Content to be added xxx")
