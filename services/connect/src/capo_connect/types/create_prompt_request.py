"""Generated from Smithy shape ``com.amazonaws.connect#CreatePromptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.common_name_length127
    import capo_connect.types.instance_id
    import capo_connect.types.prompt_description
    import capo_connect.types.s3_uri
    import capo_connect.types.tag_map


class CreatePromptRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.common_name_length127.CommonNameLength127"
    """<p>The name of the prompt.</p>"""
    description: NotRequired["capo_connect.types.prompt_description.PromptDescription"]
    """<p>The description of the prompt.</p>"""
    s3_uri: "capo_connect.types.s3_uri.S3Uri"
    """<p>The URI for the S3 bucket where the prompt is stored. You can provide S3 pre-signed URLs returned by the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_GetPromptFile.html">GetPromptFile</a> API instead of providing S3 URIs.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePromptRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["S3Uri"] = value["s3_uri"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePromptRequest:
    out: CreatePromptRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreatePromptRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("CreatePromptRequest.s3_uri required")
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
