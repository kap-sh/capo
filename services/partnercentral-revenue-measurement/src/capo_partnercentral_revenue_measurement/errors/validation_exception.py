"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_revenue_measurement.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.validation_exception_field_list
    import capo_partnercentral_revenue_measurement.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_partnercentral_revenue_measurement.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason for the validation failure.</p>"""
    field_list: NotRequired[
        "capo_partnercentral_revenue_measurement.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>A list of fields that failed validation.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_revenue_measurement.types.validation_exception_reason

    out["Reason"] = (
        capo_partnercentral_revenue_measurement.types.validation_exception_reason.serialize_cbor(
            value["reason"]
        )
    )
    if "field_list" in value:
        import capo_partnercentral_revenue_measurement.types.validation_exception_field_list

        out["FieldList"] = (
            capo_partnercentral_revenue_measurement.types.validation_exception_field_list.serialize_cbor(
                value["field_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_partnercentral_revenue_measurement.types.validation_exception_reason

        out["reason"] = (
            capo_partnercentral_revenue_measurement.types.validation_exception_reason.deserialize_cbor(
                data["Reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.validation_exception_reason.ValidationExceptionReason",
            "",
        )
    if data.get("FieldList") is not None:
        import capo_partnercentral_revenue_measurement.types.validation_exception_field_list

        out["field_list"] = (
            capo_partnercentral_revenue_measurement.types.validation_exception_field_list.deserialize_cbor(
                data["FieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(
        self,
        data: ValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_cbor(data), message, response=response)
