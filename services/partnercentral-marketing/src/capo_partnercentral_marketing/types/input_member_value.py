"""Generated from Smithy shape ``aws.iam#InputMemberValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.input_member_reference


class InputMemberValue(TypedDict, closed=True):
    member: "capo_partnercentral_marketing.types.input_member_reference.InputMemberReference"
    """Reference to a member in the operation's input."""
    value: "object"
    """Value to compare against the member's value."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InputMemberValue) -> dict:
    out: dict = {}
    out["member"] = value["member"]
    out["value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> InputMemberValue:
    out: InputMemberValue = {}  # type: ignore[typeddict-item]
    if data.get("member") is not None:
        out["member"] = data["member"]
    else:
        out["member"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = None
    return out
