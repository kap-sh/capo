"""Generated from Smithy shape ``com.amazonaws.ssmincidents#AutomationExecution``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn


class AutomationExecutionSsmExecutionArnMember(TypedDict, closed=True):
    ssmExecutionArn: "capo_ssm_incidents.types.arn.Arn"


AutomationExecution: TypeAlias = (
    AutomationExecutionSsmExecutionArnMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomationExecution) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AutomationExecution: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ssmExecutionArn" in value:
        return {"ssmExecutionArn": value["ssmExecutionArn"]}
    else:
        raise SerializationError("AutomationExecution: no variant present")


def deserialize_json(data: dict) -> AutomationExecution:
    if data.get("ssmExecutionArn") is not None:
        return {"ssmExecutionArn": data["ssmExecutionArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AutomationExecution: no recognized variant key")
