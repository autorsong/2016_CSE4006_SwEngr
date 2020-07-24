# -*- coding: utf-8 -*-

import json
import itertools
import datetime

neighboring_nation = json.loads(open('neighboring_nation.json', 'r').read())
eurailpass_price = json.loads(open('eurailpass_price.json', 'r').read())

def make_eurailpass_set(plan_data):
    origin_price = 0
    temp_set = {}
    eurailpass_set = []

    for plan in plan_data:
        origin_price += plan['price']

    for day in eurailpass_price["global"]["youth"]["not_continuous"].keys():
        price = 0
        temp_set["date"] = int(day)
        temp_set["pass_price"] = eurailpass_price["global"]["youth"]["not_continuous"][day]['price'] * (100 - eurailpass_price["discounts"]) / 100
        temp_set["nations"] = []
        temp_set["pass_name"] = make_pass_name("global", "not_continuous", int(day))
        temp_set["pass_train"] = filter_global_not_continuous_gugan(plan_data, int(day), eurailpass_price["global"]["youth"]["not_continuous"][day]["valid_days"])
        temp_set["gugan_train"] = difference(plan_data, temp_set["pass_train"])
        for gugan in temp_set["gugan_train"]:
            price += gugan['price']
        temp_set["gugan_price"] = price
        temp_set["total_price"] = temp_set["gugan_price"] + temp_set["pass_price"]
        temp_set["save_price"] = origin_price - temp_set["total_price"]
        if temp_set["pass_train"] is not []:
            if temp_set["pass_price"] > origin_price:
                temp_set["pass_price"] = 0
                temp_set["total_price"] = temp_set["gugan_price"]
                temp_set["gugan_train"] = plan_data
                temp_set["pass_train"] = []
                temp_set["save_price"] = 0
            eurailpass_set.append(temp_set)
        temp_set = {}

    nations = set()

    for plan in plan_data:
        nations.add(plan['src_nation'])
        nations.add(plan['dst_nation'])

    nations_list = list(nations)
    nations_combi = []

    for i in range(2, len(nations_list)+1):
        nations_combi.append(itertools.combinations(nations_list, i))

    for day in eurailpass_price["select4"]["youth"]["H"].keys():
        price = 0
        nations = set()
        temp_set["date"] = int(day)
        temp_set["pass_price"] = eurailpass_price["select4"]["youth"]["H"][day] * (100 - eurailpass_price["discounts"]) / 100
        temp_set["pass_name"] = make_pass_name("select4", "not_continuous", int(day))
        temp_set["pass_train"] = filter_select4_gugan(plan_data, int(day), 60)
        temp_set["gugan_train"] = difference(plan_data, temp_set["pass_train"])
        for gugan in temp_set["gugan_train"]:
            price += gugan['price']
        for gugan in temp_set["pass_train"]:
            nations.add(gugan['src_nation'])
            nations.add(gugan['dst_nation'])
        temp_set["nations"] = list(nations)
        temp_set["gugan_price"] = price
        temp_set["total_price"] = temp_set["gugan_price"] + temp_set["pass_price"]
        temp_set["save_price"] = origin_price - temp_set["total_price"]
        if temp_set["pass_train"] is not []:
            if temp_set["pass_price"] > origin_price:
                temp_set["pass_price"] = 0
                temp_set["total_price"] = temp_set["gugan_price"]
                temp_set["gugan_train"] = plan_data
                temp_set["pass_train"] = []
                temp_set["save_price"] = 0
            eurailpass_set.append(temp_set)
        temp_set = {}

    for day in eurailpass_price["select3"]["youth"]["H"].keys():
        price = 0
        nations = set()
        temp_set["date"] = int(day)
        temp_set["pass_price"] = eurailpass_price["select3"]["youth"]["H"][day] * (100 - eurailpass_price["discounts"]) / 100
        temp_set["pass_name"] = make_pass_name("select3", "not_continuous", int(day))
        temp_set["pass_train"] = filter_select3_gugan(plan_data, int(day), 60)
        temp_set["gugan_train"] = difference(plan_data, temp_set["pass_train"])
        for gugan in temp_set["gugan_train"]:
            price += gugan['price']
        for gugan in temp_set["pass_train"]:
            nations.add(gugan['src_nation'])
            nations.add(gugan['dst_nation'])
        temp_set["nations"] = list(nations)
        temp_set["gugan_price"] = price
        temp_set["total_price"] = temp_set["gugan_price"] + temp_set["pass_price"]
        temp_set["save_price"] = origin_price - temp_set["total_price"]
        if temp_set["pass_train"] is not []:
            if temp_set["pass_price"] > origin_price:
                temp_set["pass_price"] = 0
                temp_set["total_price"] = temp_set["gugan_price"]
                temp_set["gugan_train"] = plan_data
                temp_set["pass_train"] = []
                temp_set["save_price"] = 0
            eurailpass_set.append(temp_set)
        temp_set = {}

    sorted_eurailpass_set = sorted(eurailpass_set, key=lambda k: k['total_price'])

    return sorted_eurailpass_set[0]


def filter_global_not_continuous_gugan(plan_data, day, valid_days):
    return_data = []
    sort_list = []
    iter_list = []
    temp_list = []
    temp_dict = {}
    price = 0

    if len(plan_data) >= day:
        for iteration in itertools.combinations(plan_data, day):
            iter_list.append(iteration)

        for i in range(len(iter_list)):
            for j in range(len(iter_list[i])):
                temp_list.append(iter_list[i][j])
                price += iter_list[i][j]['price']
            temp_dict['plan'] = temp_list
            temp_dict['tot_price'] = price
            sort_list.append(temp_dict)
            temp_list = []
            temp_dict = {}
            price = 0

        sorted_plan_data = sorted(sort_list, key=lambda k: k['tot_price'], reverse=True)

        for i in range(len(sorted_plan_data)):
            if calculate_date(sorted_plan_data[i]['plan']) < valid_days:
                return_data = sorted_plan_data[i]['plan']
                break

    return return_data


