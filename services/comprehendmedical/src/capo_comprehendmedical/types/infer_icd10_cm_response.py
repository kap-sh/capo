"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#InferICD10CMResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.icd10_cm_entity_list
    import capo_comprehendmedical.types.string


class InferICD10CMResponse(TypedDict, closed=True):
    entities: "capo_comprehendmedical.types.icd10_cm_entity_list.ICD10CMEntityList"
    """<p>The medical conditions detected in the text linked to ICD-10-CM concepts. If the action is successful, the service sends back an HTTP 200 response, as well as the entities detected.</p>"""
    pagination_token: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p>If the result of the previous request to <code>InferICD10CM</code> was truncated, include the <code>PaginationToken</code> to fetch the next page of medical condition entities. </p>"""
    model_version: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p>The version of the model used to analyze the documents, in the format <i>n</i>.<i>n</i>.<i>n</i> You can use this information to track the model used for a particular batch of documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferICD10CMResponse) -> dict:
    out: dict = {}
    import capo_comprehendmedical.types.icd10_cm_entity_list

    out["Entities"] = (
        capo_comprehendmedical.types.icd10_cm_entity_list.serialize_aws_json_1_1(
            value["entities"]
        )
    )
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferICD10CMResponse:
    out: InferICD10CMResponse = {}  # type: ignore[typeddict-item]
    if data.get("Entities") is not None:
        import capo_comprehendmedical.types.icd10_cm_entity_list

        out["entities"] = (
            capo_comprehendmedical.types.icd10_cm_entity_list.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    else:
        out["entities"] = []
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("ModelVersion") is not None:
        out["model_version"] = data["ModelVersion"]
    return out
