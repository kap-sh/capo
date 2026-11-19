"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentOrganizationalReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.uuid


class GetAgentOrganizationalReportRequest(TypedDict, closed=True):
    report_id: "capo_wellarchitected.types.uuid.UUID"
    """<p>Identifier of the report to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentOrganizationalReportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentOrganizationalReportRequest:
    out: GetAgentOrganizationalReportRequest = {}  # type: ignore[typeddict-item]
    return out
