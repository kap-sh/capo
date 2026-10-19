"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressedDestinationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address
    import capo_sesv2.types.suppression_list_reason
    import capo_sesv2.types.timestamp


class SuppressedDestinationSummary(TypedDict, closed=True):
    email_address: "capo_sesv2.types.email_address.EmailAddress"
    """<p>The email address that's on the suppression list for your account or for a specific tenant.</p>"""
    reason: "capo_sesv2.types.suppression_list_reason.SuppressionListReason"
    """<p>The reason that the address was added to the suppression list for your account or for a specific tenant.</p>"""
    last_update_time: "capo_sesv2.types.timestamp.Timestamp"
    """<p>The date and time when the suppressed destination was last updated, shown in Unix time format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressedDestinationSummary) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    import capo_sesv2.types.suppression_list_reason

    out["Reason"] = capo_sesv2.types.suppression_list_reason.serialize_json(
        value["reason"]
    )
    import capo_sesv2.types.timestamp

    out["LastUpdateTime"] = capo_sesv2.types.timestamp.serialize_json(
        value["last_update_time"]
    )
    return out


def deserialize_json(data: dict) -> SuppressedDestinationSummary:
    out: SuppressedDestinationSummary = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    else:
        out["email_address"] = ""
    if data.get("Reason") is not None:
        import capo_sesv2.types.suppression_list_reason

        out["reason"] = capo_sesv2.types.suppression_list_reason.deserialize_json(
            data["Reason"]
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_sesv2.types.suppression_list_reason.SuppressionListReason", ""
        )
    if data.get("LastUpdateTime") is not None:
        import capo_sesv2.types.timestamp

        out["last_update_time"] = capo_sesv2.types.timestamp.deserialize_json(
            data["LastUpdateTime"]
        )
    else:
        import datetime

        out["last_update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
