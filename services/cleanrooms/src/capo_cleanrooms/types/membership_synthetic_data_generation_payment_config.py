"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipSyntheticDataGenerationPaymentConfig``."""

from typing_extensions import TypedDict


class MembershipSyntheticDataGenerationPaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates if this membership is responsible for paying for synthetic data generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipSyntheticDataGenerationPaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> MembershipSyntheticDataGenerationPaymentConfig:
    out: MembershipSyntheticDataGenerationPaymentConfig = {}  # type: ignore[typeddict-item]
    if data.get("isResponsible") is not None:
        out["is_responsible"] = data["isResponsible"]
    else:
        out["is_responsible"] = False
    return out
