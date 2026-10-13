"""Generated from Smithy shape ``com.amazonaws.fsx#Volumes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.volume

Volumes: TypeAlias = list["capo_fsx.types.volume.Volume"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Volumes) -> list:
    import capo_fsx.types.volume

    out: list = []
    for item in value:
        out.append(capo_fsx.types.volume.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Volumes:
    import capo_fsx.types.volume

    out: Volumes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fsx.types.volume.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Volumes) -> list[Any]:
    import capo_fsx.types.volume

    return [capo_fsx.types.volume.redact_sensitive(item) for item in value]
