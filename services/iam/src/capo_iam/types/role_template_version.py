"""Generated from Smithy shape ``com.amazonaws.iam#RoleTemplateVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.boolean_type
    import capo_iam.types.date_type
    import capo_iam.types.id_type
    import capo_iam.types.inline_policy_template_list_type
    import capo_iam.types.integer_type
    import capo_iam.types.managed_by_type_type
    import capo_iam.types.managed_by_value_type
    import capo_iam.types.managed_policy_arn_list_type
    import capo_iam.types.minor_version_type
    import capo_iam.types.parameters_definition_list_type
    import capo_iam.types.policy_document_type
    import capo_iam.types.role_description_pattern_type
    import capo_iam.types.role_max_session_duration_type
    import capo_iam.types.role_name_pattern_type
    import capo_iam.types.role_path_pattern_type
    import capo_iam.types.role_template_description_type
    import capo_iam.types.role_template_name_type
    import capo_iam.types.tag_template_list_type


class RoleTemplateVersion(TypedDict, closed=True):
    template_arn: NotRequired["capo_iam.types.arn_type.arnType"]
    """<p>The Amazon Resource Name (ARN) that identifies the role template.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    template_name: NotRequired[
        "capo_iam.types.role_template_name_type.roleTemplateNameType"
    ]
    """<p>The friendly name that identifies the role template.</p>"""
    template_version_id: NotRequired["capo_iam.types.id_type.idType"]
    """<p>The identifier of the role template version.</p>"""
    description: NotRequired[
        "capo_iam.types.role_template_description_type.roleTemplateDescriptionType"
    ]
    """<p>The description of the role template.</p>"""
    major_version: NotRequired["capo_iam.types.integer_type.integerType"]
    """<p>The major version number of the role template.</p>"""
    default_minor_version: NotRequired[
        "capo_iam.types.minor_version_type.minorVersionType"
    ]
    """<p>The minor version that the service uses by default when you create a role from this template without specifying a minor version.</p>"""
    managed_by_type: NotRequired[
        "capo_iam.types.managed_by_type_type.managedByTypeType"
    ]
    """<p>Indicates that the role template is managed by an Amazon Web Services service.</p>"""
    managed_by_value: NotRequired[
        "capo_iam.types.managed_by_value_type.managedByValueType"
    ]
    """<p>The identifier of the Amazon Web Services service that manages the role template.</p>"""
    enabled: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether the role template is enabled. When a template is disabled, you cannot create roles from it.</p>"""
    minor_version: NotRequired["capo_iam.types.minor_version_type.minorVersionType"]
    """<p>The minor version number of this role template version.</p>"""
    role_name_pattern: NotRequired[
        "capo_iam.types.role_name_pattern_type.roleNamePatternType"
    ]
    """<p>The pattern that is used to generate the name of a role that is created from this template. The pattern can include <code>@{parameter}</code> placeholders that are replaced with the values you supply in the <code>ReplacementValues</code> parameter of <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcquireRole.html">AcquireRole</a>.</p>"""
    role_path_pattern: NotRequired[
        "capo_iam.types.role_path_pattern_type.rolePathPatternType"
    ]
    """<p>The pattern that is used to generate the path of a role that is created from this template.</p>"""
    role_description_pattern: NotRequired[
        "capo_iam.types.role_description_pattern_type.roleDescriptionPatternType"
    ]
    """<p>The pattern that is used to generate the description of a role that is created from this template.</p>"""
    assume_role_policy_document_template: NotRequired[
        "capo_iam.types.policy_document_type.policyDocumentType"
    ]
    """<p>The trust policy template that grants an entity permission to assume roles that you create from this template.</p>"""
    inline_policy_templates: NotRequired[
        "capo_iam.types.inline_policy_template_list_type.inlinePolicyTemplateListType"
    ]
    """<p>A list of inline policy templates that the service embeds in roles that you create from this template.</p>"""
    managed_policy_arns: NotRequired[
        "capo_iam.types.managed_policy_arn_list_type.managedPolicyArnListType"
    ]
    """<p>A list of the ARNs of the managed policies that the service attaches to roles that you create from this template.</p>"""
    permission_boundary_arn: NotRequired["capo_iam.types.arn_type.arnType"]
    """<p>The ARN of the policy that sets the permissions boundary for roles that you create from this template.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    parameters_definition: NotRequired[
        "capo_iam.types.parameters_definition_list_type.parametersDefinitionListType"
    ]
    """<p>A list of the parameters that are defined for this role template version. You supply values for these parameters when you create a role with <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcquireRole.html">AcquireRole</a>.</p>"""
    role_tags_template: NotRequired[
        "capo_iam.types.tag_template_list_type.tagTemplateListType"
    ]
    """<p>A list of tag templates that are applied to roles that are created from this template.</p>"""
    max_session_duration: NotRequired[
        "capo_iam.types.role_max_session_duration_type.roleMaxSessionDurationType"
    ]
    """<p>The maximum session duration (in seconds) for roles that are created from this template.</p>"""
    version_enabled: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether this specific minor version of the role template is enabled.</p>"""
    create_timestamp: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the role template version was created.</p>"""
    update_timestamp: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the role template version was last updated.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RoleTemplateVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "template_arn" in value:
        pairs.append((f"{key_prefix}TemplateArn", str(value["template_arn"])))
    if "template_name" in value:
        pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    if "template_version_id" in value:
        pairs.append(
            (f"{key_prefix}TemplateVersionId", str(value["template_version_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "major_version" in value:
        pairs.append((f"{key_prefix}MajorVersion", str(value["major_version"])))
    if "default_minor_version" in value:
        pairs.append(
            (f"{key_prefix}DefaultMinorVersion", str(value["default_minor_version"]))
        )
    if "managed_by_type" in value:
        import capo_iam.types.managed_by_type_type

        capo_iam.types.managed_by_type_type.serialize_query(
            value["managed_by_type"], pairs, f"{key_prefix}ManagedByType"
        )
    if "managed_by_value" in value:
        pairs.append((f"{key_prefix}ManagedByValue", str(value["managed_by_value"])))
    pairs.append(
        (f"{key_prefix}Enabled", "true" if value.get("enabled", False) else "false")
    )
    if "minor_version" in value:
        pairs.append((f"{key_prefix}MinorVersion", str(value["minor_version"])))
    if "role_name_pattern" in value:
        pairs.append((f"{key_prefix}RoleNamePattern", str(value["role_name_pattern"])))
    if "role_path_pattern" in value:
        pairs.append((f"{key_prefix}RolePathPattern", str(value["role_path_pattern"])))
    if "role_description_pattern" in value:
        pairs.append(
            (
                f"{key_prefix}RoleDescriptionPattern",
                str(value["role_description_pattern"]),
            )
        )
    if "assume_role_policy_document_template" in value:
        pairs.append(
            (
                f"{key_prefix}AssumeRolePolicyDocumentTemplate",
                str(value["assume_role_policy_document_template"]),
            )
        )
    if "inline_policy_templates" in value:
        import capo_iam.types.inline_policy_template_list_type

        capo_iam.types.inline_policy_template_list_type.serialize_query(
            value["inline_policy_templates"],
            pairs,
            f"{key_prefix}InlinePolicyTemplates",
        )
    if "managed_policy_arns" in value:
        import capo_iam.types.managed_policy_arn_list_type

        capo_iam.types.managed_policy_arn_list_type.serialize_query(
            value["managed_policy_arns"], pairs, f"{key_prefix}ManagedPolicyArns"
        )
    if "permission_boundary_arn" in value:
        pairs.append(
            (
                f"{key_prefix}PermissionBoundaryArn",
                str(value["permission_boundary_arn"]),
            )
        )
    if "parameters_definition" in value:
        import capo_iam.types.parameters_definition_list_type

        capo_iam.types.parameters_definition_list_type.serialize_query(
            value["parameters_definition"], pairs, f"{key_prefix}ParametersDefinition"
        )
    if "role_tags_template" in value:
        import capo_iam.types.tag_template_list_type

        capo_iam.types.tag_template_list_type.serialize_query(
            value["role_tags_template"], pairs, f"{key_prefix}RoleTagsTemplate"
        )
    if "max_session_duration" in value:
        pairs.append(
            (f"{key_prefix}MaxSessionDuration", str(value["max_session_duration"]))
        )
    pairs.append(
        (
            f"{key_prefix}VersionEnabled",
            "true" if value.get("version_enabled", False) else "false",
        )
    )
    if "create_timestamp" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["create_timestamp"], pairs, f"{key_prefix}CreateTimestamp"
        )
    if "update_timestamp" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["update_timestamp"], pairs, f"{key_prefix}UpdateTimestamp"
        )


def deserialize_query(el: Element) -> RoleTemplateVersion:
    out: RoleTemplateVersion = {}  # type: ignore[typeddict-item]
    child_template_arn = el.find("TemplateArn")
    if child_template_arn is not None:
        out["template_arn"] = str(child_template_arn.text or "")
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_template_version_id = el.find("TemplateVersionId")
    if child_template_version_id is not None:
        out["template_version_id"] = str(child_template_version_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_major_version = el.find("MajorVersion")
    if child_major_version is not None:
        out["major_version"] = int(child_major_version.text or "")
    child_default_minor_version = el.find("DefaultMinorVersion")
    if child_default_minor_version is not None:
        out["default_minor_version"] = int(child_default_minor_version.text or "")
    child_managed_by_type = el.find("ManagedByType")
    if child_managed_by_type is not None:
        import capo_iam.types.managed_by_type_type

        out["managed_by_type"] = capo_iam.types.managed_by_type_type.deserialize_query(
            child_managed_by_type
        )
    child_managed_by_value = el.find("ManagedByValue")
    if child_managed_by_value is not None:
        out["managed_by_value"] = str(child_managed_by_value.text or "")
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_minor_version = el.find("MinorVersion")
    if child_minor_version is not None:
        out["minor_version"] = int(child_minor_version.text or "")
    child_role_name_pattern = el.find("RoleNamePattern")
    if child_role_name_pattern is not None:
        out["role_name_pattern"] = str(child_role_name_pattern.text or "")
    child_role_path_pattern = el.find("RolePathPattern")
    if child_role_path_pattern is not None:
        out["role_path_pattern"] = str(child_role_path_pattern.text or "")
    child_role_description_pattern = el.find("RoleDescriptionPattern")
    if child_role_description_pattern is not None:
        out["role_description_pattern"] = str(child_role_description_pattern.text or "")
    child_assume_role_policy_document_template = el.find(
        "AssumeRolePolicyDocumentTemplate"
    )
    if child_assume_role_policy_document_template is not None:
        out["assume_role_policy_document_template"] = str(
            child_assume_role_policy_document_template.text or ""
        )
    child_inline_policy_templates = el.find("InlinePolicyTemplates")
    if child_inline_policy_templates is not None:
        import capo_iam.types.inline_policy_template_list_type

        out["inline_policy_templates"] = (
            capo_iam.types.inline_policy_template_list_type.deserialize_query(
                child_inline_policy_templates
            )
        )
    child_managed_policy_arns = el.find("ManagedPolicyArns")
    if child_managed_policy_arns is not None:
        import capo_iam.types.managed_policy_arn_list_type

        out["managed_policy_arns"] = (
            capo_iam.types.managed_policy_arn_list_type.deserialize_query(
                child_managed_policy_arns
            )
        )
    child_permission_boundary_arn = el.find("PermissionBoundaryArn")
    if child_permission_boundary_arn is not None:
        out["permission_boundary_arn"] = str(child_permission_boundary_arn.text or "")
    child_parameters_definition = el.find("ParametersDefinition")
    if child_parameters_definition is not None:
        import capo_iam.types.parameters_definition_list_type

        out["parameters_definition"] = (
            capo_iam.types.parameters_definition_list_type.deserialize_query(
                child_parameters_definition
            )
        )
    child_role_tags_template = el.find("RoleTagsTemplate")
    if child_role_tags_template is not None:
        import capo_iam.types.tag_template_list_type

        out["role_tags_template"] = (
            capo_iam.types.tag_template_list_type.deserialize_query(
                child_role_tags_template
            )
        )
    child_max_session_duration = el.find("MaxSessionDuration")
    if child_max_session_duration is not None:
        out["max_session_duration"] = int(child_max_session_duration.text or "")
    child_version_enabled = el.find("VersionEnabled")
    if child_version_enabled is not None:
        out["version_enabled"] = (child_version_enabled.text or "").lower() == "true"
    else:
        out["version_enabled"] = False
    child_create_timestamp = el.find("CreateTimestamp")
    if child_create_timestamp is not None:
        import capo_iam.types.date_type

        out["create_timestamp"] = capo_iam.types.date_type.deserialize_query(
            child_create_timestamp
        )
    child_update_timestamp = el.find("UpdateTimestamp")
    if child_update_timestamp is not None:
        import capo_iam.types.date_type

        out["update_timestamp"] = capo_iam.types.date_type.deserialize_query(
            child_update_timestamp
        )
    return out
