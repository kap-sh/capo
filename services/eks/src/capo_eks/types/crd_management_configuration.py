"""Generated from Smithy shape ``com.amazonaws.eks#CrdManagementConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boxed_boolean


class CrdManagementConfiguration(TypedDict, closed=True):
    managed: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates if Gateway API CRD management is enabled on your EKS Auto Mode cluster. If CRD management is enabled, EKS Auto Mode will create and update the Gateway API CRDs in your EKS Auto Mode cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrdManagementConfiguration) -> dict:
    out: dict = {}
    if "managed" in value:
        out["managed"] = value["managed"]
    return out


def deserialize_json(data: dict) -> CrdManagementConfiguration:
    out: CrdManagementConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("managed") is not None:
        out["managed"] = data["managed"]
    return out
