"""Generated from Smithy shape ``com.amazonaws.cloud9#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_arn
    import capo_cloud9.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_cloud9.types.environment_arn.EnvironmentArn"
    """<p>The Amazon Resource Name (ARN) of the Cloud9 development environment to remove tags from.</p>"""
    tag_keys: "capo_cloud9.types.tag_key_list.TagKeyList"
    """<p>The tag names of the tags to remove from the given Cloud9 development environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_cloud9.types.tag_key_list

    out["TagKeys"] = capo_cloud9.types.tag_key_list.serialize_aws_json_1_1(
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
        import capo_cloud9.types.tag_key_list

        out["tag_keys"] = capo_cloud9.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out


def redact_sensitive(value: UntagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tag_keys" in value:
        out["tag_keys"] = "*** Sensitive Data Redacted ***"
    return out
