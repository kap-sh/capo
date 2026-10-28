"""Generated from Smithy shape ``com.amazonaws.dsql#TargetDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_dsql.errors import DeserializationError, SerializationError
from capo_dsql.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_dsql.types.kinesis_target_definition


class TargetDefinitionKinesisMember(TypedDict, closed=True):
    kinesis: "capo_dsql.types.kinesis_target_definition.KinesisTargetDefinition"


TargetDefinition: TypeAlias = TargetDefinitionKinesisMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: TargetDefinition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TargetDefinition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "kinesis" in value:
        import capo_dsql.types.kinesis_target_definition

        return {
            "kinesis": capo_dsql.types.kinesis_target_definition.serialize_json(
                value["kinesis"]
            )
        }
    else:
        raise SerializationError("TargetDefinition: no variant present")


def deserialize_json(data: dict) -> TargetDefinition:
    if data.get("kinesis") is not None:
        import capo_dsql.types.kinesis_target_definition

        return {
            "kinesis": capo_dsql.types.kinesis_target_definition.deserialize_json(
                data["kinesis"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TargetDefinition: no recognized variant key")
