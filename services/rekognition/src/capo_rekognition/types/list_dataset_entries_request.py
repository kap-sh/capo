"""Generated from Smithy shape ``com.amazonaws.rekognition#ListDatasetEntriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_arn
    import capo_rekognition.types.dataset_labels
    import capo_rekognition.types.extended_pagination_token
    import capo_rekognition.types.has_errors
    import capo_rekognition.types.is_labeled
    import capo_rekognition.types.list_dataset_entries_page_size
    import capo_rekognition.types.query_string


class ListDatasetEntriesRequest(TypedDict, closed=True):
    dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) for the dataset that you want to use. </p>"""
    contains_labels: NotRequired["capo_rekognition.types.dataset_labels.DatasetLabels"]
    """<p>Specifies a label filter for the response. The response includes an entry only if one or more of the labels in <code>ContainsLabels</code> exist in the entry. </p>"""
    labeled: NotRequired["capo_rekognition.types.is_labeled.IsLabeled"]
    """<p> Specify <code>true</code> to get only the JSON Lines where the image is labeled. Specify <code>false</code> to get only the JSON Lines where the image isn't labeled. If you don't specify <code>Labeled</code>, <code>ListDatasetEntries</code> returns JSON Lines for labeled and unlabeled images. </p>"""
    source_ref_contains: NotRequired["capo_rekognition.types.query_string.QueryString"]
    """<p>If specified, <code>ListDatasetEntries</code> only returns JSON Lines where the value of <code>SourceRefContains</code> is part of the <code>source-ref</code> field. The <code>source-ref</code> field contains the Amazon S3 location of the image. You can use <code>SouceRefContains</code> for tasks such as getting the JSON Line for a single image, or gettting JSON Lines for all images within a specific folder.</p>"""
    has_errors: NotRequired["capo_rekognition.types.has_errors.HasErrors"]
    """<p>Specifies an error filter for the response. Specify <code>True</code> to only include entries that have errors. </p>"""
    next_token: NotRequired[
        "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>"""
    max_results: NotRequired[
        "capo_rekognition.types.list_dataset_entries_page_size.ListDatasetEntriesPageSize"
    ]
    """<p>The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetEntriesRequest) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    if "contains_labels" in value:
        import capo_rekognition.types.dataset_labels

        out["ContainsLabels"] = (
            capo_rekognition.types.dataset_labels.serialize_aws_json_1_1(
                value["contains_labels"]
            )
        )
    if "labeled" in value:
        out["Labeled"] = value["labeled"]
    if "source_ref_contains" in value:
        out["SourceRefContains"] = value["source_ref_contains"]
    if "has_errors" in value:
        out["HasErrors"] = value["has_errors"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetEntriesRequest:
    out: ListDatasetEntriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        out["dataset_arn"] = ""
    if data.get("ContainsLabels") is not None:
        import capo_rekognition.types.dataset_labels

        out["contains_labels"] = (
            capo_rekognition.types.dataset_labels.deserialize_aws_json_1_1(
                data["ContainsLabels"]
            )
        )
    if data.get("Labeled") is not None:
        out["labeled"] = data["Labeled"]
    if data.get("SourceRefContains") is not None:
        out["source_ref_contains"] = data["SourceRefContains"]
    if data.get("HasErrors") is not None:
        out["has_errors"] = data["HasErrors"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
