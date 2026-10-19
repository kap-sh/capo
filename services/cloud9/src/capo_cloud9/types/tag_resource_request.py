"""Generated from Smithy shape ``com.amazonaws.cloud9#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_arn
    import capo_cloud9.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_cloud9.types.environment_arn.EnvironmentArn"
    """<p>The Amazon Resource Name (ARN) of the Cloud9 development environment to add tags to.</p>"""
    tags: "capo_cloud9.types.tag_list.TagList"
    """<p>The list of tags to add to the given Cloud9 development environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_cloud9.types.tag_list

    out["Tags"] = capo_cloud9.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_cloud9.types.tag_list

        out["tags"] = capo_cloud9.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    else:
        out["tags"] = []
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
