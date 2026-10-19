"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.arn
    import capo_bcm_data_exports.types.resource_tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_bcm_data_exports.types.arn.Arn"
    """<p>The unique identifier for the resource.</p>"""
    resource_tags: "capo_bcm_data_exports.types.resource_tag_list.ResourceTagList"
    """<p>The tags to associate with the resource. Each tag consists of a key and a value, and each key must be unique for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_bcm_data_exports.types.resource_tag_list

    out["ResourceTags"] = (
        capo_bcm_data_exports.types.resource_tag_list.serialize_aws_json_1_1(
            value["resource_tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("ResourceTags") is not None:
        import capo_bcm_data_exports.types.resource_tag_list

        out["resource_tags"] = (
            capo_bcm_data_exports.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    else:
        out["resource_tags"] = []
    return out
