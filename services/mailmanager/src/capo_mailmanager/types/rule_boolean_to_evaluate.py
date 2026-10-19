"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleBooleanToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.analysis
    import capo_mailmanager.types.rule_boolean_email_attribute
    import capo_mailmanager.types.rule_is_in_address_list


class _RuleBooleanToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: (
        "capo_mailmanager.types.rule_boolean_email_attribute.RuleBooleanEmailAttribute"
    )


class _RuleBooleanToEvaluate_Analysis(TypedDict, closed=True):
    Analysis: "capo_mailmanager.types.analysis.Analysis"


class _RuleBooleanToEvaluate_IsInAddressList(TypedDict, closed=True):
    IsInAddressList: (
        "capo_mailmanager.types.rule_is_in_address_list.RuleIsInAddressList"
    )


RuleBooleanToEvaluate: TypeAlias = (
    _RuleBooleanToEvaluate_Attribute
    | _RuleBooleanToEvaluate_Analysis
    | _RuleBooleanToEvaluate_IsInAddressList
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleBooleanToEvaluate) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RuleBooleanToEvaluate: cannot serialize unknown variant {value.name!r}"
        )
    elif "Attribute" in value:
        import capo_mailmanager.types.rule_boolean_email_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_boolean_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    elif "Analysis" in value:
        import capo_mailmanager.types.analysis

        return {
            "Analysis": capo_mailmanager.types.analysis.serialize_aws_json_1_0(
                value["Analysis"]
            )
        }
    elif "IsInAddressList" in value:
        import capo_mailmanager.types.rule_is_in_address_list

        return {
            "IsInAddressList": capo_mailmanager.types.rule_is_in_address_list.serialize_aws_json_1_0(
                value["IsInAddressList"]
            )
        }
    else:
        raise SerializationError("RuleBooleanToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleBooleanToEvaluate:
    if data.get("Attribute") is not None:
        import capo_mailmanager.types.rule_boolean_email_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_boolean_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    elif data.get("Analysis") is not None:
        import capo_mailmanager.types.analysis

        return {
            "Analysis": capo_mailmanager.types.analysis.deserialize_aws_json_1_0(
                data["Analysis"]
            )
        }
    elif data.get("IsInAddressList") is not None:
        import capo_mailmanager.types.rule_is_in_address_list

        return {
            "IsInAddressList": capo_mailmanager.types.rule_is_in_address_list.deserialize_aws_json_1_0(
                data["IsInAddressList"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("RuleBooleanToEvaluate: no recognized variant key")
