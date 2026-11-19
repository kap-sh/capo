"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationalReportFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_report_account_id_list
    import capo_wellarchitected.types.organizational_unit_id_list
    import capo_wellarchitected.types.pillar_list
    import capo_wellarchitected.types.priority_list
    import capo_wellarchitected.types.recommendation_status_list
    import capo_wellarchitected.types.recommendation_type_list
    import capo_wellarchitected.types.time_window


class OrganizationalReportFilters(TypedDict, closed=True):
    account_ids: NotRequired[
        "capo_wellarchitected.types.organizational_report_account_id_list.OrganizationalReportAccountIdList"
    ]
    """<p>AWS account IDs to include in the report. Absent or empty means all accounts in the organization are in scope. Each supplied account is validated against AWS Organizations membership. Accounts that do not belong to the caller's organization are excluded and recorded on the report's coverage summary.</p>"""
    organizational_unit_ids: NotRequired[
        "capo_wellarchitected.types.organizational_unit_id_list.OrganizationalUnitIdList"
    ]
    """<p>AWS Organizational Unit IDs whose member accounts are included in the report. Absent or empty means no OU-based scoping is applied. Account and OU filters combine as a union.</p>"""
    pillars: NotRequired["capo_wellarchitected.types.pillar_list.PillarList"]
    """<p>Well-Architected pillars to include. Absent or empty means all pillars.</p>"""
    recommendation_types: NotRequired[
        "capo_wellarchitected.types.recommendation_type_list.RecommendationTypeList"
    ]
    """<p>Recommendation types (RESOURCE, ARCHITECTURE, APPLICATION) to include. Absent or empty means all types.</p>"""
    statuses: NotRequired[
        "capo_wellarchitected.types.recommendation_status_list.RecommendationStatusList"
    ]
    """<p>Recommendation statuses (ACTIVE, SUPPRESSED, COMPLETED) to include. Absent or empty means all statuses.</p>"""
    priorities: NotRequired["capo_wellarchitected.types.priority_list.PriorityList"]
    """<p>Recommendation priorities (HIGH, MEDIUM, LOW) to include. Absent or empty means all priorities.</p>"""
    created_at_range: NotRequired["capo_wellarchitected.types.time_window.TimeWindow"]
    """<p>Inclusive window on recommendation creation time. Absent means no lower or upper bound on createdAt.</p>"""
    updated_at_range: NotRequired["capo_wellarchitected.types.time_window.TimeWindow"]
    """<p>Inclusive window on recommendation last-updated time. Absent means no lower or upper bound on updatedAt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalReportFilters) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_wellarchitected.types.organizational_report_account_id_list

        out["accountIds"] = (
            capo_wellarchitected.types.organizational_report_account_id_list.serialize_json(
                value["account_ids"]
            )
        )
    if "organizational_unit_ids" in value:
        import capo_wellarchitected.types.organizational_unit_id_list

        out["organizationalUnitIds"] = (
            capo_wellarchitected.types.organizational_unit_id_list.serialize_json(
                value["organizational_unit_ids"]
            )
        )
    if "pillars" in value:
        import capo_wellarchitected.types.pillar_list

        out["pillars"] = capo_wellarchitected.types.pillar_list.serialize_json(
            value["pillars"]
        )
    if "recommendation_types" in value:
        import capo_wellarchitected.types.recommendation_type_list

        out["recommendationTypes"] = (
            capo_wellarchitected.types.recommendation_type_list.serialize_json(
                value["recommendation_types"]
            )
        )
    if "statuses" in value:
        import capo_wellarchitected.types.recommendation_status_list

        out["statuses"] = (
            capo_wellarchitected.types.recommendation_status_list.serialize_json(
                value["statuses"]
            )
        )
    if "priorities" in value:
        import capo_wellarchitected.types.priority_list

        out["priorities"] = capo_wellarchitected.types.priority_list.serialize_json(
            value["priorities"]
        )
    if "created_at_range" in value:
        import capo_wellarchitected.types.time_window

        out["createdAtRange"] = capo_wellarchitected.types.time_window.serialize_json(
            value["created_at_range"]
        )
    if "updated_at_range" in value:
        import capo_wellarchitected.types.time_window

        out["updatedAtRange"] = capo_wellarchitected.types.time_window.serialize_json(
            value["updated_at_range"]
        )
    return out


def deserialize_json(data: dict) -> OrganizationalReportFilters:
    out: OrganizationalReportFilters = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_wellarchitected.types.organizational_report_account_id_list

        out["account_ids"] = (
            capo_wellarchitected.types.organizational_report_account_id_list.deserialize_json(
                data["accountIds"]
            )
        )
    if data.get("organizationalUnitIds") is not None:
        import capo_wellarchitected.types.organizational_unit_id_list

        out["organizational_unit_ids"] = (
            capo_wellarchitected.types.organizational_unit_id_list.deserialize_json(
                data["organizationalUnitIds"]
            )
        )
    if data.get("pillars") is not None:
        import capo_wellarchitected.types.pillar_list

        out["pillars"] = capo_wellarchitected.types.pillar_list.deserialize_json(
            data["pillars"]
        )
    if data.get("recommendationTypes") is not None:
        import capo_wellarchitected.types.recommendation_type_list

        out["recommendation_types"] = (
            capo_wellarchitected.types.recommendation_type_list.deserialize_json(
                data["recommendationTypes"]
            )
        )
    if data.get("statuses") is not None:
        import capo_wellarchitected.types.recommendation_status_list

        out["statuses"] = (
            capo_wellarchitected.types.recommendation_status_list.deserialize_json(
                data["statuses"]
            )
        )
    if data.get("priorities") is not None:
        import capo_wellarchitected.types.priority_list

        out["priorities"] = capo_wellarchitected.types.priority_list.deserialize_json(
            data["priorities"]
        )
    if data.get("createdAtRange") is not None:
        import capo_wellarchitected.types.time_window

        out["created_at_range"] = (
            capo_wellarchitected.types.time_window.deserialize_json(
                data["createdAtRange"]
            )
        )
    if data.get("updatedAtRange") is not None:
        import capo_wellarchitected.types.time_window

        out["updated_at_range"] = (
            capo_wellarchitected.types.time_window.deserialize_json(
                data["updatedAtRange"]
            )
        )
    return out
