"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesFindingFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.date_filter_list
    import capo_securityhub.types.map_filter_list
    import capo_securityhub.types.number_filter_list
    import capo_securityhub.types.string_filter_list


class AutomationRulesFindingFilters(TypedDict, closed=True):
    product_arn: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The Amazon Resource Name (ARN) for a third-party product that generated a finding in Security Hub CSPM. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    aws_account_id: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p>The Amazon Web Services account ID in which a finding was generated.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 100 items. </p>"""
    id: NotRequired["capo_securityhub.types.string_filter_list.StringFilterList"]
    """<p> The product-specific identifier for a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    generator_id: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The identifier for the solution-specific component that generated a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 100 items. </p>"""
    type: NotRequired["capo_securityhub.types.string_filter_list.StringFilterList"]
    """<p> One or more finding types in the format of namespace/category/classifier that classify a finding. For a list of namespaces, classifiers, and categories, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.html">Types taxonomy for ASFF</a> in the <i>Security Hub CSPM User Guide</i>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    first_observed_at: NotRequired[
        "capo_securityhub.types.date_filter_list.DateFilterList"
    ]
    """<p> A timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings product. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    last_observed_at: NotRequired[
        "capo_securityhub.types.date_filter_list.DateFilterList"
    ]
    """<p> A timestamp that indicates when the security findings provider most recently observed a change in the resource that is involved in the finding. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    created_at: NotRequired["capo_securityhub.types.date_filter_list.DateFilterList"]
    """<p> A timestamp that indicates when this finding record was created. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    updated_at: NotRequired["capo_securityhub.types.date_filter_list.DateFilterList"]
    """<p> A timestamp that indicates when the finding record was most recently updated. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    confidence: NotRequired[
        "capo_securityhub.types.number_filter_list.NumberFilterList"
    ]
    """<p>The likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. <code>Confidence</code> is scored on a 0–100 basis using a ratio scale. A value of <code>0</code> means 0 percent confidence, and a value of <code>100</code> means 100 percent confidence. For example, a data exfiltration detection based on a statistical deviation of network traffic has low confidence because an actual exfiltration hasn't been verified. For more information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-confidence">Confidence</a> in the <i>Security Hub CSPM User Guide</i>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    criticality: NotRequired[
        "capo_securityhub.types.number_filter_list.NumberFilterList"
    ]
    """<p> The level of importance that is assigned to the resources that are associated with a finding. <code>Criticality</code> is scored on a 0–100 basis, using a ratio scale that supports only full integers. A score of <code>0</code> means that the underlying resources have no criticality, and a score of <code>100</code> is reserved for the most critical resources. For more information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-criticality">Criticality</a> in the <i>Security Hub CSPM User Guide</i>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    title: NotRequired["capo_securityhub.types.string_filter_list.StringFilterList"]
    """<p> A finding's title. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 100 items. </p>"""
    description: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> A finding's description. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    source_url: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> Provides a URL that links to a page about the current finding in the finding product. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    product_name: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> Provides the name of the product that generated the finding. For control-based findings, the product name is Security Hub CSPM. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    company_name: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The name of the company for the product that generated the finding. For control-based findings, the company is Amazon Web Services. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    severity_label: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The severity value of the finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_type: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The type of resource that the finding pertains to. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_id: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The identifier for the given resource type. For Amazon Web Services resources that are identified by Amazon Resource Names (ARNs), this is the ARN. For Amazon Web Services resources that lack ARNs, this is the identifier as defined by the Amazon Web Services service that created the resource. For non-Amazon Web Services resources, this is a unique identifier that is associated with the resource. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 100 items. </p>"""
    resource_partition: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The partition in which the resource that the finding pertains to is located. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_region: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The Amazon Web Services Region where the resource that a finding pertains to is located. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_tags: NotRequired["capo_securityhub.types.map_filter_list.MapFilterList"]
    """<p> A list of Amazon Web Services tags associated with a resource at the time the finding was processed. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_details_other: NotRequired[
        "capo_securityhub.types.map_filter_list.MapFilterList"
    ]
    """<p> Custom fields and values about the resource that a finding pertains to. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    compliance_status: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The result of a security check. This field is only used for findings generated from controls. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    compliance_security_control_id: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The security control ID for which a finding was generated. Security control IDs are the same across standards.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    compliance_associated_standards_id: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p>The unique identifier of a standard in which a control is enabled. This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html">DescribeStandards</a> API response.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    verification_state: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> Provides the veracity of a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    workflow_status: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> Provides information about the status of the investigation into a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    record_state: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> Provides the current state of a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    related_findings_product_arn: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The ARN for the product that generated a related finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    related_findings_id: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The product-generated identifier for a related finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    note_text: NotRequired["capo_securityhub.types.string_filter_list.StringFilterList"]
    """<p> The text of a user-defined note that's added to a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    note_updated_at: NotRequired[
        "capo_securityhub.types.date_filter_list.DateFilterList"
    ]
    """<p> The timestamp of when the note was updated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    note_updated_by: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The principal that created a note. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    user_defined_fields: NotRequired[
        "capo_securityhub.types.map_filter_list.MapFilterList"
    ]
    """<p> A list of user-defined name and value string pairs added to a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_application_arn: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The Amazon Resource Name (ARN) of the application that is related to a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_application_name: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The name of the application that is related to a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    aws_account_name: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p>The name of the Amazon Web Services account in which a finding was generated. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_provider: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud provider that the resource belongs to. Valid values are <code>AWS</code> and <code>Azure</code>.</p>"""
    resource_owner_account_id: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p>The unique identifier of the account that owns the resource that the finding applies to, for example, Azure Subscription Id or Amazon Web Services Account Id</p>"""
    resource_owner_org_id: NotRequired[
        "capo_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p>The unique identifier of the organization that owns the resource that the finding applies to, for example, Azure Tenant Id</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesFindingFilters) -> dict:
    out: dict = {}
    if "product_arn" in value:
        import capo_securityhub.types.string_filter_list

        out["ProductArn"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["product_arn"]
        )
    if "aws_account_id" in value:
        import capo_securityhub.types.string_filter_list

        out["AwsAccountId"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["aws_account_id"]
        )
    if "id" in value:
        import capo_securityhub.types.string_filter_list

        out["Id"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["id"]
        )
    if "generator_id" in value:
        import capo_securityhub.types.string_filter_list

        out["GeneratorId"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["generator_id"]
        )
    if "type" in value:
        import capo_securityhub.types.string_filter_list

        out["Type"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["type"]
        )
    if "first_observed_at" in value:
        import capo_securityhub.types.date_filter_list

        out["FirstObservedAt"] = capo_securityhub.types.date_filter_list.serialize_json(
            value["first_observed_at"]
        )
    if "last_observed_at" in value:
        import capo_securityhub.types.date_filter_list

        out["LastObservedAt"] = capo_securityhub.types.date_filter_list.serialize_json(
            value["last_observed_at"]
        )
    if "created_at" in value:
        import capo_securityhub.types.date_filter_list

        out["CreatedAt"] = capo_securityhub.types.date_filter_list.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityhub.types.date_filter_list

        out["UpdatedAt"] = capo_securityhub.types.date_filter_list.serialize_json(
            value["updated_at"]
        )
    if "confidence" in value:
        import capo_securityhub.types.number_filter_list

        out["Confidence"] = capo_securityhub.types.number_filter_list.serialize_json(
            value["confidence"]
        )
    if "criticality" in value:
        import capo_securityhub.types.number_filter_list

        out["Criticality"] = capo_securityhub.types.number_filter_list.serialize_json(
            value["criticality"]
        )
    if "title" in value:
        import capo_securityhub.types.string_filter_list

        out["Title"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["title"]
        )
    if "description" in value:
        import capo_securityhub.types.string_filter_list

        out["Description"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["description"]
        )
    if "source_url" in value:
        import capo_securityhub.types.string_filter_list

        out["SourceUrl"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["source_url"]
        )
    if "product_name" in value:
        import capo_securityhub.types.string_filter_list

        out["ProductName"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["product_name"]
        )
    if "company_name" in value:
        import capo_securityhub.types.string_filter_list

        out["CompanyName"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["company_name"]
        )
    if "severity_label" in value:
        import capo_securityhub.types.string_filter_list

        out["SeverityLabel"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["severity_label"]
        )
    if "resource_type" in value:
        import capo_securityhub.types.string_filter_list

        out["ResourceType"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["resource_type"]
        )
    if "resource_id" in value:
        import capo_securityhub.types.string_filter_list

        out["ResourceId"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["resource_id"]
        )
    if "resource_partition" in value:
        import capo_securityhub.types.string_filter_list

        out["ResourcePartition"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["resource_partition"]
            )
        )
    if "resource_region" in value:
        import capo_securityhub.types.string_filter_list

        out["ResourceRegion"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["resource_region"]
            )
        )
    if "resource_tags" in value:
        import capo_securityhub.types.map_filter_list

        out["ResourceTags"] = capo_securityhub.types.map_filter_list.serialize_json(
            value["resource_tags"]
        )
    if "resource_details_other" in value:
        import capo_securityhub.types.map_filter_list

        out["ResourceDetailsOther"] = (
            capo_securityhub.types.map_filter_list.serialize_json(
                value["resource_details_other"]
            )
        )
    if "compliance_status" in value:
        import capo_securityhub.types.string_filter_list

        out["ComplianceStatus"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["compliance_status"]
            )
        )
    if "compliance_security_control_id" in value:
        import capo_securityhub.types.string_filter_list

        out["ComplianceSecurityControlId"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["compliance_security_control_id"]
            )
        )
    if "compliance_associated_standards_id" in value:
        import capo_securityhub.types.string_filter_list

        out["ComplianceAssociatedStandardsId"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["compliance_associated_standards_id"]
            )
        )
    if "verification_state" in value:
        import capo_securityhub.types.string_filter_list

        out["VerificationState"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["verification_state"]
            )
        )
    if "workflow_status" in value:
        import capo_securityhub.types.string_filter_list

        out["WorkflowStatus"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["workflow_status"]
            )
        )
    if "record_state" in value:
        import capo_securityhub.types.string_filter_list

        out["RecordState"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["record_state"]
        )
    if "related_findings_product_arn" in value:
        import capo_securityhub.types.string_filter_list

        out["RelatedFindingsProductArn"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["related_findings_product_arn"]
            )
        )
    if "related_findings_id" in value:
        import capo_securityhub.types.string_filter_list

        out["RelatedFindingsId"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["related_findings_id"]
            )
        )
    if "note_text" in value:
        import capo_securityhub.types.string_filter_list

        out["NoteText"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["note_text"]
        )
    if "note_updated_at" in value:
        import capo_securityhub.types.date_filter_list

        out["NoteUpdatedAt"] = capo_securityhub.types.date_filter_list.serialize_json(
            value["note_updated_at"]
        )
    if "note_updated_by" in value:
        import capo_securityhub.types.string_filter_list

        out["NoteUpdatedBy"] = capo_securityhub.types.string_filter_list.serialize_json(
            value["note_updated_by"]
        )
    if "user_defined_fields" in value:
        import capo_securityhub.types.map_filter_list

        out["UserDefinedFields"] = (
            capo_securityhub.types.map_filter_list.serialize_json(
                value["user_defined_fields"]
            )
        )
    if "resource_application_arn" in value:
        import capo_securityhub.types.string_filter_list

        out["ResourceApplicationArn"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["resource_application_arn"]
            )
        )
    if "resource_application_name" in value:
        import capo_securityhub.types.string_filter_list

        out["ResourceApplicationName"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["resource_application_name"]
            )
        )
    if "aws_account_name" in value:
        import capo_securityhub.types.string_filter_list

        out["AwsAccountName"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["aws_account_name"]
            )
        )
    if "resource_provider" in value:
        import capo_securityhub.types.string_filter_list

        out["ResourceProvider"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["resource_provider"]
            )
        )
    if "resource_owner_account_id" in value:
        import capo_securityhub.types.string_filter_list

        out["ResourceOwnerAccountId"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["resource_owner_account_id"]
            )
        )
    if "resource_owner_org_id" in value:
        import capo_securityhub.types.string_filter_list

        out["ResourceOwnerOrgId"] = (
            capo_securityhub.types.string_filter_list.serialize_json(
                value["resource_owner_org_id"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomationRulesFindingFilters:
    out: AutomationRulesFindingFilters = {}  # type: ignore[typeddict-item]
    if data.get("ProductArn") is not None:
        import capo_securityhub.types.string_filter_list

        out["product_arn"] = capo_securityhub.types.string_filter_list.deserialize_json(
            data["ProductArn"]
        )
    if data.get("AwsAccountId") is not None:
        import capo_securityhub.types.string_filter_list

        out["aws_account_id"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["AwsAccountId"]
            )
        )
    if data.get("Id") is not None:
        import capo_securityhub.types.string_filter_list

        out["id"] = capo_securityhub.types.string_filter_list.deserialize_json(
            data["Id"]
        )
    if data.get("GeneratorId") is not None:
        import capo_securityhub.types.string_filter_list

        out["generator_id"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["GeneratorId"]
            )
        )
    if data.get("Type") is not None:
        import capo_securityhub.types.string_filter_list

        out["type"] = capo_securityhub.types.string_filter_list.deserialize_json(
            data["Type"]
        )
    if data.get("FirstObservedAt") is not None:
        import capo_securityhub.types.date_filter_list

        out["first_observed_at"] = (
            capo_securityhub.types.date_filter_list.deserialize_json(
                data["FirstObservedAt"]
            )
        )
    if data.get("LastObservedAt") is not None:
        import capo_securityhub.types.date_filter_list

        out["last_observed_at"] = (
            capo_securityhub.types.date_filter_list.deserialize_json(
                data["LastObservedAt"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_securityhub.types.date_filter_list

        out["created_at"] = capo_securityhub.types.date_filter_list.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_securityhub.types.date_filter_list

        out["updated_at"] = capo_securityhub.types.date_filter_list.deserialize_json(
            data["UpdatedAt"]
        )
    if data.get("Confidence") is not None:
        import capo_securityhub.types.number_filter_list

        out["confidence"] = capo_securityhub.types.number_filter_list.deserialize_json(
            data["Confidence"]
        )
    if data.get("Criticality") is not None:
        import capo_securityhub.types.number_filter_list

        out["criticality"] = capo_securityhub.types.number_filter_list.deserialize_json(
            data["Criticality"]
        )
    if data.get("Title") is not None:
        import capo_securityhub.types.string_filter_list

        out["title"] = capo_securityhub.types.string_filter_list.deserialize_json(
            data["Title"]
        )
    if data.get("Description") is not None:
        import capo_securityhub.types.string_filter_list

        out["description"] = capo_securityhub.types.string_filter_list.deserialize_json(
            data["Description"]
        )
    if data.get("SourceUrl") is not None:
        import capo_securityhub.types.string_filter_list

        out["source_url"] = capo_securityhub.types.string_filter_list.deserialize_json(
            data["SourceUrl"]
        )
    if data.get("ProductName") is not None:
        import capo_securityhub.types.string_filter_list

        out["product_name"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ProductName"]
            )
        )
    if data.get("CompanyName") is not None:
        import capo_securityhub.types.string_filter_list

        out["company_name"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["CompanyName"]
            )
        )
    if data.get("SeverityLabel") is not None:
        import capo_securityhub.types.string_filter_list

        out["severity_label"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["SeverityLabel"]
            )
        )
    if data.get("ResourceType") is not None:
        import capo_securityhub.types.string_filter_list

        out["resource_type"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceType"]
            )
        )
    if data.get("ResourceId") is not None:
        import capo_securityhub.types.string_filter_list

        out["resource_id"] = capo_securityhub.types.string_filter_list.deserialize_json(
            data["ResourceId"]
        )
    if data.get("ResourcePartition") is not None:
        import capo_securityhub.types.string_filter_list

        out["resource_partition"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ResourcePartition"]
            )
        )
    if data.get("ResourceRegion") is not None:
        import capo_securityhub.types.string_filter_list

        out["resource_region"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceRegion"]
            )
        )
    if data.get("ResourceTags") is not None:
        import capo_securityhub.types.map_filter_list

        out["resource_tags"] = capo_securityhub.types.map_filter_list.deserialize_json(
            data["ResourceTags"]
        )
    if data.get("ResourceDetailsOther") is not None:
        import capo_securityhub.types.map_filter_list

        out["resource_details_other"] = (
            capo_securityhub.types.map_filter_list.deserialize_json(
                data["ResourceDetailsOther"]
            )
        )
    if data.get("ComplianceStatus") is not None:
        import capo_securityhub.types.string_filter_list

        out["compliance_status"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ComplianceStatus"]
            )
        )
    if data.get("ComplianceSecurityControlId") is not None:
        import capo_securityhub.types.string_filter_list

        out["compliance_security_control_id"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ComplianceSecurityControlId"]
            )
        )
    if data.get("ComplianceAssociatedStandardsId") is not None:
        import capo_securityhub.types.string_filter_list

        out["compliance_associated_standards_id"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ComplianceAssociatedStandardsId"]
            )
        )
    if data.get("VerificationState") is not None:
        import capo_securityhub.types.string_filter_list

        out["verification_state"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["VerificationState"]
            )
        )
    if data.get("WorkflowStatus") is not None:
        import capo_securityhub.types.string_filter_list

        out["workflow_status"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["WorkflowStatus"]
            )
        )
    if data.get("RecordState") is not None:
        import capo_securityhub.types.string_filter_list

        out["record_state"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["RecordState"]
            )
        )
    if data.get("RelatedFindingsProductArn") is not None:
        import capo_securityhub.types.string_filter_list

        out["related_findings_product_arn"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["RelatedFindingsProductArn"]
            )
        )
    if data.get("RelatedFindingsId") is not None:
        import capo_securityhub.types.string_filter_list

        out["related_findings_id"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["RelatedFindingsId"]
            )
        )
    if data.get("NoteText") is not None:
        import capo_securityhub.types.string_filter_list

        out["note_text"] = capo_securityhub.types.string_filter_list.deserialize_json(
            data["NoteText"]
        )
    if data.get("NoteUpdatedAt") is not None:
        import capo_securityhub.types.date_filter_list

        out["note_updated_at"] = (
            capo_securityhub.types.date_filter_list.deserialize_json(
                data["NoteUpdatedAt"]
            )
        )
    if data.get("NoteUpdatedBy") is not None:
        import capo_securityhub.types.string_filter_list

        out["note_updated_by"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["NoteUpdatedBy"]
            )
        )
    if data.get("UserDefinedFields") is not None:
        import capo_securityhub.types.map_filter_list

        out["user_defined_fields"] = (
            capo_securityhub.types.map_filter_list.deserialize_json(
                data["UserDefinedFields"]
            )
        )
    if data.get("ResourceApplicationArn") is not None:
        import capo_securityhub.types.string_filter_list

        out["resource_application_arn"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceApplicationArn"]
            )
        )
    if data.get("ResourceApplicationName") is not None:
        import capo_securityhub.types.string_filter_list

        out["resource_application_name"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceApplicationName"]
            )
        )
    if data.get("AwsAccountName") is not None:
        import capo_securityhub.types.string_filter_list

        out["aws_account_name"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["AwsAccountName"]
            )
        )
    if data.get("ResourceProvider") is not None:
        import capo_securityhub.types.string_filter_list

        out["resource_provider"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceProvider"]
            )
        )
    if data.get("ResourceOwnerAccountId") is not None:
        import capo_securityhub.types.string_filter_list

        out["resource_owner_account_id"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceOwnerAccountId"]
            )
        )
    if data.get("ResourceOwnerOrgId") is not None:
        import capo_securityhub.types.string_filter_list

        out["resource_owner_org_id"] = (
            capo_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceOwnerOrgId"]
            )
        )
    return out
