"""Generated from Smithy shape ``com.amazonaws.devicefarm#Jobs``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.job

Jobs: TypeAlias = list["capo_device_farm.types.job.Job"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Jobs) -> list:
    import capo_device_farm.types.job

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.job.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Jobs:
    import capo_device_farm.types.job

    out: Jobs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_device_farm.types.job.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Jobs) -> list[Any]:
    import capo_device_farm.types.job

    return [capo_device_farm.types.job.redact_sensitive(item) for item in value]
