import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime

# ---------------- CONFIGURATION ---------------- #
COLORS = {
    'bg_primary': '#0A0A0A',
    'bg_secondary': '#1A1A1A',
    'bg_card': '#252525',
    'accent': '#00B67A',
    'accent_hover': '#009461',
    'text_primary': '#FFFFFF',
    'text_secondary': '#B3B3B3',
    'text_muted': '#666666',
    'warning': '#FFA500',
    'success': '#00B67A',
    'info': '#3B82F6'
}

# Sample dynamic job data
driver_jobs = [
    {"pickup": "Helsinki Central", "dropoff": "Espoo Mall", "distance": "12 km", "fare": "€18.50", "weather": "☁️ Cloudy", "score": 85},
    {"pickup": "Airport", "dropoff": "City Center", "distance": "18 km", "fare": "€28.00", "weather": "🌧️ Rain", "score": 92},
    {"pickup": "University", "dropoff": "Harbor", "distance": "8 km", "fare": "€14.20", "weather": "☀️ Clear", "score": 78},
]

courier_jobs = [
    {"restaurant": "Pizza Palace", "address": "Mannerheimintie 5", "distance": "3.2 km", "fee": "€8.50", "weather": "☁️ Cloudy", "score": 88},
    {"restaurant": "Sushi Station", "address": "Aleksanterinkatu 12", "distance": "1.8 km", "fee": "€6.20", "weather": "🌧️ Rain", "score": 95},
    {"restaurant": "Burger Hub", "address": "Kamppi Center", "distance": "4.5 km", "fee": "€9.80", "weather": "☀️ Clear", "score": 82},
]

# ---------------- UTILITY FUNCTIONS ---------------- #
def get_current_time():
    return datetime.datetime.now().strftime("%H:%M")

def create_metric_card(parent, title, value, subtitle=""):
    """Create a professional metric card."""
    card = tk.Frame(parent, bg=COLORS['bg_card'], highlightbackground=COLORS['text_muted'], highlightthickness=1)
    card.pack(side="left", padx=10, fill="both", expand=True)
    
    tk.Label(card, text=title, font=("Segoe UI", 11), 
             bg=COLORS['bg_card'], fg=COLORS['text_muted']).pack(pady=(15, 5))
    
    tk.Label(card, text=value, font=("Segoe UI", 24, "bold"),
             bg=COLORS['bg_card'], fg=COLORS['text_primary']).pack()
    
    if subtitle:
        tk.Label(card, text=subtitle, font=("Segoe UI", 10),
                 bg=COLORS['bg_card'], fg=COLORS['text_secondary']).pack(pady=(5, 15))
    else:
        tk.Label(card, text="", bg=COLORS['bg_card']).pack(pady=(5, 15))
    
    return card

def create_action_button(parent, text, command, color=None):
    """Create a professional action button."""
    bg_color = color if color else COLORS['accent']
    btn = tk.Button(parent, text=text, command=command,
                    bg=bg_color, fg=COLORS['text_primary'],
                    font=("Segoe UI", 11, "bold"),
                    bd=0, relief="flat", padx=20, pady=10, cursor="hand2")
    return btn

# ---------------- MAIN FUNCTIONS ---------------- #
def show_role_selection():
    desc_frame.pack_forget()
    role_frame.pack(fill="both", expand=True)

