"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchUpdateCaseSuccessEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.case_identifier


class BatchUpdateCaseSuccessEntry(TypedDict, closed=True):
    case_identifier: "capo_connectcases.types.case_identifier.CaseIdentifier"
    """<p>The identifiers of the updated case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCaseSuccessEntry) -> dict:
    out: dict = {}
    import capo_connectcases.types.case_identifier

    out["caseIdentifier"] = capo_connectcases.types.case_identifier.serialize_json(
        value["case_identifier"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateCaseSuccessEntry:
    out: BatchUpdateCaseSuccessEntry = {}  # type: ignore[typeddict-item]
    if data.get("caseIdentifier") is not None:
        import capo_connectcases.types.case_identifier

        out["case_identifier"] = (
            capo_connectcases.types.case_identifier.deserialize_json(
                data["caseIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateCaseSuccessEntry.case_identifier required"
        )
    return out
