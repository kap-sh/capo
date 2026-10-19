"""Generated from Smithy shape ``com.amazonaws.eks#IdentityProviderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class IdentityProviderConfig(TypedDict, closed=True):
    type: "capo_eks.types.string.String"
    """<p>The type of the identity provider configuration. The only type available is <code>oidc</code>.</p>"""
    name: "capo_eks.types.string.String"
    """<p>The name of the identity provider configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> IdentityProviderConfig:
    out: IdentityProviderConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
