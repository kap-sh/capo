"""Generated from Smithy shape ``com.amazonaws.ivschat#DeleteLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.logging_configuration_identifier


class DeleteLoggingConfigurationRequest(TypedDict, closed=True):
    identifier: "capo_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier"
    """<p>Identifier of the logging configuration to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLoggingConfigurationRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> DeleteLoggingConfigurationRequest:
    out: DeleteLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
