"""Generated from Smithy shape ``com.amazonaws.fms#EntryViolations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.entry_violation

EntryViolations: TypeAlias = list["capo_fms.types.entry_violation.EntryViolation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntryViolations) -> list:
    import capo_fms.types.entry_violation

    out: list = []
    for item in value:
        out.append(capo_fms.types.entry_violation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntryViolations:
    import capo_fms.types.entry_violation

    out: EntryViolations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.entry_violation.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntryViolations) -> list:
    import capo_fms.types.entry_violation

    out: list = []
    for item in value:
        out.append(capo_fms.types.entry_violation.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EntryViolations:
    import capo_fms.types.entry_violation

    out: EntryViolations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.entry_violation.deserialize_cbor(item))
    return out
