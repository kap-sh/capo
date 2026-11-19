"""Generated from Smithy shape ``com.amazonaws.appstream#DisassociateAppBlockBuilderAppBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.name


class DisassociateAppBlockBuilderAppBlockRequest(TypedDict, closed=True):
    app_block_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the app block.</p>"""
    app_block_builder_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the app block builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateAppBlockBuilderAppBlockRequest) -> dict:
    out: dict = {}
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "app_block_builder_name" in value:
        out["AppBlockBuilderName"] = value["app_block_builder_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateAppBlockBuilderAppBlockRequest:
    out: DisassociateAppBlockBuilderAppBlockRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockArn") is not None:
        out["app_block_arn"] = data["AppBlockArn"]
    if data.get("AppBlockBuilderName") is not None:
        out["app_block_builder_name"] = data["AppBlockBuilderName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateAppBlockBuilderAppBlockRequest) -> dict:
    out: dict = {}
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "app_block_builder_name" in value:
        out["AppBlockBuilderName"] = value["app_block_builder_name"]
    return out


def deserialize_cbor(data: dict) -> DisassociateAppBlockBuilderAppBlockRequest:
    out: DisassociateAppBlockBuilderAppBlockRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockArn") is not None:
        out["app_block_arn"] = data["AppBlockArn"]
    if data.get("AppBlockBuilderName") is not None:
        out["app_block_builder_name"] = data["AppBlockBuilderName"]
    return out
