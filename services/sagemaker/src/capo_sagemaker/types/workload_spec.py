"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkloadSpec``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.string


class _WorkloadSpec_Inline(TypedDict, closed=True):
    Inline: "capo_sagemaker.types.string.String"


WorkloadSpec: TypeAlias = _WorkloadSpec_Inline | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkloadSpec) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"WorkloadSpec: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Inline" in value:
        return {"Inline": value["Inline"]}
    else:
        raise SerializationError("WorkloadSpec: no variant present")


def deserialize_aws_json_1_1(data: dict) -> WorkloadSpec:
    if data.get("Inline") is not None:
        return {"Inline": data["Inline"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("WorkloadSpec: no recognized variant key")
