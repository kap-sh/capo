"""Generated from Smithy shape ``com.amazonaws.emrcontainers#GetManagedEndpointSessionCredentialsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.credentials
    import capo_emr_containers.types.date
    import capo_emr_containers.types.resource_id_string


class GetManagedEndpointSessionCredentialsResponse(TypedDict, closed=True):
    id: NotRequired["capo_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The identifier of the session token returned.</p>"""
    credentials: NotRequired["capo_emr_containers.types.credentials.Credentials"]
    """<p>The structure containing the session credentials.</p>"""
    endpoint_credentials: NotRequired[
        "capo_emr_containers.types.credentials.Credentials"
    ]
    """<p>The session credentials that the operation returns.</p>"""
    expires_at: NotRequired["capo_emr_containers.types.date.Date"]
    """<p>The date and time when the session token will expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedEndpointSessionCredentialsResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "credentials" in value:
        import capo_emr_containers.types.credentials

        out["credentials"] = capo_emr_containers.types.credentials.serialize_json(
            value["credentials"]
        )
    if "endpoint_credentials" in value:
        import capo_emr_containers.types.credentials

        out["endpointCredentials"] = (
            capo_emr_containers.types.credentials.serialize_json(
                value["endpoint_credentials"]
            )
        )
    if "expires_at" in value:
        import capo_emr_containers.types.date

        out["expiresAt"] = capo_emr_containers.types.date.serialize_json(
            value["expires_at"]
        )
    return out


def deserialize_json(data: dict) -> GetManagedEndpointSessionCredentialsResponse:
    out: GetManagedEndpointSessionCredentialsResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("credentials") is not None:
        import capo_emr_containers.types.credentials

        out["credentials"] = capo_emr_containers.types.credentials.deserialize_json(
            data["credentials"]
        )
    if data.get("endpointCredentials") is not None:
        import capo_emr_containers.types.credentials

        out["endpoint_credentials"] = (
            capo_emr_containers.types.credentials.deserialize_json(
                data["endpointCredentials"]
            )
        )
    if data.get("expiresAt") is not None:
        import capo_emr_containers.types.date

        out["expires_at"] = capo_emr_containers.types.date.deserialize_json(
            data["expiresAt"]
        )
    return out


def redact_sensitive(
    value: GetManagedEndpointSessionCredentialsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        import capo_emr_containers.types.credentials

        out["credentials"] = capo_emr_containers.types.credentials.redact_sensitive(
            value["credentials"]
        )
    if "endpoint_credentials" in value:
        import capo_emr_containers.types.credentials

        out["endpoint_credentials"] = (
            capo_emr_containers.types.credentials.redact_sensitive(
                value["endpoint_credentials"]
            )
        )
    return out
