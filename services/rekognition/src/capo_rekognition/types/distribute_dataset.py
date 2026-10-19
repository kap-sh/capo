"""Generated from Smithy shape ``com.amazonaws.rekognition#DistributeDataset``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_arn


class DistributeDataset(TypedDict, closed=True):
    arn: "capo_rekognition.types.dataset_arn.DatasetArn"
    """<p>The Amazon Resource Name (ARN) of the dataset that you want to use. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributeDataset) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DistributeDataset:
    out: DistributeDataset = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
