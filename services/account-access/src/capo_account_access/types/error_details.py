"""Generated from Smithy shape ``com.amazonaws.accountaccess#ErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.error_code


class ErrorDetails(TypedDict, closed=True):
    code: "capo_account_access.types.error_code.ErrorCode"
    """<p>The error code that identifies the type of error.</p>"""
    message: "str"
    """<p>A human-readable message that describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> dict:
    out: dict = {}
    import capo_account_access.types.error_code

    out["code"] = capo_account_access.types.error_code.serialize_json(value["code"])
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_account_access.types.error_code

        out["code"] = capo_account_access.types.error_code.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError("ErrorDetails.code required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ErrorDetails.message required")
    return out
