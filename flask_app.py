from flask import Flask
import sys
print (sys.version)
import dash
import dash_core_components as dcc
import dash_html_components as html#
import plotly.express as px
import pandas as pd
from data_retrieval_connect_pythonanywhere_ssh import get_mostfrequent_data_all, get_mostfrequent_data_all_daterange, get_cleaned_text_data_original, get_novice_view_data, static_df #get_dataframe, 
from dash.dependencies import Input, Output
import dash_table
import plotly.graph_objs as go
import datetime
from contractions import world_abbreviations

server = Flask(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, server=server, routes_pathname_prefix='/',
                external_stylesheets=external_stylesheets)

@server.route("/about")
def about():
    return "All about Flask"


app.layout = html.Div(
    [
        html.H1("File Browser"),
        html.H2("Upload"),
        dcc.Upload(
            id="upload-data",
            children=html.Div(
                ["Drag and drop or click to select a file to upload."]
            ),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            multiple=True,
        ),
        html.H2("File List"),
        html.Ul(id="file-list"),
    ],
    style={"max-width": "500px"},
)

##df = get_dataframe()
##df = static_df
##df_data = get_mostfrequent_data_all_daterange("ALL",df['sql_datetime_object'].min(),df['sql_datetime_object'].max())
##most_frequent_words = df_data[0][:30]
##most_frequent_words_values = df_data[1][:30]
##df1.rename(columns={'sql_tweet_text': 'text', 'sql_platform': 'platform','sql_sentiment': 'sentiment','sql_datetime_object ':'datetime'}, inplace=True)

df_tweet = pd.DataFrame(columns=['text', 'platform', 'sentiment','datetime'])
#df.rename(columns={'sql_tweet_text': 'text', 'sql_platform': 'platform','sql_sentiment': 'sentiment','sql_datetime_object ':'datetime'}, inplace=True)
fig = go.Figure([go.Bar(x=[], y=[],orientation='h',name='value1')])
#fig = go.Figure([go.Bar(x=most_frequent_words_values[::-1], y=most_frequent_words[::-1],orientation='h',name='value1')])


fig.update_layout(title="Threat Term Ranking",height=680,margin=dict(l=160,r=0,b=15,t=40,pad=0),font=dict(color="black"))


novice_graph = go.Figure()
novice_df = get_novice_view_data()
novice_graph.add_trace(go.Scatter(x=novice_df.index, y=novice_df['spyware'], name='spyware'))
novice_graph.add_trace(go.Scatter(x=novice_df.index, y=novice_df['malware'], name='malware'))
novice_graph.add_trace(go.Scatter(x=novice_df.index, y=novice_df['trojan'], name='trojan'))
novice_graph.add_trace(go.Scatter(x=novice_df.index, y=novice_df['ransomware'], name='ransomware'))
novice_graph.add_trace(go.Scatter(x=novice_df.index, y=novice_df['phishing'], name='phishing'))
novice_graph.add_trace(go.Scatter(x=novice_df.index, y=novice_df['scam'], name='scam'))
novice_graph.add_trace(go.Scatter(x=novice_df.index, y=novice_df['password'], name='password'))
novice_graph.add_trace(go.Scatter(x=novice_df.index, y=novice_df['botnet'], name='botnet'))
novice_graph.update_layout(title_text='<b>Daily Threat Term Presence</b>',font_size=13,font_family="Courier New", xaxis=dict(tickmode='linear'))


#dcc.Graph(id='apt-map',figure = go.Figure(go.Choropleth(locations=abrevs)),config={'displayModeBar': False})


APTZ = pd.read_csv('APTDB.csv',encoding="latin-1")
abrevs = ["VAT"]

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}
tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}



