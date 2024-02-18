import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st
import os
import pymysql
from sqlalchemy import create_engine, text
import sqlalchemy
from plotly.subplots import make_subplots as sp
#from load_css import local_css

st.set_page_config(page_title='Dashboard',
                   layout='wide'
)
#local_css("style.css")

# st.write(
#     "Has environment variables been set:",
#     os.environ["db_username"] == st.secrets["db_username"],
# )

# user = st.secrets["db_username"]
# pw = st.secrets["db_password"]

# engine = create_engine(
#     "mysql://{user}:{pw}@172.21.64.40:3306/cp_zendesk".format(
#     user=user, pw=pw
#     ))

# with engine.connect() as conn:
#     result = conn.execute(text('SELECT * FROM cp_zendesk.cp_tickets_info LIMIT 20'))
#
# st.dataframe(result)
# org_counts = conn.query('SELECT org.name \'Organization\', sf.ARR, COUNT(zd.ticket_id) \'Ticket Count\', AVG (DATEDIFF (zd.solved_at, zd.created_at)) \'MTTR (days)\' FROM cp_salesforce.client_info sf LEFT JOIN cp_zendesk.cp_organization org ON org.name = sf.acc_name LEFT JOIN cp_zendesk.cp_tickets_info zd ON zd.organization_id = org.id WHERE org.name <> ("Null") AND zd.created_at >= "2023-01-01 00:00:00" GROUP BY org.name ORDER BY COUNT(zd.ticket_id) DESC LIMIT 20')
#
# st.DataFrame(org_counts)

# @st.cache
# def get_data():
#     df = pd.read_csv('assignee.csv')
#     return df
# df = get_data()

df = pd.read_csv('assignee.csv')
dr = pd.read_csv('resolution.csv')


#st.dataframe(df)

# Sidebar
st.sidebar.header('Select filters here:')
month = st.sidebar.multiselect(
    'Select the month:',
    options=df['month'].unique(),
    default=df['month'].unique()
)

dfs = df.query(
    "month == @month"
    # "year == @year"
)
#st.dataframe(dfs)

# tickets_2023 = int(dfs.query("year == 'y2023'").sum(axis=1).sum() - (dfs.query("year == 'y2023'").filter(like = 'Solved', axis = 1).sum()).sum() - (dfs.query("year == 'y2023'").filter(like = 'TTR', axis = 1).sum()).sum())

# Main
# st.title(f'2023 Tickets: {tickets_2023}')

nick_total2023 = int(dfs.query("year == 'y2023'")['nick'].sum())
gopi_total2023 = int(dfs.query("year == 'y2023'")['pamidi'].sum())
mani_total2023 = int(dfs.query("year == 'y2023'")['mani'].sum())
ali_total2023 = int(dfs.query("year == 'y2023'")['ali'].sum())
pratik_total2023 = int(dfs.query("year == 'y2023'")['pratik'].sum())
chad_total2023 = int(dfs.query("year == 'y2023'")['chad'].sum())
surak_total2023 = int(dfs.query("year == 'y2023'")['suraksha'].sum())
varun_total2023 = int(dfs.query("year == 'y2023'")['varun'].sum())
viswa_total2023 = int(dfs.query("year == 'y2023'")['viswa'].sum())

stse_old = nick_total2023+surak_total2023
tse_old = viswa_total2023+ali_total2023
ent_old = varun_total2023+gopi_total2023+mani_total2023+chad_total2023


