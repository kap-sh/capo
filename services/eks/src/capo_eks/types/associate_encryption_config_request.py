"""Generated from Smithy shape ``com.amazonaws.eks#AssociateEncryptionConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.encryption_config_list
    import capo_eks.types.string


class AssociateEncryptionConfigRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    encryption_config: "capo_eks.types.encryption_config_list.EncryptionConfigList"
    """<p>The configuration you are using for encryption.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateEncryptionConfigRequest) -> dict:
    out: dict = {}
    import capo_eks.types.encryption_config_list

    out["encryptionConfig"] = capo_eks.types.encryption_config_list.serialize_json(
        value["encryption_config"]
    )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> AssociateEncryptionConfigRequest:
    out: AssociateEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("encryptionConfig") is not None:
        import capo_eks.types.encryption_config_list

        out["encryption_config"] = (
            capo_eks.types.encryption_config_list.deserialize_json(
                data["encryptionConfig"]
            )
        )
    else:
        out["encryption_config"] = []
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    return out
