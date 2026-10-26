"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizerVpcConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError, SerializationError
from capo_glue.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_glue.types.glue_connection_name_string


class _TableOptimizerVpcConfiguration_glueConnectionName(TypedDict, closed=True):
    glueConnectionName: (
        "capo_glue.types.glue_connection_name_string.glueConnectionNameString"
    )


TableOptimizerVpcConfiguration: TypeAlias = (
    _TableOptimizerVpcConfiguration_glueConnectionName | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableOptimizerVpcConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TableOptimizerVpcConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "glueConnectionName" in value:
        return {"glueConnectionName": value["glueConnectionName"]}
    else:
        raise SerializationError("TableOptimizerVpcConfiguration: no variant present")


def deserialize_aws_json_1_1(data: dict) -> TableOptimizerVpcConfiguration:
    if data.get("glueConnectionName") is not None:
        return {"glueConnectionName": data["glueConnectionName"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "TableOptimizerVpcConfiguration: no recognized variant key"
        )
