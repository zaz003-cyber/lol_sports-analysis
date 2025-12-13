# Dragon Control and Victory in League of Legends

### Intro

This is a DSC80 project about League of Legends Dragon Control and Match Outcome Analysis completed at UC San Diego. This project uses professional League of Legends match data of 2025 to explore the relationship between mid-game key resources particularly dragon control and match outcomes.

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
  width="800" 
  height="600"
  frameborder="0">
</iframe>

The histogram shows dragon control distribution is skewed and slightly right-biased. Most teams control 1 to 4 dragons, with 2 to 3 dragons being the most common outcome, confirming dragon control is typically shared among multiple teams rather than monopolized by a single one. While controlling zero dragons is uncommon, it still occurs, whereas maintaining an extremely high number of dragons (5 or more) is extremely rare.

This reflects dragons as a structured and constrained game objective. Extreme values occur with low frequency, with most matches falling within a narrow, realistic range of dragon counts. This makes the variable suitable for further comparative and predictive analysis.

### Bivariate Analysis

At the same time, I also conducted bivariate analysis to examine the relationship between dragon control and match outcomes. I compared dragon-related statistics between winning and losing teams to understand the connection between objective control and competitive results in the game.

<iframe 
  src="assets/dragons_result.html"
  width="800" 
  height="600"
  frameborder="0">
</iframe>

This box plot compares the distribution of dragon control between winning and losing teams. On average, winning teams tend to secure more dragons, with a higher median and greater upper range, while losing teams cluster around lower dragon counts. This shows dragon control is closely linked to match success.

<iframe 
  src="assets/dragon_diff_result.html"
  width="800" 
  height="600"
  frameborder="0">
</iframe>

This one shows the difference in dragon control between winning and losing teams. Winning teams typically have a positive dragon differential, while losing teams often have a negative one. The disparity between the two distributions shows relative dragon control, rather than absolute quantity, is a key performance indicator.

### Interesting Aggregates

<iframe 
  src="assets/winrate.html"
  width="800" 
  height="600"
  frameborder="0">
</iframe>

This bar chart shows a clear positive correlation between the number of dragons secured and the match win rate. Teams securing fewer than two dragons rarely win, while the win rate increases steadily as more dragons are secured. Once a team secures four or more dragons, the probability of victory becomes extremely high.
So if you're a jungler, you need to connect with your team to secure Dragon Soul. Through making sure these different Dragon Soul buffs, you can expand your team's advantage and lead them to victory.


## Assessment of Missingness

### NMAR Analysis

In my dataset, I analyzed the missingness of the variable `golddiffat15`. Although `golddiffat15` has a significant missingness rate, I did not find strong evidence from permutation tests that its missingness depends on observed variables, such as match outcomes or the number of Baron Nashor kills.
However, the NMAR mechanism cannot be identified solely from the observed data. The distribution of missing gold values may depend on the unobserved values themselves or on underlying game conditions not recorded in the dataset. For example, matches that end unusually early or games with missing mid-game data are more likely to `golddiffat15`. In such instances, the missing values depend on the underlying game state rather than the observed variables.
To further assess whether the missingness in `golddiffat15` data constitutes NMAR, additional information is required, such as indicators of game premature termination or data collection interruption. In the absence of such variables, I cannot conclude whether the missingness in `golddiffat15` qualifies as NMAR. Based on the available evidence, its missingness pattern aligns more closely with MCAR or MAR rather than NMAR. Although I clearly considered the possibility of NMAR and discussed what additional information would be needed to evaluate it.

### Missingness Dependency

I analyzed whether the missingness of the variable `golddiffat15` depends on other observed columns in the dataset. This column has a non-trivial missing rate of approximately **8.2%**, making it suitable for a missingness dependency analysis. I focused on two variables, `result` and `barons`, as factors potentially underlying the missingness pattern. For both analyses, I used permutation tests with a significance level of 0.05 and selected test statistics designed to capture differences in missingness rates between groups.
I first tested whether the absence of `golddiffat15` data depended on `result`, then analyzed its correlation with the number of `barons` secured. These tests allowed me to assess whether the absence of `golddiffat15` data was associated with outcomes observed within the game or with objective control factors.

**Null Hypothesis**: The missingness of `golddiffat15` is independent of match `result`.

**Alternative Hypothesis**: The missingness of `golddiffat15` depends on match `result`.

