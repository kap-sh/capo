"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.tag_key
    import capo_partnercentral_marketing.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_partnercentral_marketing.types.tag_key.TagKey"
    """The tag key."""
    value: "capo_partnercentral_marketing.types.tag_value.TagValue"
    """The tag value."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
