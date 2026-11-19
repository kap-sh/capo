"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TagOptionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.owner
    import capo_service_catalog.types.tag_option_active
    import capo_service_catalog.types.tag_option_id
    import capo_service_catalog.types.tag_option_key
    import capo_service_catalog.types.tag_option_value


class TagOptionDetail(TypedDict, closed=True):
    key: NotRequired["capo_service_catalog.types.tag_option_key.TagOptionKey"]
    """<p>The TagOption key.</p>"""
    value: NotRequired["capo_service_catalog.types.tag_option_value.TagOptionValue"]
    """<p>The TagOption value.</p>"""
    active: NotRequired["capo_service_catalog.types.tag_option_active.TagOptionActive"]
    """<p>The TagOption active state.</p>"""
    id: NotRequired["capo_service_catalog.types.tag_option_id.TagOptionId"]
    """<p>The TagOption identifier.</p>"""
    owner: NotRequired["capo_service_catalog.types.owner.Owner"]
    """<p>The Amazon Web Services account Id of the owner account that created the TagOption.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagOptionDetail) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "active" in value:
        out["Active"] = value["active"]
    if "id" in value:
        out["Id"] = value["id"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagOptionDetail:
    out: TagOptionDetail = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Active") is not None:
        out["active"] = data["Active"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagOptionDetail) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "active" in value:
        out["Active"] = value["active"]
    if "id" in value:
        out["Id"] = value["id"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_cbor(data: dict) -> TagOptionDetail:
    out: TagOptionDetail = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Active") is not None:
        out["active"] = data["Active"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    return out
