"""Generated from Smithy shape ``com.amazonaws.connect#DeleteAttachedFileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.file_id
    import capo_connect.types.instance_id


class DeleteAttachedFileRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier of the Connect instance.</p>"""
    file_id: "capo_connect.types.file_id.FileId"
    """<p>The unique identifier of the attached file resource.</p>"""
    associated_resource_arn: "capo_connect.types.arn.ARN"
    """<p>The resource to which the attached file is (being) uploaded to. The supported resources are <a href="https://docs.aws.amazon.com/connect/latest/adminguide/cases.html">Cases</a>, <a href="https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html">Email</a>, and <a href="https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html">Task</a>.</p> <note> <p>This value must be a valid ARN.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAttachedFileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAttachedFileRequest:
    out: DeleteAttachedFileRequest = {}  # type: ignore[typeddict-item]
    return out
