// backend/src/services/email_service.py
import resend
from typing import Dict, Any
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Resend with API key
resend.api_key = os.getenv("RESEND_API_KEY")


class EmailService:
    def __init__(self):
        self.from_email = os.getenv("EMAIL_FROM", "onboarding@resend.dev")

    def send_notification(self, to_email: str, subject: str, html_body: str, text_body: str = None) -> Dict[str, Any]:
        """Send an email notification"""
        try:
            params = {
                "from": self.from_email,
                "to": to_email,
                "subject": subject,
                "html": html_body,
            }
            
            if text_body:
                params["text"] = text_body
                
            email = resend.Emails.send(params)
            return {
                "success": True,
                "message_id": email["id"]
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def send_deadline_reminder(self, to_email: str, task_title: str, reminder_time: datetime) -> Dict[str, Any]:
        """Send a deadline reminder notification"""
        subject = f"Task Deadline Reminder: {task_title}"
        html_body = f"""
        <h2>Task Deadline Reminder</h2>
        <p>Your task "{task_title}" has an upcoming deadline.</p>
        <p>Reminder time: {reminder_time.strftime('%Y-%m-%d %H:%M')}</p>
        <p>Please review and complete this task as needed.</p>
        """
        
        return self.send_notification(to_email, subject, html_body)

    def send_task_assignment_notification(self, to_email: str, assigner_name: str, task_title: str) -> Dict[str, Any]:
        """Send a task assignment notification"""
        subject = f"You've been assigned a new task: {task_title}"
        html_body = f"""
        <h2>New Task Assignment</h2>
        <p>{assigner_name} has assigned a new task to you:</p>
        <p><strong>{task_title}</strong></p>
        <p>Please check your task list for more details.</p>
        """
        
        return self.send_notification(to_email, subject, html_body)

    def send_account_alert(self, to_email: str, alert_type: str, message: str) -> Dict[str, Any]:
        """Send an account-related alert"""
        subject = f"Account Alert: {alert_type}"
        html_body = f"""
        <h2>Account Alert</h2>
        <p><strong>Type:</strong> {alert_type}</p>
        <p><strong>Message:</strong> {message}</p>
        <p>If you didn't initiate this action, please contact support immediately.</p>
        """
        
        return self.send_notification(to_email, subject, html_body)