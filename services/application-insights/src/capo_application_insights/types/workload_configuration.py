"""Generated from Smithy shape ``com.amazonaws.applicationinsights#WorkloadConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.component_configuration
    import capo_application_insights.types.tier
    import capo_application_insights.types.workload_name


class WorkloadConfiguration(TypedDict, closed=True):
    workload_name: NotRequired[
        "capo_application_insights.types.workload_name.WorkloadName"
    ]
    """<p>The name of the workload.</p>"""
    tier: NotRequired["capo_application_insights.types.tier.Tier"]
    """<p>The configuration of the workload tier.</p>"""
    configuration: NotRequired[
        "capo_application_insights.types.component_configuration.ComponentConfiguration"
    ]
    """<p>The configuration settings of the workload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkloadConfiguration) -> dict:
    out: dict = {}
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "tier" in value:
        import capo_application_insights.types.tier

        out["Tier"] = capo_application_insights.types.tier.serialize_aws_json_1_1(
            value["tier"]
        )
    if "configuration" in value:
        out["Configuration"] = value["configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkloadConfiguration:
    out: WorkloadConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("WorkloadName") is not None:
        out["workload_name"] = data["WorkloadName"]
    if data.get("Tier") is not None:
        import capo_application_insights.types.tier

        out["tier"] = capo_application_insights.types.tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    if data.get("Configuration") is not None:
        out["configuration"] = data["Configuration"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkloadConfiguration) -> dict:
    out: dict = {}
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "tier" in value:
        import capo_application_insights.types.tier

        out["Tier"] = capo_application_insights.types.tier.serialize_cbor(value["tier"])
    if "configuration" in value:
        out["Configuration"] = value["configuration"]
    return out


def deserialize_cbor(data: dict) -> WorkloadConfiguration:
    out: WorkloadConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("WorkloadName") is not None:
        out["workload_name"] = data["WorkloadName"]
    if data.get("Tier") is not None:
        import capo_application_insights.types.tier

        out["tier"] = capo_application_insights.types.tier.deserialize_cbor(
            data["Tier"]
        )
    if data.get("Configuration") is not None:
        out["configuration"] = data["Configuration"]
    return out
