import bs4 as bs
import urllib.request as req


def func(x):
  print(x)
  x=x.replace('game', 'scorecard')
  print(x)
  #http://www.espncricinfo.com/series/18074/game/1122727/india-vs-sri-lanka-2nd-odi-sl-in-india-2017-18
  sou = req.urlopen(x).read();

  soup = bs.BeautifulSoup(sou,"lxml");
  list_art = []
  for artical in soup.find_all('article',{"class" : "sub-module scorecard"}):
     list_art.append(artical)

 
  lim = len(list_art) 
  final_art = list_art [:lim]
  player_list = []
  commentary_list = []
  temp_list = []
  summ_list = []
  main_batting_list = []
  main_bowling_list = []
  for i in range(0,len(final_art)):
      for x in final_art[i].find_all("div",{"class" : "cell batsmen"}):
        player_list.append(x.text)
      for x in final_art[i].find_all("div",{"class" : "cell commentary"}):
        commentary_list.append(x.text)  
      for info in final_art[i].find_all("div",{"class" : "cell runs"}):
        temp_list.append(info.text)
      for info in final_art[i].find_all("div",{"class" : "cell"}):
        summ_list.append(info.text)    
    
      i_var = 6
      for f in range(1,len(player_list)):
         main_batting_list.append([player_list[f],commentary_list[f],temp_list[i_var:i_var+6]])
         i_var=i_var+6
    #print(main_batting_list)
      player_list.clear()
      commentary_list.clear()  
    
    
    
      table = final_art[i].find("table")
     
      table_rows = table.find_all("tr")
     
      for tr in table_rows:
           td = tr.find_all("td")
           row = [j.text for j in td]
           main_bowling_list.append(row)
         
   # print(main_bowling_list)  
      print("BATSMAN                                  R    M    B    4s    6s    SR")
      for j in range(0,len(main_batting_list)):
          print(str(main_batting_list[j][0]) + "    " +str(main_batting_list[j][1]) + "          ",end='')
          for k in main_batting_list[j][2]:
             print(str(k)+"    " ,end='')
          print("\n")
      last = len(summ_list)    
      print(str(summ_list[last-5]) + "                     ",end='')
      print(summ_list[last-4])
      print(str(summ_list[last-3]) + "                      ",end='')
      print(summ_list[last-2])
      print(summ_list[last-1])
   # print(summ_list[1])       
      print("\n\n\n\n\n")
      print("BOWLER                  O    M    R    R    W     ECON    WD    NB")
      for j in range(0,len(main_bowling_list)):
          for k in main_bowling_list[j]:
             print(str(k)+"    " ,end='')
          print("\n")
    
         
      main_batting_list.clear()
      main_bowling_list.clear()  
      summ_list.clear()
      print("\n\n\n\n\n\n\n\n")

     
  
  return

sou = req.urlopen("http://www.espncricinfo.com/ci/engine/match/index.html?view=live").read();

soup = bs.BeautifulSoup(sou,'lxml');

#print(soup.section.div);

#for an in soup.find_all('section'):
#    print(an.text)
#print (type(soup))

sec = soup.section;
list_div = []

for secc in sec.find_all('div'):
   list_div.append(secc.text)
 
 
newlist = list_div[4:]

#for x in newlist:
#   print(x)
x = len(newlist);
result = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

var = int(x/6)

z =0
for i in range(0,var):
   for j in range(0,6):
     if(z >=x):
       break
     result[i].append(newlist[z])
     if("Home" in newlist[z]): 
       z=z+1;
       break;
     z=z+1 

#for i in range(0,8):     
#   print(result[i])     
#   print("\n\n\n")

sec = soup.section;
final_link = []
for link in sec.find_all('span',{'class':'match-no'}):
   #list_link.append(link.get('href'))  
    final_link.append(link.a.get('href'))
#for i in  list_link:
#   print(i)
       

for i in range(0,var):
   print("Match id : " + str(i+1) + "\n\n")
   for j in range (0,len(result[i])):
     print(result[i][j])
   print("-------------------------------------------------------------------------------")  
   print("###############################################################################")
   print("-------------------------------------------------------------------------------")   
   
   
print("\n\n   The ID number of match whose scorebord u want to see    \n\n")
inp = int(input())
func(str(final_link[inp-1]))    
