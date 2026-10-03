"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.auto_update
    import capo_cloudformation.types.configuration_schema
    import capo_cloudformation.types.deprecated_status
    import capo_cloudformation.types.description
    import capo_cloudformation.types.is_activated
    import capo_cloudformation.types.is_default_version
    import capo_cloudformation.types.logging_config
    import capo_cloudformation.types.optional_secure_url
    import capo_cloudformation.types.provisioning_type
    import capo_cloudformation.types.public_version_number
    import capo_cloudformation.types.publisher_id
    import capo_cloudformation.types.registry_type
    import capo_cloudformation.types.required_activated_types
    import capo_cloudformation.types.role_arn2
    import capo_cloudformation.types.timestamp
    import capo_cloudformation.types.type_arn
    import capo_cloudformation.types.type_name
    import capo_cloudformation.types.type_schema
    import capo_cloudformation.types.type_tests_status
    import capo_cloudformation.types.type_tests_status_description
    import capo_cloudformation.types.type_version_id
    import capo_cloudformation.types.visibility


class DescribeTypeOutput(TypedDict, closed=True):
    arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The Amazon Resource Name (ARN) of the extension.</p>"""
    type: NotRequired["capo_cloudformation.types.registry_type.RegistryType"]
    """<p>The kind of extension.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension.</p> <p>If the extension is a public third-party type you have activated with a type name alias, CloudFormation returns the type name alias. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a>.</p>"""
    default_version_id: NotRequired[
        "capo_cloudformation.types.type_version_id.TypeVersionId"
    ]
    """<p>The ID of the default version of the extension. The default version is used when the extension version isn't specified.</p> <p>This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon Web Services and published by third parties, CloudFormation returns <code>null</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>To set the default version of an extension, use <a>SetTypeDefaultVersion</a>.</p>"""
    is_default_version: NotRequired[
        "capo_cloudformation.types.is_default_version.IsDefaultVersion"
    ]
    """<p>Whether the specified extension version is set as the default version.</p> <p>This applies only to private extensions you have registered in your account, and extensions published by Amazon Web Services. For public third-party extensions, whether they are activated in your account, CloudFormation returns <code>null</code>.</p>"""
    type_tests_status: NotRequired[
        "capo_cloudformation.types.type_tests_status.TypeTestsStatus"
    ]
    """<p>The contract test status of the registered extension version. To return the extension test status of a specific extension version, you must specify <code>VersionId</code>.</p> <p>This applies only to registered private extension versions. CloudFormation doesn't return this information for public extensions, whether they are activated in your account.</p> <ul> <li> <p> <code>PASSED</code>: The extension has passed all its contract tests.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p> </li> <li> <p> <code>FAILED</code>: The extension has failed one or more contract tests.</p> </li> <li> <p> <code>IN_PROGRESS</code>: Contract tests are currently being performed on the extension.</p> </li> <li> <p> <code>NOT_TESTED</code>: Contract tests haven't been performed on the extension.</p> </li> </ul>"""
    type_tests_status_description: NotRequired[
        "capo_cloudformation.types.type_tests_status_description.TypeTestsStatusDescription"
    ]
    """<p>The description of the test status. To return the extension test status of a specific extension version, you must specify <code>VersionId</code>.</p> <p>This applies only to registered private extension versions. CloudFormation doesn't return this information for public extensions, whether they are activated in your account.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>The description of the extension.</p>"""
    schema: NotRequired["capo_cloudformation.types.type_schema.TypeSchema"]
    """<p>The schema that defines the extension.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">Resource type schema</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i> and the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html">CloudFormation Hooks User Guide</a>.</p>"""
    provisioning_type: NotRequired[
        "capo_cloudformation.types.provisioning_type.ProvisioningType"
    ]
    """<p>For resource type extensions, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include all the following handlers, and therefore can't actually be provisioned.</p> <ul> <li> <p>create</p> </li> <li> <p>read</p> </li> <li> <p>delete</p> </li> </ul> </li> </ul>"""
    deprecated_status: NotRequired[
        "capo_cloudformation.types.deprecated_status.DeprecatedStatus"
    ]
    """<p>The deprecation status of the extension version.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is activated or registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deactivated or deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>For public third-party extensions, CloudFormation returns <code>null</code>.</p>"""
    logging_config: NotRequired[
        "capo_cloudformation.types.logging_config.LoggingConfig"
    ]
    """<p>Contains logging configuration information for private extensions. This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon Web Services and published by third parties, CloudFormation returns <code>null</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p>"""
    required_activated_types: NotRequired[
        "capo_cloudformation.types.required_activated_types.RequiredActivatedTypes"
    ]
    """<p>For extensions that are modules, the public third-party extensions that must be activated in your account in order for the module itself to be activated.</p>"""
    execution_role_arn: NotRequired["capo_cloudformation.types.role_arn2.RoleARN2"]
    """<p>The Amazon Resource Name (ARN) of the IAM execution role used to register the extension. This applies only to private extensions you have registered in your account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>If the registered extension calls any Amazon Web Services APIs, you must create an <i> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM execution role</a> </i> that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your extension with the appropriate credentials.</p>"""
    visibility: NotRequired["capo_cloudformation.types.visibility.Visibility"]
    """<p>The scope at which the extension is visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: The extension is only visible and usable within the account in which it is registered. CloudFormation marks any extensions you register as <code>PRIVATE</code>.</p> </li> <li> <p> <code>PUBLIC</code>: The extension is publicly visible and usable within any Amazon Web Services account.</p> </li> </ul>"""
    source_url: NotRequired[
        "capo_cloudformation.types.optional_secure_url.OptionalSecureUrl"
    ]
    """<p>The URL of the source code for the extension.</p>"""
    documentation_url: NotRequired[
        "capo_cloudformation.types.optional_secure_url.OptionalSecureUrl"
    ]
    """<p>The URL of a page providing detailed documentation for this extension.</p>"""
    last_updated: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>When the specified extension version was registered. This applies only to:</p> <ul> <li> <p>Private extensions you have registered in your account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> </li> <li> <p>Public extensions you have activated in your account with auto-update specified. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a>.</p> </li> </ul>"""
    time_created: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>When the specified private extension version was registered or activated in your account.</p>"""
    configuration_schema: NotRequired[
        "capo_cloudformation.types.configuration_schema.ConfigurationSchema"
    ]
    """<p>A JSON string that represent the current configuration data for the extension in this account and Region.</p> <p>To set the configuration data for an extension, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a>.</p>"""
    publisher_id: NotRequired["capo_cloudformation.types.publisher_id.PublisherId"]
    """<p>The publisher ID of the extension publisher.</p> <p>This applies only to public third-party extensions. For private registered extensions, and extensions provided by Amazon Web Services, CloudFormation returns <code>null</code>.</p>"""
    original_type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>For public extensions that have been activated for this account and Region, the type name of the public extension.</p> <p>If you specified a <code>TypeNameAlias</code> when enabling the extension in this account and Region, CloudFormation treats that alias as the extension's type name within the account and Region, not the type name of the public extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-alias">Use aliases to refer to extensions</a> in the <i>CloudFormation User Guide</i>.</p>"""
    original_type_arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>For public extensions that have been activated for this account and Region, the Amazon Resource Name (ARN) of the public extension.</p>"""
    public_version_number: NotRequired[
        "capo_cloudformation.types.public_version_number.PublicVersionNumber"
    ]
    """<p>The version number of a public third-party extension.</p> <p>This applies only if you specify a public extension you have activated in your account, or specify a public extension without specifying a version. For all other extensions, CloudFormation returns <code>null</code>.</p>"""
    latest_public_version: NotRequired[
        "capo_cloudformation.types.public_version_number.PublicVersionNumber"
    ]
    """<p>The latest version of a public extension <i>that is available</i> for use.</p> <p>This only applies if you specify a public extension, and you don't specify a version. For all other requests, CloudFormation returns <code>null</code>.</p>"""
    is_activated: NotRequired["capo_cloudformation.types.is_activated.IsActivated"]
    """<p>Whether the extension is activated in the account and Region.</p> <p>This only applies to public third-party extensions. For all other extensions, CloudFormation returns <code>null</code>.</p>"""
    auto_update: NotRequired["capo_cloudformation.types.auto_update.AutoUpdate"]
    """<p>Whether CloudFormation automatically updates the extension in this account and Region when a new <i>minor</i> version is published by the extension publisher. Major versions released by the publisher must be manually updated. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto">Automatically use new versions of extensions</a> in the <i>CloudFormation User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTypeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "type" in value:
        import capo_cloudformation.types.registry_type

        capo_cloudformation.types.registry_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "default_version_id" in value:
        pairs.append(
            (f"{key_prefix}DefaultVersionId", str(value["default_version_id"]))
        )
    if "is_default_version" in value:
        pairs.append(
            (
                f"{key_prefix}IsDefaultVersion",
                "true" if value["is_default_version"] else "false",
            )
        )
    if "type_tests_status" in value:
        import capo_cloudformation.types.type_tests_status

        capo_cloudformation.types.type_tests_status.serialize_query(
            value["type_tests_status"], pairs, f"{key_prefix}TypeTestsStatus"
        )
    if "type_tests_status_description" in value:
        pairs.append(
            (
                f"{key_prefix}TypeTestsStatusDescription",
                str(value["type_tests_status_description"]),
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "schema" in value:
        pairs.append((f"{key_prefix}Schema", str(value["schema"])))
    if "provisioning_type" in value:
        import capo_cloudformation.types.provisioning_type

        capo_cloudformation.types.provisioning_type.serialize_query(
            value["provisioning_type"], pairs, f"{key_prefix}ProvisioningType"
        )
    if "deprecated_status" in value:
        import capo_cloudformation.types.deprecated_status

        capo_cloudformation.types.deprecated_status.serialize_query(
            value["deprecated_status"], pairs, f"{key_prefix}DeprecatedStatus"
        )
    if "logging_config" in value:
        import capo_cloudformation.types.logging_config

        capo_cloudformation.types.logging_config.serialize_query(
            value["logging_config"], pairs, f"{key_prefix}LoggingConfig"
        )
    if "required_activated_types" in value:
        import capo_cloudformation.types.required_activated_types

        capo_cloudformation.types.required_activated_types.serialize_query(
            value["required_activated_types"],
            pairs,
            f"{key_prefix}RequiredActivatedTypes",
        )
    if "execution_role_arn" in value:
        pairs.append(
            (f"{key_prefix}ExecutionRoleArn", str(value["execution_role_arn"]))
        )
    if "visibility" in value:
        import capo_cloudformation.types.visibility

        capo_cloudformation.types.visibility.serialize_query(
            value["visibility"], pairs, f"{key_prefix}Visibility"
        )
    if "source_url" in value:
        pairs.append((f"{key_prefix}SourceUrl", str(value["source_url"])))
    if "documentation_url" in value:
        pairs.append((f"{key_prefix}DocumentationUrl", str(value["documentation_url"])))
    if "last_updated" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["last_updated"], pairs, f"{key_prefix}LastUpdated"
        )
    if "time_created" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["time_created"], pairs, f"{key_prefix}TimeCreated"
        )
    if "configuration_schema" in value:
        pairs.append(
            (f"{key_prefix}ConfigurationSchema", str(value["configuration_schema"]))
        )
    if "publisher_id" in value:
        pairs.append((f"{key_prefix}PublisherId", str(value["publisher_id"])))
    if "original_type_name" in value:
        pairs.append(
            (f"{key_prefix}OriginalTypeName", str(value["original_type_name"]))
        )
    if "original_type_arn" in value:
        pairs.append((f"{key_prefix}OriginalTypeArn", str(value["original_type_arn"])))
    if "public_version_number" in value:
        pairs.append(
            (f"{key_prefix}PublicVersionNumber", str(value["public_version_number"]))
        )
    if "latest_public_version" in value:
        pairs.append(
            (f"{key_prefix}LatestPublicVersion", str(value["latest_public_version"]))
        )
    if "is_activated" in value:
        pairs.append(
            (f"{key_prefix}IsActivated", "true" if value["is_activated"] else "false")
        )
    if "auto_update" in value:
        pairs.append(
            (f"{key_prefix}AutoUpdate", "true" if value["auto_update"] else "false")
        )


def deserialize_query(el: Element) -> DescribeTypeOutput:
    out: DescribeTypeOutput = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.registry_type

        out["type"] = capo_cloudformation.types.registry_type.deserialize_query(
            child_type
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_default_version_id = el.find("DefaultVersionId")
    if child_default_version_id is not None:
        out["default_version_id"] = str(child_default_version_id.text or "")
    child_is_default_version = el.find("IsDefaultVersion")
    if child_is_default_version is not None:
        out["is_default_version"] = (
            child_is_default_version.text or ""
        ).lower() == "true"
    child_type_tests_status = el.find("TypeTestsStatus")
    if child_type_tests_status is not None:
        import capo_cloudformation.types.type_tests_status

        out["type_tests_status"] = (
            capo_cloudformation.types.type_tests_status.deserialize_query(
                child_type_tests_status
            )
        )
    child_type_tests_status_description = el.find("TypeTestsStatusDescription")
    if child_type_tests_status_description is not None:
        out["type_tests_status_description"] = str(
            child_type_tests_status_description.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_schema = el.find("Schema")
    if child_schema is not None:
        out["schema"] = str(child_schema.text or "")
    child_provisioning_type = el.find("ProvisioningType")
    if child_provisioning_type is not None:
        import capo_cloudformation.types.provisioning_type

        out["provisioning_type"] = (
            capo_cloudformation.types.provisioning_type.deserialize_query(
                child_provisioning_type
            )
        )
    child_deprecated_status = el.find("DeprecatedStatus")
    if child_deprecated_status is not None:
        import capo_cloudformation.types.deprecated_status

        out["deprecated_status"] = (
            capo_cloudformation.types.deprecated_status.deserialize_query(
                child_deprecated_status
            )
        )
    child_logging_config = el.find("LoggingConfig")
    if child_logging_config is not None:
        import capo_cloudformation.types.logging_config

        out["logging_config"] = (
            capo_cloudformation.types.logging_config.deserialize_query(
                child_logging_config
            )
        )
    child_required_activated_types = el.find("RequiredActivatedTypes")
    if child_required_activated_types is not None:
        import capo_cloudformation.types.required_activated_types

        out["required_activated_types"] = (
            capo_cloudformation.types.required_activated_types.deserialize_query(
                child_required_activated_types
            )
        )
    child_execution_role_arn = el.find("ExecutionRoleArn")
    if child_execution_role_arn is not None:
        out["execution_role_arn"] = str(child_execution_role_arn.text or "")
    child_visibility = el.find("Visibility")
    if child_visibility is not None:
        import capo_cloudformation.types.visibility

        out["visibility"] = capo_cloudformation.types.visibility.deserialize_query(
            child_visibility
        )
    child_source_url = el.find("SourceUrl")
    if child_source_url is not None:
        out["source_url"] = str(child_source_url.text or "")
    child_documentation_url = el.find("DocumentationUrl")
    if child_documentation_url is not None:
        out["documentation_url"] = str(child_documentation_url.text or "")
    child_last_updated = el.find("LastUpdated")
    if child_last_updated is not None:
        import capo_cloudformation.types.timestamp

        out["last_updated"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_last_updated
        )
    child_time_created = el.find("TimeCreated")
    if child_time_created is not None:
        import capo_cloudformation.types.timestamp

        out["time_created"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_time_created
        )
    child_configuration_schema = el.find("ConfigurationSchema")
    if child_configuration_schema is not None:
        out["configuration_schema"] = str(child_configuration_schema.text or "")
    child_publisher_id = el.find("PublisherId")
    if child_publisher_id is not None:
        out["publisher_id"] = str(child_publisher_id.text or "")
    child_original_type_name = el.find("OriginalTypeName")
    if child_original_type_name is not None:
        out["original_type_name"] = str(child_original_type_name.text or "")
    child_original_type_arn = el.find("OriginalTypeArn")
    if child_original_type_arn is not None:
        out["original_type_arn"] = str(child_original_type_arn.text or "")
    child_public_version_number = el.find("PublicVersionNumber")
    if child_public_version_number is not None:
        out["public_version_number"] = str(child_public_version_number.text or "")
    child_latest_public_version = el.find("LatestPublicVersion")
    if child_latest_public_version is not None:
        out["latest_public_version"] = str(child_latest_public_version.text or "")
    child_is_activated = el.find("IsActivated")
    if child_is_activated is not None:
        out["is_activated"] = (child_is_activated.text or "").lower() == "true"
    child_auto_update = el.find("AutoUpdate")
    if child_auto_update is not None:
        out["auto_update"] = (child_auto_update.text or "").lower() == "true"
    return out