# Calculations
achar_total2023 = int(dfs.query("year == 'y2023'")['achar'].sum())
achar_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['acharSolved'].sum()/dfs.query("year == 'y2023'")['achar'].sum()))
achar_resolve = round(dr['acharResolve']-dr['acharHold']-dr['acharWait'], 1)[0]
reddy_total2023 = int(dfs.query("year == 'y2023'")['reddy'].sum())
reddy_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['reddySolved'].sum()/dfs.query("year == 'y2023'")['reddy'].sum()))
reddy_resolve = round(dr['reddyResolve']-dr['reddyHold']-dr['reddyWait'], 1)[0]
nainika_total2023 = int(dfs.query("year == 'y2023'")['nainika'].sum())
nainika_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['nainikaSolved'].sum()/dfs.query("year == 'y2023'")['nainika'].sum()))
nainika_resolve = round(dr['nainikaResolve']-dr['nainikaHold']-dr['nainikaWait'], 1)[0]
atib_total2023 = int(dfs.query("year == 'y2023'")['atib'].sum())
atib_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['atibSolved'].sum()/dfs.query("year == 'y2023'")['atib'].sum()))
atib_resolve = round(dr['atibResolve']-dr['atibHold']-dr['atibWait'], 1)[0]
hammid_total2023 = int(dfs.query("year == 'y2023'")['hammid'].sum())
hammid_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['hammidSolved'].sum()/dfs.query("year == 'y2023'")['hammid'].sum()))
hammid_resolve = round(dr['hammidResolve']-dr['hammidHold']-dr['hammidWait'], 1)[0]

tl_total2023 = achar_total2023+reddy_total2023+nainika_total2023+atib_total2023+hammid_total2023

sambit_total2023 = int(dfs.query("year == 'y2023'")['sambit'].sum())
sambit_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['sambitSolved'].sum()/dfs.query("year == 'y2023'")['sambit'].sum()))
sambit_resolve = round(dr['sambitResolve']-dr['sambitHold']-dr['sambitWait'], 1)[0]
fajer_total2023 = int(dfs.query("year == 'y2023'")['fajer'].sum())
fajer_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['fajerSolved'].sum()/dfs.query("year == 'y2023'")['fajer'].sum()))
fajer_resolve = round(dr['fajerResolve']-dr['fajerHold']-dr['fajerWait'], 1)[0]
aditya_total2023 = int(dfs.query("year == 'y2023'")['aditya'].sum())
aditya_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['adityaSolved'].sum()/dfs.query("year == 'y2023'")['aditya'].sum()))
aditya_resolve = round(dr['adityaResolve']-dr['adityaHold']-dr['adityaWait'], 1)[0]

stse_total2023 = sambit_total2023+fajer_total2023+aditya_total2023

# ali_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['aliSolved'].sum()/dfs.query("year == 'y2023'")['ali'].sum()))
# ali_resolve = round(dr['aliResolve']-dr['aliHold']-dr['aliWait'], 1)[0]
amar_total2023 = int(dfs.query("year == 'y2023'")['amar'].sum())
amar_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['amarSolved'].sum()/dfs.query("year == 'y2023'")['amar'].sum()))
amar_resolve = round(dr['amarResolve']-dr['amarHold']-dr['amarWait'], 1)[0]
fahj_total2023 = int(dfs.query("year == 'y2023'")['faheemJ'].sum())
faheemJ_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['faheemJSolved'].sum()/dfs.query("year == 'y2023'")['faheemJ'].sum()))
faheemJ_resolve = round(dr['faheemJResolve']-dr['faheemJHold']-dr['faheemJWait'], 1)[0]
fahn_total2023 = int(dfs.query("year == 'y2023'")['faheemN'].sum())
faheemN_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['faheemNSolved'].sum()/dfs.query("year == 'y2023'")['faheemN'].sum()))
faheemN_resolve = round(dr['faheemNResolve']-dr['faheemNHold']-dr['faheemNWait'], 1)[0]
mohana_total2023 = int(dfs.query("year == 'y2023'")['mohana'].sum())
mohana_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['mohanaSolved'].sum()/dfs.query("year == 'y2023'")['mohana'].sum()))
mohana_resolve = round(dr['mohanaResolve']-dr['mohanaHold']-dr['mohanaWait'], 1)[0]
muheet_total2023 = int(dfs.query("year == 'y2023'")['muheet'].sum())
muheet_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['muheetSolved'].sum()/dfs.query("year == 'y2023'")['muheet'].sum()))
muheet_resolve = round(dr['muheetResolve']-dr['muheetHold']-dr['muheetWait'], 1)[0]
pratik_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['pratikSolved'].sum()/dfs.query("year == 'y2023'")['pratik'].sum()))
pratik_resolve = round(dr['pratikResolve']-dr['pratikHold']-dr['pratikWait'], 1)[0]
maliha_total2023 = int(dfs.query("year == 'y2023'")['maliha'].sum())
maliha_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['malihaSolved'].sum()/dfs.query("year == 'y2023'")['maliha'].sum()))
maliha_resolve = round(dr['malihaResolve']-dr['malihaHold']-dr['malihaWait'], 1)[0]
abdul_total2023 = int(dfs.query("year == 'y2023'")['abdul'].sum())
abdul_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['abdulSolved'].sum()/dfs.query("year == 'y2023'")['abdul'].sum()))
abdul_resolve = round(dr['abdulResolve']-dr['abdulHold']-dr['abdulWait'], 1)[0]

