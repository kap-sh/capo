"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ChangeEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.attributes
    import capo_application_signals.types.aws_account_id
    import capo_application_signals.types.change_event_type


class ChangeEvent(TypedDict, closed=True):
    timestamp: "datetime.datetime"
    """<p>The timestamp when this change event occurred. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.</p>"""
    account_id: "capo_application_signals.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID where this change event occurred.</p>"""
    region: "str"
    """<p>The Amazon Web Services region where this change event occurred.</p>"""
    entity: "capo_application_signals.types.attributes.Attributes"
    """<p>The entity (service or resource) that was affected by this change event, including its key attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> <li> <p> <code>AwsAccountId</code> specifies the account where this object is in.</p> </li> </ul> <p>Below is an example of a service.</p> <p> <code>{ "Type": "Service", "Name": "visits-service", "Environment": "petclinic-test" }</code> </p> <p>Below is an example of a resource.</p> <p> <code>{ "Type": "AWS::Resource", "ResourceType": "AWS::DynamoDB::Table", "Identifier": "Customers" }</code> </p>"""
    change_event_type: (
        "capo_application_signals.types.change_event_type.ChangeEventType"
    )
    """<p>The type of change event that occurred, such as <code>DEPLOYMENT</code>.</p>"""
    event_id: "str"
    """<p>A unique identifier for this change event. For CloudTrail-based events, this is the CloudTrail event id. For other events, this will be <code>Unknown</code>.</p>"""
    user_name: NotRequired["str"]
    """<p>The name of the user who initiated this change event, if available.</p>"""
    event_name: NotRequired["str"]
    """<p>The name or description of this change event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeEvent) -> dict:
    out: dict = {}
    import capo_application_signals.types._prelude.timestamp

    out["Timestamp"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    out["AccountId"] = value["account_id"]
    out["Region"] = value["region"]
    import capo_application_signals.types.attributes

    out["Entity"] = capo_application_signals.types.attributes.serialize_json(
        value["entity"]
    )
    import capo_application_signals.types.change_event_type

    out["ChangeEventType"] = (
        capo_application_signals.types.change_event_type.serialize_json(
            value["change_event_type"]
        )
    )
    out["EventId"] = value["event_id"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "event_name" in value:
        out["EventName"] = value["event_name"]
    return out


def deserialize_json(data: dict) -> ChangeEvent:
    out: ChangeEvent = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["timestamp"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["Timestamp"]
            )
        )
    else:
        raise DeserializationError("ChangeEvent.timestamp required")
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("ChangeEvent.account_id required")
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("ChangeEvent.region required")
    if data.get("Entity") is not None:
        import capo_application_signals.types.attributes

        out["entity"] = capo_application_signals.types.attributes.deserialize_json(
            data["Entity"]
        )
    else:
        raise DeserializationError("ChangeEvent.entity required")
    if data.get("ChangeEventType") is not None:
        import capo_application_signals.types.change_event_type

        out["change_event_type"] = (
            capo_application_signals.types.change_event_type.deserialize_json(
                data["ChangeEventType"]
            )
        )
    else:
        raise DeserializationError("ChangeEvent.change_event_type required")
    if data.get("EventId") is not None:
        out["event_id"] = data["EventId"]
    else:
        raise DeserializationError("ChangeEvent.event_id required")
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("EventName") is not None:
        out["event_name"] = data["EventName"]
    return out
