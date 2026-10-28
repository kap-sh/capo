"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressBooleanToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_analysis
    import capo_mailmanager.types.ingress_is_in_address_list


class IngressBooleanToEvaluateAnalysisMember(TypedDict, closed=True):
    Analysis: "capo_mailmanager.types.ingress_analysis.IngressAnalysis"


class IngressBooleanToEvaluateIsInAddressListMember(TypedDict, closed=True):
    IsInAddressList: (
        "capo_mailmanager.types.ingress_is_in_address_list.IngressIsInAddressList"
    )


IngressBooleanToEvaluate: TypeAlias = (
    IngressBooleanToEvaluateAnalysisMember
    | IngressBooleanToEvaluateIsInAddressListMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressBooleanToEvaluate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IngressBooleanToEvaluate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Analysis" in value:
        import capo_mailmanager.types.ingress_analysis

        return {
            "Analysis": capo_mailmanager.types.ingress_analysis.serialize_aws_json_1_0(
                value["Analysis"]
            )
        }
    elif "IsInAddressList" in value:
        import capo_mailmanager.types.ingress_is_in_address_list

        return {
            "IsInAddressList": capo_mailmanager.types.ingress_is_in_address_list.serialize_aws_json_1_0(
                value["IsInAddressList"]
            )
        }
    else:
        raise SerializationError("IngressBooleanToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressBooleanToEvaluate:
    if data.get("Analysis") is not None:
        import capo_mailmanager.types.ingress_analysis

        return {
            "Analysis": capo_mailmanager.types.ingress_analysis.deserialize_aws_json_1_0(
                data["Analysis"]
            )
        }
    elif data.get("IsInAddressList") is not None:
        import capo_mailmanager.types.ingress_is_in_address_list

        return {
            "IsInAddressList": capo_mailmanager.types.ingress_is_in_address_list.deserialize_aws_json_1_0(
                data["IsInAddressList"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "IngressBooleanToEvaluate: no recognized variant key"
        )
