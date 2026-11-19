"""Generated from Smithy shape ``com.amazonaws.comprehend#ListPiiEntitiesDetectionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.pii_entities_detection_job_properties_list
    import capo_comprehend.types.string


class ListPiiEntitiesDetectionJobsResponse(TypedDict, closed=True):
    pii_entities_detection_job_properties_list: NotRequired[
        "capo_comprehend.types.pii_entities_detection_job_properties_list.PiiEntitiesDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPiiEntitiesDetectionJobsResponse) -> dict:
    out: dict = {}
    if "pii_entities_detection_job_properties_list" in value:
        import capo_comprehend.types.pii_entities_detection_job_properties_list

        out["PiiEntitiesDetectionJobPropertiesList"] = (
            capo_comprehend.types.pii_entities_detection_job_properties_list.serialize_aws_json_1_1(
                value["pii_entities_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPiiEntitiesDetectionJobsResponse:
    out: ListPiiEntitiesDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("PiiEntitiesDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.pii_entities_detection_job_properties_list

        out["pii_entities_detection_job_properties_list"] = (
            capo_comprehend.types.pii_entities_detection_job_properties_list.deserialize_aws_json_1_1(
                data["PiiEntitiesDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPiiEntitiesDetectionJobsResponse) -> dict:
    out: dict = {}
    if "pii_entities_detection_job_properties_list" in value:
        import capo_comprehend.types.pii_entities_detection_job_properties_list

        out["PiiEntitiesDetectionJobPropertiesList"] = (
            capo_comprehend.types.pii_entities_detection_job_properties_list.serialize_cbor(
                value["pii_entities_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListPiiEntitiesDetectionJobsResponse:
    out: ListPiiEntitiesDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("PiiEntitiesDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.pii_entities_detection_job_properties_list

        out["pii_entities_detection_job_properties_list"] = (
            capo_comprehend.types.pii_entities_detection_job_properties_list.deserialize_cbor(
                data["PiiEntitiesDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
