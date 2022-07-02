# Summary

## What's most important: Batting, Pitching, Fielding and Base Running

After going through some analysis with baseball, I came to wonder in what areas in baseball are statistically important to winning. Thus, we will see how four main skills in baseball, batting, pitching, fielding and base running, effect teams winning percentage.

    **Question : From batting, pitching, fielding and base running, what's the most important skill for winning?**
   
### Variables Used

The challenge to this analysis was to find the measurement that could indicate the performances of batting, pitching and fielding. As a reminder from the previous analysis, Moneyball analysis, the goal of baseball teams is to win. To win, you need runs and to gain runs you need to get on base. Based on this concept, I will be using Base Earned as the indicator to measure the performance of each skills. 

BATTING : $Base_{batting} = TB + BB$

PITCHING : $BaseAllowed_{pitching} = 0.89 * (1.255(H - HR) + 4*HR) + 0.56 * (BB + HBP - IBB)$

FIELDING : $Base_{fielding} = (OCS + PO + DP) - (OSB + E)$

BASE RUNNING : $Base_{running} = SB - CS$

### Era Comparison

<p align="center">
  <img src="https://github.com/jinwls/Batting_Pitching_Fielding/blob/main/plots/EraComparison.png" width="600" height="600">
</p>

MLB has endured many changes in rules, equipment, and strategies over time. Because of such shifts, Major League Baseball has been segmented into distinct eras. For this reason, will have to see if there are significant difference between each eras. According to the tone-wat ANOVA test, the p-value for all four variables is approximately 0, thus we have strong evidence that there's some pairwise group mean difference in each stats at a 5% significant level.

### Importance

Thus, the importance is measured by each era seperatly.

<p align="center">
  <img src="https://github.com/jinwls/Batting_Pitching_Fielding/blob/main/plots/Importance.png" width="600" height="240">
</p>

For all, batting and pitching have been the most significant skill for winning. It seems that in the past, batting has given more impact on teams winning percentage but since the Steroid era, pitching has got more important. 

# What Increased the Importance of Pitching?

<p align="center">
  <img src="https://github.com/jinwls/Batting_Pitching_Fielding/blob/main/plots/BatPitchPerformance.png" width="600" height="600">
</p>

From the plot above it shows that FIP(Fielding Independent Pitching) score increased since the 1980s while wOBA score decreased. Also, looking at the Strike outs and Walks ratio, we can see that the ratio of walks decreased while strike out ratio increased as year goes. This indicates that since the beginning of the Steroid era, the **overall performance of the pitchers increased** making it hard for batters to perform well.

<p align="center">
  <img src="https://github.com/jinwls/Batting_Pitching_Fielding/blob/main/plots/PlayerNum.png" width="600" height="600">
</p>

**What has changed?**

Since the 1980s, there is a **continuous increase** with the number of **pitchers** in the roster. This allows the teams to manage their pitchers efficiently and diverse and quality pitching to the game. With increasing number of pitchers, they can throw less on each games allowing them to not to overuse their shoulders and stay in great condition.  

for more detail about this analysis [click here](https://github.com/jinwls/Batting_Pitching_Fielding/blob/main/importance.ipynb)
