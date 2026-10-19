"""Generated from Smithy shape ``com.amazonaws.apprunner#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p> <p>It must be the ARN of an App Runner resource.</p>"""
    tag_keys: "capo_apprunner.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys that you want to remove.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_apprunner.types.tag_key_list

    out["TagKeys"] = capo_apprunner.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_apprunner.types.tag_key_list

        out["tag_keys"] = capo_apprunner.types.tag_key_list.deserialize_aws_json_1_0(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