app.layout = html.Div([
  html.H1("CyberText Analytics",style={'textAlign': 'left',"background": "silver","color": "blue"}),


########################################################################################################################################################################
################### CTA TAB ##########################################################################################################################################
#########################################################################################################################################################################


  dcc.Tabs([
    dcc.Tab(label='Threat Text Tracking', style=tab_style, selected_style=tab_selected_style, children=[
    html.Div([


      
      html.Div([
      
      html.Div(dcc.Graph(id='graph-output-simple', figure=novice_graph, config={'displayModeBar': False}), className="thirteen columns"),], className="row"),

        html.Div([
      html.Div(dcc.Dropdown(id='dropdown',
                            value='ALL',
                            multi=False,
                            clearable=False,
                            options=[
                                    {'label': 'Unigram', 'value': 'unigram'},
                                    {'label': 'Bigram', 'value': 'bigram'},
                                    {'label': 'Trigram', 'value': 'trigram'},
                                    {'label': 'ALL', 'value': 'ALL'}
                                    ],
                            style={
                                   'margin': 7,
                                   'marginLeft':76,
                                   'width': '150px',
                                  }
                            ), className="two columns"),
      html.Div(dcc.DatePickerRange(
                       id='date-input',
                       #min_date_allowed=df['sql_datetime_object'].min(),
                       #max_date_allowed=df['sql_datetime_object'].max(),
                       initial_visible_month=datetime.datetime.now(),
                       start_date=datetime.datetime.today() - datetime.timedelta(1),
                       end_date=datetime.datetime.today(),
                       month_format='YYYY,MMMM',
                       display_format='YYYY-MM-DD',
                       style={
                               'margin' : 7,
                               'margin-left' : '45px',
                       }
              ), className="three columns"),
              ], className="row"),



      html.Div([
        html.Div(dcc.Markdown("**Threat Term Ranking**"), style={'marginLeft': 158, 'marginRight': 0, 'marginTop': 0, 'marginBottom': 25,
               'padding': '0px 0px 0px 0px',"font-family":"Courier New",'font-size':'18px'}, className="five columns"),
        html.Div(dcc.Markdown("**Threat Tweet Data Viewer**"), style={'marginLeft': 50, 'marginRight': 0, 'marginTop': 0, 'marginBottom': 25,
               'padding': '0px 0px 0px 0px',"font-family":"Courier New",'font-size':'18px'}, className="six columns"),
              ], className="row"),



        html.Div(dcc.Graph(id='graph-output', figure=fig, className="six columns",config={'displayModeBar': False})), #TFIDF bar Graph Output
        html.Div(dash_table.DataTable(id='tweet-dataframe',                                                            #Tweet Dataframe
                                      columns=[{"name": i, "id": i} for i in df_tweet.columns],
                                      data=df_tweet.to_dict('records'),
                                      style_table={'height':'71vh','width':'auto','overflowY': 'auto' }), className="six columns")
             
             ], className="row"),


        html.Div(children=[dcc.Markdown(
                   " 2020 [CTA](https://github.com/ishikawa-rei)  All Rights Reserved.")], style={'marginLeft': 5, 'marginRight': 5, 'marginTop': 0, 'marginBottom': 10,
               'backgroundColor':'#F7FBFE',
               'border': 'thin lightgrey dashed', 'padding': '6px 0px 0px 8px'}),


########################################################################################################################################################################
################### APT DB TAB ##########################################################################################################################################
#########################################################################################################################################################################

        ]),
        dcc.Tab(label='APT DB', style=tab_style, selected_style=tab_selected_style, children=[

        html.Div([html.H5('Advanced Persistent Threat DB',style={'textAlign': 'Center',"background": "silver","color": "blue"}),

          dcc.Graph(id='apt-map',figure = go.Figure(go.Choropleth(locations=abrevs)),config={'displayModeBar': False})

          ]),

          html.Div([
              html.Div(dcc.Dropdown(id='dropdown-location',
                                      value='A',
                                      multi=False,
                                      clearable=False,
                                      options=[
                                              {'label': 'ORIGIN', 'value': 'A'},
                                              {'label': 'china', 'value': 'china'},
                                              {'label': 'gaza', 'value': 'gaza'},
                                              {'label': 'india', 'value': 'india'},
                                              {'label': 'iran', 'value': 'iran'},
                                              {'label': 'latin america', 'value': 'latin america'},
                                              {'label': 'middle east', 'value': 'middle east'},
                                              {'label': 'nigeria', 'value': 'nigeria'},
                                              {'label': 'north korea', 'value': 'north korea'},
                                              {'label': 'pakistan', 'value': 'pakistan'},
                                              {'label': 'portugal/brazil', 'value': 'portugal/brazil'},
                                              {'label': 'romania', 'value': 'romania'},
                                              {'label': 'russia', 'value': 'russia'},
                                              {'label': 'south korea', 'value': 'south korea'},
                                              {'label': 'spain', 'value': 'spain'},
                                              {'label': 'turkey', 'value': 'turkey'},
                                              {'label': 'uae', 'value': 'uae'},
                                              {'label': 'ukraine', 'value': 'ukraine'},
                                              {'label': 'unknown', 'value': 'unknown'},
                                              {'label': 'usa', 'value': 'usa'},
                                              {'label': 'vietnam', 'value': 'vietnam'}
                                              ],
                                      style={
                                             'margin': 7,
                                             'width': '150px',
                                             #'margin-left' : '30px',
                                            }

                        ), className="one columns"),




                html.Div(dcc.Dropdown(id='dropdown-sectors',
                                      value='A',
                                      multi=False,
                                      clearable=False,
                                      options=[
                                              {'label': 'SECTOR', 'value': 'A'},
                                              {'label': 'activists & dissidents', 'value': 'activists & dissidents'},
                                              {'label': 'agriculture', 'value': 'agriculture'},
                                              {'label': 'automotive', 'value': 'automotive'},
                                              {'label': 'aviation & aerospace', 'value': 'aviation & aerospace'},
                                              {'label': 'banking', 'value': 'banking'},
                                              {'label': 'biotechnology', 'value': 'biotechnology'},
                                              {'label': 'casinos & gaming', 'value': 'casinos & gaming'},
                                              {'label': 'chemical & petrochemical', 'value': 'chemical & petrochemical'},
                                              {'label': 'cryptocurrency exchanges', 'value': 'cryptocurrency exchanges'},
                                              {'label': 'diplomatic/embassies', 'value': 'diplomatic/embassies'},
                                              {'label': 'e-commerce', 'value': 'e-commerce'},
                                              {'label': 'energy', 'value': 'energy'},
                                              {'label': 'engineering', 'value': 'engineering'},
                                              {'label': 'financial institutions', 'value': 'financial institutions'},
                                              {'label': 'government & defense', 'value': 'government & defense'},
                                              {'label': 'healthcare', 'value': 'healthcare'},
                                              {'label': 'high technology', 'value': 'high technology'},
                                              {'label': 'higher education', 'value': 'higher education'},
                                              {'label': 'hospitality & retail', 'value': 'hospitality & retail'},
                                              {'label': 'infrastructure', 'value': 'infrastructure'},
                                              {'label': 'international relations', 'value': 'international relations'},
                                              {'label': 'it & electronics', 'value': 'it & electronics'},
                                              {'label': 'journalists', 'value': 'journalists'},
                                              {'label': 'law enforcement', 'value': 'law enforcement'},
                                              {'label': 'manufacturing', 'value': 'manufacturing'},
                                              {'label': 'media & entertainment', 'value': 'media & entertainment'},
                                              {'label': 'mining,oil & gas', 'value': 'mining,oil & gas'},
                                              {'label': 'navigation', 'value': 'navigation'},
                                              {'label': 'ngo/npo & think tanks', 'value': 'ngo/npo & think tanks'},
                                              {'label': 'pharmaceutical', 'value': 'pharmaceutical'},
                                              {'label': 'research institute', 'value': 'research institute'},
                                              {'label': 'shipping & logistics', 'value': 'shipping & logistics'},
                                              {'label': 'software & game development', 'value': 'software & game development'},
                                              {'label': 'telecommunications', 'value': 'telecommunications'},
                                              {'label': 'transportation', 'value': 'transportation'},
                                              {'label': 'utilities', 'value': 'utilities'}
                                              ],
                                      style={
                                             'margin': 7,
                                             'width': '150px',
                                             'margin-left' : '20px',
                                            }

                        ), className="one columns"),




                html.Div(dcc.Dropdown(id='dropdown-countries',
                                      value='A',
                                      multi=False,
                                      clearable=False,
                                      options=[
                                              {'label': 'TARGET COUNTRY', 'value': 'A'},
                                              {'label': 'AFGHANISTAN', 'value': 'AFGHANISTAN'},
                                              {'label': 'ALBANIA', 'value': 'ALBANIA'},
                                              {'label': 'ALGERIA', 'value': 'ALGERIA'},
                                              {'label': 'ARGENTINA', 'value': 'ARGENTINA'},
                                              {'label': 'ARMENIA', 'value': 'ARMENIA'},
                                              {'label': 'AUSTRALIA', 'value': 'AUSTRALIA'},
                                              {'label': 'AUSTRIA', 'value': 'AUSTRIA'},
                                              {'label': 'AZERBAIJAN', 'value': 'AZERBAIJAN'},
                                              {'label': 'BAHRAIN', 'value': 'BAHRAIN'},
                                              {'label': 'BANGLADESH', 'value': 'BANGLADESH'},
                                              {'label': 'BELGIUM', 'value': 'BELGIUM'},
                                              {'label': 'BHUTAN', 'value': 'BHUTAN'},
                                              {'label': 'BOLIVIA', 'value': 'BOLIVIA'},
                                              {'label': 'BOSNIA', 'value': 'BOSNIA'},
                                              {'label': 'BOTSWANA', 'value': 'BOTSWANA'},
                                              {'label': 'BRAZIL', 'value': 'BRAZIL'},
                                              {'label': 'BRUNEI', 'value': 'BRUNEI'},
                                              {'label': 'BULGARIA', 'value': 'BULGARIA'},
                                              {'label': 'CAMBODIA', 'value': 'CAMBODIA'},
                                              {'label': 'CANADA', 'value': 'CANADA'},
                                              {'label': 'CHILE', 'value': 'CHILE'},
                                              {'label': 'CHINA', 'value': 'CHINA'},
                                              {'label': 'COLOMBIA', 'value': 'COLOMBIA'},
                                              {'label': 'CROATIA', 'value': 'CROATIA'},
                                              {'label': 'CUBA', 'value': 'CUBA'},
                                              {'label': 'CYPRUS', 'value': 'CYPRUS'},
                                              {'label': 'CZECH', 'value': 'CZECH'},
                                              {'label': 'DENMARK', 'value': 'DENMARK'},
                                              {'label': 'DOMINICAN REPUBLIC', 'value': 'DOMINICAN REPUBLIC'},
                                              {'label': 'ECUADOR', 'value': 'ECUADOR'},
                                              {'label': 'EGYPT', 'value': 'EGYPT'},
                                              {'label': 'ESTONIA', 'value': 'ESTONIA'},
                                              {'label': 'FINLAND', 'value': 'FINLAND'},
                                              {'label': 'FRANCE', 'value': 'FRANCE'},
                                              {'label': 'GEORGIA', 'value': 'GEORGIA'},
                                              {'label': 'GERMANY', 'value': 'GERMANY'},
                                              {'label': 'GREECE', 'value': 'GREECE'},
                                              {'label': 'GUATEMALA', 'value': 'GUATEMALA'},
                                              {'label': 'HERZEGOVINA', 'value': 'HERZEGOVINA'},
                                              {'label': 'HONG KONG', 'value': 'HONG KONG'},
                                              {'label': 'HUNGARY', 'value': 'HUNGARY'},
                                              {'label': 'ICELAND', 'value': 'ICELAND'},
                                              {'label': 'INDIA', 'value': 'INDIA'},
                                              {'label': 'INDONESIA', 'value': 'INDONESIA'},
                                              {'label': 'IRAN', 'value': 'IRAN'},
                                              {'label': 'IRAQ', 'value': 'IRAQ'},
                                              {'label': 'IRELAND', 'value': 'IRELAND'},
                                              {'label': 'ISRAEL', 'value': 'ISRAEL'},
                                              {'label': 'ITALY', 'value': 'ITALY'},
                                              {'label': 'JAMAICA', 'value': 'JAMAICA'},
                                              {'label': 'JAPAN', 'value': 'JAPAN'},
                                              {'label': 'JORDAN', 'value': 'JORDAN'},
                                              {'label': 'KAZAKHSTAN', 'value': 'KAZAKHSTAN'},
                                              {'label': 'KENYA', 'value': 'KENYA'},
                                              {'label': 'KUWAIT', 'value': 'KUWAIT'},
                                              {'label': 'KYRGYZSTAN', 'value': 'KYRGYZSTAN'},
                                              {'label': 'LAOS', 'value': 'LAOS'},
                                              {'label': 'LATVIA', 'value': 'LATVIA'},
                                              {'label': 'LEBANON', 'value': 'LEBANON'},
                                              {'label': 'LIBYA', 'value': 'LIBYA'},
                                              {'label': 'LITHUANIA', 'value': 'LITHUANIA'},
                                              {'label': 'LUXEMBOURG', 'value': 'LUXEMBOURG'},
                                              {'label': 'MACEDONIA', 'value': 'MACEDONIA'},
                                              {'label': 'MALAWI', 'value': 'MALAWI'},
                                              {'label': 'MALAYSIA', 'value': 'MALAYSIA'},
                                              {'label': 'MALI', 'value': 'MALI'},
                                              {'label': 'MAURITANIA', 'value': 'MAURITANIA'},
                                              {'label': 'MEXICO', 'value': 'MEXICO'},
                                              {'label': 'MOLDOVA', 'value': 'MOLDOVA'},
                                              {'label': 'MONGOLIA', 'value': 'MONGOLIA'},
                                              {'label': 'MONTENEGRO', 'value': 'MONTENEGRO'},
                                              {'label': 'KAZAKHSTAN', 'value': 'KAZAKHSTAN'},
                                              {'label': 'MOROCCO', 'value': 'MOROCCO'},
                                              {'label': 'MOZAMBIQUE', 'value': 'MOZAMBIQUE'},
                                              {'label': 'MYANMAR', 'value': 'MYANMAR'},
                                              {'label': 'NEPAL', 'value': 'NEPAL'},
                                              {'label': 'NETHERLANDS', 'value': 'NETHERLANDS'},
                                              {'label': 'NEW ZEALAND', 'value': 'NEW ZEALAND'},
                                              {'label': 'NICARAGUA', 'value': 'NICARAGUA'},
                                              {'label': 'NIGERIA', 'value': 'NIGERIA'},
                                              {'label': 'NORTH KOREA', 'value': 'NORTH KOREA'},
                                              {'label': 'NORWAY', 'value': 'NORWAY'},
                                              {'label': 'OMAN', 'value': 'OMAN'},
                                              {'label': 'PAKISTAN', 'value': 'PAKISTAN'},
                                              {'label': 'PALESTINE', 'value': 'PALESTINE'},
                                              {'label': 'PARAGUAY', 'value': 'PARAGUAY'},
                                              {'label': 'PERU', 'value': 'PERU'},
                                              {'label': 'PHILIPPINES', 'value': 'PHILIPPINES'},
                                              {'label': 'POLAND', 'value': 'POLAND'},
                                              {'label': 'PORTUGAL', 'value': 'PORTUGAL'},
                                              {'label': 'QATAR', 'value': 'QATAR'},
                                              {'label': 'RUSSIA', 'value': 'RUSSIA'},
                                              {'label': 'RWANDA', 'value': 'RWANDA'},
                                              {'label': 'SAUDI ARABIA', 'value': 'SAUDI ARABIA'},
                                              {'label': 'SERBIA', 'value': 'SERBIA'},
                                              {'label': 'SINGAPORE', 'value': 'SINGAPORE'},
                                              {'label': 'SLOVENIA', 'value': 'SLOVENIA'},
                                              {'label': 'SOMALIA', 'value': 'SOMALIA'},
                                              {'label': 'SOUTH AFRICA', 'value': 'SOUTH AFRICA'},
                                              {'label': 'SOUTH KOREA', 'value': 'SOUTH KOREA'},
                                              {'label': 'SPAIN', 'value': 'SPAIN'},
                                              {'label': 'SRI LANKA', 'value': 'SRI LANKA'},
                                              {'label': 'SUDAN', 'value': 'SUDAN'},
                                              {'label': 'SWEDEN', 'value': 'SWEDEN'},
                                              {'label': 'SWITZERLAND', 'value': 'SWITZERLAND'},
                                              {'label': 'TAIWAN', 'value': 'TAIWAN'},
                                              {'label': 'TAJIKISTAN', 'value': 'TAJIKISTAN'},
                                              {'label': 'THAILAND', 'value': 'THAILAND'},
                                              {'label': 'TIBET', 'value': 'TIBET'},
                                              {'label': 'TUNISIA', 'value': 'TUNISIA'},
                                              {'label': 'TURKEY', 'value': 'TURKEY'},
                                              {'label': 'TURKMENISTAN', 'value': 'TURKMENISTAN'},
                                              {'label': 'UGANDA', 'value': 'UGANDA'},
                                              {'label': 'UNITED ARAB EMIRATES', 'value': 'UNITED ARAB EMIRATES'},
                                              {'label': 'UNITED KINGDOM', 'value': 'UNITED KINGDOM'},
                                              {'label': 'UNITED STATES', 'value': 'UNITED STATES'},
                                              {'label': 'URUGUAY', 'value': 'URUGUAY'},
                                              {'label': 'UZBEKISTAN', 'value': 'UZBEKISTAN'},
                                              {'label': 'VENEZUELA', 'value': 'VENEZUELA'},
                                              {'label': 'VIETNAM', 'value': 'VIETNAM'},
                                              {'label': 'YEMEN', 'value': 'YEMEN'},
                                              {'label': 'ZIMBABWE', 'value': 'ZIMBABWE'}
                                              ],
                                      style={
                                             'margin': 7,
                                             'width': '150px',
                                             'margin-left' : '32px'
                                            }
                                      ), className="one columns"),


                html.Div(dcc.Dropdown(id='dropdown-tools',
                                      value='A',
                                      multi=False,
                                      clearable=False,
                                      options=[
                                              {'label': 'TOOL', 'value': 'A'},
                                              {'label': '0days', 'value': '0days'},
                                              {'label': '3para rat', 'value': '3para rat'},
                                              {'label': '4h rat', 'value': '4h rat'},
                                              {'label': '9002 rat', 'value': '9002 rat'},
                                              {'label': 'abaddonpos', 'value': 'abaddonpos'},
                                              {'label': 'adbupd', 'value': 'adbupd'},
                                              {'label': 'adobearm', 'value': 'adobearm'},
                                              {'label': 'advstoreshell', 'value': 'advstoreshell'},
                                              {'label': 'agent orm', 'value': 'agent orm'},
                                              {'label': 'agent tesla', 'value': 'agent tesla'},
                                              {'label': 'agent.btz', 'value': 'agent.btz'},
                                              {'label': 'agent.dne', 'value': 'agent.dne'},
                                              {'label': 'airbreak', 'value': 'airbreak'},
                                              {'label': 'alphanc', 'value': 'alphanc'},
                                              {'label': 'alreay', 'value': 'alreay'},
                                              {'label': 'ammyyrat', 'value': 'ammyyrat'},
                                              {'label': 'amtsol', 'value': 'amtsol'},
                                              {'label':'androrat', 'value':'androrat'},
                                              {'label':'anel', 'value':'anel'},
                                              {'label':'antak', 'value':'antak'},
                                              {'label':'applejeus', 'value':'applejeus'},
                                              {'label':'appleworm', 'value':'appleworm'},
                                              {'label':'apt3 keylogger', 'value':'apt3 keylogger'},
                                              {'label':'aspxspy', 'value':'aspxspy'},
                                              {'label':'astra', 'value':'astra'},
                                              {'label':'ati-agent', 'value':'ati-agent'},
                                              {'label':'atmos', 'value':'atmos'},
                                              {'label':'atmosphere', 'value':'atmosphere'},
                                              {'label':'atmripper cobalt strike', 'value':'atmripper cobalt strike'},
                                              {'label':'atmspitter', 'value':'atmspitter'},
                                              {'label':'auditcred', 'value':'auditcred'},
                                              {'label':'aumlib', 'value':'aumlib'},
                                              {'label':'auriga', 'value':'auriga'},
                                              {'label':'autoit backdoor', 'value':'autoit backdoor'},
                                              {'label':'ave maria', 'value':'ave maria'},
                                              {'label':'babymetal', 'value':'babymetal'},
                                              {'label':'backbend', 'value':'backbend'},
                                              {'label':'backdoor batel', 'value':'backdoor batel'},
                                              {'label':'backspace', 'value':'backspace'},
                                              {'label':'badcall', 'value':'badcall'},
                                              {'label':'badflick', 'value':'badflick'},
                                              {'label':'badnews', 'value':'badnews'},
                                              {'label':'bahamut', 'value':'bahamut'},
                                              {'label':'bandook', 'value':'bandook'},
                                              {'label':'bangat', 'value':'bangat'},
                                              {'label':'bankshot', 'value':'bankshot'},
                                              {'label':'banswift', 'value':'banswift'},
                                              {'label':'barlaiy', 'value':'barlaiy'},
                                              {'label':'bart', 'value':'bart'},
                                              {'label':'bateleur', 'value':'bateleur'},
                                              {'label':'beacon', 'value':'beacon'},
                                              {'label':'bellhop', 'value':'bellhop'},
                                              {'label':'bemstour', 'value':'bemstour'},
                                              {'label':'bifrost', 'value':'bifrost'},
                                              {'label':'biscuit', 'value':'biscuit'},
                                              {'label':'bitsadmin', 'value':'bitsadmin'},
                                              {'label':'bitsran', 'value':'bitsran'},
                                              {'label':'blackcoffee', 'value':'blackcoffee'},
                                              {'label':'blackenergy', 'value':'blackenergy'},
                                              {'label':'bouncer', 'value':'bouncer'},
                                              {'label':'brambul', 'value':'brambul'},
                                              {'label':'bravonc', 'value':'bravonc'},
                                              {'label':'briba', 'value':'briba'},
                                              {'label':'bugjuice', 'value':'bugjuice'},
                                              {'label':'c0d0so', 'value':'c0d0so'},
                                              {'label':'cachedump', 'value':'cachedump'},
                                              {'label':'cachemoney', 'value':'cachemoney'},
                                              {'label':'cactustorch', 'value':'cactustorch'},
                                              {'label':'cageychameleon', 'value':'cageychameleon'},
                                              {'label':'cain & abel', 'value':'cain & abel'},
                                              {'label':'cakelog', 'value':'cakelog'},
                                              {'label':'calendar', 'value':'calendar'},
                                              {'label':'callme', 'value':'callme'},
                                              {'label':'candyclog', 'value':'candyclog'},
                                              {'label':'cannon', 'value':'cannon'},
                                              {'label':'carbanak', 'value':'carbanak'},
                                              {'label':'careto', 'value':'careto'},
                                              {'label':'castov', 'value':'castov'},
                                              {'label':'catchamas', 'value':'catchamas'},
                                              {'label':'certutil', 'value':'certutil'},
                                              {'label':'cettra', 'value':'cettra'},
                                              {'label':'chches', 'value':'chches'},
                                              {'label':'china chopper', 'value':'china chopper'},
                                              {'label':'chopstick', 'value':'chopstick'},
                                              {'label':'chrome-passwords', 'value':'chrome-passwords'},
                                              {'label':'chromecookiesview', 'value':'chromecookiesview'},
                                              {'label':'ckife webshells', 'value':'ckife webshells'},
                                              {'label':'cloudduke', 'value':'cloudduke'},
                                              {'label':'cloudstats', 'value':'cloudstats'},
                                              {'label':'cmd.exe', 'value':'cmd.exe'},
                                              {'label':'cobalt strike', 'value':'cobalt strike'},
                                              {'label':'cobint', 'value':'cobint'},
                                              {'label':'cobra carbon system', 'value':'cobra carbon system'},
                                              {'label':'combos', 'value':'combos'},
                                              {'label':'commix', 'value':'commix'},
                                              {'label':'computrace', 'value':'computrace'},
                                              {'label':'comrat', 'value':'comrat'},
                                              {'label':'contopee', 'value':'contopee'},
                                              {'label':'cookiebag', 'value':'cookiebag'},
                                              {'label':'cookieclog', 'value':'cookieclog'},
                                              {'label':'cookiecutter', 'value':'cookiecutter'},
                                              {'label':'coraldeck', 'value':'coraldeck'},
                                              {'label':'coreshell', 'value':'coreshell'},
                                              {'label':'cosmicduke', 'value':'cosmicduke'},
                                              {'label':'cozycar', 'value':'cozycar'},
                                              {'label':'cozyduke', 'value':'cozyduke'},
                                              {'label':'crackmapexec', 'value':'crackmapexec'},
                                              {'label':'crashoverride', 'value':'crashoverride'},
                                              {'label':'creamsicle', 'value':'creamsicle'},
                                              {'label':'crimson', 'value':'crimson'},
                                              {'label':'crossrat', 'value':'crossrat'},
                                              {'label':'cryptcat', 'value':'cryptcat'},
                                              {'label':'csext', 'value':'csext'},
                                              {'label':'cuegoe', 'value':'cuegoe'},
                                              {'label':'cwoolger', 'value':'cwoolger'},
                                              {'label':'cyst downloader', 'value':'cyst downloader'},
                                              {'label':'dairy', 'value':'dairy'},
                                              {'label':'darkcomet', 'value':'darkcomet'},
                                              {'label':'darkhotel', 'value':'darkhotel'},
                                              {'label':'darkpulsar', 'value':'darkpulsar'},
                                              {'label':'daserf', 'value':'daserf'},
                                              {'label':'datper', 'value':'datper'},
                                              {'label':'ddkong', 'value':'ddkong'},
                                              {'label':'dealerschoice', 'value':'dealerschoice'},
                                              {'label':'delphstats', 'value':'delphstats'},
                                              {'label':'deltanc', 'value':'deltanc'},
                                              {'label':'denis', 'value':'denis'},
                                              {'label':'deputydog', 'value':'deputydog'},
                                              {'label':'derusbi', 'value':'derusbi'},
                                              {'label':'destover', 'value':'destover'},
                                              {'label':'dimens', 'value':'dimens'},
                                              {'label':'dipsind', 'value':'dipsind'},
                                              {'label':'dirsearch', 'value':'dirsearch'},
                                              {'label':'disttrack', 'value':'disttrack'},
                                              {'label':'dnsmessenger', 'value':'dnsmessenger'},
                                              {'label':'dnsrat', 'value':'dnsrat'},
                                              {'label':'dogcall', 'value':'dogcall'},
                                              {'label':'dorshel', 'value':'dorshel'},
                                              {'label':'doublefantasy', 'value':'doublefantasy'},
                                              {'label':'doublepulsar', 'value':'doublepulsar'},
                                              {'label':'downdelph', 'value':'downdelph'},
                                              {'label':'downpaper', 'value':'downpaper'},
                                              {'label':'downrange', 'value':'downrange'},
                                              {'label':'dozer', 'value':'dozer'},
                                              {'label':'dridex', 'value':'dridex'},
                                              {'label':'driftpin', 'value':'driftpin'},
                                              {'label':'drigo', 'value':'drigo'},
                                              {'label':'droidjack', 'value':'droidjack'},
                                              {'label':'dropper', 'value':'dropper'},
                                              {'label':'dropshot', 'value':'dropshot'},
                                              {'label':'dustysky', 'value':'dustysky'},
                                              {'label':'duuzer', 'value':'duuzer'},
                                              {'label':'dyncalc/dnscalc', 'value':'dyncalc/dnscalc'},
                                              {'label':'electricfish', 'value':'electricfish'},
                                              {'label':'elise', 'value':'elise'},
                                              {'label':'elmer', 'value':'elmer'},
                                              {'label':'emdivi', 'value':'emdivi'},
                                              {'label':'emissary', 'value':'emissary'},
                                              {'label':'empire', 'value':'empire'},
                                              {'label':'empireproject', 'value':'empireproject'},
                                              {'label':'epic', 'value':'epic'},
                                              {'label':'equationdrug', 'value':'equationdrug'},
                                              {'label':'equationlaser', 'value':'equationlaser'},
                                              {'label':'equestre', 'value':'equestre'},
                                              {'label':'eternalblue', 'value':'eternalblue'},
                                              {'label':'etumbot', 'value':'etumbot'},
                                              {'label':'evilgrab', 'value':'evilgrab'},
                                              {'label':'eviltoss', 'value':'eviltoss'},
                                              {'label':'fakecop', 'value':'fakecop'},
                                              {'label':'fakem', 'value':'fakem'},
                                              {'label':'fakespy', 'value':'fakespy'},
                                              {'label':'fallchill rat', 'value':'fallchill rat'},
                                              {'label':'fanny', 'value':'fanny'},
                                              {'label':'farfli', 'value':'farfli'},
                                              {'label':'fastcash', 'value':'fastcash'},
                                              {'label':'felismus', 'value':'felismus'},
                                              {'label':'filemalv', 'value':'filemalv'},
                                              {'label':'fimlis', 'value':'fimlis'},
                                              {'label':'final1stspy', 'value':'final1stspy'},
                                              {'label':'finfisher', 'value':'finfisher'},
                                              {'label':'fingerprintjs2', 'value':'fingerprintjs2'},
                                              {'label':'finspy', 'value':'finspy'},
                                              {'label':'firefox', 'value':'firefox'},
                                              {'label':'firemalv', 'value':'firemalv'},
                                              {'label':'flash', 'value':'flash'},
                                              {'label':'flashflood', 'value':'flashflood'},
                                              {'label':'flawedammy', 'value':'flawedammy'},
                                              {'label':'flawedgrace', 'value':'flawedgrace'},
                                              {'label':'flipside', 'value':'flipside'},
                                              {'label':'foozer', 'value':'foozer'},
                                              {'label':'forfiles', 'value':'forfiles'},
                                              {'label':'formerfirstrat', 'value':'formerfirstrat'},
                                              {'label':'frameworkpos', 'value':'frameworkpos'},
                                              {'label':'fraudrop', 'value':'fraudrop'},
                                              {'label':'freenki loader', 'value':'freenki loader'},
                                              {'label':'frozencell', 'value':'frozencell'},
                                              {'label':'fruityc2', 'value':'fruityc2'},
                                              {'label':'funkybot', 'value':'funkybot'},
                                              {'label':'gamaredon', 'value':'gamaredon'},
                                              {'label':'gazer', 'value':'gazer'},
                                              {'label':'gcat', 'value':'gcat'},
                                              {'label':'gemcutter', 'value':'gemcutter'},
                                              {'label':'geminiduke', 'value':'geminiduke'},
                                              {'label':'getmail', 'value':'getmail'},
                                              {'label':'gh0st rat', 'value':'gh0st rat'},
                                              {'label':'ghambar', 'value':'ghambar'},
                                              {'label':'ghole', 'value':'ghole'},
                                              {'label':'glancelove', 'value':'glancelove'},
                                              {'label':'globeimposter', 'value':'globeimposter'},
                                              {'label':'glooxmail', 'value':'glooxmail'},
                                              {'label':'gnatspy', 'value':'gnatspy'},
                                              {'label':'goggles', 'value':'goggles'},
                                              {'label':'goodor', 'value':'goodor'},
                                              {'label':'goopy', 'value':'goopy'},
                                              {'label':'gpresult', 'value':'gpresult'},
                                              {'label':'grabnew', 'value':'grabnew'},
                                              {'label':'grateful pos', 'value':'grateful pos'},
                                              {'label':'grease', 'value':'grease'},
                                              {'label':'greezebackdoor', 'value':'greezebackdoor'},
                                              {'label':'griffon', 'value':'griffon'},
                                              {'label':'grillmark', 'value':'grillmark'},
                                              {'label':'grok', 'value':'grok'},
                                              {'label':'gsecdump', 'value':'gsecdump'},
                                              {'label':'hacksfase', 'value':'hacksfase'},
                                              {'label':'halfbaked', 'value':'halfbaked'},
                                              {'label':'hammerduke', 'value':'hammerduke'},
                                              {'label':'hammertoss', 'value':'hammertoss'},
                                              {'label':'happywork', 'value':'happywork'},
                                              {'label':'hardrain', 'value':'hardrain'},
                                              {'label':'hatman', 'value':'hatman'},
                                              {'label':'havex rat', 'value':'havex rat'},
                                              {'label':'havij', 'value':'havij'},
                                              {'label':'hawup', 'value':'hawup'},
                                              {'label':'haymaker', 'value':'haymaker'},
                                              {'label':'hcdloader', 'value':'hcdloader'},
                                              {'label':'hdoor', 'value':'hdoor'},
                                              {'label':'helauto', 'value':'helauto'},
                                              {'label':'hello', 'value':'hello'},
                                              {'label':'hellobridge', 'value':'hellobridge'},
                                              {'label':'heriplor', 'value':'heriplor'},
                                              {'label':'hermes', 'value':'hermes'},
                                              {'label':'hidedrv', 'value':'hidedrv'},
                                              {'label':'hightide', 'value':'hightide'},
                                              {'label':'hikit', 'value':'hikit'},
                                              {'label':'homefry', 'value':'homefry'},
                                              {'label':'hoplight', 'value':'hoplight'},
                                              {'label':'htdndownloader', 'value':'htdndownloader'},
                                              {'label':'html5 encoding', 'value':'html5 encoding'},
                                              {'label':'htran', 'value':'htran'},
                                              {'label':'httpbrowser', 'value':'httpbrowser'},
                                              {'label':'httpclient', 'value':'httpclient'},
                                              {'label':'httptunnel', 'value':'httptunnel'},
                                              {'label':'hunter', 'value':'hunter'},
                                              {'label':'hupigon', 'value':'hupigon'},
                                              {'label':'hydraq', 'value':'hydraq'},
                                              {'label':'hyperbro', 'value':'hyperbro'},
                                              {'label':'icedcoffeer', 'value':'icedcoffeer'},
                                              {'label':'igt supertool', 'value':'igt supertool'},
                                              {'label':'imecab', 'value':'imecab'},
                                              {'label':'imminent monitor rat', 'value':'imminent monitor rat'},
                                              {'label':'impacket', 'value':'impacket'},
                                              {'label':'industroyer', 'value':'industroyer'},
                                              {'label':'inveigh', 'value':'inveigh'},
                                              {'label':'ipconfig', 'value':'ipconfig'},
                                              {'label':'ironhalo', 'value':'ironhalo'},
                                              {'label':'ispysoftware', 'value':'ispysoftware'},
                                              {'label':'isr stealer', 'value':'isr stealer'},
                                              {'label':'isspace', 'value':'isspace'},
                                              {'label':'ixeshe', 'value':'ixeshe'},
                                              {'label':'jaderat', 'value':'jaderat'},
                                              {'label':'jaff', 'value':'jaff'},
                                              {'label':'jasus', 'value':'jasus'},
                                              {'label':'jerseymikes', 'value':'jerseymikes'},
                                              {'label':'jhuhugit', 'value':'jhuhugit'},
                                              {'label':'joanap', 'value':'joanap'},
                                              {'label':'jokra', 'value':'jokra'},
                                              {'label':'jpin', 'value':'jpin'},
                                              {'label':'js flash', 'value':'js flash'},
                                              {'label':'kaba', 'value':'kaba'},
                                              {'label':'kagent', 'value':'kagent'},
                                              {'label':'karae', 'value':'karae'},
                                              {'label':'karagany', 'value':'karagany'},
                                              {'label':'kasperagent', 'value':'kasperagent'},
                                              {'label':'kazuar', 'value':'kazuar'},
                                              {'label':'kegotip', 'value':'kegotip'},
                                              {'label':'kerrdown', 'value':'kerrdown'},
                                              {'label':'kevdroid', 'value':'kevdroid'},
                                              {'label':'keybase', 'value':'keybase'},
                                              {'label':'keyboy', 'value':'keyboy'},
                                              {'label':'keymarble', 'value':'keymarble'},
                                              {'label':'khrat', 'value':'khrat'},
                                              {'label':'killdisk', 'value':'killdisk'},
                                              {'label':'kivars', 'value':'kivars'},
                                              {'label':'klrd', 'value':'klrd'},
                                              {'label':'koadic', 'value':'koadic'},
                                              {'label':'komplex', 'value':'komplex'},
                                              {'label':'komprogo', 'value':'komprogo'},
                                              {'label':'kopiluwak', 'value':'kopiluwak'},
                                              {'label':'koredos', 'value':'koredos'},
                                              {'label':'kportscan', 'value':'kportscan'},
                                              {'label':'krypton', 'value':'krypton'},
                                              {'label':'ksl0t', 'value':'ksl0t'},
                                              {'label':'kurton', 'value':'kurton'},
                                              {'label':'kwampirs', 'value':'kwampirs'},
                                              {'label':'lambert', 'value':'lambert'},
                                              {'label':'lazagne', 'value':'lazagne'},
                                              {'label':'lazarus', 'value':'lazarus'},
                                              {'label':'lazycat', 'value':'lazycat'},
                                              {'label':'leash', 'value':'leash'},
                                              {'label':'leouncia', 'value':'leouncia'},
                                              {'label':'lightneuron', 'value':'lightneuron'},
                                              {'label':'lightsout', 'value':'lightsout'},
                                              {'label':'linfo', 'value':'linfo'},
                                              {'label':'listrix', 'value':'listrix'},
                                              {'label':'lockergoga', 'value':'lockergoga'},
                                              {'label':'locky', 'value':'locky'},
                                              {'label':'lojax', 'value':'lojax'},
                                              {'label':'lokibot', 'value':'lokibot'},
                                              {'label':'lolbins', 'value':'lolbins'},
                                              {'label':'lslsass', 'value':'lslsass'},
                                              {'label':'luder', 'value':'luder'},
                                              {'label':'lunchmoney', 'value':'lunchmoney'},
                                              {'label':'lurid', 'value':'lurid'},
                                              {'label':'macdownloader', 'value':'macdownloader'},
                                              {'label':'machete', 'value':'machete'},
                                              {'label':'mailpassview', 'value':'mailpassview'},
                                              {'label':'maintools.js', 'value':'maintools.js'},
                                              {'label':'malicious rar archives', 'value':'malicious rar archives'},
                                              {'label':'manitsme', 'value':'manitsme'},
                                              {'label':'manuscrypt', 'value':'manuscrypt'},
                                              {'label':'mapiget', 'value':'mapiget'},
                                              {'label':'matryoshka', 'value':'matryoshka'},
                                              {'label':'matryoshka rat', 'value':'matryoshka rat'},
                                              {'label':'mazerunner', 'value':'mazerunner'},
                                              {'label':'mbr eraser', 'value':'mbr eraser'},
                                              {'label':'mbr killer', 'value':'mbr killer'},
                                              {'label':'mechaflounder mimikatz', 'value':'mechaflounder mimikatz'},
                                              {'label':'mechanical', 'value':'mechanical'},
                                              {'label':'meek', 'value':'meek'},
                                              {'label':'metasploit', 'value':'metasploit'},
                                              {'label':'meterpreter', 'value':'meterpreter'},
                                              {'label':'metushy', 'value':'metushy'},
                                              {'label':'micropsia', 'value':'micropsia'},
                                              {'label':'milkmaid', 'value':'milkmaid'},
                                              {'label':'mimikatz', 'value':'mimikatz'},
                                              {'label':'miniasp', 'value':'miniasp'},
                                              {'label':'minidionis', 'value':'minidionis'},
                                              {'label':'miniduke', 'value':'miniduke'},
                                              {'label':'minzen', 'value':'minzen'},
                                              {'label':'miragefox', 'value':'miragefox'},
                                              {'label':'mis-type', 'value':'mis-type'},
                                              {'label':'misdat', 'value':'misdat'},
                                              {'label':'mivast', 'value':'mivast'},
                                              {'label':'mobileorder', 'value':'mobileorder'},
                                              {'label':'molerat loader', 'value':'molerat loader'},
                                              {'label':'mongall', 'value':'mongall'},
                                              {'label':'more_eggs', 'value':'more_eggs'},
                                              {'label':'mosquito', 'value':'mosquito'},
                                              {'label':'mpkbot', 'value':'mpkbot'},
                                              {'label':'ms exchange tool', 'value':'ms exchange tool'},
                                              {'label':'msupdater', 'value':'msupdater'},
                                              {'label':'muirim', 'value':'muirim'},
                                              {'label':'murkytop', 'value':'murkytop'},
                                              {'label':'mydoom', 'value':'mydoom'},
                                              {'label':'mytob', 'value':'mytob'},
                                              {'label':'mzcookiesview', 'value':'mzcookiesview'},
                                              {'label':'n1stagent', 'value':'n1stagent'},
                                              {'label':'naid', 'value':'naid'},
                                              {'label':'naikon', 'value':'naikon'},
                                              {'label':'nan', 'value':'nan'},
                                              {'label':'nanhaishu', 'value':'nanhaishu'},
                                              {'label':'nanocore', 'value':'nanocore'},
                                              {'label':'nanocore rat', 'value':'nanocore rat'},
                                              {'label':'nautilus', 'value':'nautilus'},
                                              {'label':'navrat', 'value':'navrat'},
                                              {'label':'nbtscan', 'value':'nbtscan'},
                                              {'label':'nbtstat', 'value':'nbtstat'},
                                              {'label':'ndiskmonitor', 'value':'ndiskmonitor'},
                                              {'label':'necurs', 'value':'necurs'},
                                              {'label':'ned worm', 'value':'ned worm'},
                                              {'label':'nemim', 'value':'nemim'},
                                              {'label':'nerex', 'value':'nerex'},
                                              {'label':'net crawler', 'value':'net crawler'},
                                              {'label':'net.exe', 'value':'net.exe'},
                                              {'label':'neteagle', 'value':'neteagle'},
                                              {'label':'netexec', 'value':'netexec'},
                                              {'label':'netscan', 'value':'netscan'},
                                              {'label':'nettraveler', 'value':'nettraveler'},
                                              {'label':'netwire', 'value':'netwire'},
                                              {'label':'netwire rc', 'value':'netwire rc'},
                                              {'label':'netwoolger', 'value':'netwoolger'},
                                              {'label':'network password recovery', 'value':'network password recovery'},
                                              {'label':'neuron', 'value':'neuron'},
                                              {'label':'neutrino', 'value':'neutrino'},
                                              {'label':'newcore rat', 'value':'newcore rat'},
                                              {'label':'newct', 'value':'newct'},
                                              {'label':'newct2', 'value':'newct2'},
                                              {'label':'newsreels', 'value':'newsreels'},
                                              {'label':'nflog', 'value':'nflog'},
                                              {'label':'nidiran', 'value':'nidiran'},
                                              {'label':'nioupale', 'value':'nioupale'},
                                              {'label':'nishang', 'value':'nishang'},
                                              {'label':'njrat', 'value':'njrat'},
                                              {'label':'nmap', 'value':'nmap'},
                                              {'label':'nokki', 'value':'nokki'},
                                              {'label':'non-sucking service manager (nssm)', 'value':'non-sucking service manager (nssm)'},
                                              {'label':'nukesped', 'value':'nukesped'},
                                              {'label':'odinaff', 'value':'odinaff'},
                                              {'label':'oldbait', 'value':'oldbait'},
                                              {'label':'oldrea', 'value':'oldrea'},
                                              {'label':'orangeade', 'value':'orangeade'},
                                              {'label':'orz', 'value':'orz'},
                                              {'label':'osinfo', 'value':'osinfo'},
                                              {'label':'osx_oceanlotus.d', 'value':'osx_oceanlotus.d'},
                                              {'label':'outlook backdoor', 'value':'outlook backdoor'},
                                              {'label':'owaauth', 'value':'owaauth'},
                                              {'label':'paladin', 'value':'paladin'},
                                              {'label':'pallas', 'value':'pallas'},
                                              {'label':'pasam', 'value':'pasam'},
                                              {'label':'pass-the-hash toolkit', 'value':'pass-the-hash toolkit'},
                                              {'label':'passkilldisk', 'value':'passkilldisk'},
                                              {'label':'pcclient', 'value':'pcclient'},
                                              {'label':'pcshare', 'value':'pcshare'},
                                              {'label':'penguin turla', 'value':'penguin turla'},
                                              {'label':'pfinet', 'value':'pfinet'},
                                              {'label':'pgift', 'value':'pgift'},
                                              {'label':'phandoor', 'value':'phandoor'},
                                              {'label':'philadelphia', 'value':'philadelphia'},
                                              {'label':'phisherly', 'value':'phisherly'},
                                              {'label':'phishery', 'value':'phishery'},
                                              {'label':'phoreal', 'value':'phoreal'},
                                              {'label':'photo', 'value':'photo'},
                                              {'label':'phpmailer', 'value':'phpmailer'},
                                              {'label':'phpspy', 'value':'phpspy'},
                                              {'label':'pinchduke', 'value':'pinchduke'},
                                              {'label':'pioneer', 'value':'pioneer'},
                                              {'label':'pirpi', 'value':'pirpi'},
                                              {'label':'pisloader', 'value':'pisloader'},
                                              {'label':'pitty', 'value':'pitty'},
                                              {'label':'plaintee', 'value':'plaintee'},
                                              {'label':'plead', 'value':'plead'},
                                              {'label':'plexor', 'value':'plexor'},
                                              {'label':'plink', 'value':'plink'},
                                              {'label':'plugx', 'value':'plugx'},
                                              {'label':'plugxl', 'value':'plugxl'},
                                              {'label':'pngdowner', 'value':'pngdowner'},
                                              {'label':'pocodown', 'value':'pocodown'},
                                              {'label':'poison ivy', 'value':'poison ivy'},
                                              {'label':'pony', 'value':'pony'},
                                              {'label':'poohmilk loader', 'value':'poohmilk loader'},
                                              {'label':'pooraim', 'value':'pooraim'},
                                              {'label':'popeye', 'value':'popeye'},
                                              {'label':'portqry.exe', 'value':'portqry.exe'},
                                              {'label':'poshc2', 'value':'poshc2'},
                                              {'label':'poshspy', 'value':'poshspy'},
                                              {'label':'powbat', 'value':'powbat'},
                                              {'label':'powerduke', 'value':'powerduke'},
                                              {'label':'powerpipe', 'value':'powerpipe'},
                                              {'label':'powerratankba', 'value':'powerratankba'},
                                              {'label':'powershell', 'value':'powershell'},
                                              {'label':'powersource', 'value':'powersource'},
                                              {'label':'powersploit', 'value':'powersploit'},
                                              {'label':'powerspritz', 'value':'powerspritz'},
                                              {'label':'powerstats', 'value':'powerstats'},
                                              {'label':'powerton', 'value':'powerton'},
                                              {'label':'predator pain', 'value':'predator pain'},
                                              {'label':'procdump', 'value':'procdump'},
                                              {'label':'proxysvc', 'value':'proxysvc'},
                                              {'label':'psexec', 'value':'psexec'},
                                              {'label':'psylo', 'value':'psylo'},
                                              {'label':'pteranodon', 'value':'pteranodon'},
                                              {'label':'punchbuggy', 'value':'punchbuggy'},
                                              {'label':'punchtrack', 'value':'punchtrack'},
                                              {'label':'pupyrat', 'value':'pupyrat'},
                                              {'label':'putty', 'value':'putty'},
                                              {'label':'pvcout', 'value':'pvcout'},
                                              {'label':'pwdump', 'value':'pwdump'},
                                              {'label':'quasarrat', 'value':'quasarrat'},
                                              {'label':'rambo', 'value':'rambo'},
                                              {'label':'rapidstealer', 'value':'rapidstealer'},
                                              {'label':'rarstar', 'value':'rarstar'},
                                              {'label':'rarstone', 'value':'rarstone'},
                                              {'label':'ratabankapos', 'value':'ratabankapos'},
                                              {'label':'rats', 'value':'rats'},
                                              {'label':'rawdisk', 'value':'rawdisk'},
                                              {'label':'rawpos', 'value':'rawpos'},
                                              {'label':'rcpscan', 'value':'rcpscan'},
                                              {'label':'redleaves', 'value':'redleaves'},
                                              {'label':'regeorge', 'value':'regeorge'},
                                              {'label':'regin', 'value':'regin'},
                                              {'label':'remcom', 'value':'remcom'},
                                              {'label':'remcos', 'value':'remcos'},
                                              {'label':'remexi', 'value':'remexi'},
                                              {'label':'remote desktop passview', 'value':'remote desktop passview'},
                                              {'label':'remsec', 'value':'remsec'},
                                              {'label':'resetter', 'value':'resetter'},
                                              {'label':'responder', 'value':'responder'},
                                              {'label':'revenge rat', 'value':'revenge rat'},
                                              {'label':'rifdoor', 'value':'rifdoor'},
                                              {'label':'rikamanu', 'value':'rikamanu'},
                                              {'label':'riptide', 'value':'riptide'},
                                              {'label':'rising sun', 'value':'rising sun'},
                                              {'label':'rms', 'value':'rms'},
                                              {'label':'rockloader', 'value':'rockloader'},
                                              {'label':'roguerobin', 'value':'roguerobin'},
                                              {'label':'rokrat', 'value':'rokrat'},
                                              {'label':'romeonc', 'value':'romeonc'},
                                              {'label':'roseam', 'value':'roseam'},
                                              {'label':'royal dns', 'value':'royal dns'},
                                              {'label':'royalcli', 'value':'royalcli'},
                                              {'label':'rtm', 'value':'rtm'},
                                              {'label':'ruler', 'value':'ruler'},
                                              {'label':'runhelp.exe', 'value':'runhelp.exe'},
                                              {'label':'ryuk', 'value':'ryuk'},
                                              {'label':'s-type', 'value':'s-type'},
                                              {'label':'sakula', 'value':'sakula'},
                                              {'label':'salgorea', 'value':'salgorea'},
                                              {'label':'sarit', 'value':'sarit'},
                                              {'label':'scanbox', 'value':'scanbox'},
                                              {'label':'scote', 'value':'scote'},
                                              {'label':'sdelete', 'value':'sdelete'},
                                              {'label':'seadaddy', 'value':'seadaddy'},
                                              {'label':'seaduke', 'value':'seaduke'},
                                              {'label':'searchfire', 'value':'searchfire'},
                                              {'label':'seasalt', 'value':'seasalt'},
                                              {'label':'seaweed', 'value':'seaweed'},
                                              {'label':'sechack', 'value':'sechack'},
                                              {'label':'sedkit', 'value':'sedkit'},
                                              {'label':'sedll', 'value':'sedll'},
                                              {'label':'sednit', 'value':'sednit'},
                                              {'label':'sedreco', 'value':'sedreco'},
                                              {'label':'seduploader', 'value':'seduploader'},
                                              {'label':'sekur', 'value':'sekur'},
                                              {'label':'servhelper', 'value':'servhelper'},
                                              {'label':'shadowpad winnti', 'value':'shadowpad winnti'},
                                              {'label':'shadyrat', 'value':'shadyrat'},
                                              {'label':'shamoon', 'value':'shamoon'},
                                              {'label':'shapeshift', 'value':'shapeshift'},
                                              {'label':'shareip', 'value':'shareip'},
                                              {'label':'sharpknot', 'value':'sharpknot'},
                                              {'label':'sharpstats', 'value':'sharpstats'},
                                              {'label':'sheeprat', 'value':'sheeprat'},
                                              {'label':'shelltea', 'value':'shelltea'},
                                              {'label':'shifu', 'value':'shifu'},
                                              {'label':'shipshape', 'value':'shipshape'},
                                              {'label':'shoorback', 'value':'shoorback'},
                                              {'label':'shotput', 'value':'shotput'},
                                              {'label':'shutterspeed', 'value':'shutterspeed'},
                                              {'label':'sierranc', 'value':'sierranc'},
                                              {'label':'silence', 'value':'silence'},
                                              {'label':'sisfader', 'value':'sisfader'},
                                              {'label':'skipper', 'value':'skipper'},
                                              {'label':'slowdrift', 'value':'slowdrift'},
                                              {'label':'smb hacking tools', 'value':'smb hacking tools'},
                                              {'label':'smbmap', 'value':'smbmap'},
                                              {'label':'smbscan', 'value':'smbscan'},
                                              {'label':'smbtrap', 'value':'smbtrap'},
                                              {'label':'snake', 'value':'snake'},
                                              {'label':'sniffpass', 'value':'sniffpass'},
                                              {'label':'snugride', 'value':'snugride'},
                                              {'label':'socksbot', 'value':'socksbot'},
                                              {'label':'sofacy', 'value':'sofacy'},
                                              {'label':'softperfect network scanner', 'value':'softperfect network scanner'},
                                              {'label':'soundbite', 'value':'soundbite'},
                                              {'label':'sourface', 'value':'sourface'},
                                              {'label':'spaceship', 'value':'spaceship'},
                                              {'label':'spedear', 'value':'spedear'},
                                              {'label':'spicyomelette', 'value':'spicyomelette'},
                                              {'label':'spindest', 'value':'spindest'},
                                              {'label':'splinterrat', 'value':'splinterrat'},
                                              {'label':'spwebmember', 'value':'spwebmember'},
                                              {'label':'sqlmap', 'value':'sqlmap'},
                                              {'label':'sqlrat', 'value':'sqlrat'},
                                              {'label':'sslmm', 'value':'sslmm'},
                                              {'label':'starloader', 'value':'starloader'},
                                              {'label':'starsypound', 'value':'starsypound'},
                                              {'label':'stealer builder', 'value':'stealer builder'},
                                              {'label':'steladoc', 'value':'steladoc'},
                                              {'label':'stickyfingers', 'value':'stickyfingers'},
                                              {'label':'streamex', 'value':'streamex'},
                                              {'label':'subbrute', 'value':'subbrute'},
                                              {'label':'sublist3r', 'value':'sublist3r'},
                                              {'label':'svcmondr', 'value':'svcmondr'},
                                              {'label':'sword', 'value':'sword'},
                                              {'label':'synflooder', 'value':'synflooder'},
                                              {'label':'sys10', 'value':'sys10'},
                                              {'label':'syscon', 'value':'syscon'},
                                              {'label':'sysget', 'value':'sysget'},
                                              {'label':'sysmain', 'value':'sysmain'},
                                              {'label':'systeminfo', 'value':'systeminfo'},
                                              {'label':'tabmsgsql', 'value':'tabmsgsql'},
                                              {'label':'taidoor', 'value':'taidoor'},
                                              {'label':'tapaoux', 'value':'tapaoux'},
                                              {'label':'tarsip', 'value':'tarsip'},
                                              {'label':'tasklist', 'value':'tasklist'},
                                              {'label':'tavdig', 'value':'tavdig'},
                                              {'label':'tdiscoverer.', 'value':'tdiscoverer.'},
                                              {'label':'tdrop', 'value':'tdrop'},
                                              {'label':'tdrop2', 'value':'tdrop2'},
                                              {'label':'tdtess', 'value':'tdtess'},
                                              {'label':'team viewer', 'value':'team viewer'},
                                              {'label':'teamviewer', 'value':'teamviewer'},
                                              {'label':'terracotta vpn', 'value':'terracotta vpn'},
                                              {'label':'textmate', 'value':'textmate'},
                                              {'label':'the trick', 'value':'the trick'},
                                              {'label':'threebyte', 'value':'threebyte'},
                                              {'label':'tidepool', 'value':'tidepool'},
                                              {'label':'tinymet', 'value':'tinymet'},
                                              {'label':'tinytyphon wscspl', 'value':'tinytyphon wscspl'},
                                              {'label':'tinyzbot', 'value':'tinyzbot'},
                                              {'label':'titan', 'value':'titan'},
                                              {'label':'torn rat', 'value':'torn rat'},
                                              {'label':'triplefantasy', 'value':'triplefantasy'},
                                              {'label':'trisis', 'value':'trisis'},
                                              {'label':'triton', 'value':'triton'},
                                              {'label':'trochilus rat', 'value':'trochilus rat'},
                                              {'label':'troy', 'value':'troy'},
                                              {'label':'truvasys', 'value':'truvasys'},
                                              {'label':'ttcalc', 'value':'ttcalc'},
                                              {'label':'turla', 'value':'turla'},
                                              {'label':'turnedup', 'value':'turnedup'},
                                              {'label':'typeframe', 'value':'typeframe'},
                                              {'label':'ultravnc', 'value':'ultravnc'},
                                              {'label':'upatre', 'value':'upatre'},
                                              {'label':'uppercut', 'value':'uppercut'},
                                              {'label':'uroburos', 'value':'uroburos'},
                                              {'label':'usbstealer', 'value':'usbstealer'},
                                              {'label':'vamp', 'value':'vamp'},
                                              {'label':'vasport', 'value':'vasport'},
                                              {'label':'vb flash', 'value':'vb flash'},
                                              {'label':'viperrat', 'value':'viperrat'},
                                              {'label':'vminst', 'value':'vminst'},
                                              {'label':'vnc', 'value':'vnc'},
                                              {'label':'volgmer', 'value':'volgmer'},
                                              {'label':'w32times', 'value':'w32times'},
                                              {'label':'wannacry', 'value':'wannacry'},
                                              {'label':'waterspout', 'value':'waterspout'},
                                              {'label':'wce', 'value':'wce'},
                                              {'label':'webbrowserpassview', 'value':'webbrowserpassview'},
                                              {'label':'webc2-adspace', 'value':'webc2-adspace'},
                                              {'label':'webc2-ausov', 'value':'webc2-ausov'},
                                              {'label':'webc2-bolid', 'value':'webc2-bolid'},
                                              {'label':'webc2-cson', 'value':'webc2-cson'},
                                              {'label':'webc2-div', 'value':'webc2-div'},
                                              {'label':'webc2-greencat', 'value':'webc2-greencat'},
                                              {'label':'webc2-head', 'value':'webc2-head'},
                                              {'label':'webc2-kt3', 'value':'webc2-kt3'},
                                              {'label':'webc2-qbp', 'value':'webc2-qbp'},
                                              {'label':'webc2-rave', 'value':'webc2-rave'},
                                              {'label':'webc2-table', 'value':'webc2-table'},
                                              {'label':'webc2-ugx', 'value':'webc2-ugx'},
                                              {'label':'webc2-yahoo', 'value':'webc2-yahoo'},
                                              {'label':'wellmess', 'value':'wellmess'},
                                              {'label':'wellmail', 'value':'wellmail'},
                                              {'label':'whiteatlas', 'value':'whiteatlas'},
                                              {'label':'whitebear', 'value':'whitebear'},
                                              {'label':'whoami', 'value':'whoami'},
                                              {'label':'wiarp', 'value':'wiarp'},
                                              {'label':'wii', 'value':'wii'},
                                              {'label':'windows credential editor', 'value':'windows credential editor'},
                                              {'label':'windshield', 'value':'windshield'},
                                              {'label':'winerack', 'value':'winerack'},
                                              {'label':'winexe', 'value':'winexe'},
                                              {'label':'wingbird', 'value':'wingbird'},
                                              {'label':'winids', 'value':'winids'},
                                              {'label':'winmm', 'value':'winmm'},
                                              {'label':'winnti', 'value':'winnti'},
                                              {'label':'winrar', 'value':'winrar'},
                                              {'label':'winsloader', 'value':'winsloader'},
                                              {'label':'wipbot', 'value':'wipbot'},
                                              {'label':'witchcoven', 'value':'witchcoven'},
                                              {'label':'wmi', 'value':'wmi'},
                                              {'label':'wmi ghost', 'value':'wmi ghost'},
                                              {'label':'wndtest', 'value':'wndtest'},
                                              {'label':'wolfrat', 'value':'wolfrat'},
                                              {'label':'woolger', 'value':'woolger'},
                                              {'label':'wpscan', 'value':'wpscan'},
                                              {'label':'wraith', 'value':'wraith'},
                                              {'label':'wso', 'value':'wso'},
                                              {'label':'x-agent', 'value':'x-agent'},
                                              {'label':'xbow', 'value':'xbow'},
                                              {'label':'xsplus', 'value':'xsplus'},
                                              {'label':'xtremerat', 'value':'xtremerat'},
                                              {'label':'xtunnel', 'value':'xtunnel'},
                                              {'label':'xxmm', 'value':'xxmm'},
                                              {'label':'yahoyah', 'value':'yahoyah'},
                                              {'label':'yort', 'value':'yort'},
                                              {'label':'zebrocy', 'value':'zebrocy'},
                                              {'label':'zerot', 'value':'zerot'},
                                              {'label':'zeus', 'value':'zeus'},
                                              {'label':'zhmimikatz', 'value':'zhmimikatz'},
                                              {'label':'ziptoken', 'value':'ziptoken'},
                                              {'label':'zpp', 'value':'zpp'},
                                              {'label':'zwshell', 'value':'zwshell'},
                                              {'label':'zxshell', 'value':'zxshell'}
                                              ],
                                      style={
                                             'margin': 7,
                                             'width': '150px',
                                             'margin-left' : '43px',
                                            }

                        ), className="one columns"),

              ], className="row"),


        html.Div([
          dash_table.DataTable(id='apt-table',
                               columns=[{"name": i, "id": i} for i in APTZ.columns],
                               row_selectable='single',
                               data=APTZ.to_dict('records'),
                               selected_rows=[],
                               style_table={'height': '80vh','width': "auto", 'overflowY': 'scroll' },
                               style_cell={'whiteSpace': 'normal','height':'auto'})
                 ]),

        html.Div(children=[dcc.Markdown(
                   "  2020 [CTA](https://github.com/ishikawa-rei)  All Rights Reserved.")], style={'marginLeft': 5, 'marginRight': 5, 'marginTop': 10, 'marginBottom': 10,
               'backgroundColor':'#F7FBFE',
               'border': 'thin lightgrey dashed', 'padding': '6px 0px 0px 8px'}),

        ]),
    ])

])

