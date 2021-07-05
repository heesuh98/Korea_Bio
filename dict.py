#! /usr/bin/env python

d_dict = {
        'a_str' : 'Apple!',
        'b_list': [1,2,3,4],
        'c_tuple': ('a','b','c'),
        'e_dict': {1:'one', 2:'two'}
        }

print('d_dict:',d_dict)
print('d_dista:', d_dict['a_str'])

print('d_dist0:', d_dict['b_list'][0])
print('d_dist1:', d_dict['b_list'][1])
print('d_dist2:', d_dict['b_list'][2])
print('d_dist3:', d_dict['b_list'][3])
