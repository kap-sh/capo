"""Generated from Smithy shape ``com.amazonaws.qapps#Card``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qapps.errors import DeserializationError, SerializationError
from capo_qapps.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qapps.types.file_upload_card
    import capo_qapps.types.form_input_card
    import capo_qapps.types.q_plugin_card
    import capo_qapps.types.q_query_card
    import capo_qapps.types.text_input_card


class _Card_textInput(TypedDict, closed=True):
    textInput: "capo_qapps.types.text_input_card.TextInputCard"


class _Card_qQuery(TypedDict, closed=True):
    qQuery: "capo_qapps.types.q_query_card.QQueryCard"


class _Card_qPlugin(TypedDict, closed=True):
    qPlugin: "capo_qapps.types.q_plugin_card.QPluginCard"


class _Card_fileUpload(TypedDict, closed=True):
    fileUpload: "capo_qapps.types.file_upload_card.FileUploadCard"


class _Card_formInput(TypedDict, closed=True):
    formInput: "capo_qapps.types.form_input_card.FormInputCard"


Card: TypeAlias = (
    _Card_textInput
    | _Card_qQuery
    | _Card_qPlugin
    | _Card_fileUpload
    | _Card_formInput
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Card) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Card: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "textInput" in value:
        import capo_qapps.types.text_input_card

        return {
            "textInput": capo_qapps.types.text_input_card.serialize_json(
                value["textInput"]
            )
        }
    elif "qQuery" in value:
        import capo_qapps.types.q_query_card

        return {"qQuery": capo_qapps.types.q_query_card.serialize_json(value["qQuery"])}
    elif "qPlugin" in value:
        import capo_qapps.types.q_plugin_card

        return {
            "qPlugin": capo_qapps.types.q_plugin_card.serialize_json(value["qPlugin"])
        }
    elif "fileUpload" in value:
        import capo_qapps.types.file_upload_card

        return {
            "fileUpload": capo_qapps.types.file_upload_card.serialize_json(
                value["fileUpload"]
            )
        }
    elif "formInput" in value:
        import capo_qapps.types.form_input_card

        return {
            "formInput": capo_qapps.types.form_input_card.serialize_json(
                value["formInput"]
            )
        }
    else:
        raise SerializationError("Card: no variant present")


def deserialize_json(data: dict) -> Card:
    if data.get("textInput") is not None:
        import capo_qapps.types.text_input_card

        return {
            "textInput": capo_qapps.types.text_input_card.deserialize_json(
                data["textInput"]
            )
        }
    elif data.get("qQuery") is not None:
        import capo_qapps.types.q_query_card

        return {
            "qQuery": capo_qapps.types.q_query_card.deserialize_json(data["qQuery"])
        }
    elif data.get("qPlugin") is not None:
        import capo_qapps.types.q_plugin_card

        return {
            "qPlugin": capo_qapps.types.q_plugin_card.deserialize_json(data["qPlugin"])
        }
    elif data.get("fileUpload") is not None:
        import capo_qapps.types.file_upload_card

        return {
            "fileUpload": capo_qapps.types.file_upload_card.deserialize_json(
                data["fileUpload"]
            )
        }
    elif data.get("formInput") is not None:
        import capo_qapps.types.form_input_card

        return {
            "formInput": capo_qapps.types.form_input_card.deserialize_json(
                data["formInput"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Card: no recognized variant key")
