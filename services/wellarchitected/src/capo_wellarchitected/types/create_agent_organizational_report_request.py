"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateAgentOrganizationalReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_report_filters
    import capo_wellarchitected.types.report_label


class CreateAgentOrganizationalReportRequest(TypedDict, closed=True):
    client_token: NotRequired["str"]
    """<p>A caller-supplied idempotency token. Two create calls sharing the same token within the service's idempotency window return the same reportId.</p>"""
    label: NotRequired["capo_wellarchitected.types.report_label.ReportLabel"]
    """<p>Optional human-readable label (1-500 characters) that helps callers distinguish reports created with the same filters. Carried through list and get responses.</p>"""
    filters: NotRequired[
        "capo_wellarchitected.types.organizational_report_filters.OrganizationalReportFilters"
    ]
    """<p>Optional filters narrowing the report's scope. Absent means the report covers the whole organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentOrganizationalReportRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "label" in value:
        out["label"] = value["label"]
    if "filters" in value:
        import capo_wellarchitected.types.organizational_report_filters

        out["filters"] = (
            capo_wellarchitected.types.organizational_report_filters.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAgentOrganizationalReportRequest:
    out: CreateAgentOrganizationalReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("label") is not None:
        out["label"] = data["label"]
    if data.get("filters") is not None:
        import capo_wellarchitected.types.organizational_report_filters

        out["filters"] = (
            capo_wellarchitected.types.organizational_report_filters.deserialize_json(
                data["filters"]
            )
        )
    return out
