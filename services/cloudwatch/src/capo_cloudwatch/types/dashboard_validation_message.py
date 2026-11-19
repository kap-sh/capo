"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DashboardValidationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.data_path
    import capo_cloudwatch.types.message


class DashboardValidationMessage(TypedDict, closed=True):
    data_path: NotRequired["capo_cloudwatch.types.data_path.DataPath"]
    """<p>The data path related to the message.</p>"""
    message: NotRequired["capo_cloudwatch.types.message.Message"]
    """<p>A message describing the error or warning.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardValidationMessage) -> dict:
    out: dict = {}
    if "data_path" in value:
        out["DataPath"] = value["data_path"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DashboardValidationMessage:
    out: DashboardValidationMessage = {}  # type: ignore[typeddict-item]
    if data.get("DataPath") is not None:
        out["data_path"] = data["DataPath"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DashboardValidationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "data_path" in value:
        pairs.append((f"{key_prefix}DataPath", str(value["data_path"])))
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> DashboardValidationMessage:
    out: DashboardValidationMessage = {}  # type: ignore[typeddict-item]
    child_data_path = el.find("DataPath")
    if child_data_path is not None:
        out["data_path"] = str(child_data_path.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DashboardValidationMessage) -> dict:
    out: dict = {}
    if "data_path" in value:
        out["DataPath"] = value["data_path"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> DashboardValidationMessage:
    out: DashboardValidationMessage = {}  # type: ignore[typeddict-item]
    if data.get("DataPath") is not None:
        out["data_path"] = data["DataPath"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
