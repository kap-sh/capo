"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAnalysisRulePolicyV1``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_aggregation
    import capo_cleanrooms.types.analysis_rule_custom
    import capo_cleanrooms.types.analysis_rule_list


class _ConfiguredTableAnalysisRulePolicyV1_list(TypedDict, closed=True):
    list: "capo_cleanrooms.types.analysis_rule_list.AnalysisRuleList"


class _ConfiguredTableAnalysisRulePolicyV1_aggregation(TypedDict, closed=True):
    aggregation: (
        "capo_cleanrooms.types.analysis_rule_aggregation.AnalysisRuleAggregation"
    )


class _ConfiguredTableAnalysisRulePolicyV1_custom(TypedDict, closed=True):
    custom: "capo_cleanrooms.types.analysis_rule_custom.AnalysisRuleCustom"


ConfiguredTableAnalysisRulePolicyV1: TypeAlias = (
    _ConfiguredTableAnalysisRulePolicyV1_list
    | _ConfiguredTableAnalysisRulePolicyV1_aggregation
    | _ConfiguredTableAnalysisRulePolicyV1_custom
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAnalysisRulePolicyV1) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConfiguredTableAnalysisRulePolicyV1: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "list" in value:
        import capo_cleanrooms.types.analysis_rule_list

        return {
            "list": capo_cleanrooms.types.analysis_rule_list.serialize_json(
                value["list"]
            )
        }
    elif "aggregation" in value:
        import capo_cleanrooms.types.analysis_rule_aggregation

        return {
            "aggregation": capo_cleanrooms.types.analysis_rule_aggregation.serialize_json(
                value["aggregation"]
            )
        }
    elif "custom" in value:
        import capo_cleanrooms.types.analysis_rule_custom

        return {
            "custom": capo_cleanrooms.types.analysis_rule_custom.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError(
            "ConfiguredTableAnalysisRulePolicyV1: no variant present"
        )


def deserialize_json(data: dict) -> ConfiguredTableAnalysisRulePolicyV1:
    if data.get("list") is not None:
        import capo_cleanrooms.types.analysis_rule_list

        return {
            "list": capo_cleanrooms.types.analysis_rule_list.deserialize_json(
                data["list"]
            )
        }
    elif data.get("aggregation") is not None:
        import capo_cleanrooms.types.analysis_rule_aggregation

        return {
            "aggregation": capo_cleanrooms.types.analysis_rule_aggregation.deserialize_json(
                data["aggregation"]
            )
        }
    elif data.get("custom") is not None:
        import capo_cleanrooms.types.analysis_rule_custom

        return {
            "custom": capo_cleanrooms.types.analysis_rule_custom.deserialize_json(
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
            "ConfiguredTableAnalysisRulePolicyV1: no recognized variant key"
        )
