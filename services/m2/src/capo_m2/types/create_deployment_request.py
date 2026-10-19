"""Generated from Smithy shape ``com.amazonaws.m2#CreateDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.client_token
    import capo_m2.types.identifier
    import capo_m2.types.version


class CreateDeploymentRequest(TypedDict, closed=True):
    environment_id: "capo_m2.types.identifier.Identifier"
    """<p>The identifier of the runtime environment where you want to deploy this application.</p>"""
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The application identifier.</p>"""
    application_version: "capo_m2.types.version.Version"
    """<p>The version of the application to deploy.</p>"""
    client_token: NotRequired["capo_m2.types.client_token.ClientToken"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a deployment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    out["applicationVersion"] = value["application_version"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateDeploymentRequest:
    out: CreateDeploymentRequest = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("applicationVersion") is not None:
        out["application_version"] = data["applicationVersion"]
    else:
        out["application_version"] = 0
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
