"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationFilterCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.equals
    import capo_guardduty.types.not_equals


class InvestigationFilterCondition(TypedDict, closed=True):
    equals: NotRequired["capo_guardduty.types.equals.Equals"]
    """<p>The values to match. An investigation matches if its attribute value equals any of the specified values.</p>"""
    not_equals: NotRequired["capo_guardduty.types.not_equals.NotEquals"]
    """<p>The values to exclude. An investigation matches only if its attribute value doesn't equal any of the specified values. An investigation that has no value for the attribute also matches.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationFilterCondition) -> dict:
    out: dict = {}
    if "equals" in value:
        import capo_guardduty.types.equals

        out["equals"] = capo_guardduty.types.equals.serialize_json(value["equals"])
    if "not_equals" in value:
        import capo_guardduty.types.not_equals

        out["notEquals"] = capo_guardduty.types.not_equals.serialize_json(
            value["not_equals"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationFilterCondition:
    out: InvestigationFilterCondition = {}  # type: ignore[typeddict-item]
    if data.get("equals") is not None:
        import capo_guardduty.types.equals

        out["equals"] = capo_guardduty.types.equals.deserialize_json(data["equals"])
    if data.get("notEquals") is not None:
        import capo_guardduty.types.not_equals

        out["not_equals"] = capo_guardduty.types.not_equals.deserialize_json(
            data["notEquals"]
        )
    return out
