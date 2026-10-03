"""Generated from Smithy shape ``com.amazonaws.ivs#RecordingConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.destination_configuration
    import capo_ivs.types.recording_configuration_arn
    import capo_ivs.types.recording_configuration_name
    import capo_ivs.types.recording_configuration_state
    import capo_ivs.types.tags


class RecordingConfigurationSummary(TypedDict, closed=True):
    arn: "capo_ivs.types.recording_configuration_arn.RecordingConfigurationArn"
    """<p>Recording-configuration ARN.</p>"""
    name: NotRequired[
        "capo_ivs.types.recording_configuration_name.RecordingConfigurationName"
    ]
    """<p>Recording-configuration name. The value does not need to be unique.</p>"""
    destination_configuration: (
        "capo_ivs.types.destination_configuration.DestinationConfiguration"
    )
    """<p>A complex type that contains information about where recorded video will be stored.</p>"""
    state: "capo_ivs.types.recording_configuration_state.RecordingConfigurationState"
    """<p>Indicates the current state of the recording configuration. When the state is <code>ACTIVE</code>, the configuration is ready for recording a channel stream.</p>"""
    tags: NotRequired["capo_ivs.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordingConfigurationSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_ivs.types.destination_configuration

    out["destinationConfiguration"] = (
        capo_ivs.types.destination_configuration.serialize_json(
            value["destination_configuration"]
        )
    )
    out["state"] = value["state"]
    if "tags" in value:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RecordingConfigurationSummary:
    out: RecordingConfigurationSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RecordingConfigurationSummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("destinationConfiguration") is not None:
        import capo_ivs.types.destination_configuration

        out["destination_configuration"] = (
            capo_ivs.types.destination_configuration.deserialize_json(
                data["destinationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RecordingConfigurationSummary.destination_configuration required"
        )
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        raise DeserializationError("RecordingConfigurationSummary.state required")
    if data.get("tags") is not None:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.deserialize_json(data["tags"])
    return out