# TFIDF bar graph function for filtering
@app.callback(Output('graph-output', 'figure'),
              [Input('dropdown', 'value'),
               Input('date-input', 'start_date'),
               Input('date-input', 'end_date')])
def render_graph(ngram,start_date,end_date):

  df_data = get_mostfrequent_data_all_daterange(ngram,start_date,end_date)

  most_frequent_words_values = df_data[1][:30]
  most_frequent_words = df_data[0][:30]

  fig = go.Figure([go.Bar(x=most_frequent_words_values[::-1], y=most_frequent_words[::-1],orientation='h',name='value1')])
  fig.update_layout(height=680,margin=dict(l=160,r=0,b=15,t=0,pad=0))
  #  fig.update_layout(title="<b>Threat Post Term Ranking</b>", font_family="Courier New", height=680,margin=dict(l=160,r=0,b=15,t=40,pad=0))
  return (fig)


# Tweet data filtering by clicking on TFIDF bar graph
@app.callback(
    Output('tweet-dataframe', 'data'),        # the output goes to
    [Input('graph-output', 'clickData')])     # the input to the datatable upload container data variable is the clickdata from basic-interactions graph
def display_click_data(clickData):
# clickData is the term label taken when you click on the bargraph bar###
    if clickData != None: # on first load no click
        label = str(clickData['points'][0]['label'])
    else:
        label = "security"

    
    df1 = get_cleaned_text_data_original(label)
    df1.rename(columns={'sql_tweet_text': 'text', 'sql_platform': 'platform','sql_sentiment': 'sentiment','sql_datetime_object':'datetime'}, inplace=True)

    return df1.to_dict('rows')



