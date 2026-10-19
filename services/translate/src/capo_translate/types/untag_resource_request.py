"""Generated from Smithy shape ``com.amazonaws.translate#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_translate.types.resource_arn
    import capo_translate.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_translate.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the given Amazon Translate resource from which you want to remove the tags. </p>"""
    tag_keys: "capo_translate.types.tag_key_list.TagKeyList"
    """<p>The initial part of a key-value pair that forms a tag being removed from a given resource. Keys must be unique and cannot be duplicated for a particular resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_translate.types.tag_key_list

    out["TagKeys"] = capo_translate.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_translate.types.tag_key_list

        out["tag_keys"] = capo_translate.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
