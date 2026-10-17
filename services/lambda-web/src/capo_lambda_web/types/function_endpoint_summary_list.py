"""Generated from Smithy shape ``com.amazonaws.lambdaweb#FunctionEndpointSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_web.types.function_endpoint_summary

FunctionEndpointSummaryList: TypeAlias = list[
    "capo_lambda_web.types.function_endpoint_summary.FunctionEndpointSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionEndpointSummaryList) -> list:
    import capo_lambda_web.types.function_endpoint_summary

    out: list = []
    for item in value:
        out.append(capo_lambda_web.types.function_endpoint_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunctionEndpointSummaryList:
    import capo_lambda_web.types.function_endpoint_summary

    out: FunctionEndpointSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda_web.types.function_endpoint_summary.deserialize_json(item)
        )
    return out
