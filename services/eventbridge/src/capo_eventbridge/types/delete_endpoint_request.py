"""Generated from Smithy shape ``com.amazonaws.eventbridge#DeleteEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.endpoint_name


class DeleteEndpointRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint you want to delete. For example, <code>"Name":"us-east-2-custom_bus_A-endpoint"</code>..</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEndpointRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEndpointRequest:
    out: DeleteEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteEndpointRequest.name required")
    return out
