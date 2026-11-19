"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#Attribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.entity_sub_type
    import capo_comprehendmedical.types.entity_type
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.integer
    import capo_comprehendmedical.types.relationship_type
    import capo_comprehendmedical.types.string
    import capo_comprehendmedical.types.trait_list


class Attribute(TypedDict, closed=True):
    type: NotRequired["capo_comprehendmedical.types.entity_sub_type.EntitySubType"]
    """<p> The type of attribute. </p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p> The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute. </p>"""
    relationship_score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p> The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity. </p>"""
    relationship_type: NotRequired[
        "capo_comprehendmedical.types.relationship_type.RelationshipType"
    ]
    """<p>The type of relationship between the entity and attribute. Type for the relationship is <code>OVERLAP</code>, indicating that the entity occurred at the same time as the <code>Date_Expression</code>. </p>"""
    id: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p> The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier. </p>"""
    begin_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p> The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string. </p>"""
    end_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p> The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.</p>"""
    text: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p> The segment of input text extracted as this attribute.</p>"""
    category: NotRequired["capo_comprehendmedical.types.entity_type.EntityType"]
    """<p> The category of attribute. </p>"""
    traits: NotRequired["capo_comprehendmedical.types.trait_list.TraitList"]
    """<p> Contextual information for this attribute. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attribute) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_comprehendmedical.types.entity_sub_type

        out["Type"] = (
            capo_comprehendmedical.types.entity_sub_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "score" in value:
        out["Score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "relationship_score" in value:
        out["RelationshipScore"] = (
            "NaN"
            if value["relationship_score"] != value["relationship_score"]
            else "Infinity"
            if value["relationship_score"] == float("inf")
            else "-Infinity"
            if value["relationship_score"] == float("-inf")
            else value["relationship_score"]
        )
    if "relationship_type" in value:
        import capo_comprehendmedical.types.relationship_type

        out["RelationshipType"] = (
            capo_comprehendmedical.types.relationship_type.serialize_aws_json_1_1(
                value["relationship_type"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import capo_comprehendmedical.types.entity_type

        out["Category"] = (
            capo_comprehendmedical.types.entity_type.serialize_aws_json_1_1(
                value["category"]
            )
        )
    if "traits" in value:
        import capo_comprehendmedical.types.trait_list

        out["Traits"] = capo_comprehendmedical.types.trait_list.serialize_aws_json_1_1(
            value["traits"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.entity_sub_type

        out["type"] = (
            capo_comprehendmedical.types.entity_sub_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("RelationshipScore") is not None:
        out["relationship_score"] = float(data["RelationshipScore"])
    if data.get("RelationshipType") is not None:
        import capo_comprehendmedical.types.relationship_type

        out["relationship_type"] = (
            capo_comprehendmedical.types.relationship_type.deserialize_aws_json_1_1(
                data["RelationshipType"]
            )
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Category") is not None:
        import capo_comprehendmedical.types.entity_type

        out["category"] = (
            capo_comprehendmedical.types.entity_type.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    if data.get("Traits") is not None:
        import capo_comprehendmedical.types.trait_list

        out["traits"] = (
            capo_comprehendmedical.types.trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Attribute) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_comprehendmedical.types.entity_sub_type

        out["Type"] = capo_comprehendmedical.types.entity_sub_type.serialize_cbor(
            value["type"]
        )
    if "score" in value:
        out["Score"] = value["score"]
    if "relationship_score" in value:
        out["RelationshipScore"] = value["relationship_score"]
    if "relationship_type" in value:
        import capo_comprehendmedical.types.relationship_type

        out["RelationshipType"] = (
            capo_comprehendmedical.types.relationship_type.serialize_cbor(
                value["relationship_type"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import capo_comprehendmedical.types.entity_type

        out["Category"] = capo_comprehendmedical.types.entity_type.serialize_cbor(
            value["category"]
        )
    if "traits" in value:
        import capo_comprehendmedical.types.trait_list

        out["Traits"] = capo_comprehendmedical.types.trait_list.serialize_cbor(
            value["traits"]
        )
    return out


def deserialize_cbor(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.entity_sub_type

        out["type"] = capo_comprehendmedical.types.entity_sub_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("RelationshipScore") is not None:
        out["relationship_score"] = float(data["RelationshipScore"])
    if data.get("RelationshipType") is not None:
        import capo_comprehendmedical.types.relationship_type

        out["relationship_type"] = (
            capo_comprehendmedical.types.relationship_type.deserialize_cbor(
                data["RelationshipType"]
            )
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Category") is not None:
        import capo_comprehendmedical.types.entity_type

        out["category"] = capo_comprehendmedical.types.entity_type.deserialize_cbor(
            data["Category"]
        )
    if data.get("Traits") is not None:
        import capo_comprehendmedical.types.trait_list

        out["traits"] = capo_comprehendmedical.types.trait_list.deserialize_cbor(
            data["Traits"]
        )
    return out
