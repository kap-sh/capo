"""Generated from Smithy shape ``com.amazonaws.rekognition#DistributeDatasetEntriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.distribute_dataset_metadata_list


class DistributeDatasetEntriesRequest(TypedDict, closed=True):
    datasets: "capo_rekognition.types.distribute_dataset_metadata_list.DistributeDatasetMetadataList"
    """<p>The ARNS for the training dataset and test dataset that you want to use. The datasets must belong to the same project. The test dataset must be empty. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributeDatasetEntriesRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.distribute_dataset_metadata_list

    out["Datasets"] = (
        capo_rekognition.types.distribute_dataset_metadata_list.serialize_aws_json_1_1(
            value["datasets"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DistributeDatasetEntriesRequest:
    out: DistributeDatasetEntriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Datasets") is not None:
        import capo_rekognition.types.distribute_dataset_metadata_list

        out["datasets"] = (
            capo_rekognition.types.distribute_dataset_metadata_list.deserialize_aws_json_1_1(
                data["Datasets"]
            )
        )
    else:
        out["datasets"] = []
    return out
