"""Generated from Smithy shape ``com.amazonaws.codedeploy#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.arn
    import capo_codedeploy.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_codedeploy.types.arn.Arn"
    """<p> The Amazon Resource Name (ARN) that specifies from which resource to disassociate the tags with the keys in the <code>TagKeys</code> input parameter. </p>"""
    tag_keys: "capo_codedeploy.types.tag_key_list.TagKeyList"
    """<p> A list of keys of <code>Tag</code> objects. The <code>Tag</code> objects identified by the keys are disassociated from the resource specified by the <code>ResourceArn</code> input parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_codedeploy.types.tag_key_list

    out["TagKeys"] = capo_codedeploy.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_codedeploy.types.tag_key_list

        out["tag_keys"] = capo_codedeploy.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
