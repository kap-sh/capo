"""Generated from Smithy shape ``com.amazonaws.fms#ResourceViolations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.resource_violation

ResourceViolations: TypeAlias = list[
    "capo_fms.types.resource_violation.ResourceViolation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceViolations) -> list:
    import capo_fms.types.resource_violation

    out: list = []
    for item in value:
        out.append(capo_fms.types.resource_violation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceViolations:
    import capo_fms.types.resource_violation

    out: ResourceViolations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.resource_violation.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceViolations) -> list:
    import capo_fms.types.resource_violation

    out: list = []
    for item in value:
        out.append(capo_fms.types.resource_violation.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ResourceViolations:
    import capo_fms.types.resource_violation

    out: ResourceViolations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.resource_violation.deserialize_cbor(item))
    return out
