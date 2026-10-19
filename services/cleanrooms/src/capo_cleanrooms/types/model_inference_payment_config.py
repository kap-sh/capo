"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ModelInferencePaymentConfig``."""

from typing_extensions import TypedDict


class ModelInferencePaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates whether the collaboration creator has configured the collaboration member to pay for model inference costs (<code>TRUE</code>) or has not configured the collaboration member to pay for model inference costs (<code>FALSE</code>).</p> <p>One or more members can be configured as payer candidates for model inference costs.</p> <p>If the collaboration creator hasn't specified anyone as the member paying for model inference costs, then the member who can query is the default payer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelInferencePaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> ModelInferencePaymentConfig:
    out: ModelInferencePaymentConfig = {}  # type: ignore[typeddict-item]
    if data.get("isResponsible") is not None:
        out["is_responsible"] = data["isResponsible"]
    else:
        out["is_responsible"] = False
    return out
