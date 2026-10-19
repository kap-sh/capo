"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNamedEntity``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.description_sensitive_string
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.named_entity_definitions
    import capo_quicksight.types.named_entity_sort_list
    import capo_quicksight.types.nullable_integer
    import capo_quicksight.types.semantic_entity_type
    import capo_quicksight.types.synonyms


class TopicNamedEntity(TypedDict, closed=True):
    entity_name: "capo_quicksight.types.limited_string.LimitedString"
    """<p>The name of the named entity.</p>"""
    entity_description: NotRequired[
        "capo_quicksight.types.description_sensitive_string.DescriptionSensitiveString"
    ]
    """<p>The description of the named entity.</p>"""
    entity_synonyms: NotRequired["capo_quicksight.types.synonyms.Synonyms"]
    """<p>The other names or aliases for the named entity.</p>"""
    semantic_entity_type: NotRequired[
        "capo_quicksight.types.semantic_entity_type.SemanticEntityType"
    ]
    """<p>The type of named entity that a topic represents.</p>"""
    definition: NotRequired[
        "capo_quicksight.types.named_entity_definitions.NamedEntityDefinitions"
    ]
    """<p>The definition of a named entity.</p>"""
    sort: NotRequired[
        "capo_quicksight.types.named_entity_sort_list.NamedEntitySortList"
    ]
    """<p>The sort configuration of the named entity.</p>"""
    rank_order: NotRequired["capo_quicksight.types.nullable_integer.NullableInteger"]
    """<p>The rank order of the named entity.</p>"""
    presentation_order: NotRequired[
        "capo_quicksight.types.nullable_integer.NullableInteger"
    ]
    """<p>The presentation order of the named entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicNamedEntity) -> dict:
    out: dict = {}
    out["EntityName"] = value["entity_name"]
    if "entity_description" in value:
        out["EntityDescription"] = value["entity_description"]
    if "entity_synonyms" in value:
        import capo_quicksight.types.synonyms

        out["EntitySynonyms"] = capo_quicksight.types.synonyms.serialize_json(
            value["entity_synonyms"]
        )
    if "semantic_entity_type" in value:
        import capo_quicksight.types.semantic_entity_type

        out["SemanticEntityType"] = (
            capo_quicksight.types.semantic_entity_type.serialize_json(
                value["semantic_entity_type"]
            )
        )
    if "definition" in value:
        import capo_quicksight.types.named_entity_definitions

        out["Definition"] = (
            capo_quicksight.types.named_entity_definitions.serialize_json(
                value["definition"]
            )
        )
    if "sort" in value:
        import capo_quicksight.types.named_entity_sort_list

        out["Sort"] = capo_quicksight.types.named_entity_sort_list.serialize_json(
            value["sort"]
        )
    if "rank_order" in value:
        out["RankOrder"] = value["rank_order"]
    if "presentation_order" in value:
        out["PresentationOrder"] = value["presentation_order"]
    return out


def deserialize_json(data: dict) -> TopicNamedEntity:
    out: TopicNamedEntity = {}  # type: ignore[typeddict-item]
    if data.get("EntityName") is not None:
        out["entity_name"] = data["EntityName"]
    else:
        out["entity_name"] = ""
    if data.get("EntityDescription") is not None:
        out["entity_description"] = data["EntityDescription"]
    if data.get("EntitySynonyms") is not None:
        import capo_quicksight.types.synonyms

        out["entity_synonyms"] = capo_quicksight.types.synonyms.deserialize_json(
            data["EntitySynonyms"]
        )
    if data.get("SemanticEntityType") is not None:
        import capo_quicksight.types.semantic_entity_type

        out["semantic_entity_type"] = (
            capo_quicksight.types.semantic_entity_type.deserialize_json(
                data["SemanticEntityType"]
            )
        )
    if data.get("Definition") is not None:
        import capo_quicksight.types.named_entity_definitions

        out["definition"] = (
            capo_quicksight.types.named_entity_definitions.deserialize_json(
                data["Definition"]
            )
        )
    if data.get("Sort") is not None:
        import capo_quicksight.types.named_entity_sort_list

        out["sort"] = capo_quicksight.types.named_entity_sort_list.deserialize_json(
            data["Sort"]
        )
    if data.get("RankOrder") is not None:
        out["rank_order"] = data["RankOrder"]
    if data.get("PresentationOrder") is not None:
        out["presentation_order"] = data["PresentationOrder"]
    return out


def redact_sensitive(value: TopicNamedEntity) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entity_description" in value:
        out["entity_description"] = "*** Sensitive Data Redacted ***"
    if "entity_synonyms" in value:
        import capo_quicksight.types.synonyms

        out["entity_synonyms"] = capo_quicksight.types.synonyms.redact_sensitive(
            value["entity_synonyms"]
        )
    return out
