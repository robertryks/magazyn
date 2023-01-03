from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Data aktualizacji',
                                   db_index=True)

    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Data utworzenia')

    class Meta:
        abstract = True


class Dimension(BaseModel):
    size = models.DecimalField(decimal_places=2,
                               max_digits=6,
                               verbose_name='Średnica',
                               unique=True,
                               error_messages={
                                   "unique": "Taka średnica już istnieje w bazie danych."
                               })

    def __str__(self):
        return str(self.size)

    class Meta:
        verbose_name = 'Średnica'
        verbose_name_plural = 'Średnice'
        ordering = ['size']
        indexes = [
            models.Index(fields=['size'], name='dimension_size_idx')
        ]
        constraints = [
            models.CheckConstraint(check=models.Q(size__gt=0),
                                   name='size_gt_0',
                                   violation_error_message="Średnica musi być większa od zera."),
        ]


class Grade(BaseModel):
    name = models.CharField(max_length=25,
                            verbose_name='Oznaczenie',
                            unique=True,
                            error_messages={
                                "required": "Wartość w polu gatunku jest wymagana.",
                                "unique": "Taki gatunek już istnieje w bazie danych."
                            })

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gatunek'
        verbose_name_plural = 'Gatunki'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='grade_name_idx')
        ]


class Heat(BaseModel):
    name = models.CharField(max_length=25,
                            verbose_name='Oznaczenie',
                            unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Wytop'
        verbose_name_plural = 'Wytopy'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='heat_name_idx')
        ]


class Certificate(BaseModel):
    number = models.CharField(max_length=25,
                              verbose_name='Numer',
                              unique=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Certyfikat'
        verbose_name_plural = 'Certyfikaty'
        ordering = ['number']
        indexes = [
            models.Index(fields=['number'], name='certificate_number_idx')
        ]


# Przyjęcie towaru na skład
class Supply(BaseModel):
    number = models.CharField(max_length=25,
                              verbose_name='Dokument',
                              unique=True)

    date = models.DateField(verbose_name='Data')

    can_modify = models.BooleanField(verbose_name='Modyfikacja',
                                     default=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Przychód'
        verbose_name_plural = 'Przychody'
        ordering = ['number']
        get_latest_by = 'date'
        indexes = [
            models.Index(fields=['number'], name='supply_number_idx'),
            models.Index(fields=['date'], name='supply_date_idx')
        ]


# Pozycja na dostawie towaru
class SupplyItem(BaseModel):
    supply = models.ForeignKey(Supply,
                               on_delete=models.CASCADE,
                               verbose_name='Przychód',
                               related_name='supplyitem')

    dimension = models.ForeignKey(Dimension,
                                  on_delete=models.CASCADE,
                                  verbose_name='Średnica',
                                  related_name='supplyitem')

    grade = models.ForeignKey(Grade,
                              on_delete=models.CASCADE,
                              verbose_name='Gatunek',
                              related_name='supplyitem')

    heat = models.ForeignKey(Heat,
                             on_delete=models.CASCADE,
                             verbose_name='Wytop',
                             related_name='supplyitem')

    certificate = models.ForeignKey(Certificate,
                                    on_delete=models.CASCADE,
                                    verbose_name='Certyfikat',
                                    related_name='supplyitem')

    quantity = models.DecimalField(decimal_places=2,
                                   max_digits=6,
                                   verbose_name='Ilość',
                                   default=0)

    actual = models.DecimalField(decimal_places=2,
                                 max_digits=6,
                                 verbose_name='Stan',
                                 default=0)

    can_modify = models.BooleanField(verbose_name='Modyfikacja',
                                     default=True)

    def __str__(self):
        return f'{self.dimension} mm ({self.grade}) - {self.actual} / {self.quantity} kg'

    class Meta:
        verbose_name = 'Pozycja przychodu'
        verbose_name_plural = 'Pozycje przychodu'
        indexes = [
            models.Index(fields=['dimension', 'grade'], name='supplyitem_dimension_grade_idx')
        ]


# Wydanie towaru na skład
class Issue(BaseModel):
    number = models.CharField(max_length=25,
                              verbose_name='Dokument',
                              unique=True)

    date = models.DateField(verbose_name='Data')

    can_modify = models.BooleanField(verbose_name='Modyfikacja',
                                     default=True)

    sending = models.BooleanField(verbose_name='Wysłane',
                                  default=False)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Rozchód'
        verbose_name_plural = 'Rozchody'
        ordering = ['number']
        get_latest_by = 'date'
        indexes = [
            models.Index(fields=['number'], name='issue_number_idx'),
            models.Index(fields=['date'], name='issue_date_idx')
        ]


# Pozycja na wydaniu towaru
class IssueItem(BaseModel):
    issue = models.ForeignKey(Issue,
                              on_delete=models.CASCADE,
                              verbose_name='Rozchód',
                              related_name='issueitem')

    supply_item = models.ForeignKey(SupplyItem,
                                    on_delete=models.CASCADE,
                                    verbose_name='Dostawa',
                                    related_name='issueitem')

    dimension = models.ForeignKey(Dimension,
                                  on_delete=models.CASCADE,
                                  verbose_name='Średnica',
                                  related_name='issueitem')

    grade = models.ForeignKey(Grade,
                              on_delete=models.CASCADE,
                              verbose_name='Gatunek',
                              related_name='issueitem')

    heat = models.ForeignKey(Heat,
                             on_delete=models.CASCADE,
                             verbose_name='Wytop',
                             related_name='issueitem')

    certificate = models.ForeignKey(Certificate,
                                    on_delete=models.CASCADE,
                                    verbose_name='Certyfikat',
                                    related_name='issueitem')

    quantity = models.DecimalField(decimal_places=2,
                                   max_digits=6,
                                   verbose_name='Ilość')

    can_modify = models.BooleanField(verbose_name='Modyfikacja',
                                     default=True)

    def __str__(self):
        return f'{self.dimension} mm ({self.grade}) - {self.quantity} kg'

    class Meta:
        verbose_name = 'Pozycja rozchodu'
        verbose_name_plural = 'Pozycje rozchodu'
        indexes = [
            models.Index(fields=['dimension', 'grade'], name='issueitem_dimension_grade_idx')
        ]
