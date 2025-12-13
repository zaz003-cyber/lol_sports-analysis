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

- `dragon_diff`: Dragon Control Differential, defined as `dragons` - `opp_dragons`, is used to characterize a team's relative advantage in dragon control and is a key feature in multiple analyses and modeling.

## Data Cleaning and Exploratory Data Analysis
### Data Cleaning

To improve the efficiency of subsequent analysis and modeling, this project first filtered the raw dataset, retaining only key variables directly related to match outcomes and mid-game resource control. These include `gameid`, `teamname`, `side`, `result`, `dragons`, `opp_dragons`, `barons`, `towers`, `golddiffat10`, `golddiffat15`, `goldat15`, and `dragon_diff`.

The raw data contained statistics at both the player and team levels. To maintain consistent analytical units, this project organized the data into a format where each row reflects the overall performance of a single team across an entire match, using “each team in each match” as the fundamental unit of analysis.

During data cleaning, I found missing values in certain variables related to mid-game resources and economy，e.g., `dragons` and `golddiffat15`. Given the low proportion of missing values and their concentration in a small number of match records, I chose to remove records where critical variables could not be reasonably predicted. Other missing values were handled in a manner consistent with the match structure and variable meaning to protect data completeness and consistency.

The final dataset, following these data cleaning steps, contains all key variables required for subsequent hypothesis testing and predictive modeling, providing a reliable foundation for further analysis.

The head of my cleaned team-level dataset.

| gameid              | teamname       | side | result | dragons | opp_dragons | barons | towers | golddiffat10 | golddiffat15 | goldat15 | dragon_diff  |
|---------------------|----------------|------|--------|---------|-------------|---------|--------|--------------|--------------|----------|-------------|
| 11715-11715_game_1  | Oh My God      | Red  | 0      | 1.0     | 4.0         | 0.0     | 4.0    | NaN          | NaN          | NaN      | -3.0        |
| 11715-11715_game_1  | Weibo Gaming   | Blue | 1      | 4.0     | 1.0         | 1.0     | 10.0   | NaN          | NaN          | NaN      | 3.0         |
| 11715-11715_game_2  | Oh My God      | Blue | 0      | 2.0     | 2.0         | 0.0     | 1.0    | NaN          | NaN          | NaN      | 0.0         |
| 11715-11715_game_2  | Weibo Gaming   | Red  | 1      | 2.0     | 2.0         | 1.0     | 11.0   | NaN          | NaN          | NaN      | 0.0         |
| 11715-11715_game_3  | Oh My God      | Blue | 0      | 3.0     | 0.0         | 0.0     | 3.0    | NaN          | NaN          | NaN      | 3.0         |

*Note:
The cleaned dataset shown above retains missing values in some mid-game economic variables (e.g., `golddiffat10`, `golddiffat15`, `goldat15`). These missing values arise from structural differences across leagues and matches, where certain statistics are not recorded or applicable. This dataset represents a general cleaned dataset used for exploration. In later analyses that focus specifically on economic advantages, I further subset the data to include only matches with complete economic information.

### Univariate Analysis

I performed a univariate analysis of the dragon count statistics in the dataset.

<iframe
  src="assets/dragons_distribution.html"
  width="100%"
  height="520"
  frameborder="0">
</iframe>

The histogram shows dragon control distribution is skewed and slightly right-biased. Most teams control 1 to 4 dragons, with 2 to 3 dragons being the most common outcome, confirming dragon control is typically shared among multiple teams rather than monopolized by a single one. While controlling zero dragons is uncommon, it still occurs, whereas controlling an extremely high number of dragons (5 or more is extremely rare.

This reflects dragons as a structured and constrained game objective. Extreme values occur with low frequency, with most matches falling within a narrow, realistic range of dragon counts. This makes the variable suitable for further comparative and predictive analysis.

### Bivariate Analysis

<iframe 
  src="assets/dragons_result.html"
  width="100%" 
  height="550px"
  style="border:none;">
</iframe>

This box plot compares the distribution of dragon control between winning and losing teams. On average, winning teams tend to secure more dragons, with a higher median and greater upper range, while losing teams cluster around lower dragon counts. This shows dragon control is closely linked to match success.

<iframe 
  src="assets/dragon_diff_by_result_box.html"
  width="100%" 
  height="550px"
  style="border:none;">
</iframe>

1111111

### Interesting Aggregates

<iframe 
  src="assets/winrate.html"
  width="100%" 
  height="550px"
  style="border:none;">
</iframe>

This bar chart shows a clear positive correlation between the number of dragons secured and the match win rate. Teams securing fewer than two dragons rarely win, while the win rate increases steadily as more dragons are secured. Once a team secures four or more dragons, the probability of victory becomes extremely high, showing that dragon control plays a pivotal role in the outcome of matches.
