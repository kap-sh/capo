"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentOrganizationalReportDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_report_format
    import capo_wellarchitected.types.uuid


class GetAgentOrganizationalReportDataRequest(TypedDict, closed=True):
    report_id: "capo_wellarchitected.types.uuid.UUID"
    """<p>Identifier of the report whose data is being retrieved.</p>"""
    format: "capo_wellarchitected.types.organizational_report_format.OrganizationalReportFormat"
    """<p>Format of the returned artifact (CSV, JSON, or PARQUET).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentOrganizationalReportDataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentOrganizationalReportDataRequest:
    out: GetAgentOrganizationalReportDataRequest = {}  # type: ignore[typeddict-item]
    return out
