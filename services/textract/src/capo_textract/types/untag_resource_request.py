"""Generated from Smithy shape ``com.amazonaws.textract#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.amazon_resource_name
    import capo_textract.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_textract.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) that specifies the resource to be untagged.</p>"""
    tag_keys: "capo_textract.types.tag_key_list.TagKeyList"
    """<p>Specifies the tags to be removed from the resource specified by the ResourceARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_textract.types.tag_key_list

    out["TagKeys"] = capo_textract.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_textract.types.tag_key_list

        out["tag_keys"] = capo_textract.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
