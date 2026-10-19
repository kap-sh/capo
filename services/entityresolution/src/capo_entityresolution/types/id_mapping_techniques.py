"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingTechniques``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.id_mapping_rule_based_properties
    import capo_entityresolution.types.id_mapping_type
    import capo_entityresolution.types.provider_properties


class IdMappingTechniques(TypedDict, closed=True):
    id_mapping_type: "capo_entityresolution.types.id_mapping_type.IdMappingType"
    """<p>The type of ID mapping.</p>"""
    rule_based_properties: NotRequired[
        "capo_entityresolution.types.id_mapping_rule_based_properties.IdMappingRuleBasedProperties"
    ]
    """<p> An object which defines any additional configurations required by rule-based matching.</p>"""
    provider_properties: NotRequired[
        "capo_entityresolution.types.provider_properties.ProviderProperties"
    ]
    """<p>An object which defines any additional configurations required by the provider service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTechniques) -> dict:
    out: dict = {}
    import capo_entityresolution.types.id_mapping_type

    out["idMappingType"] = capo_entityresolution.types.id_mapping_type.serialize_json(
        value["id_mapping_type"]
    )
    if "rule_based_properties" in value:
        import capo_entityresolution.types.id_mapping_rule_based_properties

        out["ruleBasedProperties"] = (
            capo_entityresolution.types.id_mapping_rule_based_properties.serialize_json(
                value["rule_based_properties"]
            )
        )
    if "provider_properties" in value:
        import capo_entityresolution.types.provider_properties

        out["providerProperties"] = (
            capo_entityresolution.types.provider_properties.serialize_json(
                value["provider_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> IdMappingTechniques:
    out: IdMappingTechniques = {}  # type: ignore[typeddict-item]
    if data.get("idMappingType") is not None:
        import capo_entityresolution.types.id_mapping_type

        out["id_mapping_type"] = (
            capo_entityresolution.types.id_mapping_type.deserialize_json(
                data["idMappingType"]
            )
        )
    else:
        import typing

        out["id_mapping_type"] = typing.cast(
            "capo_entityresolution.types.id_mapping_type.IdMappingType", ""
        )
    if data.get("ruleBasedProperties") is not None:
        import capo_entityresolution.types.id_mapping_rule_based_properties

        out["rule_based_properties"] = (
            capo_entityresolution.types.id_mapping_rule_based_properties.deserialize_json(
                data["ruleBasedProperties"]
            )
        )
    if data.get("providerProperties") is not None:
        import capo_entityresolution.types.provider_properties

        out["provider_properties"] = (
            capo_entityresolution.types.provider_properties.deserialize_json(
                data["providerProperties"]
            )
        )
    return out
