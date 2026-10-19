"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipQueryComputePaymentConfig``."""

from typing_extensions import TypedDict


class MembershipQueryComputePaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates whether the collaboration member has accepted to pay for query compute costs (<code>TRUE</code>) or has not accepted to pay for query compute costs (<code>FALSE</code>).</p> <p>If the collaboration creator has not specified anyone to pay for query compute costs, then the member who can query is the default payer. </p> <p>An error message is returned for the following reasons: </p> <ul> <li> <p>If you set the value to <code>FALSE</code> but you are responsible to pay for query compute costs. </p> </li> <li> <p>If you set the value to <code>TRUE</code> but you are not responsible to pay for query compute costs. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipQueryComputePaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> MembershipQueryComputePaymentConfig:
    out: MembershipQueryComputePaymentConfig = {}  # type: ignore[typeddict-item]
    if data.get("isResponsible") is not None:
        out["is_responsible"] = data["isResponsible"]
    else:
        out["is_responsible"] = False
    return out
