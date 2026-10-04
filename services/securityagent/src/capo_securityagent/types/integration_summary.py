"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.private_connection_name
    import capo_securityagent.types.provider
    import capo_securityagent.types.provider_type
    import capo_securityagent.types.target_url


class IntegrationSummary(TypedDict, closed=True):
    integration_id: "str"
    """<p>The unique identifier of the integration.</p>"""
    installation_id: "str"
    """<p>The installation identifier from the integration provider.</p>"""
    provider: "capo_securityagent.types.provider.Provider"
    """<p>The integration provider.</p>"""
    provider_type: "capo_securityagent.types.provider_type.ProviderType"
    """<p>The type of the integration provider.</p>"""
    display_name: "str"
    """<p>The display name of the integration.</p>"""
    target_url: NotRequired["capo_securityagent.types.target_url.TargetUrl"]
    """<p>The HTTPS URL of the customer self-hosted instance, such as a GitHub Enterprise Server or self-managed GitLab instance. This value is absent for SaaS integrations.</p>"""
    webhook_url: NotRequired["str"]
    """<p>The payload URL of the integration's webhook, once it has been created. The signing secret is never returned on a read.</p>"""
    private_connection_name: NotRequired[
        "capo_securityagent.types.private_connection_name.PrivateConnectionName"
    ]
    """<p>The name of the private connection used to reach the integration's self-hosted instance over private networking, if one is configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummary) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["installationId"] = value["installation_id"]
    import capo_securityagent.types.provider

    out["provider"] = capo_securityagent.types.provider.serialize_json(
        value["provider"]
    )
    import capo_securityagent.types.provider_type

    out["providerType"] = capo_securityagent.types.provider_type.serialize_json(
        value["provider_type"]
    )
    out["displayName"] = value["display_name"]
    if "target_url" in value:
        out["targetUrl"] = value["target_url"]
    if "webhook_url" in value:
        out["webhookUrl"] = value["webhook_url"]
    if "private_connection_name" in value:
        out["privateConnectionName"] = value["private_connection_name"]
    return out


def deserialize_json(data: dict) -> IntegrationSummary:
    out: IntegrationSummary = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("IntegrationSummary.integration_id required")
    if data.get("installationId") is not None:
        out["installation_id"] = data["installationId"]
    else:
        raise DeserializationError("IntegrationSummary.installation_id required")
    if data.get("provider") is not None:
        import capo_securityagent.types.provider

        out["provider"] = capo_securityagent.types.provider.deserialize_json(
            data["provider"]
        )
    else:
        raise DeserializationError("IntegrationSummary.provider required")
    if data.get("providerType") is not None:
        import capo_securityagent.types.provider_type

        out["provider_type"] = capo_securityagent.types.provider_type.deserialize_json(
            data["providerType"]
        )
    else:
        raise DeserializationError("IntegrationSummary.provider_type required")
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("IntegrationSummary.display_name required")
    if data.get("targetUrl") is not None:
        out["target_url"] = data["targetUrl"]
    if data.get("webhookUrl") is not None:
        out["webhook_url"] = data["webhookUrl"]
    if data.get("privateConnectionName") is not None:
        out["private_connection_name"] = data["privateConnectionName"]
    return out
