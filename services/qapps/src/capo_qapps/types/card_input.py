"""Generated from Smithy shape ``com.amazonaws.qapps#CardInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qapps.errors import DeserializationError, SerializationError
from capo_qapps.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qapps.types.file_upload_card_input
    import capo_qapps.types.form_input_card_input
    import capo_qapps.types.q_plugin_card_input
    import capo_qapps.types.q_query_card_input
    import capo_qapps.types.text_input_card_input


class CardInputTextInputMember(TypedDict, closed=True):
    textInput: "capo_qapps.types.text_input_card_input.TextInputCardInput"


class CardInputQQueryMember(TypedDict, closed=True):
    qQuery: "capo_qapps.types.q_query_card_input.QQueryCardInput"


class CardInputQPluginMember(TypedDict, closed=True):
    qPlugin: "capo_qapps.types.q_plugin_card_input.QPluginCardInput"


class CardInputFileUploadMember(TypedDict, closed=True):
    fileUpload: "capo_qapps.types.file_upload_card_input.FileUploadCardInput"


class CardInputFormInputMember(TypedDict, closed=True):
    formInput: "capo_qapps.types.form_input_card_input.FormInputCardInput"


CardInput: TypeAlias = (
    CardInputTextInputMember
    | CardInputQQueryMember
    | CardInputQPluginMember
    | CardInputFileUploadMember
    | CardInputFormInputMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CardInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CardInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "textInput" in value:
        import capo_qapps.types.text_input_card_input

        return {
            "textInput": capo_qapps.types.text_input_card_input.serialize_json(
                value["textInput"]
            )
        }
    elif "qQuery" in value:
        import capo_qapps.types.q_query_card_input

        return {
            "qQuery": capo_qapps.types.q_query_card_input.serialize_json(
                value["qQuery"]
            )
        }
    elif "qPlugin" in value:
        import capo_qapps.types.q_plugin_card_input

        return {
            "qPlugin": capo_qapps.types.q_plugin_card_input.serialize_json(
                value["qPlugin"]
            )
        }
    elif "fileUpload" in value:
        import capo_qapps.types.file_upload_card_input

        return {
            "fileUpload": capo_qapps.types.file_upload_card_input.serialize_json(
                value["fileUpload"]
            )
        }
    elif "formInput" in value:
        import capo_qapps.types.form_input_card_input

        return {
            "formInput": capo_qapps.types.form_input_card_input.serialize_json(
                value["formInput"]
            )
        }
    else:
        raise SerializationError("CardInput: no variant present")


def deserialize_json(data: dict) -> CardInput:
    if data.get("textInput") is not None:
        import capo_qapps.types.text_input_card_input

        return {
            "textInput": capo_qapps.types.text_input_card_input.deserialize_json(
                data["textInput"]
            )
        }
    elif data.get("qQuery") is not None:
        import capo_qapps.types.q_query_card_input

        return {
            "qQuery": capo_qapps.types.q_query_card_input.deserialize_json(
                data["qQuery"]
            )
        }
    elif data.get("qPlugin") is not None:
        import capo_qapps.types.q_plugin_card_input

        return {
            "qPlugin": capo_qapps.types.q_plugin_card_input.deserialize_json(
                data["qPlugin"]
            )
        }
    elif data.get("fileUpload") is not None:
        import capo_qapps.types.file_upload_card_input

        return {
            "fileUpload": capo_qapps.types.file_upload_card_input.deserialize_json(
                data["fileUpload"]
            )
        }
    elif data.get("formInput") is not None:
        import capo_qapps.types.form_input_card_input

        return {
            "formInput": capo_qapps.types.form_input_card_input.deserialize_json(
                data["formInput"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CardInput: no recognized variant key")
