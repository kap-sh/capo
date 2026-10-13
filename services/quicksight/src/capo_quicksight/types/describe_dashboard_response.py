"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeDashboardResponse(TypedDict, closed=True):
    dashboard: NotRequired["capo_quicksight.types.dashboard.Dashboard"]
    """<p>Information about the dashboard.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of this request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardResponse) -> dict:
    out: dict = {}
    if "dashboard" in value:
        import capo_quicksight.types.dashboard

        out["Dashboard"] = capo_quicksight.types.dashboard.serialize_json(
            value["dashboard"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDashboardResponse:
    out: DescribeDashboardResponse = {}  # type: ignore[typeddict-item]
    if data.get("Dashboard") is not None:
        import capo_quicksight.types.dashboard

        out["dashboard"] = capo_quicksight.types.dashboard.deserialize_json(
            data["Dashboard"]
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: DescribeDashboardResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dashboard" in value:
        import capo_quicksight.types.dashboard

        out["dashboard"] = capo_quicksight.types.dashboard.redact_sensitive(
            value["dashboard"]
        )
    return out
