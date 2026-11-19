"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationalReportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_wellarchitected.types.account_id
    import capo_wellarchitected.types.organizational_report_state
    import capo_wellarchitected.types.report_label
    import capo_wellarchitected.types.uuid


class OrganizationalReportSummary(TypedDict, closed=True):
    report_id: "capo_wellarchitected.types.uuid.UUID"
    """<p>Unique identifier of the Organizational Report assigned by the service at creation time.</p>"""
    owner_account_id: "capo_wellarchitected.types.account_id.AccountId"
    """<p>AWS account ID of the caller that created the report. Only this account or a delegated administrator of the same organization may retrieve or delete the report.</p>"""
    organization_id: "str"
    """<p>Identifier of the AWS Organization the report belongs to. Derived from the caller's authorization context at creation time and not accepted as a client-supplied input.</p>"""
    label: NotRequired["capo_wellarchitected.types.report_label.ReportLabel"]
    """<p>Optional human-readable label supplied by the caller at creation time.</p>"""
    state: "capo_wellarchitected.types.organizational_report_state.OrganizationalReportState"
    """<p>Current lifecycle state of the report.</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp at which the report was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalReportSummary) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    out["ownerAccountId"] = value["owner_account_id"]
    out["organizationId"] = value["organization_id"]
    if "label" in value:
        out["label"] = value["label"]
    import capo_wellarchitected.types.organizational_report_state

    out["state"] = (
        capo_wellarchitected.types.organizational_report_state.serialize_json(
            value["state"]
        )
    )
    import capo_wellarchitected._protocol.serialize

    out["createdAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> OrganizationalReportSummary:
    out: OrganizationalReportSummary = {}  # type: ignore[typeddict-item]
    if data.get("reportId") is not None:
        out["report_id"] = data["reportId"]
    else:
        out["report_id"] = ""
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        out["owner_account_id"] = ""
    if data.get("organizationId") is not None:
        out["organization_id"] = data["organizationId"]
    else:
        out["organization_id"] = ""
    if data.get("label") is not None:
        out["label"] = data["label"]
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
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
