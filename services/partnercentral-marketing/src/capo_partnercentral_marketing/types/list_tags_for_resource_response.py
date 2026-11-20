"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.tag_list
    import capo_partnercentral_marketing.types.taggable_resource_arn


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_arn: (
        "capo_partnercentral_marketing.types.taggable_resource_arn.TaggableResourceArn"
    )
    """The ARN of the resource the tags belong to."""
    tags: NotRequired["capo_partnercentral_marketing.types.tag_list.TagList"]
    """The tags currently applied. Absent rather than empty when the resource carries no tags."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import capo_partnercentral_marketing.types.tag_list

        out["Tags"] = capo_partnercentral_marketing.types.tag_list.serialize_cbor(
            value["tags"]
        )
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_partnercentral_marketing.types.tag_list

        out["tags"] = capo_partnercentral_marketing.types.tag_list.deserialize_cbor(
            data["Tags"]
        )
    return out
