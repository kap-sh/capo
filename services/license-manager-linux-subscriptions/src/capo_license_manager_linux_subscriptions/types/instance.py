"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_linux_subscriptions.types.product_code_list


class Instance(TypedDict, closed=True):
    ami_id: NotRequired["str"]
    """<p>The AMI ID used to launch the instance.</p>"""
    instance_id: NotRequired["str"]
    """<p>The instance ID of the resource.</p>"""
    instance_type: NotRequired["str"]
    """<p>The instance type of the resource.</p>"""
    account_id: NotRequired["str"]
    """<p>The account ID which owns the instance.</p>"""
    status: NotRequired["str"]
    """<p>The status of the instance.</p>"""
    region: NotRequired["str"]
    """<p>The Region the instance is running in.</p>"""
    usage_operation: NotRequired["str"]
    """<p>The usage operation of the instance. For more information, see For more information, see <a href="https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-usage-operation.html">Usage operation values</a> in the <i>License Manager User Guide</i>.</p>"""
    product_code: NotRequired[
        "capo_license_manager_linux_subscriptions.types.product_code_list.ProductCodeList"
    ]
    """<p>The product code for the instance. For more information, see <a href="https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-usage-operation.html">Usage operation values</a> in the <i>License Manager User Guide</i> .</p>"""
    last_updated_time: NotRequired["str"]
    """<p>The time in which the last discovery updated the instance details.</p>"""
    subscription_name: NotRequired["str"]
    """<p>The name of the license subscription that the instance uses.</p>"""
    os_version: NotRequired["str"]
    """<p>The operating system software version that runs on your instance.</p>"""
    subscription_provider_create_time: NotRequired["str"]
    """<p>The timestamp when you registered the third-party Linux subscription provider for the subscription that the instance uses.</p>"""
    subscription_provider_update_time: NotRequired["str"]
    """<p>The timestamp from the last time that the instance synced with the registered third-party Linux subscription provider.</p>"""
    dual_subscription: NotRequired["str"]
    """<p>Indicates that you have two different license subscriptions for the same software on your instance.</p>"""
    registered_with_subscription_provider: NotRequired["str"]
    """<p>Indicates that your instance uses a BYOL license subscription from a third-party Linux subscription provider that you've registered with License Manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Instance) -> dict:
    out: dict = {}
    if "ami_id" in value:
        out["AmiId"] = value["ami_id"]
    if "instance_id" in value:
        out["InstanceID"] = value["instance_id"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "account_id" in value:
        out["AccountID"] = value["account_id"]
    if "status" in value:
        out["Status"] = value["status"]
    if "region" in value:
        out["Region"] = value["region"]
    if "usage_operation" in value:
        out["UsageOperation"] = value["usage_operation"]
    if "product_code" in value:
        import capo_license_manager_linux_subscriptions.types.product_code_list

        out["ProductCode"] = (
            capo_license_manager_linux_subscriptions.types.product_code_list.serialize_json(
                value["product_code"]
            )
        )
    if "last_updated_time" in value:
        out["LastUpdatedTime"] = value["last_updated_time"]
    if "subscription_name" in value:
        out["SubscriptionName"] = value["subscription_name"]
    if "os_version" in value:
        out["OsVersion"] = value["os_version"]
    if "subscription_provider_create_time" in value:
        out["SubscriptionProviderCreateTime"] = value[
            "subscription_provider_create_time"
        ]
    if "subscription_provider_update_time" in value:
        out["SubscriptionProviderUpdateTime"] = value[
            "subscription_provider_update_time"
        ]
    if "dual_subscription" in value:
        out["DualSubscription"] = value["dual_subscription"]
    if "registered_with_subscription_provider" in value:
        out["RegisteredWithSubscriptionProvider"] = value[
            "registered_with_subscription_provider"
        ]
    return out


def deserialize_json(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if data.get("AmiId") is not None:
        out["ami_id"] = data["AmiId"]
    if data.get("InstanceID") is not None:
        out["instance_id"] = data["InstanceID"]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("AccountID") is not None:
        out["account_id"] = data["AccountID"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("UsageOperation") is not None:
        out["usage_operation"] = data["UsageOperation"]
    if data.get("ProductCode") is not None:
        import capo_license_manager_linux_subscriptions.types.product_code_list

        out["product_code"] = (
            capo_license_manager_linux_subscriptions.types.product_code_list.deserialize_json(
                data["ProductCode"]
            )
        )
    if data.get("LastUpdatedTime") is not None:
        out["last_updated_time"] = data["LastUpdatedTime"]
    if data.get("SubscriptionName") is not None:
        out["subscription_name"] = data["SubscriptionName"]
    if data.get("OsVersion") is not None:
        out["os_version"] = data["OsVersion"]
    if data.get("SubscriptionProviderCreateTime") is not None:
        out["subscription_provider_create_time"] = data[
            "SubscriptionProviderCreateTime"
        ]
    if data.get("SubscriptionProviderUpdateTime") is not None:
        out["subscription_provider_update_time"] = data[
            "SubscriptionProviderUpdateTime"
        ]
    if data.get("DualSubscription") is not None:
        out["dual_subscription"] = data["DualSubscription"]
    if data.get("RegisteredWithSubscriptionProvider") is not None:
        out["registered_with_subscription_provider"] = data[
            "RegisteredWithSubscriptionProvider"
        ]
    return out
