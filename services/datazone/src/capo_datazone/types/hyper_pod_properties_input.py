"""Generated from Smithy shape ``com.amazonaws.datazone#HyperPodPropertiesInput``."""

from typing_extensions import TypedDict


class HyperPodPropertiesInput(TypedDict, closed=True):
    cluster_name: "str"
    """<p>The cluster name the hyper pod properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HyperPodPropertiesInput) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    return out


def deserialize_json(data: dict) -> HyperPodPropertiesInput:
    out: HyperPodPropertiesInput = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    else:
        out["cluster_name"] = ""
    return out
