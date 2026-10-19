"""Generated from Smithy shape ``com.amazonaws.storagegateway#NotifyWhenUploadedInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.file_share_arn


class NotifyWhenUploadedInput(TypedDict, closed=True):
    file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyWhenUploadedInput) -> dict:
    out: dict = {}
    out["FileShareARN"] = value["file_share_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyWhenUploadedInput:
    out: NotifyWhenUploadedInput = {}  # type: ignore[typeddict-item]
    if data.get("FileShareARN") is not None:
        out["file_share_arn"] = data["FileShareARN"]
    else:
        out["file_share_arn"] = ""
    return out
