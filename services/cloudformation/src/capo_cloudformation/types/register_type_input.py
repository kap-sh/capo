"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegisterTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logging_config
    import capo_cloudformation.types.registry_type
    import capo_cloudformation.types.request_token
    import capo_cloudformation.types.role_arn2
    import capo_cloudformation.types.s3_url
    import capo_cloudformation.types.type_name


class RegisterTypeInput(TypedDict, closed=True):
    type: NotRequired["capo_cloudformation.types.registry_type.RegistryType"]
    """<p>The kind of extension.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension being registered.</p> <p>We suggest that extension names adhere to the following patterns:</p> <ul> <li> <p>For resource types, <code>company_or_organization::service::type</code>.</p> </li> <li> <p>For modules, <code>company_or_organization::service::type::MODULE</code>.</p> </li> <li> <p>For Hooks, <code>MyCompany::Testing::MyTestHook</code>.</p> </li> </ul> <note> <p>The following organization namespaces are reserved and can't be used in your extension names:</p> <ul> <li> <p> <code>Alexa</code> </p> </li> <li> <p> <code>AMZN</code> </p> </li> <li> <p> <code>Amazon</code> </p> </li> <li> <p> <code>AWS</code> </p> </li> <li> <p> <code>Custom</code> </p> </li> <li> <p> <code>Dev</code> </p> </li> </ul> </note>"""
    schema_handler_package: NotRequired["capo_cloudformation.types.s3_url.S3Url"]
    """<p>A URL to the S3 bucket that contains the extension project package that contains the necessary files for the extension you want to register.</p> <p>For information about generating a schema handler package for the extension you want to register, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html">submit</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p> <note> <p>The user registering the extension must be able to access the package in the S3 bucket. That's, the user needs to have <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html">GetObject</a> permissions for the schema handler package. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Identity and Access Management User Guide</i>.</p> </note>"""
    logging_config: NotRequired[
        "capo_cloudformation.types.logging_config.LoggingConfig"
    ]
    """<p>Specifies logging configuration information for an extension.</p>"""
    execution_role_arn: NotRequired["capo_cloudformation.types.role_arn2.RoleARN2"]
    """<p>The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the extension.</p> <p>For CloudFormation to assume the specified execution role, the role must contain a trust relationship with the CloudFormation service principal (<code>resources.cloudformation.amazonaws.com</code>). For more information about adding trust relationships, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy">Modifying a role trust policy</a> in the <i>Identity and Access Management User Guide</i>.</p> <p>If your extension calls Amazon Web Services APIs in any of its handlers, you must create an <i> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM execution role</a> </i> that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.</p>"""
    client_request_token: NotRequired[
        "capo_cloudformation.types.request_token.RequestToken"
    ]
    """<p>A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of an extension from the same registration request, even if the request is submitted multiple times.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterTypeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        import capo_cloudformation.types.registry_type

        capo_cloudformation.types.registry_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "schema_handler_package" in value:
        pairs.append(
            (f"{key_prefix}SchemaHandlerPackage", str(value["schema_handler_package"]))
        )
    if "logging_config" in value:
        import capo_cloudformation.types.logging_config

        capo_cloudformation.types.logging_config.serialize_query(
            value["logging_config"], pairs, f"{key_prefix}LoggingConfig"
        )
    if "execution_role_arn" in value:
        pairs.append(
            (f"{key_prefix}ExecutionRoleArn", str(value["execution_role_arn"]))
        )
    if "client_request_token" in value:
        pairs.append(
            (f"{key_prefix}ClientRequestToken", str(value["client_request_token"]))
        )


def deserialize_query(el: Element) -> RegisterTypeInput:
    out: RegisterTypeInput = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.registry_type

        out["type"] = capo_cloudformation.types.registry_type.deserialize_query(
            child_type
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_schema_handler_package = el.find("SchemaHandlerPackage")
    if child_schema_handler_package is not None:
        out["schema_handler_package"] = str(child_schema_handler_package.text or "")
    child_logging_config = el.find("LoggingConfig")
    if child_logging_config is not None:
        import capo_cloudformation.types.logging_config

        out["logging_config"] = (
            capo_cloudformation.types.logging_config.deserialize_query(
                child_logging_config
            )
        )
    child_execution_role_arn = el.find("ExecutionRoleArn")
    if child_execution_role_arn is not None:
        out["execution_role_arn"] = str(child_execution_role_arn.text or "")
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    return out
