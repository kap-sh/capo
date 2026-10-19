"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceInstancesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.next_token
    import capo_proton.types.service_instance_summary_list


class ListServiceInstancesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next service instance in the array of service instances, after the current requested list of service instances.</p>"""
    service_instances: (
        "capo_proton.types.service_instance_summary_list.ServiceInstanceSummaryList"
    )
    """<p>An array of service instances with summary data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceInstancesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.service_instance_summary_list

    out["serviceInstances"] = (
        capo_proton.types.service_instance_summary_list.serialize_aws_json_1_0(
            value["service_instances"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceInstancesOutput:
    out: ListServiceInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("serviceInstances") is not None:
        import capo_proton.types.service_instance_summary_list

        out["service_instances"] = (
            capo_proton.types.service_instance_summary_list.deserialize_aws_json_1_0(
                data["serviceInstances"]
            )
        )
    else:
        out["service_instances"] = []
    return out


def redact_sensitive(value: ListServiceInstancesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service_instances" in value:
        import capo_proton.types.service_instance_summary_list

        out["service_instances"] = (
            capo_proton.types.service_instance_summary_list.redact_sensitive(
                value["service_instances"]
            )
        )
    return out
