#user interface runner

import pygame, pickle, random
from os import listdir

from file_path_converter import convert_path
from schedule import get_schedule
from schedule import get_games_in_a_month
from months_in_order import get_month_number
from months_in_order import get_days_in_a_month
from months_in_order import get_number_month
from team_rating_calculator import calculate_rating
from match_sim_calculator import  match_sim
from goals_randomizer import randomize_goals

pi = False

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Currier', 25)

myfont2 = pygame.font.SysFont('Currier', 50)

myfont3 = pygame.font.SysFont('Currier', 15)

myfont4 = pygame.font.SysFont('Currier', 20)

display = pygame.display.set_mode((792, 612))

pygame.display.set_caption('Project')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
key_color = (58, 166, 221)
gray = (229, 229, 229, 255)
light_blue = (58, 166, 221, 255)

#Load Database and stuff

"""if pi :
    arsenal = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Arsenal.dat'), 'rb'))
    aston_villa = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Aston Villa.dat'), 'rb'))
    brighton_and_hove_albion = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Brighton & Hove Albion.dat'), 'rb'))
    burnley = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Burnley.dat'), 'rb'))
    chelsea = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Chelsea.dat'), 'rb'))
    crystal_palace = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Crystal Palace.dat'), 'rb'))
    everton = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Everton.dat'), 'rb'))
    fulham = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Fulham.dat'), 'rb'))
    leeds_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leeds United.dat'), 'rb'))
    leicester_city = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leicester City.dat'), 'rb'))
    liverpool = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Liverpool.dat'), 'rb'))
    manchester_city = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester City.dat'), 'rb'))
    manchester_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester United.dat'), 'rb'))
    newcastle_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Newcastle United.dat'), 'rb'))
    sheffield_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Sheffield United.dat'), 'rb'))
    southampton = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Southampton.dat'), 'rb'))
    tottenham_hotspur = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Tottenham Hotspur.dat'), 'rb'))
    west_bromwich_albion = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Bromwich Albion.dat'), 'rb'))
    west_ham_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Ham United.dat'), 'rb'))
    wolverhampton_wanderers = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Wolverhampton Wanderers.dat'), 'rb'))
else :
    arsenal = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Arsenal.dat', 'rb'))
    aston_villa = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Aston Villa.dat', 'rb'))
    brighton_and_hove_albion = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Brighton & Hove Albion.dat', 'rb'))
    burnley = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Burnley.dat', 'rb'))
    chelsea = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Chelsea.dat', 'rb'))
    crystal_palace = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Crystal Palace.dat', 'rb'))
    everton = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Everton.dat', 'rb'))
    fulham = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Fulham.dat', 'rb'))
    leeds_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leeds United.dat', 'rb'))
    leicester_city = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leicester City.dat', 'rb'))
    liverpool = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Liverpool.dat', 'rb'))
    manchester_city = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester City.dat', 'rb'))
    manchester_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester United.dat', 'rb'))
    newcastle_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Newcastle United.dat', 'rb'))
    sheffield_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Sheffield United.dat', 'rb'))
    southampton = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Southampton.dat', 'rb'))
    tottenham_hotspur = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Tottenham Hotspur.dat', 'rb'))
    west_bromwich_albion = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Bromwich Albion.dat', 'rb'))
    west_ham_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Ham United.dat', 'rb'))
    wolverhampton_wanderers = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Wolverhampton Wanderers.dat', 'rb'))
"""

#######################################################################################################################################

#Saves Screen Stuff

#######################################################################################################################################

save_number = 0

def get_save_image(save_number) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Images\\', 'Save', str(save_number), '.png'])
    if pi :
        path = convert_path(path)
    return pygame.image.load(path).convert()

save_background_images = []
for i in range(10) :
    current_save_image = get_save_image(i+1)
    save_background_images.append(current_save_image)

current_save_image = save_background_images[save_number]

save_names = []
for i in range(10) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Saves\\', 'File', str(i+1), 'BasicInfo.dat'])
    if pi :
        path = convert_path(path)
    basic_info = pickle.load(open(path, 'rb'))
    save_names.append(basic_info['SaveName'])

