"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Project``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.apn_programs
    import capo_partnercentral_selling.types.aws_partition
    import capo_partnercentral_selling.types.competitor_name
    import capo_partnercentral_selling.types.delivery_models
    import capo_partnercentral_selling.types.expected_contract_duration
    import capo_partnercentral_selling.types.expected_customer_spend_list
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.pii_string
    import capo_partnercentral_selling.types.sales_activities


class Project(TypedDict, closed=True):
    delivery_models: NotRequired[
        "capo_partnercentral_selling.types.delivery_models.DeliveryModels"
    ]
    """<p>Specifies the deployment or consumption model for your solution or service in the <code>Opportunity</code>'s context. You can select multiple options.</p> <p>Options' descriptions from the <code>Delivery Model</code> field are:</p> <ul> <li> <p>SaaS or PaaS: Your Amazon Web Services based solution deployed as SaaS or PaaS in your Amazon Web Services environment.</p> </li> <li> <p>BYOL or AMI: Your Amazon Web Services based solution deployed as BYOL or AMI in the end customer's Amazon Web Services environment.</p> </li> <li> <p>Managed Services: The end customer's Amazon Web Services business management (For example: Consulting, design, implementation, billing support, cost optimization, technical support).</p> </li> <li> <p>Professional Services: Offerings to help enterprise end customers achieve specific business outcomes for enterprise cloud adoption (For example: Advisory or transformation planning).</p> </li> <li> <p>Resell: Amazon Web Services accounts and billing management for your customers.</p> </li> <li> <p>Other: Delivery model not described above.</p> </li> </ul>"""
    expected_customer_spend: NotRequired[
        "capo_partnercentral_selling.types.expected_customer_spend_list.ExpectedCustomerSpendList"
    ]
    """<p>Represents the estimated amount that the customer is expected to spend on AWS services related to the opportunity. This helps in evaluating the potential financial value of the opportunity for AWS.</p>"""
    expected_contract_duration: NotRequired[
        "capo_partnercentral_selling.types.expected_contract_duration.ExpectedContractDuration"
    ]
    """<p>Optional. The expected duration of the contract associated with this opportunity. Partners use this value alongside expected customer spend to convert Total Contract Value (TCV) into Monthly Recurring Revenue (MRR).</p>"""
    title: NotRequired["capo_partnercentral_selling.types.pii_string.PiiString"]
    """<p>Specifies the <code>Opportunity</code>'s title or name.</p>"""
    apn_programs: NotRequired[
        "capo_partnercentral_selling.types.apn_programs.ApnPrograms"
    ]
    """<p>Specifies the Amazon Partner Network (APN) program that influenced the <code>Opportunity</code>. APN programs refer to specific partner programs or initiatives that can impact the <code>Opportunity</code>.</p> <p>Valid values: <code>APN Immersion Days | APN Solution Space | ATO (Authority to Operate) | AWS Marketplace Campaign | IS Immersion Day SFID Program | ISV Workload Migration | Migration Acceleration Program | P3 | Partner Launch Initiative | Partner Opportunity Acceleration Funded | The Next Smart | VMware Cloud on AWS | Well-Architected | Windows | Workspaces/AppStream Accelerator Program | WWPS NDPP</code> </p>"""
    customer_business_problem: NotRequired[
        "capo_partnercentral_selling.types.pii_string.PiiString"
    ]
    """<p>Describes the problem the end customer has, and how the partner is helping. Utilize this field to provide a concise narrative that outlines the customer's business challenge or issue. Elaborate on how the partner's solution or offerings align to resolve the customer's business problem. Include relevant information about the partner's value proposition, unique selling points, and expertise to tackle the issue. Offer insights on how the proposed solution meets the customer's needs and provides value. Use concise language and precise descriptions to convey the context and significance of the <code>Opportunity</code>. The content in this field helps Amazon Web Services understand the nature of the <code>Opportunity</code> and the strategic fit of the partner's solution.</p>"""
    customer_use_case: NotRequired["str"]
    """<p>Specifies the proposed solution focus or type of workload for the Opportunity. This field captures the primary use case or objective of the proposed solution, and provides context and clarity to the addressed workload.</p> <p>Valid values: <code>AI Machine Learning and Analytics | Archiving | Big Data: Data Warehouse/Data Integration/ETL/Data Lake/BI | Blockchain | Business Applications: Mainframe Modernization | Business Applications &amp; Contact Center | Business Applications &amp; SAP Production | Centralized Operations Management | Cloud Management Tools | Cloud Management Tools &amp; DevOps with Continuous Integration &amp; Continuous Delivery (CICD) | Configuration, Compliance &amp; Auditing | Connected Services | Containers &amp; Serverless | Content Delivery &amp; Edge Services | Database | Edge Computing/End User Computing | Energy | Enterprise Governance &amp; Controls | Enterprise Resource Planning | Financial Services | Healthcare and Life Sciences | High Performance Computing | Hybrid Application Platform | Industrial Software | IOT | Manufacturing, Supply Chain and Operations | Media &amp; High performance computing (HPC) | Migration/Database Migration | Monitoring, logging and performance | Monitoring &amp; Observability | Networking | Outpost | SAP | Security &amp; Compliance | Storage &amp; Backup | Training | VMC | VMWare | Web development &amp; DevOps</code> </p>"""
    related_opportunity_identifier: NotRequired[
        "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    ]
    """<p>Specifies the current opportunity's parent opportunity identifier.</p>"""
    sales_activities: NotRequired[
        "capo_partnercentral_selling.types.sales_activities.SalesActivities"
    ]
    """<p>Specifies the <code>Opportunity</code>'s sales activities conducted with the end customer. These activities help drive Amazon Web Services assignment priority.</p> <p>Valid values:</p> <ul> <li> <p>Initialized discussions with customer: Initial conversations with the customer to understand their needs and introduce your solution.</p> </li> <li> <p>Customer has shown interest in solution: After initial discussions, the customer is interested in your solution.</p> </li> <li> <p>Conducted POC/demo: You conducted a proof of concept (POC) or demonstration of the solution for the customer.</p> </li> <li> <p>In evaluation/planning stage: The customer is evaluating the solution and planning potential implementation.</p> </li> <li> <p>Agreed on solution to Business Problem: Both parties agree on how the solution addresses the customer's business problem.</p> </li> <li> <p>Completed Action Plan: A detailed action plan is complete and outlines the steps for implementation.</p> </li> <li> <p>Finalized Deployment Need: Both parties agree with and finalized the deployment needs.</p> </li> <li> <p>SOW Signed: Both parties signed a statement of work (SOW), and formalize the agreement and detail the project scope and deliverables.</p> </li> </ul>"""
    competitor_name: NotRequired[
        "capo_partnercentral_selling.types.competitor_name.CompetitorName"
    ]
    """<p>Name of the <code>Opportunity</code>'s competitor (if any). Use <code>Other</code> to submit a value not in the picklist.</p>"""
    other_competitor_names: NotRequired["str"]
    """<p>Only allowed when <code>CompetitorNames</code> has <code>Other</code> selected.</p>"""
    other_solution_description: NotRequired[
        "capo_partnercentral_selling.types.pii_string.PiiString"
    ]
    """<p>Specifies the offered solution for the customer's business problem when the <code> RelatedEntityIdentifiers.Solutions</code> field value is <code>Other</code>.</p>"""
    additional_comments: NotRequired["str"]
    """<p>Captures additional comments or information for the <code>Opportunity</code> that weren't captured in other fields.</p>"""
    aws_partition: NotRequired[
        "capo_partnercentral_selling.types.aws_partition.AwsPartition"
    ]
    """<p>AWS partition where the opportunity will be deployed. Possible values: <code>aws-eusc</code> for AWS European Sovereign Cloud, <code>null</code> for all other partitions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Project) -> dict:
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
    if "title" in value:
        out["Title"] = value["title"]
    if "apn_programs" in value:
        import capo_partnercentral_selling.types.apn_programs

        out["ApnPrograms"] = (
            capo_partnercentral_selling.types.apn_programs.serialize_aws_json_1_0(
                value["apn_programs"]
            )
        )
    if "customer_business_problem" in value:
        out["CustomerBusinessProblem"] = value["customer_business_problem"]
    if "customer_use_case" in value:
        out["CustomerUseCase"] = value["customer_use_case"]
    if "related_opportunity_identifier" in value:
        out["RelatedOpportunityIdentifier"] = value["related_opportunity_identifier"]
    if "sales_activities" in value:
        import capo_partnercentral_selling.types.sales_activities

        out["SalesActivities"] = (
            capo_partnercentral_selling.types.sales_activities.serialize_aws_json_1_0(
                value["sales_activities"]
            )
        )
    if "competitor_name" in value:
        import capo_partnercentral_selling.types.competitor_name

        out["CompetitorName"] = (
            capo_partnercentral_selling.types.competitor_name.serialize_aws_json_1_0(
                value["competitor_name"]
            )
        )
    if "other_competitor_names" in value:
        out["OtherCompetitorNames"] = value["other_competitor_names"]
    if "other_solution_description" in value:
        out["OtherSolutionDescription"] = value["other_solution_description"]
    if "additional_comments" in value:
        out["AdditionalComments"] = value["additional_comments"]
    if "aws_partition" in value:
        import capo_partnercentral_selling.types.aws_partition

        out["AwsPartition"] = (
            capo_partnercentral_selling.types.aws_partition.serialize_aws_json_1_0(
                value["aws_partition"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Project:
    out: Project = {}  # type: ignore[typeddict-item]
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
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("ApnPrograms") is not None:
        import capo_partnercentral_selling.types.apn_programs

        out["apn_programs"] = (
            capo_partnercentral_selling.types.apn_programs.deserialize_aws_json_1_0(
                data["ApnPrograms"]
            )
        )
    if data.get("CustomerBusinessProblem") is not None:
        out["customer_business_problem"] = data["CustomerBusinessProblem"]
    if data.get("CustomerUseCase") is not None:
        out["customer_use_case"] = data["CustomerUseCase"]
    if data.get("RelatedOpportunityIdentifier") is not None:
        out["related_opportunity_identifier"] = data["RelatedOpportunityIdentifier"]
    if data.get("SalesActivities") is not None:
        import capo_partnercentral_selling.types.sales_activities

        out["sales_activities"] = (
            capo_partnercentral_selling.types.sales_activities.deserialize_aws_json_1_0(
                data["SalesActivities"]
            )
        )
    if data.get("CompetitorName") is not None:
        import capo_partnercentral_selling.types.competitor_name

        out["competitor_name"] = (
            capo_partnercentral_selling.types.competitor_name.deserialize_aws_json_1_0(
                data["CompetitorName"]
            )
        )
    if data.get("OtherCompetitorNames") is not None:
        out["other_competitor_names"] = data["OtherCompetitorNames"]
    if data.get("OtherSolutionDescription") is not None:
        out["other_solution_description"] = data["OtherSolutionDescription"]
    if data.get("AdditionalComments") is not None:
        out["additional_comments"] = data["AdditionalComments"]
    if data.get("AwsPartition") is not None:
        import capo_partnercentral_selling.types.aws_partition

        out["aws_partition"] = (
            capo_partnercentral_selling.types.aws_partition.deserialize_aws_json_1_0(
                data["AwsPartition"]
            )
        )
    return out


def redact_sensitive(value: Project) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expected_customer_spend" in value:
        import capo_partnercentral_selling.types.expected_customer_spend_list

        out["expected_customer_spend"] = (
            capo_partnercentral_selling.types.expected_customer_spend_list.redact_sensitive(
                value["expected_customer_spend"]
            )
        )
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "customer_business_problem" in value:
        out["customer_business_problem"] = "*** Sensitive Data Redacted ***"
    if "other_solution_description" in value:
        out["other_solution_description"] = "*** Sensitive Data Redacted ***"
    return out
