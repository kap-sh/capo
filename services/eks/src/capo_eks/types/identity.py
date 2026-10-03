"""Generated from Smithy shape ``com.amazonaws.eks#Identity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.oidc


class Identity(TypedDict, closed=True):
    oidc: NotRequired["capo_eks.types.oidc.OIDC"]
    """<p>An object representing the <a href="https://openid.net/connect/">OpenID Connect</a> identity provider information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Identity) -> dict:
    out: dict = {}
    if "oidc" in value:
        import capo_eks.types.oidc

        out["oidc"] = capo_eks.types.oidc.serialize_json(value["oidc"])
    return out


def deserialize_json(data: dict) -> Identity:
    out: Identity = {}  # type: ignore[typeddict-item]
    if data.get("oidc") is not None:
        import capo_eks.types.oidc

        out["oidc"] = capo_eks.types.oidc.deserialize_json(data["oidc"])
    return out
