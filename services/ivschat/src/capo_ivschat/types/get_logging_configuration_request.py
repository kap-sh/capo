"""Generated from Smithy shape ``com.amazonaws.ivschat#GetLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.logging_configuration_identifier


class GetLoggingConfigurationRequest(TypedDict, closed=True):
    identifier: "capo_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier"
    """<p>Identifier of the logging configuration to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLoggingConfigurationRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> GetLoggingConfigurationRequest:
    out: GetLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
