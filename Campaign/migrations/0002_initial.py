# Generated by Django 3.2.23 on 2024-01-25 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EvalData', '0001_initial'),
        ('Campaign', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigndata',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='EvalData.market', verbose_name='Market'),
        ),
        migrations.AddField(
            model_name='campaigndata',
            name='metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='EvalData.metadata', verbose_name='Metadata'),
        ),
        migrations.AddField(
            model_name='campaigndata',
            name='modifiedBy',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='campaign_campaigndata_modified_by', related_query_name='campaign_campaigndatas', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AddField(
            model_name='campaigndata',
            name='retiredBy',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='campaign_campaigndata_retired_by', related_query_name='campaign_campaigndatas', to=settings.AUTH_USER_MODEL, verbose_name='Retired by'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='activatedBy',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='campaign_campaign_activated_by', related_query_name='campaign_campaigns', to=settings.AUTH_USER_MODEL, verbose_name='Activated by'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='batches',
            field=models.ManyToManyField(blank=True, related_name='campaign_campaign_batches', related_query_name='campaign_campaigns', to='Campaign.CampaignData', verbose_name='Batches'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='completedBy',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='campaign_campaign_completed_by', related_query_name='campaign_campaigns', to=settings.AUTH_USER_MODEL, verbose_name='Completed by'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='createdBy',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='campaign_campaign_created_by', related_query_name='campaign_campaigns', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='modifiedBy',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='campaign_campaign_modified_by', related_query_name='campaign_campaigns', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='retiredBy',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='campaign_campaign_retired_by', related_query_name='campaign_campaigns', to=settings.AUTH_USER_MODEL, verbose_name='Retired by'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='campaign_campaign_teams', related_query_name='campaign_campaigns', to='Campaign.CampaignTeam', verbose_name='Teams'),
        ),
    ]
