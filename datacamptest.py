import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


#all seasons of epl in one csv
results = pd.read_csv("results1.csv")

#preprocessing the results1.csv (splitting it to 11 seasons and remove duplicate team names then save stat of each season teams on it's own csv)

'''
#for loops used in the code
for i in range(13):
    team_number = 6 + i
    formatted_number = str(team_number).zfill(2)  # Add leading zeros
    print( f"x{formatted_number}= []")
    print(f'for i , row in stat{formatted_number}.iterrows() :')
    print(f'wins = team(row["home_team"])')
    print(f'x{formatted_number}.append(wins)')   
    print(f'stat{formatted_number}["wins"] = x{formatted_number} ')
    print(f'stat{formatted_number}.to_csv("stat{formatted_number}.csv" , index = False)')



    for i in range (13) :
     team_number = 6 + i
     formatted_number = str(team_number).zfill(2) 
     print(f"team{formatted_number}.to_csv('stat_{formatted_number}.csv' , index = False)")

     for i in range(13):
    team_number = 6 + i
    formatted_number = str(team_number).zfill(2)  # Add leading zeros
    print(f"team{formatted_number} = team{formatted_number}['home_team'].drop_duplicates")

    for i in range(13):
    team_number = 6 + i
    formatted_number = str(team_number).zfill(2)  # Add leading zeros
    print(f"team{formatted_number} = pd.read_csv('season_{formatted_number}.csv')")

f
#splitting them to 11 seasons
season_07 = results[results["season"] == "2006-2007"]
season_08 = results[results["season"] == "2007-2008"]
season_09 = results[results["season"] == "2008-2009"]
season_10 = results[results["season"] == "2009-2010"]
season_11=  results[results["season"]== "2010-2011"]
season_12 = results[results["season"] == "2011-2012"]
season_13 = results[results["season"] == "2012-2013"]
season_14 = results[results["season"] == "2013-2014"]
season_15 = results[results["season"] == "2014-2015"]
season_16 = results[results["season"] == "2015-2016"]
season_17 = results[results["season"] == "2016-2017"]

season_07.to_csv("season_07.csv" , index=False)
season_08.to_csv("season_08.csv" , index=False) 
season_09.to_csv("season_09.csv" , index=False) 
season_10.to_csv("season_10.csv" , index=False) 
season_11.to_csv("season_11.csv" , index=False)
season_12.to_csv("season_12.csv" , index=False) 
season_13.to_csv("season_13.csv" , index=False)
season_14.to_csv("season_14.csv" , index=False)
season_15.to_csv("season_15.csv" , index=False) 
season_16.to_csv("season_16.csv" , index=False) 
season_17.to_csv("season_17.csv" , index=False) 

#teams dataframes
team07 = pd.read_csv('season_07.csv')
team08 = pd.read_csv('season_08.csv')
team09 = pd.read_csv('season_09.csv')
team10 = pd.read_csv('season_10.csv')
team11 = pd.read_csv('season_11.csv')
team12 = pd.read_csv('season_12.csv')
team13 = pd.read_csv('season_13.csv')
team14 = pd.read_csv('season_14.csv')
team15 = pd.read_csv('season_15.csv')
team16 = pd.read_csv('season_16.csv')
team17 = pd.read_csv('season_17.csv')

#dropping duplicates only teams
team07 = team07['home_team'].drop_duplicates()
team08 = team08['home_team'].drop_duplicates()
team09 = team09['home_team'].drop_duplicates()
team10 = team10['home_team'].drop_duplicates()
team11 = team11['home_team'].drop_duplicates()
team12 = team12['home_team'].drop_duplicates()
team13 = team13['home_team'].drop_duplicates()
team14 = team14['home_team'].drop_duplicates()
team15 = team15['home_team'].drop_duplicates()
team16 = team16['home_team'].drop_duplicates()
team17 = team17['home_team'].drop_duplicates()

#saving every stat on its own
team07.to_csv('stat_07.csv' , index = False)
team08.to_csv('stat_08.csv' , index = False)
team09.to_csv('stat_09.csv' , index = False)
team10.to_csv('stat_10.csv' , index = False)
team11.to_csv('stat_11.csv' , index = False)
team12.to_csv('stat_12.csv' , index = False)
team13.to_csv('stat_13.csv' , index = False)
team14.to_csv('stat_14.csv' , index = False)
team15.to_csv('stat_15.csv' , index = False)
team16.to_csv('stat_16.csv' , index = False)
team17.to_csv('stat_17.csv' , index = False)

'''

