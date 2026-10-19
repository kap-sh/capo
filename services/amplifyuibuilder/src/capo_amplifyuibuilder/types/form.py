"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#Form``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.fields_map
    import capo_amplifyuibuilder.types.form_action_type
    import capo_amplifyuibuilder.types.form_cta
    import capo_amplifyuibuilder.types.form_data_type_config
    import capo_amplifyuibuilder.types.form_name
    import capo_amplifyuibuilder.types.form_style
    import capo_amplifyuibuilder.types.label_decorator
    import capo_amplifyuibuilder.types.sectional_element_map
    import capo_amplifyuibuilder.types.tags
    import capo_amplifyuibuilder.types.uuid


class Form(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app associated with the form.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID of the form.</p>"""
    name: "capo_amplifyuibuilder.types.form_name.FormName"
    """<p>The name of the form.</p>"""
    form_action_type: "capo_amplifyuibuilder.types.form_action_type.FormActionType"
    """<p>The operation to perform on the specified form.</p>"""
    style: "capo_amplifyuibuilder.types.form_style.FormStyle"
    """<p>Stores the configuration for the form's style.</p>"""
    data_type: "capo_amplifyuibuilder.types.form_data_type_config.FormDataTypeConfig"
    """<p>The type of data source to use to create the form.</p>"""
    fields: "capo_amplifyuibuilder.types.fields_map.FieldsMap"
    """<p>Stores the information about the form's fields.</p>"""
    sectional_elements: (
        "capo_amplifyuibuilder.types.sectional_element_map.SectionalElementMap"
    )
    """<p>Stores the visual helper elements for the form that are not associated with any data.</p>"""
    schema_version: "str"
    """<p>The schema version of the form when it was imported.</p>"""
    tags: NotRequired["capo_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the form.</p>"""
    cta: NotRequired["capo_amplifyuibuilder.types.form_cta.FormCTA"]
    """<p>Stores the call to action configuration for the form.</p>"""
    label_decorator: NotRequired[
        "capo_amplifyuibuilder.types.label_decorator.LabelDecorator"
    ]
    """<p>Specifies an icon or decoration to display on the form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Form) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_amplifyuibuilder.types.form_action_type

    out["formActionType"] = capo_amplifyuibuilder.types.form_action_type.serialize_json(
        value["form_action_type"]
    )
    import capo_amplifyuibuilder.types.form_style

    out["style"] = capo_amplifyuibuilder.types.form_style.serialize_json(value["style"])
    import capo_amplifyuibuilder.types.form_data_type_config

    out["dataType"] = capo_amplifyuibuilder.types.form_data_type_config.serialize_json(
        value["data_type"]
    )
    import capo_amplifyuibuilder.types.fields_map

    out["fields"] = capo_amplifyuibuilder.types.fields_map.serialize_json(
        value["fields"]
    )
    import capo_amplifyuibuilder.types.sectional_element_map

    out["sectionalElements"] = (
        capo_amplifyuibuilder.types.sectional_element_map.serialize_json(
            value["sectional_elements"]
        )
    )
    out["schemaVersion"] = value["schema_version"]
    if "tags" in value:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    if "cta" in value:
        import capo_amplifyuibuilder.types.form_cta

        out["cta"] = capo_amplifyuibuilder.types.form_cta.serialize_json(value["cta"])
    if "label_decorator" in value:
        out["labelDecorator"] = value["label_decorator"]
    return out


def deserialize_json(data: dict) -> Form:
    out: Form = {}  # type: ignore[typeddict-item]
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
    if data.get("style") is not None:
        import capo_amplifyuibuilder.types.form_style

        out["style"] = capo_amplifyuibuilder.types.form_style.deserialize_json(
            data["style"]
        )
    else:
        raise DeserializationError("Form.style required")
    if data.get("dataType") is not None:
        import capo_amplifyuibuilder.types.form_data_type_config

        out["data_type"] = (
            capo_amplifyuibuilder.types.form_data_type_config.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("Form.data_type required")
    if data.get("fields") is not None:
        import capo_amplifyuibuilder.types.fields_map

        out["fields"] = capo_amplifyuibuilder.types.fields_map.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = {}
    if data.get("sectionalElements") is not None:
        import capo_amplifyuibuilder.types.sectional_element_map

        out["sectional_elements"] = (
            capo_amplifyuibuilder.types.sectional_element_map.deserialize_json(
                data["sectionalElements"]
            )
        )
    else:
        out["sectional_elements"] = {}
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    else:
        out["schema_version"] = ""
    if data.get("tags") is not None:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    if data.get("cta") is not None:
        import capo_amplifyuibuilder.types.form_cta

        out["cta"] = capo_amplifyuibuilder.types.form_cta.deserialize_json(data["cta"])
    if data.get("labelDecorator") is not None:
        out["label_decorator"] = data["labelDecorator"]
    return out
