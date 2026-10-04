"""Generated from Smithy shape ``com.amazonaws.securityagent#InitiateProviderRegistrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.client_id
    import capo_securityagent.types.client_secret
    import capo_securityagent.types.provider
    import capo_securityagent.types.target_url


class InitiateProviderRegistrationInput(TypedDict, closed=True):
    provider: "capo_securityagent.types.provider.Provider"
    """<p>The provider to initiate registration with.</p>"""
    target_url: NotRequired["capo_securityagent.types.target_url.TargetUrl"]
    """<p>The HTTPS URL of a self-managed provider instance. Omit for SaaS providers.</p>"""
    organization_name: NotRequired["str"]
    """<p>The name of the organization to connect.</p>"""
    client_id: NotRequired["capo_securityagent.types.client_id.ClientId"]
    """<p>The client ID of the OAuth application registered on your self-managed provider instance.</p>"""
    client_secret: NotRequired["capo_securityagent.types.client_secret.ClientSecret"]
    """<p>The client secret of the OAuth application registered on your self-managed provider instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateProviderRegistrationInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.provider

    out["provider"] = capo_securityagent.types.provider.serialize_json(
        value["provider"]
    )
    if "target_url" in value:
        out["targetUrl"] = value["target_url"]
    if "organization_name" in value:
        out["organizationName"] = value["organization_name"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "client_secret" in value:
        out["clientSecret"] = value["client_secret"]
    return out


def deserialize_json(data: dict) -> InitiateProviderRegistrationInput:
    out: InitiateProviderRegistrationInput = {}  # type: ignore[typeddict-item]
    if data.get("provider") is not None:
        import capo_securityagent.types.provider

        out["provider"] = capo_securityagent.types.provider.deserialize_json(
            data["provider"]
        )
    else:
        raise DeserializationError(
            "InitiateProviderRegistrationInput.provider required"
        )
    if data.get("targetUrl") is not None:
        out["target_url"] = data["targetUrl"]
    if data.get("organizationName") is not None:
        out["organization_name"] = data["organizationName"]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    return out
