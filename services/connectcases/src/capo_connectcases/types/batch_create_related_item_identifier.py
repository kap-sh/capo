"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchCreateRelatedItemIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_identifier_union


class BatchCreateRelatedItemIdentifier(TypedDict, closed=True):
    case_identifier: "capo_connectcases.types.case_identifier_union.CaseIdentifierUnion"
    """<p>The identifier of the case to associate the related item with. Specify either the case ID or the reference ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRelatedItemIdentifier) -> dict:
    out: dict = {}
    import capo_connectcases.types.case_identifier_union

    out["caseIdentifier"] = (
        capo_connectcases.types.case_identifier_union.serialize_json(
            value["case_identifier"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateRelatedItemIdentifier:
    out: BatchCreateRelatedItemIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("caseIdentifier") is not None:
        import capo_connectcases.types.case_identifier_union

        out["case_identifier"] = (
            capo_connectcases.types.case_identifier_union.deserialize_json(
                data["caseIdentifier"]
            )
        )
    else:
        out["case_identifier"] = {"$unknown": {"name": ""}}
    return out
