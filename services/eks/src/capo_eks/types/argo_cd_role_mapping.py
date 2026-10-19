"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdRoleMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.argo_cd_role
    import capo_eks.types.sso_identity_list


class ArgoCdRoleMapping(TypedDict, closed=True):
    role: "capo_eks.types.argo_cd_role.ArgoCdRole"
    """<p>The Argo CD role to assign. Valid values are:</p> <ul> <li> <p> <code>ADMIN</code> – Full administrative access to Argo CD.</p> </li> <li> <p> <code>EDITOR</code> – Edit access to Argo CD resources.</p> </li> <li> <p> <code>VIEWER</code> – Read-only access to Argo CD resources.</p> </li> </ul>"""
    identities: "capo_eks.types.sso_identity_list.SsoIdentityList"
    """<p>A list of IAM Identity CenterIAM; Identity Center identities (users or groups) that should be assigned this Argo CD role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdRoleMapping) -> dict:
    out: dict = {}
    import capo_eks.types.argo_cd_role

    out["role"] = capo_eks.types.argo_cd_role.serialize_json(value["role"])
    import capo_eks.types.sso_identity_list

    out["identities"] = capo_eks.types.sso_identity_list.serialize_json(
        value["identities"]
    )
    return out


def deserialize_json(data: dict) -> ArgoCdRoleMapping:
    out: ArgoCdRoleMapping = {}  # type: ignore[typeddict-item]
    if data.get("role") is not None:
        import capo_eks.types.argo_cd_role

        out["role"] = capo_eks.types.argo_cd_role.deserialize_json(data["role"])
    else:
        import typing

        out["role"] = typing.cast("capo_eks.types.argo_cd_role.ArgoCdRole", "")
    if data.get("identities") is not None:
        import capo_eks.types.sso_identity_list

        out["identities"] = capo_eks.types.sso_identity_list.deserialize_json(
            data["identities"]
        )
    else:
        out["identities"] = []
    return out