#(((the upper part is for preprocessing dont remove comments)))



#made stat for every season and read it 
stat07 = pd.read_csv('stat_07.csv')
stat08 = pd.read_csv('stat_08.csv')
stat09 = pd.read_csv('stat_09.csv')
stat10 = pd.read_csv('stat_10.csv')
stat11 = pd.read_csv('stat_11.csv')
stat12 = pd.read_csv('stat_12.csv')
stat13 = pd.read_csv('stat_13.csv')
stat14 = pd.read_csv('stat_14.csv')
stat15 = pd.read_csv('stat_15.csv')
stat16 = pd.read_csv('stat_16.csv')
stat17 = pd.read_csv('stat_17.csv')

season07 = pd.read_csv('season_07.csv')
season08 = pd.read_csv('season_08.csv')
season09 = pd.read_csv('season_09.csv')
season10 = pd.read_csv('season_10.csv')
season11 = pd.read_csv('season_11.csv')
season12 = pd.read_csv('season_12.csv')
season13 = pd.read_csv('season_13.csv')
season14 = pd.read_csv('season_14.csv')
season15 = pd.read_csv('season_15.csv')
season16 = pd.read_csv('season_16.csv')
season17 = pd.read_csv('season_17.csv')





#made array of the stat and season to easy access them dynamically
statarray = [stat07 , stat08 , stat09, stat10 , stat11 , stat12 , stat13 , stat14 , stat15 , stat16 , stat17 ]
seasonarray = [season07 , season08 , season09 , season10 , season11 , season12 , season13 , season14 , season15 , season16 , season17 ]

#here get the input season from the user

def inputt() :
        x = input("please enter season: ")
        seasonNumber = int(x)

                #switch season number to indexes of statarray[ season7 = index 0 , ...]
        seasonNumber = {
                7: 0,  8: 1,  9: 2,  10: 3,
                11: 4, 12: 5, 13: 6, 14: 7,
                15: 8, 16: 9, 17: 10
                }.get(seasonNumber, -1)
        
        return seasonNumber
                


SeasonNumber= None #inputt() #if gonna run the func Run() call func inputt()
seasonNumber = SeasonNumber

#############################################################################################################################

#cal wins of each team in each season
def calWins( teamm , s ):
         
        df_team_home = seasonarray[s][seasonarray[s]["home_team"] == teamm ]
        df_team_away = seasonarray[s][seasonarray[s]["away_team"] == teamm]
        df_count_home = df_team_home[df_team_home["result"] == "H"]
        df_count_away = df_team_away[df_team_away["result"]== "A"]
        home_wins = pd.value_counts(df_count_home["result"]).sum()
        away_wins = pd.value_counts(df_count_away["result"]).sum()
        win = home_wins + away_wins
        return win 
#return list of wins of teams in everyseason
def getWins( SeasonNumber) :
        listTeam = []
        for i , row in statarray[SeasonNumber].iterrows() :
                wins = calWins(row["home_team"] , SeasonNumber)
                listTeam.append(wins) 

        return listTeam


#############################################################################################################################

#cal total matches of each team in every season
def cal_total_matches( teamm , s ):
         
        df_team_home = seasonarray[s][seasonarray[s]["home_team"] == teamm ]
        df_team_away = seasonarray[s][seasonarray[s]["away_team"] == teamm]
        df_count_home = df_team_home[(df_team_home["result"] == "H") | (df_team_home["result"] == "A") | (df_team_home["result"] == "D") ]
        df_count_away = df_team_away[(df_team_away["result"] == "H") | (df_team_away["result"] == "A") | (df_team_away["result"] == "D") ]
        home_total = pd.value_counts(df_count_home["result"]).sum()
        away_total = pd.value_counts(df_count_away["result"]).sum()
        total = home_total + away_total
        return total 


