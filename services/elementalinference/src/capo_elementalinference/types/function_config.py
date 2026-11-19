"""Generated from Smithy shape ``com.amazonaws.elementalinference#FunctionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.clipping_settings
    import capo_elementalinference.types.contextual_metadata_settings
    import capo_elementalinference.types.frame_settings
    import capo_elementalinference.types.function_arn
    import capo_elementalinference.types.subtitling_settings
    import capo_elementalinference.types.trigger


class FunctionConfig(TypedDict, closed=True):
    function_arn: "capo_elementalinference.types.function_arn.FunctionArn"
    """<p>The ARN of the function to run. The function must exist in the same account and the same Region as the feed. </p>"""
    trigger: "capo_elementalinference.types.trigger.Trigger"
    """<p>Determines when the function runs.</p>"""
    frame_settings: NotRequired[
        "capo_elementalinference.types.frame_settings.FrameSettings"
    ]
    """<p>The frames to send on each run: how many, which ones, and at what size. Applies to a function that references media.frames. If you omit this structure, Elemental Inference sends the first frame of the window, at its source size. </p>"""
    subtitling_settings: NotRequired[
        "capo_elementalinference.types.subtitling_settings.SubtitlingSettings"
    ]
    """<p>The smart subtitles output on this feed to read the transcript from. Required for a function that references media.transcript. </p>"""
    contextual_metadata_settings: NotRequired[
        "capo_elementalinference.types.contextual_metadata_settings.ContextualMetadataSettings"
    ]
    """<p>The contextual metadata output on this feed to read scenes and classifications from. Required for a perScene trigger, and for a function that references media.contextual on a perShot trigger. </p>"""
    clipping_settings: NotRequired[
        "capo_elementalinference.types.clipping_settings.ClippingSettings"
    ]
    """<p>The event clipping output on this feed to read clips from. Required for a perClip trigger, and for a function that references media.clip. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionConfig) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    import capo_elementalinference.types.trigger

    out["trigger"] = capo_elementalinference.types.trigger.serialize_json(
        value["trigger"]
    )
    if "frame_settings" in value:
        import capo_elementalinference.types.frame_settings

        out["frameSettings"] = (
            capo_elementalinference.types.frame_settings.serialize_json(
                value["frame_settings"]
            )
        )
    if "subtitling_settings" in value:
        import capo_elementalinference.types.subtitling_settings

        out["subtitlingSettings"] = (
            capo_elementalinference.types.subtitling_settings.serialize_json(
                value["subtitling_settings"]
            )
        )
    if "contextual_metadata_settings" in value:
        import capo_elementalinference.types.contextual_metadata_settings

        out["contextualMetadataSettings"] = (
            capo_elementalinference.types.contextual_metadata_settings.serialize_json(
                value["contextual_metadata_settings"]
            )
        )
    if "clipping_settings" in value:
        import capo_elementalinference.types.clipping_settings

        out["clippingSettings"] = (
            capo_elementalinference.types.clipping_settings.serialize_json(
                value["clipping_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunctionConfig:
    out: FunctionConfig = {}  # type: ignore[typeddict-item]
    if data.get("functionArn") is not None:
        out["function_arn"] = data["functionArn"]
    else:
        out["function_arn"] = ""
    if data.get("trigger") is not None:
        import capo_elementalinference.types.trigger

        out["trigger"] = capo_elementalinference.types.trigger.deserialize_json(
            data["trigger"]
        )
    else:
        out["trigger"] = {"$unknown": {"name": ""}}
    if data.get("frameSettings") is not None:
        import capo_elementalinference.types.frame_settings

        out["frame_settings"] = (
            capo_elementalinference.types.frame_settings.deserialize_json(
                data["frameSettings"]
            )
        )
    if data.get("subtitlingSettings") is not None:
        import capo_elementalinference.types.subtitling_settings

        out["subtitling_settings"] = (
            capo_elementalinference.types.subtitling_settings.deserialize_json(
                data["subtitlingSettings"]
            )
        )
    if data.get("contextualMetadataSettings") is not None:
        import capo_elementalinference.types.contextual_metadata_settings

        out["contextual_metadata_settings"] = (
            capo_elementalinference.types.contextual_metadata_settings.deserialize_json(
                data["contextualMetadataSettings"]
            )
        )
    if data.get("clippingSettings") is not None:
        import capo_elementalinference.types.clipping_settings

        out["clipping_settings"] = (
            capo_elementalinference.types.clipping_settings.deserialize_json(
                data["clippingSettings"]
            )
        )
    return out
