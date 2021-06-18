### streamlit stuff
import streamlit as st
### general stuff
import os
import sys
from datetime import datetime
###session stuff
cwd = os.getcwd()
sys.path.insert(1, cwd)
import stInfrastructure as infra
import page_debug
# get pages from pages directory
import importlib
pagesDir=cwd+"/pages"
pageFiles= [f for f in os.listdir(pagesDir) if os.path.isfile(os.path.join(pagesDir, f)) and "page_" in f and not f.endswith("~")]
pageFiles=sorted(pageFiles)
sys.path.insert(1, pagesDir)
modules= [importlib.import_module(p[:-3]) for p in pageFiles]

#####################
### main
#####################

def main():
    ### get state variable
    state = infra.get()

    ### define pages dictionary
    # zip names (after '_') with modules
    pages = dict(zip([p.split('_')[-1][:-3] for p in pageFiles],[getattr(m,"main_part") for m in modules]))
    pages['Broom cupboard']=page_debug.main_part

    ### sidebar
    st.sidebar.title(":telescope: Kené's WebApp")
    st.sidebar.markdown("---")
    page = st.sidebar.radio("Select page:", tuple(pages.keys()))
    st.sidebar.markdown("---")

    try:
        if state.debug:
            st.sidebar.markdown("page:"+page)
    except AttributeError:
        pass

    ### mini-state summary
    if st.sidebar.button("State Summary"):
        # st.write(dir(state))
        myatts=[x for x in dir(state) if "__" not in x]
        # st.sidebar.markdown(myatts)
        for ma in myatts:
            if ma=="broom": continue
            st.sidebar.markdown(f"**{ma}** defined")


    ### debug toggle
    st.sidebar.markdown("---")
    debug = st.sidebar.checkbox("Toggle debug")
    if debug:
        state.debug=True
    else: state.debug=False

    ### small print
    st.sidebar.markdown("---")
    st.sidebar.markdown("*small print*:")
    st.sidebar.markdown("[git repository](https://github.com/kwraight/streamlitTemplate)")

    st.sidebar.markdown("streamlitTemplate: "+infra.Version())

    ### display  selected page using state variable
    pages[page](state)


#########################################################################################################

#########################################################################################################

### run
if __name__ == "__main__":
    main()