#return list of matches played
def get_total_goals( SeasonNumber) :
        listTeam = []
        for i , row in statarray[SeasonNumber].iterrows() :
                total_matches = cal_total_matches(row["home_team"] , SeasonNumber)
                listTeam.append(total_matches) 

        return listTeam



#############################################################################################################################

#calculate total draws of each team in every season
def calDraw( teamm , s ):
         
        df_team_home = seasonarray[s][seasonarray[s]["home_team"] == teamm ]
        df_team_away = seasonarray[s][seasonarray[s]["away_team"] == teamm]
        df_count_home = df_team_home[df_team_home["result"] == "D" ]
        df_count_away = df_team_away[ df_team_away["result"] == "D"]
        home_total = pd.value_counts(df_count_home["result"]).sum()
        away_total = pd.value_counts(df_count_away["result"]).sum()
        total = home_total + away_total
        return total 


#gets list of draws
def getDraw( SeasonNumber) :
        listTeam = []
        for i , row in statarray[SeasonNumber].iterrows() :
                draws = calDraw(row["home_team"] , SeasonNumber)
                listTeam.append(draws) 

        return listTeam
#############################################################################################################################
#gets total nummber of goals for each team in each season
def teamGoals( teamm , s) :
        df_team_home = seasonarray[s][seasonarray[s]["home_team"] == teamm ]
        df_team_away = seasonarray[s][seasonarray[s]["away_team"] == teamm]
        away_goals= df_team_away["away_goals"].sum()
        home_goals = df_team_home["home_goals"].sum()
        total = away_goals + home_goals
        return total 

#return list of goals
def getgoals( SeasonNumber) :
        listTeam = []
        for i , row in statarray[SeasonNumber].iterrows() :
                goals = teamGoals(row["home_team"] , SeasonNumber)
                listTeam.append(goals) 

        return listTeam
#############################################################################################################################

#gets against team goals
def teamGAganistoals( teamm , s) :
        df_team_home = seasonarray[s][seasonarray[s]["home_team"] == teamm ]
        df_team_away = seasonarray[s][seasonarray[s]["away_team"] == teamm]
        away_goals= df_team_away["home_goals"].sum()
        home_goals = df_team_home["away_goals"].sum()
        total = away_goals + home_goals
        return total
       


#return list of against goals
def getAgainstgoals( SeasonNumber) :
        listTeam = []
        for i , row in statarray[SeasonNumber].iterrows() :
                against = teamGAganistoals(row["home_team"] , SeasonNumber)
                listTeam.append(against) 

        return listTeam


#############################################################################################################################
#gets the clean sheet of every teams in every season
def cleansheet( teamm , s) :
        
        clean = 0.0
        df_team_home = seasonarray[s][seasonarray[s]["home_team"] == teamm]
        df_team_away = seasonarray[s][seasonarray[s]["away_team"] == teamm]
        away_clean = (df_team_away["home_goals"] == clean).sum()
        home_clean = (df_team_home["away_goals"] == clean).sum()
        total = away_clean + home_clean
        return total

       

#return list of cleansheets
def getCleansheet( SeasonNumber) :
        listTeam = []
        for i , row in statarray[SeasonNumber].iterrows() :
                cleans = cleansheet(row["home_team"] , SeasonNumber)
                listTeam.append(cleans) 

        return listTeam



#############################################################################################################################
#calc season
def Calcseason (seasonNumber) : 
  df_season = seasonarray[seasonNumber]["season"].head(21)
  return df_season
        
#############################################################################################################################
#calc how many goals entered in each season
def seasonGoals (s) :
      x =  seasonarray[s]["total_goals"].sum()
      print(x)


#############################################################################################################################
#just for run
def enterTeam() :
        x=  input('please enter team :')   
        return x

