"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityCustomer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.customer_contacts_list


class AwsOpportunityCustomer(TypedDict, closed=True):
    contacts: NotRequired[
        "capo_partnercentral_selling.types.customer_contacts_list.CustomerContactsList"
    ]
    """<p>Provides a list of customer contacts involved in the opportunity. These contacts may include decision makers, influencers, and other stakeholders within the customer's organization.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunityCustomer) -> dict:
    out: dict = {}
    if "contacts" in value:
        import capo_partnercentral_selling.types.customer_contacts_list

        out["Contacts"] = (
            capo_partnercentral_selling.types.customer_contacts_list.serialize_aws_json_1_0(
                value["contacts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOpportunityCustomer:
    out: AwsOpportunityCustomer = {}  # type: ignore[typeddict-item]
    if data.get("Contacts") is not None:
        import capo_partnercentral_selling.types.customer_contacts_list

        out["contacts"] = (
            capo_partnercentral_selling.types.customer_contacts_list.deserialize_aws_json_1_0(
                data["Contacts"]
            )
        )
    return out


def redact_sensitive(value: AwsOpportunityCustomer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contacts" in value:
        import capo_partnercentral_selling.types.customer_contacts_list

        out["contacts"] = (
            capo_partnercentral_selling.types.customer_contacts_list.redact_sensitive(
                value["contacts"]
            )
        )
    return out
