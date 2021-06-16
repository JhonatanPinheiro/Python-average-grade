student_name = str(input('Inform the student\'s name: '))
note_1 = float(input('Inform the first note: '))
note_2 = float(input('Inform the second note: '))

weight_1 = 0.4
weight_2 = 0.6

note_1_weight = note_1 * weight_1
note_2_weight = note_2 * weight_2

print('\n')

print('First note with weight: {0}'.format(note_1_weight))
print('Second note with weight: {0}'.format(note_2_weight))

print('\n')

average = (note_1_weight + note_2_weight)

print('AVG is: {0}'.format(average))

