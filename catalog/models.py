from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название категории", help_text="Введите название категории", )
    description = models.TextField(verbose_name="Описание категории", help_text="Введите описание категории",
                                   **NULLABLE)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название товара", help_text="Введите название товара")
    description = models.TextField(verbose_name="Описание товара", help_text="Введите описание товара", **NULLABLE)
    price = models.IntegerField(verbose_name='Цена', help_text='Введите цену товара')
    photo = models.ImageField(upload_to="products/photo", **NULLABLE, verbose_name="фото",
                              help_text="загрузите фото товара", )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # manufactured_at = models.DateField(auto_now=True, verbose_name='')
    # t_ext = models.TextField(verbose_name="Описание категории", help_text="Введите описание категории",
    #                                **NULLABLE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return f"{self.name}"
