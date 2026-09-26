"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmImageBuildSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_build_summary

MicrovmImageBuildSummaries: TypeAlias = list[
    "capo_lambda_microvms.types.microvm_image_build_summary.MicrovmImageBuildSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmImageBuildSummaries) -> list:
    import capo_lambda_microvms.types.microvm_image_build_summary

    out: list = []
    for item in value:
        out.append(
            capo_lambda_microvms.types.microvm_image_build_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MicrovmImageBuildSummaries:
    import capo_lambda_microvms.types.microvm_image_build_summary

    out: MicrovmImageBuildSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda_microvms.types.microvm_image_build_summary.deserialize_json(
                item
            )
        )
    return out
