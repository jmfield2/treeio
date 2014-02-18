# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Liability.category'
        db.alter_column(u'finance_liability', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Category'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Asset.depreciation_rate'
        db.alter_column(u'finance_asset', 'depreciation_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Transaction.category'
        db.alter_column(u'finance_transaction', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Category'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Transaction.liability'
        db.alter_column(u'finance_transaction', 'liability_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Liability'], null=True, on_delete=models.SET_NULL))

    def backwards(self, orm):

        # Changing field 'Liability.category'
        db.alter_column(u'finance_liability', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Category'], null=True))

        # Changing field 'Asset.depreciation_rate'
        db.alter_column(u'finance_asset', 'depreciation_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'Transaction.category'
        db.alter_column(u'finance_transaction', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Category'], null=True))

        # Changing field 'Transaction.liability'
        db.alter_column(u'finance_transaction', 'liability_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Liability'], null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.accessentity': {
            'Meta': {'object_name': 'AccessEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dislikes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'comments_disliked'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'comments_liked'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.User']"})
        },
        u'core.group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Group', '_ormbases': [u'core.AccessEntity']},
            u'accessentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.AccessEntity']", 'unique': 'True', 'primary_key': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': u"orm['core.Group']"})
        },
        u'core.object': {
            'Meta': {'object_name': 'Object'},
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'comments'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.Comment']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'objects_created'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['core.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dislikes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_disliked'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.User']"}),
            'full_access': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_full_access'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.AccessEntity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_liked'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.User']"}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'links_rel_+'", 'null': 'True', 'to': u"orm['core.Object']"}),
            'nuvius_resource': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'object_type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'read_access': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_read_access'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.AccessEntity']"}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'subscriptions'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.User']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.Tag']", 'null': 'True', 'blank': 'True'}),
            'trash': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'core.tag': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tag'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'core.user': {
            'Meta': {'ordering': "['name']", 'object_name': 'User', '_ormbases': [u'core.AccessEntity']},
            u'accessentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.AccessEntity']", 'unique': 'True', 'primary_key': 'True'}),
            'default_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_user_set'", 'null': 'True', 'to': u"orm['core.Group']"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_access': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other_groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.Group']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'finance.account': {
            'Meta': {'ordering': "['name']", 'object_name': 'Account', '_ormbases': [u'core.Object']},
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'balance_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Currency']"}),
            'balance_display': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['identities.Contact']"})
        },
        u'finance.asset': {
            'Meta': {'ordering': "['-purchase_date']", 'object_name': 'Asset', '_ormbases': [u'core.Object']},
            'asset_type': ('django.db.models.fields.CharField', [], {'default': "'fixed'", 'max_length': '32'}),
            'current_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'depreciation_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'depreciation_type': ('django.db.models.fields.CharField', [], {'default': "'straight'", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'endlife_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'initial_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'lifetime': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '0', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['identities.Contact']"}),
            'purchase_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'})
        },
        u'finance.category': {
            'Meta': {'object_name': 'Category', '_ormbases': [u'core.Object']},
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'finance.currency': {
            'Meta': {'object_name': 'Currency', '_ormbases': [u'core.Object']},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'factor': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '10', 'decimal_places': '4'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        u'finance.equity': {
            'Meta': {'ordering': "['-purchase_date']", 'object_name': 'Equity', '_ormbases': [u'core.Object']},
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'equity_type': ('django.db.models.fields.CharField', [], {'default': "'share'", 'max_length': '32'}),
            'issue_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'issuer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finance_equity_issued'", 'to': u"orm['identities.Contact']"}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finance_equity_owned'", 'to': u"orm['identities.Contact']"}),
            'purchase_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'sell_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        },
        u'finance.liability': {
            'Meta': {'ordering': "['-due_date']", 'object_name': 'Liability', '_ormbases': [u'core.Object']},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Account']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finance_liability_source'", 'to': u"orm['identities.Contact']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finance_liability_target'", 'to': u"orm['identities.Contact']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'value_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Currency']"}),
            'value_display': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'})
        },
        u'finance.tax': {
            'Meta': {'object_name': 'Tax', '_ormbases': [u'core.Object']},
            'compound': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        u'finance.transaction': {
            'Meta': {'ordering': "['-datetime']", 'object_name': 'Transaction', '_ormbases': [u'core.Object']},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Account']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'liability': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Liability']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finance_transaction_source'", 'to': u"orm['identities.Contact']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finance_transaction_target'", 'to': u"orm['identities.Contact']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'value_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Currency']"}),
            'value_display': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'})
        },
        u'identities.contact': {
            'Meta': {'ordering': "['name']", 'object_name': 'Contact', '_ormbases': [u'core.Object']},
            'contact_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['identities.ContactType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': u"orm['identities.Contact']"}),
            'related_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.AccessEntity']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        u'identities.contactfield': {
            'Meta': {'ordering': "['name']", 'object_name': 'ContactField', '_ormbases': [u'core.Object']},
            'allowed_values': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'identities.contacttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ContactType', '_ormbases': [u'core.Object']},
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['identities.ContactField']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['finance']