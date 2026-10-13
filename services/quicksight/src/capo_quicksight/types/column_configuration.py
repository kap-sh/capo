"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.colors_configuration
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.column_role
    import capo_quicksight.types.decal_settings_configuration
    import capo_quicksight.types.format_configuration


class ColumnConfiguration(TypedDict, closed=True):
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column.</p>"""
    format_configuration: NotRequired[
        "capo_quicksight.types.format_configuration.FormatConfiguration"
    ]
    """<p>The format configuration of a column.</p>"""
    role: NotRequired["capo_quicksight.types.column_role.ColumnRole"]
    """<p>The role of the column.</p>"""
    colors_configuration: NotRequired[
        "capo_quicksight.types.colors_configuration.ColorsConfiguration"
    ]
    """<p>The color configurations of the column.</p>"""
    decal_settings_configuration: NotRequired[
        "capo_quicksight.types.decal_settings_configuration.DecalSettingsConfiguration"
    ]
    """<p>Decal configuration of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "format_configuration" in value:
        import capo_quicksight.types.format_configuration

        out["FormatConfiguration"] = (
            capo_quicksight.types.format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    if "role" in value:
        import capo_quicksight.types.column_role

        out["Role"] = capo_quicksight.types.column_role.serialize_json(value["role"])
    if "colors_configuration" in value:
        import capo_quicksight.types.colors_configuration

        out["ColorsConfiguration"] = (
            capo_quicksight.types.colors_configuration.serialize_json(
                value["colors_configuration"]
            )
        )
    if "decal_settings_configuration" in value:
        import capo_quicksight.types.decal_settings_configuration

        out["DecalSettingsConfiguration"] = (
            capo_quicksight.types.decal_settings_configuration.serialize_json(
                value["decal_settings_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnConfiguration:
    out: ColumnConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("ColumnConfiguration.column required")
    if data.get("FormatConfiguration") is not None:
        import capo_quicksight.types.format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    if data.get("Role") is not None:
        import capo_quicksight.types.column_role

        out["role"] = capo_quicksight.types.column_role.deserialize_json(data["Role"])
    if data.get("ColorsConfiguration") is not None:
        import capo_quicksight.types.colors_configuration

        out["colors_configuration"] = (
            capo_quicksight.types.colors_configuration.deserialize_json(
                data["ColorsConfiguration"]
            )
        )
    if data.get("DecalSettingsConfiguration") is not None:
        import capo_quicksight.types.decal_settings_configuration

        out["decal_settings_configuration"] = (
            capo_quicksight.types.decal_settings_configuration.deserialize_json(
                data["DecalSettingsConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ColumnConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "format_configuration" in value:
        import capo_quicksight.types.format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.format_configuration.redact_sensitive(
                value["format_configuration"]
            )
        )
    if "colors_configuration" in value:
        import capo_quicksight.types.colors_configuration

        out["colors_configuration"] = (
            capo_quicksight.types.colors_configuration.redact_sensitive(
                value["colors_configuration"]
            )
        )
    return out
