"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteEvaluationResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.string_with_char_limit64


class DeleteEvaluationResultsRequest(TypedDict, closed=True):
    config_rule_name: (
        "capo_config_service.types.string_with_char_limit64.StringWithCharLimit64"
    )
    """<p>The name of the Config rule for which you want to delete the evaluation results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEvaluationResultsRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEvaluationResultsRequest:
    out: DeleteEvaluationResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        out["config_rule_name"] = ""
    return out
