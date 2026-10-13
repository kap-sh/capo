"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Customer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.account
    import capo_partnercentral_selling.types.customer_contacts_list


class Customer(TypedDict, closed=True):
    account: NotRequired["capo_partnercentral_selling.types.account.Account"]
    """<p>An object that contains the customer's account details.</p>"""
    contacts: NotRequired[
        "capo_partnercentral_selling.types.customer_contacts_list.CustomerContactsList"
    ]
    """<p>Represents the contact details for individuals associated with the customer of the <code>Opportunity</code>. This field captures relevant contacts, including decision-makers, influencers, and technical stakeholders within the customer organization. These contacts are key to progressing the opportunity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Customer) -> dict:
    out: dict = {}
    if "account" in value:
        import capo_partnercentral_selling.types.account

        out["Account"] = (
            capo_partnercentral_selling.types.account.serialize_aws_json_1_0(
                value["account"]
            )
        )
    if "contacts" in value:
        import capo_partnercentral_selling.types.customer_contacts_list

        out["Contacts"] = (
            capo_partnercentral_selling.types.customer_contacts_list.serialize_aws_json_1_0(
                value["contacts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Customer:
    out: Customer = {}  # type: ignore[typeddict-item]
    if data.get("Account") is not None:
        import capo_partnercentral_selling.types.account

        out["account"] = (
            capo_partnercentral_selling.types.account.deserialize_aws_json_1_0(
                data["Account"]
            )
        )
    if data.get("Contacts") is not None:
        import capo_partnercentral_selling.types.customer_contacts_list

        out["contacts"] = (
            capo_partnercentral_selling.types.customer_contacts_list.deserialize_aws_json_1_0(
                data["Contacts"]
            )
        )
    return out


def redact_sensitive(value: Customer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "account" in value:
        import capo_partnercentral_selling.types.account

        out["account"] = capo_partnercentral_selling.types.account.redact_sensitive(
            value["account"]
        )
    if "contacts" in value:
        import capo_partnercentral_selling.types.customer_contacts_list

        out["contacts"] = (
            capo_partnercentral_selling.types.customer_contacts_list.redact_sensitive(
                value["contacts"]
            )
        )
    return out
