"""Generated from Smithy shape ``com.amazonaws.fms#ProtocolsListDataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.list_id
    import capo_fms.types.protocols_list
    import capo_fms.types.resource_arn
    import capo_fms.types.resource_name


class ProtocolsListDataSummary(TypedDict, closed=True):
    list_arn: NotRequired["capo_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the specified protocols list.</p>"""
    list_id: NotRequired["capo_fms.types.list_id.ListId"]
    """<p>The ID of the specified protocols list.</p>"""
    list_name: NotRequired["capo_fms.types.resource_name.ResourceName"]
    """<p>The name of the specified protocols list.</p>"""
    protocols_list: NotRequired["capo_fms.types.protocols_list.ProtocolsList"]
    """<p>An array of protocols in the Firewall Manager protocols list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtocolsListDataSummary) -> dict:
    out: dict = {}
    if "list_arn" in value:
        out["ListArn"] = value["list_arn"]
    if "list_id" in value:
        out["ListId"] = value["list_id"]
    if "list_name" in value:
        out["ListName"] = value["list_name"]
    if "protocols_list" in value:
        import capo_fms.types.protocols_list

        out["ProtocolsList"] = capo_fms.types.protocols_list.serialize_aws_json_1_1(
            value["protocols_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtocolsListDataSummary:
    out: ProtocolsListDataSummary = {}  # type: ignore[typeddict-item]
    if data.get("ListArn") is not None:
        out["list_arn"] = data["ListArn"]
    if data.get("ListId") is not None:
        out["list_id"] = data["ListId"]
    if data.get("ListName") is not None:
        out["list_name"] = data["ListName"]
    if data.get("ProtocolsList") is not None:
        import capo_fms.types.protocols_list

        out["protocols_list"] = capo_fms.types.protocols_list.deserialize_aws_json_1_1(
            data["ProtocolsList"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtocolsListDataSummary) -> dict:
    out: dict = {}
    if "list_arn" in value:
        out["ListArn"] = value["list_arn"]
    if "list_id" in value:
        out["ListId"] = value["list_id"]
    if "list_name" in value:
        out["ListName"] = value["list_name"]
    if "protocols_list" in value:
        import capo_fms.types.protocols_list

        out["ProtocolsList"] = capo_fms.types.protocols_list.serialize_cbor(
            value["protocols_list"]
        )
    return out


def deserialize_cbor(data: dict) -> ProtocolsListDataSummary:
    out: ProtocolsListDataSummary = {}  # type: ignore[typeddict-item]
    if data.get("ListArn") is not None:
        out["list_arn"] = data["ListArn"]
    if data.get("ListId") is not None:
        out["list_id"] = data["ListId"]
    if data.get("ListName") is not None:
        out["list_name"] = data["ListName"]
    if data.get("ProtocolsList") is not None:
        import capo_fms.types.protocols_list

        out["protocols_list"] = capo_fms.types.protocols_list.deserialize_cbor(
            data["ProtocolsList"]
        )
    return out
