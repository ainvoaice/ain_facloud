from app.mainapp import create_app
app = create_app()  #Dependency injection


# import fastapi, os
# from sqlalchemy import create_engine, text
 
# app = fastapi.FastAPI()
# DATABASE_URL = os.environ.get("AIN_SUPA") or os.environ.get("DATABASE_URL")
# if not DATABASE_URL:raise RuntimeError("No database URL found! Set AIN_SUPA or DATABASE_URL.")


# engine = create_engine(DATABASE_URL)

# @app.get("/")
# def main():
#     return {"message": "Hello World"}

# @app.get("/test-db")
# def test_db():
#     try:
#         with engine.connect() as conn:
#             conn.execute(text("SELECT 1"))
#         return {"success": True, "message": "Connected!"}
#     except Exception as e:
#         return {"success": False, "error": str(e)}