save_names_texts = []
for save_name in save_names :
    save_names_texts.append(myfont.render(save_name, True, (0, 0, 0)))
    
clicker_mode = False
current_clicked = (0, 0)


y_difference = 37
x_start, x_end = 43, 761
buttons = []
for i in range(10) :
    first_y = 154+(i*y_difference)
    second_y = first_y+y_difference
    buttons.append([first_y, second_y])

offset = [12, 13, 14, 16, 17, 19, 20, 22, 23, 25]


save_selected = None

#######################################################################################################################################

#Name Save Stuff

#######################################################################################################################################

if not pi :
    keyboard_order = {
        pygame.K_m:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-002.png').convert(),
        pygame.K_n:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-003.png').convert(),
        pygame.K_b:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-004.png').convert(),
        pygame.K_v:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-005.png').convert(),
        pygame.K_c:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-006.png').convert(),
        pygame.K_x:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-007.png').convert(),
        pygame.K_z:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-008.png').convert(),
        pygame.K_l:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-009.png').convert(),
        pygame.K_k:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-010.png').convert(),
        pygame.K_j:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-011.png').convert(),
        pygame.K_h:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-012.png').convert(),
        pygame.K_g:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-013.png').convert(),
        pygame.K_f:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-014.png').convert(),
        pygame.K_d:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-015.png').convert(),
        pygame.K_s:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-016.png').convert(),
        pygame.K_a:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-017.png').convert(),
        pygame.K_p:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-018.png').convert(),
        pygame.K_o:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-019.png').convert(),
        pygame.K_i:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-020.png').convert(),
        pygame.K_u:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-021.png').convert(),
        pygame.K_y:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-022.png').convert(),
        pygame.K_t:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-023.png').convert(),
        pygame.K_r:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-024.png').convert(),
        pygame.K_e:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-025.png').convert(),
        pygame.K_w:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-026.png').convert(),
        pygame.K_q:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-027.png').convert(),
        pygame.K_BACKSPACE:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-028.png').convert(),
        pygame.K_0:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-029.png').convert(),
        pygame.K_9:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-030.png').convert(),
        pygame.K_8:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-031.png').convert(),
        pygame.K_7:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-032.png').convert(),
        pygame.K_6:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-033.png').convert(),
        pygame.K_5:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-034.png').convert(),
        pygame.K_4:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-035.png').convert(),
        pygame.K_3:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-036.png').convert(),
        pygame.K_2:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-037.png').convert(),
        pygame.K_1:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-038.png').convert(),
    }
    
if pi :
    keyboard_order = {
        pygame.K_m:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-002.png')).convert(),
        pygame.K_n:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-003.png')).convert(),
        pygame.K_b:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-004.png')).convert(),
        pygame.K_v:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-005.png')).convert(),
        pygame.K_c:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-006.png')).convert(),
        pygame.K_x:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-007.png')).convert(),
        pygame.K_z:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-008.png')).convert(),
        pygame.K_l:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-009.png')).convert(),
        pygame.K_k:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-010.png')).convert(),
        pygame.K_j:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-011.png')).convert(),
        pygame.K_h:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-012.png')).convert(),
        pygame.K_g:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-013.png')).convert(),
        pygame.K_f:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-014.png')).convert(),
        pygame.K_d:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-015.png')).convert(),
        pygame.K_s:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-016.png')).convert(),
        pygame.K_a:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-017.png')).convert(),
        pygame.K_p:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-018.png')).convert(),
        pygame.K_o:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-019.png')).convert(),
        pygame.K_i:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-020.png')).convert(),
        pygame.K_u:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-021.png')).convert(),
        pygame.K_y:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-022.png')).convert(),
        pygame.K_t:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-023.png')).convert(),
        pygame.K_r:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-024.png')).convert(),
        pygame.K_e:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-025.png')).convert(),
        pygame.K_w:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-026.png')).convert(),
        pygame.K_q:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-027.png')).convert(),
        pygame.K_BACKSPACE:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-028.png')).convert(),
        pygame.K_0:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-029.png')).convert(),
        pygame.K_9:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-030.png')).convert(),
        pygame.K_8:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-031.png')).convert(),
        pygame.K_7:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-032.png')).convert(),
        pygame.K_6:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-033.png')).convert(),
        pygame.K_5:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-034.png')).convert(),
        pygame.K_4:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-035.png')).convert(),
        pygame.K_3:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-036.png')).convert(),
        pygame.K_2:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-037.png')).convert(),
        pygame.K_1:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-038.png')).convert(),
    }

