"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.auto_deployment
    import capo_cloudformation.types.capabilities
    import capo_cloudformation.types.description
    import capo_cloudformation.types.execution_role_name
    import capo_cloudformation.types.managed_execution
    import capo_cloudformation.types.organizational_unit_id_list
    import capo_cloudformation.types.parameters
    import capo_cloudformation.types.permission_models
    import capo_cloudformation.types.region_list
    import capo_cloudformation.types.role_arn
    import capo_cloudformation.types.stack_set_arn
    import capo_cloudformation.types.stack_set_drift_detection_details
    import capo_cloudformation.types.stack_set_id
    import capo_cloudformation.types.stack_set_name
    import capo_cloudformation.types.stack_set_status
    import capo_cloudformation.types.tags
    import capo_cloudformation.types.template_body


class StackSet(TypedDict, closed=True):
    stack_set_name: NotRequired["capo_cloudformation.types.stack_set_name.StackSetName"]
    """<p>The name that's associated with the StackSet.</p>"""
    stack_set_id: NotRequired["capo_cloudformation.types.stack_set_id.StackSetId"]
    """<p>The ID of the StackSet.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>A description of the StackSet that you specify when the StackSet is created or updated.</p>"""
    status: NotRequired["capo_cloudformation.types.stack_set_status.StackSetStatus"]
    """<p>The status of the StackSet.</p>"""
    template_body: NotRequired["capo_cloudformation.types.template_body.TemplateBody"]
    """<p>The structure that contains the body of the template that was used to create or update the StackSet.</p>"""
    parameters: NotRequired["capo_cloudformation.types.parameters.Parameters"]
    """<p>A list of input parameters for a StackSet.</p>"""
    capabilities: NotRequired["capo_cloudformation.types.capabilities.Capabilities"]
    """<p>The capabilities that are allowed in the StackSet. Some StackSet templates might include resources that can affect permissions in your Amazon Web Services account—for example, by creating new Identity and Access Management (IAM) users. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p>"""
    tags: NotRequired["capo_cloudformation.types.tags.Tags"]
    """<p>A list of tags that specify information about the StackSet. A maximum number of 50 tags can be specified.</p>"""
    stack_set_arn: NotRequired["capo_cloudformation.types.stack_set_arn.StackSetARN"]
    """<p>The Amazon Resource Name (ARN) of the StackSet.</p>"""
    administration_role_arn: NotRequired["capo_cloudformation.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the IAM role used to create or update the stack set.</p> <p>Use customized administrator roles to control which users or groups can manage specific StackSets within the same administrator account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Prerequisites for using CloudFormation StackSets</a> in the <i>CloudFormation User Guide</i>.</p>"""
    execution_role_name: NotRequired[
        "capo_cloudformation.types.execution_role_name.ExecutionRoleName"
    ]
    """<p>The name of the IAM execution role used to create or update the StackSet.</p> <p>Use customized execution roles to control which stack resources users and groups can include in their StackSets.</p>"""
    stack_set_drift_detection_details: NotRequired[
        "capo_cloudformation.types.stack_set_drift_detection_details.StackSetDriftDetectionDetails"
    ]
    """<p>Detailed information about the drift status of the StackSet.</p> <p>For StackSets, contains information about the last <i>completed</i> drift operation performed on the StackSet. Information about drift operations currently in progress isn't included.</p>"""
    auto_deployment: NotRequired[
        "capo_cloudformation.types.auto_deployment.AutoDeployment"
    ]
    """<p>Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organization or organizational unit (OU). Valid only if the StackSet uses service-managed permissions.</p>"""
    permission_model: NotRequired[
        "capo_cloudformation.types.permission_models.PermissionModels"
    ]
    """<p>Describes how the IAM roles required for StackSet operations are created.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html">Activate trusted access for StackSets with Organizations</a>.</p> </li> </ul>"""
    organizational_unit_ids: NotRequired[
        "capo_cloudformation.types.organizational_unit_id_list.OrganizationalUnitIdList"
    ]
    """<p>[Service-managed permissions] The organization root ID or organizational unit (OU) IDs that you specified for <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html">DeploymentTargets</a>.</p>"""
    managed_execution: NotRequired[
        "capo_cloudformation.types.managed_execution.ManagedExecution"
    ]
    """<p>Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.</p>"""
    regions: NotRequired["capo_cloudformation.types.region_list.RegionList"]
    """<p>Returns a list of all Amazon Web Services Regions the given StackSet has stack instances deployed in. The Amazon Web Services Regions list output is in no particular order.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: StackSet, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_set_name" in value:
        pairs.append((f"{key_prefix}StackSetName", str(value["stack_set_name"])))
    if "stack_set_id" in value:
        pairs.append((f"{key_prefix}StackSetId", str(value["stack_set_id"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "status" in value:
        import capo_cloudformation.types.stack_set_status

        capo_cloudformation.types.stack_set_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "template_body" in value:
        pairs.append((f"{key_prefix}TemplateBody", str(value["template_body"])))
    if "parameters" in value:
        import capo_cloudformation.types.parameters

        capo_cloudformation.types.parameters.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )
    if "capabilities" in value:
        import capo_cloudformation.types.capabilities

        capo_cloudformation.types.capabilities.serialize_query(
            value["capabilities"], pairs, f"{key_prefix}Capabilities"
        )
    if "tags" in value:
        import capo_cloudformation.types.tags

        capo_cloudformation.types.tags.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "stack_set_arn" in value:
        pairs.append((f"{key_prefix}StackSetARN", str(value["stack_set_arn"])))
    if "administration_role_arn" in value:
        pairs.append(
            (
                f"{key_prefix}AdministrationRoleARN",
                str(value["administration_role_arn"]),
            )
        )
    if "execution_role_name" in value:
        pairs.append(
            (f"{key_prefix}ExecutionRoleName", str(value["execution_role_name"]))
        )
    if "stack_set_drift_detection_details" in value:
        import capo_cloudformation.types.stack_set_drift_detection_details

        capo_cloudformation.types.stack_set_drift_detection_details.serialize_query(
            value["stack_set_drift_detection_details"],
            pairs,
            f"{key_prefix}StackSetDriftDetectionDetails",
        )
    if "auto_deployment" in value:
        import capo_cloudformation.types.auto_deployment

        capo_cloudformation.types.auto_deployment.serialize_query(
            value["auto_deployment"], pairs, f"{key_prefix}AutoDeployment"
        )
    if "permission_model" in value:
        import capo_cloudformation.types.permission_models

        capo_cloudformation.types.permission_models.serialize_query(
            value["permission_model"], pairs, f"{key_prefix}PermissionModel"
        )
    if "organizational_unit_ids" in value:
        import capo_cloudformation.types.organizational_unit_id_list

        capo_cloudformation.types.organizational_unit_id_list.serialize_query(
            value["organizational_unit_ids"],
            pairs,
            f"{key_prefix}OrganizationalUnitIds",
        )
    if "managed_execution" in value:
        import capo_cloudformation.types.managed_execution

        capo_cloudformation.types.managed_execution.serialize_query(
            value["managed_execution"], pairs, f"{key_prefix}ManagedExecution"
        )
    if "regions" in value:
        import capo_cloudformation.types.region_list

        capo_cloudformation.types.region_list.serialize_query(
            value["regions"], pairs, f"{key_prefix}Regions"
        )


def deserialize_query(el: Element) -> StackSet:
    out: StackSet = {}  # type: ignore[typeddict-item]
    child_stack_set_name = el.find("StackSetName")
    if child_stack_set_name is not None:
        out["stack_set_name"] = str(child_stack_set_name.text or "")
    child_stack_set_id = el.find("StackSetId")
    if child_stack_set_id is not None:
        out["stack_set_id"] = str(child_stack_set_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.stack_set_status

        out["status"] = capo_cloudformation.types.stack_set_status.deserialize_query(
            child_status
        )
    child_template_body = el.find("TemplateBody")
    if child_template_body is not None:
        out["template_body"] = str(child_template_body.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_cloudformation.types.parameters

        out["parameters"] = capo_cloudformation.types.parameters.deserialize_query(
            child_parameters
        )
    child_capabilities = el.find("Capabilities")
    if child_capabilities is not None:
        import capo_cloudformation.types.capabilities

        out["capabilities"] = capo_cloudformation.types.capabilities.deserialize_query(
            child_capabilities
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudformation.types.tags

        out["tags"] = capo_cloudformation.types.tags.deserialize_query(child_tags)
    child_stack_set_arn = el.find("StackSetARN")
    if child_stack_set_arn is not None:
        out["stack_set_arn"] = str(child_stack_set_arn.text or "")
    child_administration_role_arn = el.find("AdministrationRoleARN")
    if child_administration_role_arn is not None:
        out["administration_role_arn"] = str(child_administration_role_arn.text or "")
    child_execution_role_name = el.find("ExecutionRoleName")
    if child_execution_role_name is not None:
        out["execution_role_name"] = str(child_execution_role_name.text or "")
    child_stack_set_drift_detection_details = el.find("StackSetDriftDetectionDetails")
    if child_stack_set_drift_detection_details is not None:
        import capo_cloudformation.types.stack_set_drift_detection_details

        out["stack_set_drift_detection_details"] = (
            capo_cloudformation.types.stack_set_drift_detection_details.deserialize_query(
                child_stack_set_drift_detection_details
            )
        )
    child_auto_deployment = el.find("AutoDeployment")
    if child_auto_deployment is not None:
        import capo_cloudformation.types.auto_deployment

        out["auto_deployment"] = (
            capo_cloudformation.types.auto_deployment.deserialize_query(
                child_auto_deployment
            )
        )
    child_permission_model = el.find("PermissionModel")
    if child_permission_model is not None:
        import capo_cloudformation.types.permission_models

        out["permission_model"] = (
            capo_cloudformation.types.permission_models.deserialize_query(
                child_permission_model
            )
        )
    child_organizational_unit_ids = el.find("OrganizationalUnitIds")
    if child_organizational_unit_ids is not None:
        import capo_cloudformation.types.organizational_unit_id_list

        out["organizational_unit_ids"] = (
            capo_cloudformation.types.organizational_unit_id_list.deserialize_query(
                child_organizational_unit_ids
            )
        )
    child_managed_execution = el.find("ManagedExecution")
    if child_managed_execution is not None:
        import capo_cloudformation.types.managed_execution

        out["managed_execution"] = (
            capo_cloudformation.types.managed_execution.deserialize_query(
                child_managed_execution
            )
        )
    child_regions = el.find("Regions")
    if child_regions is not None:
        import capo_cloudformation.types.region_list

        out["regions"] = capo_cloudformation.types.region_list.deserialize_query(
            child_regions
        )
    return out
