"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DataSetReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.source
    import capo_iotsitewise.types.string


class DataSetReference(TypedDict, closed=True):
    dataset_arn: NotRequired["capo_iotsitewise.types.string.String"]
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">ARN</a> of the dataset. The format is <code>arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}</code>.</p>"""
    source: NotRequired["capo_iotsitewise.types.source.Source"]
    """<p>The data source for the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetReference) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["datasetArn"] = value["dataset_arn"]
    if "source" in value:
        import capo_iotsitewise.types.source

        out["source"] = capo_iotsitewise.types.source.serialize_json(value["source"])
    return out


def deserialize_json(data: dict) -> DataSetReference:
    out: DataSetReference = {}  # type: ignore[typeddict-item]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    if data.get("source") is not None:
        import capo_iotsitewise.types.source

        out["source"] = capo_iotsitewise.types.source.deserialize_json(data["source"])
    return out
