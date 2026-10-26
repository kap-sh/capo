"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetEvaluatorResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.evaluator_arn
    import capo_bedrock_agentcore_control.types.evaluator_config
    import capo_bedrock_agentcore_control.types.evaluator_description
    import capo_bedrock_agentcore_control.types.evaluator_id
    import capo_bedrock_agentcore_control.types.evaluator_level
    import capo_bedrock_agentcore_control.types.evaluator_name
    import capo_bedrock_agentcore_control.types.evaluator_status
    import capo_bedrock_agentcore_control.types.evaluator_type
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.provider


class GetEvaluatorResponse(TypedDict, closed=True):
    evaluator_arn: "capo_bedrock_agentcore_control.types.evaluator_arn.EvaluatorArn"
    """<p> The Amazon Resource Name (ARN) of the evaluator. </p>"""
    evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the evaluator. </p>"""
    evaluator_name: "capo_bedrock_agentcore_control.types.evaluator_name.EvaluatorName"
    """<p> The name of the evaluator. </p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.evaluator_description.EvaluatorDescription"
    ]
    """<p> The description of the evaluator. </p>"""
    evaluator_config: (
        "capo_bedrock_agentcore_control.types.evaluator_config.EvaluatorConfig"
    )
    """<p> The configuration of the evaluator, including LLM-as-a-Judge or code-based settings. </p>"""
    evaluator_type: NotRequired[
        "capo_bedrock_agentcore_control.types.evaluator_type.EvaluatorType"
    ]
    """<p> The kind of evaluator resource. Valid values: </p> <ul> <li> <p> <code>Builtin</code> – An Amazon Web Services-managed global evaluator.</p> </li> <li> <p> <code>ThirdParty</code> – An Amazon Web Services-managed global evaluator from a third-party provider.</p> </li> <li> <p> <code>Custom</code> – A customer-created evaluator.</p> </li> <li> <p> <code>CustomCode</code> – A customer-created code-based evaluator.</p> </li> <li> <p> <code>CustomDerived</code> – A customer-created evaluator derived from an existing base evaluator.</p> </li> </ul>"""
    provider: NotRequired["capo_bedrock_agentcore_control.types.provider.Provider"]
    """<p> The source of the evaluator's logic: Amazon Web Services, a third-party library, or you. </p>"""
    level: "capo_bedrock_agentcore_control.types.evaluator_level.EvaluatorLevel"
    """<p> The evaluation level (<code>TOOL_CALL</code>, <code>TRACE</code>, or <code>SESSION</code>) that determines the scope of evaluation. </p>"""
    status: "capo_bedrock_agentcore_control.types.evaluator_status.EvaluatorStatus"
    """<p> The current status of the evaluator. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when the evaluator was created. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the evaluator was last updated. </p>"""
    locked_for_modification: NotRequired["bool"]
    """<p> Whether the evaluator is locked for modification due to being referenced by active online evaluation configurations. </p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the customer managed KMS key used to encrypt the evaluator's sensitive data. This field is only present for evaluators encrypted with a customer managed key. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvaluatorResponse) -> dict:
    out: dict = {}
    out["evaluatorArn"] = value["evaluator_arn"]
    out["evaluatorId"] = value["evaluator_id"]
    out["evaluatorName"] = value["evaluator_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.evaluator_config

    out["evaluatorConfig"] = (
        capo_bedrock_agentcore_control.types.evaluator_config.serialize_json(
            value["evaluator_config"]
        )
    )
    if "evaluator_type" in value:
        import capo_bedrock_agentcore_control.types.evaluator_type

        out["evaluatorType"] = (
            capo_bedrock_agentcore_control.types.evaluator_type.serialize_json(
                value["evaluator_type"]
            )
        )
    if "provider" in value:
        import capo_bedrock_agentcore_control.types.provider

        out["provider"] = capo_bedrock_agentcore_control.types.provider.serialize_json(
            value["provider"]
        )
    import capo_bedrock_agentcore_control.types.evaluator_level

    out["level"] = capo_bedrock_agentcore_control.types.evaluator_level.serialize_json(
        value["level"]
    )
    import capo_bedrock_agentcore_control.types.evaluator_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.evaluator_status.serialize_json(
            value["status"]
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
    if "locked_for_modification" in value:
        out["lockedForModification"] = value["locked_for_modification"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetEvaluatorResponse:
    out: GetEvaluatorResponse = {}  # type: ignore[typeddict-item]
    if data.get("evaluatorArn") is not None:
        out["evaluator_arn"] = data["evaluatorArn"]
    else:
        out["evaluator_arn"] = ""
    if data.get("evaluatorId") is not None:
        out["evaluator_id"] = data["evaluatorId"]
    else:
        out["evaluator_id"] = ""
    if data.get("evaluatorName") is not None:
        out["evaluator_name"] = data["evaluatorName"]
    else:
        out["evaluator_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("evaluatorConfig") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_config

        out["evaluator_config"] = (
            capo_bedrock_agentcore_control.types.evaluator_config.deserialize_json(
                data["evaluatorConfig"]
            )
        )
    else:
        out["evaluator_config"] = {"$unknown": {"name": ""}}
    if data.get("evaluatorType") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_type

        out["evaluator_type"] = (
            capo_bedrock_agentcore_control.types.evaluator_type.deserialize_json(
                data["evaluatorType"]
            )
        )
    if data.get("provider") is not None:
        import capo_bedrock_agentcore_control.types.provider

        out["provider"] = (
            capo_bedrock_agentcore_control.types.provider.deserialize_json(
                data["provider"]
            )
        )
    if data.get("level") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_level

        out["level"] = (
            capo_bedrock_agentcore_control.types.evaluator_level.deserialize_json(
                data["level"]
            )
        )
    else:
        import typing

        out["level"] = typing.cast(
            "capo_bedrock_agentcore_control.types.evaluator_level.EvaluatorLevel", ""
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.evaluator_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.evaluator_status.EvaluatorStatus", ""
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
    if data.get("lockedForModification") is not None:
        out["locked_for_modification"] = data["lockedForModification"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out


def redact_sensitive(value: GetEvaluatorResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "evaluator_config" in value:
        import capo_bedrock_agentcore_control.types.evaluator_config

        out["evaluator_config"] = (
            capo_bedrock_agentcore_control.types.evaluator_config.redact_sensitive(
                value["evaluator_config"]
            )
        )
    return out
