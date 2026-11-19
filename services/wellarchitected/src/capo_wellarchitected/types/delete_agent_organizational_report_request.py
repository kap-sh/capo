"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteAgentOrganizationalReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.uuid


class DeleteAgentOrganizationalReportRequest(TypedDict, closed=True):
    report_id: "capo_wellarchitected.types.uuid.UUID"
    """<p>Identifier of the report to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentOrganizationalReportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentOrganizationalReportRequest:
    out: DeleteAgentOrganizationalReportRequest = {}  # type: ignore[typeddict-item]
    return out
