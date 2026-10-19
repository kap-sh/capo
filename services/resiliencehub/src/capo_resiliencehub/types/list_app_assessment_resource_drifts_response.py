"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppAssessmentResourceDriftsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.resource_drift_list


class ListAppAssessmentResourceDriftsResponse(TypedDict, closed=True):
    resource_drifts: "capo_resiliencehub.types.resource_drift_list.ResourceDriftList"
    """<p>Indicates all the resource drifts detected for an assessed entity.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppAssessmentResourceDriftsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.resource_drift_list

    out["resourceDrifts"] = capo_resiliencehub.types.resource_drift_list.serialize_json(
        value["resource_drifts"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppAssessmentResourceDriftsResponse:
    out: ListAppAssessmentResourceDriftsResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceDrifts") is not None:
        import capo_resiliencehub.types.resource_drift_list

        out["resource_drifts"] = (
            capo_resiliencehub.types.resource_drift_list.deserialize_json(
                data["resourceDrifts"]
            )
        )
    else:
        out["resource_drifts"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
