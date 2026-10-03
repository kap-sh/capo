"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsAgentInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.messaging_limits
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_status
    import capo_pinpoint_sms_voice_v2.types.rcs_event_type_list
    import capo_pinpoint_sms_voice_v2.types.testing_agent_information
    import capo_pinpoint_sms_voice_v2.types.two_way_channel_arn
    import capo_pinpoint_sms_voice_v2.types.two_way_media_s3_bucket_name
    import capo_pinpoint_sms_voice_v2.types.two_way_media_s3_key_prefix


class RcsAgentInformation(TypedDict, closed=True):
    rcs_agent_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the RCS agent.</p>"""
    rcs_agent_id: "str"
    """<p>The unique identifier for the RCS agent.</p>"""
    status: "capo_pinpoint_sms_voice_v2.types.rcs_agent_status.RcsAgentStatus"
    """<p>The current status of the RCS agent.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the RCS agent was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""
    deletion_protection_enabled: "bool"
    """<p>When set to true the RCS agent can't be deleted.</p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The name of the OptOutList associated with the RCS agent.</p>"""
    self_managed_opt_outs_enabled: "bool"
    """<p>When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>"""
    two_way_channel_arn: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the two way channel.</p>"""
    two_way_channel_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    two_way_enabled: "bool"
    """<p>When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.</p>"""
    pool_id: NotRequired["str"]
    """<p>The unique identifier of the pool associated with the RCS agent.</p>"""
    two_way_media_s3_bucket_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_media_s3_bucket_name.TwoWayMediaS3BucketName"
    ]
    """<p>The name of the S3 bucket where inbound RCS media files are stored.</p>"""
    two_way_media_s3_key_prefix: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_media_s3_key_prefix.TwoWayMediaS3KeyPrefix"
    ]
    """<p>The key prefix used for inbound RCS media objects in the S3 bucket.</p>"""
    two_way_media_s3_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The ARN of the IAM role used to write inbound RCS media files to the S3 bucket.</p>"""
    two_way_rcs_events_enabled: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_event_type_list.RcsEventTypeList"
    ]
    """<p>The list of RCS event types enabled for two-way messaging on the agent.</p>"""
    testing_agent: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.testing_agent_information.TestingAgentInformation"
    ]
    """<p>The testing agent information associated with the RCS agent.</p>"""
    messaging_limits: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.messaging_limits.MessagingLimits"
    ]
    """<p>The messaging limits that apply to the RCS agent, including the per-capability send rates.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsAgentInformation) -> dict:
    out: dict = {}
    out["RcsAgentArn"] = value["rcs_agent_arn"]
    out["RcsAgentId"] = value["rcs_agent_id"]
    out["Status"] = value["status"]
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    out["SelfManagedOptOutsEnabled"] = value.get("self_managed_opt_outs_enabled", False)
    if "two_way_channel_arn" in value:
        out["TwoWayChannelArn"] = value["two_way_channel_arn"]
    if "two_way_channel_role" in value:
        out["TwoWayChannelRole"] = value["two_way_channel_role"]
    out["TwoWayEnabled"] = value.get("two_way_enabled", False)
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "two_way_media_s3_bucket_name" in value:
        out["TwoWayMediaS3BucketName"] = value["two_way_media_s3_bucket_name"]
    if "two_way_media_s3_key_prefix" in value:
        out["TwoWayMediaS3KeyPrefix"] = value["two_way_media_s3_key_prefix"]
    if "two_way_media_s3_role" in value:
        out["TwoWayMediaS3Role"] = value["two_way_media_s3_role"]
    if "two_way_rcs_events_enabled" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_event_type_list

        out["TwoWayRcsEventsEnabled"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_event_type_list.serialize_aws_json_1_0(
                value["two_way_rcs_events_enabled"]
            )
        )
    if "testing_agent" in value:
        import capo_pinpoint_sms_voice_v2.types.testing_agent_information

        out["TestingAgent"] = (
            capo_pinpoint_sms_voice_v2.types.testing_agent_information.serialize_aws_json_1_0(
                value["testing_agent"]
            )
        )
    if "messaging_limits" in value:
        import capo_pinpoint_sms_voice_v2.types.messaging_limits

        out["MessagingLimits"] = (
            capo_pinpoint_sms_voice_v2.types.messaging_limits.serialize_aws_json_1_0(
                value["messaging_limits"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsAgentInformation:
    out: RcsAgentInformation = {}  # type: ignore[typeddict-item]
    if data.get("RcsAgentArn") is not None:
        out["rcs_agent_arn"] = data["RcsAgentArn"]
    else:
        raise DeserializationError("RcsAgentInformation.rcs_agent_arn required")
    if data.get("RcsAgentId") is not None:
        out["rcs_agent_id"] = data["RcsAgentId"]
    else:
        raise DeserializationError("RcsAgentInformation.rcs_agent_id required")
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("RcsAgentInformation.status required")
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("RcsAgentInformation.created_timestamp required")
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    if data.get("SelfManagedOptOutsEnabled") is not None:
        out["self_managed_opt_outs_enabled"] = data["SelfManagedOptOutsEnabled"]
    else:
        out["self_managed_opt_outs_enabled"] = False
    if data.get("TwoWayChannelArn") is not None:
        out["two_way_channel_arn"] = data["TwoWayChannelArn"]
    if data.get("TwoWayChannelRole") is not None:
        out["two_way_channel_role"] = data["TwoWayChannelRole"]
    if data.get("TwoWayEnabled") is not None:
        out["two_way_enabled"] = data["TwoWayEnabled"]
    else:
        out["two_way_enabled"] = False
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    if data.get("TwoWayMediaS3BucketName") is not None:
        out["two_way_media_s3_bucket_name"] = data["TwoWayMediaS3BucketName"]
    if data.get("TwoWayMediaS3KeyPrefix") is not None:
        out["two_way_media_s3_key_prefix"] = data["TwoWayMediaS3KeyPrefix"]
    if data.get("TwoWayMediaS3Role") is not None:
        out["two_way_media_s3_role"] = data["TwoWayMediaS3Role"]
    if data.get("TwoWayRcsEventsEnabled") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_event_type_list

        out["two_way_rcs_events_enabled"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_event_type_list.deserialize_aws_json_1_0(
                data["TwoWayRcsEventsEnabled"]
            )
        )
    if data.get("TestingAgent") is not None:
        import capo_pinpoint_sms_voice_v2.types.testing_agent_information

        out["testing_agent"] = (
            capo_pinpoint_sms_voice_v2.types.testing_agent_information.deserialize_aws_json_1_0(
                data["TestingAgent"]
            )
        )
    if data.get("MessagingLimits") is not None:
        import capo_pinpoint_sms_voice_v2.types.messaging_limits

        out["messaging_limits"] = (
            capo_pinpoint_sms_voice_v2.types.messaging_limits.deserialize_aws_json_1_0(
                data["MessagingLimits"]
            )
        )
    return out
