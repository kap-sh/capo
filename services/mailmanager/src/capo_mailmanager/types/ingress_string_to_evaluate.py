"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressStringToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_analysis
    import capo_mailmanager.types.ingress_string_email_attribute


class IngressStringToEvaluateAttributeMember(TypedDict, closed=True):
    Attribute: "capo_mailmanager.types.ingress_string_email_attribute.IngressStringEmailAttribute"


class IngressStringToEvaluateAnalysisMember(TypedDict, closed=True):
    Analysis: "capo_mailmanager.types.ingress_analysis.IngressAnalysis"


IngressStringToEvaluate: TypeAlias = (
    IngressStringToEvaluateAttributeMember
    | IngressStringToEvaluateAnalysisMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressStringToEvaluate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IngressStringToEvaluate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Attribute" in value:
        import capo_mailmanager.types.ingress_string_email_attribute

        return {
            "Attribute": capo_mailmanager.types.ingress_string_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    elif "Analysis" in value:
        import capo_mailmanager.types.ingress_analysis

        return {
            "Analysis": capo_mailmanager.types.ingress_analysis.serialize_aws_json_1_0(
                value["Analysis"]
            )
        }
    else:
        raise SerializationError("IngressStringToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressStringToEvaluate:
    if data.get("Attribute") is not None:
        import capo_mailmanager.types.ingress_string_email_attribute

        return {
            "Attribute": capo_mailmanager.types.ingress_string_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    elif data.get("Analysis") is not None:
        import capo_mailmanager.types.ingress_analysis

        return {
            "Analysis": capo_mailmanager.types.ingress_analysis.deserialize_aws_json_1_0(
                data["Analysis"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IngressStringToEvaluate: no recognized variant key")
