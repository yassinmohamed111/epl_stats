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

x = input("please enter season: ")
season = int(x)

        #switch season number to indexes of statarray[ season7 = index 0 , ...]
season = {
        7: 0,  8: 1,  9: 2,  10: 3,
        11: 4, 12: 5, 13: 6, 14: 7,
        15: 8, 16: 9, 17: 10
        }.get(season, -1)  

#this function takes season and team to calculate how many matches the team won
def calWins( teamm , s ):
         
        df_team_home = seasonarray[s][seasonarray[s]["home_team"] == teamm ]
        df_team_away = seasonarray[s][seasonarray[s]["away_team"] == teamm]
        df_count_home = df_team_home[df_team_home["result"] == "H"]
        df_count_away = df_team_away[df_team_away["result"]== "A"]
        home_wins = pd.value_counts(df_count_home["result"]).sum()
        away_wins = pd.value_counts(df_count_away["result"]).sum()
        win = home_wins + away_wins
        return win 

def getWins( SeasonNumber) :
        listTeam = []
        for i , row in statarray[SeasonNumber].iterrows() :
                wins = calWins(row["home_team"] , SeasonNumber)
                listTeam.append(wins) 

        return listTeam




#this function gets total goals
def calTotal( teamm , s ):
         
        df_team_home = seasonarray[s][seasonarray[s]["home_team"] == teamm ]
        df_team_away = seasonarray[s][seasonarray[s]["away_team"] == teamm]
        df_count_home = df_team_home[(df_team_home["result"] == "H") | (df_team_home["result"] == "A") | (df_team_home["result"] == "D") ]
        df_count_away = df_team_away[(df_team_away["result"] == "H") | (df_team_away["result"] == "A") | (df_team_away["result"] == "D") ]
        home_total = pd.value_counts(df_count_home["result"]).sum()
        away_total = pd.value_counts(df_count_away["result"]).sum()
        total = home_total + away_total
        return total 



def gettotal( SeasonNumber) :
        listTeam = []
        for i , row in statarray[SeasonNumber].iterrows() :
                wins = calTotal(row["home_team"] , SeasonNumber)
                listTeam.append(wins) 

        return listTeam



#calculate total draws
def calDraw( teamm , s ):
         
        df_team_home = seasonarray[s][seasonarray[s]["home_team"] == teamm ]
        df_team_away = seasonarray[s][seasonarray[s]["away_team"] == teamm]
        df_count_home = df_team_home[df_team_home["result"] == "D" ]
        df_count_away = df_team_away[ df_team_away["result"] == "D"]
        home_total = pd.value_counts(df_count_home["result"]).sum()
        away_total = pd.value_counts(df_count_away["result"]).sum()
        total = home_total + away_total
        return total 



def getDraw( SeasonNumber) :
        listTeam = []
        for i , row in statarray[SeasonNumber].iterrows() :
                wins = calDraw(row["home_team"] , SeasonNumber)
                listTeam.append(wins) 

        return listTeam







#get season

def Calcseason (seasonNumber) : 
  df_season = seasonarray[seasonNumber]["season"].head(21)
  return df_season
        



#here to save changes only on csv
def save() :
        #here to save a new stat it starts at season+ 7  = stat season 7 , ...(sorted)
        x = int(season) + 7 
        temp = statarray[season].sort_values(by='wins' , ascending=False)
        temp.to_csv(f"stat_{int(x)}.csv" , index= False)


#here to run the code just call run()
def run() :
        #here it takes the season number and convert it to intger 
       
        s = Calcseason(int(season))
        

        i = 6 #increamant in case we wanted to save a new stat
        #here we get the list of winnings of the specific season then add it to dataframe stat with new column ["wins"] then print the dataframe sorted and print the head == winner
        wins = getWins( int(season) )
        total  = gettotal(int(season))
        draw = getDraw(int(season))

        statarray[season]["total"] = total
        statarray[season]["wins"] = wins 
        statarray[season]["draws"] = draw
        statarray[season]['season']= s

        statarray[season]["losses"] =statarray[season]['total'] - (statarray[season]["wins"]  + statarray[season]["draws"] ) 
        statarray[season]["prop"] =statarray[season]['wins'] / statarray[season]["total"] 
        print(statarray[season].sort_values(by='wins' , ascending=False))
        temp = statarray[season].sort_values(by='wins' , ascending=False)
        print("##############################################")
        print( " the epl winner is " + temp["home_team"].head(1))
        print("##############################################")
       




#gets the winner of every season and save it in a csv ( dont run again)
def newWinnerAppend():
    
    

    temp = statarray[season].sort_values(by='wins', ascending=False).head(1)
    
    winner = pd.read_csv("winnersOFallseasons.csv")

    new_winner = pd.DataFrame({
        "winner": [temp["home_team"].values[0]],
        "wins": [temp["wins"].values[0]],
        "season": [temp["season"].values[0]]
    })

    winner = winner.append(new_winner, ignore_index=True)
    
    winner.to_csv("winnersOFallseasons.csv", index=False)






run()
#newWinnerAppend() #dont run again unless wanna save new season
#save() #dont run it unless u want to save a new season




  
        
    







