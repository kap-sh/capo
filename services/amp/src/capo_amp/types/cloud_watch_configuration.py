"""Generated from Smithy shape ``com.amazonaws.amp#CloudWatchConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.cloud_watch_dataset_arn


class CloudWatchConfiguration(TypedDict, closed=True):
    dataset_arn: "capo_amp.types.cloud_watch_dataset_arn.CloudWatchDatasetArn"
    """<p>The Amazon Resource Name (ARN) of the CloudWatch dataset. To use the default dataset, specify <code>arn:aws:cloudwatch:&lt;region&gt;:&lt;account-id&gt;:dataset/default</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchConfiguration) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    return out


def deserialize_json(data: dict) -> CloudWatchConfiguration:
    out: CloudWatchConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        out["dataset_arn"] = ""
    return out
