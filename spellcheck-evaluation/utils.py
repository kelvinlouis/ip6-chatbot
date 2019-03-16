def proxy_debug(activate):
  """Creates a proxied debugger, if the first parameter is true"""

  def debug_dummy(msg):
    return

  def debug(msg):
    print(msg)
    return

  if activate == True:
    return debug
  else:
    return debug_dummy
