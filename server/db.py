from peewee import *

db = SqliteDatabase("./crinacle_reviews.db")

class BaseModel(Model):
    class Meta:
        database = db

rank = {
    "F=": 0,
    "E=": 0,
    "D-": 0,
    "D=": 0,
    "D+": 0,
    "C-": 0,
    "C=": 0,
    "C+": 0,
    "B-": 0,
    "B=": 0,
    "B+": 0,
    "A-": 0,
    "A=": 0,
    "A+": 0,
    "S-": 0,
    "S=": 0,
}

class Review(BaseModel):
    rank = IntegerField(null=False)
    value_rating = IntegerField(null=False)
    model = CharField(64)
    price = IntegerField(null=False)
    signature = CharField(64)
    comments = CharField(256)
    tone_grade = IntegerField(null=False)
    technical_grade = IntegerField(null=False)
    driver_type = CharField(32)


if __name__ == '__main__':
    