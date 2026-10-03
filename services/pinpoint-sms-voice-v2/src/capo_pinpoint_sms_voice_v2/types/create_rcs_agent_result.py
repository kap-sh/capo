"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateRcsAgentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_status
    import capo_pinpoint_sms_voice_v2.types.rcs_event_type_list
    import capo_pinpoint_sms_voice_v2.types.tag_list
    import capo_pinpoint_sms_voice_v2.types.two_way_channel_arn
    import capo_pinpoint_sms_voice_v2.types.two_way_media_s3_bucket_name
    import capo_pinpoint_sms_voice_v2.types.two_way_media_s3_key_prefix


class CreateRcsAgentResult(TypedDict, closed=True):
    rcs_agent_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the newly created RCS agent.</p>"""
    rcs_agent_id: "str"
    """<p>The unique identifier for the RCS agent.</p>"""
    status: "capo_pinpoint_sms_voice_v2.types.rcs_agent_status.RcsAgentStatus"
    """<p>The current status of the RCS agent.</p>"""
    deletion_protection_enabled: "bool"
    """<p>When set to true deletion protection is enabled. By default this is set to false.</p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The name of the OptOutList associated with the RCS agent.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the RCS agent was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""
    self_managed_opt_outs_enabled: "bool"
    """<p>By default this is set to false. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>"""
    two_way_channel_arn: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the two way channel.</p>"""
    two_way_channel_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    two_way_enabled: "bool"
    """<p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>"""
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
    """<p>The ARN of the IAM role used to write inbound RCS media files to the S3 bucket. The role must have <code>s3:PutObject</code> permission on the bucket and a trust policy allowing <code>sms-voice.amazonaws.com</code> to assume it.</p>"""
    two_way_rcs_events_enabled: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_event_type_list.RcsEventTypeList"
    ]
    """<p>The list of RCS event types enabled for two-way messaging on the agent.</p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) associated with the RCS agent.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRcsAgentResult) -> dict:
    out: dict = {}
    out["RcsAgentArn"] = value["rcs_agent_arn"]
    out["RcsAgentId"] = value["rcs_agent_id"]
    out["Status"] = value["status"]
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    out["SelfManagedOptOutsEnabled"] = value.get("self_managed_opt_outs_enabled", False)
    if "two_way_channel_arn" in value:
        out["TwoWayChannelArn"] = value["two_way_channel_arn"]
    if "two_way_channel_role" in value:
        out["TwoWayChannelRole"] = value["two_way_channel_role"]
    out["TwoWayEnabled"] = value.get("two_way_enabled", False)
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
    if "tags" in value:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = capo_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRcsAgentResult:
    out: CreateRcsAgentResult = {}  # type: ignore[typeddict-item]
    if data.get("RcsAgentArn") is not None:
        out["rcs_agent_arn"] = data["RcsAgentArn"]
    else:
        raise DeserializationError("CreateRcsAgentResult.rcs_agent_arn required")
    if data.get("RcsAgentId") is not None:
        out["rcs_agent_id"] = data["RcsAgentId"]
    else:
        raise DeserializationError("CreateRcsAgentResult.rcs_agent_id required")
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("CreateRcsAgentResult.status required")
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("CreateRcsAgentResult.created_timestamp required")
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
    if data.get("Tags") is not None:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
