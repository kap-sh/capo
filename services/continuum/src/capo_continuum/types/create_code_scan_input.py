"""Generated from Smithy shape ``com.amazonaws.continuum#CreateCodeScanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id
    import capo_continuum.types.scan_client_token


class CreateCodeScanInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """Environment to scan."""
    client_token: NotRequired["capo_continuum.types.scan_client_token.ScanClientToken"]
    """An optional token identifying one scan request for this environment. SDKs generate a token when omitted. If a request reaches the service without a token, the service generates one for that request, so each request without a token starts a new scan. To retry a request after a lost response, supply the same token on the same environment; once a request with that token has succeeded, a retry returns the original scan. Concurrent requests with the same token, or a retry after a request that failed partway through, can leave an additional scan, which may end FAILED as superseded. A token is bound to its scan for as long as the service retains the scan's build record, with no shorter expiry. Deleting the environment makes the binding inaccessible: a later request with the token returns ResourceNotFoundException."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeScanInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateCodeScanInput:
    out: CreateCodeScanInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
