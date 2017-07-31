# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-12 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(verbose_name='学期')),
                ('class_type', models.IntegerField(choices=[(0, '周末'), (1, '脱产'), (2, '网络')])),
                ('max_student_num', models.IntegerField(default=80)),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='结业日期')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('content', models.TextField(verbose_name='合同内容')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('period', models.IntegerField(verbose_name='周期(月)')),
                ('price', models.FloatField()),
                ('outline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.IntegerField(verbose_name='节次')),
                ('name', models.CharField(max_length=128)),
                ('has_homework', models.BooleanField(default=True)),
                ('homework_requirement', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('class_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ClassList')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('qq', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('weixin', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('phone', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('content', models.TextField(verbose_name='首次咨询内容/客户详情')),
                ('status', models.SmallIntegerField(choices=[(0, '已报名'), (1, '已退费'), (2, '未报名')], default=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('consult_courses', models.ManyToManyField(to='app.Course')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_consultant', to='app.Account')),
                ('referal_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_referal', to='app.Account')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerFollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, '绝不考虑'), (1, '短期内不考虑'), (2, '已在其他机构报名'), (3, '2周内报名'), (4, '已报名'), (5, '已试听')])),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Account')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Account')),
                ('class_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ClassList')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url_type', models.IntegerField(choices=[(0, 'absolute'), (1, 'relative')], default=1)),
                ('url', models.CharField(max_length=128)),
                ('order', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.SmallIntegerField(choices=[(0, '现金'), (1, '微信'), (2, '支付宝'), (3, '刷卡'), (4, '学生贷款')])),
                ('payment_type', models.SmallIntegerField(choices=[(0, '报名费'), (1, '学费'), (2, '退费')])),
                ('amount', models.FloatField()),
                ('class_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ClassList')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('menus', models.ManyToManyField(blank=True, null=True, to='app.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (70, 'B'), (65, 'C+'), (60, 'C'), (40, 'C-'), (-50, 'D'), (0, 'N/A'), (-100, 'COPY')])),
                ('show_status', models.IntegerField(choices=[(0, '正常签到'), (1, '迟到'), (2, '缺勤'), (3, 'N/A')])),
                ('comment', models.TextField(blank=True, null=True, verbose_name='批注')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CourseRecord')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Account')),
            ],
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url_type', models.IntegerField(choices=[(0, 'absolute'), (1, 'relative')], default=1)),
                ('url', models.CharField(max_length=128)),
                ('order', models.SmallIntegerField(default=0)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=set([('url', 'url_type')]),
        ),
        migrations.AddField(
            model_name='customer',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Source'),
        ),
        migrations.AddField(
            model_name='customer',
            name='tags',
            field=models.ManyToManyField(blank=True, to='app.Tag'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Contract'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(to='app.Account'),
        ),
        migrations.AlterUniqueTogether(
            name='submenu',
            unique_together=set([('url', 'url_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([('student', 'course_record')]),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([('class_list', 'day_num')]),
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([('course', 'branch', 'semester', 'class_type')]),
        ),
    ]
