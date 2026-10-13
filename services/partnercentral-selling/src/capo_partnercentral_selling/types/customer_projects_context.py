"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CustomerProjectsContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_customer
    import capo_partnercentral_selling.types.engagement_customer_project_details


class CustomerProjectsContext(TypedDict, closed=True):
    customer: NotRequired[
        "capo_partnercentral_selling.types.engagement_customer.EngagementCustomer"
    ]
    project: NotRequired[
        "capo_partnercentral_selling.types.engagement_customer_project_details.EngagementCustomerProjectDetails"
    ]
    """<p>Information about the customer project associated with the Engagement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomerProjectsContext) -> dict:
    out: dict = {}
    if "customer" in value:
        import capo_partnercentral_selling.types.engagement_customer

        out["Customer"] = (
            capo_partnercentral_selling.types.engagement_customer.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "project" in value:
        import capo_partnercentral_selling.types.engagement_customer_project_details

        out["Project"] = (
            capo_partnercentral_selling.types.engagement_customer_project_details.serialize_aws_json_1_0(
                value["project"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomerProjectsContext:
    out: CustomerProjectsContext = {}  # type: ignore[typeddict-item]
    if data.get("Customer") is not None:
        import capo_partnercentral_selling.types.engagement_customer

        out["customer"] = (
            capo_partnercentral_selling.types.engagement_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if data.get("Project") is not None:
        import capo_partnercentral_selling.types.engagement_customer_project_details

        out["project"] = (
            capo_partnercentral_selling.types.engagement_customer_project_details.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    return out


def redact_sensitive(value: CustomerProjectsContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer" in value:
        import capo_partnercentral_selling.types.engagement_customer

        out["customer"] = (
            capo_partnercentral_selling.types.engagement_customer.redact_sensitive(
                value["customer"]
            )
        )
    if "project" in value:
        import capo_partnercentral_selling.types.engagement_customer_project_details

        out["project"] = (
            capo_partnercentral_selling.types.engagement_customer_project_details.redact_sensitive(
                value["project"]
            )
        )
    return out
