"""Generated from Smithy shape ``com.amazonaws.billing#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.resource_arn
    import capo_billing.types.resource_tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_billing.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the resource. </p>"""
    resource_tags: "capo_billing.types.resource_tag_list.ResourceTagList"
    """<p> A list of tag key value pairs that are associated with the resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_billing.types.resource_tag_list

    out["resourceTags"] = capo_billing.types.resource_tag_list.serialize_aws_json_1_0(
        value["resource_tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("resourceTags") is not None:
        import capo_billing.types.resource_tag_list

        out["resource_tags"] = (
            capo_billing.types.resource_tag_list.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    else:
        out["resource_tags"] = []
    return out
