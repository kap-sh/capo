"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListInstanceTypesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.instance_configuration_filter
    import capo_workspaces_instances.types.list_instance_types_max_results
    import capo_workspaces_instances.types.next_token


class ListInstanceTypesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_workspaces_instances.types.list_instance_types_max_results.ListInstanceTypesMaxResults"
    ]
    """<p>Maximum number of instance types to return in a single API call. Enables pagination of instance type results.</p>"""
    next_token: NotRequired["capo_workspaces_instances.types.next_token.NextToken"]
    """<p>Pagination token for retrieving subsequent pages of instance type results.</p>"""
    instance_configuration_filter: NotRequired[
        "capo_workspaces_instances.types.instance_configuration_filter.InstanceConfigurationFilter"
    ]
    """<p>Optional filter to narrow instance type results based on configuration requirements. Only returns instance types that support the specified combination of tenancy, platform type, and billing mode.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInstanceTypesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "instance_configuration_filter" in value:
        import capo_workspaces_instances.types.instance_configuration_filter

        out["InstanceConfigurationFilter"] = (
            capo_workspaces_instances.types.instance_configuration_filter.serialize_aws_json_1_0(
                value["instance_configuration_filter"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInstanceTypesRequest:
    out: ListInstanceTypesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("InstanceConfigurationFilter") is not None:
        import capo_workspaces_instances.types.instance_configuration_filter

        out["instance_configuration_filter"] = (
            capo_workspaces_instances.types.instance_configuration_filter.deserialize_aws_json_1_0(
                data["InstanceConfigurationFilter"]
            )
        )
    return out


def redact_sensitive(value: ListInstanceTypesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
