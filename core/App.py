import streamlit as st
import pages
###
import os
import sys
cwd = os.getcwd()
sys.path.insert(1, cwd+"/core")
import stInfrastructure as infra
import page_debug

#####################
### useful functions
#####################

def toggle_debug():
    st.session_state.debug = not st.session_state.debug


class App:

    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.state = {}

        self.init_pages()

    def init_pages(self):
        self.pages = {}
        for page in pages.__all__:
            p = page() #self.state)
            self.pages[p.name] = p
        self.pages["Broom Cupboard"] = page_debug
        return


#####################
### main part
#####################

    def main(self):
        st.sidebar.title(self.title)

        ### sidebar
        st.sidebar.title(":telescope: Kené's WebApp")
        st.sidebar.markdown("---")
        name = st.sidebar.radio("Select page: ", tuple(self.pages.keys()))
        st.sidebar.markdown("---")

        try:
            if st.session_state.debug:
                st.sidebar.markdown("on page: "+name)
        except AttributeError:
            pass

        ### mini-state summary
        if st.sidebar.button("State Summary"):
            # st.write(dir(state))
            myKeys=[x for x in st.session_state.keys()]
            for mk in myKeys:
                if mk=="broom": continue
                st.sidebar.markdown(f"**{mk}** defined")

        ### debug toggle
        # debug = st.checkbox(label="Toggle debug", key='debug', on_change=toggle_debug)
        # st.markdown("debug: "+str(debug))
        # st.markdown("session: "+str(st.session_state.debug))
        try:
            debug = st.sidebar.checkbox("Toggle debug",value=st.session_state.debug)
        except AttributeError:
            debug = st.sidebar.checkbox("Toggle debug")
        if debug:
            st.session_state.debug=True
        else: st.session_state.debug=False


        ### small print
        st.sidebar.markdown("---")
        st.sidebar.markdown("*small print*:")
        st.sidebar.markdown("[git repository](https://github.com/kwraight/streamlitTemplate)")
        st.sidebar.markdown("[docker repository](https://hub.docker.com/repository/docker/kwraight/template-app)")

        st.sidebar.markdown("streamlitTemplate: "+infra.Version())

        self.pages[name].main()
