"""Generated from Smithy shape ``com.amazonaws.budgets#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.amazon_resource_name
    import capo_budgets.types.resource_tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_budgets.types.amazon_resource_name.AmazonResourceName"
    """<p>The unique identifier for the resource.</p>"""
    resource_tag_keys: "capo_budgets.types.resource_tag_key_list.ResourceTagKeyList"
    """<p>The key that's associated with the tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_budgets.types.resource_tag_key_list

    out["ResourceTagKeys"] = (
        capo_budgets.types.resource_tag_key_list.serialize_aws_json_1_1(
            value["resource_tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("ResourceTagKeys") is not None:
        import capo_budgets.types.resource_tag_key_list

        out["resource_tag_keys"] = (
            capo_budgets.types.resource_tag_key_list.deserialize_aws_json_1_1(
                data["ResourceTagKeys"]
            )
        )
    else:
        out["resource_tag_keys"] = []
    return out
