"""Generated from Smithy shape ``com.amazonaws.qapps#PermissionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.action
    import capo_qapps.types.principal_output


class PermissionOutput(TypedDict, closed=True):
    action: "capo_qapps.types.action.Action"
    """<p>The action associated with the permission.</p>"""
    principal: "capo_qapps.types.principal_output.PrincipalOutput"
    """<p>The principal user to which the permission applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionOutput) -> dict:
    out: dict = {}
    import capo_qapps.types.action

    out["action"] = capo_qapps.types.action.serialize_json(value["action"])
    import capo_qapps.types.principal_output

    out["principal"] = capo_qapps.types.principal_output.serialize_json(
        value["principal"]
    )
    return out


def deserialize_json(data: dict) -> PermissionOutput:
    out: PermissionOutput = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_qapps.types.action

        out["action"] = capo_qapps.types.action.deserialize_json(data["action"])
    else:
        import typing

        out["action"] = typing.cast("capo_qapps.types.action.Action", "")
    if data.get("principal") is not None:
        import capo_qapps.types.principal_output

        out["principal"] = capo_qapps.types.principal_output.deserialize_json(
            data["principal"]
        )
    else:
        raise DeserializationError("PermissionOutput.principal required")
    return out
