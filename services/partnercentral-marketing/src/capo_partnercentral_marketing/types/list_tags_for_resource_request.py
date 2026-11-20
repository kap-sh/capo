"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.taggable_resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_partnercentral_marketing.types.taggable_resource_arn.TaggableResourceArn"
    )
    """The ARN of the resource whose tags should be returned."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
