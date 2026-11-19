"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateAgentOrganizationalReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_report_state
    import capo_wellarchitected.types.uuid


class CreateAgentOrganizationalReportResponse(TypedDict, closed=True):
    report_id: "capo_wellarchitected.types.uuid.UUID"
    """<p>Unique identifier assigned to the newly-created report.</p>"""
    state: "capo_wellarchitected.types.organizational_report_state.OrganizationalReportState"
    """<p>Lifecycle state of the report at the moment the create call returned. For a freshly-created report this is typically DISCOVERING.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentOrganizationalReportResponse) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    import capo_wellarchitected.types.organizational_report_state

    out["state"] = (
        capo_wellarchitected.types.organizational_report_state.serialize_json(
            value["state"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateAgentOrganizationalReportResponse:
    out: CreateAgentOrganizationalReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("reportId") is not None:
        out["report_id"] = data["reportId"]
    else:
        out["report_id"] = ""
    if data.get("state") is not None:
        import capo_wellarchitected.types.organizational_report_state

        out["state"] = (
            capo_wellarchitected.types.organizational_report_state.deserialize_json(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_wellarchitected.types.organizational_report_state.OrganizationalReportState",
            "",
        )
    return out
