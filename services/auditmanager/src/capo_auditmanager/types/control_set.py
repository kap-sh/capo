"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlSet``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_set_name
    import capo_auditmanager.types.controls
    import capo_auditmanager.types.uuid


class ControlSet(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The identifier of the control set in the assessment. This is the control set name in a plain string format. </p>"""
    name: NotRequired["capo_auditmanager.types.control_set_name.ControlSetName"]
    """<p> The name of the control set. </p>"""
    controls: NotRequired["capo_auditmanager.types.controls.Controls"]
    """<p> The list of controls within the control set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlSet) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "controls" in value:
        import capo_auditmanager.types.controls

        out["controls"] = capo_auditmanager.types.controls.serialize_json(
            value["controls"]
        )
    return out


def deserialize_json(data: dict) -> ControlSet:
    out: ControlSet = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("controls") is not None:
        import capo_auditmanager.types.controls

        out["controls"] = capo_auditmanager.types.controls.deserialize_json(
            data["controls"]
        )
    return out


def redact_sensitive(value: ControlSet) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "controls" in value:
        import capo_auditmanager.types.controls

        out["controls"] = capo_auditmanager.types.controls.redact_sensitive(
            value["controls"]
        )
    return out
