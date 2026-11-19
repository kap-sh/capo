"""Generated from Smithy shape ``com.amazonaws.codepipeline#WebhookAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.webhook_auth_configuration_allowed_ip_range
    import capo_codepipeline.types.webhook_auth_configuration_secret_token


class WebhookAuthConfiguration(TypedDict, closed=True):
    allowed_ip_range: NotRequired[
        "capo_codepipeline.types.webhook_auth_configuration_allowed_ip_range.WebhookAuthConfigurationAllowedIPRange"
    ]
    """<p>The property used to configure acceptance of webhooks in an IP address range. For IP, only the <code>AllowedIPRange</code> property must be set. This property must be set to a valid CIDR range.</p>"""
    secret_token: NotRequired[
        "capo_codepipeline.types.webhook_auth_configuration_secret_token.WebhookAuthConfigurationSecretToken"
    ]
    """<p>The property used to configure GitHub authentication. For GITHUB_HMAC, only the <code>SecretToken</code> property must be set.</p> <important> <p>When creating CodePipeline webhooks, do not use your own credentials or reuse the same secret token across multiple webhooks. For optimal security, generate a unique secret token for each webhook you create. The secret token is an arbitrary string that you provide, which GitHub uses to compute and sign the webhook payloads sent to CodePipeline, for protecting the integrity and authenticity of the webhook payloads. Using your own credentials or reusing the same token across multiple webhooks can lead to security vulnerabilities.</p> </important> <note> <p>If a secret token was provided, it will be redacted in the response.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookAuthConfiguration) -> dict:
    out: dict = {}
    if "allowed_ip_range" in value:
        out["AllowedIPRange"] = value["allowed_ip_range"]
    if "secret_token" in value:
        out["SecretToken"] = value["secret_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WebhookAuthConfiguration:
    out: WebhookAuthConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AllowedIPRange") is not None:
        out["allowed_ip_range"] = data["AllowedIPRange"]
    if data.get("SecretToken") is not None:
        out["secret_token"] = data["SecretToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WebhookAuthConfiguration) -> dict:
    out: dict = {}
    if "allowed_ip_range" in value:
        out["AllowedIPRange"] = value["allowed_ip_range"]
    if "secret_token" in value:
        out["SecretToken"] = value["secret_token"]
    return out


def deserialize_cbor(data: dict) -> WebhookAuthConfiguration:
    out: WebhookAuthConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AllowedIPRange") is not None:
        out["allowed_ip_range"] = data["AllowedIPRange"]
    if data.get("SecretToken") is not None:
        out["secret_token"] = data["SecretToken"]
    return out
