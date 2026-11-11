"""Generated from Smithy shape ``com.amazonaws.glue#ResourceUri``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.resource_type
    import capo_glue.types.timestamp
    import capo_glue.types.uri


class ResourceUri(TypedDict, closed=True):
    resource_type: NotRequired["capo_glue.types.resource_type.ResourceType"]
    """<p>The type of the resource.</p>"""
    uri: NotRequired["capo_glue.types.uri.URI"]
    """<p>The URI for accessing the resource.</p>"""
    last_modified: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time at which the resource was last modified in Amazon S3. Glue records this value when you create or update a function whose <code>GovernanceMode</code> is <code>LAKE_FORMATION</code>. Analytics engines use it to verify that the resource hasn't changed. This is an output-only field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceUri) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_glue.types.resource_type

        out["ResourceType"] = capo_glue.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "uri" in value:
        out["Uri"] = value["uri"]
    if "last_modified" in value:
        import capo_glue.types.timestamp

        out["LastModified"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceUri:
    out: ResourceUri = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        import capo_glue.types.resource_type

        out["resource_type"] = capo_glue.types.resource_type.deserialize_aws_json_1_1(
            data["ResourceType"]
        )
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    if data.get("LastModified") is not None:
        import capo_glue.types.timestamp

        out["last_modified"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastModified"]
        )
    return out
