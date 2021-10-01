import pygame

pygame.init()

# setting
display_size = (480, 360)
tick = 60
running = True

background = pygame.display.set_mode(display_size)
pygame.display.set_caption("pygame_test")

fps = pygame.time.Clock()

# 변수 color_black과 color_white를 설정(저장)
color_black = (0,0,0)
color_white = (255,255,255)

# color 리스트 만들고 검정색과 하얀색을 리스트에 넣음
# color_list[0] = color_black
# color_list[1] = color_white
color_list = [ color_black, color_white ]

# color 리스트 내의 item들 중, 현재의 color를 지정하는 index를 저장해줄 변수, 초기값은 0으로 color_black의 index
# color_list[current_color_index]와 같이 사용할 예정
current_color_index = 0
# color 리스트 내의 item 개수를 저장
num_color_list = len(color_list)

# color_change()라는 함수를 호출하면(사용하면) current_color_index의 다음 index를 리턴(반환)해줌
# ex) 리스트 내의 item이 총 5개일때, current가 0~3이라면 current+1을 4라면 0을 리턴
# parameter(매개변수)로 받는 current : 현재 index, total : 리스트의 총 item 개수
def color_change(current, total):
    # 다음 index는 현재 index에 1을 더한 값
    next = current + 1
    
    # 하지만 리스트의 index는 0~(리스트의 item 개수-1)을 가질 수 있으므로
    # 계산한 다음 index가 리스트의 item 개수와 같다면, 다음 아이템은 리스트의 첫 아이템, 이것의 index는 0
    if next == total:
        next = 0
        
    # 함수 실행의 결과로 계산한 다음 index를 반환
    return next

# 반복문 실행 횟수를 체크하기 위해 count 변수를 설정, 초기값 0, 반복문이 1번 실행될 때마다 1씩 up
count = 0

# running이 True일 때, 반복문을 계속해서 실행
while running:
    # 반복문이 실행되면 count를 1만큼 up
    # count += 1
    # 현재의 count를 print
    # print(count)
    
    # while문이 1초에 대략 tick번 정도 실행되도록 시간 지연 : 코드 실행이 해당 line에서 잠깐 멈춰있다고 생각하면 됨
    fps.tick(tick)
    # fps.tick(1)
    
    # background의 중앙에 반지름 7의 원을 그림
    # pygame.draw.circle(background, (0,0,255), (display_size[0]/2, display_size[1]/2), 7)
    
    # color_list에서 current_color_index+1번째 item의 color로 background를 모두 채움
    background.fill(color_list[current_color_index])
    
    # background의 중앙에 반지름 7의 원을 그림
    # pygame.draw.circle(background, (0,0,255), (display_size[0]/2, display_size[1]/2), 7)
    
    # 파이게임이 display 해주는 창을 update(갱신)
    pygame.display.update()
    
    # 사용자로부터 입력받은 이벤트 리스트를 가져와 event에 차례대로 넣으며 반복문을 실행
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            # quit를 입력으로 받으면 running을 False로 변경, quit 이벤트는 창 닫기 버튼 click시 발생
            running = False
    
    # index를 다음 index로 바꿔줌
    current_color_index = color_change(current_color_index, num_color_list)

pygame.quit()