"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ApplicationComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.component_name
    import capo_application_insights.types.detected_workload
    import capo_application_insights.types.monitor
    import capo_application_insights.types.os_type
    import capo_application_insights.types.remarks
    import capo_application_insights.types.resource_type
    import capo_application_insights.types.tier


class ApplicationComponent(TypedDict, closed=True):
    component_name: NotRequired[
        "capo_application_insights.types.component_name.ComponentName"
    ]
    """<p>The name of the component.</p>"""
    component_remarks: NotRequired["capo_application_insights.types.remarks.Remarks"]
    """<p> If logging is supported for the resource type, indicates whether the component has configured logs to be monitored. </p>"""
    resource_type: NotRequired[
        "capo_application_insights.types.resource_type.ResourceType"
    ]
    """<p>The resource type. Supported resource types include EC2 instances, Auto Scaling group, Classic ELB, Application ELB, and SQS Queue.</p>"""
    os_type: NotRequired["capo_application_insights.types.os_type.OsType"]
    """<p> The operating system of the component. </p>"""
    tier: NotRequired["capo_application_insights.types.tier.Tier"]
    """<p>The stack tier of the application component.</p>"""
    monitor: NotRequired["capo_application_insights.types.monitor.Monitor"]
    """<p>Indicates whether the application component is monitored. </p>"""
    detected_workload: NotRequired[
        "capo_application_insights.types.detected_workload.DetectedWorkload"
    ]
    """<p> Workloads detected in the application component. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationComponent) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["ComponentName"] = value["component_name"]
    if "component_remarks" in value:
        out["ComponentRemarks"] = value["component_remarks"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "os_type" in value:
        import capo_application_insights.types.os_type

        out["OsType"] = capo_application_insights.types.os_type.serialize_aws_json_1_1(
            value["os_type"]
        )
    if "tier" in value:
        import capo_application_insights.types.tier

        out["Tier"] = capo_application_insights.types.tier.serialize_aws_json_1_1(
            value["tier"]
        )
    if "monitor" in value:
        out["Monitor"] = value["monitor"]
    if "detected_workload" in value:
        import capo_application_insights.types.detected_workload

        out["DetectedWorkload"] = (
            capo_application_insights.types.detected_workload.serialize_aws_json_1_1(
                value["detected_workload"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationComponent:
    out: ApplicationComponent = {}  # type: ignore[typeddict-item]
    if data.get("ComponentName") is not None:
        out["component_name"] = data["ComponentName"]
    if data.get("ComponentRemarks") is not None:
        out["component_remarks"] = data["ComponentRemarks"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("OsType") is not None:
        import capo_application_insights.types.os_type

        out["os_type"] = (
            capo_application_insights.types.os_type.deserialize_aws_json_1_1(
                data["OsType"]
            )
        )
    if data.get("Tier") is not None:
        import capo_application_insights.types.tier

        out["tier"] = capo_application_insights.types.tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    if data.get("Monitor") is not None:
        out["monitor"] = data["Monitor"]
    if data.get("DetectedWorkload") is not None:
        import capo_application_insights.types.detected_workload

        out["detected_workload"] = (
            capo_application_insights.types.detected_workload.deserialize_aws_json_1_1(
                data["DetectedWorkload"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApplicationComponent) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["ComponentName"] = value["component_name"]
    if "component_remarks" in value:
        out["ComponentRemarks"] = value["component_remarks"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "os_type" in value:
        import capo_application_insights.types.os_type

        out["OsType"] = capo_application_insights.types.os_type.serialize_cbor(
            value["os_type"]
        )
    if "tier" in value:
        import capo_application_insights.types.tier

        out["Tier"] = capo_application_insights.types.tier.serialize_cbor(value["tier"])
    if "monitor" in value:
        out["Monitor"] = value["monitor"]
    if "detected_workload" in value:
        import capo_application_insights.types.detected_workload

        out["DetectedWorkload"] = (
            capo_application_insights.types.detected_workload.serialize_cbor(
                value["detected_workload"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ApplicationComponent:
    out: ApplicationComponent = {}  # type: ignore[typeddict-item]
    if data.get("ComponentName") is not None:
        out["component_name"] = data["ComponentName"]
    if data.get("ComponentRemarks") is not None:
        out["component_remarks"] = data["ComponentRemarks"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("OsType") is not None:
        import capo_application_insights.types.os_type

        out["os_type"] = capo_application_insights.types.os_type.deserialize_cbor(
            data["OsType"]
        )
    if data.get("Tier") is not None:
        import capo_application_insights.types.tier

        out["tier"] = capo_application_insights.types.tier.deserialize_cbor(
            data["Tier"]
        )
    if data.get("Monitor") is not None:
        out["monitor"] = data["Monitor"]
    if data.get("DetectedWorkload") is not None:
        import capo_application_insights.types.detected_workload

        out["detected_workload"] = (
            capo_application_insights.types.detected_workload.deserialize_cbor(
                data["DetectedWorkload"]
            )
        )
    return out
