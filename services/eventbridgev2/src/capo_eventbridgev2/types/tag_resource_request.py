"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.tag_map
    import capo_eventbridgev2.types.taggable_resource_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_eventbridgev2.types.taggable_resource_arn.TaggableResourceArn"
    tags: "capo_eventbridgev2.types.tag_map.TagMap"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_eventbridgev2.types.tag_map

    out["Tags"] = capo_eventbridgev2.types.tag_map.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_eventbridgev2.types.tag_map

        out["tags"] = capo_eventbridgev2.types.tag_map.deserialize_cbor(data["Tags"])
    else:
        out["tags"] = {}
    return out
