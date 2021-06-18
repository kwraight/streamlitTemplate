### streamlit stuff
import streamlit as st
import streamlit.report_thread as ReportThread
from streamlit.hashing import _CodeHasher
from streamlit.server.server import Server
###
import base64
import pandas as pd

################
### Useful functions
################

### set selection default value
DEFAULT = '< PICK A VALUE >'
def selectbox_with_default(text, values, default=DEFAULT, sidebar=False):
    func = st.sidebar.selectbox if sidebar else st.selectbox
    return func(text, np.insert(np.array(values, object), 0, default))

### get csv file from dataframe
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(sep="\t", index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

### show df with option to download
def DisplayWithOption(df):
    st.dataframe(df)
    if st.button("download table"):
        st.markdown(get_table_download_link(df), unsafe_allow_html=True)


def ColourCells(s, df, colName, flip=False):
    thisRow = pd.Series(data=False, index=s.index)
    # vailable colours: 9*x=5
    colours=['red','blue','green','orange','purple''yellow','pink','lightblue','lightgreen']*5
    names=list(df[colName].unique())
    if flip:
        return ['background-color: %s ; color: %s'% ('white',colours[names.index(s[colName])])]*len(df.columns)
    else:
        return ['background-color: %s ; color: %s'% (colours[names.index(s[colName])],'black')]*len(df.columns)

###
### Info.
###

# display component info. - require compMap style dictionary:
# compMap = [{"id":w['id'], "code":w['code'], "ASN":w['serialNumber'], "altID":w['alternativeIdentifier'], "state":w['state'], "user":w['userIdentity'], "location":w['currentLocation']['code'], "destination":w['shipmentDestination'], "cts":w['cts']} for w in selCompList if w['componentType']['code']==state.delete['compTypeCode'] and w['state']=="ready"]
def ComponentInfo(user,comp):
    # check comp info.
    st.write("**Component Information**")
    st.write("who:*",comp['user'],"*")
    if comp['user']==user['userIdentity']:
        st.write(" - **you**")
    else:
        st.write(" - **not** you")
    st.write("what:*",comp['code'],"*")
    st.write("where:*",comp['location'],"*")
    if comp['location'] in [x['code'] for x in user['institutions']]:
        st.write(" - **found** in user institutions")
    else:
        st.write(" - **not** found in user institutions")
    try:
        st.write(" * shipping destination:",comp['destination']['name'],"(id:"+comp['destination']['id']+")")
    except TypeError:
        st.write(" * no shipping destination found")
    st.write("when:*",comp['cts'],"*")
    st.write("(why:*","who can say?*)")

###
### Widgets
###

def ToggleButton(myDict, myKey, txt):
    try:
        myDict[myKey] = st.checkbox(txt, value=myDict[myKey])
    except KeyError:
        myDict[myKey] = st.checkbox(txt, value=False)

def TextBox(myDict, myKey, txt, pwd=False):
    if pwd:
        try:
            myDict[myKey] = st.text_input(label=txt, type="password", value=myDict[myKey])
        except KeyError:
            myDict[myKey] = st.text_input(label=txt, type="password")
        except ValueError:
            myDict[myKey] = st.text_input(label=txt, type="password")
    else:
        try:
            myDict[myKey] = st.text_input(label=txt, value=myDict[myKey])
        except KeyError:
            myDict[myKey] = st.text_input(label=txt)
        except ValueError:
            myDict[myKey] = st.text_input(label=txt)

def SelectBox(myDict, myKey, opts, txt, lamKey=None):
    if len(opts)<1:
        st.write("No options found for "+myKey)
        st.stop()
    sortedOpts=opts
    if type(opts[0])!=type({}) and type(opts[0])!=type([]):
        sortedOpts=sorted(opts)

    if lamKey==None:
        try:
            myDict[myKey]=st.selectbox(txt, sortedOpts, index=sortedOpts.index(myDict[myKey]) )
        except KeyError:
            myDict[myKey]=st.selectbox(txt, sortedOpts )
        except ValueError:
            myDict[myKey]=st.selectbox(txt, sortedOpts )
    else:
        #st.write("for",lamKey,"and",myDict[myKey],":",opts.index(myDict[myKey]))
        if type(opts[0])==type({}):
            sortedOpts=sorted(opts, key=lambda k: k[lamKey])
        try:
            myDict[myKey]=st.selectbox(txt, sortedOpts, format_func=lambda x: x[lamKey], index=sortedOpts.index(myDict[myKey]) )
        except KeyError:
            myDict[myKey]=st.selectbox(txt, sortedOpts, format_func=lambda x: x[lamKey] )
        except ValueError:
            myDict[myKey]=st.selectbox(txt, sortedOpts, format_func=lambda x: x[lamKey] )

### pandas dataframe variation
def SelectBoxDf(myDict, myKey, df, txt, colName):
    if colName not in list(df.columns):
        st.write("No",colName,"found in dataframe")
        st.stop()
    opts=list(df[colName].unique())
    sortedOpts=sorted(opts)
    try:
        val=st.selectbox(txt, sortedOpts, index=sortedOpts.index(myDict[myKey]) )
    except KeyError:
        val=st.selectbox(txt, sortedOpts )
    except ValueError:
        val=st.selectbox(txt, sortedOpts )
    myDict[myKey]=df.query(colName+'=="'+val+'"')

def MultiSelect(myDict, myKey, opts, txt):
    if len(opts)<1:
        st.write("No options found for "+myKey)
        st.stop()
    sortedOpts=opts
    if type(opts[0])!=type({}) and type(opts[0])!=type([]):
        sortedOpts=sorted(opts)
    try:
        myDict[myKey]=st.multiselect(txt, sortedOpts, default=myDict[myKey] )
    except KeyError:
        myDict[myKey]=st.multiselect(txt, sortedOpts )
    except ValueError:
        myDict[myKey]=st.multiselect(txt, sortedOpts )
    except st.StreamlitAPIException:
        myDict[myKey]=st.multiselect(txt, sortedOpts )

def Radio(myDict, myKey, opts, txt):
    if len(opts)<1:
        st.write("No options found for "+myKey)
        st.stop()
    sortedOpts=opts
    if type(opts[0])!=type({}) and type(opts[0])!=type([]):
        sortedOpts=sorted(opts)
    try:
        myDict[myKey]=st.radio(txt, sortedOpts, index=sortedOpts.index(myDict[myKey]))
    except KeyError:
        myDict[myKey]=st.radio(txt, sortedOpts)
    except ValueError:
        myDict[myKey]=st.radio(txt, sortedOpts)

def Slider(myDict, myKey, myMin, myMax, txt):
    try:
        myDict[myKey]=st.slider(txt,min_value=myMin,max_value=myMax,value=myDict[myKey])
    except KeyError: # default min value
        myDict[myKey]=st.slider(txt,min_value=myMin,max_value=myMax,value=myMin)
    except ValueError: # default min value
        myDict[myKey]=st.slider(txt,min_value=myMin,max_value=myMax,value=myMin)

#####################
### state functions
#####################
# https://gist.github.com/FranzDiebold/898396a6be785d9b5ca6f3706ef9b0bc
"""Hack to add per-session state to Streamlit.

Works for Streamlit >= v0.65

Usage
-----

>>> import SessionState
>>>
>>> session_state = SessionState.get(user_name='', favorite_color='black')
>>> session_state.user_name
''
>>> session_state.user_name = 'Mary'
>>> session_state.favorite_color
'black'

Since you set user_name above, next time your script runs this will be the
result:
>>> session_state = get(user_name='', favorite_color='black')
>>> session_state.user_name
'Mary'

"""

import streamlit.report_thread as ReportThread
from streamlit.server.server import Server


class SessionState():
    """SessionState: Add per-session state to Streamlit."""
    def __init__(self, **kwargs):
        """A new SessionState object.

        Parameters
        ----------
        **kwargs : any
            Default values for the session state.

        Example
        -------
        >>> session_state = SessionState(user_name='', favorite_color='black')
        >>> session_state.user_name = 'Mary'
        ''
        >>> session_state.favorite_color
        'black'

        """
        for key, val in kwargs.items():
            setattr(self, key, val)


def get(**kwargs):
    """Gets a SessionState object for the current session.

    Creates a new object if necessary.

    Parameters
    ----------
    **kwargs : any
        Default values you want to add to the session state, if we're creating a
        new one.

    Example
    -------
    >>> session_state = get(user_name='', favorite_color='black')
    >>> session_state.user_name
    ''
    >>> session_state.user_name = 'Mary'
    >>> session_state.favorite_color
    'black'

    Since you set user_name above, next time your script runs this will be the
    result:
    >>> session_state = get(user_name='', favorite_color='black')
    >>> session_state.user_name
    'Mary'

    """
    # Hack to get the session object from Streamlit.

    session_id = ReportThread.get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError('Could not get Streamlit session object.')

    this_session = session_info.session

    # Got the session object! Now let's attach some state into it.

    if not hasattr(this_session, '_custom_session_state'):
        this_session._custom_session_state = SessionState(**kwargs)

    return this_session._custom_session_state
