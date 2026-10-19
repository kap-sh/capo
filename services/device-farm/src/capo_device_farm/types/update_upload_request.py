"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.boolean
    import capo_device_farm.types.content_type
    import capo_device_farm.types.name


class UpdateUploadRequest(TypedDict, closed=True):
    arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the uploaded test spec.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The upload's test spec file name. The name must not contain any forward slashes (/). The test spec file name must end with the <code>.yaml</code> or <code>.yml</code> file extension.</p>"""
    content_type: NotRequired["capo_device_farm.types.content_type.ContentType"]
    """<p>The upload's content type (for example, <code>application/x-yaml</code>).</p>"""
    edit_content: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>Set to true if the YAML file has changed and must be updated. Otherwise, set to false.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUploadRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "edit_content" in value:
        out["editContent"] = value["edit_content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUploadRequest:
    out: UpdateUploadRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    if data.get("editContent") is not None:
        out["edit_content"] = data["editContent"]
    return out
