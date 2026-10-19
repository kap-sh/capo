"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.field_validation_code


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The name of the field that failed validation.</p>"""
    message: "str"
    """<p>A human-readable message describing why the field validation failed.</p>"""
    code: "capo_partnercentral_revenue_measurement.types.field_validation_code.FieldValidationCode"
    """<p>The specific validation error code indicating the type of validation failure.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Message"] = value["message"]
    import capo_partnercentral_revenue_measurement.types.field_validation_code

    out["Code"] = (
        capo_partnercentral_revenue_measurement.types.field_validation_code.serialize_cbor(
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
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Code") is not None:
        import capo_partnercentral_revenue_measurement.types.field_validation_code

        out["code"] = (
            capo_partnercentral_revenue_measurement.types.field_validation_code.deserialize_cbor(
                data["Code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.field_validation_code.FieldValidationCode",
            "",
        )
    return out
