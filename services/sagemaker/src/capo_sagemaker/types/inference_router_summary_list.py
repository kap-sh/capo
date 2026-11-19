"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRouterSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_summary

InferenceRouterSummaryList: TypeAlias = list[
    "capo_sagemaker.types.inference_router_summary.InferenceRouterSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRouterSummaryList) -> list:
    import capo_sagemaker.types.inference_router_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.inference_router_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceRouterSummaryList:
    import capo_sagemaker.types.inference_router_summary

    out: InferenceRouterSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.inference_router_summary.deserialize_aws_json_1_1(item)
        )
    return out
