"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeSMBFileSharesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.file_share_arn_list


class DescribeSMBFileSharesInput(TypedDict, closed=True):
    file_share_arn_list: (
        "capo_storage_gateway.types.file_share_arn_list.FileShareARNList"
    )
    """<p>An array containing the Amazon Resource Name (ARN) of each file share to be described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSMBFileSharesInput) -> dict:
    out: dict = {}
    import capo_storage_gateway.types.file_share_arn_list

    out["FileShareARNList"] = (
        capo_storage_gateway.types.file_share_arn_list.serialize_aws_json_1_1(
            value["file_share_arn_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSMBFileSharesInput:
    out: DescribeSMBFileSharesInput = {}  # type: ignore[typeddict-item]
    if data.get("FileShareARNList") is not None:
        import capo_storage_gateway.types.file_share_arn_list

        out["file_share_arn_list"] = (
            capo_storage_gateway.types.file_share_arn_list.deserialize_aws_json_1_1(
                data["FileShareARNList"]
            )
        )
    else:
        out["file_share_arn_list"] = []
    return out