@app.callback(
    Output('apt-table', 'data'),
    [Input('dropdown-countries', 'value'),
     Input('dropdown-sectors', 'value'),
     Input('dropdown-location', 'value'),
     Input('dropdown-tools', 'value')])
def filter_apt_map(country,sector,origin,tool):
  APTZ = pd.read_csv('APTDB.csv',encoding="latin-1")

  origin = origin.upper()

  if country == 'A' and sector == 'A' and origin == 'A' and tool == 'A':
    APTZ = pd.read_csv('APTDB.csv',encoding="latin-1")
  elif country == 'A' and sector == 'A' and origin == 'A' and len(tool) > 1:
    APTZ = APTZ[APTZ['TOOL'].str.contains(tool) == True]
  elif country == 'A' and sector == 'A' and len(origin) > 1 and tool == 'A':
    APTZ = APTZ[APTZ['Alleged Location'].str.contains(origin) == True]
  elif country == 'A' and sector == 'A' and len(origin) > 1 and len(tool) > 1:
    APTZ = APTZ[APTZ['TOOL'].str.contains(tool) & APTZ['Alleged Location'].str.contains(origin)]
  elif country == 'A' and len(sector) > 1 and origin == 'A' and tool == 'A':
    APTZ = APTZ[APTZ['Targeted Sectors'].str.contains(sector) == True]
  elif country == 'A' and len(sector) > 1 and origin == 'A' and len(tool) > 1:
    APTZ = APTZ[APTZ['TOOL'].str.contains(tool) & APTZ['Targeted Sectors'].str.contains(sector)]
  elif country == 'A' and len(sector) > 1 and len(origin) > 1 and tool == 'A':
    APTZ = APTZ[APTZ['Alleged Location'].str.contains(origin) & APTZ['Targeted Sectors'].str.contains(sector)]
  elif country == 'A' and len(sector) > 1 and len(origin) > 1 and len(tool) > 1:
    APTZ = APTZ[APTZ['Alleged Location'].str.contains(origin) & APTZ['Targeted Sectors'].str.contains(sector) & APTZ['TOOL'].str.contains(tool)]
  elif len(country) > 1 and sector == 'A' and origin == 'A' and tool == 'A':
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) == True]
  elif len(country) > 1 and sector == 'A' and origin == 'A' and len(tool) > 1:
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['TOOL'].str.contains(tool)]
  elif len(country) > 1 and sector == 'A' and len(origin) > 1 and tool == 'A':
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Alleged Location'].str.contains(origin)]
  elif len(country) > 1 and sector == 'A' and len(origin) > 1 and len(tool) > 1:
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Alleged Location'].str.contains(origin) & APTZ['TOOL'].str.contains(tool)]
  elif len(country) > 1 and len(sector) > 1 and origin == 'A' and tool == 'A':
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Targeted Sectors'].str.contains(sector)]
  elif len(country) > 1 and len(sector) > 1 and origin == 'A' and len(tool) > 1:
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Targeted Sectors'].str.contains(sector) & APTZ['TOOL'].str.contains(tool)]
  elif len(country) > 1 and len(sector) > 1 and len(origin) > 1 and tool == 'A':
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Targeted Sectors'].str.contains(sector) & APTZ['Alleged Location'].str.contains(origin)]
  elif len(country) > 1 and len(sector) > 1 and len(origin) > 1 and len(tool) > 1:
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Targeted Sectors'].str.contains(sector) & APTZ['Alleged Location'].str.contains(origin) & APTZ['TOOL'].str.contains(tool)]

  return APTZ.to_dict('rows')


