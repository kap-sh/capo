"""Generated from Smithy shape ``com.amazonaws.qapps#PermissionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.action


class PermissionInput(TypedDict, closed=True):
    action: "capo_qapps.types.action.Action"
    """<p>The action associated with the permission.</p>"""
    principal: "str"
    """<p>The principal user to which the permission applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionInput) -> dict:
    out: dict = {}
    import capo_qapps.types.action

    out["action"] = capo_qapps.types.action.serialize_json(value["action"])
    out["principal"] = value["principal"]
    return out


def deserialize_json(data: dict) -> PermissionInput:
    out: PermissionInput = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_qapps.types.action

        out["action"] = capo_qapps.types.action.deserialize_json(data["action"])
    else:
        import typing

        out["action"] = typing.cast("capo_qapps.types.action.Action", "")
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    else:
        out["principal"] = ""
    return out
