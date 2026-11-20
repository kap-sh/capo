"""Generated from Smithy shape ``aws.iam#InputListMemberValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.input_list_member


class InputListMemberValue(TypedDict, closed=True):
    member: "capo_partnercentral_marketing.types.input_list_member.InputListMember"
    """Reference to a list member in the operation's input."""
    value: "object"
    """Value to check for in the list."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InputListMemberValue) -> dict:
    out: dict = {}
    out["member"] = value["member"]
    out["value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> InputListMemberValue:
    out: InputListMemberValue = {}  # type: ignore[typeddict-item]
    if data.get("member") is not None:
        out["member"] = data["member"]
    else:
        out["member"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = None
    return out
