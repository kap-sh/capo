"""Generated from Smithy shape ``com.amazonaws.glue#DeleteDevEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string


class DeleteDevEndpointRequest(TypedDict, closed=True):
    endpoint_name: "capo_glue.types.generic_string.GenericString"
    """<p>The name of the <code>DevEndpoint</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDevEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointName"] = value["endpoint_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDevEndpointRequest:
    out: DeleteDevEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    else:
        out["endpoint_name"] = ""
    return out
