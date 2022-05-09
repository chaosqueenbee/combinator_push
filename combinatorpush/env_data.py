import os

def retrieve_or_fail(env_var_name):
  val = os.getenv(env_var_name)
  if not val:
     raise Exception(f"Env var \"{env_var_name}\" required, but is missing or empty")

  return val

class EnvData:
  def __init__(self):
    self.magicbell_api_key = retrieve_or_fail("MAGIC_BELL_API_KEY")
    self.magicbell_api_secret = retrieve_or_fail("MAGIC_BELL_API_SECRET")
    self.to_email = retrieve_or_fail("TO_EMAIL")