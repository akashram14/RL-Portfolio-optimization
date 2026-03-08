# RL-Portfolio-optimization

A **regime-switching, reinforcement-learning-based portfolio optimization** framework that combines classical quantitative finance techniques (Markowitz mean-variance, Black-Litterman) with modern deep RL agents to dynamically allocate capital across assets.

---

## Overview

Traditional portfolio construction methods such as mean-variance optimization (Markowitz) and the Black-Litterman model produce static allocations that do not adapt to changing market conditions. This project explores how deep reinforcement learning agents can:

- **Learn optimal allocation policies** directly from historical price data.
- **Detect and adapt to market regimes** (e.g., bull/bear markets, high/low volatility).
- **Outperform classical baselines** on risk-adjusted return metrics (Sharpe, Sortino, Calmar ratios).

---

## Project Structure

```
RL-Portfolio-optimization/
├── markowitz.ipynb          # Classical mean-variance (Markowitz) optimization baseline
├── black_litterman.ipynb    # Black-Litterman model with investor views
├── notes/
│   └── notes.md             # Research notes, paper references, and design decisions
└── README.md
```

---

## Approaches

### 1. Markowitz Mean-Variance Optimization (baseline)
`markowitz.ipynb` implements the classical Markowitz efficient frontier:
- Estimate expected returns and the covariance matrix from historical data.
- Solve the quadratic program to find the minimum-variance portfolio for a target return.
- Visualize the efficient frontier and the maximum-Sharpe-ratio portfolio.

### 2. Black-Litterman Model
`black_litterman.ipynb` augments Markowitz with a Bayesian framework:
- Combines market equilibrium (CAPM) returns with subjective investor views.
- Produces a more stable and intuitive set of expected returns.
- Serves as a stronger baseline before applying RL agents.

### 3. Deep Reinforcement Learning Agents *(in progress)*
Planned agents to train and evaluate:
| Agent | Algorithm | Notes |
|-------|-----------|-------|
| DDPG Portfolio | Deep Deterministic Policy Gradient | Continuous action space over portfolio weights |
| PPO Regime-Aware | Proximal Policy Optimization | Regime detection via HMM/clustering state features |
| SAC Portfolio | Soft Actor-Critic | Entropy-regularized for exploration |

---

## Key Challenges

- **Non-stationarity**: Financial time series have time-varying statistics that violate the i.i.d. assumption required by many RL algorithms.
- **Dimensionality**: With many assets, the state and action spaces grow quickly. PCA and other dimensionality-reduction techniques are being explored.
- **Reward shaping**: Defining a reward that balances return, risk, and transaction costs is non-trivial.
- **Regime detection**: Identifying market regimes (e.g., via Hidden Markov Models) and conditioning the agent on regime labels improves generalization.

---

## Getting Started

### Prerequisites

```bash
pip install numpy pandas matplotlib scipy cvxpy yfinance jupyter
```

For RL agents (coming soon):
```bash
pip install torch stable-baselines3 gymnasium
```

### Running the Notebooks

```bash
jupyter notebook
```

Open `markowitz.ipynb` or `black_litterman.ipynb` to run the classical baselines.

---

## References

### Research Papers
1. [Deep Deterministic Portfolio Optimization](https://arxiv.org/pdf/2003.06497)
2. [Deep RL for Optimal Portfolio Allocation: A Comparative Study with MVO](https://icaps23.icaps-conference.org/papers/finplan/FinPlan23_paper_4.pdf)
3. [Adaptive and Regime-Aware RL for Portfolio Management](https://arxiv.org/pdf/2509.14385)
4. [Bridging the Gap between Markowitz Planning and Deep Reinforcement Learning](https://arxiv.org/pdf/2010.09108)
5. [Cryptocurrency Portfolio Management with Deep Reinforcement Learning](https://arxiv.org/pdf/1612.01277)
6. [A Deep RL Framework for the Financial Portfolio Management Problem](https://arxiv.org/pdf/1706.10059)
7. [MIT MEng Thesis – Portfolio Optimization with RL](https://dspace.mit.edu/bitstream/handle/1721.1/157186/masuda-jmasuda-meng-eecs-2024-thesis.pdf)

### Books
1. [Portfolio Optimization (Roncalli)](https://portfoliooptimizationbook.com/portfolio-optimization-book.pdf)

### Reference Implementations
1. [CFMTech – Deep RL for Portfolio Optimization](https://github.com/CFMTech/Deep-RL-for-Portfolio-Optimization)
2. [GabrielNixon – RegimeAware-PPO](https://github.com/GabrielNixon/RegimeAware-PPO)

---

## License

This project is for research and educational purposes.
