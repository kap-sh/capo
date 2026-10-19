"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#KubernetesResourceType``."""

from typing_extensions import TypedDict


class KubernetesResourceType(TypedDict, closed=True):
    api_version: "str"
    """<p>The API version type for the Kubernetes resource.</p>"""
    kind: "str"
    """<p>The kind for the Kubernetes resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KubernetesResourceType) -> dict:
    out: dict = {}
    out["apiVersion"] = value["api_version"]
    out["kind"] = value["kind"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KubernetesResourceType:
    out: KubernetesResourceType = {}  # type: ignore[typeddict-item]
    if data.get("apiVersion") is not None:
        out["api_version"] = data["apiVersion"]
    else:
        out["api_version"] = ""
    if data.get("kind") is not None:
        out["kind"] = data["kind"]
    else:
        out["kind"] = ""
    return out
