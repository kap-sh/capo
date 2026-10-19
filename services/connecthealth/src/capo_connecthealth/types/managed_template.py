"""Generated from Smithy shape ``com.amazonaws.connecthealth#ManagedTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.managed_note_template


class ManagedTemplate(TypedDict, closed=True):
    template_type: "capo_connecthealth.types.managed_note_template.ManagedNoteTemplate"
    """<p>The type of managed template to use</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedTemplate) -> dict:
    out: dict = {}
    import capo_connecthealth.types.managed_note_template

    out["templateType"] = capo_connecthealth.types.managed_note_template.serialize_json(
        value["template_type"]
    )
    return out


def deserialize_json(data: dict) -> ManagedTemplate:
    out: ManagedTemplate = {}  # type: ignore[typeddict-item]
    if data.get("templateType") is not None:
        import capo_connecthealth.types.managed_note_template

        out["template_type"] = (
            capo_connecthealth.types.managed_note_template.deserialize_json(
                data["templateType"]
            )
        )
    else:
        import typing

        out["template_type"] = typing.cast(
            "capo_connecthealth.types.managed_note_template.ManagedNoteTemplate", ""
        )
    return out
