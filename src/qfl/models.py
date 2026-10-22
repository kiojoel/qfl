from datetime import datetime, timezone

from pydantic import BaseModel, Field, field_validator


class PricePoint(BaseModel):
    symbol: str = Field(
        ..., min_length=1, description="Instrument identifier, e.g. BTC"
    )
    price: float = Field(..., gt=0, description="Price in the quote currency")
    currency: str = Field(..., min_length=1, description="Quote currency, e.g. USD")
    timestamp: datetime = Field(
        ...,
        description="Observation time in UTC",
    )

    @field_validator("timestamp")
    @classmethod
    def ensure_utc(cls, value: datetime) -> datetime:
        if value.tzinfo is None:
            raise ValueError("timestamp must be timezone-aware (UTC)")
        return value.astimezone(timezone.utc)

    @field_validator("symbol", "currency")
    @classmethod
    def normalize_upper(cls, value: str) -> str:
        return value.strip().upper()