def home() :
       home = input("please enter home_team :")
       return home

def away() :
       away = input("please enter away_team :")
       return away

def search( team , season) :
      
       teamstat = statarray[season][statarray[season]["home_team"] == team]
       print(teamstat)

def searchMatch(s, home , away) :
       
       match = seasonarray[s].set_index(['home_team' , 'away_team'])
       print("///////////////////////////////////////////////////////////////////////////////////////////////////")
       print(F"///////////////////////////////////Stat of the match between {home} VS. {away} ////////////////")
       print("")
       print(match.loc[[(home , away)]])
       print("")
       print("///////////////////////////////////////////////////////////////////////////////////////////////////")
       print(F"///////////////////////////////////Stat of {home} this season //////////////////////////////////")
       print("")
       home_team= statarray[s][statarray[s]["home_team"] == home]
       print(home_team)
       print("")
       print("///////////////////////////////////////////////////////////////////////////////////////////////////")
       
       print(f"///////////////////////////////////Stat of {away} this season///////////////////////////////////")
       print("")
       away_team = statarray[s][statarray[s]["home_team"] == away]
       print(away_team)
       print("")
       print("///////////////////////////////////////////////////////////////////////////////////////////////////")






#############################################################################################################################




#################################################################################
###############functions of runs################################################
###############################################################################
#here to save changes only on csv
def save() :
        #here to save a new stat it starts at season+ 7  = stat season 7 , ...(sorted)
        x = int(seasonNumber) + 7 
        temp = statarray[seasonNumber].sort_values(by='wins' , ascending=False)
        temp.to_csv(f"stat_{int(x)}.csv" , index= False)



def runsearch() :
       
       x = enterTeam()
       search(x , seasonNumber)


def runSearchMatch() :
       h = home()
       a = away()
       searchMatch(seasonNumber , h , a)    

#here to run the code just call run()
def run() :





        #here it takes the season number and convert it to intger 
       
        s = Calcseason(int(seasonNumber))
        

        i = 6 #increamant in case we wanted to save a new stat
        #here we get the list of winnings of the specific season then add it to dataframe stat with new column ["wins"] then print the dataframe sorted and print the head == winner
        wins = getWins( int(seasonNumber) )
        total  = get_total_goals(int(seasonNumber))
        draw = getDraw(int(seasonNumber))
        goals = getgoals(int(seasonNumber))
        against = getAgainstgoals(int(seasonNumber))
        cleansheets = getCleansheet(int(seasonNumber))

        statarray[seasonNumber]["total"] = total
        statarray[seasonNumber]["wins"] = wins 
        statarray[seasonNumber]["draws"] = draw
        statarray[seasonNumber]['season']= s
        statarray[seasonNumber]["goals"] = goals
        statarray[seasonNumber]["goals_per_game"] = statarray[seasonNumber]["goals"] / statarray[seasonNumber]["total"]
        statarray[seasonNumber]["Goals_Against"] = against
        statarray[seasonNumber]["cleansheets"]= cleansheets
        statarray[seasonNumber]["cleansheets_prop"]= statarray[seasonNumber]["cleansheets"] / statarray[seasonNumber]["total"]

        statarray[seasonNumber]["losses"] =statarray[seasonNumber]['total'] - (statarray[seasonNumber]["wins"]  + statarray[seasonNumber]["draws"] ) 
        statarray[seasonNumber]["prop"] =statarray[seasonNumber]['wins'] / statarray[seasonNumber]["total"] 
        print(statarray[seasonNumber].sort_values(by='wins' , ascending=False))
        temp = statarray[seasonNumber].sort_values(by='wins' , ascending=False)
        print("##############################################")
        print( " the epl winner is " + temp["home_team"].head(1))
        print("##############################################")
       




