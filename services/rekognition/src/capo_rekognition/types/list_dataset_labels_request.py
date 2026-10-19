"""Generated from Smithy shape ``com.amazonaws.rekognition#ListDatasetLabelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_arn
    import capo_rekognition.types.extended_pagination_token
    import capo_rekognition.types.list_dataset_labels_page_size


class ListDatasetLabelsRequest(TypedDict, closed=True):
    dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset that you want to use. </p>"""
    next_token: NotRequired[
        "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>"""
    max_results: NotRequired[
        "capo_rekognition.types.list_dataset_labels_page_size.ListDatasetLabelsPageSize"
    ]
    """<p>The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetLabelsRequest) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetLabelsRequest:
    out: ListDatasetLabelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        out["dataset_arn"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
