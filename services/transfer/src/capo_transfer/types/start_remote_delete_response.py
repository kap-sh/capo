"""Generated from Smithy shape ``com.amazonaws.transfer#StartRemoteDeleteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.delete_id


class StartRemoteDeleteResponse(TypedDict, closed=True):
    delete_id: "capo_transfer.types.delete_id.DeleteId"
    """<p>Returns a unique identifier for the delete operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRemoteDeleteResponse) -> dict:
    out: dict = {}
    out["DeleteId"] = value["delete_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRemoteDeleteResponse:
    out: StartRemoteDeleteResponse = {}  # type: ignore[typeddict-item]
    if data.get("DeleteId") is not None:
        out["delete_id"] = data["DeleteId"]
    else:
        out["delete_id"] = ""
    return out
