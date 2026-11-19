"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.flywheel_summary

FlywheelSummaryList: TypeAlias = list[
    "capo_comprehend.types.flywheel_summary.FlywheelSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelSummaryList) -> list:
    import capo_comprehend.types.flywheel_summary

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.flywheel_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FlywheelSummaryList:
    import capo_comprehend.types.flywheel_summary

    out: FlywheelSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.flywheel_summary.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlywheelSummaryList) -> list:
    import capo_comprehend.types.flywheel_summary

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.flywheel_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FlywheelSummaryList:
    import capo_comprehend.types.flywheel_summary

    out: FlywheelSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.flywheel_summary.deserialize_cbor(item))
    return out
