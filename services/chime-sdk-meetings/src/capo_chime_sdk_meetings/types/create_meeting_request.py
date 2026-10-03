"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateMeetingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.client_request_token
    import capo_chime_sdk_meetings.types.external_meeting_id
    import capo_chime_sdk_meetings.types.external_user_id
    import capo_chime_sdk_meetings.types.media_placement_network_type
    import capo_chime_sdk_meetings.types.media_region
    import capo_chime_sdk_meetings.types.meeting_features_configuration
    import capo_chime_sdk_meetings.types.notifications_configuration
    import capo_chime_sdk_meetings.types.primary_meeting_id
    import capo_chime_sdk_meetings.types.tag_list
    import capo_chime_sdk_meetings.types.tenant_id_list


class CreateMeetingRequest(TypedDict, closed=True):
    client_request_token: (
        "capo_chime_sdk_meetings.types.client_request_token.ClientRequestToken"
    )
    """<p>The unique identifier for the client request. Use a different token for different meetings.</p>"""
    media_region: "capo_chime_sdk_meetings.types.media_region.MediaRegion"
    """<p>The Region in which to create the meeting.</p> <p> Available values: <code>af-south-1</code>, <code>ap-northeast-1</code>, <code>ap-northeast-2</code>, <code>ap-south-1</code>, <code>ap-southeast-1</code>, <code>ap-southeast-2</code>, <code>ca-central-1</code>, <code>eu-central-1</code>, <code>eu-north-1</code>, <code>eu-south-1</code>, <code>eu-west-1</code>, <code>eu-west-2</code>, <code>eu-west-3</code>, <code>sa-east-1</code>, <code>us-east-1</code>, <code>us-east-2</code>, <code>us-west-1</code>, <code>us-west-2</code>. </p> <p>Available values in Amazon Web Services GovCloud (US) Regions: <code>us-gov-east-1</code>, <code>us-gov-west-1</code>.</p>"""
    meeting_host_id: NotRequired[
        "capo_chime_sdk_meetings.types.external_user_id.ExternalUserId"
    ]
    """<p>Reserved.</p>"""
    external_meeting_id: (
        "capo_chime_sdk_meetings.types.external_meeting_id.ExternalMeetingId"
    )
    r"""<p>The external meeting ID.</p> <p>Pattern: <code>[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*</code> </p> <p>Values that begin with <code>aws:</code> are reserved. You can't configure a value that uses this prefix. Case insensitive.</p>"""
    notifications_configuration: NotRequired[
        "capo_chime_sdk_meetings.types.notifications_configuration.NotificationsConfiguration"
    ]
    """<p>The configuration for resource targets to receive notifications when meeting and attendee events occur.</p>"""
    meeting_features: NotRequired[
        "capo_chime_sdk_meetings.types.meeting_features_configuration.MeetingFeaturesConfiguration"
    ]
    """<p>Lists the audio and video features enabled for a meeting, such as echo reduction.</p>"""
    primary_meeting_id: NotRequired[
        "capo_chime_sdk_meetings.types.primary_meeting_id.PrimaryMeetingId"
    ]
    """<p>When specified, replicates the media from the primary meeting to the new meeting.</p>"""
    tenant_ids: NotRequired["capo_chime_sdk_meetings.types.tenant_id_list.TenantIdList"]
    """<p>A consistent and opaque identifier, created and maintained by the builder to represent a segment of their users.</p>"""
    tags: NotRequired["capo_chime_sdk_meetings.types.tag_list.TagList"]
    """<p>Applies one or more tags to an Amazon Chime SDK meeting. Note the following:</p> <ul> <li> <p>Not all resources have tags. For a list of services with resources that support tagging using this operation, see <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html">Services that support the Resource Groups Tagging API</a>. If the resource doesn't yet support this operation, the resource's service might support tagging using its own API operations. For more information, refer to the documentation for that service.</p> </li> <li> <p>Each resource can have up to 50 tags. For other limits, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions">Tag Naming and Usage Conventions</a> in the <i>AWS General Reference</i>.</p> </li> <li> <p>You can only tag resources that are located in the specified Amazon Web Services Region for the Amazon Web Services account.</p> </li> <li> <p>To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see the documentation for each service.</p> </li> </ul> <important> <p>Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.</p> </important> <p> <b>Minimum permissions</b> </p> <p>In addition to the <code>tag:TagResources</code> permission required by this operation, you must also have the tagging permission defined by the service that created the resource. For example, to tag a <code>ChimeSDKMeetings</code> instance using the <code>TagResources</code> operation, you must have both of the following permissions:</p> <p> <code>tag:TagResources</code> </p> <p> <code>ChimeSDKMeetings:CreateTags</code> </p> <note> <p>Some services might have specific requirements for tagging some resources. For example, to tag an Amazon S3 bucket, you must also have the <code>s3:GetBucketTagging</code> permission. If the expected minimum permissions don't work, check the documentation for that service's tagging APIs for more information.</p> </note>"""
    media_placement_network_type: NotRequired[
        "capo_chime_sdk_meetings.types.media_placement_network_type.MediaPlacementNetworkType"
    ]
    """<p>The type of network for the media placement. Either IPv4 only or dual-stack (IPv4 and IPv6).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeetingRequest) -> dict:
    out: dict = {}
    out["ClientRequestToken"] = value["client_request_token"]
    out["MediaRegion"] = value["media_region"]
    if "meeting_host_id" in value:
        out["MeetingHostId"] = value["meeting_host_id"]
    out["ExternalMeetingId"] = value["external_meeting_id"]
    if "notifications_configuration" in value:
        import capo_chime_sdk_meetings.types.notifications_configuration

        out["NotificationsConfiguration"] = (
            capo_chime_sdk_meetings.types.notifications_configuration.serialize_json(
                value["notifications_configuration"]
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
    if "tags" in value:
        import capo_chime_sdk_meetings.types.tag_list

        out["Tags"] = capo_chime_sdk_meetings.types.tag_list.serialize_json(
            value["tags"]
        )
    if "media_placement_network_type" in value:
        import capo_chime_sdk_meetings.types.media_placement_network_type

        out["MediaPlacementNetworkType"] = (
            capo_chime_sdk_meetings.types.media_placement_network_type.serialize_json(
                value["media_placement_network_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMeetingRequest:
    out: CreateMeetingRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError("CreateMeetingRequest.client_request_token required")
    if data.get("MediaRegion") is not None:
        out["media_region"] = data["MediaRegion"]
    else:
        raise DeserializationError("CreateMeetingRequest.media_region required")
    if data.get("MeetingHostId") is not None:
        out["meeting_host_id"] = data["MeetingHostId"]
    if data.get("ExternalMeetingId") is not None:
        out["external_meeting_id"] = data["ExternalMeetingId"]
    else:
        raise DeserializationError("CreateMeetingRequest.external_meeting_id required")
    if data.get("NotificationsConfiguration") is not None:
        import capo_chime_sdk_meetings.types.notifications_configuration

        out["notifications_configuration"] = (
            capo_chime_sdk_meetings.types.notifications_configuration.deserialize_json(
                data["NotificationsConfiguration"]
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
    if data.get("Tags") is not None:
        import capo_chime_sdk_meetings.types.tag_list

        out["tags"] = capo_chime_sdk_meetings.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if data.get("MediaPlacementNetworkType") is not None:
        import capo_chime_sdk_meetings.types.media_placement_network_type

        out["media_placement_network_type"] = (
            capo_chime_sdk_meetings.types.media_placement_network_type.deserialize_json(
                data["MediaPlacementNetworkType"]
            )
        )
    return out
