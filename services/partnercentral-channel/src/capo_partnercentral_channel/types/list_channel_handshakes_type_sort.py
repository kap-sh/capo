"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListChannelHandshakesTypeSort``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_channel.errors import DeserializationError, SerializationError
from capo_partnercentral_channel.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.program_management_account_type_sort
    import capo_partnercentral_channel.types.revoke_service_period_type_sort
    import capo_partnercentral_channel.types.start_service_period_type_sort


class ListChannelHandshakesTypeSortStartServicePeriodTypeSortMember(
    TypedDict, closed=True
):
    startServicePeriodTypeSort: "capo_partnercentral_channel.types.start_service_period_type_sort.StartServicePeriodTypeSort"


class ListChannelHandshakesTypeSortRevokeServicePeriodTypeSortMember(
    TypedDict, closed=True
):
    revokeServicePeriodTypeSort: "capo_partnercentral_channel.types.revoke_service_period_type_sort.RevokeServicePeriodTypeSort"


class ListChannelHandshakesTypeSortProgramManagementAccountTypeSortMember(
    TypedDict, closed=True
):
    programManagementAccountTypeSort: "capo_partnercentral_channel.types.program_management_account_type_sort.ProgramManagementAccountTypeSort"


ListChannelHandshakesTypeSort: TypeAlias = (
    ListChannelHandshakesTypeSortStartServicePeriodTypeSortMember
    | ListChannelHandshakesTypeSortRevokeServicePeriodTypeSortMember
    | ListChannelHandshakesTypeSortProgramManagementAccountTypeSortMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListChannelHandshakesTypeSort) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ListChannelHandshakesTypeSort: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "startServicePeriodTypeSort" in value:
        import capo_partnercentral_channel.types.start_service_period_type_sort

        return {
            "startServicePeriodTypeSort": capo_partnercentral_channel.types.start_service_period_type_sort.serialize_aws_json_1_0(
                value["startServicePeriodTypeSort"]
            )
        }
    elif "revokeServicePeriodTypeSort" in value:
        import capo_partnercentral_channel.types.revoke_service_period_type_sort

        return {
            "revokeServicePeriodTypeSort": capo_partnercentral_channel.types.revoke_service_period_type_sort.serialize_aws_json_1_0(
                value["revokeServicePeriodTypeSort"]
            )
        }
    elif "programManagementAccountTypeSort" in value:
        import capo_partnercentral_channel.types.program_management_account_type_sort

        return {
            "programManagementAccountTypeSort": capo_partnercentral_channel.types.program_management_account_type_sort.serialize_aws_json_1_0(
                value["programManagementAccountTypeSort"]
            )
        }
    else:
        raise SerializationError("ListChannelHandshakesTypeSort: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ListChannelHandshakesTypeSort:
    if data.get("startServicePeriodTypeSort") is not None:
        import capo_partnercentral_channel.types.start_service_period_type_sort

        return {
            "startServicePeriodTypeSort": capo_partnercentral_channel.types.start_service_period_type_sort.deserialize_aws_json_1_0(
                data["startServicePeriodTypeSort"]
            )
        }
    elif data.get("revokeServicePeriodTypeSort") is not None:
        import capo_partnercentral_channel.types.revoke_service_period_type_sort

        return {
            "revokeServicePeriodTypeSort": capo_partnercentral_channel.types.revoke_service_period_type_sort.deserialize_aws_json_1_0(
                data["revokeServicePeriodTypeSort"]
            )
        }
    elif data.get("programManagementAccountTypeSort") is not None:
        import capo_partnercentral_channel.types.program_management_account_type_sort

        return {
            "programManagementAccountTypeSort": capo_partnercentral_channel.types.program_management_account_type_sort.deserialize_aws_json_1_0(
                data["programManagementAccountTypeSort"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ListChannelHandshakesTypeSort: no recognized variant key"
        )
