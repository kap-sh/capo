"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorFileTransferResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.failure_code
    import capo_transfer.types.file_path
    import capo_transfer.types.message
    import capo_transfer.types.transfer_table_status


class ConnectorFileTransferResult(TypedDict, closed=True):
    file_path: "capo_transfer.types.file_path.FilePath"
    """<p>The filename and path to where the file was sent to or retrieved from.</p>"""
    status_code: "capo_transfer.types.transfer_table_status.TransferTableStatus"
    """<p>The current status for the transfer.</p>"""
    failure_code: NotRequired["capo_transfer.types.failure_code.FailureCode"]
    """<p>For transfers that fail, this parameter contains a code indicating the reason. For example, <code>RETRIEVE_FILE_NOT_FOUND</code> </p>"""
    failure_message: NotRequired["capo_transfer.types.message.Message"]
    """<p>For transfers that fail, this parameter describes the reason for the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorFileTransferResult) -> dict:
    out: dict = {}
    out["FilePath"] = value["file_path"]
    import capo_transfer.types.transfer_table_status

    out["StatusCode"] = (
        capo_transfer.types.transfer_table_status.serialize_aws_json_1_1(
            value["status_code"]
        )
    )
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorFileTransferResult:
    out: ConnectorFileTransferResult = {}  # type: ignore[typeddict-item]
    if data.get("FilePath") is not None:
        out["file_path"] = data["FilePath"]
    else:
        out["file_path"] = ""
    if data.get("StatusCode") is not None:
        import capo_transfer.types.transfer_table_status

        out["status_code"] = (
            capo_transfer.types.transfer_table_status.deserialize_aws_json_1_1(
                data["StatusCode"]
            )
        )
    else:
        import typing

        out["status_code"] = typing.cast(
            "capo_transfer.types.transfer_table_status.TransferTableStatus", ""
        )
    if data.get("FailureCode") is not None:
        out["failure_code"] = data["FailureCode"]
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    return out
