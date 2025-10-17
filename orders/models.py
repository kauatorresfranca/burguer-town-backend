from django.db import models
from users.models import Cliente
from menu.models import MenuItem

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pendente'),
        ('preparing', 'Em preparo'),
        ('delivered', 'Entregue'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"

    @property
    def total(self):
        return sum(item.total() for item in self.orderitem_set.all())


class OrderItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="order_items")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def total(self):
        return self.quantidade * self.preco_unitario
