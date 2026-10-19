"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetEndpointAccessRequest``."""

from typing_extensions import TypedDict


class GetEndpointAccessRequest(TypedDict, closed=True):
    endpoint_name: "str"
    """<p>The name of the VPC endpoint to return information for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEndpointAccessRequest) -> dict:
    out: dict = {}
    out["endpointName"] = value["endpoint_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEndpointAccessRequest:
    out: GetEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
    else:
        out["endpoint_name"] = ""
    return out