@app.callback(Output("apt-map", "figure"),
             [Input("apt-table", "selected_rows"),
              Input('dropdown-countries', 'value'),
              Input('dropdown-sectors', 'value'),
              Input('dropdown-location', 'value'),
              Input('dropdown-tools', 'value')])
def update_map(selected,country,sector,origin,tool):
  APTZ = pd.read_csv('APTDB.csv',encoding="latin-1")
  origin = origin.upper()

  if country == 'A' and sector == 'A' and origin == 'A' and tool == 'A':
    APTZ = pd.read_csv('APTDB.csv',encoding="latin-1")
  elif country == 'A' and sector == 'A' and origin == 'A' and len(tool) > 1:
    APTZ = APTZ[APTZ['TOOL'].str.contains(tool) == True]
  elif country == 'A' and sector == 'A' and len(origin) > 1 and tool == 'A':
    APTZ = APTZ[APTZ['Alleged Location'].str.contains(origin) == True]
  elif country == 'A' and sector == 'A' and len(origin) > 1 and len(tool) > 1:
    APTZ = APTZ[APTZ['TOOL'].str.contains(tool) & APTZ['Alleged Location'].str.contains(origin)]
  elif country == 'A' and len(sector) > 1 and origin == 'A' and tool == 'A':
    APTZ = APTZ[APTZ['Targeted Sectors'].str.contains(sector) == True]
  elif country == 'A' and len(sector) > 1 and origin == 'A' and len(tool) > 1:
    APTZ = APTZ[APTZ['TOOL'].str.contains(tool) & APTZ['Targeted Sectors'].str.contains(sector)]
  elif country == 'A' and len(sector) > 1 and len(origin) > 1 and tool == 'A':
    APTZ = APTZ[APTZ['Alleged Location'].str.contains(origin) & APTZ['Targeted Sectors'].str.contains(sector)]
  elif country == 'A' and len(sector) > 1 and len(origin) > 1 and len(tool) > 1:
    APTZ = APTZ[APTZ['Alleged Location'].str.contains(origin) & APTZ['Targeted Sectors'].str.contains(sector) & APTZ['TOOL'].str.contains(tool)]
  elif len(country) > 1 and sector == 'A' and origin == 'A' and tool == 'A':
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) == True]
  elif len(country) > 1 and sector == 'A' and origin == 'A' and len(tool) > 1:
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['TOOL'].str.contains(tool)]
  elif len(country) > 1 and sector == 'A' and len(origin) > 1 and tool == 'A':
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Alleged Location'].str.contains(origin)]
  elif len(country) > 1 and sector == 'A' and len(origin) > 1 and len(tool) > 1:
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Alleged Location'].str.contains(origin) & APTZ['TOOL'].str.contains(tool)]
  elif len(country) > 1 and len(sector) > 1 and origin == 'A' and tool == 'A':
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Targeted Sectors'].str.contains(sector)]
  elif len(country) > 1 and len(sector) > 1 and origin == 'A' and len(tool) > 1:
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Targeted Sectors'].str.contains(sector) & APTZ['TOOL'].str.contains(tool)]
  elif len(country) > 1 and len(sector) > 1 and len(origin) > 1 and tool == 'A':
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Targeted Sectors'].str.contains(sector) & APTZ['Alleged Location'].str.contains(origin)]
  elif len(country) > 1 and len(sector) > 1 and len(origin) > 1 and len(tool) > 1:
    APTZ = APTZ[APTZ['TARGETED COUNTRIES'].str.contains(country) & APTZ['Targeted Sectors'].str.contains(sector) & APTZ['Alleged Location'].str.contains(origin) & APTZ['TOOL'].str.contains(tool)]

  APTZ.reset_index(inplace=True,drop=True)

  if len(selected) == 0:
    line = 0
    abrevs = ["VAT"]
  else:
    line = selected[0]
    try:
      abrevs = (APTZ.loc[line][5]).split(',')
    except:
      abrevs = ["VATICAN CITY"]

    abrevs = [world_abbreviations[i.strip()] for i in abrevs]

  fig = px.choropleth(locations=abrevs)
  fig.update_layout(margin={"r":0,"t":0,"l":0,"b":5}, showlegend=False)

  return (fig)


if __name__ == '__main__':
    app.run_server(debug=True)