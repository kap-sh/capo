"""Generated from Smithy shape ``com.amazonaws.workdocs#SharePrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.id_type
    import capo_workdocs.types.principal_type
    import capo_workdocs.types.role_type


class SharePrincipal(TypedDict, closed=True):
    id: "capo_workdocs.types.id_type.IdType"
    """<p>The ID of the recipient.</p>"""
    type: "capo_workdocs.types.principal_type.PrincipalType"
    """<p>The type of the recipient.</p>"""
    role: "capo_workdocs.types.role_type.RoleType"
    """<p>The role of the recipient.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharePrincipal) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_workdocs.types.principal_type

    out["Type"] = capo_workdocs.types.principal_type.serialize_json(value["type"])
    import capo_workdocs.types.role_type

    out["Role"] = capo_workdocs.types.role_type.serialize_json(value["role"])
    return out


def deserialize_json(data: dict) -> SharePrincipal:
    out: SharePrincipal = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Type") is not None:
        import capo_workdocs.types.principal_type

        out["type"] = capo_workdocs.types.principal_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast(
            "capo_workdocs.types.principal_type.PrincipalType", ""
        )
    if data.get("Role") is not None:
        import capo_workdocs.types.role_type

        out["role"] = capo_workdocs.types.role_type.deserialize_json(data["Role"])
    else:
        import typing

        out["role"] = typing.cast("capo_workdocs.types.role_type.RoleType", "")
    return out
