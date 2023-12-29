from django.db import models


class Languages(models.Model):
    ID = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=50)


class Authors(models.Model):
    ID = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Publishers(models.Model):
    ID = models.IntegerField(primary_key=True)
    publisher = models.CharField(max_length=50)
    location = models.CharField(max_length=100)


class Categories(models.Model):
    ID = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    category_persian = models.CharField(max_length=100)


class Sections(models.Model):
    ID = models.IntegerField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    section_persian = models.CharField(max_length=100)


class Faculties(models.Model):
    ID = models.IntegerField(primary_key=True)
    faculty = models.CharField(max_length=50)
    faculty_persian = models.CharField(max_length=50)


class Books(models.Model):
    ID = models.IntegerField(primary_key=True)
    signatory = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=30)
    pages = models.IntegerField()
    language_id = models.ForeignKey(Languages, on_delete=models.CASCADE)
    edition = models.IntegerField()
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    publisher_id = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    publication_year = models.DateField()
    section_id = models.ForeignKey(Sections, on_delete=models.CASCADE)
    faculty_id = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    description = models.TextField()


class eBooks(models.Model):
    ID = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    extension = models.CharField(max_length=30)


class Copies(models.Model):
    ID = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)


class News(models.Model):
    ID = models.IntegerField(primary_key=True)
    news_title = models.CharField(max_length=255)
    news_summary = models.TextField()
    news_details = models.TextField()
    news_ref = models.CharField(max_length=255)
    news_title_persian = models.CharField(max_length=255)
    news_details_persian = models.TextField()
    news_ref_persian = models.CharField(max_length=255)
    news_date = models.DateField()
    fileext = models.CharField(max_length=3)
    faculties_id = models.ForeignKey(Faculties, on_delete=models.CASCADE)
