from abc import ABC, abstractmethod

# ==============================
# 1️⃣ S - Single Responsibility Principle (SRP)
# ==============================
# Each class has a single responsibility.

class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

class OrderRepository:
    """Handles order storage"""
    def save_order(self, order):
        print(f"Order {order.order_id} saved to the database.")

class OrderProcessor:
    """Handles order processing logic"""
    def process_order(self, order):
        print(f"Processing order {order.order_id} of amount {order.amount}")

# ==============================
# 2️⃣ O - Open/Closed Principle (OCP)
# ==============================
# New invoice types can be added without modifying existing code.

class Invoice(ABC):
    @abstractmethod
    def generate_invoice(self, order):
        pass

class PDFInvoice(Invoice):
    def generate_invoice(self, order):
        print(f"Generating PDF invoice for Order {order.order_id}")

class EmailInvoice(Invoice):
    def generate_invoice(self, order):
        print(f"Sending email invoice for Order {order.order_id}")

# ==============================
# 3️⃣ L - Liskov Substitution Principle (LSP)
# ==============================
# Payment methods should be interchangeable without breaking the code.

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass




class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

class CryptoPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Crypto payment of {amount}")

# ==============================
# 4️⃣ I - Interface Segregation Principle (ISP)
# ==============================
# Clients should not be forced to depend on methods they do not use.

class Notification(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailNotification(Notification):
    def send_notification(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send_notification(self, message):
        print(f"Sending SMS: {message}")

# ==============================
# 5️⃣ D - Dependency Inversion Principle (DIP)
# ==============================
# High-level modules should depend on abstractions, not concrete classes.

class OrderService:
    def __init__(self, order_repo: OrderRepository, payment_processor: PaymentProcessor, notification: Notification):
        self.order_repo = order_repo
        self.payment_processor = payment_processor
        self.notification = notification

    def place_order(self, order):
        self.order_repo.save_order(order)
        self.payment_processor.process_payment(order.amount)
        self.notification.send_notification(f"Order {order.order_id} placed successfully!")

# ==============================
# ✅ Running the SOLID System
# ==============================
if __name__ == "__main__":
    # Creating Order
    order1 = Order(order_id=101, amount=250.75)

    # Choosing dependencies dynamically (Dependency Injection)
    order_repo = OrderRepository()
    payment_processor = CreditCardPayment()  # Swap this with PayPalPayment or CryptoPayment easily
    notification_service = EmailNotification()  # Swap with SMSNotification if needed

    # Using Order Service
    order_service = OrderService(order_repo, payment_processor, notification_service)
    order_service.place_order(order1)


#
#
#  Breakdown of SOLID Principles Applied
# 1️⃣ SRP (Single Responsibility Principle)
#
#     OrderRepository → Handles order storage.
#     OrderProcessor → Handles order processing logic.
#     OrderService → Ties everything together.
#
# 2️⃣ OCP (Open/Closed Principle)
#
#     Invoice system allows adding new invoice formats without modifying existing code.
#         Example: We can add a MobileInvoice without modifying the core logic.
#
# 3️⃣ LSP (Liskov Substitution Principle)
#
#     Different payment methods (CreditCard, PayPal, Crypto) can be used interchangeably without breaking the code.
#         Example: Changing CreditCardPayment() to PayPalPayment() works seamlessly.
#
# 4️⃣ ISP (Interface Segregation Principle)
#
#     Different notification services (EmailNotification, SMSNotification) do not force clients to implement unnecessary methods.
#         Example: Email and SMS work independently without unnecessary dependencies.
#
# 5️⃣ DIP (Dependency Inversion Principle)
#
#     OrderService does not depend on specific implementations.
#         Instead, it relies on abstract classes (PaymentProcessor, Notification, OrderRepository).
#
