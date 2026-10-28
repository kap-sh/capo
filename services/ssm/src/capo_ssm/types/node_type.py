"""Generated from Smithy shape ``com.amazonaws.ssm#NodeType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError, SerializationError
from capo_ssm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm.types.instance_info


class NodeTypeInstanceMember(TypedDict, closed=True):
    Instance: "capo_ssm.types.instance_info.InstanceInfo"


NodeType: TypeAlias = NodeTypeInstanceMember | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeType) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"NodeType: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Instance" in value:
        import capo_ssm.types.instance_info

        return {
            "Instance": capo_ssm.types.instance_info.serialize_aws_json_1_1(
                value["Instance"]
            )
        }
    else:
        raise SerializationError("NodeType: no variant present")


def deserialize_aws_json_1_1(data: dict) -> NodeType:
    if data.get("Instance") is not None:
        import capo_ssm.types.instance_info

        return {
            "Instance": capo_ssm.types.instance_info.deserialize_aws_json_1_1(
                data["Instance"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("NodeType: no recognized variant key")


def redact_sensitive(value: NodeType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "Instance" in value:
        import capo_ssm.types.instance_info

        out["Instance"] = capo_ssm.types.instance_info.redact_sensitive(
            value["Instance"]
        )
    return out
