"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.media_pipeline_source_type


class MediaStreamSource(TypedDict, closed=True):
    source_type: "capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.MediaPipelineSourceType"
    """<p>The type of media stream source.</p>"""
    source_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The ARN of the meeting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamSource) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.media_pipeline_source_type

    out["SourceType"] = (
        capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.serialize_json(
            value["source_type"]
        )
    )
    out["SourceArn"] = value["source_arn"]
    return out


def deserialize_json(data: dict) -> MediaStreamSource:
    out: MediaStreamSource = {}  # type: ignore[typeddict-item]
    if data.get("SourceType") is not None:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_source_type

        out["source_type"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.deserialize_json(
                data["SourceType"]
            )
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.MediaPipelineSourceType",
            "",
        )
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    else:
        out["source_arn"] = ""
    return out


def redact_sensitive(value: MediaStreamSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_arn" in value:
        out["source_arn"] = "*** Sensitive Data Redacted ***"
    return out
