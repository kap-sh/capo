"""Generated from Smithy shape ``com.amazonaws.ivs#BatchStartViewerSessionRevocationViewerSession``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn
    import capo_ivs.types.viewer_id
    import capo_ivs.types.viewer_session_version


class BatchStartViewerSessionRevocationViewerSession(TypedDict, closed=True):
    channel_arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>The ARN of the channel associated with the viewer session to revoke.</p>"""
    viewer_id: "capo_ivs.types.viewer_id.ViewerId"
    """<p>The ID of the viewer associated with the viewer session to revoke. Do not use this field for personally identifying, confidential, or sensitive information.</p>"""
    viewer_session_versions_less_than_or_equal_to: (
        "capo_ivs.types.viewer_session_version.ViewerSessionVersion"
    )
    """<p>An optional filter on which versions of the viewer session to revoke. All versions less than or equal to the specified version will be revoked. Default: 0.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchStartViewerSessionRevocationViewerSession) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    out["viewerId"] = value["viewer_id"]
    out["viewerSessionVersionsLessThanOrEqualTo"] = value.get(
        "viewer_session_versions_less_than_or_equal_to", 0
    )
    return out


def deserialize_json(data: dict) -> BatchStartViewerSessionRevocationViewerSession:
    out: BatchStartViewerSessionRevocationViewerSession = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    else:
        out["channel_arn"] = ""
    if data.get("viewerId") is not None:
        out["viewer_id"] = data["viewerId"]
    else:
        out["viewer_id"] = ""
    if data.get("viewerSessionVersionsLessThanOrEqualTo") is not None:
        out["viewer_session_versions_less_than_or_equal_to"] = data[
            "viewerSessionVersionsLessThanOrEqualTo"
        ]
    else:
        out["viewer_session_versions_less_than_or_equal_to"] = 0
    return out
