"""Generated from Smithy shape ``com.amazonaws.backupgateway#ListGatewaysOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateways
    import capo_backup_gateway.types.next_token


class ListGatewaysOutput(TypedDict, closed=True):
    gateways: NotRequired["capo_backup_gateway.types.gateways.Gateways"]
    """<p>A list of your gateways.</p>"""
    next_token: NotRequired["capo_backup_gateway.types.next_token.NextToken"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListGatewaysOutput) -> dict:
    out: dict = {}
    if "gateways" in value:
        import capo_backup_gateway.types.gateways

        out["Gateways"] = capo_backup_gateway.types.gateways.serialize_aws_json_1_0(
            value["gateways"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListGatewaysOutput:
    out: ListGatewaysOutput = {}  # type: ignore[typeddict-item]
    if data.get("Gateways") is not None:
        import capo_backup_gateway.types.gateways

        out["gateways"] = capo_backup_gateway.types.gateways.deserialize_aws_json_1_0(
            data["Gateways"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListGatewaysOutput) -> dict:
    out: dict = {}
    if "gateways" in value:
        import capo_backup_gateway.types.gateways

        out["Gateways"] = capo_backup_gateway.types.gateways.serialize_cbor(
            value["gateways"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListGatewaysOutput:
    out: ListGatewaysOutput = {}  # type: ignore[typeddict-item]
    if data.get("Gateways") is not None:
        import capo_backup_gateway.types.gateways

        out["gateways"] = capo_backup_gateway.types.gateways.deserialize_cbor(
            data["Gateways"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
