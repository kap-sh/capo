"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CoverageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.failed_account_list
    import capo_wellarchitected.types.failed_organizational_unit_list
    import capo_wellarchitected.types.pillar_count_list
    import capo_wellarchitected.types.priority_count_list


class CoverageSummary(TypedDict, closed=True):
    total_accounts_in_scope: "int"
    """<p>Total number of accounts that were in scope for the report after applying all filters and AWS Organizations membership validation.</p>"""
    accounts_with_profile: "int"
    """<p>Number of in-scope accounts that had an Agent Profile and were successfully processed.</p>"""
    accounts_without_profile: "int"
    """<p>Number of in-scope accounts that had no Agent Profile at the time of the snapshot.</p>"""
    failed_account_count: "int"
    """<p>Number of in-scope accounts that errored during processing. Equal to the length of failedAccounts.</p>"""
    total_profiles: "int"
    """<p>Total number of Agent Profiles contributing to the report.</p>"""
    total_recommendations: "int"
    """<p>Total number of recommendations included in the report across all profiles and all pillars.</p>"""
    recommendation_count_by_pillar: NotRequired[
        "capo_wellarchitected.types.pillar_count_list.PillarCountList"
    ]
    """<p>Recommendation count grouped by Well-Architected pillar. Each entry pairs a Pillar enum value with a non-negative long. The counts sum to totalRecommendations.</p>"""
    recommendation_count_by_priority: NotRequired[
        "capo_wellarchitected.types.priority_count_list.PriorityCountList"
    ]
    """<p>Recommendation count grouped by Priority. Each entry pairs a Priority enum value with a non-negative long. The counts sum to totalRecommendations.</p>"""
    failed_accounts: NotRequired[
        "capo_wellarchitected.types.failed_account_list.FailedAccountList"
    ]
    """<p>Accounts that errored during processing and the reason they failed.</p>"""
    failed_organizational_units: NotRequired[
        "capo_wellarchitected.types.failed_organizational_unit_list.FailedOrganizationalUnitList"
    ]
    """<p>Organizational units named in the report's filters that could not be expanded into their member accounts, along with the reason each failed. A failed OU means the report is missing whatever accounts it contained. Absent or empty when every requested OU expanded successfully.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageSummary) -> dict:
    out: dict = {}
    out["totalAccountsInScope"] = value["total_accounts_in_scope"]
    out["accountsWithProfile"] = value["accounts_with_profile"]
    out["accountsWithoutProfile"] = value["accounts_without_profile"]
    out["failedAccountCount"] = value["failed_account_count"]
    out["totalProfiles"] = value["total_profiles"]
    out["totalRecommendations"] = value["total_recommendations"]
    if "recommendation_count_by_pillar" in value:
        import capo_wellarchitected.types.pillar_count_list

        out["recommendationCountByPillar"] = (
            capo_wellarchitected.types.pillar_count_list.serialize_json(
                value["recommendation_count_by_pillar"]
            )
        )
    if "recommendation_count_by_priority" in value:
        import capo_wellarchitected.types.priority_count_list

        out["recommendationCountByPriority"] = (
            capo_wellarchitected.types.priority_count_list.serialize_json(
                value["recommendation_count_by_priority"]
            )
        )
    if "failed_accounts" in value:
        import capo_wellarchitected.types.failed_account_list

        out["failedAccounts"] = (
            capo_wellarchitected.types.failed_account_list.serialize_json(
                value["failed_accounts"]
            )
        )
    if "failed_organizational_units" in value:
        import capo_wellarchitected.types.failed_organizational_unit_list

        out["failedOrganizationalUnits"] = (
            capo_wellarchitected.types.failed_organizational_unit_list.serialize_json(
                value["failed_organizational_units"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoverageSummary:
    out: CoverageSummary = {}  # type: ignore[typeddict-item]
    if data.get("totalAccountsInScope") is not None:
        out["total_accounts_in_scope"] = data["totalAccountsInScope"]
    else:
        out["total_accounts_in_scope"] = 0
    if data.get("accountsWithProfile") is not None:
        out["accounts_with_profile"] = data["accountsWithProfile"]
    else:
        out["accounts_with_profile"] = 0
    if data.get("accountsWithoutProfile") is not None:
        out["accounts_without_profile"] = data["accountsWithoutProfile"]
    else:
        out["accounts_without_profile"] = 0
    if data.get("failedAccountCount") is not None:
        out["failed_account_count"] = data["failedAccountCount"]
    else:
        out["failed_account_count"] = 0
    if data.get("totalProfiles") is not None:
        out["total_profiles"] = data["totalProfiles"]
    else:
        out["total_profiles"] = 0
    if data.get("totalRecommendations") is not None:
        out["total_recommendations"] = data["totalRecommendations"]
    else:
        out["total_recommendations"] = 0
    if data.get("recommendationCountByPillar") is not None:
        import capo_wellarchitected.types.pillar_count_list

        out["recommendation_count_by_pillar"] = (
            capo_wellarchitected.types.pillar_count_list.deserialize_json(
                data["recommendationCountByPillar"]
            )
        )
    if data.get("recommendationCountByPriority") is not None:
        import capo_wellarchitected.types.priority_count_list

        out["recommendation_count_by_priority"] = (
            capo_wellarchitected.types.priority_count_list.deserialize_json(
                data["recommendationCountByPriority"]
            )
        )
    if data.get("failedAccounts") is not None:
        import capo_wellarchitected.types.failed_account_list

        out["failed_accounts"] = (
            capo_wellarchitected.types.failed_account_list.deserialize_json(
                data["failedAccounts"]
            )
        )
    if data.get("failedOrganizationalUnits") is not None:
        import capo_wellarchitected.types.failed_organizational_unit_list

        out["failed_organizational_units"] = (
            capo_wellarchitected.types.failed_organizational_unit_list.deserialize_json(
                data["failedOrganizationalUnits"]
            )
        )
    return out
