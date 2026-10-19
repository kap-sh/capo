"""Generated from Smithy shape ``com.amazonaws.acmpca#EdiPartyName``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.string256


class EdiPartyName(TypedDict, closed=True):
    party_name: "capo_acm_pca.types.string256.String256"
    """<p>Specifies the party name.</p>"""
    name_assigner: NotRequired["capo_acm_pca.types.string256.String256"]
    """<p>Specifies the name assigner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdiPartyName) -> dict:
    out: dict = {}
    out["PartyName"] = value["party_name"]
    if "name_assigner" in value:
        out["NameAssigner"] = value["name_assigner"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EdiPartyName:
    out: EdiPartyName = {}  # type: ignore[typeddict-item]
    if data.get("PartyName") is not None:
        out["party_name"] = data["PartyName"]
    else:
        out["party_name"] = ""
    if data.get("NameAssigner") is not None:
        out["name_assigner"] = data["NameAssigner"]
    return out
