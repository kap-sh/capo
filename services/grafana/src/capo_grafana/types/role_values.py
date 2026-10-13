"""Generated from Smithy shape ``com.amazonaws.grafana#RoleValues``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.role_value_list


class RoleValues(TypedDict, closed=True):
    editor: NotRequired["capo_grafana.types.role_value_list.RoleValueList"]
    """<p>A list of groups from the SAML assertion attribute to grant the Grafana <code>Editor</code> role to.</p>"""
    admin: NotRequired["capo_grafana.types.role_value_list.RoleValueList"]
    """<p>A list of groups from the SAML assertion attribute to grant the Grafana <code>Admin</code> role to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoleValues) -> dict:
    out: dict = {}
    if "editor" in value:
        import capo_grafana.types.role_value_list

        out["editor"] = capo_grafana.types.role_value_list.serialize_json(
            value["editor"]
        )
    if "admin" in value:
        import capo_grafana.types.role_value_list

        out["admin"] = capo_grafana.types.role_value_list.serialize_json(value["admin"])
    return out


def deserialize_json(data: dict) -> RoleValues:
    out: RoleValues = {}  # type: ignore[typeddict-item]
    if data.get("editor") is not None:
        import capo_grafana.types.role_value_list

        out["editor"] = capo_grafana.types.role_value_list.deserialize_json(
            data["editor"]
        )
    if data.get("admin") is not None:
        import capo_grafana.types.role_value_list

        out["admin"] = capo_grafana.types.role_value_list.deserialize_json(
            data["admin"]
        )
    return out


def redact_sensitive(value: RoleValues) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "editor" in value:
        out["editor"] = "*** Sensitive Data Redacted ***"
    if "admin" in value:
        out["admin"] = "*** Sensitive Data Redacted ***"
    return out