tse_total2023 = amar_total2023+fahj_total2023+fahn_total2023+mohana_total2023+muheet_total2023+pratik_total2023+maliha_total2023+abdul_total2023

narsi_total2023 = int(dfs.query("year == 'y2023'")['narsimha'].sum())
narsi_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['narsimhaSolved'].sum()/dfs.query("year == 'y2023'")['narsimha'].sum()))
narsi_resolve = round(dr['narsimhaResolve']-dr['narsimhaHold']-dr['narsimhaWait'], 1)[0]
ram_total2023 = int(dfs.query("year == 'y2023'")['ram'].sum())
ram_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['ramSolved'].sum()/dfs.query("year == 'y2023'")['ram'].sum()))
ram_resolve = round(dr['ramResolve']-dr['ramHold']-dr['ramWait'], 1)[0]
kiran_total2023 = int(dfs.query("year == 'y2023'")['kiran'].sum())
kiran_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['kiranSolved'].sum()/dfs.query("year == 'y2023'")['kiran'].sum()))
kiran_resolve = round(dr['kiranResolve']-dr['kiranHold']-dr['kiranWait'], 1)[0]
sree_total2023 = int(dfs.query("year == 'y2023'")['sree'].sum())
sree_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['sreeSolved'].sum()/dfs.query("year == 'y2023'")['sree'].sum()))
sree_resolve = round(dr['sreeResolve']-dr['sreeHold']-dr['sreeWait'], 1)[0]
vinai_total2023 = int(dfs.query("year == 'y2023'")['vinai'].sum())
vinai_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['vinaiSolved'].sum()/dfs.query("year == 'y2023'")['vinai'].sum()))

ent_total2023 = narsi_total2023+ram_total2023+kiran_total2023+sree_total2023+vinai_total2023

venka_total2023 = int(dfs.query("year == 'y2023'")['venka'].sum())
venka_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['venkaSolved'].sum()/dfs.query("year == 'y2023'")['venka'].sum()))
shariq_total2023 = int(dfs.query("year == 'y2023'")['shariq'].sum())
shariq_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['shariqSolved'].sum()/dfs.query("year == 'y2023'")['shariq'].sum()))
ahtesh_total2023 = int(dfs.query("year == 'y2023'")['ahtesh'].sum())
ahtesh_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['ahteshSolved'].sum()/dfs.query("year == 'y2023'")['ahtesh'].sum()))
danish_total2023 = int(dfs.query("year == 'y2023'")['danish'].sum())
danish_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['danishSolved'].sum()/dfs.query("year == 'y2023'")['danish'].sum()))
shazan_total2023 = int(dfs.query("year == 'y2023'")['shazan'].sum())
shazan_solve2023 = ("{:.0%}".format(dfs.query("year == 'y2023'")['shazanSolved'].sum()/dfs.query("year == 'y2023'")['shazan'].sum()))

atse_total2023 = venka_total2023+shariq_total2023+ahtesh_total2023+danish_total2023+shazan_total2023


