"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeDirectoryDataAccessResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.data_access_status


class DescribeDirectoryDataAccessResult(TypedDict, closed=True):
    data_access_status: NotRequired[
        "capo_directory_service.types.data_access_status.DataAccessStatus"
    ]
    """<p>The current status of data access through the Directory Service Data API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectoryDataAccessResult) -> dict:
    out: dict = {}
    if "data_access_status" in value:
        import capo_directory_service.types.data_access_status

        out["DataAccessStatus"] = (
            capo_directory_service.types.data_access_status.serialize_aws_json_1_1(
                value["data_access_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectoryDataAccessResult:
    out: DescribeDirectoryDataAccessResult = {}  # type: ignore[typeddict-item]
    if data.get("DataAccessStatus") is not None:
        import capo_directory_service.types.data_access_status

        out["data_access_status"] = (
            capo_directory_service.types.data_access_status.deserialize_aws_json_1_1(
                data["DataAccessStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDirectoryDataAccessResult) -> dict:
    out: dict = {}
    if "data_access_status" in value:
        import capo_directory_service.types.data_access_status

        out["DataAccessStatus"] = (
            capo_directory_service.types.data_access_status.serialize_cbor(
                value["data_access_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeDirectoryDataAccessResult:
    out: DescribeDirectoryDataAccessResult = {}  # type: ignore[typeddict-item]
    if data.get("DataAccessStatus") is not None:
        import capo_directory_service.types.data_access_status

        out["data_access_status"] = (
            capo_directory_service.types.data_access_status.deserialize_cbor(
                data["DataAccessStatus"]
            )
        )
    return out
