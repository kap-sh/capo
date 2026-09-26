"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmImageSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_summary

MicrovmImageSummaries: TypeAlias = list[
    "capo_lambda_microvms.types.microvm_image_summary.MicrovmImageSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmImageSummaries) -> list:
    import capo_lambda_microvms.types.microvm_image_summary

    out: list = []
    for item in value:
        out.append(
            capo_lambda_microvms.types.microvm_image_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MicrovmImageSummaries:
    import capo_lambda_microvms.types.microvm_image_summary

    out: MicrovmImageSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda_microvms.types.microvm_image_summary.deserialize_json(item)
        )
    return out
