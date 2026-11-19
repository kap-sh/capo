"""Generated from Smithy shape ``com.amazonaws.comprehend#ListKeyPhrasesDetectionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.key_phrases_detection_job_properties_list
    import capo_comprehend.types.string


class ListKeyPhrasesDetectionJobsResponse(TypedDict, closed=True):
    key_phrases_detection_job_properties_list: NotRequired[
        "capo_comprehend.types.key_phrases_detection_job_properties_list.KeyPhrasesDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListKeyPhrasesDetectionJobsResponse) -> dict:
    out: dict = {}
    if "key_phrases_detection_job_properties_list" in value:
        import capo_comprehend.types.key_phrases_detection_job_properties_list

        out["KeyPhrasesDetectionJobPropertiesList"] = (
            capo_comprehend.types.key_phrases_detection_job_properties_list.serialize_aws_json_1_1(
                value["key_phrases_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListKeyPhrasesDetectionJobsResponse:
    out: ListKeyPhrasesDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyPhrasesDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.key_phrases_detection_job_properties_list

        out["key_phrases_detection_job_properties_list"] = (
            capo_comprehend.types.key_phrases_detection_job_properties_list.deserialize_aws_json_1_1(
                data["KeyPhrasesDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListKeyPhrasesDetectionJobsResponse) -> dict:
    out: dict = {}
    if "key_phrases_detection_job_properties_list" in value:
        import capo_comprehend.types.key_phrases_detection_job_properties_list

        out["KeyPhrasesDetectionJobPropertiesList"] = (
            capo_comprehend.types.key_phrases_detection_job_properties_list.serialize_cbor(
                value["key_phrases_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListKeyPhrasesDetectionJobsResponse:
    out: ListKeyPhrasesDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyPhrasesDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.key_phrases_detection_job_properties_list

        out["key_phrases_detection_job_properties_list"] = (
            capo_comprehend.types.key_phrases_detection_job_properties_list.deserialize_cbor(
                data["KeyPhrasesDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
