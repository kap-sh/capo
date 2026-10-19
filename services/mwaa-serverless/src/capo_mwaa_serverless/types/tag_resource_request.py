"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.taggable_resource_arn
    import capo_mwaa_serverless.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to which to add tags.</p>"""
    tags: "capo_mwaa_serverless.types.tags.Tags"
    """<p>A map of tags to add to the resource. Each tag consists of a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_mwaa_serverless.types.tags

    out["Tags"] = capo_mwaa_serverless.types.tags.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_mwaa_serverless.types.tags

        out["tags"] = capo_mwaa_serverless.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        out["tags"] = {}
    return out
