"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ResourceDescriptions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cloudcontrol.types.resource_description

ResourceDescriptions: TypeAlias = list[
    "capo_cloudcontrol.types.resource_description.ResourceDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceDescriptions) -> list:
    import capo_cloudcontrol.types.resource_description

    out: list = []
    for item in value:
        out.append(
            capo_cloudcontrol.types.resource_description.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceDescriptions:
    import capo_cloudcontrol.types.resource_description

    out: ResourceDescriptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudcontrol.types.resource_description.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: ResourceDescriptions) -> list[Any]:
    import capo_cloudcontrol.types.resource_description

    return [
        capo_cloudcontrol.types.resource_description.redact_sensitive(item)
        for item in value
    ]
