"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchExportFindingError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.error_code


class BatchExportFindingError(TypedDict, closed=True):
    finding_id: "str"
    """<p>The identifier of the finding this error corresponds to.</p>"""
    code: "capo_securityagent.types.error_code.ErrorCode"
    """<p>The machine-readable failure category.</p>"""
    message: "str"
    """<p>A customer-facing explanation of why the issue could not be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchExportFindingError) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    import capo_securityagent.types.error_code

    out["code"] = capo_securityagent.types.error_code.serialize_json(value["code"])
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchExportFindingError:
    out: BatchExportFindingError = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        raise DeserializationError("BatchExportFindingError.finding_id required")
    if data.get("code") is not None:
        import capo_securityagent.types.error_code

        out["code"] = capo_securityagent.types.error_code.deserialize_json(data["code"])
    else:
        raise DeserializationError("BatchExportFindingError.code required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchExportFindingError.message required")
    return out
