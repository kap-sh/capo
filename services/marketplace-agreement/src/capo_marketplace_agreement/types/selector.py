"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Selector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string


class Selector(TypedDict, closed=True):
    type: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>Category of selector.</p>"""
    value: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>Contract duration. This field supports the ISO 8601 format. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Selector) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Selector:
    out: Selector = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Selector) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> Selector:
    out: Selector = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
