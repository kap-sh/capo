"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SyntheticDataGenerationPaymentConfig``."""

from typing_extensions import TypedDict


class SyntheticDataGenerationPaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates who is responsible for paying for synthetic data generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyntheticDataGenerationPaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> SyntheticDataGenerationPaymentConfig:
    out: SyntheticDataGenerationPaymentConfig = {}  # type: ignore[typeddict-item]
    if data.get("isResponsible") is not None:
        out["is_responsible"] = data["isResponsible"]
    else:
        out["is_responsible"] = False
    return out
