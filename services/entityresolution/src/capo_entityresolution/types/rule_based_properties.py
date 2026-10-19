"""Generated from Smithy shape ``com.amazonaws.entityresolution#RuleBasedProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.attribute_matching_model
    import capo_entityresolution.types.match_purpose
    import capo_entityresolution.types.rule_list


class RuleBasedProperties(TypedDict, closed=True):
    rules: "capo_entityresolution.types.rule_list.RuleList"
    """<p>A list of <code>Rule</code> objects, each of which have fields <code>RuleName</code> and <code>MatchingKeys</code>.</p>"""
    attribute_matching_model: (
        "capo_entityresolution.types.attribute_matching_model.AttributeMatchingModel"
    )
    """<p>The comparison type. You can choose <code>ONE_TO_ONE</code> or <code>MANY_TO_MANY</code> as the <code>attributeMatchingModel</code>. </p> <p>If you choose <code>ONE_TO_ONE</code>, the system can only match attributes if the sub-types are an exact match. For example, for the <code>Email</code> attribute type, the system will only consider it a match if the value of the <code>Email</code> field of Profile A matches the value of the <code>Email</code> field of Profile B.</p> <p>If you choose <code>MANY_TO_MANY</code>, the system can match attributes across the sub-types of an attribute type. For example, if the value of the <code>Email</code> field of Profile A and the value of <code>BusinessEmail</code> field of Profile B matches, the two profiles are matched on the <code>Email</code> attribute type. </p>"""
    match_purpose: NotRequired["capo_entityresolution.types.match_purpose.MatchPurpose"]
    """<p> An indicator of whether to generate IDs and index the data or not.</p> <p>If you choose <code>IDENTIFIER_GENERATION</code>, the process generates IDs and indexes the data.</p> <p>If you choose <code>INDEXING</code>, the process indexes the data without generating IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleBasedProperties) -> dict:
    out: dict = {}
    import capo_entityresolution.types.rule_list

    out["rules"] = capo_entityresolution.types.rule_list.serialize_json(value["rules"])
    import capo_entityresolution.types.attribute_matching_model

    out["attributeMatchingModel"] = (
        capo_entityresolution.types.attribute_matching_model.serialize_json(
            value["attribute_matching_model"]
        )
    )
    if "match_purpose" in value:
        import capo_entityresolution.types.match_purpose

        out["matchPurpose"] = capo_entityresolution.types.match_purpose.serialize_json(
            value["match_purpose"]
        )
    return out


def deserialize_json(data: dict) -> RuleBasedProperties:
    out: RuleBasedProperties = {}  # type: ignore[typeddict-item]
    if data.get("rules") is not None:
        import capo_entityresolution.types.rule_list

        out["rules"] = capo_entityresolution.types.rule_list.deserialize_json(
            data["rules"]
        )
    else:
        out["rules"] = []
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
    if data.get("matchPurpose") is not None:
        import capo_entityresolution.types.match_purpose

        out["match_purpose"] = (
            capo_entityresolution.types.match_purpose.deserialize_json(
                data["matchPurpose"]
            )
        )
    return out
