"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#RegisterSubscriptionProviderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_license_manager_linux_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager_linux_subscriptions.types.secret_arn
    import capo_license_manager_linux_subscriptions.types.subscription_provider_source
    import capo_license_manager_linux_subscriptions.types.tags


class RegisterSubscriptionProviderRequest(TypedDict, closed=True):
    subscription_provider_source: "capo_license_manager_linux_subscriptions.types.subscription_provider_source.SubscriptionProviderSource"
    """<p>The supported Linux subscription provider to register.</p>"""
    secret_arn: "capo_license_manager_linux_subscriptions.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the secret where you've stored your subscription provider's access token. For RHEL subscriptions managed through the Red Hat Subscription Manager (RHSM), the secret contains your Red Hat Offline token.</p>"""
    tags: NotRequired["capo_license_manager_linux_subscriptions.types.tags.Tags"]
    """<p>The metadata tags to assign to your registered Linux subscription provider resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterSubscriptionProviderRequest) -> dict:
    out: dict = {}
    out["SubscriptionProviderSource"] = value["subscription_provider_source"]
    out["SecretArn"] = value["secret_arn"]
    if "tags" in value:
        import capo_license_manager_linux_subscriptions.types.tags

        out["Tags"] = (
            capo_license_manager_linux_subscriptions.types.tags.serialize_json(
                value["tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisterSubscriptionProviderRequest:
    out: RegisterSubscriptionProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionProviderSource") is not None:
        out["subscription_provider_source"] = data["SubscriptionProviderSource"]
    else:
        raise DeserializationError(
            "RegisterSubscriptionProviderRequest.subscription_provider_source required"
        )
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError(
            "RegisterSubscriptionProviderRequest.secret_arn required"
        )
    if data.get("Tags") is not None:
        import capo_license_manager_linux_subscriptions.types.tags

        out["tags"] = (
            capo_license_manager_linux_subscriptions.types.tags.deserialize_json(
                data["Tags"]
            )
        )
    return out


def redact_sensitive(value: RegisterSubscriptionProviderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