#gets the winner of every season and save it in a csv ( dont run again)
def newWinnerAppend():
    temp = statarray[seasonNumber].sort_values(by='wins', ascending=False).head(1)
    
    winner = pd.read_csv("winnersOFallseasons.csv")

    new_winner = pd.DataFrame({
        "winner": [temp["home_team"].values[0]],
        "wins": [temp["wins"].values[0]],
        "season": [temp["season"].values[0]],
         "goals": [temp["goals"].values[0]]
    })
    winner = winner.append(new_winner, ignore_index=True)
    winner.to_csv("winnersOFallseasons.csv", index=False)

 
#################################################################################
###############running section  ################################################
###############################################################################

#runsearch() #takes season and team as input to output stat of team in a specific season
#seasonGoals(seasonNumber) #takes season number as input and output total goals of this season
#run() #takes season as input and output season stats
#save() #to save a new season stat (dont run)
#newWinnerAppend() append new seaosn winner ( dont run)
#run()


#run()
#runsearch()
#runSearchMatch()




#***************************************************************************************************************************************
#***************************************************************************************************************************************
#                        all seasons in one stat called all_stat.csv from 2006/2007 to 2017/2018
#***************************************************************************************************************************************
#***************************************************************************************************************************************



allstat = pd.read_csv("all_stat.csv")

def cal_total_matchesall( teamm  ):
         
        df_team_home = results[results["home_team"] == teamm ]
        df_team_away = results[results["away_team"] == teamm]
        df_count_home = df_team_home[(df_team_home["result"] == "H") | (df_team_home["result"] == "A") | (df_team_home["result"] == "D") ]
        df_count_away = df_team_away[(df_team_away["result"] == "H") | (df_team_away["result"] == "A") | (df_team_away["result"] == "D") ]
        home_total = pd.value_counts(df_count_home["result"]).sum()
        away_total = pd.value_counts(df_count_away["result"]).sum()
        total = home_total + away_total
        return total 


#return list of matches played
def get_total_matchesall( ) :
        listTeam = []
        for i , row in allstat.iterrows() :
                total_matches = cal_total_matchesall(row["home_team"] )
                listTeam.append(total_matches) 

        return listTeam


#cal wins of each team in each season
def calWinsall( teamm  ):
         
        df_team_home = results[results["home_team"] == teamm ]
        df_team_away = results[results["away_team"] == teamm]
        df_count_home = df_team_home[df_team_home["result"] == "H"]
        df_count_away = df_team_away[df_team_away["result"]== "A"]
        home_wins = pd.value_counts(df_count_home["result"]).sum()
        away_wins = pd.value_counts(df_count_away["result"]).sum()
        win = home_wins + away_wins
        return win 
#return list of wins of teams in everyseason
def getWinsall( ) :
        listTeam = []
        for i , row in allstat.iterrows() :
                wins = calWinsall(row["home_team"] )
                listTeam.append(wins) 

        return listTeam


#calculate total draws of each team in every season
def calDrawall( teamm ):
         
        df_team_home = results[results["home_team"] == teamm ]
        df_team_away = results[results["away_team"] == teamm]
        df_count_home = df_team_home[df_team_home["result"] == "D" ]
        df_count_away = df_team_away[ df_team_away["result"] == "D"]
        home_total = pd.value_counts(df_count_home["result"]).sum()
        away_total = pd.value_counts(df_count_away["result"]).sum()
        total = home_total + away_total
        return total 


#gets list of draws
def getDrawall( ) :
        listTeam = []
        for i , row in allstat.iterrows() :
                draws = calDrawall(row["home_team"] )
                listTeam.append(draws) 

        return listTeam



def teamGoalsall( teamm ) :
        df_team_home = results[results["home_team"] == teamm ]
        df_team_away = results[results["away_team"] == teamm]
        away_goals= df_team_away["away_goals"].sum()
        home_goals = df_team_home["home_goals"].sum()
        total = away_goals + home_goals
        return total 

#return list of goals
def getgoalsall( ) :
        listTeam = []
        for i , row in allstat.iterrows() :
                goals = teamGoalsall(row["home_team"] )
                listTeam.append(goals) 

        return listTeam


