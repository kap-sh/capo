"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetrySourceConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError, SerializationError
from capo_observabilityadmin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_telemetry_source_configuration_input


class TelemetrySourceConfigurationInputAzureMember(TypedDict, closed=True):
    Azure: "capo_observabilityadmin.types.azure_telemetry_source_configuration_input.AzureTelemetrySourceConfigurationInput"


TelemetrySourceConfigurationInput: TypeAlias = (
    TelemetrySourceConfigurationInputAzureMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TelemetrySourceConfigurationInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TelemetrySourceConfigurationInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Azure" in value:
        import capo_observabilityadmin.types.azure_telemetry_source_configuration_input

        return {
            "Azure": capo_observabilityadmin.types.azure_telemetry_source_configuration_input.serialize_json(
                value["Azure"]
            )
        }
    else:
        raise SerializationError(
            "TelemetrySourceConfigurationInput: no variant present"
        )


def deserialize_json(data: dict) -> TelemetrySourceConfigurationInput:
    if data.get("Azure") is not None:
        import capo_observabilityadmin.types.azure_telemetry_source_configuration_input

        return {
            "Azure": capo_observabilityadmin.types.azure_telemetry_source_configuration_input.deserialize_json(
                data["Azure"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "TelemetrySourceConfigurationInput: no recognized variant key"
        )
