"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetPortalServiceProviderMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.saml_metadata


class GetPortalServiceProviderMetadataResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    service_provider_saml_metadata: NotRequired[
        "capo_workspaces_web.types.saml_metadata.SamlMetadata"
    ]
    """<p>The service provider SAML metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortalServiceProviderMetadataResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    if "service_provider_saml_metadata" in value:
        out["serviceProviderSamlMetadata"] = value["service_provider_saml_metadata"]
    return out


def deserialize_json(data: dict) -> GetPortalServiceProviderMetadataResponse:
    out: GetPortalServiceProviderMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        out["portal_arn"] = ""
    if data.get("serviceProviderSamlMetadata") is not None:
        out["service_provider_saml_metadata"] = data["serviceProviderSamlMetadata"]
    return out
