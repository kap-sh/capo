"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GridConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.attribute_key
    import capo_ivs_realtime.types.grid_gap
    import capo_ivs_realtime.types.omit_stopped_video
    import capo_ivs_realtime.types.video_aspect_ratio
    import capo_ivs_realtime.types.video_fill_mode


class GridConfiguration(TypedDict, closed=True):
    featured_participant_attribute: NotRequired[
        "capo_ivs_realtime.types.attribute_key.AttributeKey"
    ]
    """<p>This attribute name identifies the featured slot. A participant with this attribute set to <code>"true"</code> (as a string value) in <a>ParticipantTokenConfiguration</a> is placed in the featured slot. Default: <code>""</code> (no featured participant).</p>"""
    omit_stopped_video: "capo_ivs_realtime.types.omit_stopped_video.OmitStoppedVideo"
    """<p>Determines whether to omit participants with stopped video in the composition. Default: <code>false</code>.</p>"""
    video_aspect_ratio: NotRequired[
        "capo_ivs_realtime.types.video_aspect_ratio.VideoAspectRatio"
    ]
    """<p>Sets the non-featured participant display mode, to control the aspect ratio of video tiles. <code>VIDEO</code> is 16:9, <code>SQUARE</code> is 1:1, and <code>PORTRAIT</code> is 3:4. Default: <code>VIDEO</code>.</p>"""
    video_fill_mode: NotRequired[
        "capo_ivs_realtime.types.video_fill_mode.VideoFillMode"
    ]
    """<p>Defines how video content fits within the participant tile: <code>FILL</code> (stretched), <code>COVER</code> (cropped), or <code>CONTAIN</code> (letterboxed). When not set, <code>videoFillMode</code> defaults to <code>COVER</code> fill mode for participants in the grid and to <code>CONTAIN</code> fill mode for featured participants.</p>"""
    grid_gap: "capo_ivs_realtime.types.grid_gap.GridGap"
    """<p>Specifies the spacing between participant tiles in pixels. Default: <code>2</code>.</p>"""
    participant_order_attribute: NotRequired[
        "capo_ivs_realtime.types.attribute_key.AttributeKey"
    ]
    """<p>Attribute name in <a>ParticipantTokenConfiguration</a> identifying the participant ordering key. Participants with <code>participantOrderAttribute</code> set to <code>""</code> or not specified are ordered based on their arrival time into the stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GridConfiguration) -> dict:
    out: dict = {}
    if "featured_participant_attribute" in value:
        out["featuredParticipantAttribute"] = value["featured_participant_attribute"]
    out["omitStoppedVideo"] = value.get("omit_stopped_video", False)
    if "video_aspect_ratio" in value:
        import capo_ivs_realtime.types.video_aspect_ratio

        out["videoAspectRatio"] = (
            capo_ivs_realtime.types.video_aspect_ratio.serialize_json(
                value["video_aspect_ratio"]
            )
        )
    if "video_fill_mode" in value:
        import capo_ivs_realtime.types.video_fill_mode

        out["videoFillMode"] = capo_ivs_realtime.types.video_fill_mode.serialize_json(
            value["video_fill_mode"]
        )
    out["gridGap"] = value.get("grid_gap", 0)
    if "participant_order_attribute" in value:
        out["participantOrderAttribute"] = value["participant_order_attribute"]
    return out


def deserialize_json(data: dict) -> GridConfiguration:
    out: GridConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("featuredParticipantAttribute") is not None:
        out["featured_participant_attribute"] = data["featuredParticipantAttribute"]
    if data.get("omitStoppedVideo") is not None:
        out["omit_stopped_video"] = data["omitStoppedVideo"]
    else:
        out["omit_stopped_video"] = False
    if data.get("videoAspectRatio") is not None:
        import capo_ivs_realtime.types.video_aspect_ratio

        out["video_aspect_ratio"] = (
            capo_ivs_realtime.types.video_aspect_ratio.deserialize_json(
                data["videoAspectRatio"]
            )
        )
    if data.get("videoFillMode") is not None:
        import capo_ivs_realtime.types.video_fill_mode

        out["video_fill_mode"] = (
            capo_ivs_realtime.types.video_fill_mode.deserialize_json(
                data["videoFillMode"]
            )
        )
    if data.get("gridGap") is not None:
        out["grid_gap"] = data["gridGap"]
    else:
        out["grid_gap"] = 0
    if data.get("participantOrderAttribute") is not None:
        out["participant_order_attribute"] = data["participantOrderAttribute"]
    return out