After performing the permutation test, I found the observed test statistic to be 0.0000 with a p-value of 1.0000. The graph below shows the empirical distribution of the test statistic under the null hypothesis, with the observed statistic marked by the red vertical line.

<iframe
  src="assets/missingness_result.html"
  width="800" 
  height="600"
  frameborder="0">
</iframe>

The observed test statistic is **0.0000**, with a p-value of **1.0000**. This observed statistic lies fully within the empirical distribution of z-scores generated by the permutation test. Since the p-value is greater than the significance level of 0.05, we cannot reject the null hypothesis. Therefore, there is no evidence that missing values in `golddiffat15` depend on match outcomes.

After performing the second permutation test, I found that the observed statistic for this test is **0.1661**, and the p-value is 0.0566. The plot below shows the empirical distribution of the test statistic under the null hypothesis, with the observed statistic marked by the red vertical line.

**Null Hypothesis**: The missingness of `golddiffat15` is independent of the number of `barons` secured.

**Alternative Hypothesis**: The missingness of `golddiffat15` depends on the number of `barons` secured.

<iframe
  src="assets/missingness_barons.html"
  width="800" 
  height="600"
  frameborder="0">
</iframe>

The observed statistic for the variance of missing rates across different baron groups is **0.1661**, with a p-value of **0.0566**. Although this observed value is larger than most values in the permutation distribution, it still falls below the 0.05 significance threshold. Therefore, we again fail to reject the null hypothesis.

## Hypothesis Testing

In this hypothesis test, I am analyzing whether there is a significant difference in the dragon differential between winning teams and losing teams. To be specific, I am looking at whether winning teams are more likely to secure more dragons than their opposition.This analysis helps us understand whether dragon control in League of Legends correlates with match outcome, rather than being the result of random variation.

**Null Hypothesis**: The distribution of `dragon_diff` is the same for winning and losing teams. Any observed difference is due to random chance.

**Alternative Hypothesis**: The distribution of dragon differential differs between winning teams and losing teams.

**Test Statistic**: I use the difference in mean dragon differential between winning and losing teams. This statistic directly measures how many more dragons the winning team averages compared to the losing team.

**Significance Level**: I choose a significance level of α = 0.05.

<iframe 
  src="assets/hypothesis_dragon.html"
  width="800" 
  height="600"
  frameborder="0">
</iframe>

Based on the permutation test, the p-value obtained is extremely small and close to **0**. Therefore, we reject the null hypothesis at the 5% significance level. This shows dragon control is closely related to match outcomes: winning teams tend to secure more dragons than losing teams.

## Framing a Prediction Problem

I define this problem as a binary classification task. The objective is to predict whether a team will win the match using information available within the first 15 minutes of the game.

### Response Variable

The response variable is `result`, which represents the match outcome:

**1**: The team wins

**0**: The team loses

I chose this response variable because the match `result` is the primary focus and is a natural fit for a binary classification model.

### Features and Time of Prediction

When making predictions, I only use information that is actually available within the first 15 minutes of the match.
Therefore, the prediction variables include mid-game objectives control and economic data, such as:

**dragon differential at 15 minutes**

**gold differential at 15 minutes**

Then, through limiting the features to mid-game statistics, I avoid using information that is only known after the match ends, thereby making the prediction task realistic.

### Model Type

Since the response variable has two possible outcomes: win or lose, this is a binary classification problem.

### Evaluation metrics

Since the win-loss outcomes in the dataset are roughly balanced, I use accuracy to evaluate model performance. I find accuracy to be an appropriate metrics in this scenario because it directly measures the proportion of correctly predicted match results and avoids bias from class imbalance.

## Baseline Model

For the baseline model, I built a binary classification model to predict match outcomes: win or loss. I chose logistic regression as the baseline classifier because of its simple structure, high interpretability, and frequent use as a starting point for classification problems.

### Features

The model uses the following two quantitative features, both of which are observable through 15 minutes into the game:

- `dragon_diff`: the dragon differential between the two teams

- `golddiffat15`: the gold difference between the two teams at 15 minutes

Both features are numerical and continuous, so no categorical encoding is required.

### Preprocessing

Before fitting the model, I performed the following preprocessing steps:

Used `SimpleImputer` for **median imputation** to handle missing values

Used `StandardScaler` for **standardization** to make features comparable in magnitude

