import time
import urllib2
import urllib2
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange


from urllib2 import urlopen

sp500 = ['a', 'aa', 'aapl', 'abbv', 'abc', 'rsh', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp',
         'adsk', 'adt', 'aee', 'aeo', 'aep', 'aes', 'aet', 'afl', 'agn', 'aig', 'aiv', 'aiz', 'akam', 'all', 'altr',
         'alxn', 'amat', 'amd', 'amgn', 'amp', 'amt', 'amzn', 'an', 'anf', 'ann', 'aon', 'apa', 'apc', 'apd', 'aph',
         'apol', 'arg', 'arna', 'aro', 'ati', 'atvi', 'avb', 'avp', 'avy', 'axp', 'azo', 'ba', 'bac', 'bax', 'bbby',
         'bbry', 'bbt', 'bby', 'bcr', 'bdx', 'beam', 'ben', 'bf-b', 'bhi', 'big', 'biib', 'bk', 'bks', 'blk', 'bll',
         'bmc', 'bms', 'bmy', 'brcm', 'brk-b', 'bsx', 'btu', 'bwa', 'bxp', 'c', 'ca', 'cab', 'cag', 'cah', 'cam', 'cat',
         'cb', 'cbg', 'cbs', 'cce', 'cci', 'ccl', 'celg', 'cern', 'cf', 'cfn', 'chk', 'chrw', 'ci', 'cim', 'cinf', 'cl',
         'clf', 'clx', 'cma', 'cmcsa', 'cme', 'cmg', 'cmi', 'cms', 'cnp', 'cnx', 'cof', 'cog', 'coh', 'col', 'cop',
         'cost', 'cov', 'cpb', 'crm', 'csc', 'csco', 'csx', 'ctas', 'ctl', 'ctsh', 'ctxs', 'cvc', 'cvs', 'cvx', 'd',
         'dal', 'dd', 'dds', 'de', 'dell', 'df', 'dfs', 'dg', 'dgx', 'dhi', 'dhr', 'dis', 'disca', 'dks', 'dlph',
         'dltr', 'dlx', 'dnb', 'dnr', 'do', 'dov', 'dow', 'dps', 'dri', 'dsw', 'dte', 'dtv', 'duk', 'dva', 'dvn', 'ea',
         'ebay', 'ecl', 'ed', 'efx', 'eix', 'el', 'emc', 'emn', 'emr', 'eog', 'eqr', 'eqt', 'esrx', 'esv', 'etfc',
         'etn', 'etr', 'ew', 'exc', 'expd', 'expe', 'expr', 'f', 'fast', 'fb', 'fcx', 'fdo', 'fdx', 'fe', 'ffiv', 'fhn',
         'fis', 'fisv', 'fitb', 'fl', 'flir', 'flr', 'fls', 'flws', 'fmc', 'fosl', 'frx', 'fslr', 'fti', 'ftr', 'gas',
         'gci', 'gd', 'ge', 'ges', 'gild', 'gis', 'glw', 'gm', 'gmcr', 'gme', 'gnw', 'goog', 'gpc', 'gps', 'grmn',
         'grpn', 'gs', 'gt', 'gww', 'hal', 'har', 'has', 'hban', 'hcbk', 'hcn', 'hcp', 'hd', 'hes', 'hig', 'hog', 'hon',
         'hot', 'hov', 'hp', 'hpq', 'hrb', 'hrl', 'hrs', 'hsp', 'hst', 'hsy', 'hum', 'ibm', 'ice', 'iff', 'igt', 'intc',
         'intu', 'ip', 'ipg', 'ir', 'irm', 'isrg', 'itw', 'ivz', 'jbl', 'jci', 'jcp', 'jdsu', 'jec', 'jnj', 'jnpr',
         'josb', 'joy', 'jpm', 'jwn', 'k', 'key', 'kim', 'klac', 'kmb', 'kmi', 'kmx', 'ko', 'kr', 'krft', 'kss', 'ksu',
         'l', 'leg', 'len', 'lh', 'life', 'lll', 'lltc', 'lly', 'lm', 'lmt', 'lnc', 'lo', 'low', 'lrcx', 'lsi', 'ltd',
         'luk', 'luv', 'lyb', 'm', 'ma', 'mac', 'mar', 'mas', 'mat', 'mcd', 'mchp', 'mck', 'mco', 'mcp', 'mdlz', 'mdt',
         'met', 'mgm', 'mhfi', 'mjn', 'mkc', 'mmc', 'mmm', 'mnst', 'mo', 'molx', 'mon', 'mos', 'mpc', 'mrk', 'mro',
         'ms', 'msft', 'msi', 'mtb', 'mu', 'mur', 'mwv', 'myl', 'nbl', 'nbr', 'ndaq', 'ne', 'nee', 'nem', 'nflx', 'nfx',
         'ni', 'nile', 'nke', 'nly', 'noc', 'nok', 'nov', 'nrg', 'nsc', 'ntap', 'ntri', 'ntrs', 'nu', 'nue', 'nvda',
         'nwl', 'nwsa', 'nyx', 'oi', 'oke', 'omc', 'orcl', 'orly', 'oxy', 'p', 'payx', 'pbct', 'pbi', 'pcar', 'pcg',
         'pcl', 'pcln', 'pcp', 'pdco', 'peg', 'pep', 'petm', 'pets', 'pfe', 'pfg', 'pg', 'pgr', 'ph', 'phm', 'pki',
         'pld', 'pll', 'pm', 'pnc', 'pnr', 'pnw', 'pom', 'ppg', 'ppl', 'prgo', 'pru', 'psa', 'psx', 'pwr', 'px', 'pxd',
         'qcom', 'qep', 'r', 'rai', 'rdc', 'rf', 'rhi', 'rht', 'rl', 'rok', 'rop', 'rost', 'rrc', 'rsg', 'rsh', 'rtn',
         's', 'sai', 'sbux', 'scg', 'schl', 'schw', 'sd', 'se', 'see', 'sfly', 'shld', 'shw', 'sial', 'siri', 'sjm',
         'sks', 'slb', 'slm', 'sna', 'sndk', 'sne', 'sni', 'so', 'spg', 'spls', 'srcl', 'sre', 'sti', 'stj', 'stt',
         'stx', 'stz', 'swk', 'swn', 'swy', 'syk', 'symc', 'syy', 't', 'tap', 'tdc', 'te', 'teg', 'tel', 'ter', 'tgt',
         'thc', 'tibx', 'tif', 'tjx', 'tm', 'tmk', 'tmo', 'trip', 'trow', 'trv', 'tsla', 'tsn', 'tso', 'tss', 'twc',
         'twx', 'txn', 'txt', 'tyc', 'ua', 'unh', 'unm', 'unp', 'ups', 'urbn', 'usb', 'utx', 'v', 'vale', 'var', 'vfc',
         'viab', 'vitc', 'vlo', 'vmc', 'vno', 'vprt', 'vrsn', 'vtr', 'vz', 'wag', 'wat', 'wdc', 'wec', 'wfc', 'wfm',
         'whr', 'win', 'wlp', 'wm', 'wmb', 'wmt', 'wpo', 'wpx', 'wtw', 'wu', 'wy', 'wyn', 'wynn', 'x', 'xel', 'xl',
         'xlnx', 'xom', 'xray', 'xrx', 'xyl', 'yhoo', 'yum', 'zion', 'zlc', 'zmh', 'znga', 'camp', 'cldx', 'ecyt',
         'gtn', 'htz', 'nus', 'pvtb', 'qdel', 'snts', 'wgo', 'wwww']
