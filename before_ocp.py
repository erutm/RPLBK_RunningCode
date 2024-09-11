class NotificationManager:
    def send_notification(self, notification_type, message):
        if notification_type == "email":
            print(f"Mengirim Notifikasi Email: {message}")
        elif notification_type == "sms":
            print(f"Mengirim Notifikasi SMS: {message}")

manager = NotificationManager()
manager.send_notification("email", "Halo")
manager.send_notification("sms", "Haloo")