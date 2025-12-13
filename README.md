# Dragon Control and Victory in League of Legends



## Intro

This is a DSC80 projectabout League of Legends Dragon Control and Match Outcome Analysis completed at UC San Diego. This project uses professional League of Legends match data of 2025 to explore the relationship between mid-game key resources—particularly dragon control—and match outcomes.

In League of Legends, dragons are one of the core strategic objectives that shape the course of a match. Dragons with different attributes grant teams sustained buffs, and the “Dragon Soul” earned by collecting four dragons often significantly alters the game’s dynamics. This project analyzes whether dragon control advantage is more than just a reflection of overall economic lead, and whether it statistically correlates with match victories.

Based on professional match data from Oracle's Elixir, this project begins with exploratory data analysis and hypothesis testing. It then constructs predictive models to assess the feasibility of forecasting match outcomes at the 15-minute mark using only mid-game information readily available in-game, such as dragon kill differential and economic gap. Finally, the project analyzes the fairness of these models.

  Author: Zihan Zhang


### Columns Use from Dataset

The dataset used in this project contains multivariate game statistics from esports League of Legends matches. To facilitate readers' understanding of subsequent analyses, this section briefly introduces the core data columns employed in this project. These variables primarily characterize match outcomes, mid-game resource control, and team economic status.

- `gameid`: The unique ID for each match, used to tell different matches apart.

- `teamname`: Team Name. This project uses “each team in each match” as the unit of data analysis.

- `side`：The teams are divided into two sides: Blue and Red.

- `result`：Match result variable. A value of 1 indicates the team won, while 0 means they lost. This is the response variable in the prediction model for this project.
 
- `dragons`：Dragon Control Differential, defined as `dragons - opp_dragons`, is used to describe a team's relative advantage in dragon control and is a key feature in multiple analyses and modeling.

- `barons`: The number of Baron Nashor slays by the team, a key indicator of late-game resource control.

- `golddiffat10`: Economic difference at the 10-minute mark (this team relative to their opposing team).

- `golddiffat15`: The gold difference at the 15-minute mark, an important mid-game economic indicator in both predictive modeling and fairness analysis.

- `goldat15`: The total gold held by the team at the 15-minute mark, used to help assess mid-game economic status.
