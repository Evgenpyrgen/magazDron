from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30, unique = True,
                            verbose_name = "Категория")
    description = models.TextField(verbose_name = "Описание")
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.name                                          #тип memo
    class Meta:
        ordering = ["name"]
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

class Good(models.Model):
    name = models.CharField(max_length = 50, unique = True,
                            verbose_name = "Название")
    description = models.TextField(verbose_name = "Описание")
    in_stock = models.BooleanField(default = True, db_index = True,
                                    verbose_name = "В наличии")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def get_is_stock(self):
        if self.in_stock:
            return "+"
        else:
            return ""
    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + "(нет в наличии)"
        return s
    class Meta:
        ordering = ["name"]
        verbose_name = "товар"
        verbose_name_plural = "товары"
        