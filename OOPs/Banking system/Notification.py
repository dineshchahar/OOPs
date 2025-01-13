class NotificationSystem:
    """
        Handles notification for account operations.
        Adheres to Dependency Inversion Principles (DIP) by decoupling notification form core.
            
    """
    @staticmethod
    def send_notification(message):
        print(f"Notification: {message}")
        