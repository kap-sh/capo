"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_criterion


class InvestigationFilterCriteria(TypedDict, closed=True):
    criterion: NotRequired[
        "capo_guardduty.types.investigation_criterion.InvestigationCriterion"
    ]
    """<p>A map of investigation attributes to the conditions that they must match. When you specify more than one attribute, an investigation must match the conditions for every attribute. Valid attributes and values:</p> <ul> <li> <p> <code>STATUS</code> – <code>RUNNING</code>, <code>COMPLETED</code>, and <code>FAILED</code>.</p> </li> <li> <p> <code>RISK_LEVEL</code> – <code>Info</code>, <code>Low</code>, <code>Medium</code>, <code>High</code>, and <code>Critical</code>.</p> </li> <li> <p> <code>CONFIDENCE</code> – <code>Unknown</code>, <code>Low</code>, <code>Medium</code>, and <code>High</code>.</p> </li> <li> <p> <code>FINDING_ID</code> – A finding ID, which is 32 lowercase hexadecimal characters.</p> </li> <li> <p> <code>INVESTIGATION_TYPE</code> – <code>FINDING</code>, <code>ACCOUNT</code>, and <code>ORGANIZATION</code>.</p> </li> </ul> <p>Values are case sensitive. GuardDuty sets the risk level, confidence, and investigation type of an investigation only when the investigation completes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationFilterCriteria) -> dict:
    out: dict = {}
    if "criterion" in value:
        import capo_guardduty.types.investigation_criterion

        out["criterion"] = capo_guardduty.types.investigation_criterion.serialize_json(
            value["criterion"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationFilterCriteria:
    out: InvestigationFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("criterion") is not None:
        import capo_guardduty.types.investigation_criterion

        out["criterion"] = (
            capo_guardduty.types.investigation_criterion.deserialize_json(
                data["criterion"]
            )
        )
    return out
