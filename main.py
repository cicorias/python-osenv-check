import os

def set_environment( environment_set ):
  for k, v in environment_set.items():
    os.environ[k] = v
    pass

def get_environment( environment_set ):
  for k, v in environment_set.items():
    print( '{} = {}'.format( k, os.environ.get(k) ) )
    # pass

def main():
  my_variables = { 'foo': 'bar', 'biz': 'buz', 'fiz': 'foo' }
  set_environment(my_variables)
  get_environment(my_variables)


if __name__ == '__main__':
    # execute only if run as a script
    main()
    