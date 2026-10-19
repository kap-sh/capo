"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#SupportPlan``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_channel.errors import DeserializationError, SerializationError
from capo_partnercentral_channel.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.partner_led_support
    import capo_partnercentral_channel.types.resold_enterprise
    import capo_partnercentral_channel.types.resold_unified_operations


class _SupportPlan_resoldEnterprise(TypedDict, closed=True):
    resoldEnterprise: (
        "capo_partnercentral_channel.types.resold_enterprise.ResoldEnterprise"
    )


class _SupportPlan_partnerLedSupport(TypedDict, closed=True):
    partnerLedSupport: (
        "capo_partnercentral_channel.types.partner_led_support.PartnerLedSupport"
    )


class _SupportPlan_resoldUnifiedOperations(TypedDict, closed=True):
    resoldUnifiedOperations: "capo_partnercentral_channel.types.resold_unified_operations.ResoldUnifiedOperations"


SupportPlan: TypeAlias = (
    _SupportPlan_resoldEnterprise
    | _SupportPlan_partnerLedSupport
    | _SupportPlan_resoldUnifiedOperations
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportPlan) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SupportPlan: cannot serialize unknown variant {value.name!r}"
        )
    elif "resoldEnterprise" in value:
        import capo_partnercentral_channel.types.resold_enterprise

        return {
            "resoldEnterprise": capo_partnercentral_channel.types.resold_enterprise.serialize_aws_json_1_0(
                value["resoldEnterprise"]
            )
        }
    elif "partnerLedSupport" in value:
        import capo_partnercentral_channel.types.partner_led_support

        return {
            "partnerLedSupport": capo_partnercentral_channel.types.partner_led_support.serialize_aws_json_1_0(
                value["partnerLedSupport"]
            )
        }
    elif "resoldUnifiedOperations" in value:
        import capo_partnercentral_channel.types.resold_unified_operations

        return {
            "resoldUnifiedOperations": capo_partnercentral_channel.types.resold_unified_operations.serialize_aws_json_1_0(
                value["resoldUnifiedOperations"]
            )
        }
    else:
        raise SerializationError("SupportPlan: no variant present")


def deserialize_aws_json_1_0(data: dict) -> SupportPlan:
    if data.get("resoldEnterprise") is not None:
        import capo_partnercentral_channel.types.resold_enterprise

        return {
            "resoldEnterprise": capo_partnercentral_channel.types.resold_enterprise.deserialize_aws_json_1_0(
                data["resoldEnterprise"]
            )
        }
    elif data.get("partnerLedSupport") is not None:
        import capo_partnercentral_channel.types.partner_led_support

        return {
            "partnerLedSupport": capo_partnercentral_channel.types.partner_led_support.deserialize_aws_json_1_0(
                data["partnerLedSupport"]
            )
        }
    elif data.get("resoldUnifiedOperations") is not None:
        import capo_partnercentral_channel.types.resold_unified_operations

        return {
            "resoldUnifiedOperations": capo_partnercentral_channel.types.resold_unified_operations.deserialize_aws_json_1_0(
                data["resoldUnifiedOperations"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("SupportPlan: no recognized variant key")
