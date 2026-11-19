"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#PreviewResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.preview_result

PreviewResults: TypeAlias = list[
    "capo_compute_optimizer_automation.types.preview_result.PreviewResult"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreviewResults) -> list:
    import capo_compute_optimizer_automation.types.preview_result

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.preview_result.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PreviewResults:
    import capo_compute_optimizer_automation.types.preview_result

    out: PreviewResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.preview_result.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PreviewResults) -> list:
    import capo_compute_optimizer_automation.types.preview_result

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.preview_result.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PreviewResults:
    import capo_compute_optimizer_automation.types.preview_result

    out: PreviewResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.preview_result.deserialize_cbor(
                item
            )
        )
    return out
