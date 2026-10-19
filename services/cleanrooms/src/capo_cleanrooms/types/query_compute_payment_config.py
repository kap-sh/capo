"""Generated from Smithy shape ``com.amazonaws.cleanrooms#QueryComputePaymentConfig``."""

from typing_extensions import TypedDict


class QueryComputePaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates whether the collaboration creator has configured the collaboration member to pay for query compute costs (<code>TRUE</code>) or has not configured the collaboration member to pay for query compute costs (<code>FALSE</code>).</p> <p>One or more members can be configured as payer candidates for query compute costs.</p> <p>If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryComputePaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> QueryComputePaymentConfig:
    out: QueryComputePaymentConfig = {}  # type: ignore[typeddict-item]
    if data.get("isResponsible") is not None:
        out["is_responsible"] = data["isResponsible"]
    else:
        out["is_responsible"] = False
    return out
