"""Generated from Smithy shape ``com.amazonaws.invoicing#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.resource_tag_list
    import capo_invoicing.types.tagris_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_invoicing.types.tagris_arn.TagrisArn"
    """<p>The Amazon Resource Name (ARN) of the tags. </p>"""
    resource_tags: "capo_invoicing.types.resource_tag_list.ResourceTagList"
    """<p> Adds a tag to a resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_invoicing.types.resource_tag_list

    out["ResourceTags"] = capo_invoicing.types.resource_tag_list.serialize_aws_json_1_0(
        value["resource_tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("ResourceTags") is not None:
        import capo_invoicing.types.resource_tag_list

        out["resource_tags"] = (
            capo_invoicing.types.resource_tag_list.deserialize_aws_json_1_0(
                data["ResourceTags"]
            )
        )
    else:
        out["resource_tags"] = []
    return out
