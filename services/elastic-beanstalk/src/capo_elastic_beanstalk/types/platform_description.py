"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.branch_name
    import capo_elastic_beanstalk.types.creation_date
    import capo_elastic_beanstalk.types.custom_ami_list
    import capo_elastic_beanstalk.types.default_ami_list
    import capo_elastic_beanstalk.types.description
    import capo_elastic_beanstalk.types.maintainer
    import capo_elastic_beanstalk.types.operating_system_name
    import capo_elastic_beanstalk.types.operating_system_version
    import capo_elastic_beanstalk.types.platform_arn
    import capo_elastic_beanstalk.types.platform_branch_lifecycle_state
    import capo_elastic_beanstalk.types.platform_category
    import capo_elastic_beanstalk.types.platform_frameworks
    import capo_elastic_beanstalk.types.platform_lifecycle_state
    import capo_elastic_beanstalk.types.platform_name
    import capo_elastic_beanstalk.types.platform_owner
    import capo_elastic_beanstalk.types.platform_programming_languages
    import capo_elastic_beanstalk.types.platform_status
    import capo_elastic_beanstalk.types.platform_version
    import capo_elastic_beanstalk.types.solution_stack_name
    import capo_elastic_beanstalk.types.supported_addon_list
    import capo_elastic_beanstalk.types.supported_tier_list
    import capo_elastic_beanstalk.types.update_date


