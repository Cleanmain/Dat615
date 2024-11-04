class EloPool:
  def __init__(self):
    self.players = {}
    self.unactivve_players = {}

  
  
  #Förstod inte riktigt hur jag skulle bestämma hur många poäng jag skulle dela ut
  def register_player(self,player_name): 
    if player_name in self.players:
      print("Spelare redan regristerad")
    else:
      print("det lyckades sätta in")
      self.players[player_name] = 1000
      
  def match_players(self,player1_name,player2_name,result):
    rating_player1 = self.players[player1_name]
    rating_player2 = self.players[player2_name]
    k = 40
    constant = 10 ** ((rating_player1 -rating_player2)/400)
    e = 1/(constant +1)
    if result == 1:
      winnerconstant = k *(result - e)
      print(winnerconstant)
      self.players[player1_name] = self.players[player1_name] + winnerconstant
      self.players[player2_name] = self.players[player2_name] - winnerconstant
    elif result == 0:
      loserconstant = k *(e-result)
      self.players[player1_name] = self.players[player1_name] - loserconstant
      self.players[player2_name] = self.players[player2_name] + loserconstant
    
    
    def retire_player(self,player_name):
      retireplayerelo = self.players[player_name]
      givepoints = retireplayerelo / (len(self.players)-1)
      for players in self.players:
        if player_name == player:
          self.players[player_name] = 0
        else:
          self.players[player] = self.players[player] + givepoints
          
    def print_points(self):
        list = {}


p = EloPool()
print(p.register_player("Johan"))
print(p.register_player("Johan"))
print(p.register_player("Filip"))
print(p.match_players("Johan","Filip",1))
print(p.players)