"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeManagedEndpointResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.endpoint


class DescribeManagedEndpointResponse(TypedDict, closed=True):
    endpoint: NotRequired["capo_emr_containers.types.endpoint.Endpoint"]
    """<p>This output displays information about a managed endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeManagedEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        import capo_emr_containers.types.endpoint

        out["endpoint"] = capo_emr_containers.types.endpoint.serialize_json(
            value["endpoint"]
        )
    return out


def deserialize_json(data: dict) -> DescribeManagedEndpointResponse:
    out: DescribeManagedEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        import capo_emr_containers.types.endpoint

        out["endpoint"] = capo_emr_containers.types.endpoint.deserialize_json(
            data["endpoint"]
        )
    return out


def redact_sensitive(value: DescribeManagedEndpointResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoint" in value:
        import capo_emr_containers.types.endpoint

        out["endpoint"] = capo_emr_containers.types.endpoint.redact_sensitive(
            value["endpoint"]
        )
    return out
