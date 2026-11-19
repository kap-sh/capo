"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetAddonInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.addon_instance_arn
    import capo_mailmanager.types.addon_name
    import capo_mailmanager.types.addon_subscription_id


class GetAddonInstanceResponse(TypedDict, closed=True):
    addon_subscription_id: NotRequired[
        "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId"
    ]
    """<p>The subscription ID associated to the instance.</p>"""
    addon_name: NotRequired["capo_mailmanager.types.addon_name.AddonName"]
    """<p>The name of the Add On provider associated to the subscription of the instance.</p>"""
    addon_instance_arn: NotRequired[
        "capo_mailmanager.types.addon_instance_arn.AddonInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Add On instance.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the Add On instance was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAddonInstanceResponse) -> dict:
    out: dict = {}
    if "addon_subscription_id" in value:
        out["AddonSubscriptionId"] = value["addon_subscription_id"]
    if "addon_name" in value:
        out["AddonName"] = value["addon_name"]
    if "addon_instance_arn" in value:
        out["AddonInstanceArn"] = value["addon_instance_arn"]
    if "created_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAddonInstanceResponse:
    out: GetAddonInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("AddonSubscriptionId") is not None:
        out["addon_subscription_id"] = data["AddonSubscriptionId"]
    if data.get("AddonName") is not None:
        out["addon_name"] = data["AddonName"]
    if data.get("AddonInstanceArn") is not None:
        out["addon_instance_arn"] = data["AddonInstanceArn"]
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAddonInstanceResponse) -> dict:
    out: dict = {}
    if "addon_subscription_id" in value:
        out["AddonSubscriptionId"] = value["addon_subscription_id"]
    if "addon_name" in value:
        out["AddonName"] = value["addon_name"]
    if "addon_instance_arn" in value:
        out["AddonInstanceArn"] = value["addon_instance_arn"]
    if "created_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_cbor(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetAddonInstanceResponse:
    out: GetAddonInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("AddonSubscriptionId") is not None:
        out["addon_subscription_id"] = data["AddonSubscriptionId"]
    if data.get("AddonName") is not None:
        out["addon_name"] = data["AddonName"]
    if data.get("AddonInstanceArn") is not None:
        out["addon_instance_arn"] = data["AddonInstanceArn"]
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_cbor(
                data["CreatedTimestamp"]
            )
        )
    return out
