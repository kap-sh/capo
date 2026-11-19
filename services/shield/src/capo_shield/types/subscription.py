"""Generated from Smithy shape ``com.amazonaws.shield#Subscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_shield.errors import DeserializationError

if TYPE_CHECKING:
    import capo_shield.types.auto_renew
    import capo_shield.types.duration_in_seconds
    import capo_shield.types.limits
    import capo_shield.types.proactive_engagement_status
    import capo_shield.types.resource_arn
    import capo_shield.types.subscription_limits
    import capo_shield.types.timestamp


class Subscription(TypedDict, closed=True):
    start_time: NotRequired["capo_shield.types.timestamp.Timestamp"]
    """<p>The start time of the subscription, in Unix time in seconds. </p>"""
    end_time: NotRequired["capo_shield.types.timestamp.Timestamp"]
    """<p>The date and time your subscription will end.</p>"""
    time_commitment_in_seconds: (
        "capo_shield.types.duration_in_seconds.DurationInSeconds"
    )
    """<p>The length, in seconds, of the Shield Advanced subscription for the account.</p>"""
    auto_renew: NotRequired["capo_shield.types.auto_renew.AutoRenew"]
    """<p>If <code>ENABLED</code>, the subscription will be automatically renewed at the end of the existing subscription period.</p> <p>When you initally create a subscription, <code>AutoRenew</code> is set to <code>ENABLED</code>. You can change this by submitting an <code>UpdateSubscription</code> request. If the <code>UpdateSubscription</code> request does not included a value for <code>AutoRenew</code>, the existing value for <code>AutoRenew</code> remains unchanged.</p>"""
    limits: NotRequired["capo_shield.types.limits.Limits"]
    """<p>Specifies how many protections of a given type you can create.</p>"""
    proactive_engagement_status: NotRequired[
        "capo_shield.types.proactive_engagement_status.ProactiveEngagementStatus"
    ]
    """<p>If <code>ENABLED</code>, the Shield Response Team (SRT) will use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.</p> <p>If <code>PENDING</code>, you have requested proactive engagement and the request is pending. The status changes to <code>ENABLED</code> when your request is fully processed.</p> <p>If <code>DISABLED</code>, the SRT will not proactively notify contacts about escalations or to initiate proactive customer support. </p>"""
    subscription_limits: "capo_shield.types.subscription_limits.SubscriptionLimits"
    """<p>Limits settings for your subscription. </p>"""
    subscription_arn: NotRequired["capo_shield.types.resource_arn.ResourceArn"]
    """<p>The ARN (Amazon Resource Name) of the subscription.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subscription) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_shield.types.timestamp

        out["StartTime"] = capo_shield.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_shield.types.timestamp

        out["EndTime"] = capo_shield.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    out["TimeCommitmentInSeconds"] = value.get("time_commitment_in_seconds", 0)
    if "auto_renew" in value:
        import capo_shield.types.auto_renew

        out["AutoRenew"] = capo_shield.types.auto_renew.serialize_aws_json_1_1(
            value["auto_renew"]
        )
    if "limits" in value:
        import capo_shield.types.limits

        out["Limits"] = capo_shield.types.limits.serialize_aws_json_1_1(value["limits"])
    if "proactive_engagement_status" in value:
        import capo_shield.types.proactive_engagement_status

        out["ProactiveEngagementStatus"] = (
            capo_shield.types.proactive_engagement_status.serialize_aws_json_1_1(
                value["proactive_engagement_status"]
            )
        )
    import capo_shield.types.subscription_limits

    out["SubscriptionLimits"] = (
        capo_shield.types.subscription_limits.serialize_aws_json_1_1(
            value["subscription_limits"]
        )
    )
    if "subscription_arn" in value:
        out["SubscriptionArn"] = value["subscription_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_shield.types.timestamp

        out["start_time"] = capo_shield.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_shield.types.timestamp

        out["end_time"] = capo_shield.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("TimeCommitmentInSeconds") is not None:
        out["time_commitment_in_seconds"] = data["TimeCommitmentInSeconds"]
    else:
        out["time_commitment_in_seconds"] = 0
    if data.get("AutoRenew") is not None:
        import capo_shield.types.auto_renew

        out["auto_renew"] = capo_shield.types.auto_renew.deserialize_aws_json_1_1(
            data["AutoRenew"]
        )
    if data.get("Limits") is not None:
        import capo_shield.types.limits

        out["limits"] = capo_shield.types.limits.deserialize_aws_json_1_1(
            data["Limits"]
        )
    if data.get("ProactiveEngagementStatus") is not None:
        import capo_shield.types.proactive_engagement_status

        out["proactive_engagement_status"] = (
            capo_shield.types.proactive_engagement_status.deserialize_aws_json_1_1(
                data["ProactiveEngagementStatus"]
            )
        )
    if data.get("SubscriptionLimits") is not None:
        import capo_shield.types.subscription_limits

        out["subscription_limits"] = (
            capo_shield.types.subscription_limits.deserialize_aws_json_1_1(
                data["SubscriptionLimits"]
            )
        )
    else:
        raise DeserializationError("Subscription.subscription_limits required")
    if data.get("SubscriptionArn") is not None:
        out["subscription_arn"] = data["SubscriptionArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Subscription) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_shield.types.timestamp

        out["StartTime"] = capo_shield.types.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_shield.types.timestamp

        out["EndTime"] = capo_shield.types.timestamp.serialize_cbor(value["end_time"])
    out["TimeCommitmentInSeconds"] = value.get("time_commitment_in_seconds", 0)
    if "auto_renew" in value:
        import capo_shield.types.auto_renew

        out["AutoRenew"] = capo_shield.types.auto_renew.serialize_cbor(
            value["auto_renew"]
        )
    if "limits" in value:
        import capo_shield.types.limits

        out["Limits"] = capo_shield.types.limits.serialize_cbor(value["limits"])
    if "proactive_engagement_status" in value:
        import capo_shield.types.proactive_engagement_status

        out["ProactiveEngagementStatus"] = (
            capo_shield.types.proactive_engagement_status.serialize_cbor(
                value["proactive_engagement_status"]
            )
        )
    import capo_shield.types.subscription_limits

    out["SubscriptionLimits"] = capo_shield.types.subscription_limits.serialize_cbor(
        value["subscription_limits"]
    )
    if "subscription_arn" in value:
        out["SubscriptionArn"] = value["subscription_arn"]
    return out


def deserialize_cbor(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_shield.types.timestamp

        out["start_time"] = capo_shield.types.timestamp.deserialize_cbor(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_shield.types.timestamp

        out["end_time"] = capo_shield.types.timestamp.deserialize_cbor(data["EndTime"])
    if data.get("TimeCommitmentInSeconds") is not None:
        out["time_commitment_in_seconds"] = data["TimeCommitmentInSeconds"]
    else:
        out["time_commitment_in_seconds"] = 0
    if data.get("AutoRenew") is not None:
        import capo_shield.types.auto_renew

        out["auto_renew"] = capo_shield.types.auto_renew.deserialize_cbor(
            data["AutoRenew"]
        )
    if data.get("Limits") is not None:
        import capo_shield.types.limits

        out["limits"] = capo_shield.types.limits.deserialize_cbor(data["Limits"])
    if data.get("ProactiveEngagementStatus") is not None:
        import capo_shield.types.proactive_engagement_status

        out["proactive_engagement_status"] = (
            capo_shield.types.proactive_engagement_status.deserialize_cbor(
                data["ProactiveEngagementStatus"]
            )
        )
    if data.get("SubscriptionLimits") is not None:
        import capo_shield.types.subscription_limits

        out["subscription_limits"] = (
            capo_shield.types.subscription_limits.deserialize_cbor(
                data["SubscriptionLimits"]
            )
        )
    else:
        raise DeserializationError("Subscription.subscription_limits required")
    if data.get("SubscriptionArn") is not None:
        out["subscription_arn"] = data["SubscriptionArn"]
    return out
