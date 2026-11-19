"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#RunInstancesMonitoringEnabled``."""

from typing_extensions import NotRequired, TypedDict


class RunInstancesMonitoringEnabled(TypedDict, closed=True):
    enabled: NotRequired["bool"]
    """<p>Enables or disables detailed instance monitoring.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RunInstancesMonitoringEnabled) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RunInstancesMonitoringEnabled:
    out: RunInstancesMonitoringEnabled = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RunInstancesMonitoringEnabled) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_cbor(data: dict) -> RunInstancesMonitoringEnabled:
    out: RunInstancesMonitoringEnabled = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    return out
