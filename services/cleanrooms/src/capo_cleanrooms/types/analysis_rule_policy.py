"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRulePolicy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_policy_v1


class AnalysisRulePolicyV1Member(TypedDict, closed=True):
    v1: "capo_cleanrooms.types.analysis_rule_policy_v1.AnalysisRulePolicyV1"


AnalysisRulePolicy: TypeAlias = AnalysisRulePolicyV1Member | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRulePolicy) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AnalysisRulePolicy: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "v1" in value:
        import capo_cleanrooms.types.analysis_rule_policy_v1

        return {
            "v1": capo_cleanrooms.types.analysis_rule_policy_v1.serialize_json(
                value["v1"]
            )
        }
    else:
        raise SerializationError("AnalysisRulePolicy: no variant present")


def deserialize_json(data: dict) -> AnalysisRulePolicy:
    if data.get("v1") is not None:
        import capo_cleanrooms.types.analysis_rule_policy_v1

        return {
            "v1": capo_cleanrooms.types.analysis_rule_policy_v1.deserialize_json(
                data["v1"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AnalysisRulePolicy: no recognized variant key")
