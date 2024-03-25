def team_olympiad(n, skills):
    programming, math, PE = [], [], []

    for i, skill in enumerate(skills):
        if skill == 1:
            programming.append(i + 1)  # Add 1 to index to match 1-based indexing
        elif skill == 2:
            math.append(i + 1)
        else:
            PE.append(i + 1)

    min_team_size = min(len(programming), len(math), len(PE))

    if min_team_size == 0:
        return 0, []  # If any skill set is empty, no teams can be formed

    teams = []  # List to store formed teams

    for i in range(min_team_size):
        teams.append((programming[i], math[i], PE[i]))

    return min_team_size, teams

n = int(input())  # Number of participants
skills = list(map(int, input().split()))  # Skills of participants

num_teams, teams = team_olympiad(n, skills)
print(num_teams)
for team in teams:
    print(*team)
