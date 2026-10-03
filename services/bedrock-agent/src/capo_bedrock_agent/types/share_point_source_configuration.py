"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SharePointSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.microsoft365_tenant_id
    import capo_bedrock_agent.types.secret_arn
    import capo_bedrock_agent.types.share_point_auth_type
    import capo_bedrock_agent.types.share_point_domain
    import capo_bedrock_agent.types.share_point_host_type
    import capo_bedrock_agent.types.share_point_site_urls


class SharePointSourceConfiguration(TypedDict, closed=True):
    tenant_id: NotRequired[
        "capo_bedrock_agent.types.microsoft365_tenant_id.Microsoft365TenantId"
    ]
    """<p>The identifier of your Microsoft 365 tenant.</p>"""
    domain: "capo_bedrock_agent.types.share_point_domain.SharePointDomain"
    """<p>The domain of your SharePoint instance or site URL/URLs.</p>"""
    site_urls: "capo_bedrock_agent.types.share_point_site_urls.SharePointSiteUrls"
    """<p>A list of one or more SharePoint site URLs.</p>"""
    host_type: "capo_bedrock_agent.types.share_point_host_type.SharePointHostType"
    """<p>The supported host type, whether online/cloud or server/on-premises.</p>"""
    auth_type: "capo_bedrock_agent.types.share_point_auth_type.SharePointAuthType"
    """<p>The supported authentication type to authenticate and connect to your SharePoint site/sites.</p>"""
    credentials_secret_arn: "capo_bedrock_agent.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name of an Secrets Manager secret that stores your authentication credentials for your SharePoint site/sites. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sharepoint-data-source-connector.html#configuration-sharepoint-connector">SharePoint connection configuration</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharePointSourceConfiguration) -> dict:
    out: dict = {}
    if "tenant_id" in value:
        out["tenantId"] = value["tenant_id"]
    out["domain"] = value["domain"]
    import capo_bedrock_agent.types.share_point_site_urls

    out["siteUrls"] = capo_bedrock_agent.types.share_point_site_urls.serialize_json(
        value["site_urls"]
    )
    import capo_bedrock_agent.types.share_point_host_type

    out["hostType"] = capo_bedrock_agent.types.share_point_host_type.serialize_json(
        value["host_type"]
    )
    import capo_bedrock_agent.types.share_point_auth_type

    out["authType"] = capo_bedrock_agent.types.share_point_auth_type.serialize_json(
        value["auth_type"]
    )
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    return out


def deserialize_json(data: dict) -> SharePointSourceConfiguration:
    out: SharePointSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("tenantId") is not None:
        out["tenant_id"] = data["tenantId"]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("SharePointSourceConfiguration.domain required")
    if data.get("siteUrls") is not None:
        import capo_bedrock_agent.types.share_point_site_urls

        out["site_urls"] = (
            capo_bedrock_agent.types.share_point_site_urls.deserialize_json(
                data["siteUrls"]
            )
        )
    else:
        raise DeserializationError("SharePointSourceConfiguration.site_urls required")
    if data.get("hostType") is not None:
        import capo_bedrock_agent.types.share_point_host_type

        out["host_type"] = (
            capo_bedrock_agent.types.share_point_host_type.deserialize_json(
                data["hostType"]
            )
        )
    else:
        raise DeserializationError("SharePointSourceConfiguration.host_type required")
    if data.get("authType") is not None:
        import capo_bedrock_agent.types.share_point_auth_type

        out["auth_type"] = (
            capo_bedrock_agent.types.share_point_auth_type.deserialize_json(
                data["authType"]
            )
        )
    else:
        raise DeserializationError("SharePointSourceConfiguration.auth_type required")
    if data.get("credentialsSecretArn") is not None:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        raise DeserializationError(
            "SharePointSourceConfiguration.credentials_secret_arn required"
        )
    return out
