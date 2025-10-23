import React, { useState } from 'react';
import { MessageSquare, TrendingUp, Clock, ShoppingCart, AlertCircle, Zap, Users, DollarSign, Bell, X, Send, ChevronRight, Star, Package, CreditCard } from 'lucide-react';

export default function WatiProfilePrototype() {
  const [activeView, setActiveView] = useState('inbox');
  const [selectedCustomer, setSelectedCustomer] = useState(null);
  const [showAlert, setShowAlert] = useState(true);
  const [showSuggestion, setShowSuggestion] = useState(true);
  const [messages, setMessages] = useState([
    { id: 1, text: "Hi, I'm interested in your Premium plan", sender: 'customer', time: '2 days ago' },
    { id: 2, text: "I saw the pricing but wanted to know about integrations", sender: 'customer', time: '2 days ago' },
    { id: 3, text: "Great! Our Premium plan includes unlimited integrations with Shopify, Salesforce, and 50+ other platforms. Would you like a demo?", sender: 'agent', time: '2 days ago' },
  ]);

  const customers = [
    {
      id: 1,
      name: 'Sarah Chen',
      phone: '+1 (555) 234-5678',
      lastMessage: "I saw the pricing but wanted to know...",
      time: '2d ago',
      unread: 1,
      leadScore: 85,
      stage: 'Hot Lead',
      value: '$0',
      source: 'Instagram Ad',
      behavior: 'Viewed pricing 3x, Clicked integrations link',
      sentiment: 'positive',
      tags: ['Premium Interest', 'High Intent'],
      engagementScore: 78,
      lastActive: '2 days ago',
      timezone: 'PST',
      campaignsOpened: 2,
      conversationCount: 4,
      avgResponseTime: '5 min',
      purchaseHistory: [],
      cartValue: 0,
      priority: 'high'
    },
    {
      id: 2,
      name: 'Marcus Johnson',
      phone: '+1 (555) 876-5432',
      lastMessage: "Thanks for the help!",
      time: '1h ago',
      unread: 0,
      leadScore: 45,
      stage: 'Customer',
      value: '$5,240',
      source: 'Website',
      behavior: 'Order placed 30 days ago, No recent activity',
      sentiment: 'neutral',
      tags: ['VIP', 'Churn Risk'],
      engagementScore: 32,
      lastActive: '30 days ago',
      timezone: 'EST',
      campaignsOpened: 8,
      conversationCount: 12,
      avgResponseTime: '3 min',
      purchaseHistory: ['Product A', 'Product B', 'Premium Service'],
      cartValue: 0,
      priority: 'medium'
    },
    {
      id: 3,
      name: 'Emma Rodriguez',
      phone: '+1 (555) 345-7890',
      lastMessage: "When will my order ship?",
      time: '15m ago',
      unread: 1,
      leadScore: 92,
      stage: 'Customer',
      value: '$1,850',
      source: 'Referral',
      behavior: 'Active order, 2 prev shipping delays',
      sentiment: 'concerned',
      tags: ['VIP', 'Support Priority'],
      engagementScore: 88,
      lastActive: '15 min ago',
      timezone: 'CST',
      campaignsOpened: 5,
      conversationCount: 8,
      avgResponseTime: '2 min',
      purchaseHistory: ['Product C', 'Product D'],
      cartValue: 450,
      priority: 'high'
    }
  ];

  const intelligentActions = {
    1: [
      { icon: TrendingUp, label: 'Send Personalized Offer', desc: '10% discount for Premium - 85% conv. probability', impact: '+$2,400 potential ARR' },
      { icon: Clock, label: 'Schedule Demo Call', desc: 'Best time: 7-9 PM PST (peak engagement)', impact: '+65% show rate' },
      { icon: Zap, label: 'Auto-send Integration Guide', desc: 'Addresses their main question', impact: '+40% response rate' }
    ],
    2: [
      { icon: AlertCircle, label: 'Re-engagement Campaign', desc: 'Win-back offer based on past purchases', impact: 'Reduce churn by 35%' },
      { icon: Star, label: 'Request Product Review', desc: 'Satisfied customer, good timing', impact: '+1 review, boost SEO' },
      { icon: DollarSign, label: 'Upsell Opportunity', desc: 'Cross-sell Product E (high affinity)', impact: '+$850 avg order' }
    ],
    3: [
      { icon: Package, label: 'Priority Shipping Update', desc: 'VIP customer with shipping history', impact: 'Prevent escalation' },
      { icon: AlertCircle, label: 'Proactive Apology + Credit', desc: 'Past issues detected, high value customer', impact: 'Retain $5k+ LTV' },
      { icon: MessageSquare, label: 'Route to Senior Support', desc: 'Complex case, VIP treatment needed', impact: '-50% resolution time' }
    ]
  };

  const impactMetrics = {
    1: {
      title: 'Lead Conversion Impact',
      metrics: [
        { label: 'Conversion Rate Lift', value: '+42%', context: 'vs generic outreach' },
        { label: 'Response Time', value: '5 min', context: 'avg for this customer' },
        { label: 'Deal Value', value: '$2,880', context: 'Premium annual plan' },
        { label: 'Win Probability', value: '85%', context: 'based on behavior' }
      ]
    },
    2: {
      title: 'Churn Prevention Impact',
      metrics: [
        { label: 'Churn Risk', value: '68%', context: '30 days inactive' },
        { label: 'LTV at Risk', value: '$5,240', context: 'total spend to date' },
        { label: 'Recovery Rate', value: '35%', context: 'with personalized campaign' },
        { label: 'ROI', value: '12.5x', context: 'campaign cost vs recovery' }
      ]
    },
    3: {
      title: 'Support Efficiency Impact',
      metrics: [
        { label: 'Context Load Time', value: '0 sec', context: 'instant full history' },
        { label: 'Resolution Time', value: '-45%', context: 'vs no profile data' },
        { label: 'Customer Satisfaction', value: '+28%', context: 'with proactive support' },
        { label: 'Retention Impact', value: '92%', context: 'VIP retention rate' }
      ]
    }
  };

  return (
    <div className="flex h-screen bg-gray-50 font-sans">
      {/* Sidebar */}
      <div className="w-64 bg-white border-r border-gray-200 flex flex-col">
        <div className="p-4 border-b border-gray-200">
          <div className="flex items-center gap-2">
            <MessageSquare className="text-green-600" size={24} />
            <span className="font-bold text-xl">Wati</span>
          </div>
        </div>
        
        <nav className="flex-1 p-4">
          <button 
            onClick={() => setActiveView('inbox')}
            className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg mb-2 ${activeView === 'inbox' ? 'bg-green-50 text-green-700' : 'hover:bg-gray-50'}`}
          >
            <MessageSquare size={20} />
            <span>Inbox</span>
            <span className="ml-auto bg-green-600 text-white text-xs px-2 py-1 rounded-full">2</span>
          </button>
          
          <button 
            onClick={() => setActiveView('campaigns')}
            className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg mb-2 ${activeView === 'campaigns' ? 'bg-green-50 text-green-700' : 'hover:bg-gray-50'}`}
          >
            <Users size={20} />
            <span>Campaigns</span>
          </button>
          
          <button 
            onClick={() => setActiveView('analytics')}
            className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg mb-2 ${activeView === 'analytics' ? 'bg-green-50 text-green-700' : 'hover:bg-gray-50'}`}
          >
            <TrendingUp size={20} />
            <span>Analytics</span>
          </button>
        </nav>

        <div className="p-4 border-t border-gray-200">
          <div className="text-xs text-gray-500 mb-2">AI-Powered Insights</div>
          <div className="bg-gradient-to-r from-purple-50 to-blue-50 p-3 rounded-lg">
            <div className="flex items-center gap-2 text-sm font-medium text-purple-900 mb-1">
              <Zap size={16} className="text-purple-600" />
              Smart Actions Ready
            </div>
            <div className="text-xs text-purple-700">3 high-impact opportunities</div>
          </div>
        </div>
      </div>

      {/* Customer List */}
      <div className="w-80 bg-white border-r border-gray-200 flex flex-col">
        <div className="p-4 border-b border-gray-200">
          <input 
            type="text" 
            placeholder="Search conversations..." 
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          />
        </div>

        <div className="flex-1 overflow-y-auto">
          {customers.map(customer => (
            <button
              key={customer.id}
              onClick={() => setSelectedCustomer(customer)}
              className={`w-full p-4 border-b border-gray-100 hover:bg-gray-50 text-left ${selectedCustomer?.id === customer.id ? 'bg-green-50' : ''}`}
            >
              <div className="flex items-start justify-between mb-2">
                <div className="flex items-center gap-2">
                  <div className="w-10 h-10 bg-gradient-to-br from-green-400 to-blue-500 rounded-full flex items-center justify-center text-white font-semibold">
                    {customer.name.split(' ').map(n => n[0]).join('')}
                  </div>
                  <div>
                    <div className="font-semibold text-sm">{customer.name}</div>
                    <div className="text-xs text-gray-500">{customer.phone}</div>
                  </div>
                </div>
                {customer.unread > 0 && (
                  <span className="bg-green-600 text-white text-xs px-2 py-1 rounded-full">{customer.unread}</span>
                )}
              </div>
              
              <div className="flex items-center gap-2 mb-2">
                <span className={`text-xs px-2 py-1 rounded-full ${
                  customer.priority === 'high' ? 'bg-red-100 text-red-700' : 'bg-gray-100 text-gray-700'
                }`}>
                  {customer.stage}
                </span>
                <span className="text-xs text-gray-500">Score: {customer.leadScore}</span>
              </div>
              
              <div className="text-sm text-gray-600 truncate">{customer.lastMessage}</div>
              <div className="text-xs text-gray-400 mt-1">{customer.time}</div>
            </button>
          ))}
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col">
        {selectedCustomer ? (
          <>
            {/* Chat Header */}
            <div className="bg-white border-b border-gray-200 p-4">
              <div className="flex items-center justify-between">
                <div>
                  <h2 className="text-lg font-semibold">{selectedCustomer.name}</h2>
                  <div className="flex items-center gap-2 text-sm text-gray-500">
                    <span>{selectedCustomer.phone}</span>
                    <span>•</span>
                    <span>{selectedCustomer.timezone}</span>
                    <span>•</span>
                    <span className="text-green-600">Last active: {selectedCustomer.lastActive}</span>
                  </div>
                </div>
                <button 
                  onClick={() => setSelectedCustomer(null)}
                  className="text-gray-400 hover:text-gray-600"
                >
                  <X size={20} />
                </button>
              </div>
            </div>

            {/* Smart Alert Banner */}
            {showAlert && selectedCustomer.id === 1 && (
              <div className="bg-gradient-to-r from-orange-50 to-red-50 border-b border-orange-200 p-4">
                <div className="flex items-start gap-3">
                  <Zap className="text-orange-600 mt-1" size={20} />
                  <div className="flex-1">
                    <div className="font-semibold text-orange-900 mb-1">🔥 Hot Lead Alert - High Conversion Probability (85%)</div>
                    <div className="text-sm text-orange-800 mb-2">
                      Sarah has viewed pricing 3x and asked about integrations. This matches our "Ready to Buy" pattern. 
                      <span className="font-semibold"> Suggested action: Send personalized offer now.</span>
                    </div>
                    <div className="flex gap-2">
                      <button className="text-xs bg-orange-600 text-white px-3 py-1 rounded hover:bg-orange-700">
                        Send Offer (1-click)
                      </button>
                      <button className="text-xs bg-white text-orange-600 border border-orange-600 px-3 py-1 rounded hover:bg-orange-50">
                        View Full Profile
                      </button>
                    </div>
                  </div>
                  <button onClick={() => setShowAlert(false)} className="text-orange-400 hover:text-orange-600">
                    <X size={18} />
                  </button>
                </div>
              </div>
            )}

            {showAlert && selectedCustomer.id === 3 && (
              <div className="bg-gradient-to-r from-purple-50 to-blue-50 border-b border-purple-200 p-4">
                <div className="flex items-start gap-3">
                  <AlertCircle className="text-purple-600 mt-1" size={20} />
                  <div className="flex-1">
                    <div className="font-semibold text-purple-900 mb-1">⚠️ VIP Customer - Previous Shipping Issues Detected</div>
                    <div className="text-sm text-purple-800 mb-2">
                      Emma has experienced 2 shipping delays before (LTV: $1,850). Current order status: In transit. 
                      <span className="font-semibold"> Suggested: Priority handling + proactive update.</span>
                    </div>
                    <div className="flex gap-2">
                      <button className="text-xs bg-purple-600 text-white px-3 py-1 rounded hover:bg-purple-700">
                        Send Priority Update
                      </button>
                      <button className="text-xs bg-white text-purple-600 border border-purple-600 px-3 py-1 rounded hover:bg-purple-50">
                        Escalate to Senior Support
                      </button>
                    </div>
                  </div>
                  <button onClick={() => setShowAlert(false)} className="text-purple-400 hover:text-purple-600">
                    <X size={18} />
                  </button>
                </div>
              </div>
            )}

            <div className="flex-1 flex">
              {/* Messages */}
              <div className="flex-1 flex flex-col">
                <div className="flex-1 overflow-y-auto p-6 space-y-4">
                  {messages.map(msg => (
                    <div key={msg.id} className={`flex ${msg.sender === 'agent' ? 'justify-end' : 'justify-start'}`}>
                      <div className={`max-w-md px-4 py-2 rounded-2xl ${
                        msg.sender === 'agent' 
                          ? 'bg-green-600 text-white' 
                          : 'bg-white border border-gray-200'
                      }`}>
                        <div className="text-sm">{msg.text}</div>
                        <div className={`text-xs mt-1 ${msg.sender === 'agent' ? 'text-green-100' : 'text-gray-400'}`}>
                          {msg.time}
                        </div>
                      </div>
                    </div>
                  ))}

                  {/* AI Suggestion */}
                  {showSuggestion && selectedCustomer.id === 1 && (
                    <div className="bg-gradient-to-r from-blue-50 to-purple-50 border-l-4 border-blue-500 p-4 rounded-lg">
                      <div className="flex items-start gap-3">
                        <Zap className="text-blue-600 mt-1" size={18} />
                        <div className="flex-1">
                          <div className="font-semibold text-blue-900 text-sm mb-2">💡 AI-Suggested Response</div>
                          <div className="bg-white border border-blue-200 p-3 rounded-lg text-sm mb-3">
                            "Hi Sarah! I see you're interested in our Premium plan integrations. Great news - we have native integrations with Shopify, Salesforce, HubSpot, and 50+ other platforms. Plus, I can offer you 10% off your first year if you sign up this week. Would you like me to schedule a quick 15-min demo to show you how it works? 🚀"
                          </div>
                          <div className="flex gap-2">
                            <button 
                              onClick={() => {
                                setMessages([...messages, {
                                  id: messages.length + 1,
                                  text: "Hi Sarah! I see you're interested in our Premium plan integrations. Great news - we have native integrations with Shopify, Salesforce, HubSpot, and 50+ other platforms. Plus, I can offer you 10% off your first year if you sign up this week. Would you like me to schedule a quick 15-min demo? 🚀",
                                  sender: 'agent',
                                  time: 'Just now'
                                }]);
                                setShowSuggestion(false);
                              }}
                              className="text-xs bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700"
                            >
                              Send This Message
                            </button>
                            <button className="text-xs bg-white text-blue-600 border border-blue-600 px-3 py-1 rounded hover:bg-blue-50">
                              Edit First
                            </button>
                            <button 
                              onClick={() => setShowSuggestion(false)}
                              className="text-xs text-gray-500 hover:text-gray-700"
                            >
                              Dismiss
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                  )}
                </div>

                {/* Message Input */}
                <div className="border-t border-gray-200 p-4 bg-white">
                  <div className="flex items-center gap-2">
                    <input 
                      type="text" 
                      placeholder="Type a message..." 
                      className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                    />
                    <button className="bg-green-600 text-white p-2 rounded-lg hover:bg-green-700">
                      <Send size={20} />
                    </button>
                  </div>
                </div>
              </div>

              {/* Customer Profile Sidebar */}
              <div className="w-80 border-l border-gray-200 bg-white overflow-y-auto">
                <div className="p-4">
                  <h3 className="font-semibold text-lg mb-4">Customer Intelligence</h3>
                  
                  {/* Quick Stats */}
                  <div className="grid grid-cols-2 gap-3 mb-6">
                    <div className="bg-gradient-to-br from-green-50 to-emerald-50 p-3 rounded-lg">
                      <div className="text-xs text-gray-600 mb-1">Lead Score</div>
                      <div className="text-2xl font-bold text-green-700">{selectedCustomer.leadScore}</div>
                    </div>
                    <div className="bg-gradient-to-br from-blue-50 to-cyan-50 p-3 rounded-lg">
                      <div className="text-xs text-gray-600 mb-1">Lifetime Value</div>
                      <div className="text-2xl font-bold text-blue-700">{selectedCustomer.value}</div>
                    </div>
                    <div className="bg-gradient-to-br from-purple-50 to-pink-50 p-3 rounded-lg">
                      <div className="text-xs text-gray-600 mb-1">Engagement</div>
                      <div className="text-2xl font-bold text-purple-700">{selectedCustomer.engagementScore}%</div>
                    </div>
                    <div className="bg-gradient-to-br from-orange-50 to-yellow-50 p-3 rounded-lg">
                      <div className="text-xs text-gray-600 mb-1">Conversations</div>
                      <div className="text-2xl font-bold text-orange-700">{selectedCustomer.conversationCount}</div>
                    </div>
                  </div>

                  {/* Journey Info */}
                  <div className="mb-6">
                    <div className="text-sm font-semibold mb-2">Customer Journey</div>
                    <div className="space-y-2">
                      <div className="flex items-center justify-between text-sm">
                        <span className="text-gray-600">Stage:</span>
                        <span className="font-medium">{selectedCustomer.stage}</span>
                      </div>
                      <div className="flex items-center justify-between text-sm">
                        <span className="text-gray-600">Source:</span>
                        <span className="font-medium">{selectedCustomer.source}</span>
                      </div>
                      <div className="flex items-center justify-between text-sm">
                        <span className="text-gray-600">Avg Response:</span>
                        <span className="font-medium">{selectedCustomer.avgResponseTime}</span>
                      </div>
                      <div className="flex items-center justify-between text-sm">
                        <span className="text-gray-600">Campaigns Opened:</span>
                        <span className="font-medium">{selectedCustomer.campaignsOpened}</span>
                      </div>
                    </div>
                  </div>

                  {/* Tags */}
                  <div className="mb-6">
                    <div className="text-sm font-semibold mb-2">Tags</div>
                    <div className="flex flex-wrap gap-2">
                      {selectedCustomer.tags.map((tag, idx) => (
                        <span key={idx} className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded-full">
                          {tag}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* Behavioral Insights */}
                  <div className="mb-6">
                    <div className="text-sm font-semibold mb-2">Behavioral Insights</div>
                    <div className="bg-gray-50 p-3 rounded-lg text-sm text-gray-700">
                      {selectedCustomer.behavior}
                    </div>
                  </div>

                  {/* AI-Recommended Actions */}
                  <div className="mb-6">
                    <div className="text-sm font-semibold mb-3 flex items-center gap-2">
                      <Zap className="text-yellow-500" size={16} />
                      Smart Actions
                    </div>
                    <div className="space-y-3">
                      {intelligentActions[selectedCustomer.id]?.map((action, idx) => {
                        const IconComponent = action.icon;
                        return (
                          <button
                            key={idx}
                            className="w-full text-left bg-gradient-to-r from-blue-50 to-purple-50 hover:from-blue-100 hover:to-purple-100 p-3 rounded-lg border border-blue-200 transition-all"
                          >
                            <div className="flex items-start gap-3">
                              <IconComponent className="text-blue-600 mt-1" size={18} />
                              <div className="flex-1">
                                <div className="font-medium text-sm text-gray-900 mb-1">{action.label}</div>
                                <div className="text-xs text-gray-600 mb-2">{action.desc}</div>
                                <div className="text-xs text-green-600 font-semibold">💡 {action.impact}</div>
                              </div>
                              <ChevronRight className="text-blue-400" size={16} />
                            </div>
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  {/* Impact Metrics */}
                  <div className="bg-gradient-to-br from-green-50 to-blue-50 p-4 rounded-lg border border-green-200">
                    <div className="text-sm font-semibold mb-3 flex items-center gap-2">
                      <TrendingUp className="text-green-600" size={16} />
                      {impactMetrics[selectedCustomer.id]?.title}
                    </div>
                    <div className="space-y-3">
                      {impactMetrics[selectedCustomer.id]?.metrics.map((metric, idx) => (
                        <div key={idx} className="flex items-center justify-between">
                          <div>
                            <div className="text-xs text-gray-600">{metric.label}</div>
                            <div className="text-xs text-gray-500">{metric.context}</div>
                          </div>
                          <div className="text-lg font-bold text-green-700">{metric.value}</div>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Purchase History */}
                  {selectedCustomer.purchaseHistory.length > 0 && (
                    <div className="mt-6">
                      <div className="text-sm font-semibold mb-2 flex items-center gap-2">
                        <ShoppingCart size={16} />
                        Purchase History
                      </div>
                      <div className="space-y-2">
                        {selectedCustomer.purchaseHistory.map((item, idx) => (
                          <div key={idx} className="flex items-center gap-2 text-sm bg-gray-50 p-2 rounded">
                            <Package size={14} className="text-gray-400" />
                            <span className="text-gray-700">{item}</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Active Cart */}
                  {selectedCustomer.cartValue > 0 && (
                    <div className="mt-6">
                      <div className="bg-orange-50 border border-orange-200 p-3 rounded-lg">
                        <div className="text-sm font-semibold mb-1 flex items-center gap-2 text-orange-800">
                          <ShoppingCart size={16} />
                          Active Cart
                        </div>
                        <div className="text-2xl font-bold text-orange-700">${selectedCustomer.cartValue}</div>
                        <button className="mt-2 text-xs bg-orange-600 text-white px-3 py-1 rounded hover:bg-orange-700 w-full">
                          Send Cart Recovery Message
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </div>
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center text-gray-400">
            <div className="text-center">
              <MessageSquare size={64} className="mx-auto mb-4 opacity-50" />
              <p className="text-lg">Select a conversation to start</p>
              <p className="text-sm mt-2">Click on a customer from the list to view their profile</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
