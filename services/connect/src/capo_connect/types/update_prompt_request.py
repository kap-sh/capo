"""Generated from Smithy shape ``com.amazonaws.connect#UpdatePromptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.common_name_length127
    import capo_connect.types.instance_id
    import capo_connect.types.prompt_description
    import capo_connect.types.prompt_id
    import capo_connect.types.s3_uri


class UpdatePromptRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    prompt_id: "capo_connect.types.prompt_id.PromptId"
    """<p>A unique identifier for the prompt.</p>"""
    name: NotRequired["capo_connect.types.common_name_length127.CommonNameLength127"]
    """<p>The name of the prompt.</p>"""
    description: NotRequired["capo_connect.types.prompt_description.PromptDescription"]
    """<p>A description of the prompt.</p>"""
    s3_uri: NotRequired["capo_connect.types.s3_uri.S3Uri"]
    """<p>The URI for the S3 bucket where the prompt is stored. You can provide S3 pre-signed URLs returned by the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_GetPromptFile.html">GetPromptFile</a> API instead of providing S3 URIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePromptRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> UpdatePromptRequest:
    out: UpdatePromptRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    return out
