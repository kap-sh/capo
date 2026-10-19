"""Generated from Smithy shape ``com.amazonaws.transfer#StartFileTransferResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.transfer_id


class StartFileTransferResponse(TypedDict, closed=True):
    transfer_id: "capo_transfer.types.transfer_id.TransferId"
    """<p>Returns the unique identifier for the file transfer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartFileTransferResponse) -> dict:
    out: dict = {}
    out["TransferId"] = value["transfer_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartFileTransferResponse:
    out: StartFileTransferResponse = {}  # type: ignore[typeddict-item]
    if data.get("TransferId") is not None:
        out["transfer_id"] = data["TransferId"]
    else:
        out["transfer_id"] = ""
    return out
