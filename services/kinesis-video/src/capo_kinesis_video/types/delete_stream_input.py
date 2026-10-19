"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DeleteStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.version


class DeleteStreamInput(TypedDict, closed=True):
    stream_arn: "capo_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the stream that you want to delete. </p>"""
    current_version: NotRequired["capo_kinesis_video.types.version.Version"]
    """<p>Optional: The version of the stream that you want to delete. </p> <p>Specify the version as a safeguard to ensure that your are deleting the correct stream. To get the stream version, use the <code>DescribeStream</code> API.</p> <p>If not specified, only the <code>CreationTime</code> is checked before deleting the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStreamInput) -> dict:
    out: dict = {}
    out["StreamARN"] = value["stream_arn"]
    if "current_version" in value:
        out["CurrentVersion"] = value["current_version"]
    return out


def deserialize_json(data: dict) -> DeleteStreamInput:
    out: DeleteStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        out["stream_arn"] = ""
    if data.get("CurrentVersion") is not None:
        out["current_version"] = data["CurrentVersion"]
    return out
