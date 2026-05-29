import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, time

# Set premium page config
st.set_page_config(
    page_title="TikTok Post Performance Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Injectable CSS for Premium Dark Glassmorphism Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap');

    /* Global styling overrides */
    .stApp {
        background: linear-gradient(135deg, #0f0c1b 0%, #15102a 50%, #09070f 100%);
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }

    /* Gradient Title */
    .main-title {
        background: linear-gradient(90deg, #FF0050 0%, #00F2FE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 0.2rem;
        padding-top: 1rem;
    }

    .sub-title {
        text-align: center;
        color: #94A3B8;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
        font-weight: 400;
    }

    /* Glassmorphic card style */
    .glass-card {
        background: rgba(30, 27, 57, 0.4);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 24px;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    
    .glass-card:hover {
        border-color: rgba(6, 182, 212, 0.4);
        transform: translateY(-2px);
    }

    /* Form Container specific styling */
    .stForm {
        background: rgba(30, 27, 57, 0.35) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 16px !important;
        padding: 28px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
    }

    /* Metric Cards Grid */
    .metric-container {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        flex-wrap: wrap;
        margin-bottom: 24px;
    }

    .metric-card {
        flex: 1;
        min-width: 220px;
        background: rgba(25, 20, 45, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .metric-card:hover {
        border-color: rgba(255, 0, 80, 0.4);
        box-shadow: 0 8px 30px rgba(255, 0, 80, 0.15);
    }

    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
    }

    .metric-card.views::before { background: #00F2FE; }
    .metric-card.er::before { background: #FF0050; }
    .metric-card.clicks::before { background: #a855f7; }
    .metric-card.cr::before { background: #10B981; }

    .metric-value {
        font-family: 'Outfit', sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 8px 0;
        background: #ffffff;
        -webkit-background-clip: text;
        color: white;
    }

    .metric-card.views .metric-value { text-shadow: 0 0 10px rgba(0, 242, 254, 0.3); }
    .metric-card.er .metric-value { text-shadow: 0 0 10px rgba(255, 0, 80, 0.3); }
    .metric-card.clicks .metric-value { text-shadow: 0 0 10px rgba(168, 85, 247, 0.3); }
    .metric-card.cr .metric-value { text-shadow: 0 0 10px rgba(16, 185, 129, 0.3); }

    .metric-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #94A3B8;
        font-weight: 600;
    }

    /* Styled tactical alert boxes */
    .insight-box {
        padding: 16px 20px;
        border-radius: 12px;
        margin-bottom: 16px;
        border-left: 5px solid;
        background: rgba(30, 27, 57, 0.3);
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .insight-box.success {
        border-left-color: #10B981;
        background: rgba(16, 185, 129, 0.08);
        border: 1px solid rgba(16, 185, 129, 0.15);
        border-left-width: 5px;
    }
    .insight-box.info {
        border-left-color: #06B6D4;
        background: rgba(6, 182, 212, 0.08);
        border: 1px solid rgba(6, 182, 212, 0.15);
        border-left-width: 5px;
    }
    .insight-box.warning {
        border-left-color: #F59E0B;
        background: rgba(245, 158, 11, 0.08);
        border: 1px solid rgba(245, 158, 11, 0.15);
        border-left-width: 5px;
    }
    .insight-box.danger {
        border-left-color: #EF4444;
        background: rgba(239, 68, 68, 0.08);
        border: 1px solid rgba(239, 68, 68, 0.15);
        border-left-width: 5px;
    }

    .insight-title {
        font-weight: 700;
        font-family: 'Outfit', sans-serif;
        font-size: 1rem;
    }
    .insight-box.success .insight-title { color: #34D399; }
    .insight-box.info .insight-title { color: #22D3EE; }
    .insight-box.warning .insight-title { color: #FBBF24; }
    .insight-box.danger .insight-title { color: #FCA5A5; }

    .insight-text {
        font-size: 0.92rem;
        color: #CBD5E1;
        line-height: 1.5;
    }

    /* Style the forms input widgets */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        background-color: rgba(15, 12, 27, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 8px !important;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus {
        border-color: #00F2FE !important;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.2) !important;
    }

    /* Main submit button */
    .stButton>button {
        background: linear-gradient(90deg, #FF0050 0%, #a855f7 50%, #00F2FE 100%) !important;
        color: white !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 12px 30px !important;
        border-radius: 10px !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(255, 0, 80, 0.25) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 0, 80, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

# Application Header
st.markdown("<h1 class='main-title'>TikTok Post Performance Analyst</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>High-fidelity social performance intelligence dashboard & post analytics engine</div>", unsafe_allow_html=True)

# Layout: Form Block & Results Block Side-by-Side
col_left, col_right = st.columns([2, 3])

# Session state initialization for holding results
if 'calculated' not in st.session_state:
    st.session_state.calculated = False
    st.session_state.video_url = ""
    st.session_state.post_datetime = None
    st.session_state.views = 0
    st.session_state.likes = 0
    st.session_state.comments = 0
    st.session_state.shares = 0
    st.session_state.saves = 0
    st.session_state.clicks = 0
    st.session_state.total_interactions = 0
    st.session_state.er = 0.0
    st.session_state.cr = 0.0

with col_left:
    st.markdown("### 📥 Post Data Input", unsafe_allow_html=True)
    
    with st.form("post_input_form"):
        # TikTok URL
        video_url = st.text_input(
            "TikTok Video URL", 
            value=st.session_state.video_url,
            placeholder="https://www.tiktok.com/@username/video/123456789",
            help="Insert the direct link to the TikTok video for analysis."
        )
        
        # Responsive Side-by-Side Date/Time pickers
        st.markdown("<div style='margin-bottom: -15px; font-weight: 500; font-size: 0.88rem; color: #94A3B8;'>Date and Time of Post</div>", unsafe_allow_html=True)
        col_date, col_time = st.columns(2)
        with col_date:
            post_date = st.date_input("Post Date", value=datetime.today())
        with col_time:
            post_time = st.time_input("Post Time", value=time(12, 0))
            
        st.markdown("<hr style='border: 0; height: 1px; background: rgba(255,255,255,0.08); margin: 15px 0;'>", unsafe_allow_html=True)
        
        # Total Views
        views = st.number_input(
            "Total Impressions / Views", 
            min_value=0, 
            value=st.session_state.views, 
            step=1,
            help="Total times the video was viewed."
        )
        
        # Engagement Metrics (likes, comments, shares, saves)
        st.markdown("<div style='font-weight: 500; font-size: 0.88rem; color: #94A3B8; margin-bottom: 5px;'>Engagement Metrics</div>", unsafe_allow_html=True)
        col_eng_1, col_eng_2 = st.columns(2)
        with col_eng_1:
            likes = st.number_input("Likes", min_value=0, value=st.session_state.likes, step=1)
            shares = st.number_input("Shares", min_value=0, value=st.session_state.shares, step=1)
        with col_eng_2:
            comments = st.number_input("Comments", min_value=0, value=st.session_state.comments, step=1)
            saves = st.number_input("Saves", min_value=0, value=st.session_state.saves, step=1)
            
        st.markdown("<hr style='border: 0; height: 1px; background: rgba(255,255,255,0.08); margin: 15px 0;'>", unsafe_allow_html=True)
        
        # Click Traffic
        clicks = st.number_input(
            "Link / Profile Clicks", 
            min_value=0, 
            value=st.session_state.clicks, 
            step=1,
            help="Total direct link clicks or profile clicks generated by this video."
        )
        
        # Submit Button
        submit_btn = st.form_submit_button("Analyze Performance")

        if submit_btn:
            # Combines date and time
            st.session_state.post_datetime = datetime.combine(post_date, post_time)
            st.session_state.video_url = video_url
            st.session_state.views = views
            st.session_state.likes = likes
            st.session_state.comments = comments
            st.session_state.shares = shares
            st.session_state.saves = saves
            st.session_state.clicks = clicks
            
            # Calculations (Formula specifications from prompt instructions)
            st.session_state.total_interactions = likes + comments + shares + saves
            
            # Edge-case zero views handling
            if views > 0:
                st.session_state.er = (st.session_state.total_interactions / views) * 100
                st.session_state.cr = (clicks / views) * 100
            else:
                st.session_state.er = 0.0
                st.session_state.cr = 0.0
                
            st.session_state.calculated = True

# Right Side Panel: Output Analytics & Insights
with col_right:
    st.markdown("### 📊 Performance Analytics Dashboard", unsafe_allow_html=True)
    
    if st.session_state.calculated:
        # 1. High-fidelity HTML Grid of Metric Cards
        metrics_html = f"""
        <div class="metric-container">
            <div class="metric-card views">
                <div class="metric-label">Total Views</div>
                <div class="metric-value">{st.session_state.views:,}</div>
            </div>
            <div class="metric-card er">
                <div class="metric-label">Engagement Rate (ER)</div>
                <div class="metric-value">{st.session_state.er:.2f}%</div>
            </div>
            <div class="metric-card clicks">
                <div class="metric-label">Total Clicks</div>
                <div class="metric-value">{st.session_state.clicks:,}</div>
            </div>
            <div class="metric-card cr">
                <div class="metric-label">Conversion Rate (CR)</div>
                <div class="metric-value">{st.session_state.cr:.2f}%</div>
            </div>
        </div>
        """
        st.markdown(metrics_html, unsafe_allow_html=True)
        
        # Setup layouts for interactive chart and data summary
        col_chart, col_table = st.columns([13, 10])
        
        with col_chart:
            st.markdown("#### ⚡ Engagement Breakdown", unsafe_allow_html=True)
            
            # Create premium styled interactive plotly donut chart
            labels = ['Likes', 'Comments', 'Shares', 'Saves']
            values = [st.session_state.likes, st.session_state.comments, st.session_state.shares, st.session_state.saves]
            
            # Handling case where there is no interaction to show on the chart
            if sum(values) == 0:
                st.info("No interactions recorded yet. Post some interactions to view breakdown chart.")
            else:
                fig = go.Figure(data=[go.Pie(
                    labels=labels,
                    values=values,
                    hole=.5,
                    marker=dict(colors=['#FF0050', '#00F2FE', '#8B5CF6', '#F59E0B']),
                    hoverinfo="label+value+percent",
                    textinfo="percent",
                    textfont=dict(size=13, color='white', family='Inter')
                )])
                
                fig.update_layout(
                    showlegend=True,
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=-0.2,
                        xanchor="center",
                        x=0.5,
                        font=dict(color='#94A3B8', size=11, family='Inter')
                    ),
                    margin=dict(t=10, b=10, l=10, r=10),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    width=300,
                    height=280
                )
                st.plotly_chart(fig, use_container_width=True)
                
        with col_table:
            st.markdown("#### 📝 Metric Summary Table", unsafe_allow_html=True)
            
            # Formulate structured data framework for Markdown presentation
            date_str = st.session_state.post_datetime.strftime("%Y-%m-%d %H:%M:%S") if st.session_state.post_datetime else "N/A"
            url_display = f"[Link]({st.session_state.video_url})" if st.session_state.video_url.startswith("http") else "N/A"
            
            summary_markdown = f"""
| Post Metric / Attribute | Value / Result |
| :--- | :--- |
| **TikTok Video URL** | {url_display} |
| **Post Date & Time** | `{date_str}` |
| **Total Views / Impressions** | `{st.session_state.views:,}` |
| **Likes Received** | `{st.session_state.likes:,}` |
| **Comments Received** | `{st.session_state.comments:,}` |
| **Shares Executed** | `{st.session_state.shares:,}` |
| **Saves Logged** | `{st.session_state.saves:,}` |
| **Total Interactions** | `{"{:,}".format(st.session_state.total_interactions)}` |
| **Link / Profile Clicks** | `{st.session_state.clicks:,}` |
| **Engagement Rate (ER %)** | **`{st.session_state.er:.2f}%`** |
| **Conversion Rate (CR %)** | **`{st.session_state.cr:.2f}%`** |
"""
            st.markdown(summary_markdown)
            
        # 2. Logic-Driven Tactical Insights Section
        st.markdown("<hr style='border: 0; height: 1px; background: rgba(255,255,255,0.08); margin: 25px 0;'>", unsafe_allow_html=True)
        st.markdown("### 💡 Tactical Marketing Insights & Strategic Actions", unsafe_allow_html=True)
        
        # Setup conditional evaluation logic for Engagement Rates
        er_val = st.session_state.er
        if er_val >= 6.0:
            er_class = "success"
            er_title = "🔥 High-Performing Engagement Rate"
            er_text = (
                f"Your Engagement Rate is a remarkable **{er_val:.2f}%** (TikTok Benchmark: >6%). This video strongly "
                "resonated with your audience! The visual hook, audio choice, and storytelling format are exceptionally "
                "strong. **Recommendation:** Double down on this exact style, editing pace, and topic. Re-share this to "
                "other short-form video platforms (Instagram Reels, YouTube Shorts) immediately to maximize reach."
            )
        elif 3.0 <= er_val < 6.0:
            er_class = "info"
            er_title = "⚡ Healthy Engagement Rate"
            er_text = (
                f"Your Engagement Rate is **{er_val:.2f}%** which aligns well with standard healthy metrics (TikTok Benchmark: 3%-6%). "
                "The community is interacting with your content, but there is room to amplify. **Recommendation:** "
                "Initiate conversations in the comment section by replying to top comments with interactive questions. "
                "For your next video, introduce an interactive element like a TikTok Poll or Q&A sticker to stimulate comments."
            )
        else:
            # Low engagement (ER < 3.0 or Views = 0)
            if st.session_state.views == 0:
                er_class = "warning"
                er_title = "⚠️ Pending View Traffic"
                er_text = "No views recorded yet. Please input total post impressions or views to calculate true engagement metrics."
            else:
                er_class = "danger"
                er_title = "📉 Lower Engagement Threshold"
                er_text = (
                    f"Your Engagement Rate is **{er_val:.2f}%** which falls below typical high-performing criteria (TikTok Benchmark: <3%). "
                    "Audience attention is dropping off early. **Recommendation:** Critically evaluate the first 3 seconds of "
                    "your video (the hook). Ensure your next post features high-contrast text overlays, immediate action, or a strong "
                    "verbal curiosity hook. Study similar viral hooks in your niche to boost retention."
                )
                
        # Setup conditional evaluation logic for Conversion Rates
        cr_val = st.session_state.cr
        if cr_val >= 2.0:
            cr_class = "success"
            cr_title = "🎯 Outstanding Click-Through Conversion"
            cr_text = (
                f"Your Conversion Rate is a high **{cr_val:.2f}%** (Benchmark: >2%). Your audience is highly motivated "
                "to take direct action! The call-to-action (CTA) inside the video was exceptionally clear and aligned with "
                "viewer intent. **Recommendation:** Capture this momentum. Ensure the target link landing page is fully optimized "
                "for mobile, load-time optimized, and possesses a frictionless user journey to finalize their purchase or sign-up."
            )
        elif 0.8 <= cr_val < 2.0:
            cr_class = "info"
            cr_title = "🧭 Moderate Click-Through Conversion"
            cr_text = (
                f"Your Conversion Rate is **{cr_val:.2f}%** (Benchmark: 0.8%-2%). A healthy percentage of viewers visited "
                "your profile/link, but the transition from viewer to clicker could be stronger. **Recommendation:** "
                "Add a stronger sense of urgency to your call-to-action (e.g., 'Limited time offer in bio' or 'Free guide is only up "
                "this week'). Ensure you verbally state and visually point towards the link location on the screen during the video."
            )
        else:
            # Low conversion (CR < 0.8 or Views = 0)
            if st.session_state.views == 0:
                cr_class = "warning"
                cr_title = "⚠️ Pending Conversion Traffic"
                cr_text = "Input view impressions and link/profile clicks to calculate conversion effectiveness."
            else:
                cr_class = "danger"
                cr_title = "🛑 Underperforming Conversion Funnel"
                cr_text = (
                    f"Your Conversion Rate is currently **{cr_val:.2f}%** which indicates a leak in the funnel (Benchmark: <0.8%). "
                    "Viewers are watching but have very little incentive to check your profile or click your link. **Recommendation:** "
                    "Make your Call to Action (CTA) explicit. Rather than 'check link', use value-driven CTAs: 'Grab the free template "
                    "at the link in my bio!' Add high-contrast on-screen arrow graphics pointing towards your profile avatar."
                )

        # Output Styled tactical insights
        st.markdown(f"""
        <div class="insight-box {er_class}">
            <div class="insight-title">{er_title}</div>
            <div class="insight-text">{er_text}</div>
        </div>
        <div class="insight-box {cr_class}">
            <div class="insight-title">{cr_title}</div>
            <div class="insight-text">{cr_text}</div>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        # Default Welcome State
        st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 50px 30px;">
            <div style="font-size: 4rem; margin-bottom: 20px;">🚀</div>
            <h3 style="color: white; margin-bottom: 10px;">Ready for Analysis</h3>
            <p style="color: #94A3B8; max-width: 480px; margin: 0 auto 30px; line-height: 1.6;">
                Fill out the performance form on the left, including your post metrics and traffic clicks, 
                and submit to generate interactive charts, rates, and customized tactical marketing recommendations.
            </p>
            <div style="display: inline-flex; gap: 20px; flex-wrap: wrap; justify-content: center;">
                <span style="background: rgba(255, 0, 80, 0.15); border: 1px solid rgba(255, 0, 80, 0.3); border-radius: 20px; padding: 6px 16px; font-size: 0.85rem; color: #FF0050; font-weight: 600;">TikTok Benchmarks Applied</span>
                <span style="background: rgba(6, 182, 212, 0.15); border: 1px solid rgba(6, 182, 212, 0.3); border-radius: 20px; padding: 6px 16px; font-size: 0.85rem; color: #00F2FE; font-weight: 600;">Plotly Visual Breakdown</span>
                <span style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 20px; padding: 6px 16px; font-size: 0.85rem; color: #10B981; font-weight: 600;">Frictionless Conversion Calculations</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
