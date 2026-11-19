"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryManifestSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError, SerializationError
from capo_observabilityadmin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_sources


class TelemetryManifestSourceAzureMember(TypedDict, closed=True):
    Azure: "capo_observabilityadmin.types.azure_sources.AzureSources"


TelemetryManifestSource: TypeAlias = (
    TelemetryManifestSourceAzureMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryManifestSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TelemetryManifestSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Azure" in value:
        import capo_observabilityadmin.types.azure_sources

        return {
            "Azure": capo_observabilityadmin.types.azure_sources.serialize_json(
                value["Azure"]
            )
        }
    else:
        raise SerializationError("TelemetryManifestSource: no variant present")


def deserialize_json(data: dict) -> TelemetryManifestSource:
    if data.get("Azure") is not None:
        import capo_observabilityadmin.types.azure_sources

        return {
            "Azure": capo_observabilityadmin.types.azure_sources.deserialize_json(
                data["Azure"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TelemetryManifestSource: no recognized variant key")
