  
# -*- coding: utf-8 -*-

CONTRACTION_MAP = {
"ain't": "is not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"I'd": "I would",
"I'd've": "I would have",
"I'll": "I will",
"I'll've": "I will have",
"I'm": "I am",
"I've": "I have",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have",
"ur"    : "your",
"u"     : "you"
}
stopwords = ["amp", "u","ur",'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", "ain't","can't","can't've","'cause","could've","couldn't've","hadn't've","he'd","he'd've","he'll","he'll've","he's","how'd","how'd'y","how'll","how's","I'd","I'd've","I'll","I'll've","I'm","I've","i'd","i'd've","i'll","i'll've","i'm","i've","it'd","it'd've","it'll","it'll've","let's","ma'am","mayn't","might've","mightn't've","must've","mustn't've","needn't've","o'clock","oughtn't","oughtn't've","sha'n't","shan't've","she'd","she'd've","she'll","she'll've","shouldn't've","so've","so's","that'd","that'd've","that's","there'd","there'd've","there's","they'd","they'd've","they'll","they'll've","they're","they've","to've","we'd","we'd've","we'll","we'll've","we're","we've","what'll","what'll've","what're","what's","what've","when's","when've","where'd","where's","where've","who'll","who'll've","who's","who've","why's","why've","will've","won't've","would've","wouldn't've","y'all","y'all'd","y'all'd've","y'all're","y'all've","you'd've","you'll've"]

for k in CONTRACTION_MAP.keys():
	if k not in stopwords:
		print ("\""+k+"\"",end=",")


world_abbreviations = {
"AFGHANISTAN" : "AFG" ,
"ALBANIA" : "ALB" ,
"ALGERIA" : "DZA" ,
"AMERICAN SAMOA" : "ASM" ,
"ANDORRA" : "ADD" ,
"ANGOLA" : "AGO" ,
"ANGUILLA" : "AIA" ,
"ANTARCTICA" : "AQ" ,
"ANTIGUA AND BARBUDA" : "AG" ,
"ARGENTINA" : "ARG" ,
"ARMENIA" : "ARM" ,
"ARUBA" : "AW" ,
"AUSTRALIA" : "AUS" ,
"AUSTRIA" : "AUT" ,
"AZERBAIJAN" : "AZE" ,
"BAHAMAS" : "BHS" ,
"BAHRAIN" : "BHR" ,
"BANGLADESH" : "BGD" ,
"BARBADOS" : "BB" ,
"BELARUS" : "BLR" ,
"BELGIUM" : "BEL" ,
"BELIZE" : "BZ" ,
"BENIN" : "BJ" ,
"BERMUDA" : "BMU" ,
"BHUTAN" : "BTN" ,
"BOLIVIA" : "BOL" ,
"BOSNIA" : "BIH" ,
"BOTSWANA" : "BW" ,
"BOUVET ISLAND" : "BV" ,
"BRAZIL" : "BRA" ,
"BRITISH INDIAN OCEAN TERRITORY" : "IO" ,
"BRUNEI DARUSSALAM" : "BRN" ,
"BULGARIA" : "BGR" ,
"BURKINA FASO" : "BF" ,
"VATICAN CITY" : "VAT",
"BURUNDI" : "BI" ,
"CAMBODIA" : "KHM" ,
"CAMEROON" : "CMR" ,
"CANADA" : "CAN" ,
"CAPE VERDE" : "CV" ,
"CAYMAN ISLANDS" : "CYM" ,
"CENTRAL AFRICAN REPUBLIC" : "CAF" ,
"CHAD" : "TCD" ,
"CHILE" : "CHL" ,
"CHINA" : "CHN" ,
"CHRISTMAS ISLAND" : "CXR" ,
"COCOS (KEELING) ISLANDS" : "CC" ,
"COLOMBIA" : "COL" ,
"COMOROS" : "COM" ,
"CONGO" : "COG" ,
"CONGO, THE DEMOCRATIC REPUBLIC OF THE" : "COD" ,
"COOK ISLANDS" : "CK" ,
"COSTA RICA" : "CRI" ,
"IVORY COAST" : "CIV" ,
"CROATIA" : "HRV" ,
"CUBA" : "CUB" ,
"CYPRUS" : "CYP" ,
"CZECH" : "CZE" ,
"DENMARK" : "DNK" ,
"DJIBOUTI" : "DJ" ,
"DOMINICA" : "DMA" ,
"DOMINICAN REPUBLIC" : "DOM" ,
"ECUADOR" : "ECU" ,
"EGYPT" : "EGY" ,
"EL SALVADOR" : "SLV" ,
"EQUATORIAL GUINEA" : "GNQ" ,
"ERITREA" : "ER" ,
"ESTONIA" : "EST" ,
"ETHIOPIA" : "ETH" ,
"FALKLAND ISLANDS (MALVINAS)" : "FK" ,
"FAROE ISLANDS" : "FO" ,
"FIJI" : "FJI" ,
"FINLAND" : "FIN" ,
"FRANCE" : "FRA" ,
"FRENCH GUIANA" : "GF" ,
"FRENCH POLYNESIA" : "PF" ,
"FRENCH SOUTHERN TERRITORIES" : "TF" ,
"GABON" : "GAB" ,
"GAMBIA" : "GMB" ,
"GEORGIA" : "GEO" ,
"GERMANY" : "DEU" ,
"GHANA" : "GHA" ,
"GIBRALTAR" : "GI" ,
"GREECE" : "GRC" ,
"GREENLAND" : "GRL" ,
"GRENADA" : "GRD" ,
"GUADELOUPE" : "GP" ,
"GUAM" : "GUM" ,
"GUATEMALA" : "GTM" ,
"GUERNSEY" : "GGY" ,
"GUINEA" : "GN" ,
"GUINEA-BISSAU" : "GW" ,
"GUYANA" : "GUY" ,
"HAITI" : "HTI" ,
"HONDURAS" : "HND" ,
"HONG KONG" : "HKG" ,
"HUNGARY" : "HUN" ,
"ICELAND" : "ISL" ,
"INDIA" : "IND" ,
"INDONESIA" : "IDN" ,
"IRAN" : "IRN" ,
"IRAQ" : "IRQ" ,
"IRELAND" : "IRL" ,
"ISLE OF MAN" : "IM" ,
"ISRAEL" : "ISR" ,
"ITALY" : "ITA" ,
"JAMAICA" : "JAM" ,
"JAPAN" : "JPN" ,
"JERSEY" : "JE" ,
"JORDAN" : "JOR" ,
"KAZAKHSTAN" : "KAZ" ,
"KENYA" : "KEN" ,
"KIRIBATI" : "KIR" ,
"NORTH KOREA" : "PRK" ,
"SOUTH KOREA" : "KOR" ,
"KUWAIT" : "KWT" ,
"KYRGYZSTAN" : "KGZ" ,
"LAOS" : "LAO" ,
"LATVIA" : "LVA" ,
"LEBANON" : "LBN" ,
"LESOTHO" : "LS" ,
"LIBERIA" : "LBR" ,
"LIBYA" : "LBY" ,
"LIECHTENSTEIN" : "LIE" ,
"LITHUANIA" : "LTU" ,
"LUXEMBOURG" : "LUX" ,
"MACAO" : "MAC" ,
"MACEDONIA" : "MK" ,
"MADAGASCAR" : "MDG" ,
"MALAWI" : "MWI" ,
"MALAYSIA" : "MYS" ,
"MALDIVES" : "MDV" ,
"MALI" : "MLI" ,
"MALTA" : "MLT" ,
"MARSHALL ISLANDS" : "MHL" ,
"MARTINIQUE" : "MQ" ,
"MAURITANIA" : "MR" ,
"MAURITIUS" : "MU" ,
"MAYOTTE" : "YT" ,
"MEXICO" : "MEX" ,
"MICRONESIA, FEDERATED STATES OF" : "FM" ,
"MOLDOVA" : "MDA" ,
"MONACO" : "MCO" ,
"MONGOLIA" : "MNG" ,
"MONTENEGRO" : "MNE" ,
"MONTSERRAT" : "MS" ,
"MOROCCO" : "MAR" ,
"MOZAMBIQUE" : "MOZ" ,
"MYANMAR" : "MMR" ,
"NAMIBIA" : "NAM" ,
"NAURU" : "NRU" ,
"NEPAL" : "NPL" ,
"NETHERLANDS" : "NLD" ,
"NEW CALEDONIA" : "NCL" ,
"NEW ZEALAND" : "NZL" ,
"NICARAGUA" : "NIC" ,
"NIGER" : "NER" ,
"NIGERIA" : "NGA" ,
"NIUE" : "NU" ,
"NORFOLK ISLAND" : "NF" ,
"NORTHERN MARIANA ISLANDS" : "MP" ,
"NORWAY" : "NOR" ,
"OMAN" : "OMN" ,
"PAKISTAN" : "PAK" ,
"PALAU" : "PW" ,
"PALESTINE" : "PSE" ,
"PANAMA" : "PAN" ,
"PAPUA NEW GUINEA" : "PNG" ,
"PARAGUAY" : "PRY" ,
"PERU" : "PER" ,
"PHILIPPINES" : "PHL" ,
"PITCAIRN" : "PN" ,
"POLAND" : "POL" ,
"PORTUGAL" : "PRT" ,
"PUERTO RICO" : "PRI" ,
"QATAR" : "QAT" ,
"ROMANIA" : "ROU" ,
"RUSSIA" : "RUS" ,
"RWANDA" : "RWA" ,
"SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA" : "SH" ,
"SAINT KITTS AND NEVIS" : "KN" ,
"SAINT LUCIA" : "LC" ,
"SAINT MARTIN (FRENCH PART)" : "MF" ,
"SAINT PIERRE AND MIQUELON" : "PM" ,
"SAINT VINCENT AND THE GRENADINES" : "VC" ,
"SAMOA" : "WS" ,
"SAN MARINO" : "SM" ,
"SAO TOME AND PRINCIPE" : "ST" ,
"SAUDI ARABIA" : "SAU" ,
"SENEGAL" : "SEN" ,
"SERBIA" : "SRB" ,
"SEYCHELLES" : "SC" ,
"SIERRA LEONE" : "SLE" ,
"SINGAPORE" : "SGP" ,
"SLOVAKIA" : "SVK" ,
"SLOVENIA" : "SVN" ,
"SOLOMON ISLANDS" : "SLB" ,
"SOMALIA" : "SOM" ,
"SOUTH AFRICA" : "ZAF" ,
"SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS" : "GS" ,
"SOUTH SUDAN" : "SSD" ,
"SPAIN" : "ESP" ,
"SRI LANKA" : "LKA" ,
"SUDAN" : "SDN" ,
"SURINAME" : "SUR" ,
"SWAZILAND" : "SZ" ,
"SWEDEN" : "SWE" ,
"SWITZERLAND" : "CHE" ,
"SYRIA" : "SYR" ,
"TAIWAN" : "TWN" ,
"TAJIKISTAN" : "TJK" ,
"TANZANIA" : "TZA" ,
"THAILAND" : "THA" ,
"TIMOR-LESTE" : "TL" ,
"TOGO" : "TG" ,
"TOKELAU" : "TK" ,
"TONGA" : "TO" ,
"TRINIDAD AND TOBAGO" : "TT" ,
"TUNISIA" : "TUN" ,
"TURKEY" : "TUR" ,
"TURKMENISTAN" : "TKM" ,
"TURKS AND CAICOS ISLANDS" : "TC" ,
"TUVALU" : "TUV" ,
"UGANDA" : "UGA" ,
"UKRAINE" : "UKR" ,
"UNITED ARAB EMIRATES" : "ARE" ,
"UNITED KINGDOM" : "GBR" ,
"UNITED STATES" : "USA" ,
"URUGUAY" : "URY" ,
"UZBEKISTAN" : "UZB" ,
"VANUATU" : "VUT" ,
"VENEZUELA" : "VEN" ,
"VIETNAM" : "VNM" ,
"VIRGIN ISLANDS, BRITISH" : "VG" ,
"VIRGIN ISLANDS, U.S." : "VI" ,
"WALLIS AND FUTUNA" : "WF" ,
"WESTERN SAHARA" : "EH" ,
"YEMEN" : "YEM" ,
"ZAMBIA" : "ZMB" ,
"ZIMBABWE" : "ZWE" ,

}