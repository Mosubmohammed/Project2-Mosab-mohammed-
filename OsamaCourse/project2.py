from datetime import datetime



class SportClub:
    def __init__(self,name,number_of_medals,budget,location,number_of_wins,founded_year,costume_color):
        self.name = name
        self.number_of_medals = number_of_medals
        self._budget = budget
        self.location = location
        self.number_of_wins = number_of_wins
        self.founded_year =founded_year
        self.costume_color = costume_color
        
    def cal_tax_due(self):
        tax_due = 0.2 * self._budget + (self.number_of_wins * 0.1) + (self.number_of_medals * 0.1)
        return tax_due

    def cal_age(self):
        curr_year = datetime.now().year
        return curr_year - self.founded_year
    
    
    def get_budget(self):
        return self._budget
    
    def set_budget(self,val):
        if val>=0:
            self._budget=val
        else:
            print("Budget cannot be negative")
    def __str__(self):
        return f"{self.name} Club - Medals: {self.number_of_medals}, Budget: {self._budget}"
    
    def __gt__(self, other):
        return self.number_of_medals > other.number_of_medals

    def __lt__(self, other):
        return self.number_of_medals < other.number_of_medals

    def __eq__(self, other):
        return self.number_of_medals == other.number_of_medals
        
    
    
    


class player(SportClub):
    def __init__(self, player_name, number, position, goals, assists, matches, **kwargs):
        super().__init__(**kwargs)
        self.player_name = player_name
        self.number = number
        self.position = position
        self.goals = goals
        self.assists = assists
        self.matches = matches
        
    
    def cal_performance(self):
        performance_score = (self.goals * 0.7) + (self.assists * 0.15) + (self.matches * 0.15)
        return performance_score
    def __str__(self):
        return f"{self.name} - Goals: {self.goals}, Assists: {self.assists}, Matches: {self.matches}"
        
        
        


class Coach(SportClub):
    def __init__(self, coach_name, experience_level, training_certificates, **kwargs):
        super().__init__(**kwargs)
        self.coach_name = coach_name
        self.experience_level = experience_level
        self.training_certificates = training_certificates
        
    def calculate_efficiency(self):
        efficiency_score = (self.experience_level * 0.5) + (self.training_certificates * 0.2) + (self.number_of_medals * 0.3)
        return efficiency_score
    
    def __str__(self):
        return f"{self.coach_name} - Experience Level: {self.experience_level}, Training Certificates: {self.training_certificates}"


club1 = SportClub(name="Falcons", number_of_medals=10, budget=50000, location="CityA", number_of_wins=20, founded_year=1990, costume_color="Blue")
club2 = SportClub(name="Eagles", number_of_medals=15, budget=60000, location="CityB", number_of_wins=25, founded_year=1985, costume_color="Red")

player1 = player(player_name="John Doe", number=9, position="Forward", goals=30, assists=10, matches=25, 
                 name="Falcons", number_of_medals=10, budget=50000, location="CityA", number_of_wins=20, founded_year=1990, costume_color="Blue")

coach1 = Coach(coach_name="Coach Smith", experience_level=10, training_certificates=5, 
               name="Falcons", number_of_medals=10, budget=50000, location="CityA", number_of_wins=20, founded_year=1990, costume_color="Blue")





print(club1)
print("Club Tax Due:", club1.cal_tax_due())
print("Club Age:", club1.cal_age())

print(player1)
print("Player Performance Score:", player1.cal_performance())

print(coach1)
print("Coach Efficiency Score:", coach1.calculate_efficiency())

print("Is Club 1 better than Club 2 in medals?", club1 > club2)