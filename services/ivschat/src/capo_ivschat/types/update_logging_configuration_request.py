"""Generated from Smithy shape ``com.amazonaws.ivschat#UpdateLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.destination_configuration
    import capo_ivschat.types.logging_configuration_identifier
    import capo_ivschat.types.logging_configuration_name


class UpdateLoggingConfigurationRequest(TypedDict, closed=True):
    identifier: "capo_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier"
    """<p>Identifier of the logging configuration to be updated.</p>"""
    name: NotRequired[
        "capo_ivschat.types.logging_configuration_name.LoggingConfigurationName"
    ]
    """<p>Logging-configuration name. The value does not need to be unique.</p>"""
    destination_configuration: NotRequired[
        "capo_ivschat.types.destination_configuration.DestinationConfiguration"
    ]
    """<p>A complex type that contains a destination configuration for where chat content will be logged. There can be only one type of destination (<code>cloudWatchLogs</code>, <code>firehose</code>, or <code>s3</code>) in a <code>destinationConfiguration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLoggingConfigurationRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "name" in value:
        out["name"] = value["name"]
    if "destination_configuration" in value:
        import capo_ivschat.types.destination_configuration

        out["destinationConfiguration"] = (
            capo_ivschat.types.destination_configuration.serialize_json(
                value["destination_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateLoggingConfigurationRequest:
    out: UpdateLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("destinationConfiguration") is not None:
        import capo_ivschat.types.destination_configuration

        out["destination_configuration"] = (
            capo_ivschat.types.destination_configuration.deserialize_json(
                data["destinationConfiguration"]
            )
        )
    return out
