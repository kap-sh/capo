"""Generated from Smithy shape ``com.amazonaws.configservice#PutExternalEvaluationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.external_evaluation


class PutExternalEvaluationRequest(TypedDict, closed=True):
    config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule.</p>"""
    external_evaluation: (
        "capo_config_service.types.external_evaluation.ExternalEvaluation"
    )
    """<p>An <code>ExternalEvaluation</code> object that provides details about compliance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutExternalEvaluationRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    import capo_config_service.types.external_evaluation

    out["ExternalEvaluation"] = (
        capo_config_service.types.external_evaluation.serialize_aws_json_1_1(
            value["external_evaluation"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutExternalEvaluationRequest:
    out: PutExternalEvaluationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        out["config_rule_name"] = ""
    if data.get("ExternalEvaluation") is not None:
        import capo_config_service.types.external_evaluation

        out["external_evaluation"] = (
            capo_config_service.types.external_evaluation.deserialize_aws_json_1_1(
                data["ExternalEvaluation"]
            )
        )
    else:
        raise DeserializationError(
            "PutExternalEvaluationRequest.external_evaluation required"
        )
    return out
