"""Generated from Smithy shape ``com.amazonaws.transfer#ListFileTransferResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.connector_id
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.transfer_id


class ListFileTransferResultsRequest(TypedDict, closed=True):
    connector_id: "capo_transfer.types.connector_id.ConnectorId"
    """<p>A unique identifier for a connector. This value should match the value supplied to the corresponding <code>StartFileTransfer</code> call.</p>"""
    transfer_id: "capo_transfer.types.transfer_id.TransferId"
    """<p>A unique identifier for a file transfer. This value should match the value supplied to the corresponding <code>StartFileTransfer</code> call.</p>"""
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>If there are more file details than returned in this call, use this value for a subsequent call to <code>ListFileTransferResults</code> to retrieve them.</p>"""
    max_results: NotRequired["capo_transfer.types.max_results.MaxResults"]
    """<p>The maximum number of files to return in a single page. Note that currently you can specify a maximum of 10 file paths in a single <a href="https://docs.aws.amazon.com/transfer/latest/APIReference/API_StartFileTransfer.html">StartFileTransfer</a> operation. Thus, the maximum number of file transfer results that can be returned in a single page is 10. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFileTransferResultsRequest) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    out["TransferId"] = value["transfer_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFileTransferResultsRequest:
    out: ListFileTransferResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    else:
        raise DeserializationError(
            "ListFileTransferResultsRequest.connector_id required"
        )
    if data.get("TransferId") is not None:
        out["transfer_id"] = data["TransferId"]
    else:
        raise DeserializationError(
            "ListFileTransferResultsRequest.transfer_id required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
