"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#CancelConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.connection_id
    import capo_partnercentral_account.types.connection_type


class CancelConnectionRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection exists.</p>"""
    identifier: "capo_partnercentral_account.types.connection_id.ConnectionId"
    """<p>The unique identifier of the connection to cancel.</p>"""
    connection_type: "capo_partnercentral_account.types.connection_type.ConnectionType"
    """<p>The type of connection to cancel (e.g., reseller, distributor, technology partner).</p>"""
    reason: "str"
    """<p>The reason for canceling the connection, providing context for the termination.</p>"""
    client_token: "capo_partnercentral_account.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelConnectionRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    import capo_partnercentral_account.types.connection_type

    out["ConnectionType"] = (
        capo_partnercentral_account.types.connection_type.serialize_aws_json_1_0(
            value["connection_type"]
        )
    )
    out["Reason"] = value["reason"]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelConnectionRequest:
    out: CancelConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("ConnectionType") is not None:
        import capo_partnercentral_account.types.connection_type

        out["connection_type"] = (
            capo_partnercentral_account.types.connection_type.deserialize_aws_json_1_0(
                data["ConnectionType"]
            )
        )
    else:
        import typing

        out["connection_type"] = typing.cast(
            "capo_partnercentral_account.types.connection_type.ConnectionType", ""
        )
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    else:
        out["reason"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    return out
