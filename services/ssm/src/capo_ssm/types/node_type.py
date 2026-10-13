"""Generated from Smithy shape ``com.amazonaws.ssm#NodeType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_ssm.types.instance_info


class _NodeType_Instance(TypedDict, closed=True):
    Instance: "capo_ssm.types.instance_info.InstanceInfo"


NodeType: TypeAlias = _NodeType_Instance


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeType) -> dict:
    if "Instance" in value:
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
        raise DeserializationError("NodeType: no recognized variant key")


def redact_sensitive(value: NodeType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "Instance" in value:
        import capo_ssm.types.instance_info

        out["Instance"] = capo_ssm.types.instance_info.redact_sensitive(
            value["Instance"]
        )
    return out
