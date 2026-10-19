"""Generated from Smithy shape ``com.amazonaws.applicationinsights#AddWorkloadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_insights.types.component_name
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.workload_configuration


class AddWorkloadRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: "capo_application_insights.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    workload_configuration: (
        "capo_application_insights.types.workload_configuration.WorkloadConfiguration"
    )
    """<p>The configuration settings of the workload. The value is the escaped JSON of the configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddWorkloadRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    import capo_application_insights.types.workload_configuration

    out["WorkloadConfiguration"] = (
        capo_application_insights.types.workload_configuration.serialize_aws_json_1_1(
            value["workload_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddWorkloadRequest:
    out: AddWorkloadRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        out["resource_group_name"] = ""
    if data.get("ComponentName") is not None:
        out["component_name"] = data["ComponentName"]
    else:
        out["component_name"] = ""
    if data.get("WorkloadConfiguration") is not None:
        import capo_application_insights.types.workload_configuration

        out["workload_configuration"] = (
            capo_application_insights.types.workload_configuration.deserialize_aws_json_1_1(
                data["WorkloadConfiguration"]
            )
        )
    else:
        raise DeserializationError("AddWorkloadRequest.workload_configuration required")
    return out
