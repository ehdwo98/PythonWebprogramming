'''
1. 자동차 제조사 정보와 자동차 제품명을 기본으로 하고 기타 정보까지 딕셔너리로 
반환하는 make_car(manufacturer, model, **options)함수를 만들고, 실행해보세요.
'''
# 딕셔너리로 반환하는 함수
def make_car(manufacturer,model,**options):
    car_dict={
        'manufacturer':manufacturer.title(),
        'model':model.title(),
        }
    for option, value in options.items():
        car_dict[option]=value
    
    return car_dict
#함수 실행
car = make_car('subaru', 'outback', color='blue', AWD=True)
print(car)

car = make_car('honda', 'accord', year=1991, color='white', headlights='popup')
print(car)