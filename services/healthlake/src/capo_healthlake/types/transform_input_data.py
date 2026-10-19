"""Generated from Smithy shape ``com.amazon.awshealthlakedatatransformationfrontendservice#TransformInputData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, SerializationError
from capo_healthlake.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_healthlake.types.file_input_map


class _TransformInputData_CcdaInput(TypedDict, closed=True):
    CcdaInput: "str"


class _TransformInputData_CsvInput(TypedDict, closed=True):
    CsvInput: "capo_healthlake.types.file_input_map.FileInputMap"


TransformInputData: TypeAlias = (
    _TransformInputData_CcdaInput | _TransformInputData_CsvInput | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformInputData) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"TransformInputData: cannot serialize unknown variant {value.name!r}"
        )
    elif "CcdaInput" in value:
        return {"CcdaInput": value["CcdaInput"]}
    elif "CsvInput" in value:
        import capo_healthlake.types.file_input_map

        return {
            "CsvInput": capo_healthlake.types.file_input_map.serialize_aws_json_1_0(
                value["CsvInput"]
            )
        }
    else:
        raise SerializationError("TransformInputData: no variant present")


def deserialize_aws_json_1_0(data: dict) -> TransformInputData:
    if data.get("CcdaInput") is not None:
        return {"CcdaInput": data["CcdaInput"]}
    elif data.get("CsvInput") is not None:
        import capo_healthlake.types.file_input_map

        return {
            "CsvInput": capo_healthlake.types.file_input_map.deserialize_aws_json_1_0(
                data["CsvInput"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("TransformInputData: no recognized variant key")
