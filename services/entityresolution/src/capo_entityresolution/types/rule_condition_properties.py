"""Generated from Smithy shape ``com.amazonaws.entityresolution#RuleConditionProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.matching_config
    import capo_entityresolution.types.rule_condition_list


class RuleConditionProperties(TypedDict, closed=True):
    rules: "capo_entityresolution.types.rule_condition_list.RuleConditionList"
    """<p> A list of rule objects, each of which have fields <code>ruleName</code> and <code>condition</code>. </p>"""
    matching_config: NotRequired[
        "capo_entityresolution.types.matching_config.MatchingConfig"
    ]
    """<p>An object that contains configuration settings for the matching process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleConditionProperties) -> dict:
    out: dict = {}
    import capo_entityresolution.types.rule_condition_list

    out["rules"] = capo_entityresolution.types.rule_condition_list.serialize_json(
        value["rules"]
    )
    if "matching_config" in value:
        import capo_entityresolution.types.matching_config

        out["matchingConfig"] = (
            capo_entityresolution.types.matching_config.serialize_json(
                value["matching_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleConditionProperties:
    out: RuleConditionProperties = {}  # type: ignore[typeddict-item]
    if data.get("rules") is not None:
        import capo_entityresolution.types.rule_condition_list

        out["rules"] = capo_entityresolution.types.rule_condition_list.deserialize_json(
            data["rules"]
        )
    else:
        out["rules"] = []
    if data.get("matchingConfig") is not None:
        import capo_entityresolution.types.matching_config

        out["matching_config"] = (
            capo_entityresolution.types.matching_config.deserialize_json(
                data["matchingConfig"]
            )
        )
    return out
