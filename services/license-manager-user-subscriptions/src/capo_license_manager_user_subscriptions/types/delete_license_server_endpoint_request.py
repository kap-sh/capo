"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#DeleteLicenseServerEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.arn
    import capo_license_manager_user_subscriptions.types.server_type


class DeleteLicenseServerEndpointRequest(TypedDict, closed=True):
    license_server_endpoint_arn: "capo_license_manager_user_subscriptions.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the <code>LicenseServerEndpoint</code> resource to delete.</p>"""
    server_type: "capo_license_manager_user_subscriptions.types.server_type.ServerType"
    """<p>The type of License Server that the delete request refers to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLicenseServerEndpointRequest) -> dict:
    out: dict = {}
    out["LicenseServerEndpointArn"] = value["license_server_endpoint_arn"]
    out["ServerType"] = value["server_type"]
    return out


def deserialize_json(data: dict) -> DeleteLicenseServerEndpointRequest:
    out: DeleteLicenseServerEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseServerEndpointArn") is not None:
        out["license_server_endpoint_arn"] = data["LicenseServerEndpointArn"]
    else:
        out["license_server_endpoint_arn"] = ""
    if data.get("ServerType") is not None:
        out["server_type"] = data["ServerType"]
    else:
        out["server_type"] = ""
    return out
