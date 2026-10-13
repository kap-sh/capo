"""Generated from Smithy shape ``com.amazonaws.datazone#GluePropertiesPatch``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.glue_connection_patch


class GluePropertiesPatch(TypedDict, closed=True):
    glue_connection_input: NotRequired[
        "capo_datazone.types.glue_connection_patch.GlueConnectionPatch"
    ]
    """<p>The Amazon Web Services Glue properties patch of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GluePropertiesPatch) -> dict:
    out: dict = {}
    if "glue_connection_input" in value:
        import capo_datazone.types.glue_connection_patch

        out["glueConnectionInput"] = (
            capo_datazone.types.glue_connection_patch.serialize_json(
                value["glue_connection_input"]
            )
        )
    return out


def deserialize_json(data: dict) -> GluePropertiesPatch:
    out: GluePropertiesPatch = {}  # type: ignore[typeddict-item]
    if data.get("glueConnectionInput") is not None:
        import capo_datazone.types.glue_connection_patch

        out["glue_connection_input"] = (
            capo_datazone.types.glue_connection_patch.deserialize_json(
                data["glueConnectionInput"]
            )
        )
    return out


def redact_sensitive(value: GluePropertiesPatch) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "glue_connection_input" in value:
        import capo_datazone.types.glue_connection_patch

        out["glue_connection_input"] = (
            capo_datazone.types.glue_connection_patch.redact_sensitive(
                value["glue_connection_input"]
            )
        )
    return out
