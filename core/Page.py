import streamlit as st
import inspect

class Page:

    def __init__(self, name, title, instructions=[]):
        self.name = name
        self.title = title
        self.instructions = instructions

    def main(self):
        ### title and (optional) instructions
        st.title(self.title)
        if st.session_state.debug:
            st.write("_ page name:",self.name,"_")
            st.write("_ file name:",inspect.getfile(self.__class__),"_")
        st.write("---")
        if st.session_state.debug:
            for i in self.instructions:
                if "*" in i[0:3]:
                    st.write(i)
                else:
                    st.write("  *",i)
        else:
            st.write(" * toggle debug for details")
        st.write("---")

        # debug check
        if st.session_state.debug:
            st.write("### Debug is on")

        ### add page attrubute to state
        # st.write([k for k in state.keys() if k[:1] != '_'])
        if self.name in [k for k in st.session_state.keys() if k[:1] != '_']:
            if st.session_state.debug: st.write("st.session_state[\'"+self.name+"\'] defined")
        else:
            st.session_state.__setattr__(self.name,{})

        return