def select_role(role):
    """Role confirmation popup."""
    popup = tk.Toplevel(root)
    popup.configure(bg=COLORS['bg_secondary'])
    popup.geometry("500x300")
    popup.resizable(False, False)
    popup.transient(root)
    popup.grab_set()

    # Center popup
    popup.update_idletasks()
    x = (popup.winfo_screenwidth() // 2) - (500 // 2)
    y = (popup.winfo_screenheight() // 2) - (300 // 2)
    popup.geometry(f"500x300+{x}+{y}")

    frame = tk.Frame(popup, bg=COLORS['bg_secondary'])
    frame.pack(fill="both", expand=True, padx=40, pady=40)

    tk.Label(frame, text="✓ Role Confirmed", font=("Segoe UI", 13),
             bg=COLORS['bg_secondary'], fg=COLORS['success']).pack(pady=(0,10))

    tk.Label(frame, text=role, font=("Segoe UI", 32, "bold"),
             bg=COLORS['bg_secondary'], fg=COLORS['text_primary']).pack(pady=10)

    tk.Label(frame, text="Preparing your personalized dashboard...",
             font=("Segoe UI", 12), bg=COLORS['bg_secondary'], fg=COLORS['text_secondary']).pack(pady=(0,30))

    def open_dashboard():
        popup.destroy()
        role_frame.pack_forget()
        show_dashboard(role)

    continue_btn = tk.Button(frame, text="Continue →", command=open_dashboard,
              font=("Segoe UI", 14, "bold"),
              bg=COLORS['accent'], fg=COLORS['text_primary'],
              activebackground=COLORS['accent_hover'],
              bd=0, relief="flat", cursor="hand2")
    continue_btn.pack(fill="x", ipady=8)

def create_hover_button(parent, text, command, icon=""):
    btn = tk.Button(parent, text=f"{icon} {text}".strip(), command=command,
                    bg=COLORS['bg_card'], fg=COLORS['text_primary'],
                    font=("Segoe UI", 16, "bold"),
                    activebackground=COLORS['accent'],
                    bd=0, relief="flat", padx=50, pady=18, cursor="hand2")
    btn.bind("<Enter>", lambda e: btn.config(bg=COLORS['accent']))
    btn.bind("<Leave>", lambda e: btn.config(bg=COLORS['bg_card']))
    return btn

def show_dashboard(role):
    """Dynamic dashboard for Driver or Courier."""
    dashboard_frame.pack(fill="both", expand=True)

    for widget in dashboard_frame.winfo_children():
        widget.destroy()

    # Header with role and time
    header = tk.Frame(dashboard_frame, bg=COLORS['bg_secondary'], height=80)
    header.pack(fill="x")
    header.pack_propagate(False)
    
    header_content = tk.Frame(header, bg=COLORS['bg_secondary'])
    header_content.pack(fill="both", expand=True, padx=60, pady=20)
    
    tk.Label(header_content, text=f"{role} Dashboard", font=("Segoe UI", 26, "bold"),
             bg=COLORS['bg_secondary'], fg=COLORS['text_primary']).pack(side="left")
    
    time_frame = tk.Frame(header_content, bg=COLORS['bg_secondary'])
    time_frame.pack(side="right")
    
    tk.Label(time_frame, text=get_current_time(), font=("Segoe UI", 20, "bold"),
             bg=COLORS['bg_secondary'], fg=COLORS['accent']).pack(side="left", padx=(0,10))
    
    tk.Label(time_frame, text="Online", font=("Segoe UI", 12),
             bg=COLORS['bg_secondary'], fg=COLORS['success']).pack(side="left")

    # Main content area
    content = tk.Frame(dashboard_frame, bg=COLORS['bg_primary'])
    content.pack(fill="both", expand=True, padx=60, pady=20)

    # Metrics row
    metrics_frame = tk.Frame(content, bg=COLORS['bg_primary'])
    metrics_frame.pack(fill="x", pady=(0, 20))

    if role == "Driver":
        create_metric_card(metrics_frame, "Today's Earnings", "€156.80", "+12% vs yesterday")
        create_metric_card(metrics_frame, "Trips Completed", "18", "2 hours online")
        create_metric_card(metrics_frame, "Avg Rating", "4.9★", "Last 50 trips")
        create_metric_card(metrics_frame, "Next Bonus", "2 trips", "Unlock €15")
    else:  # Courier
        create_metric_card(metrics_frame, "Today's Earnings", "€89.40", "+8% vs yesterday")
        create_metric_card(metrics_frame, "Deliveries", "24", "3 hours online")
        create_metric_card(metrics_frame, "Avg Rating", "4.8★", "Last 50 orders")
        create_metric_card(metrics_frame, "Next Bonus", "4 orders", "Unlock €12")

    # Jobs section
    jobs_section = tk.Frame(content, bg=COLORS['bg_secondary'])
    jobs_section.pack(fill="both", expand=True)

    # Jobs header
    jobs_header = tk.Frame(jobs_section, bg=COLORS['bg_secondary'])
    jobs_header.pack(fill="x", padx=30, pady=(20, 10))
    
    tk.Label(jobs_header, text="🎯 Recommended Jobs" if role == "Driver" else "🎯 Top Delivery Orders",
             font=("Segoe UI", 18, "bold"),
             bg=COLORS['bg_secondary'], fg=COLORS['text_primary']).pack(side="left")
    
    refresh_btn = create_action_button(jobs_header, "↻ Refresh", lambda: show_dashboard(role))
    refresh_btn.pack(side="right")

    # Jobs table with custom styling
    table_frame = tk.Frame(jobs_section, bg=COLORS['bg_secondary'])
    table_frame.pack(fill="both", expand=True, padx=30, pady=(0, 20))

    # Style configuration for treeview
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Custom.Treeview",
                    background=COLORS['bg_card'],
                    foreground=COLORS['text_primary'],
                    fieldbackground=COLORS['bg_card'],
                    borderwidth=0,
                    font=("Segoe UI", 11))
    style.configure("Custom.Treeview.Heading",
                    background=COLORS['bg_secondary'],
                    foreground=COLORS['text_secondary'],
                    borderwidth=0,
                    font=("Segoe UI", 12, "bold"))
    style.map("Custom.Treeview",
              background=[("selected", COLORS['accent'])],
              foreground=[("selected", COLORS['text_primary'])])

    if role == "Driver":
        columns = ("Pickup", "Dropoff", "Distance", "Fare", "Weather", "Score")
        tree = ttk.Treeview(table_frame, columns=columns, show="headings", 
                           height=8, style="Custom.Treeview")
        
        col_widths = {"Pickup": 200, "Dropoff": 200, "Distance": 100, 
                     "Fare": 100, "Weather": 120, "Score": 100}
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="w" if col in ["Pickup", "Dropoff"] else "center", 
                       width=col_widths[col])
        
        for job in driver_jobs:
            score_tag = "high" if job["score"] >= 85 else "medium"
            tree.insert("", "end", values=(
                job["pickup"], job["dropoff"], job["distance"], 
                job["fare"], job["weather"], f"{job['score']}%"
            ), tags=(score_tag,))
        
        tree.tag_configure("high", foreground=COLORS['success'])
        tree.tag_configure("medium", foreground=COLORS['warning'])
        
    else:  # Courier
        columns = ("Restaurant", "Delivery Address", "Distance", "Fee", "Weather", "Score")
        tree = ttk.Treeview(table_frame, columns=columns, show="headings",
                           height=8, style="Custom.Treeview")
        
        col_widths = {"Restaurant": 200, "Delivery Address": 220, "Distance": 100,
                     "Fee": 100, "Weather": 120, "Score": 100}
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="w" if col in ["Restaurant", "Delivery Address"] else "center",
                       width=col_widths[col])
        
        for job in courier_jobs:
            score_tag = "high" if job["score"] >= 85 else "medium"
            tree.insert("", "end", values=(
                job["restaurant"], job["address"], job["distance"],
                job["fee"], job["weather"], f"{job['score']}%"
            ), tags=(score_tag,))
        
        tree.tag_configure("high", foreground=COLORS['success'])
        tree.tag_configure("medium", foreground=COLORS['warning'])

    tree.pack(fill="both", expand=True)

    # Action buttons
    action_frame = tk.Frame(jobs_section, bg=COLORS['bg_secondary'])
    action_frame.pack(fill="x", padx=30, pady=(10, 20))

    if role == "Driver":
        create_action_button(action_frame, "🗺️ View Heat Map", lambda: None).pack(side="left", padx=(0, 10))
        create_action_button(action_frame, "📊 Earnings Forecast", lambda: None).pack(side="left", padx=(0, 10))
        create_action_button(action_frame, "⚙️ Preferences", lambda: None).pack(side="left")
        
        # Go offline button on right
        offline_btn = create_action_button(action_frame, "● Go Offline", lambda: None, COLORS['text_muted'])
        offline_btn.pack(side="right")
    else:  # Courier
        create_action_button(action_frame, "🗺️ Hotspot Map", lambda: None).pack(side="left", padx=(0, 10))
        create_action_button(action_frame, "📊 Peak Hours", lambda: None).pack(side="left", padx=(0, 10))
        create_action_button(action_frame, "⚙️ Settings", lambda: None).pack(side="left")
        
        # Go offline button on right
        offline_btn = create_action_button(action_frame, "● Go Offline", lambda: None, COLORS['text_muted'])
        offline_btn.pack(side="right")

    # Quick tips section
    tips_frame = tk.Frame(content, bg=COLORS['bg_card'], highlightbackground=COLORS['text_muted'], highlightthickness=1)
    tips_frame.pack(fill="x", pady=(20, 0))
    
    tk.Label(tips_frame, text="💡 Smart Tip", font=("Segoe UI", 12, "bold"),
             bg=COLORS['bg_card'], fg=COLORS['info']).pack(anchor="w", padx=20, pady=(15, 5))
    
    if role == "Driver":
        tip_text = "Peak demand expected in City Center between 17:00-19:00. Position yourself near transit hubs for +23% earnings."
    else:
        tip_text = "Lunch rush starting soon! Restaurant clusters in Kamppi area show high order volume. Expected +18% earnings."
    
    tk.Label(tips_frame, text=tip_text, font=("Segoe UI", 11),
             bg=COLORS['bg_card'], fg=COLORS['text_secondary'],
             wraplength=1000, justify="left").pack(anchor="w", padx=20, pady=(0, 15))

