"""Generated from Smithy shape ``com.amazonaws.entityresolution#ResolutionTechniques``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.provider_properties
    import capo_entityresolution.types.resolution_type
    import capo_entityresolution.types.rule_based_properties
    import capo_entityresolution.types.rule_condition_properties


class ResolutionTechniques(TypedDict, closed=True):
    resolution_type: "capo_entityresolution.types.resolution_type.ResolutionType"
    """<p>The type of matching workflow to create. Specify one of the following types: </p> <ul> <li> <p> <code>RULE_MATCHING</code>: Match records using configurable rule-based criteria </p> </li> <li> <p> <code>ML_MATCHING</code>: Match records using machine learning models </p> </li> <li> <p> <code>PROVIDER</code>: Match records using a third-party matching provider</p> </li> </ul>"""
    rule_based_properties: NotRequired[
        "capo_entityresolution.types.rule_based_properties.RuleBasedProperties"
    ]
    """<p>An object which defines the list of matching rules to run and has a field <code>rules</code>, which is a list of rule objects.</p>"""
    rule_condition_properties: NotRequired[
        "capo_entityresolution.types.rule_condition_properties.RuleConditionProperties"
    ]
    """<p>An object containing the <code>rules</code> for a matching workflow.</p>"""
    enable_real_time_matching: NotRequired["bool"]
    """<p>Specifies whether real-time matching is enabled for the rule-based matching workflow. When you enable real-time matching, you can use the <code>GenerateMatchId</code> operation with the workflow.</p>"""
    provider_properties: NotRequired[
        "capo_entityresolution.types.provider_properties.ProviderProperties"
    ]
    """<p>The properties of the provider service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolutionTechniques) -> dict:
    out: dict = {}
    import capo_entityresolution.types.resolution_type

    out["resolutionType"] = capo_entityresolution.types.resolution_type.serialize_json(
        value["resolution_type"]
    )
    if "rule_based_properties" in value:
        import capo_entityresolution.types.rule_based_properties

        out["ruleBasedProperties"] = (
            capo_entityresolution.types.rule_based_properties.serialize_json(
                value["rule_based_properties"]
            )
        )
    if "rule_condition_properties" in value:
        import capo_entityresolution.types.rule_condition_properties

        out["ruleConditionProperties"] = (
            capo_entityresolution.types.rule_condition_properties.serialize_json(
                value["rule_condition_properties"]
            )
        )
    if "enable_real_time_matching" in value:
        out["enableRealTimeMatching"] = value["enable_real_time_matching"]
    if "provider_properties" in value:
        import capo_entityresolution.types.provider_properties

        out["providerProperties"] = (
            capo_entityresolution.types.provider_properties.serialize_json(
                value["provider_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResolutionTechniques:
    out: ResolutionTechniques = {}  # type: ignore[typeddict-item]
    if data.get("resolutionType") is not None:
        import capo_entityresolution.types.resolution_type

        out["resolution_type"] = (
            capo_entityresolution.types.resolution_type.deserialize_json(
                data["resolutionType"]
            )
        )
    else:
        import typing

        out["resolution_type"] = typing.cast(
            "capo_entityresolution.types.resolution_type.ResolutionType", ""
        )
    if data.get("ruleBasedProperties") is not None:
        import capo_entityresolution.types.rule_based_properties

        out["rule_based_properties"] = (
            capo_entityresolution.types.rule_based_properties.deserialize_json(
                data["ruleBasedProperties"]
            )
        )
    if data.get("ruleConditionProperties") is not None:
        import capo_entityresolution.types.rule_condition_properties

        out["rule_condition_properties"] = (
            capo_entityresolution.types.rule_condition_properties.deserialize_json(
                data["ruleConditionProperties"]
            )
        )
    if data.get("enableRealTimeMatching") is not None:
        out["enable_real_time_matching"] = data["enableRealTimeMatching"]
    if data.get("providerProperties") is not None:
        import capo_entityresolution.types.provider_properties

        out["provider_properties"] = (
            capo_entityresolution.types.provider_properties.deserialize_json(
                data["providerProperties"]
            )
        )
    return out
