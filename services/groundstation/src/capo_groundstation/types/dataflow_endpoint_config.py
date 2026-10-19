"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowEndpointConfig``."""

from typing_extensions import NotRequired, TypedDict


class DataflowEndpointConfig(TypedDict, closed=True):
    dataflow_endpoint_name: "str"
    """<p>Name of a dataflow endpoint.</p>"""
    dataflow_endpoint_region: NotRequired["str"]
    """<p>Region of a dataflow endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataflowEndpointConfig) -> dict:
    out: dict = {}
    out["dataflowEndpointName"] = value["dataflow_endpoint_name"]
    if "dataflow_endpoint_region" in value:
        out["dataflowEndpointRegion"] = value["dataflow_endpoint_region"]
    return out


def deserialize_json(data: dict) -> DataflowEndpointConfig:
    out: DataflowEndpointConfig = {}  # type: ignore[typeddict-item]
    if data.get("dataflowEndpointName") is not None:
        out["dataflow_endpoint_name"] = data["dataflowEndpointName"]
    else:
        out["dataflow_endpoint_name"] = ""
    if data.get("dataflowEndpointRegion") is not None:
        out["dataflow_endpoint_region"] = data["dataflowEndpointRegion"]
    return out
