"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#FragmentSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.fragment_selector_type
    import capo_chime_sdk_media_pipelines.types.timestamp_range


class FragmentSelector(TypedDict, closed=True):
    fragment_selector_type: "capo_chime_sdk_media_pipelines.types.fragment_selector_type.FragmentSelectorType"
    """<p>The origin of the timestamps to use, <code>Server</code> or <code>Producer</code>. For more information, see <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_StartSelector.html">StartSelectorType</a> in the <i>Amazon Kinesis Video Streams Developer Guide</i>.</p>"""
    timestamp_range: (
        "capo_chime_sdk_media_pipelines.types.timestamp_range.TimestampRange"
    )
    """<p>The range of timestamps to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FragmentSelector) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.fragment_selector_type

    out["FragmentSelectorType"] = (
        capo_chime_sdk_media_pipelines.types.fragment_selector_type.serialize_json(
            value["fragment_selector_type"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.timestamp_range

    out["TimestampRange"] = (
        capo_chime_sdk_media_pipelines.types.timestamp_range.serialize_json(
            value["timestamp_range"]
        )
    )
    return out


def deserialize_json(data: dict) -> FragmentSelector:
    out: FragmentSelector = {}  # type: ignore[typeddict-item]
    if data.get("FragmentSelectorType") is not None:
        import capo_chime_sdk_media_pipelines.types.fragment_selector_type

        out["fragment_selector_type"] = (
            capo_chime_sdk_media_pipelines.types.fragment_selector_type.deserialize_json(
                data["FragmentSelectorType"]
            )
        )
    else:
        raise DeserializationError("FragmentSelector.fragment_selector_type required")
    if data.get("TimestampRange") is not None:
        import capo_chime_sdk_media_pipelines.types.timestamp_range

        out["timestamp_range"] = (
            capo_chime_sdk_media_pipelines.types.timestamp_range.deserialize_json(
                data["TimestampRange"]
            )
        )
    else:
        raise DeserializationError("FragmentSelector.timestamp_range required")
    return out
