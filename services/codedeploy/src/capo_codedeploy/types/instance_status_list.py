"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.instance_status

InstanceStatusList: TypeAlias = list[
    "capo_codedeploy.types.instance_status.InstanceStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceStatusList) -> list:
    import capo_codedeploy.types.instance_status

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.instance_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceStatusList:
    import capo_codedeploy.types.instance_status

    out: InstanceStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.instance_status.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceStatusList) -> list:
    import capo_codedeploy.types.instance_status

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.instance_status.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> InstanceStatusList:
    import capo_codedeploy.types.instance_status

    out: InstanceStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.instance_status.deserialize_cbor(item))
    return out
