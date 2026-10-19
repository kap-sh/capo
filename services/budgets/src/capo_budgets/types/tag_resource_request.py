"""Generated from Smithy shape ``com.amazonaws.budgets#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.amazon_resource_name
    import capo_budgets.types.resource_tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_budgets.types.amazon_resource_name.AmazonResourceName"
    """<p>The unique identifier for the resource.</p>"""
    resource_tags: "capo_budgets.types.resource_tag_list.ResourceTagList"
    """<p>The tags associated with the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_budgets.types.resource_tag_list

    out["ResourceTags"] = capo_budgets.types.resource_tag_list.serialize_aws_json_1_1(
        value["resource_tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("ResourceTags") is not None:
        import capo_budgets.types.resource_tag_list

        out["resource_tags"] = (
            capo_budgets.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    else:
        out["resource_tags"] = []
    return out
