# Dragon Control and Victory in League of Legends


### Intro

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
 
- `dragons`：The number of dragons claimed by the team during the match. Dragons are a crucial strategic resource during the mid-game phase of League of Legends and one of the core variables studied in this project. Some matches may have missing values for this variable during the early stages.

- `opp_dragons`: The number of dragons claimed by the opposing team, used to measure the relative state of dragon control between both sides.

- `barons`: The number of Baron Nashor slays by the team, a key indicator of late-game resource control.

- `towers`: The number of defensive towers destroyed by the team, used to track map progression and structural advantages. This variable may be missing in some match records.

- `golddiffat10`: Economic difference at the 10-minute mark (this team relative to their opposing team).

- `golddiffat15`: The gold difference at the 15-minute mark, an important mid-game economic indicator in both predictive modeling and fairness analysis.

- `goldat15`: The total gold held by the team at the 15-minute mark, used to help assess mid-game economic status.


### Data Cleaning

To improve the efficiency of subsequent analysis and modeling, this project first filtered the raw dataset, retaining only key variables directly related to match outcomes and mid-game resource control. These include `gameid`, `teamname`, `side`, `result`, `dragons`, `opp_dragons`, `barons`, `towers`, `golddiffat10`, `golddiffat15`, and `goldat15`.

The raw data contained statistics at both the player and team levels. To maintain consistent analytical units, this project organized the data into a format where each row reflects the overall performance of a single team across an entire match, using “each team in each match” as the fundamental unit of analysis.

During data cleaning, I found missing values in certain variables related to mid-game resources and economy，e.g., `dragons` and `golddiffat15`. Given the low proportion of missing values and their concentration in a small number of match records, I chose to remove records where critical variables could not be reasonably predicted. Other missing values were handled in a manner consistent with the match structure and variable meaning to protect data completeness and consistency.

In addition, to better capture teams' relative advantages in dragon control, I created the dragon differential variable `dragon_diff`, defined as `dragons` - `opp_dragons`. This variable is used as a core feature in subsequent exploratory data analysis, hypothesis testing, and predictive modeling.

The final dataset, following these data cleaning steps, contains all key variables required for subsequent hypothesis testing and predictive modeling, providing a reliable foundation for further analysis.

