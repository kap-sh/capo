"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#Meeting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.amazon_resource_name
    import capo_chime_sdk_meetings.types.external_meeting_id
    import capo_chime_sdk_meetings.types.external_user_id
    import capo_chime_sdk_meetings.types.guid_string
    import capo_chime_sdk_meetings.types.media_placement
    import capo_chime_sdk_meetings.types.media_region
    import capo_chime_sdk_meetings.types.meeting_features_configuration
    import capo_chime_sdk_meetings.types.primary_meeting_id
    import capo_chime_sdk_meetings.types.tenant_id_list


class Meeting(TypedDict, closed=True):
    meeting_id: NotRequired["capo_chime_sdk_meetings.types.guid_string.GuidString"]
    """<p>The Amazon Chime SDK meeting ID.</p>"""
    meeting_host_id: NotRequired[
        "capo_chime_sdk_meetings.types.external_user_id.ExternalUserId"
    ]
    """<p>Reserved.</p>"""
    external_meeting_id: NotRequired[
        "capo_chime_sdk_meetings.types.external_meeting_id.ExternalMeetingId"
    ]
    r"""<p>The external meeting ID.</p> <p>Pattern: <code>[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*</code> </p> <p>Values that begin with <code>aws:</code> are reserved. You can't configure a value that uses this prefix. Case insensitive.</p>"""
    media_region: NotRequired["capo_chime_sdk_meetings.types.media_region.MediaRegion"]
    """<p>The Region in which you create the meeting. Available values: <code>af-south-1</code>, <code>ap-northeast-1</code>, <code>ap-northeast-2</code>, <code>ap-south-1</code>, <code>ap-southeast-1</code>, <code>ap-southeast-2</code>, <code>ca-central-1</code>, <code>eu-central-1</code>, <code>eu-north-1</code>, <code>eu-south-1</code>, <code>eu-west-1</code>, <code>eu-west-2</code>, <code>eu-west-3</code>, <code>sa-east-1</code>, <code>us-east-1</code>, <code>us-east-2</code>, <code>us-west-1</code>, <code>us-west-2</code>.</p> <p>Available values in Amazon Web Services GovCloud (US) Regions: <code>us-gov-east-1</code>, <code>us-gov-west-1</code>.</p>"""
    media_placement: NotRequired[
        "capo_chime_sdk_meetings.types.media_placement.MediaPlacement"
    ]
    """<p>The media placement for the meeting.</p>"""
    meeting_features: NotRequired[
        "capo_chime_sdk_meetings.types.meeting_features_configuration.MeetingFeaturesConfiguration"
    ]
    """<p>The features available to a meeting, such as echo reduction.</p>"""
    primary_meeting_id: NotRequired[
        "capo_chime_sdk_meetings.types.primary_meeting_id.PrimaryMeetingId"
    ]
    """<p>When specified, replicates the media from the primary meeting to this meeting.</p>"""
    tenant_ids: NotRequired["capo_chime_sdk_meetings.types.tenant_id_list.TenantIdList"]
    """<p>Array of strings.</p>"""
    meeting_arn: NotRequired[
        "capo_chime_sdk_meetings.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the meeting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Meeting) -> dict:
    out: dict = {}
    if "meeting_id" in value:
        out["MeetingId"] = value["meeting_id"]
    if "meeting_host_id" in value:
        out["MeetingHostId"] = value["meeting_host_id"]
    if "external_meeting_id" in value:
        out["ExternalMeetingId"] = value["external_meeting_id"]
    if "media_region" in value:
        out["MediaRegion"] = value["media_region"]
    if "media_placement" in value:
        import capo_chime_sdk_meetings.types.media_placement

        out["MediaPlacement"] = (
            capo_chime_sdk_meetings.types.media_placement.serialize_json(
                value["media_placement"]
            )
        )
    if "meeting_features" in value:
        import capo_chime_sdk_meetings.types.meeting_features_configuration

        out["MeetingFeatures"] = (
            capo_chime_sdk_meetings.types.meeting_features_configuration.serialize_json(
                value["meeting_features"]
            )
        )
    if "primary_meeting_id" in value:
        out["PrimaryMeetingId"] = value["primary_meeting_id"]
    if "tenant_ids" in value:
        import capo_chime_sdk_meetings.types.tenant_id_list

        out["TenantIds"] = capo_chime_sdk_meetings.types.tenant_id_list.serialize_json(
            value["tenant_ids"]
        )
    if "meeting_arn" in value:
        out["MeetingArn"] = value["meeting_arn"]
    return out


def deserialize_json(data: dict) -> Meeting:
    out: Meeting = {}  # type: ignore[typeddict-item]
    if data.get("MeetingId") is not None:
        out["meeting_id"] = data["MeetingId"]
    if data.get("MeetingHostId") is not None:
        out["meeting_host_id"] = data["MeetingHostId"]
    if data.get("ExternalMeetingId") is not None:
        out["external_meeting_id"] = data["ExternalMeetingId"]
    if data.get("MediaRegion") is not None:
        out["media_region"] = data["MediaRegion"]
    if data.get("MediaPlacement") is not None:
        import capo_chime_sdk_meetings.types.media_placement

        out["media_placement"] = (
            capo_chime_sdk_meetings.types.media_placement.deserialize_json(
                data["MediaPlacement"]
            )
        )
    if data.get("MeetingFeatures") is not None:
        import capo_chime_sdk_meetings.types.meeting_features_configuration

        out["meeting_features"] = (
            capo_chime_sdk_meetings.types.meeting_features_configuration.deserialize_json(
                data["MeetingFeatures"]
            )
        )
    if data.get("PrimaryMeetingId") is not None:
        out["primary_meeting_id"] = data["PrimaryMeetingId"]
    if data.get("TenantIds") is not None:
        import capo_chime_sdk_meetings.types.tenant_id_list

        out["tenant_ids"] = (
            capo_chime_sdk_meetings.types.tenant_id_list.deserialize_json(
                data["TenantIds"]
            )
        )
    if data.get("MeetingArn") is not None:
        out["meeting_arn"] = data["MeetingArn"]
    return out
