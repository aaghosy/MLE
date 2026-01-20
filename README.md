好，这里我给你一份**干净、专业、偏研究/教学用途的 README**，完全贴合你现在这段代码和你正在学的内容（MLE + log-likelihood）。
你可以直接放在 GitHub 仓库里用。

---

# Maximum Likelihood Estimation for a Biased Coin (Python)

## 📌 Project Overview

This project demonstrates **Maximum Likelihood Estimation (MLE)** for estimating the probability of heads in a biased coin experiment using **log-likelihood**.

We simulate a large number of coin tosses, construct the log-likelihood function of the Bernoulli/Binomial model, and numerically identify the value of the parameter that maximizes it.

The goal of this project is **conceptual clarity**, not performance optimization.

---

## 🧠 Statistical Background

We assume:

* Each coin toss follows a **Bernoulli distribution**
* The probability of heads is an unknown parameter ( p \in (0,1) )
* Given observed data, we estimate ( p ) using **maximum likelihood**

For ( N ) tosses with:

* ( H ) heads
* ( T = N - H ) tails

The **log-likelihood function** is:

[
\log L(p)
=========

H \log(p) + T \log(1 - p)
]

The MLE for ( p ) is known analytically to be:

[
\hat{p} = \frac{H}{N}
]

This project verifies that result **numerically**.

---

## 🧪 What the Code Does

1. Simulates `N = 10,000` coin tosses from a biased coin
2. Computes the number of heads and tails
3. Defines the **log-likelihood function**
4. Evaluates the log-likelihood over a grid of candidate ( p ) values
5. Identifies the **maximum likelihood estimate**
6. Visualizes the log-likelihood curve

---

## 📂 File Structure

```
.
├── mle_coin.py        # Main script
├── README.md          # Project documentation
```

---

## ▶️ How to Run

### Requirements

* Python 3.8+
* NumPy
* Matplotlib

Install dependencies if needed:

```bash
pip install numpy matplotlib
```

### Run the script

```bash
python mle_coin.py
```

---

## 📈 Example Output

* Printed output:

  * Number of heads and tails
  * Estimated MLE for ( p )

* Plot:

  * Log-likelihood as a function of ( p )
  * A clear single maximum near the true probability

---

## 🔍 Key Implementation Details

* **Log-likelihood is used instead of likelihood** to avoid numerical underflow
* Invalid parameter values (`p ≤ 0` or `p ≥ 1`) return `-∞` to enforce parameter constraints
* The MLE is found using `argmax`, not closed-form formulas, to emphasize generality

---

## 🧩 Why This Matters

This example illustrates core ideas used throughout:

* Statistical inference
* Numerical optimization
* EM algorithms
* Regime-switching and mixture models
* Quantitative finance and econometrics

Understanding this simple case makes more complex models (e.g. Gaussian mixtures, hidden states, EM) much easier to grasp.

---

## 🚀 Possible Extensions

* Derive the MLE analytically using first-order conditions
* Replace grid search with `scipy.optimize`
* Extend to a **two-coin mixture model** and implement EM
* Add confidence intervals using Fisher Information

---

## 🧠 Takeaway

> **Maximum likelihood estimation is simple in theory,
> but only works in practice when implemented with numerical care.**

This project focuses on building that care from the ground up.


