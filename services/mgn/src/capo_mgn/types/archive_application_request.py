"""Generated from Smithy shape ``com.amazonaws.mgn#ArchiveApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.application_id


class ArchiveApplicationRequest(TypedDict, closed=True):
    application_id: "capo_mgn.types.application_id.ApplicationID"
    """<p>Application ID.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveApplicationRequest) -> dict:
    out: dict = {}
    out["applicationID"] = value["application_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ArchiveApplicationRequest:
    out: ArchiveApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("applicationID") is not None:
        out["application_id"] = data["applicationID"]
    else:
        out["application_id"] = ""
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
