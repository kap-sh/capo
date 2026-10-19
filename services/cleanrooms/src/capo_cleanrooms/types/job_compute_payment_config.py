"""Generated from Smithy shape ``com.amazonaws.cleanrooms#JobComputePaymentConfig``."""

from typing_extensions import TypedDict


class JobComputePaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates whether the collaboration creator has configured the collaboration member to pay for query and job compute costs (<code>TRUE</code>) or has not configured the collaboration member to pay for query and job compute costs (<code>FALSE</code>).</p> <p>One or more members can be configured as payer candidates for query and job compute costs.</p> <p>An error is returned if the collaboration creator sets a <code>FALSE</code> value for the member who can run queries and jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobComputePaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> JobComputePaymentConfig:
    out: JobComputePaymentConfig = {}  # type: ignore[typeddict-item]
    if data.get("isResponsible") is not None:
        out["is_responsible"] = data["isResponsible"]
    else:
        out["is_responsible"] = False
    return out
