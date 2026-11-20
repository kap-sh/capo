"""Generated from Smithy shape ``aws.iam#AppliesWhen``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_marketing.errors import (
    DeserializationError,
    SerializationError,
)
from capo_partnercentral_marketing.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.input_list_member_value
    import capo_partnercentral_marketing.types.input_member_reference
    import capo_partnercentral_marketing.types.input_member_value
    import capo_partnercentral_marketing.types.resolved_by_service


class AppliesWhenIsPresentMember(TypedDict, closed=True):
    isPresent: "capo_partnercentral_marketing.types.input_member_reference.InputMemberReference"


class AppliesWhenIsNotPresentMember(TypedDict, closed=True):
    isNotPresent: "capo_partnercentral_marketing.types.input_member_reference.InputMemberReference"


class AppliesWhenIsEqualToMember(TypedDict, closed=True):
    isEqualTo: "capo_partnercentral_marketing.types.input_member_value.InputMemberValue"


class AppliesWhenIsNotEqualToMember(TypedDict, closed=True):
    isNotEqualTo: (
        "capo_partnercentral_marketing.types.input_member_value.InputMemberValue"
    )


class AppliesWhenContainsValueMember(TypedDict, closed=True):
    containsValue: "capo_partnercentral_marketing.types.input_list_member_value.InputListMemberValue"


class AppliesWhenDoesNotContainValueMember(TypedDict, closed=True):
    doesNotContainValue: "capo_partnercentral_marketing.types.input_list_member_value.InputListMemberValue"


class AppliesWhenResolvedByServiceMember(TypedDict, closed=True):
    resolvedByService: (
        "capo_partnercentral_marketing.types.resolved_by_service.ResolvedByService"
    )


AppliesWhen: TypeAlias = (
    AppliesWhenIsPresentMember
    | AppliesWhenIsNotPresentMember
    | AppliesWhenIsEqualToMember
    | AppliesWhenIsNotEqualToMember
    | AppliesWhenContainsValueMember
    | AppliesWhenDoesNotContainValueMember
    | AppliesWhenResolvedByServiceMember
    | UnknownUnionMember
)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppliesWhen) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AppliesWhen: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "isPresent" in value:
        return {"isPresent": value["isPresent"]}
    elif "isNotPresent" in value:
        return {"isNotPresent": value["isNotPresent"]}
    elif "isEqualTo" in value:
        import capo_partnercentral_marketing.types.input_member_value

        return {
            "isEqualTo": capo_partnercentral_marketing.types.input_member_value.serialize_cbor(
                value["isEqualTo"]
            )
        }
    elif "isNotEqualTo" in value:
        import capo_partnercentral_marketing.types.input_member_value

        return {
            "isNotEqualTo": capo_partnercentral_marketing.types.input_member_value.serialize_cbor(
                value["isNotEqualTo"]
            )
        }
    elif "containsValue" in value:
        import capo_partnercentral_marketing.types.input_list_member_value

        return {
            "containsValue": capo_partnercentral_marketing.types.input_list_member_value.serialize_cbor(
                value["containsValue"]
            )
        }
    elif "doesNotContainValue" in value:
        import capo_partnercentral_marketing.types.input_list_member_value

        return {
            "doesNotContainValue": capo_partnercentral_marketing.types.input_list_member_value.serialize_cbor(
                value["doesNotContainValue"]
            )
        }
    elif "resolvedByService" in value:
        import capo_partnercentral_marketing.types.resolved_by_service

        return {
            "resolvedByService": capo_partnercentral_marketing.types.resolved_by_service.serialize_cbor(
                value["resolvedByService"]
            )
        }
    else:
        raise SerializationError("AppliesWhen: no variant present")


def deserialize_cbor(data: dict) -> AppliesWhen:
    if data.get("isPresent") is not None:
        return {"isPresent": data["isPresent"]}
    elif data.get("isNotPresent") is not None:
        return {"isNotPresent": data["isNotPresent"]}
    elif data.get("isEqualTo") is not None:
        import capo_partnercentral_marketing.types.input_member_value

        return {
            "isEqualTo": capo_partnercentral_marketing.types.input_member_value.deserialize_cbor(
                data["isEqualTo"]
            )
        }
    elif data.get("isNotEqualTo") is not None:
        import capo_partnercentral_marketing.types.input_member_value

        return {
            "isNotEqualTo": capo_partnercentral_marketing.types.input_member_value.deserialize_cbor(
                data["isNotEqualTo"]
            )
        }
    elif data.get("containsValue") is not None:
        import capo_partnercentral_marketing.types.input_list_member_value

        return {
            "containsValue": capo_partnercentral_marketing.types.input_list_member_value.deserialize_cbor(
                data["containsValue"]
            )
        }
    elif data.get("doesNotContainValue") is not None:
        import capo_partnercentral_marketing.types.input_list_member_value

        return {
            "doesNotContainValue": capo_partnercentral_marketing.types.input_list_member_value.deserialize_cbor(
                data["doesNotContainValue"]
            )
        }
    elif data.get("resolvedByService") is not None:
        import capo_partnercentral_marketing.types.resolved_by_service

        return {
            "resolvedByService": capo_partnercentral_marketing.types.resolved_by_service.deserialize_cbor(
                data["resolvedByService"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AppliesWhen: no recognized variant key")