# ----------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("Smart Earner Assistant")
root.configure(bg=COLORS['bg_primary'])
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda e: root.quit())

# ----------------- DESCRIPTION SCREEN ---------------- #
desc_frame = tk.Frame(root, bg=COLORS['bg_primary'])
desc_frame.pack(fill="both", expand=True, padx=120, pady=40)

desc_card = tk.Frame(desc_frame, bg=COLORS['bg_secondary'])
desc_card.pack(fill="both", expand=True)

desc_content = tk.Frame(desc_card, bg=COLORS['bg_secondary'])
desc_content.pack(fill="both", expand=True, padx=60, pady=50)

tk.Label(desc_content, text="Smart Earner Assistant",
         font=("Segoe UI", 36, "bold"), bg=COLORS['bg_secondary'],
         fg=COLORS['text_primary']).pack(pady=(0,10))

tk.Label(desc_content, text="Professional Digital Co-Pilot for Uber Earners",
         font=("Segoe UI", 15), bg=COLORS['bg_secondary'],
         fg=COLORS['text_secondary']).pack(pady=(0,30))

# Developer names
tk.Label(desc_content, text="Anushka Patra  •  Tanisha Doshi  •  Nguyen Do",
         font=("Segoe UI", 13, "bold"), bg=COLORS['bg_secondary'], fg=COLORS['accent']).pack(pady=(0,30))

