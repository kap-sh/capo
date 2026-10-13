"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePatchStateList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_patch_state

InstancePatchStateList: TypeAlias = list[
    "capo_ssm.types.instance_patch_state.InstancePatchState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePatchStateList) -> list:
    import capo_ssm.types.instance_patch_state

    out: list = []
    for item in value:
        out.append(capo_ssm.types.instance_patch_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePatchStateList:
    import capo_ssm.types.instance_patch_state

    out: InstancePatchStateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.instance_patch_state.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: InstancePatchStateList) -> list[Any]:
    import capo_ssm.types.instance_patch_state

    return [
        capo_ssm.types.instance_patch_state.redact_sensitive(item) for item in value
    ]
