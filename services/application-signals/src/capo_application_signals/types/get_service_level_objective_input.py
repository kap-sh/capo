"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GetServiceLevelObjectiveInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.service_level_objective_id


class GetServiceLevelObjectiveInput(TypedDict, closed=True):
    id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId"
    """<p>The ARN or name of the SLO that you want to retrieve information about. You can find the ARNs of SLOs by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListServiceLevelObjectives.html">ListServiceLevelObjectives</a> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceLevelObjectiveInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceLevelObjectiveInput:
    out: GetServiceLevelObjectiveInput = {}  # type: ignore[typeddict-item]
    return out
