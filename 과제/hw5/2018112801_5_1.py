"""
1.사람 이름이 5개 포함된 리스트를 만들고, 그 중 하나를 'admin'으로 합니다.

사용자가 웹사이트에 로그인하면(로그인 환경을 가정하고 userid를 변수에 저장), 서로 다른 인사말이 출력되도록 만듭니다.

admin의 경우, "You are logged in with ADMIN privilege."
일반 사용자의 경우 "Welcome back, <userid>"메시지.
아이디가 없을 경우 "Something wrong happened."
"""
# 사용자 설정
user = ['a','b','c','d','admin']
# 사용자가 로그인했을 때의 아이디 저장
userid = ['a','b','c','d','admin','e','f']

for userid in userid :
    # 로그인했을 때 admin일 경우
    if 'admin' in userid :
        print("You are logged in with ADMIN privilege.")
    # 로그인했을 때 일반 사용자일 경우
    elif userid in user :
        print("Welcome back, "+ userid)
    # 로그인했을 때 일치하는 사용자가 없을 경우
    else :
        print("Something wrong happened.")
    
    