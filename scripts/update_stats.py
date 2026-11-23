"""Refresh the commit tiles in the profile README from GitHub contribution data.

Month  = commits since the 1st of the current month (UTC).
Total  = every commit since the account was created, summed in 1-year windows
         because GitHub caps a single contribution query at one year.
"""
import json, os, re, urllib.request
from datetime import datetime, timedelta, timezone

LOGIN = "pritam-crimson"
TOKEN = os.environ["STATS_TOKEN"]


def gql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        json.dumps({"query": query, "variables": variables}).encode(),
        {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    )
    return json.load(urllib.request.urlopen(req))["data"]["user"]


def commits(start, end):
    q = ('query($l:String!,$f:DateTime!,$t:DateTime!){user(login:$l){'
         'contributionsCollection(from:$f,to:$t){totalCommitContributions}}}')
    u = gql(q, {"l": LOGIN, "f": start.isoformat(), "t": end.isoformat()})
    return u["contributionsCollection"]["totalCommitContributions"]


now = datetime.now(timezone.utc)
month = commits(now.replace(day=1, hour=0, minute=0, second=0, microsecond=0), now)

created = gql("query($l:String!){user(login:$l){createdAt}}", {"l": LOGIN})["createdAt"]
start = datetime.fromisoformat(created.replace("Z", "+00:00"))
total = 0
while start < now:
    end = min(start + timedelta(days=364), now)
    total += commits(start, end)
    start = end

svg = (open("assets/stats-template.svg").read()
       .replace("{{MONTH}}", f"{month:,}").replace("{{TOTAL}}", f"{total:,}"))
open("assets/stats.svg", "w").write(svg)

readme = open("README.md").read()
readme = re.sub(r'assets/stats[^"?]*\.svg(\?v=[\w-]+)?', f"assets/stats.svg?v={month}-{total}", readme)
open("README.md", "w").write(readme)
print("month:", month, "total:", total)
