"""Generated from Smithy shape ``com.amazonaws.securityhub#GetSoftwareResourcesV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.software_filters
    import capo_securityhub.types.software_scopes
    import capo_securityhub.types.sort_criteria


class GetSoftwareResourcesV2Request(TypedDict, closed=True):
    package_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the software package, for example <code>openssl</code>. This value must match the <code>PackageName</code> returned by <code>GetSoftwareV2</code>.</p>"""
    package_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of the software package, for example <code>operating-system</code>, <code>application</code>, or <code>library</code>. This value must match the <code>PackageType</code> returned by <code>GetSoftwareV2</code>.</p>"""
    package_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the software package, for example <code>3.0.8</code>. If you omit this value, the response includes resources that contain any version of the package.</p>"""
    filters: NotRequired["capo_securityhub.types.software_filters.SoftwareFilters"]
    """<p>Filters the returned resources based on a set of criteria. You can nest composite filters up to three levels deep.</p>"""
    scopes: NotRequired["capo_securityhub.types.software_scopes.SoftwareScopes"]
    """<p>Limits the results to resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees resources from all accounts across the entire organization. Other accounts see only their own resources.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>"""
    sort_criteria: NotRequired["capo_securityhub.types.sort_criteria.SortCriteria"]
    """<p>The resource attribute used to sort the list of returned resources, for example <code>Region</code> or <code>ResourceType</code>. You can specify one sort criterion.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p> <p>A token expires one hour after it's issued. If you change the request parameters between calls, the token is no longer valid and the request fails with a <code>ValidationException</code>.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. Valid values are 1–100. The default is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSoftwareResourcesV2Request) -> dict:
    out: dict = {}
    if "package_name" in value:
        out["PackageName"] = value["package_name"]
    if "package_type" in value:
        out["PackageType"] = value["package_type"]
    if "package_version" in value:
        out["PackageVersion"] = value["package_version"]
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


def deserialize_json(data: dict) -> GetSoftwareResourcesV2Request:
    out: GetSoftwareResourcesV2Request = {}  # type: ignore[typeddict-item]
    if data.get("PackageName") is not None:
        out["package_name"] = data["PackageName"]
    if data.get("PackageType") is not None:
        out["package_type"] = data["PackageType"]
    if data.get("PackageVersion") is not None:
        out["package_version"] = data["PackageVersion"]
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
