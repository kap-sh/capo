"""Generated from Smithy shape ``com.amazonaws.codeconnections#Connection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.account_id
    import capo_codeconnections.types.connection_arn
    import capo_codeconnections.types.connection_name
    import capo_codeconnections.types.connection_status
    import capo_codeconnections.types.host_arn
    import capo_codeconnections.types.provider_type


class Connection(TypedDict, closed=True):
    connection_name: NotRequired[
        "capo_codeconnections.types.connection_name.ConnectionName"
    ]
    """<p>The name of the connection. Connection names must be unique in an Amazon Web Services account.</p>"""
    connection_arn: NotRequired[
        "capo_codeconnections.types.connection_arn.ConnectionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the connection. The ARN is used as the connection reference when the connection is shared between Amazon Web Services services.</p> <note> <p>The ARN is never reused if the connection is deleted.</p> </note>"""
    provider_type: NotRequired["capo_codeconnections.types.provider_type.ProviderType"]
    """<p>The name of the external provider where your third-party code repository is configured.</p>"""
    owner_account_id: NotRequired["capo_codeconnections.types.account_id.AccountId"]
    """<p>The identifier of the external provider where your third-party code repository is configured. For Bitbucket, this is the account ID of the owner of the Bitbucket repository.</p>"""
    connection_status: NotRequired[
        "capo_codeconnections.types.connection_status.ConnectionStatus"
    ]
    """<p>The current status of the connection. </p>"""
    host_arn: NotRequired["capo_codeconnections.types.host_arn.HostArn"]
    """<p>The Amazon Resource Name (ARN) of the host associated with the connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Connection) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "provider_type" in value:
        import capo_codeconnections.types.provider_type

        out["ProviderType"] = (
            capo_codeconnections.types.provider_type.serialize_aws_json_1_0(
                value["provider_type"]
            )
        )
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "connection_status" in value:
        import capo_codeconnections.types.connection_status

        out["ConnectionStatus"] = (
            capo_codeconnections.types.connection_status.serialize_aws_json_1_0(
                value["connection_status"]
            )
        )
    if "host_arn" in value:
        out["HostArn"] = value["host_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    if data.get("ProviderType") is not None:
        import capo_codeconnections.types.provider_type

        out["provider_type"] = (
            capo_codeconnections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("ConnectionStatus") is not None:
        import capo_codeconnections.types.connection_status

        out["connection_status"] = (
            capo_codeconnections.types.connection_status.deserialize_aws_json_1_0(
                data["ConnectionStatus"]
            )
        )
    if data.get("HostArn") is not None:
        out["host_arn"] = data["HostArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Connection) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "provider_type" in value:
        import capo_codeconnections.types.provider_type

        out["ProviderType"] = capo_codeconnections.types.provider_type.serialize_cbor(
            value["provider_type"]
        )
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "connection_status" in value:
        import capo_codeconnections.types.connection_status

        out["ConnectionStatus"] = (
            capo_codeconnections.types.connection_status.serialize_cbor(
                value["connection_status"]
            )
        )
    if "host_arn" in value:
        out["HostArn"] = value["host_arn"]
    return out


def deserialize_cbor(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    if data.get("ProviderType") is not None:
        import capo_codeconnections.types.provider_type

        out["provider_type"] = (
            capo_codeconnections.types.provider_type.deserialize_cbor(
                data["ProviderType"]
            )
        )
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("ConnectionStatus") is not None:
        import capo_codeconnections.types.connection_status

        out["connection_status"] = (
            capo_codeconnections.types.connection_status.deserialize_cbor(
                data["ConnectionStatus"]
            )
        )
    if data.get("HostArn") is not None:
        out["host_arn"] = data["HostArn"]
    return out
