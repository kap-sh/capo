"""Generated from Smithy shape ``com.amazonaws.workmail#Resources``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.resource

Resources: TypeAlias = list["capo_workmail.types.resource.Resource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resources) -> list:
    import capo_workmail.types.resource

    out: list = []
    for item in value:
        out.append(capo_workmail.types.resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Resources:
    import capo_workmail.types.resource

    out: Resources = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workmail.types.resource.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Resources) -> list[Any]:
    import capo_workmail.types.resource

    return [capo_workmail.types.resource.redact_sensitive(item) for item in value]
