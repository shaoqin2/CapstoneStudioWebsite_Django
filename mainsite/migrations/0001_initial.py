# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 22:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_chinese', models.CharField(max_length=300, verbose_name='中文名')),
                ('name', models.CharField(max_length=300, verbose_name='课程编号')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='开课日期')),
                ('student_number_cap', models.PositiveSmallIntegerField(blank=True, verbose_name='学生上限')),
                ('class_has_end', models.BooleanField(default=False, verbose_name='课程结束')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='反馈名称')),
                ('feedback_content', models.TextField(max_length=5000)),
                ('from_teacher', models.CharField(blank=True, max_length=100)),
                ('date', models.DateField()),
                ('for_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_chinese', models.CharField(max_length=100, verbose_name='作业名')),
                ('homework_content', models.TextField(max_length=5000)),
                ('assign_date', models.DateField()),
                ('due_date', models.DateField()),
                ('submission', models.CharField(choices=[('Submit by Email', 'Submit by Email'), ('Submit in Person', 'Submit in Person'), ('Submit by Wechat', 'Submit by Wechat'), ('Submit in Class', 'Submit in Class'), ('No need to Submit', 'No need to Submit')], default='Submit by Wechat', max_length=20)),
                ('report', models.BooleanField(default=False, verbose_name='反馈给家长？')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('name_chinese', models.CharField(max_length=50, verbose_name='中文名')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_chinese', models.CharField(max_length=80, verbose_name='中文名')),
                ('join_date', models.DateField(auto_now_add=True, verbose_name='加入时间')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=18)),
                ('toefl_score', models.CharField(blank=True, max_length=4)),
                ('sat_score', models.CharField(blank=True, max_length=5)),
                ('act_score', models.CharField(blank=True, max_length=3)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_chinese', models.CharField(max_length=100, verbose_name='中文名')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Student', verbose_name='对应学生'),
        ),
        migrations.AddField(
            model_name='homework',
            name='assigned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_homework', to='mainsite.Teacher', verbose_name='布置老师'),
        ),
        migrations.AddField(
            model_name='homework',
            name='belong_to_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_homework', to='mainsite.Class', verbose_name='所属课程'),
        ),
        migrations.AddField(
            model_name='homework',
            name='completed_student',
            field=models.ManyToManyField(blank=True, to='mainsite.Student', verbose_name='已完成的学生'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='for_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_feedback', to='mainsite.Student'),
        ),
        migrations.AddField(
            model_name='class',
            name='enrolled_student',
            field=models.ManyToManyField(related_name='related_class', to='mainsite.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ManyToManyField(to='mainsite.Teacher'),
        ),
    ]
