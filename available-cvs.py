import requests,re
from datetime import datetime

target_url = 'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.CA.json?vaccineinfo'

headers = {
'Host':'www.cvs.com',
'Connection':'close',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
'Accept':'*/*',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Dest':'empty',
'Referer':'https://www.cvs.com/immunizations/covid-19-vaccine?icid=cvs-home-hero1-link2-coronavirus-vaccine',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'en-US,en;q=0.9' }


cookies = { 
'QuantumMetricSessionLink':'https://cvs.quantummetric.com/#/users/search?autoreplay=true&qmsessioncookie=555aecdc394a267e99ae42c92c1f1897&ts=1615534626-1615621026',
'pe':'p1',
'acctdel_v1':'on',
'adh_new_ps':'on',
'adh_ps_pickup':'on',
'adh_ps_refill':'on',
'buynow':'off',
'sab_displayads':'on',
'dashboard_v1':'off',
'db-show-allrx':'on',
'disable-app-dynamics':'on',
'disable-sac':'on',
'dpp_cdc':'off',
'dpp_drug_dir':'off',
'dpp_sft':'off',
'getcust_elastic':'on',
'echomeln6':'off-p0',
'enable_imz':'on',
'enable_imz_cvd':'on',
'enable_imz_reschedule_instore':'off',
'enable_imz_reschedule_clinic':'off',
'flipp2':'on',
'gbi_cvs_coupons':'true',
'ice-phr-offer':'off',
'v3redirecton':'false',
'mc_cloud_service':'on',
'mc_hl7':'on',
'mc_home_new':'off2-p0',
'mc_ui_ssr':'off-p2',
'mc_videovisit':'on',
'memberlite':'on',
'pauth_v1':'on',
'pivotal_forgot_password':'off-p0',
'pivotal_sso':'off-p0',
'pbmplaceorder':'off',
'pbmrxhistory':'on',
'ps':'on',
'refill_chkbox_remove':'off-p0',
'rxdanshownba':'off',
'rxdfixie':'on',
'rxd_bnr':'on',
'rxd_dot_bnr':'on',
'rxdpromo':'on',
'rxduan':'on',
'rxlite':'on',
'rxlitelob':'off',
'rxm':'on',
'rxm_phone_dob':'off-p1',
'rxm_demo_hide_LN':'off',
'rxm_phdob_hide_LN':'on',
'rxm_rx_challenge':'on',
's2c_akamaidigitizecoupon':'on',
's2c_beautyclub':'off-p0',
's2c_digitizecoupon':'on',
's2c_dmenrollment':'off-p0',
's2c_herotimer':'off-p0',
's2c_newcard':'off-p0',
's2c_papercoupon':'on',
's2c_persistEcCookie':'on',
's2c_smsenrollment':'on',
's2cHero_lean6':'on',
'sft_mfr_new':'on',
'sftg':'on',
'show_exception_status':'on',
'v2-dash-redirection':'on',
'ak_bmsc':'248153273B0BA762E2BB135E91FB1835173DC39DA660000016B54B60C476877B~plP84PQmozOBFtrcJfjpyCXjZ8t6kwlBBmfpKq876sQL5W9MGIR2JX0/QQUEnp3hKXnbpi/wzSnAl0TMFUk+iYsUuhZ1Ib67yBoM2J2nZsUGviJt6i+c6lOLHWW+2uwHiTD1IzUcIA/FPZZa6IgONHr1bAj827Rr5nIzo8WVX1Tz+LHb03CgI3IThOZQ50QXRP0q03M2GRrsuS1WjLThgDw1wOoJx8XkIEbEpg2UBaFUE=',
'bm_sz':'AA5E5E69333B8033C65B400BFD1F4837~YAAQncM9FxI8GiF4AQAAwWG7JwtmsW3I/CcwsVR+04iXcW+TB6WOAqSpCy6kWhWxMdMr805RgJ00Wg71oWwl0gjw8AKn7BbxMww5tgTDpe626IhJqCuI3rCWM+oU2gP8CX+MMwWMpzXStAPrbYERYLADpIua4snIpWSM/fgZIK10VZjl7nik94QSdeZP',
'mt.v':'2.935223142.1615574295699',
'_group1':'quantum',
'AMCVS_06660D1556E030D17F000101%40AdobeOrg':'1',
'CVPF':'CT-USR',
's_cc':'true',
'AMCV_06660D1556E030D17F000101%40AdobeOrg':'-330454231%7CMCIDTS%7C18699%7CMCMID%7C42402602258885136953403765318971640534%7CMCAAMLH-1616179099%7C9%7CMCAAMB-1616179099%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1615581499s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18706%7CvVersion%7C3.1.2',
'_gcl_au':'1.1.1068033678.1615574302',
'_4c_mc_':'ee61d923-8edb-4b36-a2eb-15458053dd30',
'bm_sv':'E77F0DE906531D32F1A35B9394F4172A~4ACU14vW5P7YbIrjeTzxyc975e6luBo7fEWXVJlRkdW+ISSZQu8uu8M2cBLB3elPQcw811fnSTzPI2m12RITyiCC65vcJi9l59xO3GoURve9ObX/doMxuwo2WVPo+RtY0l7zbTn8ftBXqdJ3FFT4JA==',
'akavpau_www_cvs_com_general':'1615574723~id=7536affb31903339fd87ac36fc400eb2',
'_abck':'E96DDB02B9E0592351E3319B8CFF829B~0~YAAQncM9Fz4+GiF4AQAA/IO7JwXSH3lpWM9vDTSThRSIeXXd2H9U0xSDuP9g0tPPrTCNEhjFUvWVqU6B6RctrLskEfo4m5+5kXaDoYXx10Vzsr4BEPTW2l8yi11/EmBw1CKmVniKxomlE2SM0WrXeIfQfFlWIAh5KZkh//2wRD8Z+J7nmYlB8bFG8JmfeSDzpxIswMHdoSpP7EemCOGGAh8w/Zw3+RgNlyF4/UVro2JkYssy3BGRmxFi51rSy4PqFoZt279crz2z4TqfpBJajwM9Ie0HKL7PoRybG4WpLDewWzLpUp2pRTmzmHRuPscxg+nO9bhIo1/skHdnnOq/1oIq/vPhPtiiBUztJ/LtzuL/9bQ/Z/k8ZGFk1mD5yBbwka5ymkGiPvin8G+e7CfxJUGLcsSH~-1~||-1||~-1',
'gbi_visitorId':'ckm6n87l70001398qyi4myesc',
'QuantumMetricUserID':'4e51c9e8dc2c296c5d961300246280fe',
'QuantumMetricSessionID':'555aecdc394a267e99ae42c92c1f1897',
'RT':'"z=1&dm=cvs.com&si=09a6668d-8dcd-42f7-977c-a554168a1ac4&ss=km6n7zkg&sl=0&tt=0&bcn=%2F%2Fb855d7f9.akstat.io%2F&nu=ifz4dlr5&cl=24ae9"',
'qmexp':'1615579653460',
'gpv_p10':'www.cvs.com%2Fimmunizations%2Fcovid-19-vaccine',
'gpv_e5':'cvs%7Cdweb%7Cimmunizations%7Ccovid-19-vaccine%7Cpromo%3A%20covid-19%20vaccines%20in%20california%20modal',
's_sq':'%5B%5BB%5D%5D',
'utag_main':'v_id:017827bb686600016672385a57af02073006006b00fb8$_sn:1$_ss:1$_st:1615579653753$vapi_domain:cvs.com' }

r = requests.get(target_url, headers=headers, cookies=cookies)
print(r)
#print(r.text)
available_cities = re.findall(r"\"city\":\"(\w+)\",\"state\":\"CA\",\"status\":\"Available\"",r.text)
if not available_cities:
  print("No Availability Found")
else:
  now = datetime.now()
  print("Check Time: {}".format(now.strftime("%H:%M:%S %m/%d/%Y ")))
  print("{} CA Cities have vaccines\n".format(len(available_cities)))
#print(available_cities)
  for city in available_cities:
    print("Available City: {}".format(city))