keyboard_letters = {
    pygame.K_m:'M',
    pygame.K_n:'N',
    pygame.K_b:'B',
    pygame.K_v:'V',
    pygame.K_c:'C',
    pygame.K_x:'X',
    pygame.K_z:'Z',
    pygame.K_l:'L',
    pygame.K_k:'K',
    pygame.K_j:'J',
    pygame.K_h:'H',
    pygame.K_g:'G',
    pygame.K_f:'F',
    pygame.K_d:'D',
    pygame.K_s:'S',
    pygame.K_a:'A',
    pygame.K_p:'P',
    pygame.K_o:'O',
    pygame.K_i:'I',
    pygame.K_u:'U',
    pygame.K_y:'Y',
    pygame.K_t:'T',
    pygame.K_r:'R',
    pygame.K_e:'E',
    pygame.K_w:'W',
    pygame.K_q:'Q',
    pygame.K_0:'0',
    pygame.K_9:'9',
    pygame.K_8:'8',
    pygame.K_7:'7',
    pygame.K_6:'6',
    pygame.K_5:'5',
    pygame.K_4:'4',
    pygame.K_3:'3',
    pygame.K_2:'1',
    pygame.K_1:'1',
}

def get_x_value(width) :
    return int((792-width)/2)

current_typed = ""
current_typed_text = myfont2.render(current_typed, True, light_blue)
current_typed_x = get_x_value(current_typed_text.get_width())

if pi :
    default_typed_screen = pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-001.png')).convert()

if not pi :
    default_typed_screen = pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-001.png').convert()

current_typed_screen = default_typed_screen

space_bar_down = False

enter_extension_string = "the Save"
string2 = "save"

name_save_header = myfont2.render("Enter a Name for "+enter_extension_string, True, light_blue)
name_save_header_x = get_x_value(name_save_header.get_width())

too_many_chars_text = myfont.render("You've reached the max amount of characters!", True, red)
too_many_chars_x = get_x_value(too_many_chars_text.get_width())

too_many_chars = False

enter_or_submit = True
over_submit = False

new_save_name = ''

entering_save = True

#######################################################################################################################################

#Calendar Screen

#Temporary Save Stuff

current_data = {
    'TeamName':'Arsenal',
    'ManagerName':'Reggie Hyde',
    'CurrentLineup':['Bernd Leno', 'Hector Bellerin', 'David Luiz', 'Gabriel', 'Kieran Tierney', 'Thomas Partey', 'Granit Xhaka', 'Bukayo Saka', 'Gabriel Martinelli', 'Martin Odegaard', 'Alexandre Lacazette'],
    'CurrentFormation':'4-2-3-1 (Wide)',
    'CurrentBudget':100000000,
    'CurrentTeamOverall':79,
    'CurrentDate':'September 1 2020',
    'CurrentEmails':[['Welcome to Arsenal, Manager Hyde. Here is your email inbox where you will receive important messages. Be sure to check your email to stay updated on the Premier League.', 'urmom', '6/1/2020']],
    'UnreadEmails':0,
    'CurrentStandings':{},
    'CurrentStandingsInOrder':[],
    'TopScorers':{},
    'TopScorersInOrder':[],
    'TopAssistors':{},
    'TopAssistorsInOrder':[],
    'Arsenal_Players':{},
    'Arsenal_Formation':'4-2-3-1 (Wide)',
    'Arsenal_Lineup':['Bernd Leno', 'Hector Bellerin', 'David Luiz', 'Gabriel', 'Kieran Tierney', 'Thomas Partey', 'Granit Xhaka', 'Bukayo Saka', 'Gabriel Martinelli', 'Martin Odegaard', 'Alexandre Lacazette'],
    'Aston Villa_Players':{},
    'Aston Villa_Formation':'4-2-3-1 (Wide)',
    'Aston Villa_Lineup':['Emiliano Martinez', 'Matty Cash', 'Ezri Konsa', 'Tyrone Mings', 'Matt Targett', 'Douglas Luiz', 'John McGinn', 'Bertrand Traore', 'Anwar El Ghazi', 'Jack Grealish', 'Ollie Watkins'],
}


