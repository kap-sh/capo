"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetrySourceConfigurationOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError, SerializationError
from capo_observabilityadmin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_telemetry_source_configuration_output


class TelemetrySourceConfigurationOutputAzureMember(TypedDict, closed=True):
    Azure: "capo_observabilityadmin.types.azure_telemetry_source_configuration_output.AzureTelemetrySourceConfigurationOutput"


TelemetrySourceConfigurationOutput: TypeAlias = (
    TelemetrySourceConfigurationOutputAzureMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TelemetrySourceConfigurationOutput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TelemetrySourceConfigurationOutput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Azure" in value:
        import capo_observabilityadmin.types.azure_telemetry_source_configuration_output

        return {
            "Azure": capo_observabilityadmin.types.azure_telemetry_source_configuration_output.serialize_json(
                value["Azure"]
            )
        }
    else:
        raise SerializationError(
            "TelemetrySourceConfigurationOutput: no variant present"
        )


def deserialize_json(data: dict) -> TelemetrySourceConfigurationOutput:
    if data.get("Azure") is not None:
        import capo_observabilityadmin.types.azure_telemetry_source_configuration_output

        return {
            "Azure": capo_observabilityadmin.types.azure_telemetry_source_configuration_output.deserialize_json(
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
            "TelemetrySourceConfigurationOutput: no recognized variant key"
        )
