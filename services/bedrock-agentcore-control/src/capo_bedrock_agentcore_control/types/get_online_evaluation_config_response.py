"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetOnlineEvaluationConfigResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.clustering_config
    import capo_bedrock_agentcore_control.types.data_source_config
    import capo_bedrock_agentcore_control.types.evaluation_config_description
    import capo_bedrock_agentcore_control.types.evaluation_config_name
    import capo_bedrock_agentcore_control.types.evaluator_list
    import capo_bedrock_agentcore_control.types.insight_list
    import capo_bedrock_agentcore_control.types.online_evaluation_config_arn
    import capo_bedrock_agentcore_control.types.online_evaluation_config_id
    import capo_bedrock_agentcore_control.types.online_evaluation_config_status
    import capo_bedrock_agentcore_control.types.online_evaluation_execution_status
    import capo_bedrock_agentcore_control.types.output_config
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.rule


class GetOnlineEvaluationConfigResponse(TypedDict, closed=True):
    online_evaluation_config_arn: "capo_bedrock_agentcore_control.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p> The Amazon Resource Name (ARN) of the online evaluation configuration. </p>"""
    online_evaluation_config_id: "capo_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the online evaluation configuration. </p>"""
    online_evaluation_config_name: "capo_bedrock_agentcore_control.types.evaluation_config_name.EvaluationConfigName"
    """<p> The name of the online evaluation configuration. </p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
    ]
    """<p> The description of the online evaluation configuration. </p>"""
    rule: "capo_bedrock_agentcore_control.types.rule.Rule"
    """<p> The evaluation rule containing sampling configuration, filters, and session settings. </p>"""
    data_source_config: (
        "capo_bedrock_agentcore_control.types.data_source_config.DataSourceConfig"
    )
    """<p> The data source configuration specifying CloudWatch log groups and service names to monitor. </p>"""
    evaluators: "capo_bedrock_agentcore_control.types.evaluator_list.EvaluatorList"
    """<p> The list of evaluators applied during online evaluation. </p>"""
    insights: NotRequired[
        "capo_bedrock_agentcore_control.types.insight_list.InsightList"
    ]
    """<p>The list of insight types configured for this evaluation.</p>"""
    clustering_config: NotRequired[
        "capo_bedrock_agentcore_control.types.clustering_config.ClusteringConfig"
    ]
    """<p>The clustering configuration for periodic batch evaluation.</p>"""
    output_config: NotRequired[
        "capo_bedrock_agentcore_control.types.output_config.OutputConfig"
    ]
    """<p> The output configuration specifying where evaluation results are written. </p>"""
    evaluation_execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the IAM role used for evaluation execution. </p>"""
    status: "capo_bedrock_agentcore_control.types.online_evaluation_config_status.OnlineEvaluationConfigStatus"
    """<p> The status of the online evaluation configuration. </p>"""
    execution_status: "capo_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus"
    """<p> The execution status indicating whether the online evaluation is currently running. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when the online evaluation configuration was created. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the online evaluation configuration was last updated. </p>"""
    failure_reason: NotRequired["str"]
    """<p> The reason for failure if the online evaluation configuration execution failed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOnlineEvaluationConfigResponse) -> dict:
    out: dict = {}
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    out["onlineEvaluationConfigId"] = value["online_evaluation_config_id"]
    out["onlineEvaluationConfigName"] = value["online_evaluation_config_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.rule

    out["rule"] = capo_bedrock_agentcore_control.types.rule.serialize_json(
        value["rule"]
    )
    import capo_bedrock_agentcore_control.types.data_source_config

    out["dataSourceConfig"] = (
        capo_bedrock_agentcore_control.types.data_source_config.serialize_json(
            value["data_source_config"]
        )
    )
    import capo_bedrock_agentcore_control.types.evaluator_list

    out["evaluators"] = (
        capo_bedrock_agentcore_control.types.evaluator_list.serialize_json(
            value.get("evaluators", [])
        )
    )
    if "insights" in value:
        import capo_bedrock_agentcore_control.types.insight_list

        out["insights"] = (
            capo_bedrock_agentcore_control.types.insight_list.serialize_json(
                value["insights"]
            )
        )
    if "clustering_config" in value:
        import capo_bedrock_agentcore_control.types.clustering_config

        out["clusteringConfig"] = (
            capo_bedrock_agentcore_control.types.clustering_config.serialize_json(
                value["clustering_config"]
            )
        )
    if "output_config" in value:
        import capo_bedrock_agentcore_control.types.output_config

        out["outputConfig"] = (
            capo_bedrock_agentcore_control.types.output_config.serialize_json(
                value["output_config"]
            )
        )
    if "evaluation_execution_role_arn" in value:
        out["evaluationExecutionRoleArn"] = value["evaluation_execution_role_arn"]
    import capo_bedrock_agentcore_control.types.online_evaluation_config_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.online_evaluation_config_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types.online_evaluation_execution_status

    out["executionStatus"] = (
        capo_bedrock_agentcore_control.types.online_evaluation_execution_status.serialize_json(
            value["execution_status"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> GetOnlineEvaluationConfigResponse:
    out: GetOnlineEvaluationConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("onlineEvaluationConfigArn") is not None:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        out["online_evaluation_config_arn"] = ""
    if data.get("onlineEvaluationConfigId") is not None:
        out["online_evaluation_config_id"] = data["onlineEvaluationConfigId"]
    else:
        out["online_evaluation_config_id"] = ""
    if data.get("onlineEvaluationConfigName") is not None:
        out["online_evaluation_config_name"] = data["onlineEvaluationConfigName"]
    else:
        out["online_evaluation_config_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("rule") is not None:
        import capo_bedrock_agentcore_control.types.rule

        out["rule"] = capo_bedrock_agentcore_control.types.rule.deserialize_json(
            data["rule"]
        )
    else:
        raise DeserializationError("GetOnlineEvaluationConfigResponse.rule required")
    if data.get("dataSourceConfig") is not None:
        import capo_bedrock_agentcore_control.types.data_source_config

        out["data_source_config"] = (
            capo_bedrock_agentcore_control.types.data_source_config.deserialize_json(
                data["dataSourceConfig"]
            )
        )
    else:
        out["data_source_config"] = {"$unknown": {"name": ""}}
    if data.get("evaluators") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_list

        out["evaluators"] = (
            capo_bedrock_agentcore_control.types.evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
    else:
        out["evaluators"] = []
    if data.get("insights") is not None:
        import capo_bedrock_agentcore_control.types.insight_list

        out["insights"] = (
            capo_bedrock_agentcore_control.types.insight_list.deserialize_json(
                data["insights"]
            )
        )
    if data.get("clusteringConfig") is not None:
        import capo_bedrock_agentcore_control.types.clustering_config

        out["clustering_config"] = (
            capo_bedrock_agentcore_control.types.clustering_config.deserialize_json(
                data["clusteringConfig"]
            )
        )
    if data.get("outputConfig") is not None:
        import capo_bedrock_agentcore_control.types.output_config

        out["output_config"] = (
            capo_bedrock_agentcore_control.types.output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    if data.get("evaluationExecutionRoleArn") is not None:
        out["evaluation_execution_role_arn"] = data["evaluationExecutionRoleArn"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.online_evaluation_config_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_config_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.online_evaluation_config_status.OnlineEvaluationConfigStatus",
            "",
        )
    if data.get("executionStatus") is not None:
        import capo_bedrock_agentcore_control.types.online_evaluation_execution_status

        out["execution_status"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        import typing

        out["execution_status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out


def redact_sensitive(value: GetOnlineEvaluationConfigResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