teams_in_league = ['Arsenal', 'Aston Villa']

for team in teams_in_league :
    if pi :
        team_path = convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\'+team+'.dat')
    else :
        team_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\'+team+'.dat'
    key = team+'_Players'
    current_data[key] = pickle.load(open(team_path, 'rb'))


red_cover = pygame.Surface((71,71))  # the size of your rect
red_cover.set_alpha(128)                # alpha level
red_cover.fill((255,0,0))           # this fills the entire surface


"""
while calendar :
    display.fill(white)
    display.blit(current_calendar_screen, (0, 0))
    display.blit(red_cover, (day_x, day_y))
    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONDOWN :
            coords = pygame.mouse.get_pos()
            print(coords)
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                day_x += 1
            elif event.key == pygame.K_LEFT :
                day_x -= 1
            elif event.key == pygame.K_DOWN :
                day_y += 1
            elif event.key == pygame.K_UP :
                day_y -= 1
            elif event.key == pygame.K_RETURN :
                coords_of_days[current_date] = [day_x, day_y]
                current_date, change_screen = advance_one_day(current_date)
                if change_screen :
                    print(coords_of_days)
                    quit()
                day_x, day_y = guess_coords_of_day(current_date)
    pygame.display.update()
"""

teams_in_league = [
    'Arsenal',
    'Aston Villa',
    'Brighton & Hove Albion',
    'Burnley',
    'Chelsea',
    'Crystal Palace',
    'Everton',
    'Fulham',
    'Leeds United',
    'Leicester City',
    'Liverpool',
    'Manchester City',
    'Manchester United',
    'Newcastle United',
    'Sheffield United',
    'Southampton',
    'Tottenham Hotspur',
    'West Bromwich Albion',
    'West Ham United',
    'Wolverhampton Wanderers'
]

coords_of_days = {
    '1': (55, 190),
    '2': (127, 190),
    '3': (199, 190),
    '4': (271, 190),
    '5': (343, 190),
    '6': (415, 190),
    '7': (487, 190),
    '8': (56, 262),
    '9': (128, 262),
    '10': (200, 262),
    '11': (272, 262),
    '12': (344, 262),
    '13': (416, 262),
    '14': (487, 262),
    '15': (56, 335),
    '16': (128, 335),
    '17': (200, 335),
    '18': (272, 335),
    '19': (344, 335),
    '20': (416, 335),
    '21': (487, 335),
    '22': (56, 407),
    '23': (128, 407),
    '24': (200, 407),
    '25': (272, 407),
    '26': (344, 407),
    '27': (416, 407),
    '28': (487, 407),
    '29': (56, 479),
    '30': (128, 479),
    '31': (200, 479)
}



def unpack_date(date) :
    splitted = date.split(' ') 
    return [splitted[0], int(splitted[1]), int(splitted[2])]

def build_date(month, day, year) :
    return ' '.join([month, str(day), str(year)])

def advance_one_day(date) :
    month, day, year = unpack_date(date)
    month_number = get_month_number(month)
    change_screen = False
    if day == get_days_in_a_month(month) :
        if month == 'December' :
            month, day, year = 'January', 1, year+1
        else :
            month, day, year = get_number_month(month_number+1), 1, year
        change_screen = True
    else :
        month, day, year = month, day+1, year
    return build_date(month, day, year), change_screen

def guess_coords_of_day(date) :
    month, day, year = unpack_date(date)
    mod = day % 7
    if mod == 0 :
        down, right = int((day-mod)/7)-1, 7
    else :
        down, right = int((day-mod)/7), mod
    return ((right-1)*73)+55, (down*73)+190


calendar_screens = []

for i in range(12) :
    path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Month-'+str(i+1)+'.png'
    if pi :
        path = convert_path(path)
    calendar_screens.append(pygame.image.load(path).convert())

