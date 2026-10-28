"""Generated from Smithy shape ``com.amazonaws.amp#ExporterConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError
from capo_amp.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_amp.types.open_search_exporter_configuration


class ExporterConfigurationOpenSearchConfigurationMember(TypedDict, closed=True):
    openSearchConfiguration: "capo_amp.types.open_search_exporter_configuration.OpenSearchExporterConfiguration"


ExporterConfiguration: TypeAlias = (
    ExporterConfigurationOpenSearchConfigurationMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ExporterConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ExporterConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "openSearchConfiguration" in value:
        import capo_amp.types.open_search_exporter_configuration

        return {
            "openSearchConfiguration": capo_amp.types.open_search_exporter_configuration.serialize_json(
                value["openSearchConfiguration"]
            )
        }
    else:
        raise SerializationError("ExporterConfiguration: no variant present")


def deserialize_json(data: dict) -> ExporterConfiguration:
    if data.get("openSearchConfiguration") is not None:
        import capo_amp.types.open_search_exporter_configuration

        return {
            "openSearchConfiguration": capo_amp.types.open_search_exporter_configuration.deserialize_json(
                data["openSearchConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ExporterConfiguration: no recognized variant key")
