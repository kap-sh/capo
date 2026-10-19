"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#Theme``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_amplifyuibuilder.types.tags
    import capo_amplifyuibuilder.types.theme_name
    import capo_amplifyuibuilder.types.theme_values_list
    import capo_amplifyuibuilder.types.uuid


class Theme(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID for the Amplify app associated with the theme.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The ID for the theme.</p>"""
    name: "capo_amplifyuibuilder.types.theme_name.ThemeName"
    """<p>The name of the theme.</p>"""
    created_at: "datetime.datetime"
    """<p>The time that the theme was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The time that the theme was modified.</p>"""
    values: "capo_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    """<p>A list of key-value pairs that defines the properties of the theme.</p>"""
    overrides: NotRequired[
        "capo_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    ]
    """<p>Describes the properties that can be overriden to customize a theme.</p>"""
    tags: NotRequired["capo_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Theme) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_amplifyuibuilder._protocol.serialize

    out["createdAt"] = capo_amplifyuibuilder._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "modified_at" in value:
        import capo_amplifyuibuilder._protocol.serialize

        out["modifiedAt"] = capo_amplifyuibuilder._protocol.serialize.fmt_date_time(
            value["modified_at"]
        )
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


def deserialize_json(data: dict) -> Theme:
    out: Theme = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        out["environment_name"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("modifiedAt") is not None:
        import datetime

        out["modified_at"] = datetime.datetime.fromisoformat(
            data["modifiedAt"].replace("Z", "+00:00")
        )
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
