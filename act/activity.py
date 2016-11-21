# coding=utf-8
import sql


class activity:
    def __init__(self,act_id):
        self.act_id=act_id   # 活动id
        self.create_userid=''  # 活动创建人
        self.title=''   # 活动标题
        self.date=0   # 活动创建日期
        self.num=1   # 已参与人数
        self.id_list=[]  # 参与人id
        self.remark=''  # 活动备注


def create_act(userid,content):
    # 创建活动
    l=content.split()
    if len(l)!=2:
        return '你输入的信息格式有误！'
    else:
        title=l[0]
        remark=l[1]
        act_id= sql.get_max_actid() + 1
        act= activity.activity(act_id)
        act.title=title
        act.date=get_time()
        act.remark=remark
        # 插入表
        act.id_list.append(userid)
        act.create_userid=userid
        sql.insert_act(act)
        # 更新user表
        u= sql.select_user(userid)
        u.create_act_list.append(act_id)
        sql.update_user(u, flag=0)
        return str(act_id)


def show_act(act):
    msg='''活动标题：%s
创建人：%s
创建日期：%s
参与人数：%d
报名人:%s
'''%(act.title,act.create_userid,act.date,act.num,' '.join(act.id_list))
    return msg


def join_act(userid,act_id):
    act= sql.select_act(act_id)
    if act==None:
        return '没有此活动号,请确认活动号！'
    if userid in act.id_list:
        return '你已报名此活动！'
    act.id_list.append(userid)
    sql.update_act(act, id_list=True)
    u= sql.select_user(userid)
    u.join_act_list.append(act_id)
    sql.update_user(u, flag=1)
    return show_act(act)