team = current_data['TeamName']
print(team)
current_date = current_data['CurrentDate']
month, day, year = unpack_date(current_date)
month_number = get_month_number(month)
current_calendar_screen = calendar_screens[month_number]



team_logos = {}
team_simming_logos = {}

for t in teams_in_league :
    path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Images\\'+t+'.png'
    if pi :
        path = convert_path(path)
    loaded_image_logo = pygame.image.load(path).convert_alpha()
    team_logos[t] = pygame.transform.scale(loaded_image_logo, (40, 40))
    team_simming_logos[t] = pygame.transform.scale(loaded_image_logo, (70, 70))

def get_coords_of_logo_and_text(team, left_or_right) :
    x_difference = 35
    logo = team_simming_logos[team]
    logo_text = myfont.render(team, True, white)
    logo_text_width = logo_text.get_width()
    logo_full_width = sum([logo_text_width, 70, x_difference])
    logo_x = int((int(792/2)-logo_full_width)/2)
    logo_text_x = sum([logo_x, 40, x_difference])
    offset = (int(792/2)*left_or_right)
    if left_or_right == 0 :
        return logo, logo_text, logo_x+offset, logo_text_x+offset, 30, 57
    return logo, logo_text, logo_text_x+offset, logo_x+offset, 30, 57
 



schedule_dict = get_schedule()
dates_of_games_in_month = get_games_in_a_month(month, schedule_dict, team)

GAME_text = myfont3.render("GAME", True, white)
GAMEVS_text = myfont3.render("VS", True, white)

def mouse_over_button(pos, x, y, width, height) :
    return pos[0] >= x and pos[0] <= x+width and pos[1] >= y and pos[1] <= y+height

def display_button(button, pos) :
    x, y, width, height = button[0], button[1], button[2], button[3]
    over_button = mouse_over_button(pos, x, y, width, height)
    if over_button :
        color = button[5]
        text = button[7]
    else :
        color = button[4]
        text = button[6]
    text_width, text_height = button[-2], button[-1]
    text_x, text_y = x+int((width-text_width)/2), y+int((height-text_height)/2)
    pygame.draw.rect(display, color, pygame.Rect(x, y, width, height))
    display.blit(text, (text_x, text_y))
    return over_button

calendar_buttons = [
    [300, 120, 100, 30, white, red, myfont3.render("START SIM", True, red), myfont3.render("START SIM", True, white)],
    [300, 120, 100, 30, red, white, myfont3.render("END SIM", True, white), myfont3.render("END SIM", True, red)],
    [300, 120, 100, 30, white, red, myfont3.render("PLAY MATCH", True, red), myfont3.render("PLAY MATCH", True, white)],
]

for i, calendar_button in enumerate(calendar_buttons) :
    calendar_buttons[i] = calendar_buttons[i] + [calendar_button[-2].get_width(), calendar_button[-2].get_height()]


over_sim_button = False
simming = False
simming_count = 0
button_index = 0

match_simming = False 
stopped_on_matchday = False
match_sim_background_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Match Sim.png'
if pi :
    match_sim_background_path = convert_path(match_sim_background_path)
match_sim_background = pygame.image.load(match_sim_background_path).convert()

#######################################################################################################################################

manager_loop = True
saves_menu = False
name_save = False
calendar = True



