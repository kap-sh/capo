"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.attribute_list
    import capo_comprehendmedical.types.entity_sub_type
    import capo_comprehendmedical.types.entity_type
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.integer
    import capo_comprehendmedical.types.string
    import capo_comprehendmedical.types.trait_list


class Entity(TypedDict, closed=True):
    id: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p> The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier. </p>"""
    begin_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p> The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string. </p>"""
    end_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p> The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string. </p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has in the accuracy of the detection.</p>"""
    text: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p> The segment of input text extracted as this entity.</p>"""
    category: NotRequired["capo_comprehendmedical.types.entity_type.EntityType"]
    """<p> The category of the entity.</p>"""
    type: NotRequired["capo_comprehendmedical.types.entity_sub_type.EntitySubType"]
    """<p> Describes the specific type of entity with category of entities.</p>"""
    traits: NotRequired["capo_comprehendmedical.types.trait_list.TraitList"]
    """<p>Contextual information for the entity.</p>"""
    attributes: NotRequired["capo_comprehendmedical.types.attribute_list.AttributeList"]
    """<p> The extracted attributes that relate to this entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
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
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import capo_comprehendmedical.types.entity_type

        out["Category"] = (
            capo_comprehendmedical.types.entity_type.serialize_aws_json_1_1(
                value["category"]
            )
        )
    if "type" in value:
        import capo_comprehendmedical.types.entity_sub_type

        out["Type"] = (
            capo_comprehendmedical.types.entity_sub_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "traits" in value:
        import capo_comprehendmedical.types.trait_list

        out["Traits"] = capo_comprehendmedical.types.trait_list.serialize_aws_json_1_1(
            value["traits"]
        )
    if "attributes" in value:
        import capo_comprehendmedical.types.attribute_list

        out["Attributes"] = (
            capo_comprehendmedical.types.attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Category") is not None:
        import capo_comprehendmedical.types.entity_type

        out["category"] = (
            capo_comprehendmedical.types.entity_type.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.entity_sub_type

        out["type"] = (
            capo_comprehendmedical.types.entity_sub_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Traits") is not None:
        import capo_comprehendmedical.types.trait_list

        out["traits"] = (
            capo_comprehendmedical.types.trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    if data.get("Attributes") is not None:
        import capo_comprehendmedical.types.attribute_list

        out["attributes"] = (
            capo_comprehendmedical.types.attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Entity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "score" in value:
        out["Score"] = value["score"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import capo_comprehendmedical.types.entity_type

        out["Category"] = capo_comprehendmedical.types.entity_type.serialize_cbor(
            value["category"]
        )
    if "type" in value:
        import capo_comprehendmedical.types.entity_sub_type

        out["Type"] = capo_comprehendmedical.types.entity_sub_type.serialize_cbor(
            value["type"]
        )
    if "traits" in value:
        import capo_comprehendmedical.types.trait_list

        out["Traits"] = capo_comprehendmedical.types.trait_list.serialize_cbor(
            value["traits"]
        )
    if "attributes" in value:
        import capo_comprehendmedical.types.attribute_list

        out["Attributes"] = capo_comprehendmedical.types.attribute_list.serialize_cbor(
            value["attributes"]
        )
    return out


def deserialize_cbor(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Category") is not None:
        import capo_comprehendmedical.types.entity_type

        out["category"] = capo_comprehendmedical.types.entity_type.deserialize_cbor(
            data["Category"]
        )
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.entity_sub_type

        out["type"] = capo_comprehendmedical.types.entity_sub_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("Traits") is not None:
        import capo_comprehendmedical.types.trait_list

        out["traits"] = capo_comprehendmedical.types.trait_list.deserialize_cbor(
            data["Traits"]
        )
    if data.get("Attributes") is not None:
        import capo_comprehendmedical.types.attribute_list

        out["attributes"] = (
            capo_comprehendmedical.types.attribute_list.deserialize_cbor(
                data["Attributes"]
            )
        )
    return out
