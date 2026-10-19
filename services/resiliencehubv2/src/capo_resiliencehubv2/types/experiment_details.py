"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ExperimentDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn


class ExperimentDetails(TypedDict, closed=True):
    experiment_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the AWS FIS experiment.</p>"""
    details: NotRequired["str"]
    """<p>Additional details about the experiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentDetails) -> dict:
    out: dict = {}
    out["experimentArn"] = value["experiment_arn"]
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_json(data: dict) -> ExperimentDetails:
    out: ExperimentDetails = {}  # type: ignore[typeddict-item]
    if data.get("experimentArn") is not None:
        out["experiment_arn"] = data["experimentArn"]
    else:
        out["experiment_arn"] = ""
    if data.get("details") is not None:
        out["details"] = data["details"]
    return out
