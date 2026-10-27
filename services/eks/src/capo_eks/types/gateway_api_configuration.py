"""Generated from Smithy shape ``com.amazonaws.eks#GatewayApiConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.crd_management_configuration


class GatewayApiConfiguration(TypedDict, closed=True):
    crds: NotRequired[
        "capo_eks.types.crd_management_configuration.CrdManagementConfiguration"
    ]
    """<p>Indicates the current configuration of Gateway API custom resource definition (CRD) management on your EKS Auto Mode cluster. For example, if CRD management is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayApiConfiguration) -> dict:
    out: dict = {}
    if "crds" in value:
        import capo_eks.types.crd_management_configuration

        out["crds"] = capo_eks.types.crd_management_configuration.serialize_json(
            value["crds"]
        )
    return out


def deserialize_json(data: dict) -> GatewayApiConfiguration:
    out: GatewayApiConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("crds") is not None:
        import capo_eks.types.crd_management_configuration

        out["crds"] = capo_eks.types.crd_management_configuration.deserialize_json(
            data["crds"]
        )
    return out
