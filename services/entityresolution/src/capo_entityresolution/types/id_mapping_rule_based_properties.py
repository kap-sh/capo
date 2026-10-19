"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingRuleBasedProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.attribute_matching_model
    import capo_entityresolution.types.id_mapping_workflow_rule_definition_type
    import capo_entityresolution.types.record_matching_model
    import capo_entityresolution.types.rule_list


class IdMappingRuleBasedProperties(TypedDict, closed=True):
    rules: NotRequired["capo_entityresolution.types.rule_list.RuleList"]
    """<p> The rules that can be used for ID mapping.</p>"""
    rule_definition_type: "capo_entityresolution.types.id_mapping_workflow_rule_definition_type.IdMappingWorkflowRuleDefinitionType"
    """<p> The set of rules you can use in an ID mapping workflow. The limitations specified for the source or target to define the match rules must be compatible.</p>"""
    attribute_matching_model: (
        "capo_entityresolution.types.attribute_matching_model.AttributeMatchingModel"
    )
    """<p>The comparison type. You can either choose <code>ONE_TO_ONE</code> or <code>MANY_TO_MANY</code> as the <code>attributeMatchingModel</code>. </p> <p>If you choose <code>ONE_TO_ONE</code>, the system can only match attributes if the sub-types are an exact match. For example, for the <code>Email</code> attribute type, the system will only consider it a match if the value of the <code>Email</code> field of Profile A matches the value of the <code>Email</code> field of Profile B.</p> <p>If you choose <code>MANY_TO_MANY</code>, the system can match attributes across the sub-types of an attribute type. For example, if the value of the <code>Email</code> field of Profile A matches the value of the <code>BusinessEmail</code> field of Profile B, the two profiles are matched on the <code>Email</code> attribute type. </p>"""
    record_matching_model: (
        "capo_entityresolution.types.record_matching_model.RecordMatchingModel"
    )
    """<p> The type of matching record that is allowed to be used in an ID mapping workflow. </p> <p>If the value is set to <code>ONE_SOURCE_TO_ONE_TARGET</code>, only one record in the source can be matched to the same record in the target.</p> <p>If the value is set to <code>MANY_SOURCE_TO_ONE_TARGET</code>, multiple records in the source can be matched to one record in the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingRuleBasedProperties) -> dict:
    out: dict = {}
    if "rules" in value:
        import capo_entityresolution.types.rule_list

        out["rules"] = capo_entityresolution.types.rule_list.serialize_json(
            value["rules"]
        )
    import capo_entityresolution.types.id_mapping_workflow_rule_definition_type

    out["ruleDefinitionType"] = (
        capo_entityresolution.types.id_mapping_workflow_rule_definition_type.serialize_json(
            value["rule_definition_type"]
        )
    )
    import capo_entityresolution.types.attribute_matching_model

    out["attributeMatchingModel"] = (
        capo_entityresolution.types.attribute_matching_model.serialize_json(
            value["attribute_matching_model"]
        )
    )
    import capo_entityresolution.types.record_matching_model

    out["recordMatchingModel"] = (
        capo_entityresolution.types.record_matching_model.serialize_json(
            value["record_matching_model"]
        )
    )
    return out


def deserialize_json(data: dict) -> IdMappingRuleBasedProperties:
    out: IdMappingRuleBasedProperties = {}  # type: ignore[typeddict-item]
    if data.get("rules") is not None:
        import capo_entityresolution.types.rule_list

        out["rules"] = capo_entityresolution.types.rule_list.deserialize_json(
            data["rules"]
        )
    if data.get("ruleDefinitionType") is not None:
        import capo_entityresolution.types.id_mapping_workflow_rule_definition_type

        out["rule_definition_type"] = (
            capo_entityresolution.types.id_mapping_workflow_rule_definition_type.deserialize_json(
                data["ruleDefinitionType"]
            )
        )
    else:
        import typing

        out["rule_definition_type"] = typing.cast(
            "capo_entityresolution.types.id_mapping_workflow_rule_definition_type.IdMappingWorkflowRuleDefinitionType",
            "",
        )
    if data.get("attributeMatchingModel") is not None:
        import capo_entityresolution.types.attribute_matching_model

        out["attribute_matching_model"] = (
            capo_entityresolution.types.attribute_matching_model.deserialize_json(
                data["attributeMatchingModel"]
            )
        )
    else:
        import typing

        out["attribute_matching_model"] = typing.cast(
            "capo_entityresolution.types.attribute_matching_model.AttributeMatchingModel",
            "",
        )
    if data.get("recordMatchingModel") is not None:
        import capo_entityresolution.types.record_matching_model

        out["record_matching_model"] = (
            capo_entityresolution.types.record_matching_model.deserialize_json(
                data["recordMatchingModel"]
            )
        )
    else:
        import typing

        out["record_matching_model"] = typing.cast(
            "capo_entityresolution.types.record_matching_model.RecordMatchingModel", ""
        )
    return out
