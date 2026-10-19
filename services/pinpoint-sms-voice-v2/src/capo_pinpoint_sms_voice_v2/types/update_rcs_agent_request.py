"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdateRcsAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.iam_role_arn_or_unset
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.rcs_event_type_list
    import capo_pinpoint_sms_voice_v2.types.two_way_channel_arn
    import capo_pinpoint_sms_voice_v2.types.two_way_media_s3_bucket_name_or_unset
    import capo_pinpoint_sms_voice_v2.types.two_way_media_s3_key_prefix


class UpdateRcsAgentRequest(TypedDict, closed=True):
    rcs_agent_id: "capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn"
    """<p>The unique identifier of the RCS agent to update. You can use either the RcsAgentId or RcsAgentArn.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the RCS agent can't be deleted.</p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
    ]
    """<p>The OptOutList to associate with the RCS agent. Valid values are either OptOutListName or OptOutListArn.</p>"""
    self_managed_opt_outs_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>"""
    two_way_channel_arn: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the two way channel.</p>"""
    two_way_channel_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    two_way_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>"""
    two_way_media_s3_bucket_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_media_s3_bucket_name_or_unset.TwoWayMediaS3BucketNameOrUnset"
    ]
    """<p>The name of the S3 bucket where inbound RCS media files are stored. Two-way messaging must be enabled on the agent. To remove the media configuration, pass the sentinel value <code>UNSET_RCS_MEDIA_CONFIGURATION</code> for both this field and TwoWayMediaS3Role.</p>"""
    two_way_media_s3_key_prefix: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_media_s3_key_prefix.TwoWayMediaS3KeyPrefix"
    ]
    """<p>The key prefix used for inbound RCS media objects in the S3 bucket.</p>"""
    two_way_media_s3_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn_or_unset.IamRoleArnOrUnset"
    ]
    """<p>The ARN of the IAM role used to write inbound RCS media files to the S3 bucket. The role must have <code>s3:PutObject</code> permission on the bucket and a trust policy allowing <code>sms-voice.amazonaws.com</code> to assume it. To remove the media configuration, pass the sentinel value <code>UNSET_RCS_MEDIA_CONFIGURATION</code> for both this field and TwoWayMediaS3BucketName.</p>"""
    two_way_rcs_events_enabled: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_event_type_list.RcsEventTypeList"
    ]
    """<p>The list of RCS event types to enable for two-way messaging. Pass an empty list to disable all event types. The special value <code>ALL</code> enables all current and future event types and must be the sole element if used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRcsAgentRequest) -> dict:
    out: dict = {}
    out["RcsAgentId"] = value["rcs_agent_id"]
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    if "self_managed_opt_outs_enabled" in value:
        out["SelfManagedOptOutsEnabled"] = value["self_managed_opt_outs_enabled"]
    if "two_way_channel_arn" in value:
        out["TwoWayChannelArn"] = value["two_way_channel_arn"]
    if "two_way_channel_role" in value:
        out["TwoWayChannelRole"] = value["two_way_channel_role"]
    if "two_way_enabled" in value:
        out["TwoWayEnabled"] = value["two_way_enabled"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRcsAgentRequest:
    out: UpdateRcsAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("RcsAgentId") is not None:
        out["rcs_agent_id"] = data["RcsAgentId"]
    else:
        out["rcs_agent_id"] = ""
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    if data.get("SelfManagedOptOutsEnabled") is not None:
        out["self_managed_opt_outs_enabled"] = data["SelfManagedOptOutsEnabled"]
    if data.get("TwoWayChannelArn") is not None:
        out["two_way_channel_arn"] = data["TwoWayChannelArn"]
    if data.get("TwoWayChannelRole") is not None:
        out["two_way_channel_role"] = data["TwoWayChannelRole"]
    if data.get("TwoWayEnabled") is not None:
        out["two_way_enabled"] = data["TwoWayEnabled"]
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
    return out
