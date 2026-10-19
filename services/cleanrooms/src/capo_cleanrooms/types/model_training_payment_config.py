"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ModelTrainingPaymentConfig``."""

from typing_extensions import TypedDict


class ModelTrainingPaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates whether the collaboration creator has configured the collaboration member to pay for model training costs (<code>TRUE</code>) or has not configured the collaboration member to pay for model training costs (<code>FALSE</code>).</p> <p>One or more members can be configured as payer candidates for model training costs.</p> <p>If the collaboration creator hasn't specified anyone as the member paying for model training costs, then the member who can query is the default payer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelTrainingPaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> ModelTrainingPaymentConfig:
    out: ModelTrainingPaymentConfig = {}  # type: ignore[typeddict-item]
    if data.get("isResponsible") is not None:
        out["is_responsible"] = data["isResponsible"]
    else:
        out["is_responsible"] = False
    return out
