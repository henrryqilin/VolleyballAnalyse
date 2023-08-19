import os

def create(Comand_Input,Configs):
    file=open(Comand_Input,'w',encoding='utf-8')
    return file

def tips(Info,Configs):
    in_chinese,in_english=[list(),list()]
    
    if Info['file_open'] ==True:
        in_chinese.append('正在打开文件:{0}\n使用/help指令获取帮助'.format(Info['file_name']))
        in_english.append('Opening file:{0}\nUse command \"/help\" to get helps.'.format(Info['file_name']))
    elif Info['file_open'] ==False:
        in_chinese.append('没有打开中的文件\n使用 /open 指令或 /create 指令打开文件')
        in_english.append('NO file opened\nUse command \"/open\" or \"/create\" to open files.')
    #输出
    print('#{:_^50}'.format('_'))
    if Configs['language'] == 'English':
        for i in in_english:
            print(i)
    elif Configs['language'] == 'Chinese':
        for i in in_chinese:
            print(i)

def master():
    information=dict()
    information['file_open']=False
    information['file_name']=None
    try:
        f=open('config.json','r',encoding='utf-8')
        config=eval(f.read())
        f.close()
    except:
        pass
    
    while True:
        tips(information,config)
        inputbox=input()
        # print('\n')
        inputbox=inputbox.split(' ')
        if '/' in inputbox[0]:
            if '/create' == inputbox[0]:
                try:
                    f.close()
                except NameError:
                    pass
                f=create(inputbox[1])
                information['file_open']=True
                information['file_name']=inputbox[1]
            elif '/help' == inputbox[0]:
                pass
            elif '/config_' in inputbox[0]:
                if '/config_save' == inputbox[0]:
                    pass
                elif '/config_load' == inputbox[0]:
                    pass
            elif '/bind' == inputbox[0]:
                pass
            elif '/unbind' == inputbox[0]:
                pass
            elif '/open' == inputbox[0]:
                information['file_open']=True
            elif '/close' == inputbox[0]:
                try:
                    f.close()
                except:
                    pass
                information['file_open']=False
                information['file_name']=None
            elif '/exit' == inputbox[0]:
                print('Are you sure to exit? press (y/n)\n\n是否确定退出 按(y/n)\n')
                if 'y' in input():
                    try:
                        f.close()
                    except NameError:
                        pass
                    break
        else:
            if len(inputbox) < 3 and 'n' in inputbox or 'l' in inputbox:
                pass
            else:
                pass

if __name__ == '__main__':
    master()
