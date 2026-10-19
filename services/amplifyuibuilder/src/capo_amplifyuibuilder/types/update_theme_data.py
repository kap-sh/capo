"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateThemeData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.theme_name
    import capo_amplifyuibuilder.types.theme_values_list
    import capo_amplifyuibuilder.types.uuid


class UpdateThemeData(TypedDict, closed=True):
    id: NotRequired["capo_amplifyuibuilder.types.uuid.Uuid"]
    """<p>The unique ID of the theme to update.</p>"""
    name: NotRequired["capo_amplifyuibuilder.types.theme_name.ThemeName"]
    """<p>The name of the theme to update.</p>"""
    values: "capo_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    """<p>A list of key-value pairs that define the theme's properties.</p>"""
    overrides: NotRequired[
        "capo_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    ]
    """<p>Describes the properties that can be overriden to customize the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeData) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_amplifyuibuilder.types.theme_values_list

    out["values"] = capo_amplifyuibuilder.types.theme_values_list.serialize_json(
        value["values"]
    )
    if "overrides" in value:
        import capo_amplifyuibuilder.types.theme_values_list

        out["overrides"] = capo_amplifyuibuilder.types.theme_values_list.serialize_json(
            value["overrides"]
        )
    return out


def deserialize_json(data: dict) -> UpdateThemeData:
    out: UpdateThemeData = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("values") is not None:
        import capo_amplifyuibuilder.types.theme_values_list

        out["values"] = capo_amplifyuibuilder.types.theme_values_list.deserialize_json(
            data["values"]
        )
    else:
        out["values"] = []
    if data.get("overrides") is not None:
        import capo_amplifyuibuilder.types.theme_values_list

        out["overrides"] = (
            capo_amplifyuibuilder.types.theme_values_list.deserialize_json(
                data["overrides"]
            )
        )
    return out
