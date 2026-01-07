import pandas as pd
import logging
from .models import UserRecord

logger = logging.getLogger('core')

REQUIRED_COLUMNS = {'Id', 'Name', 'Age', 'Education'}

def process_excel(file_path):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path, encoding='utf-8', errors='ignore')
        else:
            df = pd.read_excel(file_path)
    except Exception as e:
        logger.error(f"File read error: {e}")
        return 0, 0

    if not REQUIRED_COLUMNS.issubset(df.columns):
        logger.error("Invalid Excel format")
        return 0, 0

    inserted = skipped = 0

    for _, row in df.iterrows():
        try:
            excel_id = int(row['Id'])
            name = str(row['Name']).strip()
            age = int(row['Age'])
            education = str(row['Education']).strip()

            if not name or age <= 0 or not education:
                raise ValueError("Validation failed")

            UserRecord.objects.create(
                excel_id=excel_id,
                name=name,
                age=age,
                education=education
            )
            inserted += 1

        except Exception as e:
            skipped += 1
            logger.info(f"Skipped row {row.to_dict()} | {e}")

    return inserted, skipped