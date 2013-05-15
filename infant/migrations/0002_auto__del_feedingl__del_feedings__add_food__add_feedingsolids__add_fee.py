# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FeedingL'
        db.delete_table(u'infant_feedingl')

        # Deleting model 'FeedingS'
        db.delete_table(u'infant_feedings')

        # Adding model 'Food'
        db.create_table(u'infant_food', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('food_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'infant', ['Food'])

        # Adding model 'FeedingSolids'
        db.create_table(u'infant_feedingsolids', (
            (u'feeding_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['infant.Feeding'], unique=True, primary_key=True)),
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['infant.Food'])),
        ))
        db.send_create_signal(u'infant', ['FeedingSolids'])

        # Adding model 'FeedingLiquids'
        db.create_table(u'infant_feedingliquids', (
            (u'feeding_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['infant.Feeding'], unique=True, primary_key=True)),
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['infant.Food'])),
        ))
        db.send_create_signal(u'infant', ['FeedingLiquids'])

        # Deleting field 'Feeding.food_type'
        db.delete_column(u'infant_feeding', 'food_type')


    def backwards(self, orm):
        # Adding model 'FeedingL'
        db.create_table(u'infant_feedingl', (
            ('helper', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('type', self.gf('django.db.models.fields.TextField')()),
            ('help_type', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'infant', ['FeedingL'])

        # Adding model 'FeedingS'
        db.create_table(u'infant_feedings', (
            ('amount', self.gf('django.db.models.fields.TextField')()),
            ('infant', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.TextField')()),
            ('helper', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('type', self.gf('django.db.models.fields.TextField')()),
            ('help_type', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'infant', ['FeedingS'])

        # Deleting model 'Food'
        db.delete_table(u'infant_food')

        # Deleting model 'FeedingSolids'
        db.delete_table(u'infant_feedingsolids')

        # Deleting model 'FeedingLiquids'
        db.delete_table(u'infant_feedingliquids')

        # Adding field 'Feeding.food_type'
        db.add_column(u'infant_feeding', 'food_type',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=20),
                      keep_default=False)


    models = {
        u'infant.diapering': {
            'Meta': {'object_name': 'Diapering'},
            'd_type': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infant': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ointment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'infant.feeding': {
            'Meta': {'object_name': 'Feeding'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'help_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20'}),
            'helper': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infant': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'infant.feedingliquids': {
            'Meta': {'object_name': 'FeedingLiquids', '_ormbases': [u'infant.Feeding']},
            u'feeding_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['infant.Feeding']", 'unique': 'True', 'primary_key': 'True'}),
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['infant.Food']"})
        },
        u'infant.feedingsolids': {
            'Meta': {'object_name': 'FeedingSolids', '_ormbases': [u'infant.Feeding']},
            u'feeding_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['infant.Feeding']", 'unique': 'True', 'primary_key': 'True'}),
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['infant.Food']"})
        },
        u'infant.food': {
            'Meta': {'object_name': 'Food'},
            'food_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'infant.nap': {
            'Meta': {'object_name': 'Nap'},
            'endAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infant': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'startAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['infant']