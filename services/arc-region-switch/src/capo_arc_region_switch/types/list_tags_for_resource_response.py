"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_tags: NotRequired["capo_arc_region_switch.types.tags.Tags"]
    """<p>The tags for a resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import capo_arc_region_switch.types.tags

        out["resourceTags"] = capo_arc_region_switch.types.tags.serialize_aws_json_1_0(
            value["resource_tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceTags") is not None:
        import capo_arc_region_switch.types.tags

        out["resource_tags"] = (
            capo_arc_region_switch.types.tags.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import capo_arc_region_switch.types.tags

        out["resourceTags"] = capo_arc_region_switch.types.tags.serialize_cbor(
            value["resource_tags"]
        )
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceTags") is not None:
        import capo_arc_region_switch.types.tags

        out["resource_tags"] = capo_arc_region_switch.types.tags.deserialize_cbor(
            data["resourceTags"]
        )
    return out
