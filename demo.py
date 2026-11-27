"""Local model only: no market feed or order execution."""
from analytics import option_price
import argparse, json
p=argparse.ArgumentParser();p.add_argument('--spot',type=float,default=100);p.add_argument('--strike',type=float,default=100);p.add_argument('--days',type=int,default=30);p.add_argument('--vol',type=float,default=20);p.add_argument('--rate',type=float,default=2);p.add_argument('--type',choices=['call','put'],default='call');a=p.parse_args();print(json.dumps(option_price(a.spot,a.strike,a.days,a.vol,a.rate,a.type),indent=2))