desc_text = (
    "Optimize daily operations, maximize earnings, and enhance well-being through "
    "predictive analytics and intelligent recommendations.\n\n"
    "Key Capabilities:\n"
    "• Real-time trip optimization and demand forecasting\n"
    "• Personalized efficiency and earnings guidance\n"
    "• Safety notifications and wellness monitoring\n"
    "• AI-powered behavioral insights and earnings strategies\n\n"
    "Work smarter, reduce idle time, and balance productivity with personal well-being."
)

tk.Label(desc_content, text=desc_text, font=("Segoe UI", 13),
         wraplength=900, justify="left",
         bg=COLORS['bg_secondary'], fg=COLORS['text_secondary']).pack(pady=(0,40))

start_btn = tk.Button(desc_content, text="Get Started →", command=show_role_selection,
          font=("Segoe UI", 15, "bold"),
          bg=COLORS['accent'], fg=COLORS['text_primary'],
          activebackground=COLORS['accent_hover'],
          bd=0, relief="flat", cursor="hand2")
start_btn.pack(fill="x", ipady=10)

# ----------------- ROLE SELECTION SCREEN ---------------- #
role_frame = tk.Frame(root, bg=COLORS['bg_primary'])

role_content = tk.Frame(role_frame, bg=COLORS['bg_primary'])
role_content.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(role_content, text="Select Your Role",
         bg=COLORS['bg_primary'], fg=COLORS['text_primary'],
         font=("Segoe UI", 32, "bold")).pack(pady=(0, 10))

tk.Label(role_content, text="Choose how you earn with Uber",
         bg=COLORS['bg_primary'], fg=COLORS['text_secondary'],
         font=("Segoe UI", 14)).pack(pady=(0, 50))

driver_btn = create_hover_button(role_content, "Driver", lambda: select_role("Driver"), "🚗")
driver_btn.pack(pady=15)

courier_btn = create_hover_button(role_content, "Courier", lambda: select_role("Courier"), "🛵")
courier_btn.pack(pady=15)

# ----------------- DASHBOARD FRAME ---------------- #
dashboard_frame = tk.Frame(root, bg=COLORS['bg_primary'])

# ----------------- FOOTER ---------------- #
footer = tk.Label(root, text="© 2025 Smart Earner Assistant  •  Built for Junction Hackathon",
                  bg=COLORS['bg_primary'], fg=COLORS['text_muted'],
                  font=("Segoe UI", 10))
footer.pack(side="bottom", pady=15)

# ----------------- RUN ---------------- #
root.mainloop()