def find_match(api_ips, db_ips):
    apiMap = {}

    for api_ip in api_ips:
        for key, value in api_ip.items():
            apiMap[key] = set(value)

    print("apiMap ::: ", apiMap)

    for dp_ip in db_ips:
        for key, value in dp_ip.items():
            if key not in apiMap:
                return False
            
            if apiMap[key] != set(value):
                return False
    return True   


api_ips = [
 {'australia': ['34.1.1.1', '1.1.1.1']},
 {'india': ['2.2.2.2']}
]

db_ips = [
 {'india': ['2.2.2.2']},
 {'australia': ['1.1.1.1']}
]

result = find_match(api_ips, db_ips)

print("RESULT: ", result)