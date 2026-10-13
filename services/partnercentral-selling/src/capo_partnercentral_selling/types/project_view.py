"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProjectView``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.delivery_models
    import capo_partnercentral_selling.types.expected_contract_duration
    import capo_partnercentral_selling.types.expected_customer_spend_list
    import capo_partnercentral_selling.types.pii_string
    import capo_partnercentral_selling.types.sales_activities


class ProjectView(TypedDict, closed=True):
    delivery_models: NotRequired[
        "capo_partnercentral_selling.types.delivery_models.DeliveryModels"
    ]
    """<p> Describes the deployment or consumption model for the partner solution or offering. This field indicates how the project's solution will be delivered or implemented for the customer. </p>"""
    expected_customer_spend: NotRequired[
        "capo_partnercentral_selling.types.expected_customer_spend_list.ExpectedCustomerSpendList"
    ]
    """<p> Provides information about the anticipated customer spend related to this project. This may include details such as amount, frequency, and currency of expected expenditure. </p>"""
    expected_contract_duration: NotRequired[
        "capo_partnercentral_selling.types.expected_contract_duration.ExpectedContractDuration"
    ]
    """<p>Optional. The expected contract duration for this opportunity, representing the anticipated length of the contract in the unit specified by <code>Term</code>.</p>"""
    customer_use_case: NotRequired["str"]
    """<p> Specifies the proposed solution focus or type of workload for the project. </p>"""
    sales_activities: NotRequired[
        "capo_partnercentral_selling.types.sales_activities.SalesActivities"
    ]
    """<p> Lists the pre-sales activities that have occurred with the end-customer related to the opportunity. This field is conditionally mandatory when the project is qualified for Co-Sell and helps drive assignment priority on the AWS side. It provides insight into the engagement level with the customer. </p>"""
    other_solution_description: NotRequired[
        "capo_partnercentral_selling.types.pii_string.PiiString"
    ]
    """<p> Offers a description of other solutions if the standard solutions do not adequately cover the project's scope. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProjectView) -> dict:
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
    if "customer_use_case" in value:
        out["CustomerUseCase"] = value["customer_use_case"]
    if "sales_activities" in value:
        import capo_partnercentral_selling.types.sales_activities

        out["SalesActivities"] = (
            capo_partnercentral_selling.types.sales_activities.serialize_aws_json_1_0(
                value["sales_activities"]
            )
        )
    if "other_solution_description" in value:
        out["OtherSolutionDescription"] = value["other_solution_description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProjectView:
    out: ProjectView = {}  # type: ignore[typeddict-item]
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
    if data.get("CustomerUseCase") is not None:
        out["customer_use_case"] = data["CustomerUseCase"]
    if data.get("SalesActivities") is not None:
        import capo_partnercentral_selling.types.sales_activities

        out["sales_activities"] = (
            capo_partnercentral_selling.types.sales_activities.deserialize_aws_json_1_0(
                data["SalesActivities"]
            )
        )
    if data.get("OtherSolutionDescription") is not None:
        out["other_solution_description"] = data["OtherSolutionDescription"]
    return out


def redact_sensitive(value: ProjectView) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expected_customer_spend" in value:
        import capo_partnercentral_selling.types.expected_customer_spend_list

        out["expected_customer_spend"] = (
            capo_partnercentral_selling.types.expected_customer_spend_list.redact_sensitive(
                value["expected_customer_spend"]
            )
        )
    if "other_solution_description" in value:
        out["other_solution_description"] = "*** Sensitive Data Redacted ***"
    return out
