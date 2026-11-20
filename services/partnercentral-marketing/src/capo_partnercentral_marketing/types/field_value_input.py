"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#FieldValueInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.template_field_id
    import capo_partnercentral_marketing.types.template_field_value


class FieldValueInput(TypedDict, closed=True):
    field_id: "capo_partnercentral_marketing.types.template_field_id.TemplateFieldId"
    """The field to update; must match a FieldId in the asset's stored schema."""
    value: NotRequired[
        "capo_partnercentral_marketing.types.template_field_value.TemplateFieldValue"
    ]
    """The new value. Omit to clear the field."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FieldValueInput) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "value" in value:
        import capo_partnercentral_marketing.types.template_field_value

        out["Value"] = (
            capo_partnercentral_marketing.types.template_field_value.serialize_cbor(
                value["value"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> FieldValueInput:
    out: FieldValueInput = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("Value") is not None:
        import capo_partnercentral_marketing.types.template_field_value

        out["value"] = (
            capo_partnercentral_marketing.types.template_field_value.deserialize_cbor(
                data["Value"]
            )
        )
    return out


def redact_sensitive(value: FieldValueInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        import capo_partnercentral_marketing.types.template_field_value

        out["value"] = (
            capo_partnercentral_marketing.types.template_field_value.redact_sensitive(
                value["value"]
            )
        )
    return out
