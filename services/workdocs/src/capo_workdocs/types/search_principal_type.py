"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchPrincipalType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.id_type
    import capo_workdocs.types.search_principal_role_list


class SearchPrincipalType(TypedDict, closed=True):
    id: "capo_workdocs.types.id_type.IdType"
    """<p>UserIds or GroupIds.</p>"""
    roles: NotRequired[
        "capo_workdocs.types.search_principal_role_list.SearchPrincipalRoleList"
    ]
    """<p>The Role of a User or Group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPrincipalType) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "roles" in value:
        import capo_workdocs.types.search_principal_role_list

        out["Roles"] = capo_workdocs.types.search_principal_role_list.serialize_json(
            value["roles"]
        )
    return out


def deserialize_json(data: dict) -> SearchPrincipalType:
    out: SearchPrincipalType = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Roles") is not None:
        import capo_workdocs.types.search_principal_role_list

        out["roles"] = capo_workdocs.types.search_principal_role_list.deserialize_json(
            data["Roles"]
        )
    return out