def filter_global_continuous_gugan(plan_data, day):
    sort_list = []
    iter_list = []
    temp_list = []
    temp_dict = {}
    price = 0
    if calculate_date(plan_data) >= day:
        for iteration in itertools.combinations(plan_data, day):
            iter_list.append(iteration)
        for i in range(len(iter_list)):
            for j in range(len(iter_list[i])):
                temp_list.append(iter_list[i][j])
                price += iter_list[i][j]['price']
            temp_dict['plan'] = temp_list
            temp_dict['tot_price'] = price
            sort_list.append(temp_dict)
            temp_list = []
            temp_dict = {}
            price = 0

        sorted_plan_data = sorted(sort_list, key=lambda k: k['tot_price'], reverse=True)
        return sorted_plan_data[0]['plan']

        for i in range(len(sorted_plan_data)):
            if calculate_date(sorted_plan_data[i]['plan']) < day:
                return sorted_plan_data[i]['plan']

    return []


def filter_select4_gugan(plan_data, day, valid_days):
    return_data = []
    sort_list = []
    iter_list = []
    temp_list = []
    temp_dict = {}
    price = 0
    temp_flag = False
    if len(plan_data) >= day:
        for iteration in itertools.combinations(plan_data, day):
            iter_list.append(iteration)
        for i in range(len(iter_list)):
            for j in range(len(iter_list[i])):
                temp_list.append(iter_list[i][j])
                price += iter_list[i][j]['price']
            temp_dict['plan'] = temp_list
            temp_dict['tot_price'] = price
            sort_list.append(temp_dict)
            temp_list = []
            temp_dict = {}
            price = 0

        sorted_plan_data = sorted(sort_list, key=lambda k: k['tot_price'], reverse=True)
        return sorted_plan_data[0]['plan']

        for i in range(len(sorted_plan_data)):
            if calculate_date(sorted_plan_data[i]['plan']) < valid_days:
                nations = set()
                for plan in sorted_plan_data[i]['plan']:
                    nations.add(plan['src_nation'])
                    nations.add(plan['dst_nation'])

                    if len(nations) <= 4:
                        if check_neighboring_nation(list(nations)):
                            return_data = sorted_plan_data[i]['plan']
                            temp_flag = True
                            break
                nations = set()
                if temp_flag == True:
                    break

    return return_data


def filter_select3_gugan(plan_data, day, valid_days):
    return_data = []
    sort_list = []
    iter_list = []
    temp_list = []
    temp_dict = {}
    price = 0
    temp_flag = False
    if len(plan_data) >= day:
        for iteration in itertools.combinations(plan_data, day):
            iter_list.append(iteration)
        for i in range(len(iter_list)):
            for j in range(len(iter_list[i])):
                temp_list.append(iter_list[i][j])
                price += iter_list[i][j]['price']
            temp_dict['plan'] = temp_list
            temp_dict['tot_price'] = price
            sort_list.append(temp_dict)
            temp_list = []
            temp_dict = {}
            price = 0

        sorted_plan_data = sorted(sort_list, key=lambda k: k['tot_price'], reverse=True)
        return sorted_plan_data[0]['plan']

        for i in len(sorted_plan_data):
            if calculate_date(sorted_plan_data[i]['plan']) < valid_days:
                nations = set()
                for plan in sorted_plan_data[i]['plan']:
                    nations.add(plan['src_nation'])
                    nations.add(plan['dst_nation'])
                    if len(nations) <= 3:
                        if check_neighboring_nation(list(nations)):
                            return_data = sorted_plan_data[i]['plan']
                            temp_flag = True
                            break
                nations = set()
                if temp_flag == True:
                    break

    return return_data


def make_pass_name(name, continuous, day):
    if(name == "global"):
        pass_name = "글로벌 패스 "
    elif(name == "select4"):
        pass_name = "4개국 셀렉트 패스 "
    elif(name == "select3"):
        pass_name = "3개국 셀렉트 패스 "
    else:
        pass_name = ""

    if(continuous == "continuous"):
        pass_name = pass_name + "연속사용 "
    elif(continuous == "not_continuous"):
        pass_name = pass_name + "선택사용 "

    pass_name = pass_name + str(day) + "일권"

    return unicode(pass_name, 'utf-8')


def calculate_price_level(nations_combi_list):
    return "H"


def difference(plan_data, another_data):
    temp_list = []
    in_flag = False
    if another_data is not []:
        for plan in plan_data:
            for another in another_data:
                if another['id'] == plan['id']:
                    in_flag = True
            if in_flag is False:
                temp_list.append(plan)
            in_flag = False

    return temp_list


def calculate_date(plan_data):
    start_date = datetime.date(plan_data[0]['year'], plan_data[0]['month'], plan_data[0]['day'])
    end_date = datetime.date(plan_data[0]['year'], plan_data[0]['month'], plan_data[0]['day'])

    for plan in plan_data:
        now_date = datetime.date(plan['year'], plan['month'], plan['day'])

        if(start_date > now_date):
            start_date = now_date

        if(end_date < now_date):
            end_date = now_date

    return (end_date - start_date).days


def check_neighboring_nation(nations_list):
    for nation in nations_list:
        nations_flag = True
        if(len(nations.difference(set(neighboring_nation[nation]))) is not 0):
            nations_flag = False
            break

    return nations_flag
