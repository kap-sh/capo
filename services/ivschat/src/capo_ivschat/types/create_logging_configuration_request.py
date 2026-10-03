"""Generated from Smithy shape ``com.amazonaws.ivschat#CreateLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivschat.types.destination_configuration
    import capo_ivschat.types.logging_configuration_name
    import capo_ivschat.types.tags


class CreateLoggingConfigurationRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_ivschat.types.logging_configuration_name.LoggingConfigurationName"
    ]
    """<p>Logging-configuration name. The value does not need to be unique.</p>"""
    destination_configuration: (
        "capo_ivschat.types.destination_configuration.DestinationConfiguration"
    )
    """<p>A complex type that contains a destination configuration for where chat content will be logged. There can be only one type of destination (<code>cloudWatchLogs</code>, <code>firehose</code>, or <code>s3</code>) in a <code>destinationConfiguration</code>.</p>"""
    tags: NotRequired["capo_ivschat.types.tags.Tags"]
    """<p>Tags to attach to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS Chat has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLoggingConfigurationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    import capo_ivschat.types.destination_configuration

    out["destinationConfiguration"] = (
        capo_ivschat.types.destination_configuration.serialize_json(
            value["destination_configuration"]
        )
    )
    if "tags" in value:
        import capo_ivschat.types.tags

        out["tags"] = capo_ivschat.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateLoggingConfigurationRequest:
    out: CreateLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("destinationConfiguration") is not None:
        import capo_ivschat.types.destination_configuration

        out["destination_configuration"] = (
            capo_ivschat.types.destination_configuration.deserialize_json(
                data["destinationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLoggingConfigurationRequest.destination_configuration required"
        )
    if data.get("tags") is not None:
        import capo_ivschat.types.tags

        out["tags"] = capo_ivschat.types.tags.deserialize_json(data["tags"])
    return out
