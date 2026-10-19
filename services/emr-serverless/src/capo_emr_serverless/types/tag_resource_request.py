"""Generated from Smithy shape ``com.amazonaws.emrserverless#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.resource_arn
    import capo_emr_serverless.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_emr_serverless.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon EMR Serverless applications and job runs.</p>"""
    tags: "capo_emr_serverless.types.tag_map.TagMap"
    """<p>The tags to add to the resource. A tag is an array of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_emr_serverless.types.tag_map

    out["tags"] = capo_emr_serverless.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_emr_serverless.types.tag_map

        out["tags"] = capo_emr_serverless.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
