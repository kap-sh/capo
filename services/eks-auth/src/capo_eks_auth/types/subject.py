"""Generated from Smithy shape ``com.amazonaws.eksauth#Subject``."""

from typing_extensions import TypedDict


class Subject(TypedDict, closed=True):
    namespace: "str"
    """<p>The name of the Kubernetes namespace inside the cluster to create the association in. The service account and the pods that use the service account must be in this namespace.</p>"""
    service_account: "str"
    """<p>The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Subject) -> dict:
    out: dict = {}
    out["namespace"] = value["namespace"]
    out["serviceAccount"] = value["service_account"]
    return out


def deserialize_json(data: dict) -> Subject:
    out: Subject = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        out["namespace"] = ""
    if data.get("serviceAccount") is not None:
        out["service_account"] = data["serviceAccount"]
    else:
        out["service_account"] = ""
    return out
