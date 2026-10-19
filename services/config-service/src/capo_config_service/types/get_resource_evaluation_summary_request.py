"""Generated from Smithy shape ``com.amazonaws.configservice#GetResourceEvaluationSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.resource_evaluation_id


class GetResourceEvaluationSummaryRequest(TypedDict, closed=True):
    resource_evaluation_id: (
        "capo_config_service.types.resource_evaluation_id.ResourceEvaluationId"
    )
    """<p>The unique <code>ResourceEvaluationId</code> of Amazon Web Services resource execution for which you want to retrieve the evaluation summary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceEvaluationSummaryRequest) -> dict:
    out: dict = {}
    out["ResourceEvaluationId"] = value["resource_evaluation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceEvaluationSummaryRequest:
    out: GetResourceEvaluationSummaryRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceEvaluationId") is not None:
        out["resource_evaluation_id"] = data["ResourceEvaluationId"]
    else:
        out["resource_evaluation_id"] = ""
    return out
