"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdictToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.analysis
    import capo_mailmanager.types.rule_verdict_attribute


class RuleVerdictToEvaluateAttributeMember(TypedDict, closed=True):
    Attribute: "capo_mailmanager.types.rule_verdict_attribute.RuleVerdictAttribute"


class RuleVerdictToEvaluateAnalysisMember(TypedDict, closed=True):
    Analysis: "capo_mailmanager.types.analysis.Analysis"


RuleVerdictToEvaluate: TypeAlias = (
    RuleVerdictToEvaluateAttributeMember
    | RuleVerdictToEvaluateAnalysisMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVerdictToEvaluate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RuleVerdictToEvaluate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Attribute" in value:
        import capo_mailmanager.types.rule_verdict_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_verdict_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    elif "Analysis" in value:
        import capo_mailmanager.types.analysis

        return {
            "Analysis": capo_mailmanager.types.analysis.serialize_aws_json_1_0(
                value["Analysis"]
            )
        }
    else:
        raise SerializationError("RuleVerdictToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleVerdictToEvaluate:
    if data.get("Attribute") is not None:
        import capo_mailmanager.types.rule_verdict_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_verdict_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    elif data.get("Analysis") is not None:
        import capo_mailmanager.types.analysis

        return {
            "Analysis": capo_mailmanager.types.analysis.deserialize_aws_json_1_0(
                data["Analysis"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RuleVerdictToEvaluate: no recognized variant key")
