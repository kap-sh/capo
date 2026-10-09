"""Generated from Smithy shape ``com.amazonaws.eks#UpdateCapabilityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.update_ack_config
    import capo_eks.types.update_argo_cd_config


class UpdateCapabilityConfiguration(TypedDict, closed=True):
    argo_cd: NotRequired["capo_eks.types.update_argo_cd_config.UpdateArgoCdConfig"]
    """<p>Configuration updates specific to Argo CD capabilities.</p>"""
    ack: NotRequired["capo_eks.types.update_ack_config.UpdateAckConfig"]
    """<p>Configuration updates specific to ACK (Amazon Web Services Controllers for Kubernetes) capabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCapabilityConfiguration) -> dict:
    out: dict = {}
    if "argo_cd" in value:
        import capo_eks.types.update_argo_cd_config

        out["argoCd"] = capo_eks.types.update_argo_cd_config.serialize_json(
            value["argo_cd"]
        )
    if "ack" in value:
        import capo_eks.types.update_ack_config

        out["ack"] = capo_eks.types.update_ack_config.serialize_json(value["ack"])
    return out


def deserialize_json(data: dict) -> UpdateCapabilityConfiguration:
    out: UpdateCapabilityConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("argoCd") is not None:
        import capo_eks.types.update_argo_cd_config

        out["argo_cd"] = capo_eks.types.update_argo_cd_config.deserialize_json(
            data["argoCd"]
        )
    if data.get("ack") is not None:
        import capo_eks.types.update_ack_config

        out["ack"] = capo_eks.types.update_ack_config.deserialize_json(data["ack"])
    return out
