from django.db.models import Q

Author.objects.filter(Q(name__icontains='tom', email__icontains='example', created_on__year=2018))

Author.objects.filter(name__icontains='tom', email__icontains='example', created_on__year=2019)

# Bitwise | (OR) operator
Author.objects.filter(Q(name__iexact='tommy') | Q(name__iexact='jerry'))

# We can pass multiple Q objects to the lookup functions (e.g filter(), exclude(), get() etc) as position
# arguments. If we do so, the Q objects will be ANDed together. For example:
q = Author.objects.filter(
    Q(created_on__year=2019),
    Q(name__iexact='tommy') | Q(name__iexact='jerry')
)

>>> q.query
<django.db.models.sql.query.Query object at 0x7f3ba422a748>
>>> print(q.query)
SELECT "djangobin_author"."id", "djangobin_author"."name", "djangobin_author"."email", "djangobin_author"."active",
       "djangobin_author"."created_on", "djangobin_author"."last_logged_in"
FROM "djangobin_author"
WHERE ("djangobin_author"."created_on" BETWEEN 2019-01-01 00:00:00 AND 2019-12-31 23:59:59.999999
     AND ("djangobin_author"."name" LIKE tommy
          OR
          "djangobin_author"."name" LIKE jerry
     ))

# Finally we can also mix keyword arguments with Q objects while calling the lookup function. In doing so,
# remember that all the arguments to the lookup function will be ANDed together and all the Q objects must appear
# before any keyword arguments. That means the following is a valid query:
Author.objects.filter(
    Q(name__iexact='tommy') | Q(name__iexact='jerry'),
    active=True
)

# print(q.query)
SELECT "djangobin_author"."id", "djangobin_author"."name", "djangobin_author"."email", "djangobin_author"."active", "djangobin_author"."created_on", "djangobin_author"."last_logged_in" FROM "djangobin_author" WHERE (("djangobin_author"."name" LIKE tommy ESCAPE '\' OR "djangobin_author"."name" LIKE jerry ESCAPE '\') AND "djangobin_author"."active" = True)

