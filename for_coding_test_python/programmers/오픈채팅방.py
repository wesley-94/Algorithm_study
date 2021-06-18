# 프로그래머스
# 2019 KAKAO BLIND RECRUITMENT
# 오픈채팅방

def solution(records):
    records = list(map(lambda r: r.split(), records))

    users = {}
    for record in records:
        if len(record) > 2:
            users[record[1]] = record[2]

    msg = { 'Enter' : '님이 들어왔습니다.', 'Leave' : '님이 나갔습니다.' }
    msgs = []
    for record in records:
        if record[0] != 'Change':
            msgs.append(users[record[1]] + msg[record[0]])
    return msgs