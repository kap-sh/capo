"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetDataQualityRulesetEvaluationRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_ruleset_evaluation_run_id_list


class BatchGetDataQualityRulesetEvaluationRunRequest(TypedDict, closed=True):
    run_ids: "capo_glue.types.data_quality_ruleset_evaluation_run_id_list.DataQualityRulesetEvaluationRunIdList"
    """<p>A list of unique run identifiers for the evaluation runs to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchGetDataQualityRulesetEvaluationRunRequest,
) -> dict:
    out: dict = {}
    import capo_glue.types.data_quality_ruleset_evaluation_run_id_list

    out["RunIds"] = (
        capo_glue.types.data_quality_ruleset_evaluation_run_id_list.serialize_aws_json_1_1(
            value["run_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchGetDataQualityRulesetEvaluationRunRequest:
    out: BatchGetDataQualityRulesetEvaluationRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("RunIds") is not None:
        import capo_glue.types.data_quality_ruleset_evaluation_run_id_list

        out["run_ids"] = (
            capo_glue.types.data_quality_ruleset_evaluation_run_id_list.deserialize_aws_json_1_1(
                data["RunIds"]
            )
        )
    else:
        out["run_ids"] = []
    return out
