"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FulfillmentDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_benefits.errors import DeserializationError, SerializationError
from capo_partnercentral_benefits.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.access_details
    import capo_partnercentral_benefits.types.consumable_details
    import capo_partnercentral_benefits.types.credit_details
    import capo_partnercentral_benefits.types.disbursement_details


class FulfillmentDetailsDisbursementDetailsMember(TypedDict, closed=True):
    DisbursementDetails: (
        "capo_partnercentral_benefits.types.disbursement_details.DisbursementDetails"
    )


class FulfillmentDetailsConsumableDetailsMember(TypedDict, closed=True):
    ConsumableDetails: (
        "capo_partnercentral_benefits.types.consumable_details.ConsumableDetails"
    )


class FulfillmentDetailsCreditDetailsMember(TypedDict, closed=True):
    CreditDetails: "capo_partnercentral_benefits.types.credit_details.CreditDetails"


class FulfillmentDetailsAccessDetailsMember(TypedDict, closed=True):
    AccessDetails: "capo_partnercentral_benefits.types.access_details.AccessDetails"


FulfillmentDetails: TypeAlias = (
    FulfillmentDetailsDisbursementDetailsMember
    | FulfillmentDetailsConsumableDetailsMember
    | FulfillmentDetailsCreditDetailsMember
    | FulfillmentDetailsAccessDetailsMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FulfillmentDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FulfillmentDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "DisbursementDetails" in value:
        import capo_partnercentral_benefits.types.disbursement_details

        return {
            "DisbursementDetails": capo_partnercentral_benefits.types.disbursement_details.serialize_aws_json_1_0(
                value["DisbursementDetails"]
            )
        }
    elif "ConsumableDetails" in value:
        import capo_partnercentral_benefits.types.consumable_details

        return {
            "ConsumableDetails": capo_partnercentral_benefits.types.consumable_details.serialize_aws_json_1_0(
                value["ConsumableDetails"]
            )
        }
    elif "CreditDetails" in value:
        import capo_partnercentral_benefits.types.credit_details

        return {
            "CreditDetails": capo_partnercentral_benefits.types.credit_details.serialize_aws_json_1_0(
                value["CreditDetails"]
            )
        }
    elif "AccessDetails" in value:
        import capo_partnercentral_benefits.types.access_details

        return {
            "AccessDetails": capo_partnercentral_benefits.types.access_details.serialize_aws_json_1_0(
                value["AccessDetails"]
            )
        }
    else:
        raise SerializationError("FulfillmentDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> FulfillmentDetails:
    if data.get("DisbursementDetails") is not None:
        import capo_partnercentral_benefits.types.disbursement_details

        return {
            "DisbursementDetails": capo_partnercentral_benefits.types.disbursement_details.deserialize_aws_json_1_0(
                data["DisbursementDetails"]
            )
        }
    elif data.get("ConsumableDetails") is not None:
        import capo_partnercentral_benefits.types.consumable_details

        return {
            "ConsumableDetails": capo_partnercentral_benefits.types.consumable_details.deserialize_aws_json_1_0(
                data["ConsumableDetails"]
            )
        }
    elif data.get("CreditDetails") is not None:
        import capo_partnercentral_benefits.types.credit_details

        return {
            "CreditDetails": capo_partnercentral_benefits.types.credit_details.deserialize_aws_json_1_0(
                data["CreditDetails"]
            )
        }
    elif data.get("AccessDetails") is not None:
        import capo_partnercentral_benefits.types.access_details

        return {
            "AccessDetails": capo_partnercentral_benefits.types.access_details.deserialize_aws_json_1_0(
                data["AccessDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FulfillmentDetails: no recognized variant key")
