"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UsageInstructions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.usage_instruction

UsageInstructions: TypeAlias = list[
    "capo_service_catalog.types.usage_instruction.UsageInstruction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageInstructions) -> list:
    import capo_service_catalog.types.usage_instruction

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.usage_instruction.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UsageInstructions:
    import capo_service_catalog.types.usage_instruction

    out: UsageInstructions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.usage_instruction.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UsageInstructions) -> list:
    import capo_service_catalog.types.usage_instruction

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.usage_instruction.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> UsageInstructions:
    import capo_service_catalog.types.usage_instruction

    out: UsageInstructions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.usage_instruction.deserialize_cbor(item))
    return out
