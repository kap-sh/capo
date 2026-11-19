"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceRoutersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_summary_list
    import capo_sagemaker.types.next_token


class ListInferenceRoutersOutput(TypedDict, closed=True):
    inference_routers: NotRequired[
        "capo_sagemaker.types.inference_router_summary_list.InferenceRouterSummaryList"
    ]
    """<p>A list of summaries of the inference routers.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker AI returns this token. To get the next set of inference routers, use it in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceRoutersOutput) -> dict:
    out: dict = {}
    if "inference_routers" in value:
        import capo_sagemaker.types.inference_router_summary_list

        out["InferenceRouters"] = (
            capo_sagemaker.types.inference_router_summary_list.serialize_aws_json_1_1(
                value["inference_routers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInferenceRoutersOutput:
    out: ListInferenceRoutersOutput = {}  # type: ignore[typeddict-item]
    if data.get("InferenceRouters") is not None:
        import capo_sagemaker.types.inference_router_summary_list

        out["inference_routers"] = (
            capo_sagemaker.types.inference_router_summary_list.deserialize_aws_json_1_1(
                data["InferenceRouters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
