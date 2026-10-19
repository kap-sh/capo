"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartBatchEvaluationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.batch_evaluation_description
    import capo_bedrock_agentcore.types.batch_evaluation_name
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.data_source_config
    import capo_bedrock_agentcore.types.evaluation_metadata
    import capo_bedrock_agentcore.types.evaluator_list
    import capo_bedrock_agentcore.types.insight_list
    import capo_bedrock_agentcore.types.kms_key_arn
    import capo_bedrock_agentcore.types.output_config
    import capo_bedrock_agentcore.types.tags_map


class StartBatchEvaluationRequest(TypedDict, closed=True):
    batch_evaluation_name: (
        "capo_bedrock_agentcore.types.batch_evaluation_name.BatchEvaluationName"
    )
    """<p>The name of the batch evaluation. Must be unique within your account.</p>"""
    evaluators: NotRequired["capo_bedrock_agentcore.types.evaluator_list.EvaluatorList"]
    """<p>The list of evaluators to apply during the batch evaluation. Can include both built-in evaluators and custom evaluators. Maximum of 10 evaluators.</p>"""
    insights: NotRequired["capo_bedrock_agentcore.types.insight_list.InsightList"]
    """<p>The list of insight analyses to run against sessions during the batch evaluation. Maximum of 10 insights.</p>"""
    data_source_config: (
        "capo_bedrock_agentcore.types.data_source_config.DataSourceConfig"
    )
    """<p>The data source configuration that specifies where to pull agent session traces from for evaluation.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""
    evaluation_metadata: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_metadata.EvaluationMetadata"
    ]
    """<p>Optional metadata for the evaluation, including session-specific ground truth data and test scenario identifiers.</p>"""
    tags: NotRequired["capo_bedrock_agentcore.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to associate with the batch evaluation.</p>"""
    kms_key_arn: NotRequired["capo_bedrock_agentcore.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key used to encrypt evaluation data. If provided, customer data is encrypted at rest with the specified key.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"
    ]
    """<p>The description of the batch evaluation.</p>"""
    output_config: NotRequired[
        "capo_bedrock_agentcore.types.output_config.OutputConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: StartBatchEvaluationRequest) -> dict:
    out: dict = {}
    out["batchEvaluationName"] = value["batch_evaluation_name"]
    if "evaluators" in value:
        import capo_bedrock_agentcore.types.evaluator_list

        out["evaluators"] = capo_bedrock_agentcore.types.evaluator_list.serialize_json(
            value["evaluators"]
        )
    if "insights" in value:
        import capo_bedrock_agentcore.types.insight_list

        out["insights"] = capo_bedrock_agentcore.types.insight_list.serialize_json(
            value["insights"]
        )
    import capo_bedrock_agentcore.types.data_source_config

    out["dataSourceConfig"] = (
        capo_bedrock_agentcore.types.data_source_config.serialize_json(
            value["data_source_config"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "evaluation_metadata" in value:
        import capo_bedrock_agentcore.types.evaluation_metadata

        out["evaluationMetadata"] = (
            capo_bedrock_agentcore.types.evaluation_metadata.serialize_json(
                value["evaluation_metadata"]
            )
        )
    if "tags" in value:
        import capo_bedrock_agentcore.types.tags_map

        out["tags"] = capo_bedrock_agentcore.types.tags_map.serialize_json(
            value["tags"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "output_config" in value:
        import capo_bedrock_agentcore.types.output_config

        out["outputConfig"] = capo_bedrock_agentcore.types.output_config.serialize_json(
            value["output_config"]
        )
    return out


def deserialize_json(data: dict) -> StartBatchEvaluationRequest:
    out: StartBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
    if data.get("batchEvaluationName") is not None:
        out["batch_evaluation_name"] = data["batchEvaluationName"]
    else:
        out["batch_evaluation_name"] = ""
    if data.get("evaluators") is not None:
        import capo_bedrock_agentcore.types.evaluator_list

        out["evaluators"] = (
            capo_bedrock_agentcore.types.evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
    if data.get("insights") is not None:
        import capo_bedrock_agentcore.types.insight_list

        out["insights"] = capo_bedrock_agentcore.types.insight_list.deserialize_json(
            data["insights"]
        )
    if data.get("dataSourceConfig") is not None:
        import capo_bedrock_agentcore.types.data_source_config

        out["data_source_config"] = (
            capo_bedrock_agentcore.types.data_source_config.deserialize_json(
                data["dataSourceConfig"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["data_source_config"] = (
            capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("evaluationMetadata") is not None:
        import capo_bedrock_agentcore.types.evaluation_metadata

        out["evaluation_metadata"] = (
            capo_bedrock_agentcore.types.evaluation_metadata.deserialize_json(
                data["evaluationMetadata"]
            )
        )
    if data.get("tags") is not None:
        import capo_bedrock_agentcore.types.tags_map

        out["tags"] = capo_bedrock_agentcore.types.tags_map.deserialize_json(
            data["tags"]
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("outputConfig") is not None:
        import capo_bedrock_agentcore.types.output_config

        out["output_config"] = (
            capo_bedrock_agentcore.types.output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    return out
