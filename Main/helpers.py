from django.utils.text import slugify
import string
import random

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    return res 

def generate_slug(text):
    new_slug = slugify(text)
    from Main.models import Post
    if Post.objects.filter(slug = new_slug).filter():
        return generate_slug(text + '-' + generate_random_string(3))

    return new_slug


def generate_slug_category(text):
    new_slug = slugify(text)
    from Main.models import Category
    if Category.objects.filter(slug = new_slug).filter():
        return generate_slug_category(text + '-' + generate_random_string(3))

    return new_slug