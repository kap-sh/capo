"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#InferRxNormResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.rx_norm_entity_list
    import capo_comprehendmedical.types.string


class InferRxNormResponse(TypedDict, closed=True):
    entities: "capo_comprehendmedical.types.rx_norm_entity_list.RxNormEntityList"
    """<p>The medication entities detected in the text linked to RxNorm concepts. If the action is successful, the service sends back an HTTP 200 response, as well as the entities detected.</p>"""
    pagination_token: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p>If the result of the previous request to <code>InferRxNorm</code> was truncated, include the <code>PaginationToken</code> to fetch the next page of medication entities.</p>"""
    model_version: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p>The version of the model used to analyze the documents, in the format <i>n</i>.<i>n</i>.<i>n</i> You can use this information to track the model used for a particular batch of documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferRxNormResponse) -> dict:
    out: dict = {}
    import capo_comprehendmedical.types.rx_norm_entity_list

    out["Entities"] = (
        capo_comprehendmedical.types.rx_norm_entity_list.serialize_aws_json_1_1(
            value["entities"]
        )
    )
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferRxNormResponse:
    out: InferRxNormResponse = {}  # type: ignore[typeddict-item]
    if data.get("Entities") is not None:
        import capo_comprehendmedical.types.rx_norm_entity_list

        out["entities"] = (
            capo_comprehendmedical.types.rx_norm_entity_list.deserialize_aws_json_1_1(
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
