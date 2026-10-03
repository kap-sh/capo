"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetInstancesHealthStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.instance_id_list
    import capo_servicediscovery.types.max_results
    import capo_servicediscovery.types.next_token


class GetInstancesHealthStatusRequest(TypedDict, closed=True):
    service_id: "capo_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the service that the instance is associated with. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    instances: NotRequired[
        "capo_servicediscovery.types.instance_id_list.InstanceIdList"
    ]
    """<p>An array that contains the IDs of all the instances that you want to get the health status for.</p> <p>If you omit <code>Instances</code>, Cloud Map returns the health status for all the instances that are associated with the specified service.</p> <note> <p>To get the IDs for the instances that you've registered by using a specified service, submit a <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_ListInstances.html">ListInstances</a> request.</p> </note>"""
    max_results: NotRequired["capo_servicediscovery.types.max_results.MaxResults"]
    """<p>The maximum number of instances that you want Cloud Map to return in the response to a <code>GetInstancesHealthStatus</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 instances.</p>"""
    next_token: NotRequired["capo_servicediscovery.types.next_token.NextToken"]
    """<p>For the first <code>GetInstancesHealthStatus</code> request, omit this value.</p> <p>If more than <code>MaxResults</code> instances match the specified criteria, you can submit another <code>GetInstancesHealthStatus</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstancesHealthStatusRequest) -> dict:
    out: dict = {}
    out["ServiceId"] = value["service_id"]
    if "instances" in value:
        import capo_servicediscovery.types.instance_id_list

        out["Instances"] = (
            capo_servicediscovery.types.instance_id_list.serialize_aws_json_1_1(
                value["instances"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstancesHealthStatusRequest:
    out: GetInstancesHealthStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceId") is not None:
        out["service_id"] = data["ServiceId"]
    else:
        raise DeserializationError(
            "GetInstancesHealthStatusRequest.service_id required"
        )
    if data.get("Instances") is not None:
        import capo_servicediscovery.types.instance_id_list

        out["instances"] = (
            capo_servicediscovery.types.instance_id_list.deserialize_aws_json_1_1(
                data["Instances"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
