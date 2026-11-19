"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MessageData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.message_data_code
    import capo_cloudwatch.types.message_data_value


class MessageData(TypedDict, closed=True):
    code: NotRequired["capo_cloudwatch.types.message_data_code.MessageDataCode"]
    """<p>The error code or status code associated with the message.</p>"""
    value: NotRequired["capo_cloudwatch.types.message_data_value.MessageDataValue"]
    """<p>The message text.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageData) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MessageData:
    out: MessageData = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MessageData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        pairs.append((f"{key_prefix}Code", str(value["code"])))
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_query(el: Element) -> MessageData:
    out: MessageData = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MessageData) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> MessageData:
    out: MessageData = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
