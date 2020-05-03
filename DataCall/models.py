from django.db import models


class Author(models.Model):
    authorid = models.AutoField(db_column='AuthorID', primary_key=True)  # Field name made lowercase.
    authorfname = models.CharField(db_column='AuthorFName', max_length=50)  # Field name made lowercase.
    authorlname = models.CharField(db_column='AuthorLName', max_length=50)  # Field name made lowercase.
    authorage = models.CharField(db_column='AuthorAge', max_length=50, blank=True, null=True)  # Field name made lowercase.
    authorcountry = models.CharField(max_length=50, blank=True, null=True)
    alive = models.BooleanField()
    sex = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Author'



class Books(models.Model):
    bookid = models.AutoField(db_column='BookID', primary_key=True)  # Field name made lowercase.
    bookisbn = models.IntegerField(db_column='BookISBN', blank=True, null=True)  # Field name made lowercase.
    bookname = models.CharField(db_column='BookName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    noofpages = models.CharField(db_column='NoOfPages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reviewid = models.ForeignKey('Reviews', models.DO_NOTHING, db_column='reviewid', blank=True, null=True)
    bookdifficulty = models.IntegerField(db_column='bookdifficulty')

    class Meta:
        managed = False
        db_table = 'Books'

    @classmethod
    def execute(cls, param):
        pass


class Authorbooks(models.Model):
    authorid = models.ForeignKey(Author, models.DO_NOTHING, db_column='authorid')
    bookid = models.ForeignKey(Books, models.DO_NOTHING, db_column='bookid')

    class Meta:
        managed = False
        db_table = 'authorbooks'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Reviews(models.Model):
    reviewid = models.AutoField(primary_key=True)
    reviewname = models.CharField(max_length=100)
    lengthofreview = models.IntegerField(blank=True, null=True)
    reviewtext = models.TextField()

    class Meta:
        managed = False
        db_table = 'reviews'