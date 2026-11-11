"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchCreateRelatedItemSuccessEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.case_identifier
    import capo_connectcases.types.related_item_arn
    import capo_connectcases.types.related_item_id


class BatchCreateRelatedItemSuccessEntry(TypedDict, closed=True):
    case_identifier: "capo_connectcases.types.case_identifier.CaseIdentifier"
    """<p>The identifiers of the case that the related item is associated with.</p>"""
    related_item_id: "capo_connectcases.types.related_item_id.RelatedItemId"
    """<p>The unique identifier of the related item.</p>"""
    related_item_arn: "capo_connectcases.types.related_item_arn.RelatedItemArn"
    """<p>The Amazon Resource Name (ARN) of the related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRelatedItemSuccessEntry) -> dict:
    out: dict = {}
    import capo_connectcases.types.case_identifier

    out["caseIdentifier"] = capo_connectcases.types.case_identifier.serialize_json(
        value["case_identifier"]
    )
    out["relatedItemId"] = value["related_item_id"]
    out["relatedItemArn"] = value["related_item_arn"]
    return out


def deserialize_json(data: dict) -> BatchCreateRelatedItemSuccessEntry:
    out: BatchCreateRelatedItemSuccessEntry = {}  # type: ignore[typeddict-item]
    if data.get("caseIdentifier") is not None:
        import capo_connectcases.types.case_identifier

        out["case_identifier"] = (
            capo_connectcases.types.case_identifier.deserialize_json(
                data["caseIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateRelatedItemSuccessEntry.case_identifier required"
        )
    if data.get("relatedItemId") is not None:
        out["related_item_id"] = data["relatedItemId"]
    else:
        out["related_item_id"] = ""
    if data.get("relatedItemArn") is not None:
        out["related_item_arn"] = data["relatedItemArn"]
    else:
        out["related_item_arn"] = ""
    return out
