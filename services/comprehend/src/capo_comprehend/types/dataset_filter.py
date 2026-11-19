"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.dataset_status
    import capo_comprehend.types.dataset_type
    import capo_comprehend.types.timestamp


class DatasetFilter(TypedDict, closed=True):
    status: NotRequired["capo_comprehend.types.dataset_status.DatasetStatus"]
    """<p>Filter the datasets based on the dataset status.</p>"""
    dataset_type: NotRequired["capo_comprehend.types.dataset_type.DatasetType"]
    """<p>Filter the datasets based on the dataset type.</p>"""
    creation_time_after: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Filter the datasets to include datasets created after the specified time.</p>"""
    creation_time_before: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Filter the datasets to include datasets created before the specified time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_comprehend.types.dataset_status

        out["Status"] = capo_comprehend.types.dataset_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "dataset_type" in value:
        import capo_comprehend.types.dataset_type

        out["DatasetType"] = capo_comprehend.types.dataset_type.serialize_aws_json_1_1(
            value["dataset_type"]
        )
    if "creation_time_after" in value:
        import capo_comprehend.types.timestamp

        out["CreationTimeAfter"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import capo_comprehend.types.timestamp

        out["CreationTimeBefore"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetFilter:
    out: DatasetFilter = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_comprehend.types.dataset_status

        out["status"] = capo_comprehend.types.dataset_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("DatasetType") is not None:
        import capo_comprehend.types.dataset_type

        out["dataset_type"] = (
            capo_comprehend.types.dataset_type.deserialize_aws_json_1_1(
                data["DatasetType"]
            )
        )
    if data.get("CreationTimeAfter") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time_after"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if data.get("CreationTimeBefore") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time_before"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DatasetFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_comprehend.types.dataset_status

        out["Status"] = capo_comprehend.types.dataset_status.serialize_cbor(
            value["status"]
        )
    if "dataset_type" in value:
        import capo_comprehend.types.dataset_type

        out["DatasetType"] = capo_comprehend.types.dataset_type.serialize_cbor(
            value["dataset_type"]
        )
    if "creation_time_after" in value:
        import capo_comprehend.types.timestamp

        out["CreationTimeAfter"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["creation_time_after"]
        )
    if "creation_time_before" in value:
        import capo_comprehend.types.timestamp

        out["CreationTimeBefore"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["creation_time_before"]
        )
    return out


def deserialize_cbor(data: dict) -> DatasetFilter:
    out: DatasetFilter = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_comprehend.types.dataset_status

        out["status"] = capo_comprehend.types.dataset_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("DatasetType") is not None:
        import capo_comprehend.types.dataset_type

        out["dataset_type"] = capo_comprehend.types.dataset_type.deserialize_cbor(
            data["DatasetType"]
        )
    if data.get("CreationTimeAfter") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time_after"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["CreationTimeAfter"]
        )
    if data.get("CreationTimeBefore") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time_before"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["CreationTimeBefore"]
        )
    return out
