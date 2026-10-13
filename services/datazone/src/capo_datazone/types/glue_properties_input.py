"""Generated from Smithy shape ``com.amazonaws.datazone#GluePropertiesInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.glue_connection_input


class GluePropertiesInput(TypedDict, closed=True):
    glue_connection_input: NotRequired[
        "capo_datazone.types.glue_connection_input.GlueConnectionInput"
    ]
    """<p>The Amazon Web Services Glue connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GluePropertiesInput) -> dict:
    out: dict = {}
    if "glue_connection_input" in value:
        import capo_datazone.types.glue_connection_input

        out["glueConnectionInput"] = (
            capo_datazone.types.glue_connection_input.serialize_json(
                value["glue_connection_input"]
            )
        )
    return out


def deserialize_json(data: dict) -> GluePropertiesInput:
    out: GluePropertiesInput = {}  # type: ignore[typeddict-item]
    if data.get("glueConnectionInput") is not None:
        import capo_datazone.types.glue_connection_input

        out["glue_connection_input"] = (
            capo_datazone.types.glue_connection_input.deserialize_json(
                data["glueConnectionInput"]
            )
        )
    return out


def redact_sensitive(value: GluePropertiesInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "glue_connection_input" in value:
        import capo_datazone.types.glue_connection_input

        out["glue_connection_input"] = (
            capo_datazone.types.glue_connection_input.redact_sensitive(
                value["glue_connection_input"]
            )
        )
    return out
