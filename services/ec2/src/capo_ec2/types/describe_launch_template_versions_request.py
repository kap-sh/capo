"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLaunchTemplateVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.integer
    import capo_ec2.types.launch_template_id
    import capo_ec2.types.launch_template_name
    import capo_ec2.types.string
    import capo_ec2.types.version_string_list


class DescribeLaunchTemplateVersionsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    launch_template_id: NotRequired[
        "capo_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template.</p> <p>To describe one or more versions of a specified launch template, you must specify either the launch template ID or the launch template name, but not both.</p> <p>To describe all the latest or default launch template versions in your account, you must omit this parameter.</p>"""
    launch_template_name: NotRequired[
        "capo_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p> <p>To describe one or more versions of a specified launch template, you must specify either the launch template name or the launch template ID, but not both.</p> <p>To describe all the latest or default launch template versions in your account, you must omit this parameter.</p>"""
    versions: NotRequired["capo_ec2.types.version_string_list.VersionStringList"]
    """<p>One or more versions of the launch template. Valid values depend on whether you are describing a specified launch template (by ID or name) or all launch templates in your account.</p> <p>To describe one or more versions of a specified launch template, valid values are <code>$Latest</code>, <code>$Default</code>, and numbers.</p> <p>To describe all launch templates in your account that are defined as the latest version, the valid value is <code>$Latest</code>. To describe all launch templates in your account that are defined as the default version, the valid value is <code>$Default</code>. You can specify <code>$Latest</code> and <code>$Default</code> in the same request. You cannot specify numbers.</p>"""
    min_version: NotRequired["capo_ec2.types.string.String"]
    """<p>The version number after which to describe launch template versions.</p>"""
    max_version: NotRequired["capo_ec2.types.string.String"]
    """<p>The version number up to which to describe launch template versions.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to request the next page of results.</p>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. This value can be between 1 and 200.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>create-time</code> - The time the launch template version was created.</p> </li> <li> <p> <code>ebs-optimized</code> - A boolean that indicates whether the instance is optimized for Amazon EBS I/O.</p> </li> <li> <p> <code>http-endpoint</code> - Indicates whether the HTTP metadata endpoint on your instances is enabled (<code>enabled</code> | <code>disabled</code>).</p> </li> <li> <p> <code>http-protocol-ipv4</code> - Indicates whether the IPv4 endpoint for the instance metadata service is enabled (<code>enabled</code> | <code>disabled</code>).</p> </li> <li> <p> <code>host-resource-group-arn</code> - The ARN of the host resource group in which to launch the instances.</p> </li> <li> <p> <code>http-tokens</code> - The state of token usage for your instance metadata requests (<code>optional</code> | <code>required</code>).</p> </li> <li> <p> <code>iam-instance-profile</code> - The ARN of the IAM instance profile.</p> </li> <li> <p> <code>image-id</code> - The ID of the AMI.</p> </li> <li> <p> <code>instance-type</code> - The instance type.</p> </li> <li> <p> <code>is-default-version</code> - A boolean that indicates whether the launch template version is the default version.</p> </li> <li> <p> <code>kernel-id</code> - The kernel ID.</p> </li> <li> <p> <code>license-configuration-arn</code> - The ARN of the license configuration.</p> </li> <li> <p> <code>network-card-index</code> - The index of the network card.</p> </li> <li> <p> <code>ram-disk-id</code> - The RAM disk ID.</p> </li> </ul>"""
    resolve_alias: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, and if a Systems Manager parameter is specified for <code>ImageId</code>, the AMI ID is displayed in the response for <code>imageId</code>.</p> <p>If <code>false</code>, and if a Systems Manager parameter is specified for <code>ImageId</code>, the parameter is displayed in the response for <code>imageId</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id">Use a Systems Manager parameter instead of an AMI ID</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>false</code> </p>"""
    include_managed_resources: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to include managed resources in the output. If this parameter is set to <code>true</code>, the output includes resources that are managed by Amazon Web Services services, even if managed resource visibility is set to hidden.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLaunchTemplateVersionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "launch_template_id" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateId", str(value["launch_template_id"]))
        )
    if "launch_template_name" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateName", str(value["launch_template_name"]))
        )
    if "versions" in value:
        import capo_ec2.types.version_string_list

        capo_ec2.types.version_string_list.serialize_ec2_query(
            value["versions"], pairs, f"{key_prefix}LaunchTemplateVersion"
        )
    if "min_version" in value:
        pairs.append((f"{key_prefix}MinVersion", str(value["min_version"])))
    if "max_version" in value:
        pairs.append((f"{key_prefix}MaxVersion", str(value["max_version"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "resolve_alias" in value:
        pairs.append(
            (f"{key_prefix}ResolveAlias", "true" if value["resolve_alias"] else "false")
        )
    if "include_managed_resources" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeManagedResources",
                "true" if value["include_managed_resources"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> DescribeLaunchTemplateVersionsRequest:
    out: DescribeLaunchTemplateVersionsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_launch_template_id = el.find("LaunchTemplateId")
    if child_launch_template_id is not None:
        out["launch_template_id"] = str(child_launch_template_id.text or "")
    child_launch_template_name = el.find("LaunchTemplateName")
    if child_launch_template_name is not None:
        out["launch_template_name"] = str(child_launch_template_name.text or "")
    child_versions = el.find("LaunchTemplateVersion")
    if child_versions is not None:
        import capo_ec2.types.version_string_list

        out["versions"] = capo_ec2.types.version_string_list.deserialize_ec2_query(
            child_versions
        )
    child_min_version = el.find("MinVersion")
    if child_min_version is not None:
        out["min_version"] = str(child_min_version.text or "")
    child_max_version = el.find("MaxVersion")
    if child_max_version is not None:
        out["max_version"] = str(child_max_version.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_resolve_alias = el.find("ResolveAlias")
    if child_resolve_alias is not None:
        out["resolve_alias"] = (child_resolve_alias.text or "").lower() == "true"
    child_include_managed_resources = el.find("IncludeManagedResources")
    if child_include_managed_resources is not None:
        out["include_managed_resources"] = (
            child_include_managed_resources.text or ""
        ).lower() == "true"
    return out
