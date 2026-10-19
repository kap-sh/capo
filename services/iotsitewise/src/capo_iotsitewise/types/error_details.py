"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.detailed_errors
    import capo_iotsitewise.types.error_code
    import capo_iotsitewise.types.error_message


class ErrorDetails(TypedDict, closed=True):
    code: "capo_iotsitewise.types.error_code.ErrorCode"
    """<p>The error code.</p>"""
    message: "capo_iotsitewise.types.error_message.ErrorMessage"
    """<p>The error message.</p>"""
    details: NotRequired["capo_iotsitewise.types.detailed_errors.DetailedErrors"]
    """<p> A list of detailed errors. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.error_code

    out["code"] = capo_iotsitewise.types.error_code.serialize_json(value["code"])
    out["message"] = value["message"]
    if "details" in value:
        import capo_iotsitewise.types.detailed_errors

        out["details"] = capo_iotsitewise.types.detailed_errors.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_iotsitewise.types.error_code

        out["code"] = capo_iotsitewise.types.error_code.deserialize_json(data["code"])
    else:
        import typing

        out["code"] = typing.cast("capo_iotsitewise.types.error_code.ErrorCode", "")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("details") is not None:
        import capo_iotsitewise.types.detailed_errors

        out["details"] = capo_iotsitewise.types.detailed_errors.deserialize_json(
            data["details"]
        )
    return out
