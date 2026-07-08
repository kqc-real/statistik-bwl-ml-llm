"""Reproduzierbare didaktische Datensätze für den Statistik-BWL-Kurs."""
from __future__ import annotations

import numpy as np
import pandas as pd


def online_retail(n: int = 12_000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    countries = np.array(["United Kingdom", "Germany", "France", "Netherlands", "Spain"])
    descriptions = np.array([
        "WHITE HANGING HEART T-LIGHT HOLDER", "JUMBO BAG RED RETROSPOT",
        "REGENCY CAKESTAND 3 TIER", "PARTY BUNTING", "LUNCH BAG RED RETROSPOT",
        "SET OF 3 CAKE TINS PANTRY DESIGN", "ASSORTED COLOUR BIRD ORNAMENT",
    ])
    dates = pd.Timestamp("2011-01-01") + pd.to_timedelta(rng.integers(0, 330, n), unit="D")
    customer_ids = rng.integers(12300, 18200, n).astype(float)
    customer_ids[rng.random(n) < 0.08] = np.nan
    quantity = np.maximum(1, rng.negative_binomial(2, 0.28, n))
    unit_price = np.round(rng.lognormal(mean=1.0, sigma=0.85, size=n), 2)
    invoice_numbers = 500000 + rng.integers(0, 2500, n)
    cancelled = rng.random(n) < 0.025
    invoice = invoice_numbers.astype(str)
    invoice[cancelled] = np.char.add("C", invoice[cancelled])
    quantity[cancelled] *= -1
    unit_price[rng.random(n) < 0.004] = 0
    return pd.DataFrame({
        "InvoiceNo": invoice,
        "StockCode": rng.integers(10000, 99999, n).astype(str),
        "Description": rng.choice(descriptions, n),
        "Quantity": quantity,
        "InvoiceDate": dates,
        "UnitPrice": unit_price,
        "CustomerID": customer_ids,
        "Country": rng.choice(countries, n, p=[0.80, 0.07, 0.06, 0.04, 0.03]),
    })


def online_shoppers(n: int = 6_000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    product_pages = rng.poisson(30, n)
    product_duration = np.maximum(0, rng.gamma(2.2, 350, n) + product_pages * 8)
    bounce = np.clip(rng.beta(1.2, 12, n) * 0.25, 0, 0.20)
    exit_rate = np.clip(bounce + rng.beta(1.5, 8, n) * 0.18, 0, 0.30)
    page_value = np.where(rng.random(n) < 0.65, 0, rng.gamma(2.0, 8.0, n))
    returning = rng.random(n) < 0.72
    weekend = rng.random(n) < 0.28
    month = rng.choice(["Feb", "Mar", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], n)
    special_day = np.where(rng.random(n) < 0.12, rng.choice([0.2, 0.4, 0.6, 0.8, 1.0], n), 0)
    logit = (-3.2 + 0.055 * page_value + 0.00035 * product_duration + 0.35 * returning
             - 6.0 * bounce - 2.0 * exit_rate + 0.12 * weekend)
    prob = 1 / (1 + np.exp(-logit))
    revenue = rng.random(n) < prob
    return pd.DataFrame({
        "Administrative": rng.poisson(2.3, n),
        "Administrative_Duration": rng.gamma(1.6, 55, n),
        "Informational": rng.poisson(0.5, n),
        "Informational_Duration": rng.gamma(1.2, 25, n),
        "ProductRelated": product_pages,
        "ProductRelated_Duration": product_duration,
        "BounceRates": bounce,
        "ExitRates": exit_rate,
        "PageValues": page_value,
        "SpecialDay": special_day,
        "Month": month,
        "OperatingSystems": rng.integers(1, 9, n),
        "Browser": rng.integers(1, 14, n),
        "Region": rng.integers(1, 10, n),
        "TrafficType": rng.integers(1, 21, n),
        "VisitorType": np.where(returning, "Returning_Visitor", "New_Visitor"),
        "Weekend": weekend,
        "Revenue": revenue,
    })


def bike_sharing(n: int = 731, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    day = np.arange(1, n + 1)
    yr = (day > 365).astype(int)
    season = ((day % 365) // 91 + 1).clip(1, 4)
    weekday = day % 7
    holiday = rng.random(n) < 0.03
    workingday = (~holiday) & (~np.isin(weekday, [0, 6]))
    weathersit = rng.choice([1, 2, 3], n, p=[0.67, 0.27, 0.06])
    temp = np.clip(0.5 + 0.27 * np.sin(2 * np.pi * (day % 365) / 365 - 1.2) + rng.normal(0, 0.08, n), 0.05, 0.95)
    atemp = np.clip(temp + rng.normal(0, 0.035, n), 0.03, 1.0)
    hum = np.clip(0.62 + 0.10 * (weathersit - 1) + rng.normal(0, 0.10, n), 0.2, 1.0)
    windspeed = np.clip(rng.beta(2, 5, n) * 0.6, 0, 0.6)
    base = 1800 + 3100 * yr + 3800 * temp - 700 * (weathersit - 1) - 900 * hum + 250 * workingday
    cnt = np.maximum(120, base + rng.normal(0, 650, n)).astype(int)
    registered = np.maximum(0, (cnt * rng.uniform(0.65, 0.88, n)).astype(int))
    casual = cnt - registered
    return pd.DataFrame({
        "instant": day,
        "dteday": pd.Timestamp("2011-01-01") + pd.to_timedelta(day - 1, unit="D"),
        "season": season,
        "yr": yr,
        "mnth": ((day % 365) // 30 + 1).clip(1, 12),
        "holiday": holiday.astype(int),
        "weekday": weekday,
        "workingday": workingday.astype(int),
        "weathersit": weathersit,
        "temp": temp,
        "atemp": atemp,
        "hum": hum,
        "windspeed": windspeed,
        "casual": casual,
        "registered": registered,
        "cnt": cnt,
    })
