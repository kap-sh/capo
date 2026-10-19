"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateIdentityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.subresource_arn


class CreateIdentityProviderResponse(TypedDict, closed=True):
    identity_provider_arn: "capo_workspaces_web.types.subresource_arn.SubresourceARN"
    """<p>The ARN of the identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIdentityProviderResponse) -> dict:
    out: dict = {}
    out["identityProviderArn"] = value["identity_provider_arn"]
    return out


def deserialize_json(data: dict) -> CreateIdentityProviderResponse:
    out: CreateIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("identityProviderArn") is not None:
        out["identity_provider_arn"] = data["identityProviderArn"]
    else:
        out["identity_provider_arn"] = ""
    return out
