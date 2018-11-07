from tr import tr
from ford_fulkerson import fordFulkerson
from dijkstra import dijkstra


if __name__ == "__main__": 
	G1 = {
		'AC' : {'RO':3072},
		'RO' : {'MT':3072, 'AC':3072},
		'MT' : {'RO':3072, 'MS':10240, 'GO':10240, 'PTT-MT':80},
		'PTT-MT' : {'MT':80},
		'MS' : {'MT':10240, 'PR':10240},
		'GO' : {'MT':10240, 'TO':10240, 'DF':20480},
		'TO' : {'GO':10240, 'PA':10240},
		'DF' : {'GO':20480, 'SP':10240, 'EBT-DF':2048, 'FIX':10240, 'RJ':10240, 'MG':10240, 'CE':10240, 'AM':3072},
		'PR' : {'PTT-PR':10240, 'RS':10240, 'SP':20480},
		'PTT-PR' : {'PR':10240},
		'RS' : {'PR':10240, 'SC':10240, 'EBT-RS':1024, 'PTT-RS':10240, 'MIA-RS':3072},
		'SP' : {'SC':2048, 'PR':2048, 'ANSP':10240, 'PTT-TR':30720, 'CLARA':6144, 'EBT-SP':1024, 'PTT-SP':40960, 'MIA-SP':102400, 'RJ':10240, 'CE':40960, 'MG':10240, 'DF':10240},
		'ANSP' : {'SP':10240},
		'PTT-TR' : {'SP':30720},
		'CLARA' : {'SP':6144},
		'EBT-SP' : {'SP':1024},
		'PTT-SP' : {'SP':40960},
		'MIA-SP' : {'SP':102400, 'FL-IX':10240, 'PTT-NAP':10240, 'CMDTY1':6144, 'CMDTY2':6144},
		'FL-IX': {'MIA-SP':10240},
		'PTT-NAP': {'MIA-SP':10240},
		'CMDTY1': {'MIA-SP':6144},
		'CMDTY2': {'MIA-SP':6144},
		'EBT-RS' : {'RS':1024},
		'PTT-RS' : {'RS':10240},
		'MIA-RS' : {'RS':3072},
		'SC' : {'RS':10240, 'PTT-SC':10240, 'SP':20480},
		'PTT-SC' : {'SC':10240},
		'RJ': {'SP':10240, 'DF':10240, 'MG':10240,'ES':10240, 'RdRio':10240, 'EBT-RJ':1024, 'PTT-RJ':20480},
		'EBT-DF' : {'DF':2048},
		'FIX' : {'DF':10240},
		'MG' : {'DF':10240, 'RJ':10240, 'SP':10240, 'BA':10240, 'CE':1024, 'PTT-MG':10240},
		'CE' : {'DF':10240, 'MG':10240, 'SP':40960, 'RR':1024, 'MA':10240, 'RN':10240, 'PTT-CE':10240, 'MIA-CE':40960, 'PE':10240},
		'AM' : {'DF':3072, 'PA':3072, 'RR':1024, 'PTT-AM':1024},
		'PA' : {'TO':10240, 'AM':3072, 'AP':1024, 'PI':3072, 'PTT-PA':1024, 'MA':10240},
		'ES' : {'RJ':10240, 'PTT-ES':1024, 'BA':20480},
		'RdRio': {'RJ':10240},
		'EBT-RJ' : {'RJ':1024},
		'PTT-RJ' : {'RJ':20480},
		'BA' : {'MG':10240, 'ES':20480, 'PTT-BA':10240, 'SE':10240, 'PE':10240},
		'PTT-MG' : {'MG':10240},
		'RR' : {'CE':1024, 'AM':1024},
		'MA' : {'CE':10240, 'PTT-MA':1024, 'PA':1240},
		'RN' : {'CE':10240, 'PTT-RN':1024, 'PB-JPA':10240, 'PB-CGE':102400},
		'MIA-CE' : {'CE':40960},
		'PTT-CE' : {'CE':10240},
		'PTT-MA' : {'MA':1024},
		'PE' : {'CE':10240, 'BA':10240, 'PTT-PE':10240, 'PB-CGE':102400, 'PI':3072, 'AL':10240},
		'PTT-AM' : {'AM':1024},
		'AP' : {'PA':1024},
		'PI' : {'PA':3072, 'PE':3072, 'PTT-PI':1024},
		'PTT-PA' : {'PA':1024},
		'PTT-ES' : {'ES':1024},
		'PTT-BA' : {'BA':10240},
		'SE' : {'BA':10240, 'AL':10240, 'PTT-SE':1024},
		'PTT-RN' : {'RN':1024},
		'PB-JPA' : {'RN':10240, 'PB-CGE':10240},
		'PB-CGE' : {'RN':102400, 'PE':102400, 'PB-JPA':10240, 'PTT-PB':2048},
		'PTT-PE' : {'PE':10240},
		'AL' : {'PE':10240, 'SE':10240, 'PTT-AL':1024},
		'PTT-PI' : {'PI':1024},
		'PTT-SE' : {'SE':1024},
		'PTT-PB' : {'PB-CGE':2048},
		'PTT-AL' : {'AL':1024},
	}

	G2 = {
		0 : {1:16, 2:13},
		1 : {3:12, 2:10},
		2 : {1:4, 4:14},
		3 : {2:9, 5:20},
		4 : {3:7, 5:4},
		5 : {}
	}

	max_flow = fordFulkerson(G1, 'SP', 'CE')
	#print(max_flow)
	#for key, value in max_flow.items():
	#	print(key, value)

	max_value = 0
	with open('output.txt', 'w') as f:
		for key, value in max_flow.items():
			string = str(key) + ' ' + str(value) + '\n'
			f.write(string)

		print('value', value)



