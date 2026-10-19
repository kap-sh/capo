"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GetPlanEvaluationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_arc_region_switch.types.evaluation_status
    import capo_arc_region_switch.types.next_token
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.plan_warnings
    import capo_arc_region_switch.types.region


class GetPlanEvaluationStatusResponse(TypedDict, closed=True):
    plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    last_evaluation_time: NotRequired["datetime.datetime"]
    """<p>The time of the last time that Region switch ran an evaluation of the plan.</p>"""
    last_evaluated_version: NotRequired["str"]
    """<p>The version of the last evaluation of the plan.</p>"""
    region: NotRequired["capo_arc_region_switch.types.region.Region"]
    """<p>The Amazon Web Services Region for the plan.</p>"""
    evaluation_state: NotRequired[
        "capo_arc_region_switch.types.evaluation_status.EvaluationStatus"
    ]
    """<p>The evaluation state for the plan.</p>"""
    warnings: NotRequired["capo_arc_region_switch.types.plan_warnings.PlanWarnings"]
    """<p>The current evaluation warnings for the plan. </p>"""
    next_token: NotRequired["capo_arc_region_switch.types.next_token.NextToken"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPlanEvaluationStatusResponse) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    if "last_evaluation_time" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["lastEvaluationTime"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_evaluation_time"]
            )
        )
    if "last_evaluated_version" in value:
        out["lastEvaluatedVersion"] = value["last_evaluated_version"]
    if "region" in value:
        out["region"] = value["region"]
    if "evaluation_state" in value:
        import capo_arc_region_switch.types.evaluation_status

        out["evaluationState"] = (
            capo_arc_region_switch.types.evaluation_status.serialize_aws_json_1_0(
                value["evaluation_state"]
            )
        )
    if "warnings" in value:
        import capo_arc_region_switch.types.plan_warnings

        out["warnings"] = (
            capo_arc_region_switch.types.plan_warnings.serialize_aws_json_1_0(
                value["warnings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPlanEvaluationStatusResponse:
    out: GetPlanEvaluationStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("planArn") is not None:
        out["plan_arn"] = data["planArn"]
    else:
        out["plan_arn"] = ""
    if data.get("lastEvaluationTime") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["last_evaluation_time"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastEvaluationTime"]
            )
        )
    if data.get("lastEvaluatedVersion") is not None:
        out["last_evaluated_version"] = data["lastEvaluatedVersion"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("evaluationState") is not None:
        import capo_arc_region_switch.types.evaluation_status

        out["evaluation_state"] = (
            capo_arc_region_switch.types.evaluation_status.deserialize_aws_json_1_0(
                data["evaluationState"]
            )
        )
    if data.get("warnings") is not None:
        import capo_arc_region_switch.types.plan_warnings

        out["warnings"] = (
            capo_arc_region_switch.types.plan_warnings.deserialize_aws_json_1_0(
                data["warnings"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
