"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceOperationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.attributes
    import capo_application_signals.types.list_service_operation_max_results
    import capo_application_signals.types.next_token


class ListServiceOperationsInput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested end time will be rounded to the nearest hour.</p>"""
    key_attributes: "capo_application_signals.types.attributes.Attributes"
    """<p>Use this field to specify which service you want to retrieve information for. You must specify at least the <code>Type</code>, <code>Name</code>, and <code>Environment</code> attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_application_signals.types.list_service_operation_max_results.ListServiceOperationMaxResults"
    ]
    """<p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of service operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceOperationsInput) -> dict:
    out: dict = {}
    import capo_application_signals.types.attributes

    out["KeyAttributes"] = capo_application_signals.types.attributes.serialize_json(
        value["key_attributes"]
    )
    return out


def deserialize_json(data: dict) -> ListServiceOperationsInput:
    out: ListServiceOperationsInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyAttributes") is not None:
        import capo_application_signals.types.attributes

        out["key_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["KeyAttributes"]
            )
        )
    else:
        raise DeserializationError("ListServiceOperationsInput.key_attributes required")
    return out
