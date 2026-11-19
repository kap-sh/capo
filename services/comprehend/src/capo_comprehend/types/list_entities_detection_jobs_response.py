"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEntitiesDetectionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.entities_detection_job_properties_list
    import capo_comprehend.types.string


class ListEntitiesDetectionJobsResponse(TypedDict, closed=True):
    entities_detection_job_properties_list: NotRequired[
        "capo_comprehend.types.entities_detection_job_properties_list.EntitiesDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntitiesDetectionJobsResponse) -> dict:
    out: dict = {}
    if "entities_detection_job_properties_list" in value:
        import capo_comprehend.types.entities_detection_job_properties_list

        out["EntitiesDetectionJobPropertiesList"] = (
            capo_comprehend.types.entities_detection_job_properties_list.serialize_aws_json_1_1(
                value["entities_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntitiesDetectionJobsResponse:
    out: ListEntitiesDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EntitiesDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.entities_detection_job_properties_list

        out["entities_detection_job_properties_list"] = (
            capo_comprehend.types.entities_detection_job_properties_list.deserialize_aws_json_1_1(
                data["EntitiesDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListEntitiesDetectionJobsResponse) -> dict:
    out: dict = {}
    if "entities_detection_job_properties_list" in value:
        import capo_comprehend.types.entities_detection_job_properties_list

        out["EntitiesDetectionJobPropertiesList"] = (
            capo_comprehend.types.entities_detection_job_properties_list.serialize_cbor(
                value["entities_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListEntitiesDetectionJobsResponse:
    out: ListEntitiesDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EntitiesDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.entities_detection_job_properties_list

        out["entities_detection_job_properties_list"] = (
            capo_comprehend.types.entities_detection_job_properties_list.deserialize_cbor(
                data["EntitiesDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
