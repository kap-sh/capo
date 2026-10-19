"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleStringToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.analysis
    import capo_mailmanager.types.mime_header_attribute
    import capo_mailmanager.types.rule_client_certificate_attribute
    import capo_mailmanager.types.rule_string_email_attribute


class _RuleStringToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: (
        "capo_mailmanager.types.rule_string_email_attribute.RuleStringEmailAttribute"
    )


class _RuleStringToEvaluate_MimeHeaderAttribute(TypedDict, closed=True):
    MimeHeaderAttribute: (
        "capo_mailmanager.types.mime_header_attribute.MimeHeaderAttribute"
    )


class _RuleStringToEvaluate_Analysis(TypedDict, closed=True):
    Analysis: "capo_mailmanager.types.analysis.Analysis"


class _RuleStringToEvaluate_ClientCertificateAttribute(TypedDict, closed=True):
    ClientCertificateAttribute: "capo_mailmanager.types.rule_client_certificate_attribute.RuleClientCertificateAttribute"


RuleStringToEvaluate: TypeAlias = (
    _RuleStringToEvaluate_Attribute
    | _RuleStringToEvaluate_MimeHeaderAttribute
    | _RuleStringToEvaluate_Analysis
    | _RuleStringToEvaluate_ClientCertificateAttribute
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleStringToEvaluate) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RuleStringToEvaluate: cannot serialize unknown variant {value.name!r}"
        )
    elif "Attribute" in value:
        import capo_mailmanager.types.rule_string_email_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_string_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    elif "MimeHeaderAttribute" in value:
        return {"MimeHeaderAttribute": value["MimeHeaderAttribute"]}
    elif "Analysis" in value:
        import capo_mailmanager.types.analysis

        return {
            "Analysis": capo_mailmanager.types.analysis.serialize_aws_json_1_0(
                value["Analysis"]
            )
        }
    elif "ClientCertificateAttribute" in value:
        import capo_mailmanager.types.rule_client_certificate_attribute

        return {
            "ClientCertificateAttribute": capo_mailmanager.types.rule_client_certificate_attribute.serialize_aws_json_1_0(
                value["ClientCertificateAttribute"]
            )
        }
    else:
        raise SerializationError("RuleStringToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleStringToEvaluate:
    if data.get("Attribute") is not None:
        import capo_mailmanager.types.rule_string_email_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_string_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    elif data.get("MimeHeaderAttribute") is not None:
        return {"MimeHeaderAttribute": data["MimeHeaderAttribute"]}
    elif data.get("Analysis") is not None:
        import capo_mailmanager.types.analysis

        return {
            "Analysis": capo_mailmanager.types.analysis.deserialize_aws_json_1_0(
                data["Analysis"]
            )
        }
    elif data.get("ClientCertificateAttribute") is not None:
        import capo_mailmanager.types.rule_client_certificate_attribute

        return {
            "ClientCertificateAttribute": capo_mailmanager.types.rule_client_certificate_attribute.deserialize_aws_json_1_0(
                data["ClientCertificateAttribute"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("RuleStringToEvaluate: no recognized variant key")
