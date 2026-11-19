"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEventsDetectionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.events_detection_job_properties_list
    import capo_comprehend.types.string


class ListEventsDetectionJobsResponse(TypedDict, closed=True):
    events_detection_job_properties_list: NotRequired[
        "capo_comprehend.types.events_detection_job_properties_list.EventsDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventsDetectionJobsResponse) -> dict:
    out: dict = {}
    if "events_detection_job_properties_list" in value:
        import capo_comprehend.types.events_detection_job_properties_list

        out["EventsDetectionJobPropertiesList"] = (
            capo_comprehend.types.events_detection_job_properties_list.serialize_aws_json_1_1(
                value["events_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventsDetectionJobsResponse:
    out: ListEventsDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventsDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.events_detection_job_properties_list

        out["events_detection_job_properties_list"] = (
            capo_comprehend.types.events_detection_job_properties_list.deserialize_aws_json_1_1(
                data["EventsDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListEventsDetectionJobsResponse) -> dict:
    out: dict = {}
    if "events_detection_job_properties_list" in value:
        import capo_comprehend.types.events_detection_job_properties_list

        out["EventsDetectionJobPropertiesList"] = (
            capo_comprehend.types.events_detection_job_properties_list.serialize_cbor(
                value["events_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListEventsDetectionJobsResponse:
    out: ListEventsDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventsDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.events_detection_job_properties_list

        out["events_detection_job_properties_list"] = (
            capo_comprehend.types.events_detection_job_properties_list.deserialize_cbor(
                data["EventsDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
