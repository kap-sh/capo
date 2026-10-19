"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEksWorkloadInfo``."""

from typing_extensions import TypedDict


class AwsEksWorkloadInfo(TypedDict, closed=True):
    name: "str"
    """<p>The name of the workload.</p>"""
    type: "str"
    """<p>The workload type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEksWorkloadInfo) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsEksWorkloadInfo:
    out: AwsEksWorkloadInfo = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
