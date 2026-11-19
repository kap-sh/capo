"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.event_actionability
    import capo_health.types.event_arn
    import capo_health.types.event_persona_list
    import capo_health.types.event_scope_code
    import capo_health.types.event_status_code
    import capo_health.types.event_type_category
    import capo_health.types.event_type_code
    import capo_health.types.region
    import capo_health.types.service
    import capo_health.types.timestamp


class OrganizationEvent(TypedDict, closed=True):
    arn: NotRequired["capo_health.types.event_arn.eventArn"]
    """<p>The unique identifier for the event. The event ARN has the <code>arn:aws:health:<i>event-region</i>::event/<i>SERVICE</i>/<i>EVENT_TYPE_CODE</i>/<i>EVENT_TYPE_PLUS_ID</i> </code> format.</p> <p>For example, an event ARN might look like the following:</p> <p> <code>arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456</code> </p>"""
    service: NotRequired["capo_health.types.service.service"]
    """<p>The Amazon Web Services service that is affected by the event, such as EC2 and RDS.</p>"""
    event_type_code: NotRequired["capo_health.types.event_type_code.eventTypeCode"]
    """<p>The unique identifier for the event type. The format is <code>AWS_SERVICE_DESCRIPTION</code>. For example, <code>AWS_EC2_SYSTEM_MAINTENANCE_EVENT</code>.</p>"""
    event_type_category: NotRequired[
        "capo_health.types.event_type_category.eventTypeCategory"
    ]
    """<p>A list of event type category codes. Possible values are <code>issue</code>, <code>accountNotification</code>, or <code>scheduledChange</code>. Currently, the <code>investigation</code> value isn't supported at this time.</p>"""
    event_scope_code: NotRequired["capo_health.types.event_scope_code.eventScopeCode"]
    """<p>This parameter specifies if the Health event is a public Amazon Web Services service event or an account-specific event.</p> <ul> <li> <p>If the <code>eventScopeCode</code> value is <code>PUBLIC</code>, then the <code>affectedAccounts</code> value is always empty.</p> </li> <li> <p>If the <code>eventScopeCode</code> value is <code>ACCOUNT_SPECIFIC</code>, then the <code>affectedAccounts</code> value lists the affected Amazon Web Services accounts in your organization. For example, if an event affects a service such as Amazon Elastic Compute Cloud and you have Amazon Web Services accounts that use that service, those account IDs appear in the response.</p> </li> <li> <p>If the <code>eventScopeCode</code> value is <code>NONE</code>, then the <code>eventArn</code> that you specified in the request is invalid or doesn't exist.</p> </li> </ul>"""
    region: NotRequired["capo_health.types.region.region"]
    """<p>The Amazon Web Services Region name of the event.</p>"""
    start_time: NotRequired["capo_health.types.timestamp.timestamp"]
    """<p>The date and time that the event began.</p>"""
    end_time: NotRequired["capo_health.types.timestamp.timestamp"]
    """<p>The date and time that the event ended.</p>"""
    last_updated_time: NotRequired["capo_health.types.timestamp.timestamp"]
    """<p>The most recent date and time that the event was updated.</p>"""
    status_code: NotRequired["capo_health.types.event_status_code.eventStatusCode"]
    """<p>The most recent status of the event. Possible values are <code>open</code>, <code>closed</code>, and <code>upcoming</code>.</p>"""
    actionability: NotRequired[
        "capo_health.types.event_actionability.EventActionability"
    ]
    """<p>The actionability classification of the event. Possible values are <code>ACTION_REQUIRED</code>, <code>ACTION_MAY_BE_REQUIRED</code> and <code>INFORMATIONAL</code>. Events with <code>ACTION_REQUIRED</code> actionability require customer action to resolve or mitigate the event. Events with <code>ACTION_MAY_BE_REQUIRED</code> actionability indicates that the current status is unknown or conditional and inspection is needed to determine if action is required. Events with <code>INFORMATIONAL</code> actionability are provided for awareness and do not require immediate action.</p>"""
    personas: NotRequired["capo_health.types.event_persona_list.EventPersonaList"]
    """<p>A list of persona classifications that indicate the target audience for the event. Possible values are <code>OPERATIONS</code>, <code>SECURITY</code>, and <code>BILLING</code>. Events can be associated with multiple personas to indicate relevance to different teams or roles within an organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEvent) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "service" in value:
        out["service"] = value["service"]
    if "event_type_code" in value:
        out["eventTypeCode"] = value["event_type_code"]
    if "event_type_category" in value:
        import capo_health.types.event_type_category

        out["eventTypeCategory"] = (
            capo_health.types.event_type_category.serialize_aws_json_1_1(
                value["event_type_category"]
            )
        )
    if "event_scope_code" in value:
        import capo_health.types.event_scope_code

        out["eventScopeCode"] = (
            capo_health.types.event_scope_code.serialize_aws_json_1_1(
                value["event_scope_code"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "start_time" in value:
        import capo_health.types.timestamp

        out["startTime"] = capo_health.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_health.types.timestamp

        out["endTime"] = capo_health.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "last_updated_time" in value:
        import capo_health.types.timestamp

        out["lastUpdatedTime"] = capo_health.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    if "status_code" in value:
        import capo_health.types.event_status_code

        out["statusCode"] = capo_health.types.event_status_code.serialize_aws_json_1_1(
            value["status_code"]
        )
    if "actionability" in value:
        import capo_health.types.event_actionability

        out["actionability"] = (
            capo_health.types.event_actionability.serialize_aws_json_1_1(
                value["actionability"]
            )
        )
    if "personas" in value:
        import capo_health.types.event_persona_list

        out["personas"] = capo_health.types.event_persona_list.serialize_aws_json_1_1(
            value["personas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationEvent:
    out: OrganizationEvent = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("eventTypeCode") is not None:
        out["event_type_code"] = data["eventTypeCode"]
    if data.get("eventTypeCategory") is not None:
        import capo_health.types.event_type_category

        out["event_type_category"] = (
            capo_health.types.event_type_category.deserialize_aws_json_1_1(
                data["eventTypeCategory"]
            )
        )
    if data.get("eventScopeCode") is not None:
        import capo_health.types.event_scope_code

        out["event_scope_code"] = (
            capo_health.types.event_scope_code.deserialize_aws_json_1_1(
                data["eventScopeCode"]
            )
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("startTime") is not None:
        import capo_health.types.timestamp

        out["start_time"] = capo_health.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_health.types.timestamp

        out["end_time"] = capo_health.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if data.get("lastUpdatedTime") is not None:
        import capo_health.types.timestamp

        out["last_updated_time"] = capo_health.types.timestamp.deserialize_aws_json_1_1(
            data["lastUpdatedTime"]
        )
    if data.get("statusCode") is not None:
        import capo_health.types.event_status_code

        out["status_code"] = (
            capo_health.types.event_status_code.deserialize_aws_json_1_1(
                data["statusCode"]
            )
        )
    if data.get("actionability") is not None:
        import capo_health.types.event_actionability

        out["actionability"] = (
            capo_health.types.event_actionability.deserialize_aws_json_1_1(
                data["actionability"]
            )
        )
    if data.get("personas") is not None:
        import capo_health.types.event_persona_list

        out["personas"] = capo_health.types.event_persona_list.deserialize_aws_json_1_1(
            data["personas"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationEvent) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "service" in value:
        out["service"] = value["service"]
    if "event_type_code" in value:
        out["eventTypeCode"] = value["event_type_code"]
    if "event_type_category" in value:
        import capo_health.types.event_type_category

        out["eventTypeCategory"] = capo_health.types.event_type_category.serialize_cbor(
            value["event_type_category"]
        )
    if "event_scope_code" in value:
        import capo_health.types.event_scope_code

        out["eventScopeCode"] = capo_health.types.event_scope_code.serialize_cbor(
            value["event_scope_code"]
        )
    if "region" in value:
        out["region"] = value["region"]
    if "start_time" in value:
        import capo_health.types.timestamp

        out["startTime"] = capo_health.types.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_health.types.timestamp

        out["endTime"] = capo_health.types.timestamp.serialize_cbor(value["end_time"])
    if "last_updated_time" in value:
        import capo_health.types.timestamp

        out["lastUpdatedTime"] = capo_health.types.timestamp.serialize_cbor(
            value["last_updated_time"]
        )
    if "status_code" in value:
        import capo_health.types.event_status_code

        out["statusCode"] = capo_health.types.event_status_code.serialize_cbor(
            value["status_code"]
        )
    if "actionability" in value:
        import capo_health.types.event_actionability

        out["actionability"] = capo_health.types.event_actionability.serialize_cbor(
            value["actionability"]
        )
    if "personas" in value:
        import capo_health.types.event_persona_list

        out["personas"] = capo_health.types.event_persona_list.serialize_cbor(
            value["personas"]
        )
    return out


def deserialize_cbor(data: dict) -> OrganizationEvent:
    out: OrganizationEvent = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("eventTypeCode") is not None:
        out["event_type_code"] = data["eventTypeCode"]
    if data.get("eventTypeCategory") is not None:
        import capo_health.types.event_type_category

        out["event_type_category"] = (
            capo_health.types.event_type_category.deserialize_cbor(
                data["eventTypeCategory"]
            )
        )
    if data.get("eventScopeCode") is not None:
        import capo_health.types.event_scope_code

        out["event_scope_code"] = capo_health.types.event_scope_code.deserialize_cbor(
            data["eventScopeCode"]
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("startTime") is not None:
        import capo_health.types.timestamp

        out["start_time"] = capo_health.types.timestamp.deserialize_cbor(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_health.types.timestamp

        out["end_time"] = capo_health.types.timestamp.deserialize_cbor(data["endTime"])
    if data.get("lastUpdatedTime") is not None:
        import capo_health.types.timestamp

        out["last_updated_time"] = capo_health.types.timestamp.deserialize_cbor(
            data["lastUpdatedTime"]
        )
    if data.get("statusCode") is not None:
        import capo_health.types.event_status_code

        out["status_code"] = capo_health.types.event_status_code.deserialize_cbor(
            data["statusCode"]
        )
    if data.get("actionability") is not None:
        import capo_health.types.event_actionability

        out["actionability"] = capo_health.types.event_actionability.deserialize_cbor(
            data["actionability"]
        )
    if data.get("personas") is not None:
        import capo_health.types.event_persona_list

        out["personas"] = capo_health.types.event_persona_list.deserialize_cbor(
            data["personas"]
        )
    return out
