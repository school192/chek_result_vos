import requests

def get_results(token):
    r = requests.post("https://online.olimpiada.ru/smt-portal/register/login", json={"token":token}).json()
    if not "canPassTest" in r:
        return ["Не участвовал"]
    r = r["canPassTest"]
    r = requests.get(f"https://online.olimpiada.ru/smt-portal/test?regQuizId={r["liContestId"]}&sid={r["liSessionId"]}").json()
    t = list(filter(lambda t: t["tag"] == "HasResults", r["tsInfo"]["contents"]))
    return r["tsUser"]["userName"], t[0]["contents"]["userScore"] if len(t) > 0 else "Не участвовал"

print("Введите коды, затем \"exec\"")
lines = []
while (line := input()) != "exec":
    line = line.strip()
    if len(line) > 0:
        lines.append(line)

print("----------------------------------")

for t in lines:
    print(t, *get_results(t), sep=" == ")
