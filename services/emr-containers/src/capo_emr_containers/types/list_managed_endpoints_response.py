"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListManagedEndpointsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.endpoints
    import capo_emr_containers.types.next_token


class ListManagedEndpointsResponse(TypedDict, closed=True):
    endpoints: NotRequired["capo_emr_containers.types.endpoints.Endpoints"]
    """<p>The managed endpoints to be listed.</p>"""
    next_token: NotRequired["capo_emr_containers.types.next_token.NextToken"]
    """<p> The token for the next set of endpoints to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import capo_emr_containers.types.endpoints

        out["endpoints"] = capo_emr_containers.types.endpoints.serialize_json(
            value["endpoints"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedEndpointsResponse:
    out: ListManagedEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("endpoints") is not None:
        import capo_emr_containers.types.endpoints

        out["endpoints"] = capo_emr_containers.types.endpoints.deserialize_json(
            data["endpoints"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListManagedEndpointsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoints" in value:
        import capo_emr_containers.types.endpoints

        out["endpoints"] = capo_emr_containers.types.endpoints.redact_sensitive(
            value["endpoints"]
        )
    return out
