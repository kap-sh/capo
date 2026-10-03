"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLaunchTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.operator_request
    import capo_ec2.types.request_launch_template_data
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.version_description


class CreateLaunchTemplateRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If a client token isn't specified, a randomly generated token is used in the request to ensure idempotency.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p> <p>Constraint: Maximum 128 ASCII characters.</p>"""
    launch_template_name: NotRequired["capo_ec2.types.string.String"]
    """<p>A name for the launch template.</p>"""
    version_description: NotRequired[
        "capo_ec2.types.version_description.VersionDescription"
    ]
    """<p>A description for the first version of the launch template.</p>"""
    launch_template_data: NotRequired[
        "capo_ec2.types.request_launch_template_data.RequestLaunchTemplateData"
    ]
    """<p>The information for the launch template.</p>"""
    operator: NotRequired["capo_ec2.types.operator_request.OperatorRequest"]
    """<p>Reserved for internal use.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the launch template on creation. To tag the launch template, the resource type must be <code>launch-template</code>.</p> <p>To specify the tags for the resources that are created when an instance is launched, you must use the <code>TagSpecifications</code> parameter in the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestLaunchTemplateData.html">launch template data</a> structure.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateLaunchTemplateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "launch_template_name" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateName", str(value["launch_template_name"]))
        )
    if "version_description" in value:
        pairs.append(
            (f"{key_prefix}VersionDescription", str(value["version_description"]))
        )
    if "launch_template_data" in value:
        import capo_ec2.types.request_launch_template_data

        capo_ec2.types.request_launch_template_data.serialize_ec2_query(
            value["launch_template_data"], pairs, f"{key_prefix}LaunchTemplateData"
        )
    if "operator" in value:
        import capo_ec2.types.operator_request

        capo_ec2.types.operator_request.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )


def deserialize_ec2_query(el: Element) -> CreateLaunchTemplateRequest:
    out: CreateLaunchTemplateRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_launch_template_name = el.find("LaunchTemplateName")
    if child_launch_template_name is not None:
        out["launch_template_name"] = str(child_launch_template_name.text or "")
    child_version_description = el.find("VersionDescription")
    if child_version_description is not None:
        out["version_description"] = str(child_version_description.text or "")
    child_launch_template_data = el.find("LaunchTemplateData")
    if child_launch_template_data is not None:
        import capo_ec2.types.request_launch_template_data

        out["launch_template_data"] = (
            capo_ec2.types.request_launch_template_data.deserialize_ec2_query(
                child_launch_template_data
            )
        )
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_request

        out["operator"] = capo_ec2.types.operator_request.deserialize_ec2_query(
            child_operator
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    return out
