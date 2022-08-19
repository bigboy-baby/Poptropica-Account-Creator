#Code by bigboybigboi#0001 skid if ur homosexual (ew)
import requests, random, string, threading

def create():
  while True:
    rnd = ('').join(random.choices(string.ascii_letters + string.digits, k=10))
    d = {
      'login': f'big{rnd}',
      'pass_hash': '18fb1913594bb2b48e638b240f162544',
    }

    r = requests.post('https://poptropica.com/reguser.php', data=d)

    s = r.text
    ss = s.split("=")
    if ss[1] == "ok&login":
      print(f"Account Created | Username big{rnd} // Password Hashed: 18fb1913594bb2b48e638b240f162544")
      f = open("Accounts.txt", "a")
      f.write(f"big{rnd}:18fb1913594bb2b48e638b240f162544\n")
      f.close()
    else:
      print(f"Failed | Username:big{rnd}")


am = int(input("Threads: "))

threads = list()
for index in range(am):
  x = threading.Thread(target=create)
  threads.append(x)
  x.start()
for index, thread in enumerate(threads):
  thread.join()
