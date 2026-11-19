"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.dataset_properties


class DescribeDatasetResponse(TypedDict, closed=True):
    dataset_properties: NotRequired[
        "capo_comprehend.types.dataset_properties.DatasetProperties"
    ]
    """<p>The dataset properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_properties" in value:
        import capo_comprehend.types.dataset_properties

        out["DatasetProperties"] = (
            capo_comprehend.types.dataset_properties.serialize_aws_json_1_1(
                value["dataset_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatasetProperties") is not None:
        import capo_comprehend.types.dataset_properties

        out["dataset_properties"] = (
            capo_comprehend.types.dataset_properties.deserialize_aws_json_1_1(
                data["DatasetProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_properties" in value:
        import capo_comprehend.types.dataset_properties

        out["DatasetProperties"] = (
            capo_comprehend.types.dataset_properties.serialize_cbor(
                value["dataset_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatasetProperties") is not None:
        import capo_comprehend.types.dataset_properties

        out["dataset_properties"] = (
            capo_comprehend.types.dataset_properties.deserialize_cbor(
                data["DatasetProperties"]
            )
        )
    return out
