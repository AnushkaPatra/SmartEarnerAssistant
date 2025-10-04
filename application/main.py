import tkinter as tk
from ui.colors import COLORS

def create_description_screen(root, show_role_selection):
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

    return desc_frame
import tkinter as tk
from ui.utils import create_hover_button
from ui.colors import COLORS

def create_role_selection_screen(root, select_role):
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

    return role_frame
import tkinter as tk
from tkinter import ttk
from ui.colors import COLORS
from ui.utils import create_metric_card, create_action_button
import datetime

# Pass driver_jobs and courier_jobs from main or load from resources
def show_dashboard(dashboard_frame, role, driver_jobs, courier_jobs):
    dashboard_frame.pack(fill="both", expand=True)
    for widget in dashboard_frame.winfo_children():
        widget.destroy()

    # Header
    header = tk.Frame(dashboard_frame, bg=COLORS['bg_secondary'], height=80)
    header.pack(fill="x")
    header.pack_propagate(False)

    header_content = tk.Frame(header, bg=COLORS['bg_secondary'])
    header_content.pack(fill="both", expand=True, padx=60, pady=20)

    tk.Label(header_content, text=f"{role} Dashboard", font=("Segoe UI", 26, "bold"),
             bg=COLORS['bg_secondary'], fg=COLORS['text_primary']).pack(side="left")

    time_frame = tk.Frame(header_content, bg=COLORS['bg_secondary'])
    time_frame.pack(side="right")

    tk.Label(time_frame, text=datetime.datetime.now().strftime("%H:%M"), font=("Segoe UI", 20, "bold"),
             bg=COLORS['bg_secondary'], fg=COLORS['accent']).pack(side="left", padx=(0,10))
    tk.Label(time_frame, text="Online", font=("Segoe UI", 12),
             bg=COLORS['bg_secondary'], fg=COLORS['success']).pack(side="left")

    # Content
    content = tk.Frame(dashboard_frame, bg=COLORS['bg_primary'])
    content.pack(fill="both", expand=True, padx=60, pady=20)

    # Metrics
    metrics_frame = tk.Frame(content, bg=COLORS['bg_primary'])
    metrics_frame.pack(fill="x", pady=(0, 20))

    if role == "Driver":
        create_metric_card(metrics_frame, "Today's Earnings", "€156.80", "+12% vs yesterday")
        create_metric_card(metrics_frame, "Trips Completed", "18", "2 hours online")
        create_metric_card(metrics_frame, "Avg Rating", "4.9★", "Last 50 trips")
        create_metric_card(metrics_frame, "Next Bonus", "2 trips", "Unlock €15")
    else:
        create_metric_card(metrics_frame, "Today's Earnings", "€89.40", "+8% vs yesterday")
        create_metric_card(metrics_frame, "Deliveries", "24", "3 hours online")
        create_metric_card(metrics_frame, "Avg Rating", "4.8★", "Last 50 orders")
        create_metric_card(metrics_frame, "Next Bonus", "4 orders", "Unlock €12")

    # Jobs Table & Buttons (similar to original, pass driver_jobs/courier_jobs)
    # Can be further modularized if needed

    return dashboard_frame
import tkinter as tk
from ui.colors import COLORS
from ui.utils import create_action_button
from ui.description import create_description_screen
from ui.role_selection import create_role_selection_screen
from ui.dashboard import show_dashboard

# Sample data (can be loaded from resources CSVs later)
driver_jobs = [...]
courier_jobs = [...]

root = tk.Tk()
root.title("Smart Earner Assistant")
root.configure(bg=COLORS['bg_primary'])
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda e: root.quit())

# Callbacks
def show_role_selection():
    desc_frame.pack_forget()
    role_frame.pack(fill="both", expand=True)

def select_role(role):
    # Role confirmation popup (can also be moved to ui/role_popup.py)
    from tkinter import Toplevel, Label, Button, Frame
    popup = Toplevel(root)
    popup.configure(bg=COLORS['bg_secondary'])
    popup.geometry("500x300")
    popup.resizable(False, False)
    popup.transient(root)
    popup.grab_set()

    frame = Frame(popup, bg=COLORS['bg_secondary'])
    frame.pack(fill="both", expand=True, padx=40, pady=40)

    Label(frame, text="✓ Role Confirmed", font=("Segoe UI", 13),
          bg=COLORS['bg_secondary'], fg=COLORS['success']).pack(pady=(0,10))
    Label(frame, text=role, font=("Segoe UI", 32, "bold"),
          bg=COLORS['bg_secondary'], fg=COLORS['text_primary']).pack(pady=10)
    Label(frame, text="Preparing your personalized dashboard...",
          font=("Segoe UI", 12), bg=COLORS['bg_secondary'], fg=COLORS['text_secondary']).pack(pady=(0,30))

    def open_dashboard():
        popup.destroy()
        role_frame.pack_forget()
        show_dashboard(dashboard_frame, role, driver_jobs, courier_jobs)

    Button(frame, text="Continue →", command=open_dashboard,
           font=("Segoe UI", 14, "bold"),
           bg=COLORS['accent'], fg=COLORS['text_primary'],
           activebackground=COLORS['accent_hover'],
           bd=0, relief="flat", cursor="hand2").pack(fill="x", ipady=8)

# UI
desc_frame = create_description_screen(root, show_role_selection)
role_frame = create_role_selection_screen(root, select_role)
dashboard_frame = tk.Frame(root, bg=COLORS['bg_primary'])

# Footer
footer = tk.Label(root, text="© 2025 Smart Earner Assistant  •  Built for Junction Hackathon",
                  bg=COLORS['bg_primary'], fg=COLORS['text_muted'],
                  font=("Segoe UI", 10))
footer.pack(side="bottom", pady=15)

root.mainloop()