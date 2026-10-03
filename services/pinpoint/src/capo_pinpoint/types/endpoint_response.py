"""Generated from Smithy shape ``com.amazonaws.pinpoint#EndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.channel_type
    import capo_pinpoint.types.endpoint_demographic
    import capo_pinpoint.types.endpoint_location
    import capo_pinpoint.types.endpoint_user
    import capo_pinpoint.types.map_of__double
    import capo_pinpoint.types.map_of_list_of__string


class EndpointResponse(TypedDict, closed=True):
    address: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The destination address for messages or push notifications that you send to the endpoint. The address varies by channel. For example, the address for a push-notification channel is typically the token provided by a push notification service, such as an Apple Push Notification service (APNs) device token or a Firebase Cloud Messaging (FCM) registration token. The address for the SMS channel is a phone number in E.164 format, such as +12065550100. The address for the email channel is an email address.</p>"""
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that's associated with the endpoint.</p>"""
    attributes: NotRequired[
        "capo_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    """<p>One or more custom attributes that describe the endpoint by associating a name with an array of values. For example, the value of a custom attribute named Interests might be: ["Science", "Music", "Travel"]. You can use these attributes as filter criteria when you create segments.</p>"""
    channel_type: NotRequired["capo_pinpoint.types.channel_type.ChannelType"]
    """<p>The channel that's used when sending messages or push notifications to the endpoint.</p>"""
    cohort_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A number from 0-99 that represents the cohort that the endpoint is assigned to. Endpoints are grouped into cohorts randomly, and each cohort contains approximately 1 percent of the endpoints for an application. Amazon Pinpoint assigns cohorts to the holdout or treatment allocations for campaigns.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the endpoint was created.</p>"""
    demographic: NotRequired[
        "capo_pinpoint.types.endpoint_demographic.EndpointDemographic"
    ]
    """<p>The demographic information for the endpoint, such as the time zone and platform.</p>"""
    effective_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the endpoint was last updated.</p>"""
    endpoint_status: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>Specifies whether messages or push notifications are sent to the endpoint. Possible values are: ACTIVE, messages are sent to the endpoint; and, INACTIVE, messages aren’t sent to the endpoint.</p> <p>Amazon Pinpoint automatically sets this value to ACTIVE when you create an endpoint or update an existing endpoint. Amazon Pinpoint automatically sets this value to INACTIVE if you update another endpoint that has the same address specified by the Address property.</p>"""
    id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier that you assigned to the endpoint. The identifier should be a globally unique identifier (GUID) to ensure that it doesn't conflict with other endpoint identifiers that are associated with the application.</p>"""
    location: NotRequired["capo_pinpoint.types.endpoint_location.EndpointLocation"]
    """<p>The geographic information for the endpoint.</p>"""
    metrics: NotRequired["capo_pinpoint.types.map_of__double.MapOf__double"]
    """<p>One or more custom metrics that your app reports to Amazon Pinpoint for the endpoint.</p>"""
    opt_out: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>Specifies whether the user who's associated with the endpoint has opted out of receiving messages and push notifications from you. Possible values are: ALL, the user has opted out and doesn't want to receive any messages or push notifications; and, NONE, the user hasn't opted out and wants to receive all messages and push notifications.</p>"""
    request_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the most recent request to update the endpoint.</p>"""
    user: NotRequired["capo_pinpoint.types.endpoint_user.EndpointUser"]
    """<p>One or more custom user attributes that your app reports to Amazon Pinpoint for the user who's associated with the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointResponse) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "attributes" in value:
        import capo_pinpoint.types.map_of_list_of__string

        out["Attributes"] = capo_pinpoint.types.map_of_list_of__string.serialize_json(
            value["attributes"]
        )
    if "channel_type" in value:
        import capo_pinpoint.types.channel_type

        out["ChannelType"] = capo_pinpoint.types.channel_type.serialize_json(
            value["channel_type"]
        )
    if "cohort_id" in value:
        out["CohortId"] = value["cohort_id"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "demographic" in value:
        import capo_pinpoint.types.endpoint_demographic

        out["Demographic"] = capo_pinpoint.types.endpoint_demographic.serialize_json(
            value["demographic"]
        )
    if "effective_date" in value:
        out["EffectiveDate"] = value["effective_date"]
    if "endpoint_status" in value:
        out["EndpointStatus"] = value["endpoint_status"]
    if "id" in value:
        out["Id"] = value["id"]
    if "location" in value:
        import capo_pinpoint.types.endpoint_location

        out["Location"] = capo_pinpoint.types.endpoint_location.serialize_json(
            value["location"]
        )
    if "metrics" in value:
        import capo_pinpoint.types.map_of__double

        out["Metrics"] = capo_pinpoint.types.map_of__double.serialize_json(
            value["metrics"]
        )
    if "opt_out" in value:
        out["OptOut"] = value["opt_out"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "user" in value:
        import capo_pinpoint.types.endpoint_user

        out["User"] = capo_pinpoint.types.endpoint_user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> EndpointResponse:
    out: EndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("Address") is not None:
        out["address"] = data["Address"]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("Attributes") is not None:
        import capo_pinpoint.types.map_of_list_of__string

        out["attributes"] = capo_pinpoint.types.map_of_list_of__string.deserialize_json(
            data["Attributes"]
        )
    if data.get("ChannelType") is not None:
        import capo_pinpoint.types.channel_type

        out["channel_type"] = capo_pinpoint.types.channel_type.deserialize_json(
            data["ChannelType"]
        )
    if data.get("CohortId") is not None:
        out["cohort_id"] = data["CohortId"]
    if data.get("CreationDate") is not None:
        out["creation_date"] = data["CreationDate"]
    if data.get("Demographic") is not None:
        import capo_pinpoint.types.endpoint_demographic

        out["demographic"] = capo_pinpoint.types.endpoint_demographic.deserialize_json(
            data["Demographic"]
        )
    if data.get("EffectiveDate") is not None:
        out["effective_date"] = data["EffectiveDate"]
    if data.get("EndpointStatus") is not None:
        out["endpoint_status"] = data["EndpointStatus"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Location") is not None:
        import capo_pinpoint.types.endpoint_location

        out["location"] = capo_pinpoint.types.endpoint_location.deserialize_json(
            data["Location"]
        )
    if data.get("Metrics") is not None:
        import capo_pinpoint.types.map_of__double

        out["metrics"] = capo_pinpoint.types.map_of__double.deserialize_json(
            data["Metrics"]
        )
    if data.get("OptOut") is not None:
        out["opt_out"] = data["OptOut"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("User") is not None:
        import capo_pinpoint.types.endpoint_user

        out["user"] = capo_pinpoint.types.endpoint_user.deserialize_json(data["User"])
    return out
