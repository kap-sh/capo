"""Generated from Smithy shape ``com.amazonaws.connect#BatchGetAttachedFileMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.file_id_list
    import capo_connect.types.instance_id


class BatchGetAttachedFileMetadataRequest(TypedDict, closed=True):
    file_ids: "capo_connect.types.file_id_list.FileIdList"
    """<p>The unique identifiers of the attached file resource.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier of the Connect instance.</p>"""
    associated_resource_arn: "capo_connect.types.arn.ARN"
    """<p>The resource to which the attached file is (being) uploaded to. The supported resources are <a href="https://docs.aws.amazon.com/connect/latest/adminguide/cases.html">Cases</a>, <a href="https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html">Email</a>, and <a href="https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html">Task</a>.</p> <note> <p>This value must be a valid ARN.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAttachedFileMetadataRequest) -> dict:
    out: dict = {}
    import capo_connect.types.file_id_list

    out["FileIds"] = capo_connect.types.file_id_list.serialize_json(value["file_ids"])
    return out


def deserialize_json(data: dict) -> BatchGetAttachedFileMetadataRequest:
    out: BatchGetAttachedFileMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("FileIds") is not None:
        import capo_connect.types.file_id_list

        out["file_ids"] = capo_connect.types.file_id_list.deserialize_json(
            data["FileIds"]
        )
    else:
        raise DeserializationError(
            "BatchGetAttachedFileMetadataRequest.file_ids required"
        )
    return out