achar_ttr2023 = round(dfs.query("year == 'y2023'")['acharTTR'].mean(),1)
reddy_ttr2023 = round(dfs.query("year == 'y2023'")['reddyTTR'].mean(),1)
nainika_ttr2023 = round(dfs.query("year == 'y2023'")['nainikaTTR'].mean(),1)
atib_ttr2023 = round(dfs.query("year == 'y2023'")['atibTTR'].mean(),1)
hammid_ttr2023 = round(dfs.query("year == 'y2023'")['hammidTTR'].mean(),1)
sambit_ttr2023 = round(dfs.query("year == 'y2023'")['sambitTTR'].mean(),1)
fajer_ttr2023 = round(dfs.query("year == 'y2023'")['fajerTTR'].mean(),1)
aditya_ttr2023 = round(dfs.query("year == 'y2023'")['adityaTTR'].mean(),1)
amar_ttr2023 = round(dfs.query("year == 'y2023'")['amarTTR'].mean(),1)
faheemJ_ttr2023 = round(dfs.query("year == 'y2023'")['faheemJTTR'].mean(),1)
faheemN_ttr2023 = round(dfs.query("year == 'y2023'")['faheemNTTR'].mean(),1)
pratik_ttr2023 = round(dfs.query("year == 'y2023'")['pratikTTR'].mean(),1)
mohana_ttr2023 = round(dfs.query("year == 'y2023'")['mohanaTTR'].mean(),1)
muheet_ttr2023 = round(dfs.query("year == 'y2023'")['muheetTTR'].mean(),1)
maliha_ttr2023 = round(dfs.query("year == 'y2023'")['malihaTTR'].mean(),1)
abdul_ttr2023 = round(dfs.query("year == 'y2023'")['abdulTTR'].mean(),1)
shazan_ttr2023 = round(dfs.query("year == 'y2023'")['shazanTTR'].mean(),1)
narsi_ttr2023 = round(dfs.query("year == 'y2023'")['narsimhaTTR'].mean(),1)
ram_ttr2023 = round(dfs.query("year == 'y2023'")['ramTTR'].mean(),1)
kiran_ttr2023 = round(dfs.query("year == 'y2023'")['kiranTTR'].mean(),1)
sree_ttr2023 = round(dfs.query("year == 'y2023'")['sreeTTR'].mean(),1)
vinai_ttr2023 = round(dfs.query("year == 'y2023'")['vinaiTTR'].mean(),1)
venka_ttr2023 = round(dfs.query("year == 'y2023'")['venkaTTR'].mean(),1)
shariq_ttr2023 = round(dfs.query("year == 'y2023'")['shariqTTR'].mean(),1)
ahtesh_ttr2023 = round(dfs.query("year == 'y2023'")['ahteshTTR'].mean(),1)
danish_ttr2023 = round(dfs.query("year == 'y2023'")['danishTTR'].mean(),1)

atse_ttr2023 = round(dfs.query("year == 'y2023'").loc[:, ['ahteshTTR','danishTTR','shazanTTR','shariqTTR','venkaTTR']].stack().mean(),1)
ent_ttr2023 = round(dfs.query("year == 'y2023'").loc[:, ['kiranTTR','narsimhaTTR','ramTTR','sreeTTR','vinaiTTR']].stack().mean(),1)
tse_ttr2023 = round(dfs.query("year == 'y2023'").loc[:, ['amarTTR','faheemJTTR','faheemNTTR','mohanaTTR','muheetTTR','pratikTTR','malihaTTR','abdulTTR']].stack().mean(),1)
stse_ttr2023 = round(dfs.query("year == 'y2023'").loc[:, ['adityaTTR','fajerTTR','sambitTTR']].stack().mean(),1)
tl_ttr2023 = round(dfs.query("year == 'y2023'").loc[:, ['nainikaTTR','acharTTR','reddyTTR','hammidTTR','atibTTR']].stack().mean(),1)

tl_dic2023 = dict({
    'TL 1':[achar_total2023, achar_solve2023, achar_ttr2023],
    'TL 2':[reddy_total2023, reddy_solve2023, reddy_ttr2023],
    'TL 3':[nainika_total2023, nainika_solve2023, nainika_ttr2023],
    'TL 4':[hammid_total2023, hammid_solve2023, hammid_ttr2023],
    'TL 5':[atib_total2023, atib_solve2023, atib_ttr2023]
})

stse_dic2023 = dict({
    'STSE 1':[sambit_total2023, sambit_solve2023, sambit_ttr2023],
    'STSE 2':[fajer_total2023, fajer_solve2023, fajer_ttr2023],
    'STSE 3':[aditya_total2023, aditya_solve2023, aditya_ttr2023]
})

