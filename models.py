from django.db import models
from django.conf import settings
# Create your models here.

from django.db import models
from django.conf import settings

class Direction(models.Model):
    name = models.CharField('Название направления', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class DefaultGoal(models.Model):
    direction = models.ForeignKey(Direction, related_name='default_goals', on_delete=models.CASCADE)
    goal_view_name = models.CharField('Название системной цели', max_length=50)

    def __str__(self):
        return self.goal_view_name

    class Meta:
        verbose_name = "Базовая цель"
        verbose_name_plural = "Базовые цели"


class DefaultSubGoal(models.Model):
    main_goal = models.ForeignKey(DefaultGoal, related_name='default_subgoals', on_delete=models.CASCADE)
    sub_goal_name = models.CharField('Название побочной цели', max_length=50)

    def __str__(self):
        return self.sub_goal_name

    class Meta:
        verbose_name = "Базовая побочная цель"
        verbose_name_plural = "Базовые побочные цели"


class DefaultStep(models.Model):
    subgoal = models.ForeignKey(DefaultSubGoal, related_name='default_steps', on_delete=models.CASCADE)
    step_description = models.CharField('Описание шага', max_length=100)

    def __str__(self):
        return self.step_description

    class Meta:
        verbose_name = "Базовый шаг"
        verbose_name_plural = "Базовые шаги"

class Goal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    goal_name = models.CharField('Название цели', max_length=50)
    progress_goal = models.IntegerField(default=0)

    default_goal = models.ForeignKey(
        'DefaultGoal',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Базовая цель"
    )

    subgoals = models.ManyToManyField('SubGoal', related_name='goals', blank=True)
 

    def __str__(self):
        return self.goal_name

    def get_subgoals(self):
        return self.subgoals.all()

    class Meta:
        verbose_name = "Цель пользователя"
        verbose_name_plural = "Цели пользователей"



class SubGoal(models.Model):
    main_goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='all_subgoals')
    progress_subgoal = models.IntegerField(default=0)

    # Привязка к дефолтной подцели
    default_subgoal = models.ForeignKey(
        'DefaultSubGoal',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Базовая побочная цель"
    )

    def __str__(self):
        return self.sub_goal_name

    class Meta:
        verbose_name = "Побочная цель пользователя"
        verbose_name_plural = "Побочные цели пользователей"


class Step(models.Model):
    subgoal = models.ForeignKey(SubGoal, related_name='steps', on_delete=models.CASCADE)
    step_description = models.CharField('Описание шага', max_length=100)
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")

    # Привязка к дефолтному шагу
    default_step = models.ForeignKey(
        'DefaultStep',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Базовый шаг"
    )

    def __str__(self):
        return self.step_description

    class Meta:
        verbose_name = "Шаг пользователя"
        verbose_name_plural = "Шаги пользователей"
