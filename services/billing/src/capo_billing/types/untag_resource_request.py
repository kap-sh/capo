"""Generated from Smithy shape ``com.amazonaws.billing#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.resource_arn
    import capo_billing.types.resource_tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_billing.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the resource. </p>"""
    resource_tag_keys: "capo_billing.types.resource_tag_key_list.ResourceTagKeyList"
    """<p> A list of tag key value pairs that are associated with the resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_billing.types.resource_tag_key_list

    out["resourceTagKeys"] = (
        capo_billing.types.resource_tag_key_list.serialize_aws_json_1_0(
            value["resource_tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("resourceTagKeys") is not None:
        import capo_billing.types.resource_tag_key_list

        out["resource_tag_keys"] = (
            capo_billing.types.resource_tag_key_list.deserialize_aws_json_1_0(
                data["resourceTagKeys"]
            )
        )
    else:
        out["resource_tag_keys"] = []
    return out
