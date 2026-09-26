"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ListResourceSynchronizationStatusesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.resource_synchronization_status_summary_list


class ListResourceSynchronizationStatusesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_network_security_manager.types.next_token.NextToken"]
    """<p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>"""
    resource_synchronization_statuses: "capo_network_security_manager.types.resource_synchronization_status_summary_list.ResourceSynchronizationStatusSummaryList"
    """<p>The list of resource synchronization statuses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceSynchronizationStatusesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_network_security_manager.types.resource_synchronization_status_summary_list

    out["resourceSynchronizationStatuses"] = (
        capo_network_security_manager.types.resource_synchronization_status_summary_list.serialize_json(
            value["resource_synchronization_statuses"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListResourceSynchronizationStatusesOutput:
    out: ListResourceSynchronizationStatusesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("resourceSynchronizationStatuses") is not None:
        import capo_network_security_manager.types.resource_synchronization_status_summary_list

        out["resource_synchronization_statuses"] = (
            capo_network_security_manager.types.resource_synchronization_status_summary_list.deserialize_json(
                data["resourceSynchronizationStatuses"]
            )
        )
    else:
        raise DeserializationError(
            "ListResourceSynchronizationStatusesOutput.resource_synchronization_statuses required"
        )
    return out
