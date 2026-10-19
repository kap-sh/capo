"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdatePoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.pool_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.two_way_channel_arn


class UpdatePoolRequest(TypedDict, closed=True):
    pool_id: "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"
    """<p>The unique identifier of the pool to update. Valid values are either the PoolId or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    two_way_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>"""
    two_way_channel_arn: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the two way channel.</p>"""
    two_way_channel_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    self_managed_opt_outs_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
    ]
    """<p>The OptOutList to associate with the pool. Valid values are either OptOutListName or OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    shared_routes_enabled: NotRequired["bool"]
    """<p>Indicates whether shared routes are enabled for the pool.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>When set to true the pool can't be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePoolRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    if "two_way_enabled" in value:
        out["TwoWayEnabled"] = value["two_way_enabled"]
    if "two_way_channel_arn" in value:
        out["TwoWayChannelArn"] = value["two_way_channel_arn"]
    if "two_way_channel_role" in value:
        out["TwoWayChannelRole"] = value["two_way_channel_role"]
    if "self_managed_opt_outs_enabled" in value:
        out["SelfManagedOptOutsEnabled"] = value["self_managed_opt_outs_enabled"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    if "shared_routes_enabled" in value:
        out["SharedRoutesEnabled"] = value["shared_routes_enabled"]
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePoolRequest:
    out: UpdatePoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    if data.get("TwoWayEnabled") is not None:
        out["two_way_enabled"] = data["TwoWayEnabled"]
    if data.get("TwoWayChannelArn") is not None:
        out["two_way_channel_arn"] = data["TwoWayChannelArn"]
    if data.get("TwoWayChannelRole") is not None:
        out["two_way_channel_role"] = data["TwoWayChannelRole"]
    if data.get("SelfManagedOptOutsEnabled") is not None:
        out["self_managed_opt_outs_enabled"] = data["SelfManagedOptOutsEnabled"]
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    if data.get("SharedRoutesEnabled") is not None:
        out["shared_routes_enabled"] = data["SharedRoutesEnabled"]
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    return out
