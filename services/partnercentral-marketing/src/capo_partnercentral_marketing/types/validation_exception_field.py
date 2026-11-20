"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.template_field_id
    import capo_partnercentral_marketing.types.validation_exception_field_code


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """The member of the request that failed, as the request names it: `FieldValues` for a template field value, `Layout`, `EmailTarget`, `Identifier`, and so on. It is never a template field id: a template field is always `FieldValues`, with the field in `FieldId`."""
    field_id: NotRequired[
        "capo_partnercentral_marketing.types.template_field_id.TemplateFieldId"
    ]
    """The template field that failed, when `Name` is `FieldValues`; absent otherwise."""
    message: "str"
    """Why this field failed, in prose a partner can be shown directly."""
    code: NotRequired[
        "capo_partnercentral_marketing.types.validation_exception_field_code.ValidationExceptionFieldCode"
    ]
    """Why this field failed, as a value a client branches on. Read this rather than `Message`."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "field_id" in value:
        out["FieldId"] = value["field_id"]
    out["Message"] = value["message"]
    if "code" in value:
        import capo_partnercentral_marketing.types.validation_exception_field_code

        out["Code"] = (
            capo_partnercentral_marketing.types.validation_exception_field_code.serialize_cbor(
                value["code"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Code") is not None:
        import capo_partnercentral_marketing.types.validation_exception_field_code

        out["code"] = (
            capo_partnercentral_marketing.types.validation_exception_field_code.deserialize_cbor(
                data["Code"]
            )
        )
    return out
