"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.member_account_rankings
    import capo_guardduty.types.string


class AccountOverview(TypedDict, closed=True):
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    account_status: NotRequired["capo_guardduty.types.string.String"]
    """<p>The status of the account.</p>"""
    detector_id: NotRequired["capo_guardduty.types.detector_id.DetectorId"]
    """<p>The ID of the detector of the account.</p>"""
    region: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services Region of the detector.</p>"""
    delegated_admin_account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The account ID of the GuardDuty delegated administrator account.</p>"""
    total_member_accounts: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The total number of member accounts.</p>"""
    total_findings: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The total number of findings.</p>"""
    affected_account_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of accounts that have findings.</p>"""
    account_rankings: NotRequired[
        "capo_guardduty.types.member_account_rankings.MemberAccountRankings"
    ]
    """<p>A ranking of member accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountOverview) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "account_status" in value:
        out["accountStatus"] = value["account_status"]
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "delegated_admin_account_id" in value:
        out["delegatedAdminAccountId"] = value["delegated_admin_account_id"]
    if "total_member_accounts" in value:
        out["totalMemberAccounts"] = value["total_member_accounts"]
    if "total_findings" in value:
        out["totalFindings"] = value["total_findings"]
    if "affected_account_count" in value:
        out["affectedAccountCount"] = value["affected_account_count"]
    if "account_rankings" in value:
        import capo_guardduty.types.member_account_rankings

        out["accountRankings"] = (
            capo_guardduty.types.member_account_rankings.serialize_json(
                value["account_rankings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountOverview:
    out: AccountOverview = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("accountStatus") is not None:
        out["account_status"] = data["accountStatus"]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("delegatedAdminAccountId") is not None:
        out["delegated_admin_account_id"] = data["delegatedAdminAccountId"]
    if data.get("totalMemberAccounts") is not None:
        out["total_member_accounts"] = data["totalMemberAccounts"]
    if data.get("totalFindings") is not None:
        out["total_findings"] = data["totalFindings"]
    if data.get("affectedAccountCount") is not None:
        out["affected_account_count"] = data["affectedAccountCount"]
    if data.get("accountRankings") is not None:
        import capo_guardduty.types.member_account_rankings

        out["account_rankings"] = (
            capo_guardduty.types.member_account_rankings.deserialize_json(
                data["accountRankings"]
            )
        )
    return out
