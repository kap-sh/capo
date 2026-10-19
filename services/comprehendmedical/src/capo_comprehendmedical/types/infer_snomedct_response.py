"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#InferSNOMEDCTResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.characters
    import capo_comprehendmedical.types.snomedct_details
    import capo_comprehendmedical.types.snomedct_entity_list
    import capo_comprehendmedical.types.string


class InferSNOMEDCTResponse(TypedDict, closed=True):
    entities: "capo_comprehendmedical.types.snomedct_entity_list.SNOMEDCTEntityList"
    """<p> The collection of medical concept entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned. </p>"""
    pagination_token: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p> If the result of the request is truncated, the pagination token can be used to fetch the next page of entities. </p>"""
    model_version: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p> The version of the model used to analyze the documents, in the format n.n.n You can use this information to track the model used for a particular batch of documents. </p>"""
    snomedct_details: NotRequired[
        "capo_comprehendmedical.types.snomedct_details.SNOMEDCTDetails"
    ]
    """<p> The details of the SNOMED-CT revision, including the edition, language, and version date. </p>"""
    characters: NotRequired["capo_comprehendmedical.types.characters.Characters"]
    """<p> The number of characters in the input request documentation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferSNOMEDCTResponse) -> dict:
    out: dict = {}
    import capo_comprehendmedical.types.snomedct_entity_list

    out["Entities"] = (
        capo_comprehendmedical.types.snomedct_entity_list.serialize_aws_json_1_1(
            value["entities"]
        )
    )
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "snomedct_details" in value:
        import capo_comprehendmedical.types.snomedct_details

        out["SNOMEDCTDetails"] = (
            capo_comprehendmedical.types.snomedct_details.serialize_aws_json_1_1(
                value["snomedct_details"]
            )
        )
    if "characters" in value:
        import capo_comprehendmedical.types.characters

        out["Characters"] = (
            capo_comprehendmedical.types.characters.serialize_aws_json_1_1(
                value["characters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferSNOMEDCTResponse:
    out: InferSNOMEDCTResponse = {}  # type: ignore[typeddict-item]
    if data.get("Entities") is not None:
        import capo_comprehendmedical.types.snomedct_entity_list

        out["entities"] = (
            capo_comprehendmedical.types.snomedct_entity_list.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    else:
        out["entities"] = []
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("ModelVersion") is not None:
        out["model_version"] = data["ModelVersion"]
    if data.get("SNOMEDCTDetails") is not None:
        import capo_comprehendmedical.types.snomedct_details

        out["snomedct_details"] = (
            capo_comprehendmedical.types.snomedct_details.deserialize_aws_json_1_1(
                data["SNOMEDCTDetails"]
            )
        )
    if data.get("Characters") is not None:
        import capo_comprehendmedical.types.characters

        out["characters"] = (
            capo_comprehendmedical.types.characters.deserialize_aws_json_1_1(
                data["Characters"]
            )
        )
    return out
