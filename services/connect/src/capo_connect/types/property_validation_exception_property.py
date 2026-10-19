"""Generated from Smithy shape ``com.amazonaws.connect#PropertyValidationExceptionProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.message
    import capo_connect.types.property_validation_exception_reason
    import capo_connect.types.string


class PropertyValidationExceptionProperty(TypedDict, closed=True):
    property_path: "capo_connect.types.string.String"
    """<p>The full property path.</p>"""
    reason: "capo_connect.types.property_validation_exception_reason.PropertyValidationExceptionReason"
    """<p>Why the property is not valid.</p>"""
    message: "capo_connect.types.message.Message"
    """<p>A message describing why the property is not valid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValidationExceptionProperty) -> dict:
    out: dict = {}
    out["PropertyPath"] = value["property_path"]
    import capo_connect.types.property_validation_exception_reason

    out["Reason"] = (
        capo_connect.types.property_validation_exception_reason.serialize_json(
            value["reason"]
        )
    )
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PropertyValidationExceptionProperty:
    out: PropertyValidationExceptionProperty = {}  # type: ignore[typeddict-item]
    if data.get("PropertyPath") is not None:
        out["property_path"] = data["PropertyPath"]
    else:
        out["property_path"] = ""
    if data.get("Reason") is not None:
        import capo_connect.types.property_validation_exception_reason

        out["reason"] = (
            capo_connect.types.property_validation_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_connect.types.property_validation_exception_reason.PropertyValidationExceptionReason",
            "",
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
