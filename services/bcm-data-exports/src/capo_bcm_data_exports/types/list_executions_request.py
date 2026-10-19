"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ListExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.arn
    import capo_bcm_data_exports.types.max_results
    import capo_bcm_data_exports.types.next_page_token


class ListExecutionsRequest(TypedDict, closed=True):
    export_arn: "capo_bcm_data_exports.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""
    max_results: NotRequired["capo_bcm_data_exports.types.max_results.MaxResults"]
    """<p>The maximum number of objects that are returned for the request.</p>"""
    next_token: NotRequired["capo_bcm_data_exports.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExecutionsRequest) -> dict:
    out: dict = {}
    out["ExportArn"] = value["export_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExecutionsRequest:
    out: ListExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExportArn") is not None:
        out["export_arn"] = data["ExportArn"]
    else:
        out["export_arn"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
