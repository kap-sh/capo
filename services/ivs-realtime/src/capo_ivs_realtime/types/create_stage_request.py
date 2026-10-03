"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CreateStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.auto_participant_recording_configuration
    import capo_ivs_realtime.types.participant_token_configurations
    import capo_ivs_realtime.types.stage_name
    import capo_ivs_realtime.types.tags


class CreateStageRequest(TypedDict, closed=True):
    name: NotRequired["capo_ivs_realtime.types.stage_name.StageName"]
    """<p>Optional name that can be specified for the stage being created.</p>"""
    participant_token_configurations: NotRequired[
        "capo_ivs_realtime.types.participant_token_configurations.ParticipantTokenConfigurations"
    ]
    """<p>Array of participant token configuration objects to attach to the new stage.</p>"""
    tags: NotRequired["capo_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there. </p>"""
    auto_participant_recording_configuration: NotRequired[
        "capo_ivs_realtime.types.auto_participant_recording_configuration.AutoParticipantRecordingConfiguration"
    ]
    """<p>Configuration object for individual participant recording, to attach to the new stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStageRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "participant_token_configurations" in value:
        import capo_ivs_realtime.types.participant_token_configurations

        out["participantTokenConfigurations"] = (
            capo_ivs_realtime.types.participant_token_configurations.serialize_json(
                value["participant_token_configurations"]
            )
        )
    if "tags" in value:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.serialize_json(value["tags"])
    if "auto_participant_recording_configuration" in value:
        import capo_ivs_realtime.types.auto_participant_recording_configuration

        out["autoParticipantRecordingConfiguration"] = (
            capo_ivs_realtime.types.auto_participant_recording_configuration.serialize_json(
                value["auto_participant_recording_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateStageRequest:
    out: CreateStageRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("participantTokenConfigurations") is not None:
        import capo_ivs_realtime.types.participant_token_configurations

        out["participant_token_configurations"] = (
            capo_ivs_realtime.types.participant_token_configurations.deserialize_json(
                data["participantTokenConfigurations"]
            )
        )
    if data.get("tags") is not None:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.deserialize_json(data["tags"])
    if data.get("autoParticipantRecordingConfiguration") is not None:
        import capo_ivs_realtime.types.auto_participant_recording_configuration

        out["auto_participant_recording_configuration"] = (
            capo_ivs_realtime.types.auto_participant_recording_configuration.deserialize_json(
                data["autoParticipantRecordingConfiguration"]
            )
        )
    return out
