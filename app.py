from fastapi import FastAPI
from scrapers import (fetch_institution_agreements, fetch_agreements_categories,
                      fetch_agreements, fetch_articulation_agreements)

app = FastAPI()

@app.get("/api/institution_agreements/{institution_id}")
async def institution_agreements(institution_id: int):
    return await fetch_institution_agreements(institution_id)

@app.get("/api/agreements_categories")
async def agreements_categories(receiving_institution_id: int, sending_institution_id: int, academic_year_id: int):
    return await fetch_agreements_categories(receiving_institution_id, sending_institution_id, academic_year_id)

@app.get("/api/agreements")
async def agreements(receiving_institution_id: int, sending_institution_id: int, academic_year_id: int, category_code: str):
    return await fetch_agreements(receiving_institution_id, sending_institution_id, academic_year_id, category_code)

@app.get("/api/articulation_agreements/{key}")
async def articulation_agreements(key: str):
    return await fetch_articulation_agreements(key)
