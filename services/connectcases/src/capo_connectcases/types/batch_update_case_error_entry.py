"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchUpdateCaseErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.case_identifier


class BatchUpdateCaseErrorEntry(TypedDict, closed=True):
    case_identifier: "capo_connectcases.types.case_identifier.CaseIdentifier"
    """<p>The identifiers of the case that wasn't updated.</p>"""
    error_code: "str"
    """<p>The error code. For possible values, see <code>failedCases</code>.</p>"""
    error_message: "str"
    """<p>A message that describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCaseErrorEntry) -> dict:
    out: dict = {}
    import capo_connectcases.types.case_identifier

    out["caseIdentifier"] = capo_connectcases.types.case_identifier.serialize_json(
        value["case_identifier"]
    )
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateCaseErrorEntry:
    out: BatchUpdateCaseErrorEntry = {}  # type: ignore[typeddict-item]
    if data.get("caseIdentifier") is not None:
        import capo_connectcases.types.case_identifier

        out["case_identifier"] = (
            capo_connectcases.types.case_identifier.deserialize_json(
                data["caseIdentifier"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateCaseErrorEntry.case_identifier required")
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
