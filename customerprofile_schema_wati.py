import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Wati Customer Intelligence",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2rem;
        font-weight: bold;
        color: #16a34a;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #bbf7d0;
        margin-bottom: 1rem;
    }
    .metric-card-blue {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border: 1px solid #bfdbfe;
    }
    .metric-card-purple {
        background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
        border: 1px solid #e9d5ff;
    }
    .metric-card-orange {
        background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
        border: 1px solid #fed7aa;
    }
    .alert-high {
        background: linear-gradient(135deg, #fff7ed 0%, #fef2f2 100%);
        border-left: 4px solid #f97316;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .alert-warning {
        background: linear-gradient(135deg, #faf5ff 0%, #eff6ff 100%);
        border-left: 4px solid #a855f7;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .action-card {
        background: linear-gradient(135deg, #eff6ff 0%, #f3e8ff 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #c7d2fe;
        margin-bottom: 0.75rem;
    }
    .impact-metric {
        background: linear-gradient(135deg, #f0fdf4 0%, #dbeafe 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #86efac;
        margin-top: 1rem;
    }
    .chat-message-user {
        background: white;
        border: 1px solid #e5e7eb;
        padding: 0.75rem;
        border-radius: 1rem;
        margin-bottom: 0.5rem;
        max-width: 70%;
    }
    .chat-message-agent {
        background: #16a34a;
        color: white;
        padding: 0.75rem;
        border-radius: 1rem;
        margin-bottom: 0.5rem;
        max-width: 70%;
        margin-left: auto;
    }
    .tag {
        display: inline-block;
        background: #dbeafe;
        color: #1e40af;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .suggestion-box {
        background: linear-gradient(135deg, #dbeafe 0%, #e9d5ff 100%);
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Customer data
customers = {
    "Sarah Chen": {
        "phone": "+1 (555) 234-5678",
        "lead_score": 85,
        "stage": "Hot Lead",
        "value": "$0",
        "source": "Instagram Ad",
        "behavior": "Viewed pricing 3x, Clicked integrations link",
        "tags": ["Premium Interest", "High Intent"],
        "engagement_score": 78,
        "last_active": "2 days ago",
        "timezone": "PST",
        "campaigns_opened": 2,
        "conversation_count": 4,
        "avg_response_time": "5 min",
        "purchase_history": [],
        "cart_value": 0,
        "priority": "high",
        "messages": [
            {"sender": "customer", "text": "Hi, I'm interested in your Premium plan", "time": "2 days ago"},
            {"sender": "customer", "text": "I saw the pricing but wanted to know about integrations", "time": "2 days ago"},
            {"sender": "agent", "text": "Great! Our Premium plan includes unlimited integrations with Shopify, Salesforce, and 50+ other platforms. Would you like a demo?", "time": "2 days ago"}
        ]
    },
    "Marcus Johnson": {
        "phone": "+1 (555) 876-5432",
        "lead_score": 45,
        "stage": "Customer",
        "value": "$5,240",
        "source": "Website",
        "behavior": "Order placed 30 days ago, No recent activity",
        "tags": ["VIP", "Churn Risk"],
        "engagement_score": 32,
        "last_active": "30 days ago",
        "timezone": "EST",
        "campaigns_opened": 8,
        "conversation_count": 12,
        "avg_response_time": "3 min",
        "purchase_history": ["Product A", "Product B", "Premium Service"],
        "cart_value": 0,
        "priority": "medium",
        "messages": [
            {"sender": "customer", "text": "I love the product!", "time": "30 days ago"},
            {"sender": "agent", "text": "That's wonderful to hear! Let us know if you need anything.", "time": "30 days ago"},
            {"sender": "customer", "text": "Thanks for the help!", "time": "30 days ago"}
        ]
    },
    "Emma Rodriguez": {
        "phone": "+1 (555) 345-7890",
        "lead_score": 92,
        "stage": "Customer",
        "value": "$1,850",
        "source": "Referral",
        "behavior": "Active order, 2 prev shipping delays",
        "tags": ["VIP", "Support Priority"],
        "engagement_score": 88,
        "last_active": "15 min ago",
        "timezone": "CST",
        "campaigns_opened": 5,
        "conversation_count": 8,
        "avg_response_time": "2 min",
        "purchase_history": ["Product C", "Product D"],
        "cart_value": 450,
        "priority": "high",
        "messages": [
            {"sender": "customer", "text": "When will my order ship?", "time": "15 min ago"},
            {"sender": "agent", "text": "Let me check that for you right away!", "time": "14 min ago"}
        ]
    }
}

# Smart actions
smart_actions = {
    "Sarah Chen": [
        {
            "icon": "📈",
            "label": "Send Personalized Offer",
            "desc": "10% discount for Premium - 85% conv. probability",
            "impact": "+$2,400 potential ARR"
        },
        {
            "icon": "⏰",
            "label": "Schedule Demo Call",
            "desc": "Best time: 7-9 PM PST (peak engagement)",
            "impact": "+65% show rate"
        },
        {
            "icon": "⚡",
            "label": "Auto-send Integration Guide",
            "desc": "Addresses their main question",
            "impact": "+40% response rate"
        }
    ],
    "Marcus Johnson": [
        {
            "icon": "⚠️",
            "label": "Re-engagement Campaign",
            "desc": "Win-back offer based on past purchases",
            "impact": "Reduce churn by 35%"
        },
        {
            "icon": "⭐",
            "label": "Request Product Review",
            "desc": "Satisfied customer, good timing",
            "impact": "+1 review, boost SEO"
        },
        {
            "icon": "💰",
            "label": "Upsell Opportunity",
            "desc": "Cross-sell Product E (high affinity)",
            "impact": "+$850 avg order"
        }
    ],
    "Emma Rodriguez": [
        {
            "icon": "📦",
            "label": "Priority Shipping Update",
            "desc": "VIP customer with shipping history",
            "impact": "Prevent escalation"
        },
        {
            "icon": "⚠️",
            "label": "Proactive Apology + Credit",
            "desc": "Past issues detected, high value customer",
            "impact": "Retain $5k+ LTV"
        },
        {
            "icon": "💬",
            "label": "Route to Senior Support",
            "desc": "Complex case, VIP treatment needed",
            "impact": "-50% resolution time"
        }
    ]
}

# Impact metrics
impact_metrics = {
    "Sarah Chen": {
        "title": "Lead Conversion Impact",
        "metrics": [
            {"label": "Conversion Rate Lift", "value": "+42%", "context": "vs generic outreach"},
            {"label": "Response Time", "value": "5 min", "context": "avg for this customer"},
            {"label": "Deal Value", "value": "$2,880", "context": "Premium annual plan"},
            {"label": "Win Probability", "value": "85%", "context": "based on behavior"}
        ]
    },
    "Marcus Johnson": {
        "title": "Churn Prevention Impact",
        "metrics": [
            {"label": "Churn Risk", "value": "68%", "context": "30 days inactive"},
            {"label": "LTV at Risk", "value": "$5,240", "context": "total spend to date"},
            {"label": "Recovery Rate", "value": "35%", "context": "with personalized campaign"},
            {"label": "ROI", "value": "12.5x", "context": "campaign cost vs recovery"}
        ]
    },
    "Emma Rodriguez": {
        "title": "Support Efficiency Impact",
        "metrics": [
            {"label": "Context Load Time", "value": "0 sec", "context": "instant full history"},
            {"label": "Resolution Time", "value": "-45%", "context": "vs no profile data"},
            {"label": "Customer Satisfaction", "value": "+28%", "context": "with proactive support"},
            {"label": "Retention Impact", "value": "92%", "context": "VIP retention rate"}
        ]
    }
}

# Initialize session state
if 'selected_customer' not in st.session_state:
    st.session_state.selected_customer = "Sarah Chen"
if 'show_alert' not in st.session_state:
    st.session_state.show_alert = True
if 'show_suggestion' not in st.session_state:
    st.session_state.show_suggestion = True

# Sidebar
with st.sidebar:
    st.markdown('<div class="main-header">💬 Wati</div>', unsafe_allow_html=True)
    
    st.markdown("### Navigation")
    nav_option = st.radio("", ["📥 Inbox", "📢 Campaigns", "📊 Analytics"], label_visibility="collapsed")
    
    st.markdown("---")
    
    st.markdown("### AI-Powered Insights")
    st.info("⚡ **Smart Actions Ready**\n\n3 high-impact opportunities")
    
    st.markdown("---")
    
    st.markdown("### Select Customer")
    selected = st.selectbox(
        "Choose a customer:",
        list(customers.keys()),
        index=list(customers.keys()).index(st.session_state.selected_customer)
    )
    
    if selected != st.session_state.selected_customer:
        st.session_state.selected_customer = selected
        st.session_state.show_alert = True
        st.session_state.show_suggestion = True
        st.rerun()

# Main content
customer = customers[st.session_state.selected_customer]

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f'<div class="main-header">{st.session_state.selected_customer}</div>', unsafe_allow_html=True)
    st.markdown(f"**{customer['phone']}** • {customer['timezone']} • Last active: {customer['last_active']}")

# Smart alerts
if st.session_state.show_alert:
    if st.session_state.selected_customer == "Sarah Chen":
        st.markdown("""
        <div class="alert-high">
            <h4>🔥 Hot Lead Alert - High Conversion Probability (85%)</h4>
            <p>Sarah has viewed pricing 3x and asked about integrations. This matches our "Ready to Buy" pattern. 
            <strong>Suggested action: Send personalized offer now.</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 2, 6])
        with col1:
            if st.button("✅ Send Offer (1-click)", key="send_offer"):
                st.success("Offer sent!")
        with col2:
            if st.button("👁️ View Full Profile", key="view_profile"):
                st.info("Viewing full profile...")
        with col3:
            if st.button("✕ Dismiss", key="dismiss_sarah"):
                st.session_state.show_alert = False
                st.rerun()
    
    elif st.session_state.selected_customer == "Emma Rodriguez":
        st.markdown("""
        <div class="alert-warning">
            <h4>⚠️ VIP Customer - Previous Shipping Issues Detected</h4>
            <p>Emma has experienced 2 shipping delays before (LTV: $1,850). Current order status: In transit. 
            <strong>Suggested: Priority handling + proactive update.</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 2, 6])
        with col1:
            if st.button("📦 Send Priority Update", key="priority_update"):
                st.success("Priority update sent!")
        with col2:
            if st.button("🆙 Escalate to Senior Support", key="escalate"):
                st.info("Escalated to senior support")
        with col3:
            if st.button("✕ Dismiss", key="dismiss_emma"):
                st.session_state.show_alert = False
                st.rerun()

st.markdown("---")

# Main layout
col_chat, col_profile = st.columns([2, 1])

with col_chat:
    st.markdown("### 💬 Conversation")
    
    # Chat messages
    for msg in customer["messages"]:
        if msg["sender"] == "customer":
            st.markdown(f"""
            <div class="chat-message-user">
                <div style="font-size: 0.9rem;">{msg['text']}</div>
                <div style="font-size: 0.75rem; color: #9ca3af; margin-top: 0.25rem;">{msg['time']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="text-align: right;">
                <div class="chat-message-agent">
                    <div style="font-size: 0.9rem;">{msg['text']}</div>
                    <div style="font-size: 0.75rem; opacity: 0.8; margin-top: 0.25rem;">{msg['time']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # AI Suggestion
    if st.session_state.show_suggestion and st.session_state.selected_customer == "Sarah Chen":
        st.markdown("""
        <div class="suggestion-box">
            <h4>💡 AI-Suggested Response</h4>
            <div style="background: white; padding: 1rem; border-radius: 0.5rem; margin: 0.75rem 0; border: 1px solid #bfdbfe;">
                "Hi Sarah! I see you're interested in our Premium plan integrations. Great news - we have native integrations with Shopify, Salesforce, HubSpot, and 50+ other platforms. Plus, I can offer you 10% off your first year if you sign up this week. Would you like me to schedule a quick 15-min demo to show you how it works? 🚀"
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 2, 6])
        with col1:
            if st.button("📤 Send This Message", key="send_suggested"):
                st.success("Message sent!")
                st.session_state.show_suggestion = False
                st.rerun()
        with col2:
            if st.button("✏️ Edit First", key="edit_suggested"):
                st.info("Opening editor...")
        with col3:
            if st.button("✕ Dismiss Suggestion", key="dismiss_suggestion"):
                st.session_state.show_suggestion = False
                st.rerun()
    
    # Message input
    st.text_input("Type a message...", key="message_input", placeholder="Type your message here...")
    if st.button("📤 Send", key="send_message"):
        st.success("Message sent!")

with col_profile:
    st.markdown("### 🎯 Customer Intelligence")
    
    # Quick stats
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 0.75rem; color: #4b5563;">Lead Score</div>
            <div style="font-size: 2rem; font-weight: bold; color: #16a34a;">{customer['lead_score']}</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card metric-card-blue">
            <div style="font-size: 0.75rem; color: #4b5563;">Lifetime Value</div>
            <div style="font-size: 2rem; font-weight: bold; color: #2563eb;">{customer['value']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown(f"""
        <div class="metric-card metric-card-purple">
            <div style="font-size: 0.75rem; color: #4b5563;">Engagement</div>
            <div style="font-size: 2rem; font-weight: bold; color: #9333ea;">{customer['engagement_score']}%</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-card metric-card-orange">
            <div style="font-size: 0.75rem; color: #4b5563;">Conversations</div>
            <div style="font-size: 2rem; font-weight: bold; color: #ea580c;">{customer['conversation_count']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Journey info
    st.markdown("#### Customer Journey")
    st.markdown(f"""
    - **Stage:** {customer['stage']}
    - **Source:** {customer['source']}
    - **Avg Response:** {customer['avg_response_time']}
    - **Campaigns Opened:** {customer['campaigns_opened']}
    """)
    
    # Tags
    st.markdown("#### Tags")
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in customer['tags']])
    st.markdown(tags_html, unsafe_allow_html=True)
    
    # Behavioral insights
    st.markdown("#### Behavioral Insights")
    st.info(customer['behavior'])
    
    # Smart actions
    st.markdown("#### ⚡ Smart Actions")
    for action in smart_actions[st.session_state.selected_customer]:
        st.markdown(f"""
        <div class="action-card">
            <div style="font-weight: 600; margin-bottom: 0.25rem;">{action['icon']} {action['label']}</div>
            <div style="font-size: 0.85rem; color: #4b5563; margin-bottom: 0.5rem;">{action['desc']}</div>
            <div style="font-size: 0.75rem; color: #16a34a; font-weight: 600;">💡 {action['impact']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Impact metrics
    st.markdown(f"#### 📈 {impact_metrics[st.session_state.selected_customer]['title']}")
    for metric in impact_metrics[st.session_state.selected_customer]['metrics']:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"""
            <div style="font-size: 0.85rem; font-weight: 600;">{metric['label']}</div>
            <div style="font-size: 0.75rem; color: #6b7280;">{metric['context']}</div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div style="font-size: 1.5rem; font-weight: bold; color: #16a34a; text-align: right;">{metric['value']}</div>
            """, unsafe_allow_html=True)
    
    # Purchase history
    if customer['purchase_history']:
        st.markdown("#### 🛍️ Purchase History")
        for item in customer['purchase_history']:
            st.markdown(f"📦 {item}")
    
    # Active cart
    if customer['cart_value'] > 0:
        st.markdown("#### 🛒 Active Cart")
        st.warning(f"**${customer['cart_value']}** in cart")
        if st.button("📤 Send Cart Recovery Message", key="cart_recovery"):
            st.success("Cart recovery message sent!")
