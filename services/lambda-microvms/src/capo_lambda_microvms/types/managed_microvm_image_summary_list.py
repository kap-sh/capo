"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ManagedMicrovmImageSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.managed_microvm_image_summary

ManagedMicrovmImageSummaryList: TypeAlias = list[
    "capo_lambda_microvms.types.managed_microvm_image_summary.ManagedMicrovmImageSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedMicrovmImageSummaryList) -> list:
    import capo_lambda_microvms.types.managed_microvm_image_summary

    out: list = []
    for item in value:
        out.append(
            capo_lambda_microvms.types.managed_microvm_image_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedMicrovmImageSummaryList:
    import capo_lambda_microvms.types.managed_microvm_image_summary

    out: ManagedMicrovmImageSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda_microvms.types.managed_microvm_image_summary.deserialize_json(
                item
            )
        )
    return out
