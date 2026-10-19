"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#UpdateMediaInsightsPipelineStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_pipeline_status_update
    import capo_chime_sdk_media_pipelines.types.non_empty_string


class UpdateMediaInsightsPipelineStatusRequest(TypedDict, closed=True):
    identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    """<p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>"""
    update_status: "capo_chime_sdk_media_pipelines.types.media_pipeline_status_update.MediaPipelineStatusUpdate"
    """<p>The requested status of the media insights pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMediaInsightsPipelineStatusRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.media_pipeline_status_update

    out["UpdateStatus"] = (
        capo_chime_sdk_media_pipelines.types.media_pipeline_status_update.serialize_json(
            value["update_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateMediaInsightsPipelineStatusRequest:
    out: UpdateMediaInsightsPipelineStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("UpdateStatus") is not None:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_status_update

        out["update_status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_status_update.deserialize_json(
                data["UpdateStatus"]
            )
        )
    else:
        import typing

        out["update_status"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.media_pipeline_status_update.MediaPipelineStatusUpdate",
            "",
        )
    return out
