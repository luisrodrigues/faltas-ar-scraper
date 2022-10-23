class ScraperConstants:
    def __init__(self):
        # Events list
        self.ATTENDANCE_EVENTS_URL = 'https://www.parlamento.pt/DeputadoGP/Paginas/PresencasReunioesPlenarias.aspx?BID=3'
        self.ATTENDANCE_EVENTS_TABLE_ID = 'ctl00_ctl50_g_7c7df12c_f153_404a_aa14_230620d8a929_ctl00_pnlResults'
        # Event attendance page
        self.BID = '299201'
        self.ATTENDANCE_TABLE_URL = 'https://www.parlamento.pt/DeputadoGP/Paginas/DetalheReuniaoPlenaria.aspx?BID='
        self.ATTENDANCE_TABLE_ID = 'ctl00_ctl50_g_6319d967_bcb6_4ba9_b9fc_c9bb325b19f1_ctl00_pnlDetalhe'
        self.ATTENDANCE_PAGE_TITLE = 'ctl00_ctl50_g_6319d967_bcb6_4ba9_b9fc_c9bb325b19f1_ctl00_lblHeader'


app_constants = ScraperConstants()
