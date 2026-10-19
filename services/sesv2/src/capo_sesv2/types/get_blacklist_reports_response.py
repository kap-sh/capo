"""Generated from Smithy shape ``com.amazonaws.sesv2#GetBlacklistReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.blacklist_report


class GetBlacklistReportsResponse(TypedDict, closed=True):
    blacklist_report: "capo_sesv2.types.blacklist_report.BlacklistReport"
    """<p>An object that contains information about a blacklist that one of your dedicated IP addresses appears on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBlacklistReportsResponse) -> dict:
    out: dict = {}
    import capo_sesv2.types.blacklist_report

    out["BlacklistReport"] = capo_sesv2.types.blacklist_report.serialize_json(
        value["blacklist_report"]
    )
    return out


def deserialize_json(data: dict) -> GetBlacklistReportsResponse:
    out: GetBlacklistReportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("BlacklistReport") is not None:
        import capo_sesv2.types.blacklist_report

        out["blacklist_report"] = capo_sesv2.types.blacklist_report.deserialize_json(
            data["BlacklistReport"]
        )
    else:
        out["blacklist_report"] = {}
    return out
