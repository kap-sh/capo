"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UsageInstruction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.instruction_type
    import capo_service_catalog.types.instruction_value


class UsageInstruction(TypedDict, closed=True):
    type: NotRequired["capo_service_catalog.types.instruction_type.InstructionType"]
    """<p>The usage instruction type for the value.</p>"""
    value: NotRequired["capo_service_catalog.types.instruction_value.InstructionValue"]
    """<p>The usage instruction value for this type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageInstruction) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UsageInstruction:
    out: UsageInstruction = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UsageInstruction) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> UsageInstruction:
    out: UsageInstruction = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
