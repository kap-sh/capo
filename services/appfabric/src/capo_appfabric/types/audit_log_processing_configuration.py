"""Generated from Smithy shape ``com.amazonaws.appfabric#AuditLogProcessingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.format
    import capo_appfabric.types.schema


class AuditLogProcessingConfiguration(TypedDict, closed=True):
    schema: "capo_appfabric.types.schema.Schema"
    """<p>The event schema in which the audit logs need to be formatted.</p>"""
    format: "capo_appfabric.types.format.Format"
    """<p>The format in which the audit logs need to be formatted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditLogProcessingConfiguration) -> dict:
    out: dict = {}
    import capo_appfabric.types.schema

    out["schema"] = capo_appfabric.types.schema.serialize_json(value["schema"])
    import capo_appfabric.types.format

    out["format"] = capo_appfabric.types.format.serialize_json(value["format"])
    return out


def deserialize_json(data: dict) -> AuditLogProcessingConfiguration:
    out: AuditLogProcessingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("schema") is not None:
        import capo_appfabric.types.schema

        out["schema"] = capo_appfabric.types.schema.deserialize_json(data["schema"])
    else:
        import typing

        out["schema"] = typing.cast("capo_appfabric.types.schema.Schema", "")
    if data.get("format") is not None:
        import capo_appfabric.types.format

        out["format"] = capo_appfabric.types.format.deserialize_json(data["format"])
    else:
        import typing

        out["format"] = typing.cast("capo_appfabric.types.format.Format", "")
    return out
