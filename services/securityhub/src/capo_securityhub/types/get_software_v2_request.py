"""Generated from Smithy shape ``com.amazonaws.securityhub#GetSoftwareV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.software_filters
    import capo_securityhub.types.software_scopes
    import capo_securityhub.types.sort_criteria


class GetSoftwareV2Request(TypedDict, closed=True):
    filters: NotRequired["capo_securityhub.types.software_filters.SoftwareFilters"]
    """<p>Filters software packages based on a set of criteria. You can nest composite filters up to three levels deep.</p>"""
    scopes: NotRequired["capo_securityhub.types.software_scopes.SoftwareScopes"]
    """<p>Limits the results to software on resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees software from all accounts across the entire organization. Other accounts see only software on their own resources.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>"""
    sort_criteria: NotRequired["capo_securityhub.types.sort_criteria.SortCriteria"]
    """<p>The software attributes used to sort the list of returned software packages. You can't sort by <code>ResourceCount</code>.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p> <p>A token expires one hour after it's issued. If you change <code>Filters</code> or <code>SortCriteria</code> between calls, the token is no longer valid and the request fails with a <code>ValidationException</code>.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. Valid values are 1–100. The default is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSoftwareV2Request) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_securityhub.types.software_filters

        out["Filters"] = capo_securityhub.types.software_filters.serialize_json(
            value["filters"]
        )
    if "scopes" in value:
        import capo_securityhub.types.software_scopes

        out["Scopes"] = capo_securityhub.types.software_scopes.serialize_json(
            value["scopes"]
        )
    if "sort_criteria" in value:
        import capo_securityhub.types.sort_criteria

        out["SortCriteria"] = capo_securityhub.types.sort_criteria.serialize_json(
            value["sort_criteria"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetSoftwareV2Request:
    out: GetSoftwareV2Request = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_securityhub.types.software_filters

        out["filters"] = capo_securityhub.types.software_filters.deserialize_json(
            data["Filters"]
        )
    if data.get("Scopes") is not None:
        import capo_securityhub.types.software_scopes

        out["scopes"] = capo_securityhub.types.software_scopes.deserialize_json(
            data["Scopes"]
        )
    if data.get("SortCriteria") is not None:
        import capo_securityhub.types.sort_criteria

        out["sort_criteria"] = capo_securityhub.types.sort_criteria.deserialize_json(
            data["SortCriteria"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
