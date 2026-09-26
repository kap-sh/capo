"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#CreateSubscriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pricing_plan_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pricing_plan_manager.types.approval_mode
    import capo_pricing_plan_manager.types.idempotency_token
    import capo_pricing_plan_manager.types.resource_arns


class CreateSubscriptionInput(TypedDict, closed=True):
    plan_family: "str"
    """<p>The pricing plan family to subscribe to, such as <code>CloudFront</code>.</p>"""
    plan_tier: "str"
    """<p>The tier level for the subscription, such as <code>FREE</code>, <code>PRO</code>, <code>BUSINESS</code>, or <code>PREMIUM</code>.</p>"""
    usage_level: NotRequired["str"]
    """<p>The usage level within the plan tier. Specify <code>DEFAULT</code> for the base configuration, or a higher level if your plan tier supports it.</p>"""
    resource_arns: "capo_pricing_plan_manager.types.resource_arns.ResourceArns"
    """<p>The ARNs of the resources to include in the subscription. Specify one or more supported resources.</p> <note> <p>For subscriptions in the CloudFront plan family, the resources must include exactly one Amazon CloudFront distribution and exactly one WAF web ACL. You can also include other supported resources, such as Amazon Route 53 hosted zones and CloudFront KeyValueStores.</p> </note>"""
    approval_mode: NotRequired[
        "capo_pricing_plan_manager.types.approval_mode.ApprovalMode"
    ]
    """<p>Determines whether the subscription requires explicit approval before billing starts. Set to <code>MANUAL</code> to require a separate <code>ApprovePaidSubscription</code> call, or <code>IMMEDIATE</code> to activate the subscription right away. For paid tier plans, this defaults to <code>MANUAL</code> if not specified. For the <code>FREE</code> plan tier, only <code>IMMEDIATE</code> is supported, and it is the default.</p>"""
    client_token: NotRequired[
        "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the request is handled only once. If you send the same request with the same client token, the API returns the original response without creating a duplicate subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionInput) -> dict:
    out: dict = {}
    out["planFamily"] = value["plan_family"]
    out["planTier"] = value["plan_tier"]
    if "usage_level" in value:
        out["usageLevel"] = value["usage_level"]
    import capo_pricing_plan_manager.types.resource_arns

    out["resourceArns"] = capo_pricing_plan_manager.types.resource_arns.serialize_json(
        value["resource_arns"]
    )
    if "approval_mode" in value:
        import capo_pricing_plan_manager.types.approval_mode

        out["approvalMode"] = (
            capo_pricing_plan_manager.types.approval_mode.serialize_json(
                value["approval_mode"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateSubscriptionInput:
    out: CreateSubscriptionInput = {}  # type: ignore[typeddict-item]
    if data.get("planFamily") is not None:
        out["plan_family"] = data["planFamily"]
    else:
        raise DeserializationError("CreateSubscriptionInput.plan_family required")
    if data.get("planTier") is not None:
        out["plan_tier"] = data["planTier"]
    else:
        raise DeserializationError("CreateSubscriptionInput.plan_tier required")
    if data.get("usageLevel") is not None:
        out["usage_level"] = data["usageLevel"]
    if data.get("resourceArns") is not None:
        import capo_pricing_plan_manager.types.resource_arns

        out["resource_arns"] = (
            capo_pricing_plan_manager.types.resource_arns.deserialize_json(
                data["resourceArns"]
            )
        )
    else:
        raise DeserializationError("CreateSubscriptionInput.resource_arns required")
    if data.get("approvalMode") is not None:
        import capo_pricing_plan_manager.types.approval_mode

        out["approval_mode"] = (
            capo_pricing_plan_manager.types.approval_mode.deserialize_json(
                data["approvalMode"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
