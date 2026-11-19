"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.finding_id
    import capo_guardduty.types.investigation_type
    import capo_guardduty.types.query_time_window


class InvestigationScope(TypedDict, closed=True):
    investigation_type: NotRequired[
        "capo_guardduty.types.investigation_type.InvestigationType"
    ]
    """<p>The type of investigation. Possible values:</p> <ul> <li> <p> <code>FINDING</code> – An investigation of a specific GuardDuty finding.</p> </li> <li> <p> <code>ACCOUNT</code> – An investigation of the threat posture of an Amazon Web Services account.</p> </li> <li> <p> <code>ORGANIZATION</code> – An investigation of your organization's threat posture.</p> </li> </ul>"""
    finding_id: NotRequired["capo_guardduty.types.finding_id.FindingId"]
    """<p>The ID of the finding that the investigation analyzed. Set only when <code>InvestigationType</code> is <code>FINDING</code>.</p>"""
    account_id: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that the investigation analyzed. Set only when <code>InvestigationType</code> is <code>ACCOUNT</code>.</p>"""
    admin_account_id: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The ID of the administrator account of the organization that the investigation analyzed. Set only when <code>InvestigationType</code> is <code>ORGANIZATION</code>.</p>"""
    query_time_window: NotRequired[
        "capo_guardduty.types.query_time_window.QueryTimeWindow"
    ]
    """<p>The time window over which the investigation queried data, set only when <code>InvestigationType</code> is <code>ACCOUNT</code> or <code>ORGANIZATION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationScope) -> dict:
    out: dict = {}
    if "investigation_type" in value:
        import capo_guardduty.types.investigation_type

        out["investigationType"] = (
            capo_guardduty.types.investigation_type.serialize_json(
                value["investigation_type"]
            )
        )
    if "finding_id" in value:
        out["findingId"] = value["finding_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "admin_account_id" in value:
        out["adminAccountId"] = value["admin_account_id"]
    if "query_time_window" in value:
        import capo_guardduty.types.query_time_window

        out["queryTimeWindow"] = capo_guardduty.types.query_time_window.serialize_json(
            value["query_time_window"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationScope:
    out: InvestigationScope = {}  # type: ignore[typeddict-item]
    if data.get("investigationType") is not None:
        import capo_guardduty.types.investigation_type

        out["investigation_type"] = (
            capo_guardduty.types.investigation_type.deserialize_json(
                data["investigationType"]
            )
        )
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("adminAccountId") is not None:
        out["admin_account_id"] = data["adminAccountId"]
    if data.get("queryTimeWindow") is not None:
        import capo_guardduty.types.query_time_window

        out["query_time_window"] = (
            capo_guardduty.types.query_time_window.deserialize_json(
                data["queryTimeWindow"]
            )
        )
    return out
