def Rank_Sort(total_rank_Dict,country):
    counter=1
    for k,v in sorted(total_rank_Dict.items(), key=lambda p:p[1],reverse=True):
        if(k==country):
            print("World_Rank Of",k,":",counter)
            print("Rank_Value =",int(v))
        counter+=1


def Top(total_rank_Dict):
    counter=1
    for k,v in sorted(total_rank_Dict.items(), key=lambda p:p[1],reverse=True):
        print("World_Rank Of",k,":",counter)
        print("Rank_Value =",int(v))
        counter+=1
        if (counter==11):
            break






    