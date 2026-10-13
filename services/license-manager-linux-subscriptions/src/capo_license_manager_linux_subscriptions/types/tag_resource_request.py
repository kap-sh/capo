"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_license_manager_linux_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager_linux_subscriptions.types.subscription_provider_arn
    import capo_license_manager_linux_subscriptions.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services resource to which to add the specified metadata tags.</p>"""
    tags: "capo_license_manager_linux_subscriptions.types.tags.Tags"
    """<p>The metadata tags to assign to the Amazon Web Services resource. Tags are formatted as key value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_license_manager_linux_subscriptions.types.tags

    out["tags"] = capo_license_manager_linux_subscriptions.types.tags.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_license_manager_linux_subscriptions.types.tags

        out["tags"] = (
            capo_license_manager_linux_subscriptions.types.tags.deserialize_json(
                data["tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
