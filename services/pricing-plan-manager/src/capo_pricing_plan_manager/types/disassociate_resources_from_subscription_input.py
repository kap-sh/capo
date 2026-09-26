"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#DisassociateResourcesFromSubscriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pricing_plan_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pricing_plan_manager.types.idempotency_token
    import capo_pricing_plan_manager.types.resource_arns
    import capo_pricing_plan_manager.types.subscription_arn


class DisassociateResourcesFromSubscriptionInput(TypedDict, closed=True):
    arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn"
    """<p>The ARN of the subscription to remove resources from.</p>"""
    resource_arns: "capo_pricing_plan_manager.types.resource_arns.ResourceArns"
    """<p>The ARNs of the resources to remove from the subscription. For subscriptions in the CloudFront plan family, you cannot remove the required CloudFront distribution or WAF web ACL.</p>"""
    if_match: "str"
    """<p>The <code>ETag</code> value from a previous <code>GetSubscription</code> or <code>ListSubscriptions</code> response.</p>"""
    client_token: NotRequired[
        "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the request is handled only once.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourcesFromSubscriptionInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_pricing_plan_manager.types.resource_arns

    out["resourceArns"] = capo_pricing_plan_manager.types.resource_arns.serialize_json(
        value["resource_arns"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DisassociateResourcesFromSubscriptionInput:
    out: DisassociateResourcesFromSubscriptionInput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "DisassociateResourcesFromSubscriptionInput.arn required"
        )
    if data.get("resourceArns") is not None:
        import capo_pricing_plan_manager.types.resource_arns

        out["resource_arns"] = (
            capo_pricing_plan_manager.types.resource_arns.deserialize_json(
                data["resourceArns"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateResourcesFromSubscriptionInput.resource_arns required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
