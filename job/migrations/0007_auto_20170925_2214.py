# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-25 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20170920_2249'),
        ('job', '0006_auto_20170919_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nm_Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appId', models.IntegerField(null=True, verbose_name='\u4e1a\u52a1id')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u6b65\u9aa4\u540d\u79f0')),
                ('type', models.IntegerField(null=True, verbose_name='\u6b65\u9aa4\u7c7b\u578b')),
                ('ord', models.IntegerField(null=True, verbose_name='\u5c0f\u6b65\u9aa4\u6267\u884c\u7684\u6b21\u5e8f')),
                ('blockOrd', models.IntegerField(null=True, verbose_name='\u5757\u6b21\u5e8f')),
                ('blockName', models.CharField(max_length=255, null=True, verbose_name='\u5757\u540d\u79f0')),
                ('account', models.CharField(max_length=255, null=True, verbose_name='\u76ee\u6807\u673a\u5668\u7684\u6267\u884c\u8d26\u6237\u540d')),
                ('serverSetId', models.CharField(max_length=255, null=True, verbose_name='\u670d\u52a1\u5668\u5206\u7ec4Id')),
                ('ipList', models.CharField(max_length=255, null=True, verbose_name='\u76ee\u6807\u673a\u5668\u7684\u670d\u52a1\u5668IP')),
                ('scriptParam', models.CharField(max_length=255, null=True, verbose_name='\u6267\u884c\u811a\u672c\u7684\u53c2\u6570')),
                ('scriptTimeout', models.IntegerField(null=True, verbose_name='\u6267\u884c\u811a\u672c\u7684\u8d85\u65f6\u65f6\u95f4')),
                ('fileSource', models.CharField(max_length=255, null=True, verbose_name='\u6587\u4ef6\u4f20\u8f93\u7684\u6e90\u6587\u4ef6')),
                ('fileTargetPath', models.CharField(max_length=255, null=True, verbose_name='\u6587\u4ef6\u4f20\u8f93\u7684\u76ee\u6807\u76ee\u5f55')),
                ('fileSpeedLimit', models.IntegerField(null=True, verbose_name='\u4f20\u8f93\u6587\u4ef6\u7684\u9650\u901f')),
                ('text', models.CharField(max_length=255, null=True, verbose_name='\u6587\u672c\u901a\u77e5')),
                ('creater', models.CharField(max_length=255, null=True, verbose_name='\u521b\u5efa\u4eba')),
                ('createTime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('lastModifyUser', models.CharField(max_length=255, null=True, verbose_name='\u6700\u540e\u4fee\u6539\u4eba')),
                ('lastModifyTime', models.DateTimeField(null=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('isPause', models.IntegerField(default=0, null=True, verbose_name='\u662f\u5426\u9700\u8981\u6682\u505c')),
                ('companyId', models.IntegerField(default=0, null=True, verbose_name='\u5f00\u53d1\u5546id')),
                ('ccScriptId', models.IntegerField(null=True, verbose_name='CC\u811a\u672cID')),
                ('paramType', models.IntegerField(null=True, verbose_name='\u6267\u884c\u811a\u672c\u5165\u53e3\u53c2\u6570\u7c7b\u578b')),
                ('ccScriptParam', models.CharField(max_length=255, null=True, verbose_name='CC\u811a\u672c\u7684\u6267\u884c\u53c2\u6570')),
                ('ccServerSetId', models.IntegerField(null=True, verbose_name='cc\u670d\u52a1\u5668\u5206\u7ec4Id')),
                ('useIpGlobleVar', models.IntegerField(null=True, verbose_name='IP\u670d\u52a1\u5668\u662f\u5426\u4f7f\u7528\u5168\u5c40\u53d8\u91cf')),
                ('scriptId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nm_script_set', to='business.Nm_Script')),
            ],
            options={
                'db_table': 'nm_step',
            },
        ),
        migrations.CreateModel(
            name='Nm_Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appId', models.IntegerField(null=True, verbose_name='\u4e1a\u52a1ID')),
                ('name', models.CharField(max_length=255, null=True, unique=True, verbose_name='\u4f5c\u4e1a\u540d\u79f0')),
                ('account', models.CharField(max_length=255, null=True, verbose_name='\u76ee\u6807\u673a\u5668\u7684\u6267\u884c\u8d26\u6237\u540d')),
                ('serverSetId', models.IntegerField(null=True, verbose_name='\u76ee\u6807\u673a\u5668\u7684\u670d\u52a1\u5668\u96c6\u5408ID')),
                ('ipList', models.CharField(max_length=255, null=True, verbose_name='\u76ee\u6807\u673a\u5668\u7684IP,\u9017\u53f7\u5206\u5272')),
                ('creater', models.CharField(max_length=255, null=True, verbose_name='\u6267\u884c\u4eba')),
                ('createTime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('lastModifyUser', models.CharField(max_length=255, null=True, verbose_name='\u6700\u540e\u4fee\u6539\u4eba')),
                ('lastModifyTime', models.DateTimeField(null=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('tagId', models.IntegerField(null=True, verbose_name='\u6807\u7b7eId')),
            ],
            options={
                'db_table': 'nm_task',
            },
        ),
        migrations.RemoveField(
            model_name='nm_iplist',
            name='stepInstance_id',
        ),
        migrations.AddField(
            model_name='nm_step',
            name='serverId',
            field=models.ManyToManyField(related_name='nm_iplist_set', to='job.Nm_ipList'),
        ),
        migrations.AddField(
            model_name='nm_step',
            name='taskId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nm_task_set', to='job.Nm_Task'),
        ),
    ]
