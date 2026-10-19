"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListSensorStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.ingestion_job_id
    import capo_lookoutequipment.types.max_results
    import capo_lookoutequipment.types.next_token


class ListSensorStatisticsRequest(TypedDict, closed=True):
    dataset_name: "capo_lookoutequipment.types.dataset_name.DatasetName"
    """<p> The name of the dataset associated with the list of Sensor Statistics. </p>"""
    ingestion_job_id: NotRequired[
        "capo_lookoutequipment.types.ingestion_job_id.IngestionJobId"
    ]
    """<p> The ingestion job id associated with the list of Sensor Statistics. To get sensor statistics for a particular ingestion job id, both dataset name and ingestion job id must be submitted as inputs. </p>"""
    max_results: NotRequired["capo_lookoutequipment.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of sensors for which to retrieve statistics. </p>"""
    next_token: NotRequired["capo_lookoutequipment.types.next_token.NextToken"]
    """<p>An opaque pagination token indicating where to continue the listing of sensor statistics. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSensorStatisticsRequest) -> dict:
    out: dict = {}
    out["DatasetName"] = value["dataset_name"]
    if "ingestion_job_id" in value:
        out["IngestionJobId"] = value["ingestion_job_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSensorStatisticsRequest:
    out: ListSensorStatisticsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    else:
        out["dataset_name"] = ""
    if data.get("IngestionJobId") is not None:
        out["ingestion_job_id"] = data["IngestionJobId"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
