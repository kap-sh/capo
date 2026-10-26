"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAnalysisRulePolicy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_analysis_rule_policy_v1


class _ConfiguredTableAnalysisRulePolicy_v1(TypedDict, closed=True):
    v1: "capo_cleanrooms.types.configured_table_analysis_rule_policy_v1.ConfiguredTableAnalysisRulePolicyV1"


ConfiguredTableAnalysisRulePolicy: TypeAlias = (
    _ConfiguredTableAnalysisRulePolicy_v1 | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAnalysisRulePolicy) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConfiguredTableAnalysisRulePolicy: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "v1" in value:
        import capo_cleanrooms.types.configured_table_analysis_rule_policy_v1

        return {
            "v1": capo_cleanrooms.types.configured_table_analysis_rule_policy_v1.serialize_json(
                value["v1"]
            )
        }
    else:
        raise SerializationError(
            "ConfiguredTableAnalysisRulePolicy: no variant present"
        )


def deserialize_json(data: dict) -> ConfiguredTableAnalysisRulePolicy:
    if data.get("v1") is not None:
        import capo_cleanrooms.types.configured_table_analysis_rule_policy_v1

        return {
            "v1": capo_cleanrooms.types.configured_table_analysis_rule_policy_v1.deserialize_json(
                data["v1"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ConfiguredTableAnalysisRulePolicy: no recognized variant key"
        )