ent_dic2023 = dict({
    'ENT 1':[narsi_total2023, narsi_solve2023, narsi_ttr2023],
    'ENT 2':[ram_total2023, ram_solve2023, ram_ttr2023],
    'ENT 3':[kiran_total2023, kiran_solve2023, kiran_ttr2023],
    'ENT 4':[sree_total2023, sree_solve2023, sree_ttr2023],
    'ENT 5':[vinai_total2023,vinai_solve2023, vinai_ttr2023]
})

tse_dic2023 = dict({
    # 'Ali':[ali_total2023, ali_solve2023, ali_ttr2023],
    'TSE 1':[amar_total2023, amar_solve2023, amar_ttr2023],
    'TSE 2':[fahj_total2023, faheemJ_solve2023, faheemJ_ttr2023],
    'TSE 3':[fahn_total2023, faheemN_solve2023, faheemN_ttr2023],
    'TSE 4':[mohana_total2023, mohana_solve2023, mohana_ttr2023],
    'TSE 5':[muheet_total2023, muheet_solve2023, muheet_ttr2023],
    'TSE 6':[pratik_total2023, pratik_solve2023, pratik_ttr2023],
    'TSE 7':[abdul_total2023, abdul_solve2023, abdul_ttr2023],
    'TSE 8':[maliha_total2023, maliha_solve2023, maliha_ttr2023]

})

atse_dic2023 = dict({
    'ATSE 1':[venka_total2023, venka_solve2023, venka_ttr2023],
    'ATSE 2':[shariq_total2023, shariq_solve2023, shariq_ttr2023],
    'ATSE 3':[ahtesh_total2023,ahtesh_solve2023, ahtesh_ttr2023],
    'ATSE 4':[danish_total2023,danish_solve2023, danish_ttr2023],
    'ATSE 5':[shazan_total2023, shazan_solve2023, shazan_ttr2023]
})

tl_s2023 = sorted(tl_dic2023.items(), key=lambda item: item[1], reverse=True)
stse_s2023 = sorted(stse_dic2023.items(), key=lambda item: item[1], reverse=True)
ent_s2023 = sorted(ent_dic2023.items(), key=lambda item: item[1], reverse=True)
tse_s2023 = sorted(tse_dic2023.items(), key=lambda item: item[1], reverse=True)
atse_s2023 = sorted(atse_dic2023.items(), key=lambda item: item[1], reverse=True)

metrics = "<span class='bold'><span class='blue'>Ticket Count</span> | <span class='orange'>Solve Rate</span> | <span class='purple'>MTTR (days)</span></span>"

st.markdown(metrics, unsafe_allow_html=True)

column2023_1, column2023_2, column2023_3, column2023_4, column2023_5 = st.columns(5)
with column2023_1:
    # st.subheader(f'TL \n % of Total: {"{:.0%}".format(tl_total2023/tickets_2023)}')
    st.markdown(f'<span class="bold"><span class="purple">Group MTTR: {tl_ttr2023}</span></span>', unsafe_allow_html=True)
    for x in tl_s2023:
        st.markdown(f'<span class="bold"><span class="black">{x[0]}</span>: <span class="blue">{x[1][0]}</span> | <span class="orange">{x[1][1]}</span> | <span class="purple">{x[1][2]}</span></span>', unsafe_allow_html=True)
        # st.markdown(f'<span class="bold"><span class="black">{x[0]}</span>: <span class="blue">{x[1][0]}</span> | <span class="orange">{x[1][1]}</span> | <span class="gray">{x[1][2]}</span></span>', unsafe_allow_html=True)
    # st.text(f' {tl_s2023[0][0]}: {tl_s2023[0][1][0]} | {tl_s2023[0][1][1]} | {tl_s2023[0][1][2]} \n {tl_s2023[1][0]}: {tl_s2023[1][1][0]} | {tl_s2023[1][1][1]} | {tl_s2023[1][1][2]} \n {tl_s2023[2][0]}: {tl_s2023[2][1][0]} | {tl_s2023[2][1][1]} | {tl_s2023[2][1][2]} \n {tl_s2023[3][0]}: {tl_s2023[3][1][0]} | {tl_s2023[3][1][1]} | {tl_s2023[3][1][2]}')

