"""Generated from Smithy shape ``com.amazonaws.lambdaweb#FunctionRevisionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_web.types.function_revision_summary

FunctionRevisionSummaryList: TypeAlias = list[
    "capo_lambda_web.types.function_revision_summary.FunctionRevisionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionRevisionSummaryList) -> list:
    import capo_lambda_web.types.function_revision_summary

    out: list = []
    for item in value:
        out.append(capo_lambda_web.types.function_revision_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunctionRevisionSummaryList:
    import capo_lambda_web.types.function_revision_summary

    out: FunctionRevisionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda_web.types.function_revision_summary.deserialize_json(item)
        )
    return out
