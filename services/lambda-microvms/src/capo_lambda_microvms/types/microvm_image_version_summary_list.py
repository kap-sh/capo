"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmImageVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_version_summary

MicrovmImageVersionSummaryList: TypeAlias = list[
    "capo_lambda_microvms.types.microvm_image_version_summary.MicrovmImageVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmImageVersionSummaryList) -> list:
    import capo_lambda_microvms.types.microvm_image_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_lambda_microvms.types.microvm_image_version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MicrovmImageVersionSummaryList:
    import capo_lambda_microvms.types.microvm_image_version_summary

    out: MicrovmImageVersionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda_microvms.types.microvm_image_version_summary.deserialize_json(
                item
            )
        )
    return out
