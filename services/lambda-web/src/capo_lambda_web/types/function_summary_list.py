"""Generated from Smithy shape ``com.amazonaws.lambdaweb#FunctionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_web.types.function_summary

FunctionSummaryList: TypeAlias = list[
    "capo_lambda_web.types.function_summary.FunctionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionSummaryList) -> list:
    import capo_lambda_web.types.function_summary

    out: list = []
    for item in value:
        out.append(capo_lambda_web.types.function_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunctionSummaryList:
    import capo_lambda_web.types.function_summary

    out: FunctionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_web.types.function_summary.deserialize_json(item))
    return out
