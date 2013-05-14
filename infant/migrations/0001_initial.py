# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feeding'
        db.create_table(u'infant_feeding', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('infant', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('helper', self.gf('django.db.models.fields.CharField')(default=None, max_length=20)),
            ('help_type', self.gf('django.db.models.fields.CharField')(default=None, max_length=20)),
            ('food_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'infant', ['Feeding'])

        # Adding model 'FeedingL'
        db.create_table(u'infant_feedingl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('helper', self.gf('django.db.models.fields.TextField')()),
            ('help_type', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.TextField')()),
            ('amount', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'infant', ['FeedingL'])

        # Adding model 'FeedingS'
        db.create_table(u'infant_feedings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.TextField')()),
            ('helper', self.gf('django.db.models.fields.TextField')()),
            ('help_type', self.gf('django.db.models.fields.TextField')()),
            ('infant', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.TextField')()),
            ('amount', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'infant', ['FeedingS'])

        # Adding model 'Nap'
        db.create_table(u'infant_nap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('infant', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('startAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('endAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'infant', ['Nap'])

        # Adding model 'Diapering'
        db.create_table(u'infant_diapering', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('infant', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('d_type', self.gf('django.db.models.fields.TextField')()),
            ('ointment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'infant', ['Diapering'])


    def backwards(self, orm):
        # Deleting model 'Feeding'
        db.delete_table(u'infant_feeding')

        # Deleting model 'FeedingL'
        db.delete_table(u'infant_feedingl')

        # Deleting model 'FeedingS'
        db.delete_table(u'infant_feedings')

        # Deleting model 'Nap'
        db.delete_table(u'infant_nap')

        # Deleting model 'Diapering'
        db.delete_table(u'infant_diapering')


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
            'food_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'help_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20'}),
            'helper': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infant': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'infant.feedingl': {
            'Meta': {'object_name': 'FeedingL'},
            'amount': ('django.db.models.fields.TextField', [], {}),
            'help_type': ('django.db.models.fields.TextField', [], {}),
            'helper': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'type': ('django.db.models.fields.TextField', [], {})
        },
        u'infant.feedings': {
            'Meta': {'object_name': 'FeedingS'},
            'amount': ('django.db.models.fields.TextField', [], {}),
            'help_type': ('django.db.models.fields.TextField', [], {}),
            'helper': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infant': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'type': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.TextField', [], {})
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