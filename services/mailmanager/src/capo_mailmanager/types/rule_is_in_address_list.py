"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleIsInAddressList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_address_list_arn_list
    import capo_mailmanager.types.rule_address_list_email_attribute


class RuleIsInAddressList(TypedDict, closed=True):
    attribute: "capo_mailmanager.types.rule_address_list_email_attribute.RuleAddressListEmailAttribute"
    """<p>The email attribute that needs to be evaluated against the address list.</p>"""
    address_lists: (
        "capo_mailmanager.types.rule_address_list_arn_list.RuleAddressListArnList"
    )
    """<p>The address lists that will be used for evaluation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleIsInAddressList) -> dict:
    out: dict = {}
    import capo_mailmanager.types.rule_address_list_email_attribute

    out["Attribute"] = (
        capo_mailmanager.types.rule_address_list_email_attribute.serialize_aws_json_1_0(
            value["attribute"]
        )
    )
    import capo_mailmanager.types.rule_address_list_arn_list

    out["AddressLists"] = (
        capo_mailmanager.types.rule_address_list_arn_list.serialize_aws_json_1_0(
            value["address_lists"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleIsInAddressList:
    out: RuleIsInAddressList = {}  # type: ignore[typeddict-item]
    if data.get("Attribute") is not None:
        import capo_mailmanager.types.rule_address_list_email_attribute

        out["attribute"] = (
            capo_mailmanager.types.rule_address_list_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        )
    else:
        import typing

        out["attribute"] = typing.cast(
            "capo_mailmanager.types.rule_address_list_email_attribute.RuleAddressListEmailAttribute",
            "",
        )
    if data.get("AddressLists") is not None:
        import capo_mailmanager.types.rule_address_list_arn_list

        out["address_lists"] = (
            capo_mailmanager.types.rule_address_list_arn_list.deserialize_aws_json_1_0(
                data["AddressLists"]
            )
        )
    else:
        out["address_lists"] = []
    return out
