"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateControlResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control


class UpdateControlResponse(TypedDict, closed=True):
    control: NotRequired["capo_auditmanager.types.control.Control"]
    """<p> The name of the updated control set that the <code>UpdateControl</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateControlResponse) -> dict:
    out: dict = {}
    if "control" in value:
        import capo_auditmanager.types.control

        out["control"] = capo_auditmanager.types.control.serialize_json(
            value["control"]
        )
    return out


def deserialize_json(data: dict) -> UpdateControlResponse:
    out: UpdateControlResponse = {}  # type: ignore[typeddict-item]
    if data.get("control") is not None:
        import capo_auditmanager.types.control

        out["control"] = capo_auditmanager.types.control.deserialize_json(
            data["control"]
        )
    return out


def redact_sensitive(value: UpdateControlResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "control" in value:
        import capo_auditmanager.types.control

        out["control"] = capo_auditmanager.types.control.redact_sensitive(
            value["control"]
        )
    return out
