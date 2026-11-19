"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.icd10_cm_attribute_list
    import capo_comprehendmedical.types.icd10_cm_concept_list
    import capo_comprehendmedical.types.icd10_cm_entity_category
    import capo_comprehendmedical.types.icd10_cm_entity_type
    import capo_comprehendmedical.types.icd10_cm_trait_list
    import capo_comprehendmedical.types.integer
    import capo_comprehendmedical.types.ontology_linking_bounded_length_string


class ICD10CMEntity(TypedDict, closed=True):
    id: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.</p>"""
    text: NotRequired[
        "capo_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString"
    ]
    """<p>The segment of input text that is matched to the detected entity.</p>"""
    category: NotRequired[
        "capo_comprehendmedical.types.icd10_cm_entity_category.ICD10CMEntityCategory"
    ]
    """<p> The category of the entity. InferICD10CM detects entities in the <code>MEDICAL_CONDITION</code> category. </p>"""
    type: NotRequired[
        "capo_comprehendmedical.types.icd10_cm_entity_type.ICD10CMEntityType"
    ]
    """<p>Describes the specific type of entity with category of entities. InferICD10CM detects entities of the type <code>DX_NAME</code> and <code>TIME_EXPRESSION</code>.</p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has in the accuracy of the detection.</p>"""
    begin_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.</p>"""
    end_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.</p>"""
    attributes: NotRequired[
        "capo_comprehendmedical.types.icd10_cm_attribute_list.ICD10CMAttributeList"
    ]
    """<p>The detected attributes that relate to the entity. An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the nature of a medical condition.</p>"""
    traits: NotRequired[
        "capo_comprehendmedical.types.icd10_cm_trait_list.ICD10CMTraitList"
    ]
    """<p>Provides Contextual information for the entity. The traits recognized by InferICD10CM are <code>DIAGNOSIS</code>, <code>SIGN</code>, <code>SYMPTOM</code>, and <code>NEGATION.</code> </p>"""
    icd10_cm_concepts: NotRequired[
        "capo_comprehendmedical.types.icd10_cm_concept_list.ICD10CMConceptList"
    ]
    """<p>The ICD-10-CM concepts that the entity could refer to, along with a score indicating the likelihood of the match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMEntity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import capo_comprehendmedical.types.icd10_cm_entity_category

        out["Category"] = (
            capo_comprehendmedical.types.icd10_cm_entity_category.serialize_aws_json_1_1(
                value["category"]
            )
        )
    if "type" in value:
        import capo_comprehendmedical.types.icd10_cm_entity_type

        out["Type"] = (
            capo_comprehendmedical.types.icd10_cm_entity_type.serialize_aws_json_1_1(
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
        import capo_comprehendmedical.types.icd10_cm_attribute_list

        out["Attributes"] = (
            capo_comprehendmedical.types.icd10_cm_attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    if "traits" in value:
        import capo_comprehendmedical.types.icd10_cm_trait_list

        out["Traits"] = (
            capo_comprehendmedical.types.icd10_cm_trait_list.serialize_aws_json_1_1(
                value["traits"]
            )
        )
    if "icd10_cm_concepts" in value:
        import capo_comprehendmedical.types.icd10_cm_concept_list

        out["ICD10CMConcepts"] = (
            capo_comprehendmedical.types.icd10_cm_concept_list.serialize_aws_json_1_1(
                value["icd10_cm_concepts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ICD10CMEntity:
    out: ICD10CMEntity = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Category") is not None:
        import capo_comprehendmedical.types.icd10_cm_entity_category

        out["category"] = (
            capo_comprehendmedical.types.icd10_cm_entity_category.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.icd10_cm_entity_type

        out["type"] = (
            capo_comprehendmedical.types.icd10_cm_entity_type.deserialize_aws_json_1_1(
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
        import capo_comprehendmedical.types.icd10_cm_attribute_list

        out["attributes"] = (
            capo_comprehendmedical.types.icd10_cm_attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if data.get("Traits") is not None:
        import capo_comprehendmedical.types.icd10_cm_trait_list

        out["traits"] = (
            capo_comprehendmedical.types.icd10_cm_trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    if data.get("ICD10CMConcepts") is not None:
        import capo_comprehendmedical.types.icd10_cm_concept_list

        out["icd10_cm_concepts"] = (
            capo_comprehendmedical.types.icd10_cm_concept_list.deserialize_aws_json_1_1(
                data["ICD10CMConcepts"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ICD10CMEntity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import capo_comprehendmedical.types.icd10_cm_entity_category

        out["Category"] = (
            capo_comprehendmedical.types.icd10_cm_entity_category.serialize_cbor(
                value["category"]
            )
        )
    if "type" in value:
        import capo_comprehendmedical.types.icd10_cm_entity_type

        out["Type"] = capo_comprehendmedical.types.icd10_cm_entity_type.serialize_cbor(
            value["type"]
        )
    if "score" in value:
        out["Score"] = value["score"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "attributes" in value:
        import capo_comprehendmedical.types.icd10_cm_attribute_list

        out["Attributes"] = (
            capo_comprehendmedical.types.icd10_cm_attribute_list.serialize_cbor(
                value["attributes"]
            )
        )
    if "traits" in value:
        import capo_comprehendmedical.types.icd10_cm_trait_list

        out["Traits"] = capo_comprehendmedical.types.icd10_cm_trait_list.serialize_cbor(
            value["traits"]
        )
    if "icd10_cm_concepts" in value:
        import capo_comprehendmedical.types.icd10_cm_concept_list

        out["ICD10CMConcepts"] = (
            capo_comprehendmedical.types.icd10_cm_concept_list.serialize_cbor(
                value["icd10_cm_concepts"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ICD10CMEntity:
    out: ICD10CMEntity = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Category") is not None:
        import capo_comprehendmedical.types.icd10_cm_entity_category

        out["category"] = (
            capo_comprehendmedical.types.icd10_cm_entity_category.deserialize_cbor(
                data["Category"]
            )
        )
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.icd10_cm_entity_type

        out["type"] = (
            capo_comprehendmedical.types.icd10_cm_entity_type.deserialize_cbor(
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
        import capo_comprehendmedical.types.icd10_cm_attribute_list

        out["attributes"] = (
            capo_comprehendmedical.types.icd10_cm_attribute_list.deserialize_cbor(
                data["Attributes"]
            )
        )
    if data.get("Traits") is not None:
        import capo_comprehendmedical.types.icd10_cm_trait_list

        out["traits"] = (
            capo_comprehendmedical.types.icd10_cm_trait_list.deserialize_cbor(
                data["Traits"]
            )
        )
    if data.get("ICD10CMConcepts") is not None:
        import capo_comprehendmedical.types.icd10_cm_concept_list

        out["icd10_cm_concepts"] = (
            capo_comprehendmedical.types.icd10_cm_concept_list.deserialize_cbor(
                data["ICD10CMConcepts"]
            )
        )
    return out
