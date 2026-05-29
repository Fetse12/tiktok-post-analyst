# 📊 TikTok Post Performance Analyst

A modern, high-fidelity single-page web application designed to analyze TikTok video metrics, visualize audience engagement, and deliver dynamic tactical marketing insights using **Streamlit**, **Pandas**, and **Plotly**.

---

## ✨ Features

- 🎨 **Premium Aesthetics**: Engineered with a dark-mode glassmorphic user interface, neon gradients, Google Fonts (`Outfit` and `Inter`), and custom-styled responsive metrics cards.
- 📥 **Interactive Input Block**: Frictionless input for TikTok Video URLs, post scheduling (Date & Time pickers), Impressions/Views, Clicks, and Engagement components.
- 📐 **Rigorous Calculations**: Automatic processing of post performance with specialized mathematical modules:
  - **Total Interactions** = $\text{Likes} + \text{Comments} + \text{Shares} + \text{Saves}$
  - **Engagement Rate (ER %)** = $\left(\frac{\text{Total Interactions}}{\text{Total Views}}\right) \times 100$
  - **Conversion Rate (CR %)** = $\left(\frac{\text{Link Clicks}}{\text{Total Views}}\right) \times 100$
  - *Robust edge-case handling guarantees zero division errors when views equal zero.*
- 📈 **Stunning Visual Analytics**:
  - CSS-based glowing dashboard cards highlighting Views, ER %, Click Traffic, and CR %.
  - Interactive **Plotly** donut charts representing the interaction mix (Likes vs. Comments vs. Shares vs. Saves).
  - Clear, structured tracking summary tables.
- 💡 **Tactical Marketing Alerts**: Logic-driven evaluation engine comparing performance against standard industry benchmarks to output actionable marketing cards (Success, Info, Warning, Error alerts) with specific optimization guidelines.

---

## 📈 Industry Benchmarks Applied

### 1. Engagement Rate (ER %)
* **High ($\ge$ 6%)**: Excellent performance! Audience strongly resonates with content style, pacing, and hooks.
* **Medium (3% - 6%)**: Healthy engagement. Standard benchmarks met with room to boost comment interaction.
* **Low (< 3%)**: Lower retention. Indicates that the first 3 seconds (the hook) need improvement.

### 2. Conversion Rate (CR %)
* **High ($\ge$ 2%)**: Strong click-through. Exceptional value-driven call to action.
* **Medium (0.8% - 2%)**: Moderate conversion. Suggests boosting clicks with a stronger sense of urgency.
* **Low (< 0.8%)**: Underperforming funnel. Suggests introducing explicit visual or verbal CTAs.

---

## 🚀 Running the Application Locally

### Prerequisites
Make sure you have Python 3.8+ installed on your local machine.

### Installation & Execution
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Fetse12/tiktok-post-analyst.git
   cd tiktok-post-analyst
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the application**:
   ```bash
   streamlit run tiktok_post_analyst/app.py
   ```

The dashboard will open automatically in your local web browser!
