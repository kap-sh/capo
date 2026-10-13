"""Generated from Smithy shape ``com.amazonaws.ssm#NodeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.node

NodeList: TypeAlias = list["capo_ssm.types.node.Node"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeList) -> list:
    import capo_ssm.types.node

    out: list = []
    for item in value:
        out.append(capo_ssm.types.node.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NodeList:
    import capo_ssm.types.node

    out: NodeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.node.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: NodeList) -> list[Any]:
    import capo_ssm.types.node

    return [capo_ssm.types.node.redact_sensitive(item) for item in value]
