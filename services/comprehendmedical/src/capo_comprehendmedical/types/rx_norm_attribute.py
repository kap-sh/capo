"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.integer
    import capo_comprehendmedical.types.rx_norm_attribute_type
    import capo_comprehendmedical.types.rx_norm_trait_list
    import capo_comprehendmedical.types.string


class RxNormAttribute(TypedDict, closed=True):
    type: NotRequired[
        "capo_comprehendmedical.types.rx_norm_attribute_type.RxNormAttributeType"
    ]
    """<p>The type of attribute. The types of attributes recognized by InferRxNorm are <code>BRAND_NAME</code> and <code>GENERIC_NAME</code>.</p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.</p>"""
    relationship_score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has that the attribute is accurately linked to an entity.</p>"""
    id: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.</p>"""
    begin_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.</p>"""
    end_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.</p>"""
    text: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p>The segment of input text which corresponds to the detected attribute.</p>"""
    traits: NotRequired[
        "capo_comprehendmedical.types.rx_norm_trait_list.RxNormTraitList"
    ]
    """<p>Contextual information for the attribute. InferRxNorm recognizes the trait <code>NEGATION</code> for attributes, i.e. that the patient is not taking a specific dose or form of a medication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormAttribute) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_comprehendmedical.types.rx_norm_attribute_type

        out["Type"] = (
            capo_comprehendmedical.types.rx_norm_attribute_type.serialize_aws_json_1_1(
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
    if "id" in value:
        out["Id"] = value["id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "text" in value:
        out["Text"] = value["text"]
    if "traits" in value:
        import capo_comprehendmedical.types.rx_norm_trait_list

        out["Traits"] = (
            capo_comprehendmedical.types.rx_norm_trait_list.serialize_aws_json_1_1(
                value["traits"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RxNormAttribute:
    out: RxNormAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.rx_norm_attribute_type

        out["type"] = (
            capo_comprehendmedical.types.rx_norm_attribute_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("RelationshipScore") is not None:
        out["relationship_score"] = float(data["RelationshipScore"])
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Traits") is not None:
        import capo_comprehendmedical.types.rx_norm_trait_list

        out["traits"] = (
            capo_comprehendmedical.types.rx_norm_trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RxNormAttribute) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_comprehendmedical.types.rx_norm_attribute_type

        out["Type"] = (
            capo_comprehendmedical.types.rx_norm_attribute_type.serialize_cbor(
                value["type"]
            )
        )
    if "score" in value:
        out["Score"] = value["score"]
    if "relationship_score" in value:
        out["RelationshipScore"] = value["relationship_score"]
    if "id" in value:
        out["Id"] = value["id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "text" in value:
        out["Text"] = value["text"]
    if "traits" in value:
        import capo_comprehendmedical.types.rx_norm_trait_list

        out["Traits"] = capo_comprehendmedical.types.rx_norm_trait_list.serialize_cbor(
            value["traits"]
        )
    return out


def deserialize_cbor(data: dict) -> RxNormAttribute:
    out: RxNormAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.rx_norm_attribute_type

        out["type"] = (
            capo_comprehendmedical.types.rx_norm_attribute_type.deserialize_cbor(
                data["Type"]
            )
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("RelationshipScore") is not None:
        out["relationship_score"] = float(data["RelationshipScore"])
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Traits") is not None:
        import capo_comprehendmedical.types.rx_norm_trait_list

        out["traits"] = (
            capo_comprehendmedical.types.rx_norm_trait_list.deserialize_cbor(
                data["Traits"]
            )
        )
    return out