#gets against team goals
def teamGAganistoalsall( teamm ) :
        df_team_home = results[results["home_team"] == teamm ]
        df_team_away = results[results["away_team"] == teamm]
        away_goals= df_team_away["home_goals"].sum()
        home_goals = df_team_home["away_goals"].sum()
        total = away_goals + home_goals
        return total
       


#return list of against goals
def getAgainstgoalsall( ) :
        listTeam = []
        for i , row in allstat.iterrows() :
                against = teamGAganistoalsall(row["home_team"])
                listTeam.append(against) 

        return listTeam

def cleansheetall( teamm ) :
        
        clean = 0.0
        df_team_home = results[results["home_team"] == teamm]
        df_team_away = results[results["away_team"] == teamm]
        away_clean = (df_team_away["home_goals"] == clean).sum()
        home_clean = (df_team_home["away_goals"] == clean).sum()
        total = away_clean + home_clean
        return total

       

#return list of cleansheets
def getCleansheetall( ) :
        listTeam = []
        for i , row in allstat.iterrows() :
                cleans = cleansheetall(row["home_team"] )
                listTeam.append(cleans) 

        return listTeam

def run_all() :
        total = get_total_matchesall()
        wins = getWinsall()
        draw = getDrawall()
        goals = getgoalsall()
        clean = getCleansheetall()
        against = getAgainstgoalsall()
        allstat["total"] = total
        allstat["wins"] = wins
        allstat["draws"] = draw
        allstat["lossess"] = allstat["total"] - (allstat["wins"] + allstat["draws"])
        allstat["total_goals"] = goals
        allstat["against_goals"] = against
        allstat["cleansheets"] = clean
        x = allstat["total_goals"] / allstat["total"]
        allstat["goals_per_game"] = x
        y = allstat["against_goals"] / allstat["total"]
        allstat["against_goals_per_game"] = y
        allstat["cleansheets_prop"] = allstat["cleansheets"] / allstat["total"]
        w = allstat["wins"] / allstat["total"]
        prop = (w * 100 )

        allstat["win_prop"] = prop
        print(allstat)


def save_all() : 
        temp_stat = allstat.sort_values(by="wins" , ascending=False , inplace=True)
        allstat.to_csv("all_stat.csv" , index=False)




#***************************************************************************************************************************************
#***************************************************************************************************************************************
#                        visualizations
#***************************************************************************************************************************************
#***************************************************************************************************************************************



import matplotlib.pyplot as plt 



def inputteam(num):
        team = []
        for i in range (num) :
                x= input(f"team{i+1} :") 
                team.append(x)

        return team


# Plotting
def winsplot(num) :
        teams = inputteam(num)
        allstatINdexed = allstat.set_index("home_team")
        wins = allstatINdexed.loc[teams]
        plt.bar(wins.index , wins["wins"])
       
        plt.title(f"number of wins of these {num}each team")
        plt.show()


def winprop(num) :
        teams = inputteam(num)
        allstatIndexed = allstat.set_index("home_team")
        prop = allstatIndexed.loc[teams]
        plt.bar(prop.index , prop["win_prop"])
        plt.title(f"win prop of these {num} each teams")
        plt.show()




def goalsPiechart(num):
    teams = inputteam(num)
    allstatindexed = allstat.set_index("home_team")
    goalss = allstatindexed.loc[teams]
    pie = goalss["total_goals"] / allstatindexed["total_goals"].sum()
    labels = teams
    plt.pie(pie, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.legend(labels, loc="best")
    plt.axis('equal')  
    plt.show()



def winsPiechart(num):
        teams = inputteam(num)
        allstatindexed = allstat.set_index("home_team")
        wins = allstatindexed.loc[teams]
        pie = wins["wins"] / allstatindexed["wins"].sum()
        plt.pie(pie , labels = teams , autopct='%1.1f%%' , startangle=140)
        plt.title(f"winning propotion of these {num} teams")
        #plt.legend(teams , loc = "best")
        plt.axis = "equal"
        plt.show()

#winsplot() #add number of teams you want to add
#winprop(7) #add number of teams you want to add
#winsPiechart(7)
#goalsPiechart(6) #add number of teams you want to add
