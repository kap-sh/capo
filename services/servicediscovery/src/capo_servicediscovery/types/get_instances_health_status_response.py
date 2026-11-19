"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetInstancesHealthStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.instance_health_status_map
    import capo_servicediscovery.types.next_token


class GetInstancesHealthStatusResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_servicediscovery.types.instance_health_status_map.InstanceHealthStatusMap"
    ]
    """<p>A complex type that contains the IDs and the health status of the instances that you specified in the <code>GetInstancesHealthStatus</code> request.</p>"""
    next_token: NotRequired["capo_servicediscovery.types.next_token.NextToken"]
    """<p>If more than <code>MaxResults</code> instances match the specified criteria, you can submit another <code>GetInstancesHealthStatus</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstancesHealthStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_servicediscovery.types.instance_health_status_map

        out["Status"] = (
            capo_servicediscovery.types.instance_health_status_map.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstancesHealthStatusResponse:
    out: GetInstancesHealthStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_servicediscovery.types.instance_health_status_map

        out["status"] = (
            capo_servicediscovery.types.instance_health_status_map.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetInstancesHealthStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_servicediscovery.types.instance_health_status_map

        out["Status"] = (
            capo_servicediscovery.types.instance_health_status_map.serialize_cbor(
                value["status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> GetInstancesHealthStatusResponse:
    out: GetInstancesHealthStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_servicediscovery.types.instance_health_status_map

        out["status"] = (
            capo_servicediscovery.types.instance_health_status_map.deserialize_cbor(
                data["Status"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
