"""Generated from Smithy shape ``com.amazonaws.health#AccountTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.account_tag_type
    import capo_health.types.tag_key
    import capo_health.types.tag_value


class AccountTag(TypedDict, closed=True):
    key: NotRequired["capo_health.types.tag_key.tagKey"]
    """<p>The tag key.</p>"""
    value: NotRequired["capo_health.types.tag_value.tagValue"]
    """<p>The tag value.</p>"""
    type: NotRequired["capo_health.types.account_tag_type.AccountTagType"]
    """<p>The type of tag (resource tag or account tag).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountTag) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    if "type" in value:
        import capo_health.types.account_tag_type

        out["type"] = capo_health.types.account_tag_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountTag:
    out: AccountTag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("type") is not None:
        import capo_health.types.account_tag_type

        out["type"] = capo_health.types.account_tag_type.deserialize_aws_json_1_1(
            data["type"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountTag) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    if "type" in value:
        import capo_health.types.account_tag_type

        out["type"] = capo_health.types.account_tag_type.serialize_cbor(value["type"])
    return out


def deserialize_cbor(data: dict) -> AccountTag:
    out: AccountTag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("type") is not None:
        import capo_health.types.account_tag_type

        out["type"] = capo_health.types.account_tag_type.deserialize_cbor(data["type"])
    return out
