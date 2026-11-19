"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetAddonSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.addon_name
    import capo_mailmanager.types.addon_subscription_arn


class GetAddonSubscriptionResponse(TypedDict, closed=True):
    addon_name: NotRequired["capo_mailmanager.types.addon_name.AddonName"]
    """<p>The name of the Add On for the subscription.</p>"""
    addon_subscription_arn: NotRequired[
        "capo_mailmanager.types.addon_subscription_arn.AddonSubscriptionArn"
    ]
    """<p>Amazon Resource Name (ARN) for the subscription.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the Add On subscription was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAddonSubscriptionResponse) -> dict:
    out: dict = {}
    if "addon_name" in value:
        out["AddonName"] = value["addon_name"]
    if "addon_subscription_arn" in value:
        out["AddonSubscriptionArn"] = value["addon_subscription_arn"]
    if "created_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAddonSubscriptionResponse:
    out: GetAddonSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("AddonName") is not None:
        out["addon_name"] = data["AddonName"]
    if data.get("AddonSubscriptionArn") is not None:
        out["addon_subscription_arn"] = data["AddonSubscriptionArn"]
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAddonSubscriptionResponse) -> dict:
    out: dict = {}
    if "addon_name" in value:
        out["AddonName"] = value["addon_name"]
    if "addon_subscription_arn" in value:
        out["AddonSubscriptionArn"] = value["addon_subscription_arn"]
    if "created_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_cbor(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetAddonSubscriptionResponse:
    out: GetAddonSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("AddonName") is not None:
        out["addon_name"] = data["AddonName"]
    if data.get("AddonSubscriptionArn") is not None:
        out["addon_subscription_arn"] = data["AddonSubscriptionArn"]
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_cbor(
                data["CreatedTimestamp"]
            )
        )
    return out