with column2023_2:
    # st.subheader(f'STSE \n % of Total: {"{:.0%}".format(stse_total2023/tickets_2023)}')
    st.markdown(f'<span class="bold"><span class="purple">Group MTTR: {stse_ttr2023}</span></span>', unsafe_allow_html=True)
    for x in stse_s2023:
        st.markdown(f'<span class="bold"><span class="black">{x[0]}</span>: <span class="blue">{x[1][0]}</span> | <span class="orange">{x[1][1]}</span> | <span class="purple">{x[1][2]}</span></span>', unsafe_allow_html=True)
    # st.text(f' {stse_s2023[0][0]}: {stse_s2023[0][1][0]} | {stse_s2023[0][1][1]} \n {stse_s2023[1][0]}: {stse_s2023[1][1][0]} | {stse_s2023[1][1][1]} \n {stse_s2023[2][0]}: {stse_s2023[2][1][0]} | {stse_s2023[2][1][1]} \n {stse_s2023[3][0]}: {stse_s2023[3][1][0]} | {stse_s2023[3][1][1]}')

with column2023_3:
    # st.subheader(f'ENT \n % of Total: {"{:.0%}".format(ent_total2023/tickets_2023)}')
    st.markdown(f'<span class="bold"><span class="purple">Group MTTR: {ent_ttr2023}</span></span>', unsafe_allow_html=True)

    for x in ent_s2023:
        st.markdown(f'<span class="bold"><span class="black">{x[0]}</span>: <span class="blue">{x[1][0]}</span> | <span class="orange">{x[1][1]}</span> | <span class="purple">{x[1][2]}</span></span>', unsafe_allow_html=True)
    # st.text(f' {ent_s2023[0][0]}: {ent_s2023[0][1][0]} | {ent_s2023[0][1][1]} \n {ent_s2023[1][0]}: {ent_s2023[1][1][0]} | {ent_s2023[1][1][1]} \n {ent_s2023[2][0]}: {ent_s2023[2][1][0]} | {ent_s2023[2][1][1]} \n {ent_s2023[3][0]}: {ent_s2023[3][1][0]} | {ent_s2023[3][1][1]}')

with column2023_5:
    # st.subheader(f'ATSE \n % of Total: {"{:.0%}".format(atse_total2023/tickets_2023)}')
    st.markdown(f'<span class="bold"><span class="purple">Group MTTR: {atse_ttr2023}</span></span>', unsafe_allow_html=True)
    for x in atse_s2023:
        st.markdown(f'<span class="bold"><span class="black">{x[0]}</span>: <span class="blue">{x[1][0]}</span> | <span class="orange">{x[1][1]}</span> | <span class="purple">{x[1][2]}</span></span>', unsafe_allow_html=True)
    # st.text(f' {atse_s2023[0][0]}: {atse_s2023[0][1][0]} | {atse_s2023[0][1][1]} \n {atse_s2023[1][0]}: {atse_s2023[1][1][0]} | {atse_s2023[1][1][1]} \n {atse_s2023[2][0]}: {atse_s2023[2][1][0]} | {atse_s2023[2][1][1]} \n {atse_s2023[3][0]}: {atse_s2023[3][1][0]} | {atse_s2023[3][1][1]}')

with column2023_4:
    # st.subheader(f'TSE \n % of Total: {"{:.0%}".format(tse_total2023/tickets_2023)}')
    st.markdown(f'<span class="bold"><span class="purple">Group MTTR: {tse_ttr2023}</span></span>', unsafe_allow_html=True)

    for x in tse_s2023:
        st.markdown(f'<span class="bold"><span class="black">{x[0]}</span>: <span class="blue">{x[1][0]}</span> | <span class="orange">{x[1][1]}</span> | <span class="purple">{x[1][2]}</span></span>', unsafe_allow_html=True)
    # st.text(f' {tse_s2023[0][0]}: {tse_s2023[0][1][0]} | {tse_s2023[0][1][1]} \n {tse_s2023[1][0]}: {tse_s2023[1][1][0]} | {tse_s2023[1][1][1]} \n {tse_s2023[2][0]}: {tse_s2023[2][1][0]} | {tse_s2023[2][1][1]} \n {tse_s2023[3][0]}: {tse_s2023[3][1][0]} | {tse_s2023[3][1][1]} \n {tse_s2023[4][0]}: {tse_s2023[4][1][0]} | {tse_s2023[4][1][1]} \n {tse_s2023[5][0]}: {tse_s2023[5][1][0]} | {tse_s2023[5][1][1]} \n {tse_s2023[6][0]}: {tse_s2023[6][1][0]} | {tse_s2023[6][1][1]}')

