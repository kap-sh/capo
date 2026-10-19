"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipModelTrainingPaymentConfig``."""

from typing_extensions import TypedDict


class MembershipModelTrainingPaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates whether the collaboration member has accepted to pay for model training costs (<code>TRUE</code>) or has not accepted to pay for model training costs (<code>FALSE</code>).</p> <p>If the collaboration creator has not specified anyone to pay for model training costs, then the member who can query is the default payer. </p> <p>An error message is returned for the following reasons: </p> <ul> <li> <p>If you set the value to <code>FALSE</code> but you are responsible to pay for model training costs. </p> </li> <li> <p>If you set the value to <code>TRUE</code> but you are not responsible to pay for model training costs. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipModelTrainingPaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> MembershipModelTrainingPaymentConfig:
    out: MembershipModelTrainingPaymentConfig = {}  # type: ignore[typeddict-item]
    if data.get("isResponsible") is not None:
        out["is_responsible"] = data["isResponsible"]
    else:
        out["is_responsible"] = False
    return out
