"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#HandshakeDetail``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_channel.errors import DeserializationError, SerializationError
from capo_partnercentral_channel.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.program_management_account_handshake_detail
    import capo_partnercentral_channel.types.revoke_service_period_handshake_detail
    import capo_partnercentral_channel.types.start_service_period_handshake_detail


class _HandshakeDetail_startServicePeriodHandshakeDetail(TypedDict, closed=True):
    startServicePeriodHandshakeDetail: "capo_partnercentral_channel.types.start_service_period_handshake_detail.StartServicePeriodHandshakeDetail"


class _HandshakeDetail_revokeServicePeriodHandshakeDetail(TypedDict, closed=True):
    revokeServicePeriodHandshakeDetail: "capo_partnercentral_channel.types.revoke_service_period_handshake_detail.RevokeServicePeriodHandshakeDetail"


class _HandshakeDetail_programManagementAccountHandshakeDetail(TypedDict, closed=True):
    programManagementAccountHandshakeDetail: "capo_partnercentral_channel.types.program_management_account_handshake_detail.ProgramManagementAccountHandshakeDetail"


HandshakeDetail: TypeAlias = (
    _HandshakeDetail_startServicePeriodHandshakeDetail
    | _HandshakeDetail_revokeServicePeriodHandshakeDetail
    | _HandshakeDetail_programManagementAccountHandshakeDetail
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HandshakeDetail) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"HandshakeDetail: cannot serialize unknown variant {value.name!r}"
        )
    elif "startServicePeriodHandshakeDetail" in value:
        import capo_partnercentral_channel.types.start_service_period_handshake_detail

        return {
            "startServicePeriodHandshakeDetail": capo_partnercentral_channel.types.start_service_period_handshake_detail.serialize_aws_json_1_0(
                value["startServicePeriodHandshakeDetail"]
            )
        }
    elif "revokeServicePeriodHandshakeDetail" in value:
        import capo_partnercentral_channel.types.revoke_service_period_handshake_detail

        return {
            "revokeServicePeriodHandshakeDetail": capo_partnercentral_channel.types.revoke_service_period_handshake_detail.serialize_aws_json_1_0(
                value["revokeServicePeriodHandshakeDetail"]
            )
        }
    elif "programManagementAccountHandshakeDetail" in value:
        import capo_partnercentral_channel.types.program_management_account_handshake_detail

        return {
            "programManagementAccountHandshakeDetail": capo_partnercentral_channel.types.program_management_account_handshake_detail.serialize_aws_json_1_0(
                value["programManagementAccountHandshakeDetail"]
            )
        }
    else:
        raise SerializationError("HandshakeDetail: no variant present")


def deserialize_aws_json_1_0(data: dict) -> HandshakeDetail:
    if data.get("startServicePeriodHandshakeDetail") is not None:
        import capo_partnercentral_channel.types.start_service_period_handshake_detail

        return {
            "startServicePeriodHandshakeDetail": capo_partnercentral_channel.types.start_service_period_handshake_detail.deserialize_aws_json_1_0(
                data["startServicePeriodHandshakeDetail"]
            )
        }
    elif data.get("revokeServicePeriodHandshakeDetail") is not None:
        import capo_partnercentral_channel.types.revoke_service_period_handshake_detail

        return {
            "revokeServicePeriodHandshakeDetail": capo_partnercentral_channel.types.revoke_service_period_handshake_detail.deserialize_aws_json_1_0(
                data["revokeServicePeriodHandshakeDetail"]
            )
        }
    elif data.get("programManagementAccountHandshakeDetail") is not None:
        import capo_partnercentral_channel.types.program_management_account_handshake_detail

        return {
            "programManagementAccountHandshakeDetail": capo_partnercentral_channel.types.program_management_account_handshake_detail.deserialize_aws_json_1_0(
                data["programManagementAccountHandshakeDetail"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("HandshakeDetail: no recognized variant key")
