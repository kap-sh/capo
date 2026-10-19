"""Generated from Smithy shape ``com.amazonaws.m2#DataSetExportConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError
from capo_m2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_m2.types.data_set_export_list


class _DataSetExportConfig_s3Location(TypedDict, closed=True):
    s3Location: "str"


class _DataSetExportConfig_dataSets(TypedDict, closed=True):
    dataSets: "capo_m2.types.data_set_export_list.DataSetExportList"


DataSetExportConfig: TypeAlias = (
    _DataSetExportConfig_s3Location | _DataSetExportConfig_dataSets | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSetExportConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DataSetExportConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "s3Location" in value:
        return {"s3Location": value["s3Location"]}
    elif "dataSets" in value:
        import capo_m2.types.data_set_export_list

        return {
            "dataSets": capo_m2.types.data_set_export_list.serialize_json(
                value["dataSets"]
            )
        }
    else:
        raise SerializationError("DataSetExportConfig: no variant present")


def deserialize_json(data: dict) -> DataSetExportConfig:
    if data.get("s3Location") is not None:
        return {"s3Location": data["s3Location"]}
    elif data.get("dataSets") is not None:
        import capo_m2.types.data_set_export_list

        return {
            "dataSets": capo_m2.types.data_set_export_list.deserialize_json(
                data["dataSets"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("DataSetExportConfig: no recognized variant key")
