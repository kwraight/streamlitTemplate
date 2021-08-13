import streamlit as st
import corePages
import userPages
###
import os
import sys
import stInfrastructure as infra

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
        allPages= corePages.__all__ + userPages.__all__
        # order pages if required
        #allPages.insert(0, allPages.pop([p().name for p in allPages.index("NAME")))
        allPages.append(allPages.pop([p().name for p in allPages].index("Broom Cupboard")))
        for page in allPages:
            p = page() #self.state)
            self.pages[p.name] = p
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
