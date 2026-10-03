"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PoolInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.message_type
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name
    import capo_pinpoint_sms_voice_v2.types.pool_status
    import capo_pinpoint_sms_voice_v2.types.two_way_channel_arn


class PoolInformation(TypedDict, closed=True):
    pool_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the pool.</p>"""
    pool_id: "str"
    """<p>The unique identifier for the pool.</p>"""
    status: "capo_pinpoint_sms_voice_v2.types.pool_status.PoolStatus"
    """<p>The current status of the pool.</p>"""
    message_type: "capo_pinpoint_sms_voice_v2.types.message_type.MessageType"
    """<p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>"""
    two_way_enabled: "bool"
    """<p>When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.</p>"""
    two_way_channel_arn: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the two way channel.</p>"""
    two_way_channel_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    self_managed_opt_outs_enabled: "bool"
    """<p>When set to false, an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests. For more information see <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/settings-sms-managing.html#settings-account-sms-self-managed-opt-out">Self-managed opt-outs</a> </p>"""
    opt_out_list_name: (
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    )
    """<p>The name of the OptOutList associated with the pool.</p>"""
    shared_routes_enabled: "bool"
    """<p>Allows you to enable shared routes on your pool.</p> <p>By default, this is set to <code>False</code>. If you set this value to <code>True</code>, your messages are sent using phone numbers or sender IDs (depending on the country) that are shared with other users. In some countries, such as the United States, senders aren't allowed to use shared routes and must use a dedicated phone number or short code.</p>"""
    deletion_protection_enabled: "bool"
    """<p>When set to true the pool can't be deleted.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the pool was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PoolInformation) -> dict:
    out: dict = {}
    out["PoolArn"] = value["pool_arn"]
    out["PoolId"] = value["pool_id"]
    out["Status"] = value["status"]
    out["MessageType"] = value["message_type"]
    out["TwoWayEnabled"] = value.get("two_way_enabled", False)
    if "two_way_channel_arn" in value:
        out["TwoWayChannelArn"] = value["two_way_channel_arn"]
    if "two_way_channel_role" in value:
        out["TwoWayChannelRole"] = value["two_way_channel_role"]
    out["SelfManagedOptOutsEnabled"] = value.get("self_managed_opt_outs_enabled", False)
    out["OptOutListName"] = value["opt_out_list_name"]
    out["SharedRoutesEnabled"] = value.get("shared_routes_enabled", False)
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PoolInformation:
    out: PoolInformation = {}  # type: ignore[typeddict-item]
    if data.get("PoolArn") is not None:
        out["pool_arn"] = data["PoolArn"]
    else:
        raise DeserializationError("PoolInformation.pool_arn required")
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError("PoolInformation.pool_id required")
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("PoolInformation.status required")
    if data.get("MessageType") is not None:
        out["message_type"] = data["MessageType"]
    else:
        raise DeserializationError("PoolInformation.message_type required")
    if data.get("TwoWayEnabled") is not None:
        out["two_way_enabled"] = data["TwoWayEnabled"]
    else:
        out["two_way_enabled"] = False
    if data.get("TwoWayChannelArn") is not None:
        out["two_way_channel_arn"] = data["TwoWayChannelArn"]
    if data.get("TwoWayChannelRole") is not None:
        out["two_way_channel_role"] = data["TwoWayChannelRole"]
    if data.get("SelfManagedOptOutsEnabled") is not None:
        out["self_managed_opt_outs_enabled"] = data["SelfManagedOptOutsEnabled"]
    else:
        out["self_managed_opt_outs_enabled"] = False
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    else:
        raise DeserializationError("PoolInformation.opt_out_list_name required")
    if data.get("SharedRoutesEnabled") is not None:
        out["shared_routes_enabled"] = data["SharedRoutesEnabled"]
    else:
        out["shared_routes_enabled"] = False
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("PoolInformation.created_timestamp required")
    return out
