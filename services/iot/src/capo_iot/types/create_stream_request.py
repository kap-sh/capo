"""Generated from Smithy shape ``com.amazonaws.iot#CreateStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.role_arn
    import capo_iot.types.stream_description
    import capo_iot.types.stream_files
    import capo_iot.types.stream_id
    import capo_iot.types.tag_list


class CreateStreamRequest(TypedDict, closed=True):
    stream_id: "capo_iot.types.stream_id.StreamId"
    """<p>The stream ID.</p>"""
    description: NotRequired["capo_iot.types.stream_description.StreamDescription"]
    """<p>A description of the stream.</p>"""
    files: "capo_iot.types.stream_files.StreamFiles"
    """<p>The files to stream.</p>"""
    role_arn: "capo_iot.types.role_arn.RoleArn"
    """<p>An IAM role that allows the IoT service principal to access your S3 files.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage streams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import capo_iot.types.stream_files

    out["files"] = capo_iot.types.stream_files.serialize_json(value["files"])
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateStreamRequest:
    out: CreateStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("files") is not None:
        import capo_iot.types.stream_files

        out["files"] = capo_iot.types.stream_files.deserialize_json(data["files"])
    else:
        out["files"] = []
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    return out
