"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProjectSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.delivery_models
    import capo_partnercentral_selling.types.expected_contract_duration
    import capo_partnercentral_selling.types.expected_customer_spend_list


class ProjectSummary(TypedDict, closed=True):
    delivery_models: NotRequired[
        "capo_partnercentral_selling.types.delivery_models.DeliveryModels"
    ]
    """<p>Specifies your solution or service's deployment or consumption model in the <code>Opportunity</code>'s context. You can select multiple options.</p> <p>Options' descriptions from the <code>Delivery Model</code> field are:</p> <ul> <li> <p>SaaS or PaaS: Your Amazon Web Services based solution deployed as SaaS or PaaS in your Amazon Web Services environment.</p> </li> <li> <p>BYOL or AMI: Your Amazon Web Services based solution deployed as BYOL or AMI in the end customer's Amazon Web Services environment.</p> </li> <li> <p>Managed Services: The end customer's Amazon Web Services business management (For example: Consulting, design, implementation, billing support, cost optimization, technical support).</p> </li> <li> <p>Professional Services: Offerings to help enterprise end customers achieve specific business outcomes for enterprise cloud adoption (For example: Advisory or transformation planning).</p> </li> <li> <p>Resell: Amazon Web Services accounts and billing management for your customers.</p> </li> <li> <p>Other: Delivery model not described above.</p> </li> </ul>"""
    expected_customer_spend: NotRequired[
        "capo_partnercentral_selling.types.expected_customer_spend_list.ExpectedCustomerSpendList"
    ]
    """<p>Provides a summary of the expected customer spend for the project, offering a high-level view of the potential financial impact.</p>"""
    expected_contract_duration: NotRequired[
        "capo_partnercentral_selling.types.expected_contract_duration.ExpectedContractDuration"
    ]
    """<p>Optional. The expected contract duration for this opportunity, representing the anticipated length of the contract in the unit specified by <code>Term</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProjectSummary) -> dict:
    out: dict = {}
    if "delivery_models" in value:
        import capo_partnercentral_selling.types.delivery_models

        out["DeliveryModels"] = (
            capo_partnercentral_selling.types.delivery_models.serialize_aws_json_1_0(
                value["delivery_models"]
            )
        )
    if "expected_customer_spend" in value:
        import capo_partnercentral_selling.types.expected_customer_spend_list

        out["ExpectedCustomerSpend"] = (
            capo_partnercentral_selling.types.expected_customer_spend_list.serialize_aws_json_1_0(
                value["expected_customer_spend"]
            )
        )
    if "expected_contract_duration" in value:
        import capo_partnercentral_selling.types.expected_contract_duration

        out["ExpectedContractDuration"] = (
            capo_partnercentral_selling.types.expected_contract_duration.serialize_aws_json_1_0(
                value["expected_contract_duration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProjectSummary:
    out: ProjectSummary = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryModels") is not None:
        import capo_partnercentral_selling.types.delivery_models

        out["delivery_models"] = (
            capo_partnercentral_selling.types.delivery_models.deserialize_aws_json_1_0(
                data["DeliveryModels"]
            )
        )
    if data.get("ExpectedCustomerSpend") is not None:
        import capo_partnercentral_selling.types.expected_customer_spend_list

        out["expected_customer_spend"] = (
            capo_partnercentral_selling.types.expected_customer_spend_list.deserialize_aws_json_1_0(
                data["ExpectedCustomerSpend"]
            )
        )
    if data.get("ExpectedContractDuration") is not None:
        import capo_partnercentral_selling.types.expected_contract_duration

        out["expected_contract_duration"] = (
            capo_partnercentral_selling.types.expected_contract_duration.deserialize_aws_json_1_0(
                data["ExpectedContractDuration"]
            )
        )
    return out


def redact_sensitive(value: ProjectSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expected_customer_spend" in value:
        import capo_partnercentral_selling.types.expected_customer_spend_list

        out["expected_customer_spend"] = (
            capo_partnercentral_selling.types.expected_customer_spend_list.redact_sensitive(
                value["expected_customer_spend"]
            )
        )
    return out
