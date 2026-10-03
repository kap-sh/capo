"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLaunchTemplateVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.launch_template_id
    import capo_ec2.types.launch_template_name
    import capo_ec2.types.request_launch_template_data
    import capo_ec2.types.string
    import capo_ec2.types.version_description


class CreateLaunchTemplateVersionRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If a client token isn't specified, a randomly generated token is used in the request to ensure idempotency.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p> <p>Constraint: Maximum 128 ASCII characters.</p>"""
    launch_template_id: NotRequired[
        "capo_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    launch_template_name: NotRequired[
        "capo_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    source_version: NotRequired["capo_ec2.types.string.String"]
    """<p>The version of the launch template on which to base the new version. Snapshots applied to the block device mapping are ignored when creating a new version unless they are explicitly included.</p> <p>If you specify this parameter, the new version inherits the launch parameters from the source version. If you specify additional launch parameters for the new version, they overwrite any corresponding launch parameters inherited from the source version.</p> <p>If you omit this parameter, the new version contains only the launch parameters that you specify for the new version.</p>"""
    version_description: NotRequired[
        "capo_ec2.types.version_description.VersionDescription"
    ]
    """<p>A description for the version of the launch template.</p>"""
    launch_template_data: NotRequired[
        "capo_ec2.types.request_launch_template_data.RequestLaunchTemplateData"
    ]
    """<p>The information for the launch template.</p>"""
    resolve_alias: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, and if a Systems Manager parameter is specified for <code>ImageId</code>, the AMI ID is displayed in the response for <code>imageID</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id">Use a Systems Manager parameter instead of an AMI ID</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateLaunchTemplateVersionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "launch_template_id" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateId", str(value["launch_template_id"]))
        )
    if "launch_template_name" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateName", str(value["launch_template_name"]))
        )
    if "source_version" in value:
        pairs.append((f"{key_prefix}SourceVersion", str(value["source_version"])))
    if "version_description" in value:
        pairs.append(
            (f"{key_prefix}VersionDescription", str(value["version_description"]))
        )
    if "launch_template_data" in value:
        import capo_ec2.types.request_launch_template_data

        capo_ec2.types.request_launch_template_data.serialize_ec2_query(
            value["launch_template_data"], pairs, f"{key_prefix}LaunchTemplateData"
        )
    if "resolve_alias" in value:
        pairs.append(
            (f"{key_prefix}ResolveAlias", "true" if value["resolve_alias"] else "false")
        )


def deserialize_ec2_query(el: Element) -> CreateLaunchTemplateVersionRequest:
    out: CreateLaunchTemplateVersionRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_launch_template_id = el.find("LaunchTemplateId")
    if child_launch_template_id is not None:
        out["launch_template_id"] = str(child_launch_template_id.text or "")
    child_launch_template_name = el.find("LaunchTemplateName")
    if child_launch_template_name is not None:
        out["launch_template_name"] = str(child_launch_template_name.text or "")
    child_source_version = el.find("SourceVersion")
    if child_source_version is not None:
        out["source_version"] = str(child_source_version.text or "")
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
    child_resolve_alias = el.find("ResolveAlias")
    if child_resolve_alias is not None:
        out["resolve_alias"] = (child_resolve_alias.text or "").lower() == "true"
    return out
