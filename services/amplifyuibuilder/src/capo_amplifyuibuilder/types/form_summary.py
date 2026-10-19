"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.form_action_type
    import capo_amplifyuibuilder.types.form_data_type_config
    import capo_amplifyuibuilder.types.form_name
    import capo_amplifyuibuilder.types.uuid


class FormSummary(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID for the app associated with the form summary.</p>"""
    data_type: "capo_amplifyuibuilder.types.form_data_type_config.FormDataTypeConfig"
    """<p>The form's data source type.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    form_action_type: "capo_amplifyuibuilder.types.form_action_type.FormActionType"
    """<p>The type of operation to perform on the form.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The ID of the form.</p>"""
    name: "capo_amplifyuibuilder.types.form_name.FormName"
    """<p>The name of the form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormSummary) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    import capo_amplifyuibuilder.types.form_data_type_config

    out["dataType"] = capo_amplifyuibuilder.types.form_data_type_config.serialize_json(
        value["data_type"]
    )
    out["environmentName"] = value["environment_name"]
    import capo_amplifyuibuilder.types.form_action_type

    out["formActionType"] = capo_amplifyuibuilder.types.form_action_type.serialize_json(
        value["form_action_type"]
    )
    out["id"] = value["id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> FormSummary:
    out: FormSummary = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("dataType") is not None:
        import capo_amplifyuibuilder.types.form_data_type_config

        out["data_type"] = (
            capo_amplifyuibuilder.types.form_data_type_config.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("FormSummary.data_type required")
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        out["environment_name"] = ""
    if data.get("formActionType") is not None:
        import capo_amplifyuibuilder.types.form_action_type

        out["form_action_type"] = (
            capo_amplifyuibuilder.types.form_action_type.deserialize_json(
                data["formActionType"]
            )
        )
    else:
        import typing

        out["form_action_type"] = typing.cast(
            "capo_amplifyuibuilder.types.form_action_type.FormActionType", ""
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
