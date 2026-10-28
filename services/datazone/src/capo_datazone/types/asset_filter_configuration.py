"""Generated from Smithy shape ``com.amazonaws.datazone#AssetFilterConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.column_filter_configuration
    import capo_datazone.types.row_filter_configuration


class AssetFilterConfigurationColumnConfigurationMember(TypedDict, closed=True):
    columnConfiguration: (
        "capo_datazone.types.column_filter_configuration.ColumnFilterConfiguration"
    )


class AssetFilterConfigurationRowConfigurationMember(TypedDict, closed=True):
    rowConfiguration: (
        "capo_datazone.types.row_filter_configuration.RowFilterConfiguration"
    )


AssetFilterConfiguration: TypeAlias = (
    AssetFilterConfigurationColumnConfigurationMember
    | AssetFilterConfigurationRowConfigurationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssetFilterConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssetFilterConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "columnConfiguration" in value:
        import capo_datazone.types.column_filter_configuration

        return {
            "columnConfiguration": capo_datazone.types.column_filter_configuration.serialize_json(
                value["columnConfiguration"]
            )
        }
    elif "rowConfiguration" in value:
        import capo_datazone.types.row_filter_configuration

        return {
            "rowConfiguration": capo_datazone.types.row_filter_configuration.serialize_json(
                value["rowConfiguration"]
            )
        }
    else:
        raise SerializationError("AssetFilterConfiguration: no variant present")


def deserialize_json(data: dict) -> AssetFilterConfiguration:
    if data.get("columnConfiguration") is not None:
        import capo_datazone.types.column_filter_configuration

        return {
            "columnConfiguration": capo_datazone.types.column_filter_configuration.deserialize_json(
                data["columnConfiguration"]
            )
        }
    elif data.get("rowConfiguration") is not None:
        import capo_datazone.types.row_filter_configuration

        return {
            "rowConfiguration": capo_datazone.types.row_filter_configuration.deserialize_json(
                data["rowConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AssetFilterConfiguration: no recognized variant key"
        )
