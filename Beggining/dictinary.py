dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"
tinydict = { 'name': 'afif', 'code': 86, 'dept': 'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

alien_0={'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])

my_points=alien_0['points']
print(f"You just earned {my_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0={}
alien_0['color']='blue'
alien_0['points']=20
print(alien_0)

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"original positionL:{alien_0['x_position']}")
if alien_0['speed']== 'slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print(f"new position :{ alien_0['x_position']}")

