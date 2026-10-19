"""Generated from Smithy shape ``com.amazonaws.ivs#BatchStartViewerSessionRevocationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn
    import capo_ivs.types.error_code
    import capo_ivs.types.error_message
    import capo_ivs.types.viewer_id


class BatchStartViewerSessionRevocationError(TypedDict, closed=True):
    channel_arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>Channel ARN.</p>"""
    viewer_id: "capo_ivs.types.viewer_id.ViewerId"
    """<p>The ID of the viewer session to revoke.</p>"""
    code: NotRequired["capo_ivs.types.error_code.errorCode"]
    """<p>Error code.</p>"""
    message: NotRequired["capo_ivs.types.error_message.errorMessage"]
    """<p>Error message, determined by the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchStartViewerSessionRevocationError) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    out["viewerId"] = value["viewer_id"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchStartViewerSessionRevocationError:
    out: BatchStartViewerSessionRevocationError = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    else:
        out["channel_arn"] = ""
    if data.get("viewerId") is not None:
        out["viewer_id"] = data["viewerId"]
    else:
        out["viewer_id"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
