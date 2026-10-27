"""Generated from Smithy shape ``com.amazonaws.deadline#CreateWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.host_properties_request
    import capo_deadline.types.tags


class CreateWorkerRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm to connect to the worker."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID to connect to the worker."""
    host_properties: NotRequired[
        "capo_deadline.types.host_properties_request.HostPropertiesRequest"
    ]
    """The IP address and host name of the worker."""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """The unique token which the server uses to recognize retries of the same request."""
    tags: NotRequired["capo_deadline.types.tags.Tags"]
    """Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkerRequest) -> dict:
    out: dict = {}
    if "host_properties" in value:
        import capo_deadline.types.host_properties_request

        out["hostProperties"] = (
            capo_deadline.types.host_properties_request.serialize_json(
                value["host_properties"]
            )
        )
    if "tags" in value:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWorkerRequest:
    out: CreateWorkerRequest = {}  # type: ignore[typeddict-item]
    if data.get("hostProperties") is not None:
        import capo_deadline.types.host_properties_request

        out["host_properties"] = (
            capo_deadline.types.host_properties_request.deserialize_json(
                data["hostProperties"]
            )
        )
    if data.get("tags") is not None:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.deserialize_json(data["tags"])
    return out
