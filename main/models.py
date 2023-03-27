from django.urls import reverse
from django.db import models


class Vacancy(models.Model):
    """ Model for posting vacancies """

    title = models.CharField(
        max_length=127,
        verbose_name='Вакансия',
        null=False,
        blank=False
    )
    description = models.TextField(verbose_name='Описание')
    active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ('active', '-id')


class Direction(models.Model):
    """ Model for directions for Project model """

    title = models.CharField(
        max_length=31,
        verbose_name='Направление',
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
        ordering = ('title',)


class Industry(models.Model):
    """ Model for industries for Project model """

    title = models.CharField(
        max_length=127,
        verbose_name='Отрасль',
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отрасль'
        verbose_name_plural = 'Отрасли'
        ordering = ('title', )


class Project(models.Model):  # is Project model
    """ Model for list of projects and projects """

    direction = models.ForeignKey(
        Direction,
        on_delete=models.PROTECT,
        verbose_name='Направление',
        null=False,
        blank=False
    )
    industry = models.ManyToManyField(
        Industry,
        verbose_name='Отрасль',
    )
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Заголовок',
        null=False,
        blank=False
    )
    content = models.TextField(
        verbose_name='Описание',
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Url'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('-created_at', )


class CostGroup(models.Model):
    """ Model for cost groups in cost table. Works together with Cost model """

    title = models.CharField(
        max_length=350,
        verbose_name='Название группы',
        null=False,
        blank=False,
        # unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа цен'
        verbose_name_plural = 'Группы цен'
        ordering = ('-id',)


class Cost(models.Model):
    """ Model for cost table. Works together with CostGroup model """

    costgroup = models.ForeignKey(
        to=CostGroup,
        on_delete=models.PROTECT,
        verbose_name='Группа услуг',
        related_name='cost',
        related_query_name='costs'
    )
    title = models.CharField(
        max_length=350,
        verbose_name='Название услуги',
        null=False,
        blank=False
        )
    cost = models.CharField(
        max_length=200,
        verbose_name='Стоимость',
        null=False,
        blank=False
    )
    term = models.CharField(
        max_length=200,
        verbose_name='Срок'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        ordering = ('-id',)


class Slider(models.Model):
    """ Model for posting ad """

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
