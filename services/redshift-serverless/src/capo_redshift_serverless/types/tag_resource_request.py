"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.amazon_resource_name
    import capo_redshift_serverless.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_redshift_serverless.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "capo_redshift_serverless.types.tag_list.TagList"
    """<p>The map of the key-value pairs used to tag the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_redshift_serverless.types.tag_list

    out["tags"] = capo_redshift_serverless.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_redshift_serverless.types.tag_list

        out["tags"] = capo_redshift_serverless.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = []
    return out
