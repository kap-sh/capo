"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateOnlineEvaluationConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.clustering_config
    import capo_bedrock_agentcore_control.types.data_source_config
    import capo_bedrock_agentcore_control.types.evaluation_config_description
    import capo_bedrock_agentcore_control.types.evaluator_list
    import capo_bedrock_agentcore_control.types.insight_list
    import capo_bedrock_agentcore_control.types.online_evaluation_config_id
    import capo_bedrock_agentcore_control.types.online_evaluation_execution_status
    import capo_bedrock_agentcore_control.types.output_config
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.rule


class UpdateOnlineEvaluationConfigRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    online_evaluation_config_id: "capo_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the online evaluation configuration to update. </p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
    ]
    """<p> The updated description of the online evaluation configuration. </p>"""
    rule: NotRequired["capo_bedrock_agentcore_control.types.rule.Rule"]
    """<p> The updated evaluation rule containing sampling configuration, filters, and session settings. </p>"""
    data_source_config: NotRequired[
        "capo_bedrock_agentcore_control.types.data_source_config.DataSourceConfig"
    ]
    """<p> The updated data source configuration specifying CloudWatch log groups and service names to monitor. </p>"""
    evaluators: NotRequired[
        "capo_bedrock_agentcore_control.types.evaluator_list.EvaluatorList"
    ]
    """<p> The updated list of evaluators to apply during online evaluation. </p>"""
    insights: NotRequired[
        "capo_bedrock_agentcore_control.types.insight_list.InsightList"
    ]
    """<p>The updated list of insight types to run against agent sessions.</p>"""
    clustering_config: NotRequired[
        "capo_bedrock_agentcore_control.types.clustering_config.ClusteringConfig"
    ]
    """<p>The updated clustering configuration for periodic batch evaluation.</p>"""
    output_config: NotRequired[
        "capo_bedrock_agentcore_control.types.output_config.OutputConfig"
    ]
    evaluation_execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    ]
    """<p> The updated Amazon Resource Name (ARN) of the IAM role used for evaluation execution. </p>"""
    execution_status: NotRequired[
        "capo_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus"
    ]
    """<p> The updated execution status to enable or disable the online evaluation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOnlineEvaluationConfigRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "rule" in value:
        import capo_bedrock_agentcore_control.types.rule

        out["rule"] = capo_bedrock_agentcore_control.types.rule.serialize_json(
            value["rule"]
        )
    if "data_source_config" in value:
        import capo_bedrock_agentcore_control.types.data_source_config

        out["dataSourceConfig"] = (
            capo_bedrock_agentcore_control.types.data_source_config.serialize_json(
                value["data_source_config"]
            )
        )
    if "evaluators" in value:
        import capo_bedrock_agentcore_control.types.evaluator_list

        out["evaluators"] = (
            capo_bedrock_agentcore_control.types.evaluator_list.serialize_json(
                value["evaluators"]
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
    if "execution_status" in value:
        import capo_bedrock_agentcore_control.types.online_evaluation_execution_status

        out["executionStatus"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_execution_status.serialize_json(
                value["execution_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateOnlineEvaluationConfigRequest:
    out: UpdateOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("rule") is not None:
        import capo_bedrock_agentcore_control.types.rule

        out["rule"] = capo_bedrock_agentcore_control.types.rule.deserialize_json(
            data["rule"]
        )
    if data.get("dataSourceConfig") is not None:
        import capo_bedrock_agentcore_control.types.data_source_config

        out["data_source_config"] = (
            capo_bedrock_agentcore_control.types.data_source_config.deserialize_json(
                data["dataSourceConfig"]
            )
        )
    if data.get("evaluators") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_list

        out["evaluators"] = (
            capo_bedrock_agentcore_control.types.evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
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
    if data.get("executionStatus") is not None:
        import capo_bedrock_agentcore_control.types.online_evaluation_execution_status

        out["execution_status"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    return out
