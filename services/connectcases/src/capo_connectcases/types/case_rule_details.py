"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.field_options_case_rule
    import capo_connectcases.types.hidden_case_rule
    import capo_connectcases.types.required_case_rule


class CaseRuleDetailsRequiredMember(TypedDict, closed=True):
    required: "capo_connectcases.types.required_case_rule.RequiredCaseRule"


class CaseRuleDetailsFieldOptionsMember(TypedDict, closed=True):
    fieldOptions: "capo_connectcases.types.field_options_case_rule.FieldOptionsCaseRule"


class CaseRuleDetailsHiddenMember(TypedDict, closed=True):
    hidden: "capo_connectcases.types.hidden_case_rule.HiddenCaseRule"


CaseRuleDetails: TypeAlias = (
    CaseRuleDetailsRequiredMember
    | CaseRuleDetailsFieldOptionsMember
    | CaseRuleDetailsHiddenMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CaseRuleDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "required" in value:
        import capo_connectcases.types.required_case_rule

        return {
            "required": capo_connectcases.types.required_case_rule.serialize_json(
                value["required"]
            )
        }
    elif "fieldOptions" in value:
        import capo_connectcases.types.field_options_case_rule

        return {
            "fieldOptions": capo_connectcases.types.field_options_case_rule.serialize_json(
                value["fieldOptions"]
            )
        }
    elif "hidden" in value:
        import capo_connectcases.types.hidden_case_rule

        return {
            "hidden": capo_connectcases.types.hidden_case_rule.serialize_json(
                value["hidden"]
            )
        }
    else:
        raise SerializationError("CaseRuleDetails: no variant present")


def deserialize_json(data: dict) -> CaseRuleDetails:
    if data.get("required") is not None:
        import capo_connectcases.types.required_case_rule

        return {
            "required": capo_connectcases.types.required_case_rule.deserialize_json(
                data["required"]
            )
        }
    elif data.get("fieldOptions") is not None:
        import capo_connectcases.types.field_options_case_rule

        return {
            "fieldOptions": capo_connectcases.types.field_options_case_rule.deserialize_json(
                data["fieldOptions"]
            )
        }
    elif data.get("hidden") is not None:
        import capo_connectcases.types.hidden_case_rule

        return {
            "hidden": capo_connectcases.types.hidden_case_rule.deserialize_json(
                data["hidden"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CaseRuleDetails: no recognized variant key")
