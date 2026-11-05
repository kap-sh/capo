"""Generated from Smithy shape ``com.amazonaws.securityhub#GetSoftwareStatisticsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.max_statistic_results
    import capo_securityhub.types.software_group_by_rules
    import capo_securityhub.types.software_scopes
    import capo_securityhub.types.sort_order


class GetSoftwareStatisticsV2Request(TypedDict, closed=True):
    group_by_rules: NotRequired[
        "capo_securityhub.types.software_group_by_rules.SoftwareGroupByRules"
    ]
    """<p>How software statistics should be aggregated and organized in the response.</p>"""
    scopes: NotRequired["capo_securityhub.types.software_scopes.SoftwareScopes"]
    """<p>Limits the results to software on resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees statistics from all accounts across the entire organization. Other accounts see only statistics for software on their own resources.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>"""
    sort_order: NotRequired["capo_securityhub.types.sort_order.SortOrder"]
    """<p>Sorts aggregated statistics by count. The default is descending, which returns the values with the highest counts first.</p>"""
    max_statistic_results: NotRequired[
        "capo_securityhub.types.max_statistic_results.MaxStatisticResults"
    ]
    """<p>The maximum number of grouping values to return. Valid values are 1–400. The default is 400.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSoftwareStatisticsV2Request) -> dict:
    out: dict = {}
    if "group_by_rules" in value:
        import capo_securityhub.types.software_group_by_rules

        out["GroupByRules"] = (
            capo_securityhub.types.software_group_by_rules.serialize_json(
                value["group_by_rules"]
            )
        )
    if "scopes" in value:
        import capo_securityhub.types.software_scopes

        out["Scopes"] = capo_securityhub.types.software_scopes.serialize_json(
            value["scopes"]
        )
    if "sort_order" in value:
        import capo_securityhub.types.sort_order

        out["SortOrder"] = capo_securityhub.types.sort_order.serialize_json(
            value["sort_order"]
        )
    if "max_statistic_results" in value:
        out["MaxStatisticResults"] = value["max_statistic_results"]
    return out


def deserialize_json(data: dict) -> GetSoftwareStatisticsV2Request:
    out: GetSoftwareStatisticsV2Request = {}  # type: ignore[typeddict-item]
    if data.get("GroupByRules") is not None:
        import capo_securityhub.types.software_group_by_rules

        out["group_by_rules"] = (
            capo_securityhub.types.software_group_by_rules.deserialize_json(
                data["GroupByRules"]
            )
        )
    if data.get("Scopes") is not None:
        import capo_securityhub.types.software_scopes

        out["scopes"] = capo_securityhub.types.software_scopes.deserialize_json(
            data["Scopes"]
        )
    if data.get("SortOrder") is not None:
        import capo_securityhub.types.sort_order

        out["sort_order"] = capo_securityhub.types.sort_order.deserialize_json(
            data["SortOrder"]
        )
    if data.get("MaxStatisticResults") is not None:
        out["max_statistic_results"] = data["MaxStatisticResults"]
    return out
