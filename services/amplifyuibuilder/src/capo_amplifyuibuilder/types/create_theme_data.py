"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CreateThemeData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.tags
    import capo_amplifyuibuilder.types.theme_name
    import capo_amplifyuibuilder.types.theme_values_list


class CreateThemeData(TypedDict, closed=True):
    name: "capo_amplifyuibuilder.types.theme_name.ThemeName"
    """<p>The name of the theme.</p>"""
    values: "capo_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    """<p>A list of key-value pairs that deﬁnes the properties of the theme.</p>"""
    overrides: NotRequired[
        "capo_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    ]
    """<p>Describes the properties that can be overriden to customize an instance of the theme.</p>"""
    tags: NotRequired["capo_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the theme data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThemeData) -> dict:
    out: dict = {}
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
    if "tags" in value:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateThemeData:
    out: CreateThemeData = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
    if data.get("tags") is not None:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    return out
