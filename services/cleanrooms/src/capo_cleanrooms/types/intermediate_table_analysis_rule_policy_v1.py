"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableAnalysisRulePolicyV1``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_analysis_rule_custom


class _IntermediateTableAnalysisRulePolicyV1_custom(TypedDict, closed=True):
    custom: "capo_cleanrooms.types.intermediate_table_analysis_rule_custom.IntermediateTableAnalysisRuleCustom"


IntermediateTableAnalysisRulePolicyV1: TypeAlias = (
    _IntermediateTableAnalysisRulePolicyV1_custom | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableAnalysisRulePolicyV1) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IntermediateTableAnalysisRulePolicyV1: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "custom" in value:
        import capo_cleanrooms.types.intermediate_table_analysis_rule_custom

        return {
            "custom": capo_cleanrooms.types.intermediate_table_analysis_rule_custom.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError(
            "IntermediateTableAnalysisRulePolicyV1: no variant present"
        )


def deserialize_json(data: dict) -> IntermediateTableAnalysisRulePolicyV1:
    if data.get("custom") is not None:
        import capo_cleanrooms.types.intermediate_table_analysis_rule_custom

        return {
            "custom": capo_cleanrooms.types.intermediate_table_analysis_rule_custom.deserialize_json(
                data["custom"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "IntermediateTableAnalysisRulePolicyV1: no recognized variant key"
        )
