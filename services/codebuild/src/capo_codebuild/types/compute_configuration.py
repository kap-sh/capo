"""Generated from Smithy shape ``com.amazonaws.codebuild#ComputeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.machine_type
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.wrapper_long


class ComputeConfiguration(TypedDict, closed=True):
    v_cpu: NotRequired["capo_codebuild.types.wrapper_long.WrapperLong"]
    """<p>The number of vCPUs of the instance type included in your fleet.</p>"""
    memory: NotRequired["capo_codebuild.types.wrapper_long.WrapperLong"]
    """<p>The amount of memory of the instance type included in your fleet.</p>"""
    disk: NotRequired["capo_codebuild.types.wrapper_long.WrapperLong"]
    """<p>The amount of disk space of the instance type included in your fleet.</p>"""
    machine_type: NotRequired["capo_codebuild.types.machine_type.MachineType"]
    """<p>The machine type of the instance type included in your fleet.</p>"""
    instance_type: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The EC2 instance type to be launched in your fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeConfiguration) -> dict:
    out: dict = {}
    if "v_cpu" in value:
        out["vCpu"] = value["v_cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "disk" in value:
        out["disk"] = value["disk"]
    if "machine_type" in value:
        import capo_codebuild.types.machine_type

        out["machineType"] = capo_codebuild.types.machine_type.serialize_aws_json_1_1(
            value["machine_type"]
        )
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeConfiguration:
    out: ComputeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("vCpu") is not None:
        out["v_cpu"] = data["vCpu"]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("disk") is not None:
        out["disk"] = data["disk"]
    if data.get("machineType") is not None:
        import capo_codebuild.types.machine_type

        out["machine_type"] = (
            capo_codebuild.types.machine_type.deserialize_aws_json_1_1(
                data["machineType"]
            )
        )
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComputeConfiguration) -> dict:
    out: dict = {}
    if "v_cpu" in value:
        out["vCpu"] = value["v_cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "disk" in value:
        out["disk"] = value["disk"]
    if "machine_type" in value:
        import capo_codebuild.types.machine_type

        out["machineType"] = capo_codebuild.types.machine_type.serialize_cbor(
            value["machine_type"]
        )
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    return out


def deserialize_cbor(data: dict) -> ComputeConfiguration:
    out: ComputeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("vCpu") is not None:
        out["v_cpu"] = data["vCpu"]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("disk") is not None:
        out["disk"] = data["disk"]
    if data.get("machineType") is not None:
        import capo_codebuild.types.machine_type

        out["machine_type"] = capo_codebuild.types.machine_type.deserialize_cbor(
            data["machineType"]
        )
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    return out
