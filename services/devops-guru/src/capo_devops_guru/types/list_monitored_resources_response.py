"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListMonitoredResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.monitored_resource_identifiers
    import capo_devops_guru.types.uuid_next_token


class ListMonitoredResourcesResponse(TypedDict, closed=True):
    monitored_resource_identifiers: "capo_devops_guru.types.monitored_resource_identifiers.MonitoredResourceIdentifiers"
    """<p> Information about the resource that is being monitored, including the name of the resource, the type of resource, and whether or not permission is given to DevOps Guru to access that resource. </p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitoredResourcesResponse) -> dict:
    out: dict = {}
    import capo_devops_guru.types.monitored_resource_identifiers

    out["MonitoredResourceIdentifiers"] = (
        capo_devops_guru.types.monitored_resource_identifiers.serialize_json(
            value["monitored_resource_identifiers"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMonitoredResourcesResponse:
    out: ListMonitoredResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("MonitoredResourceIdentifiers") is not None:
        import capo_devops_guru.types.monitored_resource_identifiers

        out["monitored_resource_identifiers"] = (
            capo_devops_guru.types.monitored_resource_identifiers.deserialize_json(
                data["MonitoredResourceIdentifiers"]
            )
        )
    else:
        out["monitored_resource_identifiers"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
