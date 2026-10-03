"""Generated from Smithy shape ``com.amazonaws.connect#GetAttachedFileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.file_id
    import capo_connect.types.instance_id
    import capo_connect.types.url_expiry_in_seconds


class GetAttachedFileRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier of the Connect Customer instance.</p>"""
    file_id: "capo_connect.types.file_id.FileId"
    """<p>The unique identifier of the attached file resource.</p>"""
    url_expiry_in_seconds: NotRequired[
        "capo_connect.types.url_expiry_in_seconds.URLExpiryInSeconds"
    ]
    """<p>Optional override for the expiry of the pre-signed S3 URL in seconds. The default value is 300.</p>"""
    associated_resource_arn: "capo_connect.types.arn.ARN"
    """<p>The resource to which the attached file is (being) uploaded to. The supported resources are <a href="https://docs.aws.amazon.com/connect/latest/adminguide/cases.html">Cases</a>, <a href="https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html">Email</a>, and <a href="https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html">Task</a>.</p> <note> <p>This value must be a valid ARN.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAttachedFileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAttachedFileRequest:
    out: GetAttachedFileRequest = {}  # type: ignore[typeddict-item]
    return out
