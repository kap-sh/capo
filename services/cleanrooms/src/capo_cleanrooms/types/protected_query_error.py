"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.retry_info


class ProtectedQueryError(TypedDict, closed=True):
    message: "str"
    """<p>A description of why the protected query failed.</p>"""
    code: "str"
    """<p>A code that identifies the category of the failure. Valid values are:</p> <ul> <li> <p> <code>MALFORMED_QUERY</code> – The query is not valid (syntax, semantics, columns, or an unsupported operation).</p> </li> <li> <p> <code>RESOURCE_NOT_FOUND</code> – A referenced resource doesn't exist.</p> </li> <li> <p> <code>INVALID_RESOURCE</code> – A referenced resource exists, but you can't use it because its configuration, state, or data is not valid.</p> </li> <li> <p> <code>RESOURCE_ACCESS_DENIED</code> – A required permission is missing for a data source or resource.</p> </li> <li> <p> <code>INSUFFICIENT_COMPUTE</code> – The query exceeded the available compute (memory, disk, or time).</p> </li> <li> <p> <code>TRANSIENT_ERROR</code> – A temporary condition caused the failure, such as throttling or a network interruption.</p> </li> <li> <p> <code>INTERNAL_ERROR</code> – Clean Rooms encountered an unexpected error. If the error persists, contact AWS Support.</p> </li> <li> <p> <code>UNKNOWN_ERROR</code> – The failure couldn't be classified.</p> </li> </ul> <p>For more information about error codes, see <a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/error-codes.html">https://docs.aws.amazon.com/clean-rooms/latest/userguide/error-codes.html</a> in the Clean Rooms User Guide.</p>"""
    retry: NotRequired["capo_cleanrooms.types.retry_info.RetryInfo"]
    """<p>Contains information about whether running the same protected query again might succeed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["code"] = value["code"]
    if "retry" in value:
        import capo_cleanrooms.types.retry_info

        out["retry"] = capo_cleanrooms.types.retry_info.serialize_json(value["retry"])
    return out


def deserialize_json(data: dict) -> ProtectedQueryError:
    out: ProtectedQueryError = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("retry") is not None:
        import capo_cleanrooms.types.retry_info

        out["retry"] = capo_cleanrooms.types.retry_info.deserialize_json(data["retry"])
    return out
