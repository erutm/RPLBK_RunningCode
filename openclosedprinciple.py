from abc import ABC, abstractmethod

# Abstraksi Notifikasi
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Mengirim Notifikasi Email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Mengirim Notifikasi SMS: {message}")

class BrowserNotification(Notification):
    def send(self, message):
        print(f"Mengirim Notifikasi Browser: {message}")

# Kelas untuk Mengelola Notifikasi
class NotificationManager:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send_notification(self, message):
        self.notification.send(message)

email_notification = EmailNotification()
sms_notification = SMSNotification()
broswer_notification = BrowserNotification()

manager = NotificationManager(email_notification)
manager.send_notification("Halo")

manager = NotificationManager(sms_notification)
manager.send_notification("Haloo")

manager = NotificationManager(broswer_notification)
manager.send_notification("Halooo")