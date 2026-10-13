"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ChimeSdkMeetingConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.artifacts_configuration
    import capo_chime_sdk_media_pipelines.types.source_configuration


class ChimeSdkMeetingConfiguration(TypedDict, closed=True):
    source_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.source_configuration.SourceConfiguration"
    ]
    """<p>The source configuration for a specified media pipeline.</p>"""
    artifacts_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.artifacts_configuration.ArtifactsConfiguration"
    ]
    """<p>The configuration for the artifacts in an Amazon Chime SDK meeting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChimeSdkMeetingConfiguration) -> dict:
    out: dict = {}
    if "source_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.source_configuration

        out["SourceConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "artifacts_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.artifacts_configuration

        out["ArtifactsConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.artifacts_configuration.serialize_json(
                value["artifacts_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChimeSdkMeetingConfiguration:
    out: ChimeSdkMeetingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SourceConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.source_configuration

        out["source_configuration"] = (
            capo_chime_sdk_media_pipelines.types.source_configuration.deserialize_json(
                data["SourceConfiguration"]
            )
        )
    if data.get("ArtifactsConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.artifacts_configuration

        out["artifacts_configuration"] = (
            capo_chime_sdk_media_pipelines.types.artifacts_configuration.deserialize_json(
                data["ArtifactsConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ChimeSdkMeetingConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.source_configuration

        out["source_configuration"] = (
            capo_chime_sdk_media_pipelines.types.source_configuration.redact_sensitive(
                value["source_configuration"]
            )
        )
    return out
