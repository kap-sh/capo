"""Generated from Smithy shape ``com.amazonaws.m2#DataSetImportConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError
from capo_m2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_m2.types.data_set_import_list
    import capo_m2.types.string2000


class _DataSetImportConfig_s3Location(TypedDict, closed=True):
    s3Location: "capo_m2.types.string2000.String2000"


class _DataSetImportConfig_dataSets(TypedDict, closed=True):
    dataSets: "capo_m2.types.data_set_import_list.DataSetImportList"


DataSetImportConfig: TypeAlias = (
    _DataSetImportConfig_s3Location | _DataSetImportConfig_dataSets | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSetImportConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DataSetImportConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "s3Location" in value:
        return {"s3Location": value["s3Location"]}
    elif "dataSets" in value:
        import capo_m2.types.data_set_import_list

        return {
            "dataSets": capo_m2.types.data_set_import_list.serialize_json(
                value["dataSets"]
            )
        }
    else:
        raise SerializationError("DataSetImportConfig: no variant present")


def deserialize_json(data: dict) -> DataSetImportConfig:
    if data.get("s3Location") is not None:
        return {"s3Location": data["s3Location"]}
    elif data.get("dataSets") is not None:
        import capo_m2.types.data_set_import_list

        return {
            "dataSets": capo_m2.types.data_set_import_list.deserialize_json(
                data["dataSets"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("DataSetImportConfig: no recognized variant key")
