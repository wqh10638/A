'''我的主页'''
import streamlit as st
from PIL import Image
import random
import time

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智能词典','我的留言区','我的编程工具','我的游戏区'])

def p1():
    '''我的兴趣推荐'''
    st.write('我的游戏推荐')
    with open('Trackformerz-Call Of The Ambulance.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format = 'mp3',start_time = 0)
    st.text('《暗区突围 》是由腾讯魔方工作室群开发的第一人称射击类手游。该游戏于2021年8月17日在进行了先锋测试，于2022年7月13日正式公测。游戏以从暗区撤离并收集物资满载而归作为最终目的，带出的战利品可以存储在仓中，又可以出售用以换取游戏金钱,可玩性极高')
    st.image("5dd4fd16-5405-4603-b33c-007675e8cf3b.jpg")
    st.write("----")
    st.text('《和平精英》是一款由腾讯光子工作室群自研打造的反恐军事竞赛体验手游。游戏中，玩家可以在不同的拟真场景里，通过完成搜集侦查、组队合作、战术分工、掩护救援等，在百人军事竞技中获得最后的胜利。游戏和平精英是一款射击类的游戏，在这款游戏当中可以体验杀敌人的快感，通过击杀敌人最后取得胜利，就可以得到很高的分数，得到的分数可以用来提升段位，分数越高段位越高，并且上升段位也会获得游戏当中相应的奖励，人物在到达战场以后是不携带任何东西的，需要在战场当中寻找并获取自己需要的物资，然后用自己获得的物资去攻击对方。')
    st.image("和平.png")
    st.image("和.jpg")

def p2():
    '''我的图片处理工具'''
    st.write(':radioactive_sign::warning:我的小程序:warning::radioactive_sign:')
    upf = st.file_uploader("上传图片",type=['png','jpeg','jpg','gif'])
    my_open = st.toggle('开关')
    if my_open:
        if upf:
            fn = upf.name
            ft = upf.type
            fs = upf.size
            img =Image.open(upf)
            tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["原","1","2","3","4","5"])
            with tab1:
                st.image(img)
            with tab2:
                st.image(icg(img,0,2,1))
            with tab3:
                st.image(icg(img,1,0,2))
            with tab4:
                st.image(icg(img,1,2,0))
            with tab5:
                st.image(icg(img,2,1,0))
            with tab6:
                st.image(icg(img,2,0,1))
    st.image("cs.jpg")
    st.write(":blue[https://www.67tool.com/images/convert/Ico]")
def p3():
    '''我的智能词典'''
    st.write('智能词典')
    with open('words_space.txt','r',encoding='utf-8') as f:
        wl = f.read().split('\n')
    for i in range(len(wl)):
        wl[i] = wl[i].split('#')
    wd = {}
    for i in wl:
        wd[i[1]] = [int(i[0]),i[2]]
    with open("check_out_times.txt",'r',encoding='utf-8') as f:
        tl = f.read().split('\n')
        for i in range(len(tl)):
            tl[i] = tl[i].split('#')
    td = {}
    for i in tl:
        td[int(i[0])] = int(i[1])
    w = st.text_input('查什么单词？')
    if w in wd:
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.02)
            roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
        st.write(wd[w])
        n = wd[w][0]
        if n in td:
            td[n] += 1
        else:
            td[n] = 1
        with open("check_out_times.txt",'w',encoding='utf-8') as f:
            m = ''
            for k,v in td.items():
                m += str(k) + '#' + str(v) + '\n'
            m = m[:-1]
            f.write(m)
        st.write('次数：',td[n])
        if w == 'python':
            st.code('''#恭喜你触发彩蛋，这是一行Python代码。print('Hello world')''')
        if w == 'Eric':
            st.code('''#恭喜你触发彩蛋，"作者的英文名字"''')
            st.balloons()
            st.snow()
            
def p4():
    '''我的留言区'''
    st.write('留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        ml = f.read().split('\n')
    for i in range(len(ml)):
        ml[i] = ml[i].split("#")
    for i in ml:
        if i[1] == '阿短':
            with st.chat_message('😀'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('😁'):
                st.write(i[1],':',i[2])
        elif i[1] == '小笛':
            with st.chat_message('😂'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……',['阿短','编程猫','小笛'])
    nn = st.text_input('想要说的话……')
    nnn = 5
    if st.button('留言'):
        ml.append([str(int(ml[-1][0])+1),name,nn])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            m = ''
            for i in ml:
                m += i[0] +'#' + i[1] + '#' + i[2] + '\n'
            m = m[:-1]
            f.write(m)


def p5():
    '''我的编程工具'''
    st.image("编程猫.jpg")
    st.write(':blue[https://shequ.codemao.cn/]')
def p6():
    '''我的游戏区'''
    st.write('视频软件')
    st.image("哔哩哔哩.jpg")
    st.write(':blue[https://www.bilibili.com/]')
    st.image("爱奇艺.jpg")
    st.write(':blue[https://www.iqiyi.com/]')
    st.image("优酷.jpg")
    st.write(':blue[https://www.youku.com/]')
    st.image("芒果TV.jpg")
    st.write(':blue[https://www.mgtv.com/]')
    st.write("----")
    st.write("----")
    st.write('游戏软件')
    st.image("4399.jpg")
    st.write(':blue[https://www.4399.com/]')
def icg(img,rc,gc,bc):
    w,h = img.size
    ia = img.load()
    for x in range(w):
        for y in range(h):
            r = ia[x,y][rc]
            g = ia[x,y][bc]
            b = ia[x,y][gc]
            ia[x,y] = (r,g,b)
    return img
if page == '我的兴趣推荐':
    p1()
elif page == '我的图片处理工具':
   p2() 
elif page == '我的智能词典':
   p3() 
elif page == '我的留言区':
   p4()
elif page == '我的编程工具':
   p5() 
elif page == '我的游戏区':
   p6()