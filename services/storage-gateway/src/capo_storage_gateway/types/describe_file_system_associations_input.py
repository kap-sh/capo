"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeFileSystemAssociationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.file_system_association_arn_list


class DescribeFileSystemAssociationsInput(TypedDict, closed=True):
    file_system_association_arn_list: "capo_storage_gateway.types.file_system_association_arn_list.FileSystemAssociationARNList"
    """<p>An array containing the Amazon Resource Name (ARN) of each file system association to be described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileSystemAssociationsInput) -> dict:
    out: dict = {}
    import capo_storage_gateway.types.file_system_association_arn_list

    out["FileSystemAssociationARNList"] = (
        capo_storage_gateway.types.file_system_association_arn_list.serialize_aws_json_1_1(
            value["file_system_association_arn_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileSystemAssociationsInput:
    out: DescribeFileSystemAssociationsInput = {}  # type: ignore[typeddict-item]
    if data.get("FileSystemAssociationARNList") is not None:
        import capo_storage_gateway.types.file_system_association_arn_list

        out["file_system_association_arn_list"] = (
            capo_storage_gateway.types.file_system_association_arn_list.deserialize_aws_json_1_1(
                data["FileSystemAssociationARNList"]
            )
        )
    else:
        out["file_system_association_arn_list"] = []
    return out
