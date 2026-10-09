"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.ack_config_response
    import capo_eks.types.argo_cd_config_response


class CapabilityConfigurationResponse(TypedDict, closed=True):
    argo_cd: NotRequired["capo_eks.types.argo_cd_config_response.ArgoCdConfigResponse"]
    """<p>Configuration settings for an Argo CD capability, including the server URL and other Argo CD-specific settings.</p>"""
    ack: NotRequired["capo_eks.types.ack_config_response.AckConfigResponse"]
    """<p>Configuration settings for an ACK (Amazon Web Services Controllers for Kubernetes) capability, including the cross-namespace reference setting and the list of disabled services.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityConfigurationResponse) -> dict:
    out: dict = {}
    if "argo_cd" in value:
        import capo_eks.types.argo_cd_config_response

        out["argoCd"] = capo_eks.types.argo_cd_config_response.serialize_json(
            value["argo_cd"]
        )
    if "ack" in value:
        import capo_eks.types.ack_config_response

        out["ack"] = capo_eks.types.ack_config_response.serialize_json(value["ack"])
    return out


def deserialize_json(data: dict) -> CapabilityConfigurationResponse:
    out: CapabilityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("argoCd") is not None:
        import capo_eks.types.argo_cd_config_response

        out["argo_cd"] = capo_eks.types.argo_cd_config_response.deserialize_json(
            data["argoCd"]
        )
    if data.get("ack") is not None:
        import capo_eks.types.ack_config_response

        out["ack"] = capo_eks.types.ack_config_response.deserialize_json(data["ack"])
    return out
