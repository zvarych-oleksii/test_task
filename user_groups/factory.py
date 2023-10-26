import factory
import random
from .models import CustomUser, CustomGroup
from factory.faker import faker
from django.contrib.auth.hashers import make_password


fake = faker.Faker()



class CustomGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomGroup

    name = factory.Faker('user_name')
    description = fake.paragraph(nb_sentences=1)



class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    @factory.lazy_attribute
    def password(self):
        return make_password('1Password.')

    @factory.lazy_attribute
    def custom_group(self):
        all_groups = CustomGroup.objects.all()
        random_group = random.choice(all_groups)
        return random_group


def create_test_db():
    CustomGroupFactory.create_batch(10)
    CustomUserFactory.create_batch(100)
