"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.tag_keys
    import capo_mwaa_serverless.types.taggable_resource_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>"""
    tag_keys: "capo_mwaa_serverless.types.tag_keys.TagKeys"
    """<p>A list of tag keys to remove from the resource. Only the keys are required; the values are ignored.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_mwaa_serverless.types.tag_keys

    out["TagKeys"] = capo_mwaa_serverless.types.tag_keys.serialize_aws_json_1_0(
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
        import capo_mwaa_serverless.types.tag_keys

        out["tag_keys"] = capo_mwaa_serverless.types.tag_keys.deserialize_aws_json_1_0(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
