"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.integer
    import capo_comprehendmedical.types.ontology_linking_bounded_length_string
    import capo_comprehendmedical.types.rx_norm_attribute_list
    import capo_comprehendmedical.types.rx_norm_concept_list
    import capo_comprehendmedical.types.rx_norm_entity_category
    import capo_comprehendmedical.types.rx_norm_entity_type
    import capo_comprehendmedical.types.rx_norm_trait_list


class RxNormEntity(TypedDict, closed=True):
    id: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.</p>"""
    text: NotRequired[
        "capo_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString"
    ]
    """<p>The segment of input text extracted from which the entity was detected.</p>"""
    category: NotRequired[
        "capo_comprehendmedical.types.rx_norm_entity_category.RxNormEntityCategory"
    ]
    """<p>The category of the entity. The recognized categories are <code>GENERIC</code> or <code>BRAND_NAME</code>.</p>"""
    type: NotRequired[
        "capo_comprehendmedical.types.rx_norm_entity_type.RxNormEntityType"
    ]
    """<p> Describes the specific type of entity. For InferRxNorm, the recognized entity type is <code>MEDICATION</code>.</p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected entity.</p>"""
    begin_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.</p>"""
    end_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.</p>"""
    attributes: NotRequired[
        "capo_comprehendmedical.types.rx_norm_attribute_list.RxNormAttributeList"
    ]
    """<p>The extracted attributes that relate to the entity. The attributes recognized by InferRxNorm are <code>DOSAGE</code>, <code>DURATION</code>, <code>FORM</code>, <code>FREQUENCY</code>, <code>RATE</code>, <code>ROUTE_OR_MODE</code>, and <code>STRENGTH</code>.</p>"""
    traits: NotRequired[
        "capo_comprehendmedical.types.rx_norm_trait_list.RxNormTraitList"
    ]
    """<p>Contextual information for the entity.</p>"""
    rx_norm_concepts: NotRequired[
        "capo_comprehendmedical.types.rx_norm_concept_list.RxNormConceptList"
    ]
    """<p>The RxNorm concepts that the entity could refer to, along with a score indicating the likelihood of the match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormEntity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import capo_comprehendmedical.types.rx_norm_entity_category

        out["Category"] = (
            capo_comprehendmedical.types.rx_norm_entity_category.serialize_aws_json_1_1(
                value["category"]
            )
        )
    if "type" in value:
        import capo_comprehendmedical.types.rx_norm_entity_type

        out["Type"] = (
            capo_comprehendmedical.types.rx_norm_entity_type.serialize_aws_json_1_1(
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
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "attributes" in value:
        import capo_comprehendmedical.types.rx_norm_attribute_list

        out["Attributes"] = (
            capo_comprehendmedical.types.rx_norm_attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    if "traits" in value:
        import capo_comprehendmedical.types.rx_norm_trait_list

        out["Traits"] = (
            capo_comprehendmedical.types.rx_norm_trait_list.serialize_aws_json_1_1(
                value["traits"]
            )
        )
    if "rx_norm_concepts" in value:
        import capo_comprehendmedical.types.rx_norm_concept_list

        out["RxNormConcepts"] = (
            capo_comprehendmedical.types.rx_norm_concept_list.serialize_aws_json_1_1(
                value["rx_norm_concepts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RxNormEntity:
    out: RxNormEntity = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Category") is not None:
        import capo_comprehendmedical.types.rx_norm_entity_category

        out["category"] = (
            capo_comprehendmedical.types.rx_norm_entity_category.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.rx_norm_entity_type

        out["type"] = (
            capo_comprehendmedical.types.rx_norm_entity_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("Attributes") is not None:
        import capo_comprehendmedical.types.rx_norm_attribute_list

        out["attributes"] = (
            capo_comprehendmedical.types.rx_norm_attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if data.get("Traits") is not None:
        import capo_comprehendmedical.types.rx_norm_trait_list

        out["traits"] = (
            capo_comprehendmedical.types.rx_norm_trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    if data.get("RxNormConcepts") is not None:
        import capo_comprehendmedical.types.rx_norm_concept_list

        out["rx_norm_concepts"] = (
            capo_comprehendmedical.types.rx_norm_concept_list.deserialize_aws_json_1_1(
                data["RxNormConcepts"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RxNormEntity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import capo_comprehendmedical.types.rx_norm_entity_category

        out["Category"] = (
            capo_comprehendmedical.types.rx_norm_entity_category.serialize_cbor(
                value["category"]
            )
        )
    if "type" in value:
        import capo_comprehendmedical.types.rx_norm_entity_type

        out["Type"] = capo_comprehendmedical.types.rx_norm_entity_type.serialize_cbor(
            value["type"]
        )
    if "score" in value:
        out["Score"] = value["score"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "attributes" in value:
        import capo_comprehendmedical.types.rx_norm_attribute_list

        out["Attributes"] = (
            capo_comprehendmedical.types.rx_norm_attribute_list.serialize_cbor(
                value["attributes"]
            )
        )
    if "traits" in value:
        import capo_comprehendmedical.types.rx_norm_trait_list

        out["Traits"] = capo_comprehendmedical.types.rx_norm_trait_list.serialize_cbor(
            value["traits"]
        )
    if "rx_norm_concepts" in value:
        import capo_comprehendmedical.types.rx_norm_concept_list

        out["RxNormConcepts"] = (
            capo_comprehendmedical.types.rx_norm_concept_list.serialize_cbor(
                value["rx_norm_concepts"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RxNormEntity:
    out: RxNormEntity = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Category") is not None:
        import capo_comprehendmedical.types.rx_norm_entity_category

        out["category"] = (
            capo_comprehendmedical.types.rx_norm_entity_category.deserialize_cbor(
                data["Category"]
            )
        )
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.rx_norm_entity_type

        out["type"] = capo_comprehendmedical.types.rx_norm_entity_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("Attributes") is not None:
        import capo_comprehendmedical.types.rx_norm_attribute_list

        out["attributes"] = (
            capo_comprehendmedical.types.rx_norm_attribute_list.deserialize_cbor(
                data["Attributes"]
            )
        )
    if data.get("Traits") is not None:
        import capo_comprehendmedical.types.rx_norm_trait_list

        out["traits"] = (
            capo_comprehendmedical.types.rx_norm_trait_list.deserialize_cbor(
                data["Traits"]
            )
        )
    if data.get("RxNormConcepts") is not None:
        import capo_comprehendmedical.types.rx_norm_concept_list

        out["rx_norm_concepts"] = (
            capo_comprehendmedical.types.rx_norm_concept_list.deserialize_cbor(
                data["RxNormConcepts"]
            )
        )
    return out
