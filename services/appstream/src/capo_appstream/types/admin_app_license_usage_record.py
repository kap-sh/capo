"""Generated from Smithy shape ``com.amazonaws.appstream#AdminAppLicenseUsageRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.aws_account_id
    import capo_appstream.types.string
    import capo_appstream.types.timestamp


class AdminAppLicenseUsageRecord(TypedDict, closed=True):
    user_arn: NotRequired["capo_appstream.types.string.String"]
    """<p>The ARN of the user who used the license-included application.</p>"""
    billing_period: NotRequired["capo_appstream.types.string.String"]
    """<p>The billing period for the license usage record.</p>"""
    owner_aws_account_id: NotRequired[
        "capo_appstream.types.aws_account_id.AwsAccountId"
    ]
    """<p>The account ID of the owner of the license.</p>"""
    subscription_first_used_date: NotRequired[
        "capo_appstream.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the license was first used.</p>"""
    subscription_last_used_date: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The date and time when the license was last used.</p>"""
    license_type: NotRequired["capo_appstream.types.string.String"]
    """<p>The type of license (for example, Microsoft Office).</p>"""
    user_id: NotRequired["capo_appstream.types.string.String"]
    """<p>The ID of the user who used the license-included application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminAppLicenseUsageRecord) -> dict:
    out: dict = {}
    if "user_arn" in value:
        out["UserArn"] = value["user_arn"]
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "owner_aws_account_id" in value:
        out["OwnerAWSAccountId"] = value["owner_aws_account_id"]
    if "subscription_first_used_date" in value:
        import capo_appstream.types.timestamp

        out["SubscriptionFirstUsedDate"] = (
            capo_appstream.types.timestamp.serialize_aws_json_1_1(
                value["subscription_first_used_date"]
            )
        )
    if "subscription_last_used_date" in value:
        import capo_appstream.types.timestamp

        out["SubscriptionLastUsedDate"] = (
            capo_appstream.types.timestamp.serialize_aws_json_1_1(
                value["subscription_last_used_date"]
            )
        )
    if "license_type" in value:
        out["LicenseType"] = value["license_type"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminAppLicenseUsageRecord:
    out: AdminAppLicenseUsageRecord = {}  # type: ignore[typeddict-item]
    if data.get("UserArn") is not None:
        out["user_arn"] = data["UserArn"]
    if data.get("BillingPeriod") is not None:
        out["billing_period"] = data["BillingPeriod"]
    if data.get("OwnerAWSAccountId") is not None:
        out["owner_aws_account_id"] = data["OwnerAWSAccountId"]
    if data.get("SubscriptionFirstUsedDate") is not None:
        import capo_appstream.types.timestamp

        out["subscription_first_used_date"] = (
            capo_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["SubscriptionFirstUsedDate"]
            )
        )
    if data.get("SubscriptionLastUsedDate") is not None:
        import capo_appstream.types.timestamp

        out["subscription_last_used_date"] = (
            capo_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["SubscriptionLastUsedDate"]
            )
        )
    if data.get("LicenseType") is not None:
        out["license_type"] = data["LicenseType"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AdminAppLicenseUsageRecord) -> dict:
    out: dict = {}
    if "user_arn" in value:
        out["UserArn"] = value["user_arn"]
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "owner_aws_account_id" in value:
        out["OwnerAWSAccountId"] = value["owner_aws_account_id"]
    if "subscription_first_used_date" in value:
        import capo_appstream.types.timestamp

        out["SubscriptionFirstUsedDate"] = (
            capo_appstream.types.timestamp.serialize_cbor(
                value["subscription_first_used_date"]
            )
        )
    if "subscription_last_used_date" in value:
        import capo_appstream.types.timestamp

        out["SubscriptionLastUsedDate"] = capo_appstream.types.timestamp.serialize_cbor(
            value["subscription_last_used_date"]
        )
    if "license_type" in value:
        out["LicenseType"] = value["license_type"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_cbor(data: dict) -> AdminAppLicenseUsageRecord:
    out: AdminAppLicenseUsageRecord = {}  # type: ignore[typeddict-item]
    if data.get("UserArn") is not None:
        out["user_arn"] = data["UserArn"]
    if data.get("BillingPeriod") is not None:
        out["billing_period"] = data["BillingPeriod"]
    if data.get("OwnerAWSAccountId") is not None:
        out["owner_aws_account_id"] = data["OwnerAWSAccountId"]
    if data.get("SubscriptionFirstUsedDate") is not None:
        import capo_appstream.types.timestamp

        out["subscription_first_used_date"] = (
            capo_appstream.types.timestamp.deserialize_cbor(
                data["SubscriptionFirstUsedDate"]
            )
        )
    if data.get("SubscriptionLastUsedDate") is not None:
        import capo_appstream.types.timestamp

        out["subscription_last_used_date"] = (
            capo_appstream.types.timestamp.deserialize_cbor(
                data["SubscriptionLastUsedDate"]
            )
        )
    if data.get("LicenseType") is not None:
        out["license_type"] = data["LicenseType"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    return out
