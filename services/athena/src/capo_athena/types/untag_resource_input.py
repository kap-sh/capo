"""Generated from Smithy shape ``com.amazonaws.athena#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.amazon_resource_name
    import capo_athena.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_athena.types.amazon_resource_name.AmazonResourceName"
    """<p>Specifies the ARN of the resource from which tags are to be removed.</p>"""
    tag_keys: "capo_athena.types.tag_key_list.TagKeyList"
    """<p>A comma-separated list of one or more tag keys whose tags are to be removed from the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_athena.types.tag_key_list

    out["TagKeys"] = capo_athena.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_athena.types.tag_key_list

        out["tag_keys"] = capo_athena.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
