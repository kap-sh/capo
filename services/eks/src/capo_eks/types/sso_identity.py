"""Generated from Smithy shape ``com.amazonaws.eks#SsoIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.sso_identity_type
    import capo_eks.types.string


class SsoIdentity(TypedDict, closed=True):
    id: "capo_eks.types.string.String"
    """<p>The unique identifier of the IAM Identity CenterIAM; Identity Center user or group.</p>"""
    type: "capo_eks.types.sso_identity_type.SsoIdentityType"
    """<p>The type of identity. Valid values are <code>SSO_USER</code> or <code>SSO_GROUP</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsoIdentity) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_eks.types.sso_identity_type

    out["type"] = capo_eks.types.sso_identity_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SsoIdentity:
    out: SsoIdentity = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        import capo_eks.types.sso_identity_type

        out["type"] = capo_eks.types.sso_identity_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast(
            "capo_eks.types.sso_identity_type.SsoIdentityType", ""
        )
    return out
