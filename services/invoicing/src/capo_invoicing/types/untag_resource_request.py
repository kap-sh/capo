"""Generated from Smithy shape ``com.amazonaws.invoicing#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.resource_tag_key_list
    import capo_invoicing.types.tagris_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_invoicing.types.tagris_arn.TagrisArn"
    """<p> The Amazon Resource Name (ARN) to untag. </p>"""
    resource_tag_keys: "capo_invoicing.types.resource_tag_key_list.ResourceTagKeyList"
    """<p> Keys for the tags to be removed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_invoicing.types.resource_tag_key_list

    out["ResourceTagKeys"] = (
        capo_invoicing.types.resource_tag_key_list.serialize_aws_json_1_0(
            value["resource_tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("ResourceTagKeys") is not None:
        import capo_invoicing.types.resource_tag_key_list

        out["resource_tag_keys"] = (
            capo_invoicing.types.resource_tag_key_list.deserialize_aws_json_1_0(
                data["ResourceTagKeys"]
            )
        )
    else:
        out["resource_tag_keys"] = []
    return out
