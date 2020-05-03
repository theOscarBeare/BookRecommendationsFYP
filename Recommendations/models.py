from django.db import models
from DataCall.models import Books


class enduser(models.Model):
    userid = models.AutoField(db_column='userid', primary_key=True)
    username = models.CharField(db_column='username', max_length=50)
    userfname = models.CharField(db_column='userfname', max_length= 50)
    userlname = models.CharField(db_column='userlname', max_length=50)
    userknowledgelevel = models.IntegerField(db_column='userknowledgelevel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enduser'

    @classmethod
    def execute(cls, param):
        pass


class userinformation(models.Model):
    informationid = models.AutoField(db_column='informationid', primary_key=True)
    bookidread = models.ForeignKey(Books, models.DO_NOTHING, db_column='bookidread')
    userid = models.ForeignKey(enduser, models.DO_NOTHING, db_column='userid')
    bookidreviewed = models.IntegerField(db_column='booksReviewedID')

    class Meta:
        managed = False
        db_table = 'userinformation'


class userrecommendations(models.Model):
    recomendationid = models.AutoField(db_column='recommendationid', primary_key=True)
    userid = models.ForeignKey(enduser, models.DO_NOTHING, db_column='enduser')
    bookid = models.ForeignKey(Books, models.DO_NOTHING, db_column='bookid')

    class Meta:
        managed = True
        db_table = 'userrecommendations'

    @classmethod
    def execute(cls, param):
        pass