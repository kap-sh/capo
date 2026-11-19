"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EC2ManagedInstance``."""

from typing_extensions import NotRequired, TypedDict


class EC2ManagedInstance(TypedDict, closed=True):
    instance_id: NotRequired["str"]
    """<p>Unique identifier of the managed EC2 instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EC2ManagedInstance) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EC2ManagedInstance:
    out: EC2ManagedInstance = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2ManagedInstance) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    return out


def deserialize_cbor(data: dict) -> EC2ManagedInstance:
    out: EC2ManagedInstance = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    return out
