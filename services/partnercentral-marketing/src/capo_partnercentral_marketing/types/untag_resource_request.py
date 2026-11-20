"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.tag_key_list
    import capo_partnercentral_marketing.types.taggable_resource_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_partnercentral_marketing.types.taggable_resource_arn.TaggableResourceArn"
    )
    """The ARN of the resource to remove tags from."""
    tag_keys: "capo_partnercentral_marketing.types.tag_key_list.TagKeyList"
    """The tag keys to remove. Associated values are removed with them."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_partnercentral_marketing.types.tag_key_list

    out["TagKeys"] = capo_partnercentral_marketing.types.tag_key_list.serialize_cbor(
        value["tag_keys"]
    )
    return out


def deserialize_cbor(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_partnercentral_marketing.types.tag_key_list

        out["tag_keys"] = (
            capo_partnercentral_marketing.types.tag_key_list.deserialize_cbor(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
