"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipJobComputePaymentConfig``."""

from typing_extensions import TypedDict


class MembershipJobComputePaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates whether the collaboration member has accepted to pay for job compute costs (<code>TRUE</code>) or has not accepted to pay for query and job compute costs (<code>FALSE</code>).</p> <p>There can be one or more members who are designated as payer candidates for queries and jobs. </p> <p>An error message is returned for the following reasons: </p> <ul> <li> <p>If you set the value to <code>FALSE</code> but you are responsible to pay for query and job compute costs. </p> </li> <li> <p>If you set the value to <code>TRUE</code> but you are not responsible to pay for query and job compute costs. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipJobComputePaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> MembershipJobComputePaymentConfig:
    out: MembershipJobComputePaymentConfig = {}  # type: ignore[typeddict-item]
    if data.get("isResponsible") is not None:
        out["is_responsible"] = data["isResponsible"]
    else:
        out["is_responsible"] = False
    return out
