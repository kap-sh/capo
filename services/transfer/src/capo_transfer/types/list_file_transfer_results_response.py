"""Generated from Smithy shape ``com.amazonaws.transfer#ListFileTransferResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.connector_file_transfer_results
    import capo_transfer.types.next_token


class ListFileTransferResultsResponse(TypedDict, closed=True):
    file_transfer_results: "capo_transfer.types.connector_file_transfer_results.ConnectorFileTransferResults"
    """<p>Returns the details for the files transferred in the transfer identified by the <code>TransferId</code> and <code>ConnectorId</code> specified.</p> <ul> <li> <p> <code>FilePath</code>: the filename and path to where the file was sent to or retrieved from.</p> </li> <li> <p> <code>StatusCode</code>: current status for the transfer. The status returned is one of the following values:<code>QUEUED</code>, <code>IN_PROGRESS</code>, <code>COMPLETED</code>, or <code>FAILED</code> </p> </li> <li> <p> <code>FailureCode</code>: for transfers that fail, this parameter contains a code indicating the reason. For example, <code>RETRIEVE_FILE_NOT_FOUND</code> </p> </li> <li> <p> <code>FailureMessage</code>: for transfers that fail, this parameter describes the reason for the failure.</p> </li> </ul>"""
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>Returns a token that you can use to call <code>ListFileTransferResults</code> again and receive additional results, if there are any (against the same <code>TransferId</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFileTransferResultsResponse) -> dict:
    out: dict = {}
    import capo_transfer.types.connector_file_transfer_results

    out["FileTransferResults"] = (
        capo_transfer.types.connector_file_transfer_results.serialize_aws_json_1_1(
            value["file_transfer_results"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFileTransferResultsResponse:
    out: ListFileTransferResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FileTransferResults") is not None:
        import capo_transfer.types.connector_file_transfer_results

        out["file_transfer_results"] = (
            capo_transfer.types.connector_file_transfer_results.deserialize_aws_json_1_1(
                data["FileTransferResults"]
            )
        )
    else:
        out["file_transfer_results"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
