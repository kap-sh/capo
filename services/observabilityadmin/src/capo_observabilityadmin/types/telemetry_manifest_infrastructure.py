"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryManifestInfrastructure``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError, SerializationError
from capo_observabilityadmin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_infrastructure


class TelemetryManifestInfrastructureAzureMember(TypedDict, closed=True):
    Azure: "capo_observabilityadmin.types.azure_infrastructure.AzureInfrastructure"


TelemetryManifestInfrastructure: TypeAlias = (
    TelemetryManifestInfrastructureAzureMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryManifestInfrastructure) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TelemetryManifestInfrastructure: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Azure" in value:
        import capo_observabilityadmin.types.azure_infrastructure

        return {
            "Azure": capo_observabilityadmin.types.azure_infrastructure.serialize_json(
                value["Azure"]
            )
        }
    else:
        raise SerializationError("TelemetryManifestInfrastructure: no variant present")


def deserialize_json(data: dict) -> TelemetryManifestInfrastructure:
    if data.get("Azure") is not None:
        import capo_observabilityadmin.types.azure_infrastructure

        return {
            "Azure": capo_observabilityadmin.types.azure_infrastructure.deserialize_json(
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
            "TelemetryManifestInfrastructure: no recognized variant key"
        )
