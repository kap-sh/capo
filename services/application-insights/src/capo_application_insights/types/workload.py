"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Workload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.component_name
    import capo_application_insights.types.missing_workload_config
    import capo_application_insights.types.remarks
    import capo_application_insights.types.tier
    import capo_application_insights.types.workload_id
    import capo_application_insights.types.workload_name


class Workload(TypedDict, closed=True):
    workload_id: NotRequired["capo_application_insights.types.workload_id.WorkloadId"]
    """<p>The ID of the workload.</p>"""
    component_name: NotRequired[
        "capo_application_insights.types.component_name.ComponentName"
    ]
    """<p>The name of the component.</p>"""
    workload_name: NotRequired[
        "capo_application_insights.types.workload_name.WorkloadName"
    ]
    """<p>The name of the workload.</p>"""
    tier: NotRequired["capo_application_insights.types.tier.Tier"]
    """<p>The tier of the workload.</p>"""
    workload_remarks: NotRequired["capo_application_insights.types.remarks.Remarks"]
    """<p>If logging is supported for the resource type, shows whether the component has configured logs to be monitored.</p>"""
    missing_workload_config: NotRequired[
        "capo_application_insights.types.missing_workload_config.MissingWorkloadConfig"
    ]
    """<p>Indicates whether all of the component configurations required to monitor a workload were provided.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Workload) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "component_name" in value:
        out["ComponentName"] = value["component_name"]
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "tier" in value:
        import capo_application_insights.types.tier

        out["Tier"] = capo_application_insights.types.tier.serialize_aws_json_1_1(
            value["tier"]
        )
    if "workload_remarks" in value:
        out["WorkloadRemarks"] = value["workload_remarks"]
    if "missing_workload_config" in value:
        out["MissingWorkloadConfig"] = value["missing_workload_config"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Workload:
    out: Workload = {}  # type: ignore[typeddict-item]
    if data.get("WorkloadId") is not None:
        out["workload_id"] = data["WorkloadId"]
    if data.get("ComponentName") is not None:
        out["component_name"] = data["ComponentName"]
    if data.get("WorkloadName") is not None:
        out["workload_name"] = data["WorkloadName"]
    if data.get("Tier") is not None:
        import capo_application_insights.types.tier

        out["tier"] = capo_application_insights.types.tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    if data.get("WorkloadRemarks") is not None:
        out["workload_remarks"] = data["WorkloadRemarks"]
    if data.get("MissingWorkloadConfig") is not None:
        out["missing_workload_config"] = data["MissingWorkloadConfig"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Workload) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "component_name" in value:
        out["ComponentName"] = value["component_name"]
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "tier" in value:
        import capo_application_insights.types.tier

        out["Tier"] = capo_application_insights.types.tier.serialize_cbor(value["tier"])
    if "workload_remarks" in value:
        out["WorkloadRemarks"] = value["workload_remarks"]
    if "missing_workload_config" in value:
        out["MissingWorkloadConfig"] = value["missing_workload_config"]
    return out


def deserialize_cbor(data: dict) -> Workload:
    out: Workload = {}  # type: ignore[typeddict-item]
    if data.get("WorkloadId") is not None:
        out["workload_id"] = data["WorkloadId"]
    if data.get("ComponentName") is not None:
        out["component_name"] = data["ComponentName"]
    if data.get("WorkloadName") is not None:
        out["workload_name"] = data["WorkloadName"]
    if data.get("Tier") is not None:
        import capo_application_insights.types.tier

        out["tier"] = capo_application_insights.types.tier.deserialize_cbor(
            data["Tier"]
        )
    if data.get("WorkloadRemarks") is not None:
        out["workload_remarks"] = data["WorkloadRemarks"]
    if data.get("MissingWorkloadConfig") is not None:
        out["missing_workload_config"] = data["MissingWorkloadConfig"]
    return out