while manager_loop :
    while calendar :
        display.fill(white)
        if match_simming :
            display.blit(match_sim_background, (0, 0))
            display.blit(stadium_text, (stadium_text_x, 500))
            display.blit(user_logo, (user_logo_x, user_logo_y))
            display.blit(user_logo_text, (user_logo_text_x, user_logo_text_y))
            display.blit(opponent_logo, (opponent_logo_x, opponent_logo_y))
            display.blit(opponent_logo_text, (opponent_logo_text_x, opponent_logo_text_y))
        else :
            display.blit(current_calendar_screen, (0, 0))
            x, y = pygame.mouse.get_pos()
            for game_date in dates_of_games_in_month :
                opponent, stadium, left_or_right = dates_of_games_in_month[game_date]
                m, d = game_date.split(' ')
                display_coords = coords_of_days[d]
                display_coords_logo = (display_coords[0]+15, display_coords[1]+30)
                display_coords_text = (display_coords[0]+22, display_coords[1]+10)
                display_coords_text2 = (display_coords[0]+30, display_coords[1]+20)
                display.blit(team_logos[opponent], display_coords_logo)
                display.blit(GAME_text, display_coords_text)
                display.blit(GAMEVS_text, display_coords_text2)
            for event in pygame.event.get() :
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if over_sim_button :
                        if stopped_on_matchday :
                            match_simming = True
                            stadium_text = myfont.render(next_stadium, True, white)
                            stadium_text_width = stadium_text.get_width()
                            stadium_text_x = int((792-stadium_text_width)/2)
                            user_logo, user_logo_text, user_logo_x, user_logo_text_x, user_logo_y, user_logo_text_y = get_coords_of_logo_and_text(team, next_left_or_right)
                            if next_left_or_right == 0 :
                                opponent_lor = 1
                            else :
                                opponent_lor = 0
                            opponent_logo, opponent_logo_text, opponent_logo_x, opponent_logo_text_x, opponent_logo_y, opponent_logo_text_y = get_coords_of_logo_and_text(next_opponent, opponent_lor)


                            user_formation = current_data['CurrentFormation']
                            user_players = current_data[team+'_Players']
                            user_lineup = current_data['CurrentLineup']


                            next_opponent = 'Aston Villa'
                            opponent_formation = current_data[next_opponent+'_Formation']
                            opponent_players = current_data[next_opponent+'_Players']
                            opponent_lineup = current_data[next_opponent+'_Lineup']
                            
                            
                            user_rating = calculate_rating(user_players, user_lineup, user_formation)
                            opponent_rating = calculate_rating(opponent_players, opponent_lineup, opponent_formation)

                            if next_left_or_right == 0 :
                                winner, score_difference = match_sim(user_rating, opponent_rating, team, next_opponent)
                                score, user_scorers, opponent_scorers = randomize_goals(user_players, opponent_players, user_lineup, opponent_lineup, team, next_opponent, user_formation, opponent_formation, winner, score_difference)
                                s_one, s_two = score.split('-')
                                final_user_score, final_opponent_score = int(s_one), int(s_two)
                            else :
                                winner, score_difference = match_sim(opponent_rating, user_rating, next_opponent, team)
                                score, opponent_scorers, user_scorers = randomize_goals(opponent_players, user_players, opponent_lineup, user_lineup, next_opponent, team, opponent_formation, user_formation, winner, score_difference)
                                s_one, s_two = score.split('-')
                                final_opponent_score, final_user_score = int(s_one), int(s_two)
                                                            
                            print(winner, score_difference)
                            print(score, user_scorers, opponent_scorers)
                                
                            
                            current_user_score, opponent_score = 0, 0
                            current_minute = 1
                            current_minute_count = 0
                            current_minute_max_count = 100
                            user_score_minutes, opponent_score_minutes = [], []
                            for i in range(final_user_score) :
                                user_score_minutes.append(random.randint(1, 90))
                            for i in range(final_opponent_score) :
                                opponent_score_minutes.append(random.randint(1, 90))

                            print(user_score_minutes, opponent_score_minutes)

                            
                            #quit()
                        else :
                            if not simming :
                                simming = True
                                button_index += 1
                            else :
                                simming = False
                                button_index -= 1
                                simming_count = 0
            display.blit(red_cover, coords_of_days[str(day)])
            over_sim_button = display_button(calendar_buttons[button_index], (x, y))
            if simming :
                simming_count += 1
                if simming_count == 700 :
                    current_date, next_month = advance_one_day(current_date)
                    month, day, year = unpack_date(current_date)
                    without_year = ' '.join([month, str(day)])
                    if next_month :
                        month_number = get_month_number(month)
                        current_calendar_screen = calendar_screens[month_number]
                        dates_of_games_in_month = get_games_in_a_month(month, schedule_dict, team)
                    try :
                        next_opponent, next_stadium, next_left_or_right = dates_of_games_in_month[without_year]
                        
                        stopped_on_matchday = True

                        simming = False
                        button_index = 2
                        simming_count = 0
                    except :
                        pass
                    simming_count = 0
        pygame.display.update()
    while saves_menu :
        display.fill(white)
        display.blit(current_save_image, (0, 0))
        display.set_at(current_clicked, red)
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                coords = pygame.mouse.get_pos()
                if clicker_mode :
                    current_clicked = coords
                save_selected = save_number
                print(save_selected)
                saves_menu = False
                name_save = True
                
        
        for i, save_name_text in enumerate(save_names_texts) :
            text_y = buttons[i][0]+offset[i]
            display.blit(save_name_text, (100, text_y))
            
        if x >= x_start and x <= x_end :
            for i, button in enumerate(buttons) :
                if y >= button[0] and y <= button[1] :
                    save_number = i
                    current_save_image = save_background_images[save_number]
        pygame.display.update()
        
        
    while name_save :
        display.fill(white)
        display.blit(current_typed_screen, (0, 0))
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                coords = pygame.mouse.get_pos()
                if over_submit :
                    if entering_save :
                        new_save_name = current_typed
                        current_typed = ""
                        current_typed_text = myfont2.render(current_typed, True, light_blue)
                        current_typed_x = get_x_value(current_typed_text.get_width())
                        current_typed_screen = default_typed_screen

                        space_bar_down = False

                        enter_extension_string = "your Manager"
                        string2 = "manager"

                        name_save_header = myfont2.render("Enter a Name for "+enter_extension_string, True, light_blue)
                        name_save_header_x = get_x_value(name_save_header.get_width())

                        too_many_chars = False

                        enter_or_submit = True
                        over_submit = False

                        entering_save = False
                    else :
                        new_manager_name = current_typed
                        quit()
            if event.type == pygame.KEYDOWN :
                try :
                    key = event.key
                    if key == pygame.K_SPACE :
                        if len(current_typed) < 20 :
                            space_bar_down = True
                            current_typed += ' '
                        else :
                            too_many_chars = True
                    elif key == pygame.K_BACKSPACE :
                        current_typed = current_typed[:-1]
                        current_typed_screen = keyboard_order[key]
                        too_many_chars = False
                    else :
                        if len(current_typed) < 20 :
                            current_typed_screen = keyboard_order[key]
                            current_typed += keyboard_letters[key]
                        else :
                            too_many_chars = True
                    current_typed_text = myfont2.render(current_typed, True, light_blue)
                    current_typed_x = get_x_value(current_typed_text.get_width())
                except :
                    pass
                if current_typed != '' and enter_or_submit :
                    name_save_header = myfont2.render("Click here to submit "+string2+" name", True, light_blue)
                    name_save_header_x = get_x_value(name_save_header.get_width())
                    enter_or_submit = False
                if current_typed == '' and not enter_or_submit :
                    name_save_header = myfont2.render("Enter a Name for "+enter_extension_string, True, light_blue)
                    name_save_header_x = get_x_value(name_save_header.get_width())
                    enter_or_submit = True
                    over_submit = False
            if event.type == pygame.KEYUP :
                if key == pygame.K_SPACE :
                    space_bar_down = False
                current_typed_screen = default_typed_screen
        
        if x >= 42 and x <= 745 and y >= 51 and y <= 109 and (not enter_or_submit) and (not over_submit) :
            over_submit = True
            name_save_header = myfont2.render("Click here to submit "+string2+" name", True, gray)
        if over_submit and not (x >= 42 and x <= 745 and y >= 51 and y <= 109) :
            over_submit = False
            name_save_header = myfont2.render("Click here to submit "+string2+" name", True, light_blue)
        if space_bar_down :
            pygame.draw.rect(display, key_color, pygame.Rect(240, 505, 315, 50))
        else :
            pygame.draw.rect(display, white, pygame.Rect(240, 505, 315, 50))
        if over_submit :
            pygame.draw.rect(display, light_blue, pygame.Rect(42, 51, 703, 58))
        else :
            pygame.draw.rect(display, gray, pygame.Rect(42, 51, 703, 58))
        display.blit(name_save_header, (name_save_header_x, 60))
        display.blit(current_typed_text, (current_typed_x, 160))
        if too_many_chars :
            display.blit(too_many_chars_text, (too_many_chars_x, 575))
        pygame.display.update()