fig_tickets_2023 = sp()

fig_tickets_2023.add_trace(go.Scatter(
    x=dfs.query("year == 'y2023'")['month'],
    y=dfs.query("year == 'y2023'")['achar']+dfs.query("year == 'y2023'")['nainika']+dfs.query("year == 'y2023'")['reddy']+dfs.query("year == 'y2023'")['hammid']+dfs.query("year == 'y2023'")['atib'],
    name='TL'
))

fig_tickets_2023.add_trace(go.Scatter(
    x=dfs.query("year == 'y2023'")['month'],
    y=dfs.query("year == 'y2023'")['sambit']+dfs.query("year == 'y2023'")['fajer']+dfs.query("year == 'y2023'")['aditya'],
    name='STSE'
))

fig_tickets_2023.add_trace(go.Scatter(
    x=dfs.query("year == 'y2023'")['month'],
    y=dfs.query("year == 'y2023'")['abdul']+dfs.query("year == 'y2023'")['maliha']+dfs.query("year == 'y2023'")['muheet']+dfs.query("year == 'y2023'")['mohana']+dfs.query("year == 'y2023'")['faheemN']+dfs.query("year == 'y2023'")['faheemJ']+dfs.query("year == 'y2023'")['amar']+dfs.query("year == 'y2023'")['pratik']+dfs.query("year == 'y2023'")['shazan'],
    name='TSE'
))

fig_tickets_2023.add_trace(go.Scatter(
    x=dfs.query("year == 'y2023'")['month'],
    y=dfs.query("year == 'y2023'")['narsimha']+dfs.query("year == 'y2023'")['kiran']+dfs.query("year == 'y2023'")['ram']+dfs.query("year == 'y2023'")['sree'],
    name='ENT'
))

fig_tickets_2023.add_trace(go.Scatter(
    x=dfs.query("year == 'y2023'")['month'],
    y=+dfs.query("year == 'y2023'")['venka']+dfs.query("year == 'y2023'")['shariq']+dfs.query("year == 'y2023'")['ahtesh']+dfs.query("year == 'y2023'")['danish']+dfs.query("year == 'y2023'")['vinai'],
    name='ATSE'
))

# chart_total_2023 = dfs.query("year == 'y2023'")['achar']+dfs.query("year == 'y2023'")['nainika']+dfs.query("year == 'y2023'")['reddy']+dfs.query("year == 'y2023'")['atib']+dfs.query("year == 'y2023'")['sambit']+dfs.query("year == 'y2023'")['hammid']+dfs.query("year == 'y2023'")['fajer']+dfs.query("year == 'y2023'")['aditya']+dfs.query("year == 'y2023'")['muheet']+dfs.query("year == 'y2023'")['mohana']+dfs.query("year == 'y2023'")['faheemN']+dfs.query("year == 'y2023'")['faheemJ']+dfs.query("year == 'y2023'")['amar']+dfs.query("year == 'y2023'")['maliha']+dfs.query("year == 'y2023'")['venka']+dfs.query("year == 'y2023'")['abdul']+dfs.query("year == 'y2023'")['shariq']+dfs.query("year == 'y2023'")['ahtesh']+query("year == 'y2023'")['narsimha']+dfs.query("year == 'y2023'")['kiran']+dfs.query("year == 'y2023'")['ram']+dfs.query("year == 'y2023'")['sree']

# fig_tickets_2023.add_trace(go.Scatter(
#     x=dfs.query("year == 'y2023'")['month'],
#     y=dfs.query("year == 'y2023'").filter(like = 'Solved')[dfs.sum(axis=1) !=0].sum(axis=1),
#     name='Total'
# ))


fig_tickets_2023.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=(dict(showgrid=False)),
    yaxis=dict(range=[0,700], showgrid=False),
    height=500,
    width=1200,
    title='2023 Team Volume'
)

st.plotly_chart(fig_tickets_2023)


# Hide Streamlit Style
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
