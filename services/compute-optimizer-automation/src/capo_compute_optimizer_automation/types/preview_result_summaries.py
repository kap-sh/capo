"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#PreviewResultSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.preview_result_summary

PreviewResultSummaries: TypeAlias = list[
    "capo_compute_optimizer_automation.types.preview_result_summary.PreviewResultSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreviewResultSummaries) -> list:
    import capo_compute_optimizer_automation.types.preview_result_summary

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.preview_result_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PreviewResultSummaries:
    import capo_compute_optimizer_automation.types.preview_result_summary

    out: PreviewResultSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.preview_result_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PreviewResultSummaries) -> list:
    import capo_compute_optimizer_automation.types.preview_result_summary

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.preview_result_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> PreviewResultSummaries:
    import capo_compute_optimizer_automation.types.preview_result_summary

    out: PreviewResultSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.preview_result_summary.deserialize_cbor(
                item
            )
        )
    return out
