"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListAuditFindingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.audit_findings
    import capo_application_signals.types.next_token


class ListAuditFindingsOutput(TypedDict, closed=True):
    start_time: NotRequired["datetime.datetime"]
    """<p>The start of the time period that the returned audit findings apply to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code> </p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end of the time period that the returned audit findings apply to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code> </p>"""
    audit_findings: "capo_application_signals.types.audit_findings.AuditFindings"
    """<p>An array of structures, where each structure contains information about one audit finding, including the auditor results, severity, and associated metric and dependency graphs.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get the next set of audit findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditFindingsOutput) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_application_signals.types._prelude.timestamp

        out["StartTime"] = (
            capo_application_signals.types._prelude.timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_application_signals.types._prelude.timestamp

        out["EndTime"] = (
            capo_application_signals.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    import capo_application_signals.types.audit_findings

    out["AuditFindings"] = capo_application_signals.types.audit_findings.serialize_json(
        value["audit_findings"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAuditFindingsOutput:
    out: ListAuditFindingsOutput = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["start_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["end_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    if data.get("AuditFindings") is not None:
        import capo_application_signals.types.audit_findings

        out["audit_findings"] = (
            capo_application_signals.types.audit_findings.deserialize_json(
                data["AuditFindings"]
            )
        )
    else:
        out["audit_findings"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
