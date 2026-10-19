"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteEndpointAccessRequest``."""

from typing_extensions import TypedDict


class DeleteEndpointAccessRequest(TypedDict, closed=True):
    endpoint_name: "str"
    """<p>The name of the VPC endpoint to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEndpointAccessRequest) -> dict:
    out: dict = {}
    out["endpointName"] = value["endpoint_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEndpointAccessRequest:
    out: DeleteEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
    else:
        out["endpoint_name"] = ""
    return out
