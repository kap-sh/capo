"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListChannelHandshakesTypeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_channel.errors import DeserializationError, SerializationError
from capo_partnercentral_channel.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.program_management_account_type_filters
    import capo_partnercentral_channel.types.revoke_service_period_type_filters
    import capo_partnercentral_channel.types.start_service_period_type_filters


class _ListChannelHandshakesTypeFilters_startServicePeriodTypeFilters(
    TypedDict, closed=True
):
    startServicePeriodTypeFilters: "capo_partnercentral_channel.types.start_service_period_type_filters.StartServicePeriodTypeFilters"


class _ListChannelHandshakesTypeFilters_revokeServicePeriodTypeFilters(
    TypedDict, closed=True
):
    revokeServicePeriodTypeFilters: "capo_partnercentral_channel.types.revoke_service_period_type_filters.RevokeServicePeriodTypeFilters"


class _ListChannelHandshakesTypeFilters_programManagementAccountTypeFilters(
    TypedDict, closed=True
):
    programManagementAccountTypeFilters: "capo_partnercentral_channel.types.program_management_account_type_filters.ProgramManagementAccountTypeFilters"


ListChannelHandshakesTypeFilters: TypeAlias = (
    _ListChannelHandshakesTypeFilters_startServicePeriodTypeFilters
    | _ListChannelHandshakesTypeFilters_revokeServicePeriodTypeFilters
    | _ListChannelHandshakesTypeFilters_programManagementAccountTypeFilters
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListChannelHandshakesTypeFilters) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ListChannelHandshakesTypeFilters: cannot serialize unknown variant {value.name!r}"
        )
    elif "startServicePeriodTypeFilters" in value:
        import capo_partnercentral_channel.types.start_service_period_type_filters

        return {
            "startServicePeriodTypeFilters": capo_partnercentral_channel.types.start_service_period_type_filters.serialize_aws_json_1_0(
                value["startServicePeriodTypeFilters"]
            )
        }
    elif "revokeServicePeriodTypeFilters" in value:
        import capo_partnercentral_channel.types.revoke_service_period_type_filters

        return {
            "revokeServicePeriodTypeFilters": capo_partnercentral_channel.types.revoke_service_period_type_filters.serialize_aws_json_1_0(
                value["revokeServicePeriodTypeFilters"]
            )
        }
    elif "programManagementAccountTypeFilters" in value:
        import capo_partnercentral_channel.types.program_management_account_type_filters

        return {
            "programManagementAccountTypeFilters": capo_partnercentral_channel.types.program_management_account_type_filters.serialize_aws_json_1_0(
                value["programManagementAccountTypeFilters"]
            )
        }
    else:
        raise SerializationError("ListChannelHandshakesTypeFilters: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ListChannelHandshakesTypeFilters:
    if data.get("startServicePeriodTypeFilters") is not None:
        import capo_partnercentral_channel.types.start_service_period_type_filters

        return {
            "startServicePeriodTypeFilters": capo_partnercentral_channel.types.start_service_period_type_filters.deserialize_aws_json_1_0(
                data["startServicePeriodTypeFilters"]
            )
        }
    elif data.get("revokeServicePeriodTypeFilters") is not None:
        import capo_partnercentral_channel.types.revoke_service_period_type_filters

        return {
            "revokeServicePeriodTypeFilters": capo_partnercentral_channel.types.revoke_service_period_type_filters.deserialize_aws_json_1_0(
                data["revokeServicePeriodTypeFilters"]
            )
        }
    elif data.get("programManagementAccountTypeFilters") is not None:
        import capo_partnercentral_channel.types.program_management_account_type_filters

        return {
            "programManagementAccountTypeFilters": capo_partnercentral_channel.types.program_management_account_type_filters.deserialize_aws_json_1_0(
                data["programManagementAccountTypeFilters"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "ListChannelHandshakesTypeFilters: no recognized variant key"
        )