sp500short = ['a', 'aa', 'aapl', 'abbv', 'rsh', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp']
russell3000=['ADBE', 'ADTN', 'ADRO', 'AAP', 'WMS', 'AEIS', 'AMD', 'ADXS', 'ADVM', 'ABCO', 'ACM', 'AEGN', 'AEPI', 'AERI', 'HIVE', 'AJRD', 'AVAV', 'AES', 'AET', 'AMG', 'AFL', 'MITT', 'AGCO', 'AGEN', 'AGRX', 'A', 'AGYS', 'AGIO', 'GAS', 'ADC', 'AGFS', 'AIMT', 'AL', 'AIRM', 'APD', 'ATSG', 'AYR', 'AKS', 'AKAM', 'AKBA', 'AKRX', 'ALG', 'ALRM', 'ALK', 'AIN', 'AMRI', 'ALB', 'AA', 'AAL', 'AAT', 'AXL', 'ACC', 'MTGE', 'AGNC', 'AEO', 'AEP', 'AEL', 'AXP', 'AFG', 'AMH', 'AMIC', 'AIG', 'ANAT', 'AMNB', 'ARII', 'ARA', 'ASEI', 'AMSWA', 'AWR', 'AMSC', 'AMT', 'AVD', 'AMWD', 'AWK', 'CRMT', 'AMP', 'ABCB', 'AMSF', 'ABC', 'ATLO', 'AME', 'AMGN', 'FOLD', 'AMKR', 'AHS', 'AP', 'AMPH', 'APH', 'AMPE', 'BETR', 'AMSG', 'AFSI', 'APC', 'ADI', 'ALOG', 'AVXL', 'ANDE', 'AFI', 'AWI', 'ARRY', 'ARRS', 'ARW', 'AROW', 'ARWR', 'ARTNA', 'APAM', 'ANET', 'ABG', 'ASNA', 'ASCMA', 'AHP', 'AHT', 'ASH', 'AHL', 'AZPN', 'ASB', 'AC', 'AIZ', 'AGO', 'ASTE', 'AST', 'AF', 'ATRO', 'T', 'ATRA', 'ATHN', 'ATHX', 'ACBI', 'AT', 'ABY', 'AAWW', 'AFH', 'TEAM', 'ATO', 'ATNI', 'ATRC', 'ATRI', 'ATW', 'ABTL', 'ADSK', 'ADP', 'AN', 'AZO', 'AVB', 'AGR', 'AVNU', 'BAX', 'BV', 'BBT', 'BBCN', 'BBX', 'BEAV', 'BECN', 'BSF', 'BZH', 'BDX', 'BBBY', 'BELFB', 'BDC', 'BLCM', 'BEL', 'BMS', 'BHE', 'BNCL', 'BNFT', 'WRB', 'BRK.B', 'BHLB', 'BERY', 'BBY', 'BGCP', 'BGFV', 'BIG', 'BH', 'BBG', 'BPTH', 'BCRX', 'BIIB', 'BMRN', 'BIO', 'BIOS', 'BSTC', 'TECH', 'BEAT', 'BTX', 'BJRI', 'BBOX', 'BKH', 'BKFS', 'BLKB', 'HAWK', 'BLK', 'HRB', 'BLMN', 'BCOR', 'BRKR', 'BC', 'BMTC', 'BLMT', 'BKE', 'BWLD', 'BBW', 'BLDR', 'BG', 'BURL', 'BWXT', 'CFFI', 'CHRW', 'BNK', 'CA', 'CAB', 'CABO', 'CBT', 'CCMP', 'COG', 'CACI', 'CDNS', 'CACQ', 'CZR', 'CSTE', 'CAI', 'CALM', 'CLMS', 'CAMP', 'CAA', 'CVGW', 'CAL', 'CCC', 'CFNB', 'CRC', 'CWT', 'CALX', 'ELY', 'CALD', 'CPE', 'CPN', 'ABCD', 'CBM', 'CAC', 'CPT', 'CPB', 'CMN', 'CPLA', 'CBF', 'CDR', 'CGI', 'CE', 'CPXX', 'CELG', 'CLDX', 'CBMG', 'CEMP', 'CNC', 'CNP', 'CSFL', 'CETV', 'CENT', 'CPF', 'CVCY', 'CENX', 'CNBKA', 'CNTY', 'CCS', 'CTL', 'CPHD', 'CERN', 'CERS', 'CEVA', 'CF', 'ECOM', 'CRL', 'GTLS', 'CHTR', 'CHFN', 'CCF', 'CLDT', 'CAKE', 'CHEF', 'CHGG', 'CHE', 'CHFC', 'CCXI', 'CHMT', 'CHMG', 'LNG', 'CHK', 'CHSP', 'CPK', 'CVX', 'CBI', 'CHS', 'PLCE', 'COBZ', 'COKE', 'KO', 'CDXS', 'CVLY', 'CDE', 'CCOI', 'CGNX', 'CTSH', 'CNS', 'COHR', 'CHRS', 'COHU', 'CFX', 'CL', 'CLCT', 'COLL', 'CLNY', 'SFR', 'COLB', 'CPGX', 'CXP', 'COLM', 'CMCO', 'CMCSA', 'CMA', 'FIX', 'CSAL', 'CBSH', 'CMC', 'COMM', 'CBU', 'CYH', 'CHCT', 'CTBI', 'COB', 'CVLT', 'CMP', 'CPSI', 'CSC', 'CIX', 'SCOR', 'CMTL', 'CAG', 'CNCE', 'CXO', 'CFMS', 'CNMD', 'CTWS', 'CACC', 'CREE', 'CROX', 'CCRN', 'CCI', 'CCK', 'CRY', 'CSGS', 'CSRA', 'CSS', 'CST', 'CSWI', 'CSX', 'CTS', 'CUNB', 'CUBE', 'CUB', 'CFR', 'CFI', 'CMI', 'CRIS', 'CW', 'CUBI', 'CUTR', 'CVBF', 'CVT', 'CVI', 'CVS', 'CYNO', 'CY', 'CONE', 'CYS', 'CYTK', 'CTMX', 'CYTR', 'DHI', 'DJCO', 'DAKT', 'DAN', 'DHR', 'DRI', 'DAR', 'DTLK', 'PLAY', 'DVA', 'DWSN', 'DCT', 'DDR', 'DF', 'DPZ', 'UFS', 'DCI', 'DGICA', 'RRD', 'LPG', 'DORM', 'PLOW', 'DEI', 'DOV', 'DOW', 'DPS', 'DWA', 'DW', 'DRQ', 'DSPG', 'DST', 'DSW', 'DTE', 'DTSI', 'DD', 'DCO', 'DUK', 'DRE', 'DLTH', 'DNB', 'DNKN', 'DFT', 'DRRX', 'DXPE', 'DY', 'BOOM', 'DVAX', 'DYN', 'DX', 'ETFC', 'EGBN', 'EXP', 'EGRX', 'ELNK', 'ESTE', 'EWBC', 'DEA', 'EGP', 'EMN', 'KODK', 'ETN', 'EV', 'EBAY', 'EBF', 'ENVA', 'NPO', 'ESV', 'ENSG', 'ESGR', 'ENTG', 'ENTL', 'ETM', 'ETR', 'EBTC', 'EFSC', 'EVC', 'ENV', 'EVHC', 'ENZ', 'EOG', 'EPE', 'EPAM', 'EPIQ', 'EPZM', 'PLUS', 'EPR', 'EQT', 'EFX', 'EQIX', 'EQBK', 'EQC', 'ELS', 'EQY', 'EQR', 'ERA', 'ERIE', 'ERN', 'EROS', 'ESCA', 'ESE', 'ESPR', 'ESSA', 'ESND', 'ESNT', 'ESS', 'EL', 'ESL', 'ETH', 'ETSY', 'EEFT', 'EVER', 'EVR', 'FNHC', 'FDX', 'FEIC', 'FCH', 'FOE', 'GSM', 'FGEN', 'FGL', 'FIS', 'LION', 'FRGI', 'FSAM', 'FITB', 'FNGN', 'FISI', 'FNSR', 'FINL', 'FEYE', 'FAF', 'FNLC', 'FBNC', 'FBP', 'BUSE', 'FBIZ', 'FCFS', 'FCNCA', 'FCBC', 'FCF', 'FCFP', 'FBNK', 'FDC', 'FDEF', 'FFBC', 'THFF', 'FFIN', 'FFNW', 'FFWM', 'FHN', 'FR', 'INBK', 'FIBK', 'FLIC', 'FRME', 'FMBH', 'FMBI', 'FNBC', 'FNFG', 'FNWB', 'FPO', 'BEN', 'FSP', 'FRED', 'FCX', 'RAIL', 'FDP', 'FRPT', 'FTR', 'FRO', 'FRPH', 'FTD', 'FCN', 'FCEL', 'FULT', 'FF', 'GK', 'GAIA', 'GCAP', 'GALE', 'AJG', 'GBL', 'GME', 'GLPI', 'GCI', 'GPS', 'GRMN', 'IT', 'GLOG', 'GMT', 'GCP', 'GENC', 'GNRT', 'GNRC', 'BGC', 'GNCMA', 'GD', 'GE', 'GGP', 'GIS', 'GM', 'GCO', 'GWR', 'GEN', 'GNE', 'GNMK', 'GHDX', 'G', 'GNTX', 'GIII', 'GVA', 'GPK', 'GTN', 'AJX', 'GLDD', 'GXP', 'GSBC', 'GWB', 'GB', 'GNBC', 'GRBK', 'GDOT', 'GPRE', 'GBX', 'GCBC', 'GHL', 'GLRE', 'GEF', 'GRIF', 'GFF', 'GPI', 'GRPN', 'GRUB', 'GTT', 'GBNK', 'GES', 'GUID', 'GWRE', 'GPOR', 'HEES', 'HABT', 'HCKT', 'HAE', 'HAIN', 'HAL', 'HALL', 'HALO', 'HYH', 'HMPR', 'HBHC', 'HNH', 'HBI', 'HAFC', 'HASI', 'THG', 'HDNG', 'HOG', 'HAR', 'HTZ', 'HSKA', 'HES', 'HPE', 'HXL', 'HF', 'HIBB', 'ONE', 'HIW', 'HIL', 'HI', 'HRC', 'HTH', 'HLT', 'HIFS', 'HMSY', 'HNI', 'HFC', 'HOLX', 'HBCP', 'HOMB', 'HD', 'HMST', 'HTBI', 'HON', 'HOFT', 'HMN', 'HBNC', 'HZN', 'HZNP', 'HRL', 'HOS', 'HDP', 'HPT', 'HST', 'HMHC', 'HLI', 'HOV', 'HHC', 'HPQ', 'HRG', 'HSNI', 'HUBG', 'HUBB', 'HUBS', 'HPP', 'HUM', 'HBAN', 'HII', 'IMKTA', 'IM', 'INGR', 'INWK', 'IPHS', 'IOSP', 'INVA', 'INGN', 'ITEK', 'INOV', 'INO', 'IPHI', 'NSIT', 'INSM', 'NSP', 'IBP', 'IIIN', 'INST', 'PODD', 'INSY', 'IART', 'IDTI', 'INTC', 'IQNT', 'NTLA', 'I', 'IPAR', 'IBKR', 'ININ', 'ICPT', 'ICE', 'IDCC', 'TILE', 'IBOC', 'IGT', 'IP', 'ISCA', 'IPG', 'XENT', 'ISIL', 'IILG', 'IBM', 'INTL', 'IFF', 'ITCI', 'IL', 'SNOW', 'XON', 'INTU', 'JNPR', 'JUNO', 'LRN', 'KTWO', 'KAI', 'KALU', 'KAMN', 'KSU', 'KS', 'KAR', 'KPTI', 'KATE', 'KBH', 'KBR', 'KCG', 'KRNY', 'K', 'KELYA', 'KMPR', 'KMT', 'KW', 'KERX', 'KEY', 'KEYS', 'KEYW', 'KFRC', 'KRC', 'KE', 'KBAL', 'KMB', 'KIM', 'KMI', 'KND', 'KEX', 'KIRK', 'KITE', 'KRG', 'KLAC', 'KLXI', 'KMG', 'KNX', 'KNL', 'KN', 'KSS', 'KONA', 'KOPN', 'KOP', 'KFY', 'KOS', 'LXK', 'LGIH', 'LHCG', 'LBY', 'BATRA', 'BATRK', 'LBRDA', 'LBRDK', 'QVCA', 'LMCA', 'LMCK', 'LPT', 'LSXMA', 'LSXMK', 'TAX', 'LTRPA', 'LVNTA', 'LOCK', 'LPNT', 'LCUT', 'LFVN', 'LWAY', 'LGND', 'LLY', 'LLNW', 'LMNR', 'LECO', 'LNC', 'LIND', 'LNN', 'LLTC', 'LNKD', 'LBIO', 'LIOX', 'LGF', 'LPCN', 'LQDT', 'LAD', 'LFUS', 'LYV', 'LOB', 'LPSN', 'LKQ', 'LMT', 'L', 'LOGM', 'LORL', 'LPX', 'LOW', 'VAC', 'MMC', 'MRTN', 'MLM', 'MRVL', 'MAS', 'MASI', 'DOOR', 'MTZ', 'MA', 'MTDR', 'MTCH', 'MTRN', 'MTRX', 'MATX', 'MAT', 'MATW', 'MFRM', 'MXIM', 'MMS', 'MXL', 'MXWL', 'MBFI', 'MBI', 'MBTF', 'MCFT', 'MKC', 'MDR', 'MCD', 'MGRC', 'MCK', 'MDCA', 'MDC', 'MDU', 'MJN', 'MDGN', 'MEG', 'MPW', 'MDCO', 'MNOV', 'MDSO', 'MED', 'MDVN', 'MDLY', 'MD', 'MDT', 'MEET', 'MRD', 'MENT', 'MOD', 'MC', 'MHK', 'MOH', 'TAP', 'MNTA', 'MCRI', 'MDLZ', 'MGI', 'MNR', 'MORE', 'MPWR', 'TYPE', 'MNRO', 'MON', 'MNST', 'MWW', 'MCO', 'MOG.A', 'MS', 'MORN', 'MOS', 'MPAA', 'MSI', 'MOV', 'MRC', 'MSA', 'MSM', 'MSCI', 'MSGN', 'MTSC', 'MLI', 'MWA', 'LABL', 'MPSX', 'MFLX', 'MUR', 'MUSA', 'MFSF', 'MYE', 'MYL', 'MYOK', 'MYRG', 'MYGN', 'NBR', 'NC', 'NANO', 'NSTG', 'NK', 'NBIX', 'NSR', 'NVRO', 'NWHM', 'NJR', 'NEWM', 'NEWR', 'NRZ', 'SNR', 'NYCB', 'NYMT', 'NYRT', 'NYT', 'NWL', 'NFX', 'NLNK', 'NEU', 'NEM', 'NR', 'NWSA', 'NWS', 'NEWS', 'NXRT', 'NXST', 'NEE', 'EGOV', 'NCBS', 'NLSN', 'NIHD', 'NKE', 'NMBL', 'NI', 'NL', 'NMIH', 'NNBR', 'HLTH', 'NE', 'NBL', 'NDLS', 'NAT', 'NDSN', 'JWN', 'NSC', 'NTK', 'NOG', 'NTRS', 'NFBK', 'NRIM', 'NOC', 'OHI', 'OME', 'OMER', 'OMCL', 'OMC', 'OMN', 'ASGN', 'ONDK', 'ON', 'OMED', 'OGS', 'OLP', 'OB', 'OMF', 'OKE', 'OPHT', 'OPK', 'OPY', 'OPB', 'ORCL', 'OSUR', 'ORBC', 'OA', 'ORC', 'TIS', 'ONVO', 'ORN', 'ORIT', 'ORA', 'ORRF', 'OFIX', 'OSK', 'OSIS', 'OSIR', 'OTIC', 'OTTR', 'OUTR', 'OUT', 'OVAS', 'OSG', 'OSTK', 'OMI', 'OC', 'OI', 'ORM', 'OXFD', 'OXM', 'PTSI', 'PCCC', 'PFSI', 'PMT', 'PAG', 'PNR', 'PEN', 'PEBO', 'PFIS', 'PBCT', 'PUB', 'PEP', 'PRFT', 'PFGC', 'PSG', 'PKI', 'PRGO', 'PETS', 'PFNX', 'PFE', 'PFSW', 'PCG', 'PGTI', 'PIP', 'PMC', 'PHH', 'PHIIK', 'PAHC', 'PM', 'PSX', 'PLAB', 'DOC', 'PICO', 'PNY', 'PDM', 'PIR', 'PPC', 'PNK', 'PNFP', 'PF', 'PNW', 'PES', 'PXD', 'PJC', 'PBI', 'PJT', 'PLNT', 'PLPM', 'PLT', 'PAH', 'PLXS', 'PRLB', 'PRSC', 'PVBC', 'PFS', 'PROV', 'PRU', 'PSB', 'PTC', 'PTCT', 'PSA', 'PEG', 'PHM', 'PBYI', 'PSTG', 'PVH', 'PZN', 'QTWO', 'QADA', 'QCRH', 'QEP', 'QGEN', 'QLIK', 'QLGC', 'QRVO', 'QTS', 'QUAD', 'KWR', 'QCOM', 'QSII', 'QLYS', 'NX', 'PWR', 'DGX', 'STR', 'QDEL', 'QNST', 'Q', 'QHC', 'QUOT', 'RAX', 'RDN', 'RLGT', 'ROIAK', 'RSYS', 'RDUS', 'RDNT', 'RAS', 'RL', 'RMBS', 'ROIC', 'RPAI', 'SALE', 'RTRX', 'RVNC', 'REV', 'REX', 'REXR', 'RXN', 'RAI', 'RICE', 'RIGL', 'NAME', 'RNET', 'REI', 'RNG', 'RAD', 'RLI', 'RLJ', 'RMR', 'RRTS', 'RHI', 'ROK', 'COL', 'RMTI', 'RSTI', 'ROG', 'ROL', 'ROP', 'RST', 'ROST', 'RSE', 'ROVI', 'RDC', 'RCL', 'RGLD', 'RES', 'RPM', 'RPXC', 'RSPP', 'RTIX', 'RUBI', 'RT', 'RTEC', 'RUSHA', 'RUTH', 'R', 'RYI', 'SHOS', 'SGEN', 'SEAS', 'EYES', 'SCWX', 'SEIC', 'SCSS', 'SIR', 'SEM', 'SIGI', 'SEMG', 'SRE', 'SMTC', 'SENEA', 'SNH', 'SENS', 'SXT', 'SQBG', 'MCRB', 'SRG', 'SCI', 'SERV', 'NOW', 'SREV', 'SFBS', 'SHAK', 'SHEN', 'SHW', 'SFL', 'SCVL', 'SHBI', 'SHOR', 'SFLY', 'SSTK', 'SIFI', 'BSRR', 'SIGM', 'SBNY', 'SIG', 'SLGN', 'SILC', 'SGI', 'SLAB', 'SBY', 'SSNI', 'SAMG', 'SFNC', 'SPG', 'SSD', 'SPR', 'SAVE', 'SRC', 'SPLK', 'SPOK', 'SPWH', 'S', 'SFM', 'SPSC', 'SPXC', 'FLOW', 'SQ', 'SSNC', 'JOE', 'STJ', 'STAA', 'STAG', 'SSI', 'STMP', 'SMP', 'SXI', 'SWK', 'SPLS', 'SBUX', 'HOT', 'STWD', 'STRZA', 'STFC', 'STBZ', 'SNC', 'STT', 'STLD', 'SCS', 'SMRT', 'STML', 'SCL', 'SRCL', 'STL', 'STC', 'SF', 'SWC', 'SYBT', 'SGBK', 'SRI', 'STOR', 'STRP', 'SSYS', 'STRT', 'STRS', 'TLRD', 'TTWO', 'TAL', 'TLN', 'TLMR', 'TNDM', 'SKT', 'TNGO', 'TRGP', 'TGT', 'TASR', 'TCO', 'TMHC', 'TCB', 'AMTD', 'TMH', 'TISI', 'TECD', 'TTGT', 'TE', 'TK', 'TNK', 'TGNA', 'TRC', 'TDOC', 'TDY', 'TFX', 'TNAV', 'TDS', 'TTEC', 'TLGT', 'TPX', 'THC', 'TNC', 'TEN', 'TDC', 'TER', 'TEX', 'GLBL', 'TERP', 'TVIA', 'TRNO', 'TBNK', 'TSRO', 'TESO', 'TSLA', 'TSO', 'TSRA', 'TTEK', 'TDG', 'TRXC', 'RIG', 'TRU', 'TRV', 'TVPT', 'TRR', 'TREC', 'TG', 'THS', 'TRVN', 'TREX', 'TPH', 'TRCO', 'TCBK', 'TRS', 'TRMB', 'TNET', 'TRN', 'TPHS', 'TSE', 'TRIP', 'GTS', 'TSC', 'TBK', 'TGI', 'TRNC', 'TROX', 'TROV', 'TBI', 'TRUE', 'TRUP', 'TRST', 'TRMK', 'TTMI', 'TUBE', 'TUES', 'TUMI', 'TUP', 'TPB', 'TPC', 'TWTR', 'TWO', 'TYC', 'TYL', 'TSN', 'USCR', 'USG', 'USPH', 'UHS', 'UVE', 'ULH', 'UVSP', 'UNM', 'UE', 'URBN', 'UBA', 'USB', 'ECOL', 'USFD', 'USAT', 'USAK', 'USNA', 'USMD', 'UTMD', 'VFC', 'MTN', 'VLO', 'VHI', 'VR', 'VLY', 'VMI', 'VAL', 'VALU', 'VNDA', 'VNTV', 'VAR', 'VRNS', 'VDSI', 'VASC', 'WOOF', 'VGR', 'VVC', 'VEC', 'VECO', 'VEEV', 'VTR', 'VRA', 'VCYT', 'VER', 'PAY', 'VRNT', 'VRSN', 'VRSK', 'VBTX', 'VRTV', 'VZ', 'VSAR', 'WM', 'WAT', 'WSBF', 'WSO', 'WTS', 'WVE', 'W', 'WCIC', 'WDFC', 'WFT', 'WEB', 'WBMD', 'WBS', 'WEC', 'WTW', 'WRI', 'WMK', 'WCG', 'WFC', 'HCN', 'WERN', 'WSBC', 'WAIR', 'WCC', 'WTBA', 'WSTC', 'WMAR', 'WST', 'WABC', 'WR', 'WAL', 'WMC', 'WDC', 'WNR', 'WU', 'WFD', 'WLK', 'WLB', 'WRK', 'WHG', 'WEX', 'WEYS', 'WY', 'WGL', 'WHR', 'WTM', 'WSR', 'WWAV', 'WLL', 'YORW', 'YCB', 'YRCW', 'YUM', 'ZFGN', 'ZAGG', 'ZAYO', 'ZBRA', 'ZLTQ', 'ZEN', 'ZG', 'Z', 'ZBH', 'ZION', 'ZIOP', 'ZIXI', 'ZOES', 'ZTS', 'ZGNX', 'ZUMZ', 'ZNGA', 'WWD', 'WDAY', 'WKHS', 'WK', 'WRLD', 'INT', 'WWE', 'WOR', 'WPG', 'WPX', 'WMGI', 'WSFS', 'WYN', 'WYNN', 'XTLY', 'XBIT', 'XEL', 'XCRA', 'XNCR', 'XHR', 'XNPT', 'XRX', 'XLNX', 'XL', 'XOXO', 'XPO', 'MESG', 'XYL', 'YDKN', 'YHOO', 'YELP']

showCharts = raw_input('Would you like to show the financial data charts? (y/n)')

if showCharts.lower()=='y':
    print 'ok, charts will be shown'
elif showCharts.lower()=='n':
    print 'charts will not be shown'

def yahooKeyStats(stock):
    try:
        sourceCode = urllib2.urlopen('https://uk.finance.yahoo.com/q/ks?s=' + stock).read()
        pbr = sourceCode.split('Price/Book (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]

        if float(pbr) < 2.70:
            print 'price to book ratio', stock, pbr

            PEG5 = sourceCode.split(
                'PEG Ratio (5 yr expected)<font size="-1"><sup>1</sup></font>:</td><td class="yfnc_tabledata1">')[
                1].split('</td>')[0]
            if float(PEG5) < 1:

                PE12t = sourceCode.split('Trailing P/E (ttm, intraday):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
            if float(PE12t)<15:
                print'_________________________________'
                print''
                print stock, 'meets resquiremnts'
                print 'price to book', pbr
                print 'PEG forward 5 years', PEG5
                print 'Tradiling PE(12mo)', PE12t
                print'__________________________________'

                if showCharts.lower()=='y':

                    endLink = 'sort_order=asc'
                    netIncomeAr = []
                    revAr = []
                    endLink = 'sort_order=asc'

                    try:
                        netIncome = urllib2.urlopen(
                            'https://www.quandl.com/api/v3/datasets/RAYMOND/' + stock + '_NET_INCOME_Q.csv?api_key=EnsMMxcWJfz6mrzs3v6X').read()
                        print stock
                        print '+++++++++++++++++++++++++++++++'
                        revenue = urllib2.urlopen(
                            'https://www.quandl.com/api/v3/datasets/RAYMOND/' + stock + '_REVENUE_Q.csv?api_key=EnsMMxcWJfz6mrzs3v6X').read()

                        splitNI = netIncome.split('\n')
                        print 'Net Income'
                        for eachNI in splitNI[1:-1]:
                            print eachNI
                            netIncomeAr.append(eachNI)
                        print'_______________________'
                        splitRev = revenue.split('\n')
                        print 'Revenue:'
                        for eachRev in splitRev[1:-1]:
                            print eachRev
                            revAr.append(eachRev)
                        incomeDate, income = np.loadtxt(netIncomeAr, delimiter=',', unpack=True,
                                                        converters={0: mdates.strpdate2num('%Y-%M-%d')})

                        revDate, revenue = np.loadtxt(revAr, delimiter=',', unpack=True,
                                                      converters={0: mdates.strpdate2num('%Y-%M-%d')})
                        fig = plt.figure()
                        ax1 = plt.subplot2grid((6, 6), (0, 0), rowspan=3, colspan=6)
                        ax1.plot(incomeDate, income)
                        plt.ylabel('Net Income')
                        ax2 = plt.subplot2grid((6, 6), (3, 0), rowspan=3, colspan=6)
                        ax2.plot(revDate, revenue)
                        plt.ylabel('Revenue')

                        ax1.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
                        ax2.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

                        plt.subplots_adjust(hspace=0.53)

                        plt.show()


                    except Exception, e:
                        print 'failed the main quandle loop for reason of', str(e)


    except Exception, e:
        print 'failed in the main loop', str(e)


for eachStock in sp500:
    yahooKeyStats(eachStock)
    time.sleep(0.5)

