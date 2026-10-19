"""Generated from Smithy shape ``com.amazonaws.directconnect#DisassociateConnectionsFromResiliencyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_identifier_list
    import capo_direct_connect.types.idempotency_token
    import capo_direct_connect.types.resiliency_group_id


class DisassociateConnectionsFromResiliencyGroupRequest(TypedDict, closed=True):
    connection_identifiers: (
        "capo_direct_connect.types.connection_identifier_list.ConnectionIdentifierList"
    )
    """<p>The IDs or ARNs of the connections to disassociate from the resiliency group.</p>"""
    resiliency_group_id: (
        "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId"
    )
    """<p>The ID of the resiliency group.</p>"""
    client_token: NotRequired[
        "capo_direct_connect.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateConnectionsFromResiliencyGroupRequest,
) -> dict:
    out: dict = {}
    import capo_direct_connect.types.connection_identifier_list

    out["connectionIdentifiers"] = (
        capo_direct_connect.types.connection_identifier_list.serialize_aws_json_1_1(
            value["connection_identifiers"]
        )
    )
    out["resiliencyGroupId"] = value["resiliency_group_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateConnectionsFromResiliencyGroupRequest:
    out: DisassociateConnectionsFromResiliencyGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionIdentifiers") is not None:
        import capo_direct_connect.types.connection_identifier_list

        out["connection_identifiers"] = (
            capo_direct_connect.types.connection_identifier_list.deserialize_aws_json_1_1(
                data["connectionIdentifiers"]
            )
        )
    else:
        out["connection_identifiers"] = []
    if data.get("resiliencyGroupId") is not None:
        out["resiliency_group_id"] = data["resiliencyGroupId"]
    else:
        out["resiliency_group_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
