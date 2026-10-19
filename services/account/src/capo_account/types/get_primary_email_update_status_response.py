"""Generated from Smithy shape ``com.amazonaws.account#GetPrimaryEmailUpdateStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_account.types.primary_email_update_status


class GetPrimaryEmailUpdateStatusResponse(TypedDict, closed=True):
    status: "capo_account.types.primary_email_update_status.PrimaryEmailUpdateStatus"
    """<p>The status of the most recent primary email update request.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the most recent primary email update status was last changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPrimaryEmailUpdateStatusResponse) -> dict:
    out: dict = {}
    out["Status"] = value["status"]
    if "updated_at" in value:
        import capo_account.types._prelude.timestamp

        out["UpdatedAt"] = capo_account.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetPrimaryEmailUpdateStatusResponse:
    out: GetPrimaryEmailUpdateStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("UpdatedAt") is not None:
        import capo_account.types._prelude.timestamp

        out["updated_at"] = capo_account.types._prelude.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