These steps were performed through a `pipeline` to guarantee consistency in preprocessing during both training and testing.

### Model Training and Assessment

The data was split into 75% training data and 25% test data, with the response variable balanced through stratification to maintain an even distribution of wins and losses.

After model fitting, I performed accuracy evaluation on the test set. This metric proved suitable given the roughly balanced distribution of win/loss outcomes.

The baseline model achieved an accuracy of 0.791, meaning it correctly predicted approximately 79.1% of match results in the test data.

Although this accuracy shows  the mid-game dragon and gold gap contains useful predictive information, the baseline model is relatively simple, depending on only two features.
Therefore, there is still space for improvement by adding more relevant features in the later stages and exploring more complex models.


## Final Model

In the final model, I optimized the baseline approach through the introduction of artificial features. These features more accurately measure a team's relative strengths in terms of objective control and economic advantage, rather than relying solely on raw count data.

I built the features below:

- `dragon_diff`: the difference in dragons secured between the two teams

- `tower_diff`: a tower differential that reflects structural advantage during the game

- `baron_diff`: the number of barons secured by the team

- `objective_diff`: a composite feature combining dragon, tower, and baron differentials

These features stem from the game's core resource accrual mechanism, where advantages accumulate through objective control and eventually convert into an economic lead.
The model more accurately reflects a team's overall strength during the mid-game phase. This is done by combining multiple objectives into a single aggregate score.

### Model and Preprocessing：

I continued to use logistic regression as the modeling algorithm to maintain consistency with the baseline model, while enhancing feature representation capabilities.
Additionally, all features were quantitative, so no categorical encoding was required. I performed the following steps in a pipeline for preprocessing: **Median imputation** to handle missing values, and used `StandardScaler` for **standardization** to make sure features are on comparable scales.This preprocessing is consistently used during the training, validation, and testing phases.

### Hyperparameter Tuning

To improve model performance, I adjusted the regularization strength **C** of the logistic regression model. Hyperparameter C controls the balance between model complexity and regularization: A smaller **C** value will impose stronger regularization, and a larger value will allow the model to fit more complex decision boundary. I performed **5-fold cross-validation** with `GridSearchCV`, searching within the logarithmic range of **C** values: **{0.01, 0.1, 1, 10}**. The optimal parameter value chosen through cross-validation is **C = 1**.

### Model Performance

I evaluated the final model on the same test set as the baseline model. The final model achieved an accuracy of **0.986**, a significant improvement over the baseline model's accuracy of approximately **0.79**. This success confirms the target-designed features effectively captured key information about match outcomes information not sufficiently represented in the baseline feature set.

Through comparing with the baseline model, the final model significantly improved predictive performance. This was achieved through integrating more informative features, which more accurately reflect mid-game objective control and team-wide advantages. Moreover, the model moved away from the isolation of statistical metrics and adopted a composite objective approach. This allows it to more effectively capture how game advantages accumulate and translate into victory. Also, through hyperparameter tuning, the model achieves a better balance between flexibility and regularization. This significantly improves predictive performance while maintaining consistency with the original prediction framework.

## Fairness Analysis

In this section, I will analyze how the final model performs differently across groups with varying early-game economic advantages. To be specific, I pose the following question: **Does the model show differing performance for teams with positive gold differences and those with negative gold differences at the 15-minute mark?** To answer this, I will perform a permutation test and analyze the accuracy differences between the two sets of models.

**Group X** is made up of teams with a positive gold difference at the 15-minute mark, while **Group Y** is made up of teams with a negative gold difference at the 15-minute mark. My evaluation metric is accuracy, with a significance level set at **0.05**.

**Null hypothesis**: The model is fair, that is, it has the same accuracy for **Group X** and **Group Y**.

**Alternative hypothesis**: The model is unfair, that is, there is a difference in accuracy between the two groups. Our test statistic is the difference in accuracy between the two groups.

<iframe 
  src="assets/accuracy_perm.html"
  width="800" 
  height="600"
  frameborder="0">
</iframe>

After completing the permutation test, I received a p-value = **0.7142**， it is greater than 0.05. Thus, we fail to reject the null hypothesis. This shows no strong statistical evidence of a difference in the model's predictive accuracy between teams with and without an opening monetary advantage. Based on this analysis, the model appears to be fair under this grouping standard.
