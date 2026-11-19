"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentOrganizationalReportDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class GetAgentOrganizationalReportDataResponse(TypedDict, closed=True):
    download_url: "str"
    """<p>Presigned URL that can be used to download the artifact.</p>"""
    expires_at: "datetime.datetime"
    """<p>Expiration time of downloadUrl.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentOrganizationalReportDataResponse) -> dict:
    out: dict = {}
    out["downloadUrl"] = value["download_url"]
    import capo_wellarchitected._protocol.serialize

    out["expiresAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
        value["expires_at"]
    )
    return out


def deserialize_json(data: dict) -> GetAgentOrganizationalReportDataResponse:
    out: GetAgentOrganizationalReportDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("downloadUrl") is not None:
        out["download_url"] = data["downloadUrl"]
    else:
        out["download_url"] = ""
    if data.get("expiresAt") is not None:
        import datetime

        out["expires_at"] = datetime.datetime.fromisoformat(
            data["expiresAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["expires_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
