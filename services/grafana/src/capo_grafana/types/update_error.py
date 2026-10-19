"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.update_instruction


class UpdateError(TypedDict, closed=True):
    code: "int"
    """<p>The error code.</p>"""
    message: "str"
    """<p>The message for this error.</p>"""
    caused_by: "capo_grafana.types.update_instruction.UpdateInstruction"
    """<p>Specifies which permission update caused the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateError) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    import capo_grafana.types.update_instruction

    out["causedBy"] = capo_grafana.types.update_instruction.serialize_json(
        value["caused_by"]
    )
    return out


def deserialize_json(data: dict) -> UpdateError:
    out: UpdateError = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = 0
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("causedBy") is not None:
        import capo_grafana.types.update_instruction

        out["caused_by"] = capo_grafana.types.update_instruction.deserialize_json(
            data["causedBy"]
        )
    else:
        raise DeserializationError("UpdateError.caused_by required")
    return out
