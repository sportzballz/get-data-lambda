class Prediction:
    def __init__(self, winning_team: str, losing_team: str, winning_pitcher: str, losing_pitcher: str, gameDate: str,
                 gameTime: str, ampm: str,
                 odds: int, confidence: str, data_points: str = '0/0'):
        self.winning_team = winning_team
        self.losing_team = losing_team
        self.winning_pitcher = winning_pitcher
        self.losing_pitcher = losing_pitcher
        self.gameDate = gameDate
        self.gameTime = gameTime
        self.ampm = ampm
        self.odds = odds
        self.confidence = confidence
        self.data_points = data_points

    def print_string(self):
        print(self.to_string())

    def to_string(self):
        try:
            self.odds = int(self.odds)
        except ValueError:
            self.odds = 0
        if self.odds > 0:
            self.odds = f"+{self.odds}"
        elif self.odds == 0:
            self.odds = "----"
        return f"```{self.odds} {self.winning_team.upper()} over {self.losing_team.upper()} c:{self.confidence} dp:{self.data_points}```"

    def to_csv(self):
        print(f"{self.odds},{self.winning_team},{self.losing_team},{self.gameDate},{self.winning_pitcher}")

    def get_csv(self):
        return f",{self.odds},{self.winning_team},{self.losing_team},{self.gameDate},{self.winning_pitcher}"


class PredictionActual:
    def __init__(self, prediction: Prediction, actual: str):
        self.prediction = prediction
        self.actual = actual


class PitchingMatchup:
    def __init__(self, whip_advantage: int, win_percentage_advantage: int):
        self.whip_advantage = whip_advantage
        self.win_percentage_advantage = win_percentage_advantage


class Team:
    def __init__(self, abbreviation: str, id: int, name: str):
        self.abbreviation = abbreviation
        self.name = name
        self.id = id


class AdvantageScore:
    def __init__(self, home: int = 0, away: int = 0, home_stats=[], away_stats=[]):
        self.home = home
        self.away = away
        self.home_stats = home_stats
        self.away_stats = away_stats


class WEIGHT:
    def __init__(self, weight: int, lower_is_better: bool):
        self.weight = weight
        self.lower_is_better = lower_is_better


class LineupPlayer:
    def __init__(self, player_id, player_name, player_position, player_batting_order):
        self.player_id = player_id
        self.player_name = player_name
        self.player_position = player_position
        self.player_batting_order = player_batting_order


class Lineup:
    def __init__(self, team_id, lineup_players):
        self.team_id = team_id
        self.lineup_players = lineup_players
