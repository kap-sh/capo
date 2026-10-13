"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePatchStatesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_patch_state

InstancePatchStatesList: TypeAlias = list[
    "capo_ssm.types.instance_patch_state.InstancePatchState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePatchStatesList) -> list:
    import capo_ssm.types.instance_patch_state

    out: list = []
    for item in value:
        out.append(capo_ssm.types.instance_patch_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePatchStatesList:
    import capo_ssm.types.instance_patch_state

    out: InstancePatchStatesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.instance_patch_state.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: InstancePatchStatesList) -> list[Any]:
    import capo_ssm.types.instance_patch_state

    return [
        capo_ssm.types.instance_patch_state.redact_sensitive(item) for item in value
    ]
