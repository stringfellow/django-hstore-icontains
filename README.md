# Failure test case

Problem: Docs say you can do e.g. `data__icontains={'foo': 'bar'}` but this
produces a failure with django 1.7 (it did not with 1.6).

# `django_hstore` 1.3.6, `django` 1.7.7

    E
    ======================================================================
    ERROR: test_icontains (lookup_test.tests.IContainsTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/spike/Code/hstore-icontains/lookup_test/tests.py", line 12, in test_icontains
        data__icontains={'foo': 'bar'}
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/models/manager.py", line 92, in manager_method
        return getattr(self.get_queryset(), name)(*args, **kwargs)
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/models/query.py", line 351, in get
        num = len(clone)
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/models/query.py", line 122, in __len__
        self._fetch_all()
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/models/query.py", line 966, in _fetch_all
        self._result_cache = list(self.iterator())
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/models/query.py", line 265, in iterator
        for row in compiler.results_iter():
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 700, in results_iter
        for rows in self.execute_sql(MULTI):
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 786, in execute_sql
        cursor.execute(sql, params)
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/backends/utils.py", line 65, in execute
        return self.cursor.execute(sql, params)
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/utils.py", line 94, in __exit__
        six.reraise(dj_exc_type, dj_exc_value, traceback)
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/backends/utils.py", line 65, in execute
        return self.cursor.execute(sql, params)
    ProgrammingError: operator does not exist: text -> unknown
    LINE 1: ...WHERE (UPPER("lookup_test_somemodel"."data"::text)->'foo') =...
                                                                 ^
    HINT:  No operator matches the given name and argument type(s). You might need to add explicit type casts.


    ----------------------------------------------------------------------
    Ran 1 test in 0.011s

    FAILED (errors=1)
    Creating test database for alias 'default'...
    Destroying test database for alias 'default'...

# `django_hstore` 1.3.6, `django` 1.6.8

    E
    ======================================================================
    ERROR: test_icontains (lookup_test.tests.IContainsTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/spike/Code/hstore-icontains/lookup_test/tests.py", line 12, in test_icontains
        data__icontains={'foo': 'bar'}
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/models/manager.py", line 151, in get
        return self.get_queryset().get(*args, **kwargs)
      File "/Users/spike/.virtualenvs/hstore-icontains/lib/python2.7/site-packages/django/db/models/query.py", line 310, in get
        self.model._meta.object_name)
    DoesNotExist: SomeModel matching query does not exist.

    ----------------------------------------------------------------------
    Ran 1 test in 0.012s

    FAILED (errors=1)
    Creating test database for alias 'default'...
    Destroying test database for alias 'default'...