class PlatformDescription(TypedDict, closed=True):
    platform_arn: NotRequired["capo_elastic_beanstalk.types.platform_arn.PlatformArn"]
    """<p>The ARN of the platform version.</p>"""
    platform_owner: NotRequired[
        "capo_elastic_beanstalk.types.platform_owner.PlatformOwner"
    ]
    """<p>The Amazon Web Services account ID of the person who created the platform version.</p>"""
    platform_name: NotRequired[
        "capo_elastic_beanstalk.types.platform_name.PlatformName"
    ]
    """<p>The name of the platform version.</p>"""
    platform_version: NotRequired[
        "capo_elastic_beanstalk.types.platform_version.PlatformVersion"
    ]
    """<p>The version of the platform version.</p>"""
    solution_stack_name: NotRequired[
        "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
    ]
    """<p>The name of the solution stack used by the platform version.</p>"""
    platform_status: NotRequired[
        "capo_elastic_beanstalk.types.platform_status.PlatformStatus"
    ]
    """<p>The status of the platform version.</p>"""
    date_created: NotRequired["capo_elastic_beanstalk.types.creation_date.CreationDate"]
    """<p>The date when the platform version was created.</p>"""
    date_updated: NotRequired["capo_elastic_beanstalk.types.update_date.UpdateDate"]
    """<p>The date when the platform version was last updated.</p>"""
    platform_category: NotRequired[
        "capo_elastic_beanstalk.types.platform_category.PlatformCategory"
    ]
    """<p>The category of the platform version.</p>"""
    description: NotRequired["capo_elastic_beanstalk.types.description.Description"]
    """<p>The description of the platform version.</p>"""
    maintainer: NotRequired["capo_elastic_beanstalk.types.maintainer.Maintainer"]
    """<p>Information about the maintainer of the platform version.</p>"""
    operating_system_name: NotRequired[
        "capo_elastic_beanstalk.types.operating_system_name.OperatingSystemName"
    ]
    """<p>The operating system used by the platform version.</p>"""
    operating_system_version: NotRequired[
        "capo_elastic_beanstalk.types.operating_system_version.OperatingSystemVersion"
    ]
    """<p>The version of the operating system used by the platform version.</p>"""
    programming_languages: NotRequired[
        "capo_elastic_beanstalk.types.platform_programming_languages.PlatformProgrammingLanguages"
    ]
    """<p>The programming languages supported by the platform version.</p>"""
    frameworks: NotRequired[
        "capo_elastic_beanstalk.types.platform_frameworks.PlatformFrameworks"
    ]
    """<p>The frameworks supported by the platform version.</p>"""
    custom_ami_list: NotRequired[
        "capo_elastic_beanstalk.types.custom_ami_list.CustomAmiList"
    ]
    """<p>The AMIs of the platform version, by virtualization type. For Elastic Beanstalk managed platforms, these are the default <code>x86_64</code> AMIs; for custom platforms, the <code>hvm</code> entry is the AMI built for the platform version. To find a managed platform's default AMIs for every supported processor architecture, including <code>arm64</code>, use <code>DefaultAmiList</code>.</p>"""
    default_ami_list: NotRequired[
        "capo_elastic_beanstalk.types.default_ami_list.DefaultAmiList"
    ]
    """<p>The AMIs that Elastic Beanstalk uses by default for the platform version, one for each supported processor architecture. When an environment doesn't specify a custom AMI, Elastic Beanstalk chooses the default AMI that matches the environment's architecture.</p> <p>This list isn't returned for custom platforms.</p>"""
    supported_tier_list: NotRequired[
        "capo_elastic_beanstalk.types.supported_tier_list.SupportedTierList"
    ]
    """<p>The tiers supported by the platform version.</p>"""
    supported_addon_list: NotRequired[
        "capo_elastic_beanstalk.types.supported_addon_list.SupportedAddonList"
    ]
    """<p>The additions supported by the platform version.</p>"""
    platform_lifecycle_state: NotRequired[
        "capo_elastic_beanstalk.types.platform_lifecycle_state.PlatformLifecycleState"
    ]
    """<p>The state of the platform version in its lifecycle.</p> <p>Possible values: <code>Recommended</code> | <code>null</code> </p> <p>If a null value is returned, the platform version isn't the recommended one for its branch. Each platform branch has a single recommended platform version, typically the most recent one.</p>"""
    platform_branch_name: NotRequired[
        "capo_elastic_beanstalk.types.branch_name.BranchName"
    ]
    """<p>The platform branch to which the platform version belongs.</p>"""
    platform_branch_lifecycle_state: NotRequired[
        "capo_elastic_beanstalk.types.platform_branch_lifecycle_state.PlatformBranchLifecycleState"
    ]
    """<p>The state of the platform version's branch in its lifecycle.</p> <p>Possible values: <code>Beta</code> | <code>Supported</code> | <code>Deprecated</code> | <code>Retired</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "platform_arn" in value:
        pairs.append((f"{key_prefix}PlatformArn", str(value["platform_arn"])))
    if "platform_owner" in value:
        pairs.append((f"{key_prefix}PlatformOwner", str(value["platform_owner"])))
    if "platform_name" in value:
        pairs.append((f"{key_prefix}PlatformName", str(value["platform_name"])))
    if "platform_version" in value:
        pairs.append((f"{key_prefix}PlatformVersion", str(value["platform_version"])))
    if "solution_stack_name" in value:
        pairs.append(
            (f"{key_prefix}SolutionStackName", str(value["solution_stack_name"]))
        )
    if "platform_status" in value:
        import capo_elastic_beanstalk.types.platform_status

        capo_elastic_beanstalk.types.platform_status.serialize_query(
            value["platform_status"], pairs, f"{key_prefix}PlatformStatus"
        )
    if "date_created" in value:
        import capo_elastic_beanstalk.types.creation_date

        capo_elastic_beanstalk.types.creation_date.serialize_query(
            value["date_created"], pairs, f"{key_prefix}DateCreated"
        )
    if "date_updated" in value:
        import capo_elastic_beanstalk.types.update_date

        capo_elastic_beanstalk.types.update_date.serialize_query(
            value["date_updated"], pairs, f"{key_prefix}DateUpdated"
        )
    if "platform_category" in value:
        pairs.append((f"{key_prefix}PlatformCategory", str(value["platform_category"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "maintainer" in value:
        pairs.append((f"{key_prefix}Maintainer", str(value["maintainer"])))
    if "operating_system_name" in value:
        pairs.append(
            (f"{key_prefix}OperatingSystemName", str(value["operating_system_name"]))
        )
    if "operating_system_version" in value:
        pairs.append(
            (
                f"{key_prefix}OperatingSystemVersion",
                str(value["operating_system_version"]),
            )
        )
    if "programming_languages" in value:
        import capo_elastic_beanstalk.types.platform_programming_languages

        capo_elastic_beanstalk.types.platform_programming_languages.serialize_query(
            value["programming_languages"], pairs, f"{key_prefix}ProgrammingLanguages"
        )
    if "frameworks" in value:
        import capo_elastic_beanstalk.types.platform_frameworks

        capo_elastic_beanstalk.types.platform_frameworks.serialize_query(
            value["frameworks"], pairs, f"{key_prefix}Frameworks"
        )
    if "custom_ami_list" in value:
        import capo_elastic_beanstalk.types.custom_ami_list

        capo_elastic_beanstalk.types.custom_ami_list.serialize_query(
            value["custom_ami_list"], pairs, f"{key_prefix}CustomAmiList"
        )
    if "default_ami_list" in value:
        import capo_elastic_beanstalk.types.default_ami_list

        capo_elastic_beanstalk.types.default_ami_list.serialize_query(
            value["default_ami_list"], pairs, f"{key_prefix}DefaultAmiList"
        )
    if "supported_tier_list" in value:
        import capo_elastic_beanstalk.types.supported_tier_list

        capo_elastic_beanstalk.types.supported_tier_list.serialize_query(
            value["supported_tier_list"], pairs, f"{key_prefix}SupportedTierList"
        )
    if "supported_addon_list" in value:
        import capo_elastic_beanstalk.types.supported_addon_list

        capo_elastic_beanstalk.types.supported_addon_list.serialize_query(
            value["supported_addon_list"], pairs, f"{key_prefix}SupportedAddonList"
        )
    if "platform_lifecycle_state" in value:
        pairs.append(
            (
                f"{key_prefix}PlatformLifecycleState",
                str(value["platform_lifecycle_state"]),
            )
        )
    if "platform_branch_name" in value:
        pairs.append(
            (f"{key_prefix}PlatformBranchName", str(value["platform_branch_name"]))
        )
    if "platform_branch_lifecycle_state" in value:
        pairs.append(
            (
                f"{key_prefix}PlatformBranchLifecycleState",
                str(value["platform_branch_lifecycle_state"]),
            )
        )


def deserialize_query(el: Element) -> PlatformDescription:
    out: PlatformDescription = {}  # type: ignore[typeddict-item]
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    child_platform_owner = el.find("PlatformOwner")
    if child_platform_owner is not None:
        out["platform_owner"] = str(child_platform_owner.text or "")
    child_platform_name = el.find("PlatformName")
    if child_platform_name is not None:
        out["platform_name"] = str(child_platform_name.text or "")
    child_platform_version = el.find("PlatformVersion")
    if child_platform_version is not None:
        out["platform_version"] = str(child_platform_version.text or "")
    child_solution_stack_name = el.find("SolutionStackName")
    if child_solution_stack_name is not None:
        out["solution_stack_name"] = str(child_solution_stack_name.text or "")
    child_platform_status = el.find("PlatformStatus")
    if child_platform_status is not None:
        import capo_elastic_beanstalk.types.platform_status

        out["platform_status"] = (
            capo_elastic_beanstalk.types.platform_status.deserialize_query(
                child_platform_status
            )
        )
    child_date_created = el.find("DateCreated")
    if child_date_created is not None:
        import capo_elastic_beanstalk.types.creation_date

        out["date_created"] = (
            capo_elastic_beanstalk.types.creation_date.deserialize_query(
                child_date_created
            )
        )
    child_date_updated = el.find("DateUpdated")
    if child_date_updated is not None:
        import capo_elastic_beanstalk.types.update_date

        out["date_updated"] = (
            capo_elastic_beanstalk.types.update_date.deserialize_query(
                child_date_updated
            )
        )
    child_platform_category = el.find("PlatformCategory")
    if child_platform_category is not None:
        out["platform_category"] = str(child_platform_category.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_maintainer = el.find("Maintainer")
    if child_maintainer is not None:
        out["maintainer"] = str(child_maintainer.text or "")
    child_operating_system_name = el.find("OperatingSystemName")
    if child_operating_system_name is not None:
        out["operating_system_name"] = str(child_operating_system_name.text or "")
    child_operating_system_version = el.find("OperatingSystemVersion")
    if child_operating_system_version is not None:
        out["operating_system_version"] = str(child_operating_system_version.text or "")
    child_programming_languages = el.find("ProgrammingLanguages")
    if child_programming_languages is not None:
        import capo_elastic_beanstalk.types.platform_programming_languages

        out["programming_languages"] = (
            capo_elastic_beanstalk.types.platform_programming_languages.deserialize_query(
                child_programming_languages
            )
        )
    child_frameworks = el.find("Frameworks")
    if child_frameworks is not None:
        import capo_elastic_beanstalk.types.platform_frameworks

        out["frameworks"] = (
            capo_elastic_beanstalk.types.platform_frameworks.deserialize_query(
                child_frameworks
            )
        )
    child_custom_ami_list = el.find("CustomAmiList")
    if child_custom_ami_list is not None:
        import capo_elastic_beanstalk.types.custom_ami_list

        out["custom_ami_list"] = (
            capo_elastic_beanstalk.types.custom_ami_list.deserialize_query(
                child_custom_ami_list
            )
        )
    child_default_ami_list = el.find("DefaultAmiList")
    if child_default_ami_list is not None:
        import capo_elastic_beanstalk.types.default_ami_list

        out["default_ami_list"] = (
            capo_elastic_beanstalk.types.default_ami_list.deserialize_query(
                child_default_ami_list
            )
        )
    child_supported_tier_list = el.find("SupportedTierList")
    if child_supported_tier_list is not None:
        import capo_elastic_beanstalk.types.supported_tier_list

        out["supported_tier_list"] = (
            capo_elastic_beanstalk.types.supported_tier_list.deserialize_query(
                child_supported_tier_list
            )
        )
    child_supported_addon_list = el.find("SupportedAddonList")
    if child_supported_addon_list is not None:
        import capo_elastic_beanstalk.types.supported_addon_list

        out["supported_addon_list"] = (
            capo_elastic_beanstalk.types.supported_addon_list.deserialize_query(
                child_supported_addon_list
            )
        )
    child_platform_lifecycle_state = el.find("PlatformLifecycleState")
    if child_platform_lifecycle_state is not None:
        out["platform_lifecycle_state"] = str(child_platform_lifecycle_state.text or "")
    child_platform_branch_name = el.find("PlatformBranchName")
    if child_platform_branch_name is not None:
        out["platform_branch_name"] = str(child_platform_branch_name.text or "")
    child_platform_branch_lifecycle_state = el.find("PlatformBranchLifecycleState")
    if child_platform_branch_lifecycle_state is not None:
        out["platform_branch_lifecycle_state"] = str(
            child_platform_branch_lifecycle_state.text or ""
        )
    return out
