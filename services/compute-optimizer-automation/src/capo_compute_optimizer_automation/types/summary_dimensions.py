"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#SummaryDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.summary_dimension

SummaryDimensions: TypeAlias = list[
    "capo_compute_optimizer_automation.types.summary_dimension.SummaryDimension"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryDimensions) -> list:
    import capo_compute_optimizer_automation.types.summary_dimension

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.summary_dimension.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SummaryDimensions:
    import capo_compute_optimizer_automation.types.summary_dimension

    out: SummaryDimensions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.summary_dimension.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SummaryDimensions) -> list:
    import capo_compute_optimizer_automation.types.summary_dimension

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.summary_dimension.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> SummaryDimensions:
    import capo_compute_optimizer_automation.types.summary_dimension

    out: SummaryDimensions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.summary_dimension.deserialize_cbor(
                item
            )
        )
    return out
