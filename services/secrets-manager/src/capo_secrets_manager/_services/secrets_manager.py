"""Generated from Smithy shape ``com.amazonaws.secretsmanager#secretsmanager``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_secrets_manager._auth._signers
import capo_secrets_manager._auth._sigv4
from capo_secrets_manager._auth._identity import Credentials
from capo_secrets_manager._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_secrets_manager._auth._zapros_handler import AuthMiddleware
from capo_secrets_manager._pagination import resolve_path as _resolve_path
from capo_secrets_manager._services._aws_config import aws_config
from capo_secrets_manager._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_secrets_manager.types.add_replica_region_list_type
    import capo_secrets_manager.types.batch_get_secret_value_request
    import capo_secrets_manager.types.batch_get_secret_value_response
    import capo_secrets_manager.types.boolean_type
    import capo_secrets_manager.types.cancel_rotate_secret_request
    import capo_secrets_manager.types.cancel_rotate_secret_response
    import capo_secrets_manager.types.client_request_token_type
    import capo_secrets_manager.types.create_secret_request
    import capo_secrets_manager.types.create_secret_response
    import capo_secrets_manager.types.delete_resource_policy_request
    import capo_secrets_manager.types.delete_resource_policy_response
    import capo_secrets_manager.types.delete_secret_request
    import capo_secrets_manager.types.delete_secret_response
    import capo_secrets_manager.types.describe_secret_request
    import capo_secrets_manager.types.describe_secret_response
    import capo_secrets_manager.types.description_type
    import capo_secrets_manager.types.exclude_characters_type
    import capo_secrets_manager.types.exclude_lowercase_type
    import capo_secrets_manager.types.exclude_numbers_type
    import capo_secrets_manager.types.exclude_punctuation_type
    import capo_secrets_manager.types.exclude_uppercase_type
    import capo_secrets_manager.types.external_secret_rotation_metadata_type
    import capo_secrets_manager.types.filters_list_type
    import capo_secrets_manager.types.get_random_password_request
    import capo_secrets_manager.types.get_random_password_response
    import capo_secrets_manager.types.get_resource_policy_request
    import capo_secrets_manager.types.get_resource_policy_response
    import capo_secrets_manager.types.get_secret_value_request
    import capo_secrets_manager.types.get_secret_value_response
    import capo_secrets_manager.types.include_space_type
    import capo_secrets_manager.types.kms_key_id_type
    import capo_secrets_manager.types.list_secret_version_ids_request
    import capo_secrets_manager.types.list_secret_version_ids_response
    import capo_secrets_manager.types.list_secrets_request
    import capo_secrets_manager.types.list_secrets_response
    import capo_secrets_manager.types.max_results_batch_type
    import capo_secrets_manager.types.max_results_type
    import capo_secrets_manager.types.medea_type_type
    import capo_secrets_manager.types.name_type
    import capo_secrets_manager.types.next_token_type
    import capo_secrets_manager.types.non_empty_resource_policy_type
    import capo_secrets_manager.types.password_length_type
    import capo_secrets_manager.types.put_resource_policy_request
    import capo_secrets_manager.types.put_resource_policy_response
    import capo_secrets_manager.types.put_secret_value_request
    import capo_secrets_manager.types.put_secret_value_response
    import capo_secrets_manager.types.recovery_window_in_days_type
    import capo_secrets_manager.types.remove_regions_from_replication_request
    import capo_secrets_manager.types.remove_regions_from_replication_response
    import capo_secrets_manager.types.remove_replica_region_list_type
    import capo_secrets_manager.types.replicate_secret_to_regions_request
    import capo_secrets_manager.types.replicate_secret_to_regions_response
    import capo_secrets_manager.types.require_each_included_type_type
    import capo_secrets_manager.types.restore_secret_request
    import capo_secrets_manager.types.restore_secret_response
    import capo_secrets_manager.types.role_arn_type
    import capo_secrets_manager.types.rotate_secret_request
    import capo_secrets_manager.types.rotate_secret_response
    import capo_secrets_manager.types.rotation_lambda_arn_type
    import capo_secrets_manager.types.rotation_rules_type
    import capo_secrets_manager.types.rotation_token_type
    import capo_secrets_manager.types.secret_binary_type
    import capo_secrets_manager.types.secret_id_list_type
    import capo_secrets_manager.types.secret_id_type
    import capo_secrets_manager.types.secret_string_type
    import capo_secrets_manager.types.secret_version_id_type
    import capo_secrets_manager.types.secret_version_stage_type
    import capo_secrets_manager.types.secret_version_stages_type
    import capo_secrets_manager.types.sort_by_type
    import capo_secrets_manager.types.sort_order_type
    import capo_secrets_manager.types.stop_replication_to_replica_request
    import capo_secrets_manager.types.stop_replication_to_replica_response
    import capo_secrets_manager.types.tag_key_list_type
    import capo_secrets_manager.types.tag_list_type
    import capo_secrets_manager.types.tag_resource_request
    import capo_secrets_manager.types.untag_resource_request
    import capo_secrets_manager.types.update_secret_request
    import capo_secrets_manager.types.update_secret_response
    import capo_secrets_manager.types.update_secret_version_stage_request
    import capo_secrets_manager.types.update_secret_version_stage_response
    import capo_secrets_manager.types.validate_resource_policy_request
    import capo_secrets_manager.types.validate_resource_policy_response


class SecretsManagerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SecretsManagerClient:
    """A client for the ``SecretsManager`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = SecretsManagerClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[SecretsManagerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SecretsManagerClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def batch_get_secret_value(
        self,
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        secret_id_list: Optional[
            "capo_secrets_manager.types.secret_id_list_type.SecretIdListType"
        ] = None,
        filters: Optional[
            "capo_secrets_manager.types.filters_list_type.FiltersListType"
        ] = None,
        max_results: Optional[
            "capo_secrets_manager.types.max_results_batch_type.MaxResultsBatchType"
        ] = None,
        next_token: Optional[
            "capo_secrets_manager.types.next_token_type.NextTokenType"
        ] = None,
    ) -> "capo_secrets_manager.types.batch_get_secret_value_response.BatchGetSecretValueResponse":
        """<p>Retrieves the contents of the encrypted fields <code>SecretString</code> or <code>SecretBinary</code> for up to 20 secrets. To retrieve a single secret, call <a>GetSecretValue</a>. </p> <p>To choose which secrets to retrieve, you can specify a list of secrets by name or ARN, or you can use filters. If Secrets Manager encounters errors such as <code>AccessDeniedException</code> while attempting to retrieve any of the secrets, you can see the errors in <code>Errors</code> in the response.</p> <p>Secrets Manager generates CloudTrail <code>GetSecretValue</code> log entries for each secret you request when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:BatchGetSecretValue</code>, and you must have <code>secretsmanager:GetSecretValue</code> for each secret. If you use filters, you must also have <code>secretsmanager:ListSecrets</code>. If the secrets are encrypted using customer-managed keys instead of the Amazon Web Services managed key <code>aws/secretsmanager</code>, then you also need <code>kms:Decrypt</code> permissions for the keys. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id_list: <p>The ARN or names of the secrets to retrieve. You must include <code>Filters</code> or <code>SecretIdList</code>, but not both.</p>
            filters: <p>The filters to choose which secrets to retrieve. You must include <code>Filters</code> or <code>SecretIdList</code>, but not both.</p>
            max_results: <p>The number of results to include in the response.</p> <p>If there are more results available, in the response, Secrets Manager includes <code>NextToken</code>. To get the next results, call <code>BatchGetSecretValue</code> again with the value from <code>NextToken</code>. To use this parameter, you must also use the <code>Filters</code> parameter.</p>
            next_token: <p>A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call <code>BatchGetSecretValue</code> again with this value.</p>

        Raises:
            capo_secrets_manager.errors.decryption_failure.DecryptionFailure: <p>Secrets Manager can't decrypt the protected secret text using the provided KMS key. </p>
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is invalid.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve the secret values for a group of secrets listed by name
            The following example gets the values for three secrets.

            >>> client.batch_get_secret_value(secret_id_list=['MySecret1', 'MySecret2', 'MySecret3'])
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.batch_get_secret_value_request.BatchGetSecretValueRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.batch_get_secret_value_response.BatchGetSecretValueResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.batch_get_secret_value

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.batch_get_secret_value.batch_get_secret_value(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.batch_get_secret_value_request.BatchGetSecretValueRequest = {}
        if secret_id_list is not None:
            input_["secret_id_list"] = secret_id_list
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_batch_get_secret_value(
        self,
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        secret_id_list: Optional[
            "capo_secrets_manager.types.secret_id_list_type.SecretIdListType"
        ] = None,
        filters: Optional[
            "capo_secrets_manager.types.filters_list_type.FiltersListType"
        ] = None,
        max_results: Optional[
            "capo_secrets_manager.types.max_results_batch_type.MaxResultsBatchType"
        ] = None,
        next_token: Optional[
            "capo_secrets_manager.types.next_token_type.NextTokenType"
        ] = None,
    ) -> "Iterator[capo_secrets_manager.types.batch_get_secret_value_response.BatchGetSecretValueResponse]":
        _token = next_token
        while True:
            _response = self.batch_get_secret_value(
                config_overrides=config_overrides,
                secret_id_list=secret_id_list,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def cancel_rotate_secret(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
    ) -> "capo_secrets_manager.types.cancel_rotate_secret_response.CancelRotateSecretResponse":
        """<p>Turns off automatic rotation, and if a rotation is currently in progress, cancels the rotation.</p> <p>If you cancel a rotation in progress, it can leave the <code>VersionStage</code> labels in an unexpected state. You might need to remove the staging label <code>AWSPENDING</code> from the partially created version. You also need to determine whether to roll back to the previous version of the secret by moving the staging label <code>AWSCURRENT</code> to the version that has <code>AWSPENDING</code>. To determine which version has a specific staging label, call <a>ListSecretVersionIds</a>. Then use <a>UpdateSecretVersionStage</a> to change staging labels. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html">How rotation works</a>.</p> <p>To turn on automatic rotation again, call <a>RotateSecret</a>.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:CancelRotateSecret</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To cancel scheduled rotation for a secret
            The following example shows how to cancel rotation for a secret. The operation sets the RotationEnabled field to false and cancels all scheduled rotations. To resume scheduled rotations, you must re-enable rotation by calling the rotate-secret operation.

            >>> client.cancel_rotate_secret(secret_id='MyTestDatabaseSecret')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.cancel_rotate_secret_request.CancelRotateSecretRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.cancel_rotate_secret_response.CancelRotateSecretResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.cancel_rotate_secret

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.cancel_rotate_secret.cancel_rotate_secret(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.cancel_rotate_secret_request.CancelRotateSecretRequest = {
            "secret_id": secret_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_secret(
        self,
        name: "capo_secrets_manager.types.name_type.NameType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        client_request_token: Optional[
            "capo_secrets_manager.types.client_request_token_type.ClientRequestTokenType"
        ] = None,
        description: Optional[
            "capo_secrets_manager.types.description_type.DescriptionType"
        ] = None,
        kms_key_id: Optional[
            "capo_secrets_manager.types.kms_key_id_type.KmsKeyIdType"
        ] = None,
        secret_binary: Optional[
            "capo_secrets_manager.types.secret_binary_type.SecretBinaryType"
        ] = None,
        secret_string: Optional[
            "capo_secrets_manager.types.secret_string_type.SecretStringType"
        ] = None,
        tags: Optional["capo_secrets_manager.types.tag_list_type.TagListType"] = None,
        add_replica_regions: Optional[
            "capo_secrets_manager.types.add_replica_region_list_type.AddReplicaRegionListType"
        ] = None,
        force_overwrite_replica_secret: Optional[
            "capo_secrets_manager.types.boolean_type.BooleanType"
        ] = None,
        type: Optional[
            "capo_secrets_manager.types.medea_type_type.MedeaTypeType"
        ] = None,
    ) -> "capo_secrets_manager.types.create_secret_response.CreateSecretResponse":
        """<p>Creates a new secret. A <i>secret</i> can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager. The secret also includes the connection information to access a database or other service, which Secrets Manager doesn't encrypt. A secret in Secrets Manager consists of both the protected secret data and the important information needed to manage the secret.</p> <p>For secrets that use <i>managed rotation</i>, you need to create the secret through the managing service. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets Manager secrets managed by other Amazon Web Services services</a>. </p> <p>For information about creating a secret in the console, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html">Create a secret</a>.</p> <p>To create a secret, you can provide the secret value to be encrypted in either the <code>SecretString</code> parameter or the <code>SecretBinary</code> parameter, but not both. If you include <code>SecretString</code> or <code>SecretBinary</code> then Secrets Manager creates an initial secret version and automatically attaches the staging label <code>AWSCURRENT</code> to it.</p> <p>For database credentials you want to rotate, for Secrets Manager to be able to rotate the secret, you must make sure the JSON you store in the <code>SecretString</code> matches the <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_secret_json_structure.html">JSON structure of a database secret</a>.</p> <p>If you don't specify an KMS encryption key, Secrets Manager uses the Amazon Web Services managed key <code>aws/secretsmanager</code>. If this key doesn't already exist in your account, then Secrets Manager creates it for you automatically. All users and roles in the Amazon Web Services account automatically have access to use <code>aws/secretsmanager</code>. Creating <code>aws/secretsmanager</code> can result in a one-time significant delay in returning the result.</p> <p>If the secret is in a different Amazon Web Services account from the credentials calling the API, then you can't use <code>aws/secretsmanager</code> to encrypt the secret, and you must create and use a customer managed KMS key. </p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters except <code>SecretBinary</code> or <code>SecretString</code> because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:CreateSecret</code>. If you include tags in the secret, you also need <code>secretsmanager:TagResource</code>. To add replica Regions, you must also have <code>secretsmanager:ReplicateSecretToRegions</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p> <p>To encrypt the secret with a KMS key other than <code>aws/secretsmanager</code>, you need <code>kms:GenerateDataKey</code> and <code>kms:Decrypt</code> permission to the key. </p> <important> <p>When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. This is a concern if the command includes the value of a secret. Learn how to <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/security_cli-exposure-risks.html">Mitigate the risks of using command-line tools to store Secrets Manager secrets</a>.</p> </important>

        Args:
            name: <p>The name of the new secret.</p> <p>The secret name can contain ASCII letters, numbers, and the following characters: /_+=.@-</p> <p>Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.</p>
            client_request_token: <p>If you include <code>SecretString</code> or <code>SecretBinary</code>, then Secrets Manager creates an initial version for the secret, and this parameter specifies the unique identifier for the new version. </p> <note> <p>If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request. </p> </note> <p>If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a <code>ClientRequestToken</code> and include it in the request.</p> <p>This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type</a> value to ensure uniqueness of your versions within the specified secret. </p> <ul> <li> <p>If the <code>ClientRequestToken</code> value isn't already associated with a version of the secret then a new version of the secret is created. </p> </li> <li> <p>If a version with this value already exists and the version <code>SecretString</code> and <code>SecretBinary</code> values are the same as those in the request, then the request is ignored.</p> </li> <li> <p>If a version with this value already exists and that version's <code>SecretString</code> and <code>SecretBinary</code> values are different from those in the request, then the request fails because you cannot modify an existing version. Instead, use <a>PutSecretValue</a> to create a new version.</p> </li> </ul> <p>This value becomes the <code>VersionId</code> of the new version.</p>
            description: <p>The description of the secret.</p>
            kms_key_id: <p>The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by <code>alias/</code>, for example <code>alias/aws/secretsmanager</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html">About aliases</a>.</p> <p>To use a KMS key in a different account, use the key ARN or the alias ARN.</p> <p>If you don't specify this value, then Secrets Manager uses the key <code>aws/secretsmanager</code>. If that key doesn't yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value.</p> <p>If the secret is in a different Amazon Web Services account from the credentials calling the API, then you can't use <code>aws/secretsmanager</code> to encrypt the secret, and you must create and use a customer managed KMS key. </p>
            secret_binary: <p>The binary data to encrypt and store in the new version of the secret. We recommend that you store your binary data in a file and then pass the contents of the file as a parameter.</p> <p>Either <code>SecretString</code> or <code>SecretBinary</code> must have a value, but not both.</p> <p>This parameter is not available in the Secrets Manager console.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>
            secret_string: <p>The text data to encrypt and store in this new version of the secret. We recommend you use a JSON structure of key/value pairs for your secret value.</p> <p>Either <code>SecretString</code> or <code>SecretBinary</code> must have a value, but not both.</p> <p>If you create a secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the <code>SecretString</code> parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that a Lambda rotation function can parse.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>
            tags: <p>A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string, for example:</p> <p> <code>[{"Key":"CostCenter","Value":"12345"},{"Key":"environment","Value":"production"}]</code> </p> <p>Secrets Manager tag key names are case sensitive. A tag with the key "ABC" is a different tag from one with key "abc".</p> <p>If you check tags in permissions policies as part of your security strategy, then adding or removing a tag can change permissions. If the completion of this operation would result in you losing your permissions for this secret, then Secrets Manager blocks the operation and returns an <code>Access Denied</code> error. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#tag-secrets-abac">Control access to secrets using tags</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_tags2">Limit access to identities with tags that match secrets' tags</a>.</p> <p>For information about how to format a JSON parameter for the various command line tool environments, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json">Using JSON for Parameters</a>. If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.</p> <p>For tag quotas and naming restrictions, see <a href="https://docs.aws.amazon.com/general/latest/gr/arg.html#taged-reference-quotas">Service quotas for Tagging</a> in the <i>Amazon Web Services General Reference guide</i>.</p>
            add_replica_regions: <p>A list of Regions and KMS keys to replicate secrets.</p>
            force_overwrite_replica_secret: <p>Specifies whether to overwrite a secret with the same name in the destination Region. By default, secrets aren't overwritten.</p>
            type: <p>The exact string that identifies the partner that holds the external secret. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html">Using Secrets Manager managed external secrets</a>.</p>

        Raises:
            capo_secrets_manager.errors.decryption_failure.DecryptionFailure: <p>Secrets Manager can't decrypt the protected secret text using the provided KMS key. </p>
            capo_secrets_manager.errors.encryption_failure.EncryptionFailure: <p>Secrets Manager can't encrypt the protected secret text using the provided KMS key. Check that the KMS key is available, enabled, and not in an invalid state. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">Key state: Effect on your KMS key</a>.</p>
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.limit_exceeded_exception.LimitExceededException: <p>The request failed because it would exceed one of the Secrets Manager quotas.</p>
            capo_secrets_manager.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>The resource policy has syntax errors.</p>
            capo_secrets_manager.errors.precondition_not_met_exception.PreconditionNotMetException: <p>The request failed because you did not complete all the prerequisite steps.</p>
            capo_secrets_manager.errors.resource_exists_exception.ResourceExistsException: <p>A resource with the ID you requested already exists.</p>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a basic secret
            The following example shows how to create a secret. The credentials stored in the encrypted secret value are retrieved from a file on disk named mycreds.json.

            >>> client.create_secret(name='MyTestDatabaseSecret', description='My test database secret created with the CLI', secret_string='{"username":"david","password":"EXAMPLE-PASSWORD"}', client_request_token='EXAMPLE1-90ab-cdef-fedc-ba987SECRET1')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.create_secret_request.CreateSecretRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.create_secret_response.CreateSecretResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.create_secret

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.create_secret.create_secret(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.create_secret_request.CreateSecretRequest = {
            "name": name
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if description is not None:
            input_["description"] = description
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if secret_binary is not None:
            input_["secret_binary"] = secret_binary
        if secret_string is not None:
            input_["secret_string"] = secret_string
        if tags is not None:
            input_["tags"] = tags
        if add_replica_regions is not None:
            input_["add_replica_regions"] = add_replica_regions
        if force_overwrite_replica_secret is not None:
            input_["force_overwrite_replica_secret"] = force_overwrite_replica_secret
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
    ) -> "capo_secrets_manager.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes the resource-based permission policy attached to the secret. To attach a policy to a secret, use <a>PutResourcePolicy</a>.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:DeleteResourcePolicy</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret to delete the attached resource-based policy for.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete the resource-based policy attached to a secret
            The following example shows how to delete the resource-based policy that is attached to a secret.

            >>> client.delete_resource_policy(secret_id='MyTestDatabaseSecret')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.delete_resource_policy

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "secret_id": secret_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_secret(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        recovery_window_in_days: Optional[
            "capo_secrets_manager.types.recovery_window_in_days_type.RecoveryWindowInDaysType"
        ] = None,
        force_delete_without_recovery: Optional[
            "capo_secrets_manager.types.boolean_type.BooleanType"
        ] = None,
    ) -> "capo_secrets_manager.types.delete_secret_response.DeleteSecretResponse":
        """<p>Deletes a secret and all of its versions. You can specify a recovery window during which you can restore the secret. The minimum recovery window is 7 days. The default recovery window is 30 days. Secrets Manager attaches a <code>DeletionDate</code> stamp to the secret that specifies the end of the recovery window. At the end of the recovery window, Secrets Manager deletes the secret permanently.</p> <p>You can't delete a primary secret that is replicated to other Regions. You must first delete the replicas using <a>RemoveRegionsFromReplication</a>, and then delete the primary secret. When you delete a replica, it is deleted immediately.</p> <p>You can't directly delete a version of a secret. Instead, you remove all staging labels from the version using <a>UpdateSecretVersionStage</a>. This marks the version as deprecated, and then Secrets Manager can automatically delete the version in the background.</p> <p>To determine whether an application still uses a secret, you can create an Amazon CloudWatch alarm to alert you to any attempts to access a secret during the recovery window. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring_cloudwatch_deleted-secrets.html"> Monitor secrets scheduled for deletion</a>.</p> <p>Secrets Manager performs the permanent secret deletion at the end of the waiting period as a background task with low priority. There is no guarantee of a specific time after the recovery window for the permanent delete to occur.</p> <p>At any time before recovery window ends, you can use <a>RestoreSecret</a> to remove the <code>DeletionDate</code> and cancel the deletion of the secret.</p> <p>When a secret is scheduled for deletion, you cannot retrieve the secret value. You must first cancel the deletion with <a>RestoreSecret</a> and then you can retrieve the secret.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:DeleteSecret</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret to delete.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>
            recovery_window_in_days: <p>The number of days from 7 to 30 that Secrets Manager waits before permanently deleting the secret. You can't use both this parameter and <code>ForceDeleteWithoutRecovery</code> in the same call. If you don't use either, then by default Secrets Manager uses a 30 day recovery window.</p>
            force_delete_without_recovery: <p>Specifies whether to delete the secret without any recovery window. You can't use both this parameter and <code>RecoveryWindowInDays</code> in the same call. If you don't use either, then by default Secrets Manager uses a 30 day recovery window.</p> <p>Secrets Manager performs the actual deletion with an asynchronous background process, so there might be a short delay before the secret is permanently deleted. If you delete a secret and then immediately create a secret with the same name, use appropriate back off and retry logic.</p> <p>If you forcibly delete an already deleted or nonexistent secret, the operation does not return <code>ResourceNotFoundException</code>.</p> <important> <p>Use this parameter with caution. This parameter causes the operation to skip the normal recovery window before the permanent deletion that Secrets Manager would normally impose with the <code>RecoveryWindowInDays</code> parameter. If you delete a secret with the <code>ForceDeleteWithoutRecovery</code> parameter, then you have no opportunity to recover the secret. You lose the secret permanently.</p> </important>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.delete_secret_request.DeleteSecretRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.delete_secret_response.DeleteSecretResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.delete_secret

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.delete_secret.delete_secret(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.delete_secret_request.DeleteSecretRequest = {
            "secret_id": secret_id
        }
        if recovery_window_in_days is not None:
            input_["recovery_window_in_days"] = recovery_window_in_days
        if force_delete_without_recovery is not None:
            input_["force_delete_without_recovery"] = force_delete_without_recovery

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_secret(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
    ) -> "capo_secrets_manager.types.describe_secret_response.DescribeSecretResponse":
        """<p>Retrieves the details of a secret. It does not include the encrypted secret value. Secrets Manager only returns fields that have a value in the response. </p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:DescribeSecret</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret. </p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.describe_secret_request.DescribeSecretRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.describe_secret_response.DescribeSecretResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.describe_secret

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.describe_secret.describe_secret(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.describe_secret_request.DescribeSecretRequest = {
            "secret_id": secret_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_random_password(
        self,
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        password_length: Optional[
            "capo_secrets_manager.types.password_length_type.PasswordLengthType"
        ] = None,
        exclude_characters: Optional[
            "capo_secrets_manager.types.exclude_characters_type.ExcludeCharactersType"
        ] = None,
        exclude_numbers: Optional[
            "capo_secrets_manager.types.exclude_numbers_type.ExcludeNumbersType"
        ] = None,
        exclude_punctuation: Optional[
            "capo_secrets_manager.types.exclude_punctuation_type.ExcludePunctuationType"
        ] = None,
        exclude_uppercase: Optional[
            "capo_secrets_manager.types.exclude_uppercase_type.ExcludeUppercaseType"
        ] = None,
        exclude_lowercase: Optional[
            "capo_secrets_manager.types.exclude_lowercase_type.ExcludeLowercaseType"
        ] = None,
        include_space: Optional[
            "capo_secrets_manager.types.include_space_type.IncludeSpaceType"
        ] = None,
        require_each_included_type: Optional[
            "capo_secrets_manager.types.require_each_included_type_type.RequireEachIncludedTypeType"
        ] = None,
    ) -> "capo_secrets_manager.types.get_random_password_response.GetRandomPasswordResponse":
        r"""<p>Generates a random password. We recommend that you specify the maximum length and include every character type that the system you are generating a password for can support. By default, Secrets Manager uses uppercase and lowercase letters, numbers, and the following characters in passwords: <code>!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~</code> </p> <p>Secrets Manager generates a CloudTrail log entry when you call this action.</p> <p> <b>Required permissions: </b> <code>secretsmanager:GetRandomPassword</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            password_length: <p>The length of the password. If you don't include this parameter, the default length is 32 characters.</p>
            exclude_characters: <p>A string of the characters that you don't want in the password.</p>
            exclude_numbers: <p>Specifies whether to exclude numbers from the password. If you don't include this switch, the password can contain numbers.</p>
            exclude_punctuation: <p>Specifies whether to exclude the following punctuation characters from the password: <code>! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~</code>. If you don't include this switch, the password can contain punctuation.</p>
            exclude_uppercase: <p>Specifies whether to exclude uppercase letters from the password. If you don't include this switch, the password can contain uppercase letters.</p>
            exclude_lowercase: <p>Specifies whether to exclude lowercase letters from the password. If you don't include this switch, the password can contain lowercase letters.</p>
            include_space: <p>Specifies whether to include the space character. If you include this switch, the password can contain space characters.</p>
            require_each_included_type: <p>Specifies whether to include at least one upper and lowercase letter, one number, and one punctuation. If you don't include this switch, the password contains at least one of every character type.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To generate a random password
            The following example shows how to request a randomly generated password. This example includes the optional flags to require spaces and at least one character of each included type. It specifies a length of 20 characters.

            >>> client.get_random_password(password_length=20, include_space=True, require_each_included_type=True)
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.get_random_password_request.GetRandomPasswordRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.get_random_password_response.GetRandomPasswordResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.get_random_password

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.get_random_password.get_random_password(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.get_random_password_request.GetRandomPasswordRequest = {}
        if password_length is not None:
            input_["password_length"] = password_length
        if exclude_characters is not None:
            input_["exclude_characters"] = exclude_characters
        if exclude_numbers is not None:
            input_["exclude_numbers"] = exclude_numbers
        if exclude_punctuation is not None:
            input_["exclude_punctuation"] = exclude_punctuation
        if exclude_uppercase is not None:
            input_["exclude_uppercase"] = exclude_uppercase
        if exclude_lowercase is not None:
            input_["exclude_lowercase"] = exclude_lowercase
        if include_space is not None:
            input_["include_space"] = include_space
        if require_each_included_type is not None:
            input_["require_each_included_type"] = require_each_included_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
    ) -> "capo_secrets_manager.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the JSON text of the resource-based policy document attached to the secret. For more information about permissions policies attached to a secret, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html">Permissions policies attached to a secret</a>.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:GetResourcePolicy</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret to retrieve the attached resource-based policy for.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve the resource-based policy attached to a secret
            The following example shows how to retrieve the resource-based policy that is attached to a secret.

            >>> client.get_resource_policy(secret_id='MyTestDatabaseSecret')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.get_resource_policy

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "secret_id": secret_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_secret_value(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        version_id: Optional[
            "capo_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
        ] = None,
        version_stage: Optional[
            "capo_secrets_manager.types.secret_version_stage_type.SecretVersionStageType"
        ] = None,
    ) -> "capo_secrets_manager.types.get_secret_value_response.GetSecretValueResponse":
        """<p>Retrieves the contents of the encrypted fields <code>SecretString</code> or <code>SecretBinary</code> from the specified version of a secret, whichever contains content.</p> <p>To retrieve the values for a group of secrets, call <a>BatchGetSecretValue</a>.</p> <p>We recommend that you cache your secret values by using client-side caching. Caching secrets improves speed and reduces your costs. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html">Cache secrets for your applications</a>.</p> <p>To retrieve the previous version of a secret, use <code>VersionStage</code> and specify AWSPREVIOUS. To revert to the previous version of a secret, call <a href="https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/update-secret-version-stage.html">UpdateSecretVersionStage</a>.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:GetSecretValue</code>. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key <code>aws/secretsmanager</code>, then you also need <code>kms:Decrypt</code> permissions for that key. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret to retrieve. To retrieve a secret from another account, you must use an ARN.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>
            version_id: <p>The unique identifier of the version of the secret to retrieve. If you include both this parameter and <code>VersionStage</code>, the two parameters must refer to the same secret version. If you don't specify either a <code>VersionStage</code> or <code>VersionId</code>, then Secrets Manager returns the <code>AWSCURRENT</code> version.</p> <p>This value is typically a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type</a> value with 32 hexadecimal digits.</p>
            version_stage: <p>The staging label of the version of the secret to retrieve. </p> <p>Secrets Manager uses staging labels to keep track of different versions during the rotation process. If you include both this parameter and <code>VersionId</code>, the two parameters must refer to the same secret version. If you don't specify either a <code>VersionStage</code> or <code>VersionId</code>, Secrets Manager returns the <code>AWSCURRENT</code> version.</p>

        Raises:
            capo_secrets_manager.errors.decryption_failure.DecryptionFailure: <p>Secrets Manager can't decrypt the protected secret text using the provided KMS key. </p>
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve the encrypted secret value of a secret
            The following example shows how to retrieve a secret string value.

            >>> client.get_secret_value(secret_id='MyTestDatabaseSecret')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.get_secret_value_request.GetSecretValueRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.get_secret_value_response.GetSecretValueResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.get_secret_value

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.get_secret_value.get_secret_value(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.get_secret_value_request.GetSecretValueRequest = {
            "secret_id": secret_id
        }
        if version_id is not None:
            input_["version_id"] = version_id
        if version_stage is not None:
            input_["version_stage"] = version_stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_secrets(
        self,
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        include_planned_deletion: Optional[
            "capo_secrets_manager.types.boolean_type.BooleanType"
        ] = None,
        max_results: Optional[
            "capo_secrets_manager.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "capo_secrets_manager.types.next_token_type.NextTokenType"
        ] = None,
        filters: Optional[
            "capo_secrets_manager.types.filters_list_type.FiltersListType"
        ] = None,
        sort_order: Optional[
            "capo_secrets_manager.types.sort_order_type.SortOrderType"
        ] = None,
        sort_by: Optional["capo_secrets_manager.types.sort_by_type.SortByType"] = None,
    ) -> "capo_secrets_manager.types.list_secrets_response.ListSecretsResponse":
        """<p>Lists the secrets that are stored by Secrets Manager in the Amazon Web Services account, not including secrets that are marked for deletion. To see secrets marked for deletion, use the Secrets Manager console.</p> <p>All Secrets Manager operations are eventually consistent. ListSecrets might not reflect changes from the last five minutes. You can get more recent information for a specific secret by calling <a>DescribeSecret</a>.</p> <p>To list the versions of a secret, use <a>ListSecretVersionIds</a>.</p> <p>To retrieve the values for the secrets, call <a>BatchGetSecretValue</a> or <a>GetSecretValue</a>.</p> <p>For information about finding secrets in the console, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html">Find secrets in Secrets Manager</a>.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:ListSecrets</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            include_planned_deletion: <p>Specifies whether to include secrets scheduled for deletion. By default, secrets scheduled for deletion aren't included.</p>
            max_results: <p>The number of results to include in the response.</p> <p>If there are more results available, in the response, Secrets Manager includes <code>NextToken</code>. To get the next results, call <code>ListSecrets</code> again with the value from <code>NextToken</code>.</p>
            next_token: <p>A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call <code>ListSecrets</code> again with this value.</p>
            filters: <p>The filters to apply to the list of secrets.</p>
            sort_order: <p>Secrets are listed by <code>CreatedDate</code>. </p>
            sort_by: <p>If not specified, secrets are listed by <code>CreatedDate</code>.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is invalid.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the secrets in your account
            The following example shows how to list all of the secrets in your account.

            >>> client.list_secrets()
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.list_secrets_request.ListSecretsRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.list_secrets_response.ListSecretsResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.list_secrets

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.list_secrets.list_secrets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.list_secrets_request.ListSecretsRequest = {}
        if include_planned_deletion is not None:
            input_["include_planned_deletion"] = include_planned_deletion
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_secrets(
        self,
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        include_planned_deletion: Optional[
            "capo_secrets_manager.types.boolean_type.BooleanType"
        ] = None,
        max_results: Optional[
            "capo_secrets_manager.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "capo_secrets_manager.types.next_token_type.NextTokenType"
        ] = None,
        filters: Optional[
            "capo_secrets_manager.types.filters_list_type.FiltersListType"
        ] = None,
        sort_order: Optional[
            "capo_secrets_manager.types.sort_order_type.SortOrderType"
        ] = None,
        sort_by: Optional["capo_secrets_manager.types.sort_by_type.SortByType"] = None,
    ) -> (
        "Iterator[capo_secrets_manager.types.list_secrets_response.ListSecretsResponse]"
    ):
        _token = next_token
        while True:
            _response = self.list_secrets(
                config_overrides=config_overrides,
                include_planned_deletion=include_planned_deletion,
                max_results=max_results,
                next_token=_token,
                filters=filters,
                sort_order=sort_order,
                sort_by=sort_by,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_secret_version_ids(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        max_results: Optional[
            "capo_secrets_manager.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "capo_secrets_manager.types.next_token_type.NextTokenType"
        ] = None,
        include_deprecated: Optional[
            "capo_secrets_manager.types.boolean_type.BooleanType"
        ] = None,
    ) -> "capo_secrets_manager.types.list_secret_version_ids_response.ListSecretVersionIdsResponse":
        """<p>Lists the versions of a secret. Secrets Manager uses staging labels to indicate the different versions of a secret. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version"> Secrets Manager concepts: Versions</a>.</p> <p>To list the secrets in the account, use <a>ListSecrets</a>.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:ListSecretVersionIds</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret whose versions you want to list.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>
            max_results: <p>The number of results to include in the response.</p> <p>If there are more results available, in the response, Secrets Manager includes <code>NextToken</code>. To get the next results, call <code>ListSecretVersionIds</code> again with the value from <code>NextToken</code>. </p>
            next_token: <p>A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call <code>ListSecretVersionIds</code> again with this value.</p>
            include_deprecated: <p>Specifies whether to include versions of secrets that don't have any staging labels attached to them. Versions without staging labels are considered deprecated and are subject to deletion by Secrets Manager. By default, versions without staging labels aren't included.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is invalid.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list all of the secret versions associated with a secret
            The following example shows how to retrieve a list of all of the versions of a secret, including those without any staging labels.

            >>> client.list_secret_version_ids(secret_id='MyTestDatabaseSecret', include_deprecated=True)
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.list_secret_version_ids_request.ListSecretVersionIdsRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.list_secret_version_ids_response.ListSecretVersionIdsResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.list_secret_version_ids

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.list_secret_version_ids.list_secret_version_ids(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.list_secret_version_ids_request.ListSecretVersionIdsRequest = {
            "secret_id": secret_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_deprecated is not None:
            input_["include_deprecated"] = include_deprecated

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_secret_version_ids(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        max_results: Optional[
            "capo_secrets_manager.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "capo_secrets_manager.types.next_token_type.NextTokenType"
        ] = None,
        include_deprecated: Optional[
            "capo_secrets_manager.types.boolean_type.BooleanType"
        ] = None,
    ) -> "Iterator[capo_secrets_manager.types.list_secret_version_ids_response.ListSecretVersionIdsResponse]":
        _token = next_token
        while True:
            _response = self.list_secret_version_ids(
                secret_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                include_deprecated=include_deprecated,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_resource_policy(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        resource_policy: "capo_secrets_manager.types.non_empty_resource_policy_type.NonEmptyResourcePolicyType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        block_public_policy: Optional[
            "capo_secrets_manager.types.boolean_type.BooleanType"
        ] = None,
    ) -> "capo_secrets_manager.types.put_resource_policy_response.PutResourcePolicyResponse":
        r"""<p>Attaches a resource-based permission policy to a secret. A resource-based policy is optional. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control for Secrets Manager</a> </p> <p>For information about attaching a policy in the console, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html">Attach a permissions policy to a secret</a>.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:PutResourcePolicy</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret to attach the resource-based policy.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>
            resource_policy: <p>A JSON-formatted string for an Amazon Web Services resource-based policy. For example policies, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html">Permissions policy examples</a>.</p>
            block_public_policy: <p>Specifies whether to block resource-based policies that allow broad access to the secret, for example those that use a wildcard for the principal. By default, public policies aren't blocked.</p> <important> <p>Resource policy validation and the BlockPublicPolicy parameter help protect your resources by preventing public access from being granted through the resource policies that are directly attached to your secrets. In addition to using these features, carefully inspect the following policies to confirm that they do not grant public access:</p> <ul> <li> <p>Identity-based policies attached to associated Amazon Web Services principals (for example, IAM roles)</p> </li> <li> <p>Resource-based policies attached to associated Amazon Web Services resources (for example, Key Management Service (KMS) keys)</p> </li> </ul> <p>To review permissions to your secrets, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/determine-acccess_examine-iam-policies.html">Determine who has permissions to your secrets</a>.</p> </important>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>The resource policy has syntax errors.</p>
            capo_secrets_manager.errors.public_policy_exception.PublicPolicyException: <p>The <code>BlockPublicPolicy</code> parameter is set to true, and the resource policy did not prevent broad access to the secret.</p>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add a resource-based policy to a secret
            The following example shows how to add a resource-based policy to a secret.

            >>> client.put_resource_policy(secret_id='MyTestDatabaseSecret', resource_policy='{\n"Version":"2012-10-17",\n"Statement":[{\n"Effect":"Allow",\n"Principal":{\n"AWS":"arn:aws:iam::123456789012:root"\n},\n"Action":"secretsmanager:GetSecretValue",\n"Resource":"*"\n}]\n}')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.put_resource_policy

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "secret_id": secret_id,
            "resource_policy": resource_policy,
        }
        if block_public_policy is not None:
            input_["block_public_policy"] = block_public_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_secret_value(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        client_request_token: Optional[
            "capo_secrets_manager.types.client_request_token_type.ClientRequestTokenType"
        ] = None,
        secret_binary: Optional[
            "capo_secrets_manager.types.secret_binary_type.SecretBinaryType"
        ] = None,
        secret_string: Optional[
            "capo_secrets_manager.types.secret_string_type.SecretStringType"
        ] = None,
        version_stages: Optional[
            "capo_secrets_manager.types.secret_version_stages_type.SecretVersionStagesType"
        ] = None,
        rotation_token: Optional[
            "capo_secrets_manager.types.rotation_token_type.RotationTokenType"
        ] = None,
    ) -> "capo_secrets_manager.types.put_secret_value_response.PutSecretValueResponse":
        """<p>Creates a new version of your secret by creating a new encrypted value and attaching it to the secret. version can contain a new <code>SecretString</code> value or a new <code>SecretBinary</code> value. </p> <p>Do not call <code>PutSecretValue</code> at a sustained rate of more than once every 10 minutes. When you update the secret value, Secrets Manager creates a new version of the secret. Secrets Manager keeps 100 of the most recent versions, but it keeps <i>all</i> secret versions created in the last 24 hours. If you call <code>PutSecretValue</code> more than once every 10 minutes, you will create more versions than Secrets Manager removes, and you will reach the quota for secret versions.</p> <p>You can specify the staging labels to attach to the new version in <code>VersionStages</code>. If you don't include <code>VersionStages</code>, then Secrets Manager automatically moves the staging label <code>AWSCURRENT</code> to this version. If this operation creates the first version for the secret, then Secrets Manager automatically attaches the staging label <code>AWSCURRENT</code> to it. If this operation moves the staging label <code>AWSCURRENT</code> from another version to this version, then Secrets Manager also automatically moves the staging label <code>AWSPREVIOUS</code> to the version that <code>AWSCURRENT</code> was removed from.</p> <p>This operation is idempotent. If you call this operation with a <code>ClientRequestToken</code> that matches an existing version's VersionId, and you specify the same secret data, the operation succeeds but does nothing. However, if the secret data is different, then the operation fails because you can't modify an existing version; you can only create new ones.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters except <code>SecretBinary</code>, <code>SecretString</code>, or <code>RotationToken</code> because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:PutSecretValue</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p> <important> <p>When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. This is a concern if the command includes the value of a secret. Learn how to <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/security_cli-exposure-risks.html">Mitigate the risks of using command-line tools to store Secrets Manager secrets</a>.</p> </important>

        Args:
            secret_id: <p>The ARN or name of the secret to add a new version to.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p> <p>If the secret doesn't already exist, use <code>CreateSecret</code> instead.</p>
            client_request_token: <p>A unique identifier for the new version of the secret. </p> <note> <p>If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request. </p> </note> <p>If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a <code>ClientRequestToken</code> and include it in the request.</p> <p>This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type</a> value to ensure uniqueness of your versions within the specified secret. </p> <ul> <li> <p>If the <code>ClientRequestToken</code> value isn't already associated with a version of the secret then a new version of the secret is created. </p> </li> <li> <p>If a version with this value already exists and that version's <code>SecretString</code> or <code>SecretBinary</code> values are the same as those in the request then the request is ignored. The operation is idempotent. </p> </li> <li> <p>If a version with this value already exists and the version of the <code>SecretString</code> and <code>SecretBinary</code> values are different from those in the request, then the request fails because you can't modify a secret version. You can only create new versions to store new secret values.</p> </li> </ul> <p>This value becomes the <code>VersionId</code> of the new version.</p>
            secret_binary: <p>The binary data to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then pass the contents of the file as a parameter. </p> <p>You must include <code>SecretBinary</code> or <code>SecretString</code>, but not both.</p> <p>You can't access this value from the Secrets Manager console.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>
            secret_string: <p>The text to encrypt and store in the new version of the secret. </p> <p>You must include <code>SecretBinary</code> or <code>SecretString</code>, but not both.</p> <p>We recommend you create the secret string as JSON key/value pairs, as shown in the example.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>
            version_stages: <p>A list of staging labels to attach to this version of the secret. Secrets Manager uses staging labels to track versions of a secret through the rotation process.</p> <p>If you specify a staging label that's already associated with a different version of the same secret, then Secrets Manager removes the label from the other version and attaches it to this version. If you specify <code>AWSCURRENT</code>, and it is already attached to another version, then Secrets Manager also moves the staging label <code>AWSPREVIOUS</code> to the version that <code>AWSCURRENT</code> was removed from.</p> <p>If you don't include <code>VersionStages</code>, then Secrets Manager automatically moves the staging label <code>AWSCURRENT</code> to this version.</p>
            rotation_token: <p>A unique identifier that indicates the source of the request. Required for secret rotations using an IAM assumed role or cross-account rotation, in which you rotate a secret in one account by using a Lambda rotation function in another account. In both cases, the rotation function assumes an IAM role to call Secrets Manager, and then Secrets Manager validates the identity using the token. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html">How rotation works</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_lambda">Rotation by Lambda functions</a>.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>

        Raises:
            capo_secrets_manager.errors.decryption_failure.DecryptionFailure: <p>Secrets Manager can't decrypt the protected secret text using the provided KMS key. </p>
            capo_secrets_manager.errors.encryption_failure.EncryptionFailure: <p>Secrets Manager can't encrypt the protected secret text using the provided KMS key. Check that the KMS key is available, enabled, and not in an invalid state. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">Key state: Effect on your KMS key</a>.</p>
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.limit_exceeded_exception.LimitExceededException: <p>The request failed because it would exceed one of the Secrets Manager quotas.</p>
            capo_secrets_manager.errors.resource_exists_exception.ResourceExistsException: <p>A resource with the ID you requested already exists.</p>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To store a secret value in a new version of a secret
            The following example shows how to create a new version of the secret. Alternatively, you can use the update-secret command.

            >>> client.put_secret_value(secret_id='MyTestDatabaseSecret', secret_string='{"username":"david","password":"EXAMPLE-PASSWORD"}', client_request_token='EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.put_secret_value_request.PutSecretValueRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.put_secret_value_response.PutSecretValueResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.put_secret_value

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.put_secret_value.put_secret_value(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.put_secret_value_request.PutSecretValueRequest = {
            "secret_id": secret_id
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if secret_binary is not None:
            input_["secret_binary"] = secret_binary
        if secret_string is not None:
            input_["secret_string"] = secret_string
        if version_stages is not None:
            input_["version_stages"] = version_stages
        if rotation_token is not None:
            input_["rotation_token"] = rotation_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_regions_from_replication(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        remove_replica_regions: "capo_secrets_manager.types.remove_replica_region_list_type.RemoveReplicaRegionListType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
    ) -> "capo_secrets_manager.types.remove_regions_from_replication_response.RemoveRegionsFromReplicationResponse":
        """<p>For a secret that is replicated to other Regions, deletes the secret replicas from the Regions you specify.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:RemoveRegionsFromReplication</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret.</p>
            remove_replica_regions: <p>The Regions of the replicas to remove.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.remove_regions_from_replication_request.RemoveRegionsFromReplicationRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.remove_regions_from_replication_response.RemoveRegionsFromReplicationResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.remove_regions_from_replication

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.remove_regions_from_replication.remove_regions_from_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.remove_regions_from_replication_request.RemoveRegionsFromReplicationRequest = {
            "secret_id": secret_id,
            "remove_replica_regions": remove_replica_regions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def replicate_secret_to_regions(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        add_replica_regions: "capo_secrets_manager.types.add_replica_region_list_type.AddReplicaRegionListType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        force_overwrite_replica_secret: Optional[
            "capo_secrets_manager.types.boolean_type.BooleanType"
        ] = None,
    ) -> "capo_secrets_manager.types.replicate_secret_to_regions_response.ReplicateSecretToRegionsResponse":
        """<p>Replicates the secret to a new Regions. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html">Multi-Region secrets</a>.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:ReplicateSecretToRegions</code>. If the primary secret is encrypted with a KMS key other than <code>aws/secretsmanager</code>, you also need <code>kms:Decrypt</code> permission to the key. To encrypt the replicated secret with a KMS key other than <code>aws/secretsmanager</code>, you need <code>kms:GenerateDataKey</code> and <code>kms:Encrypt</code> to the key. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret to replicate.</p>
            add_replica_regions: <p>A list of Regions in which to replicate the secret.</p>
            force_overwrite_replica_secret: <p>Specifies whether to overwrite a secret with the same name in the destination Region. By default, secrets aren't overwritten.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example
            The following example replicates a secret to eu-west-3. The replica is encrypted with the AWS managed key aws/secretsmanager.

            >>> client.replicate_secret_to_regions(secret_id='MyTestSecret', add_replica_regions=[{'Region': 'eu-west-3'}], force_overwrite_replica_secret=True)
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.replicate_secret_to_regions_request.ReplicateSecretToRegionsRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.replicate_secret_to_regions_response.ReplicateSecretToRegionsResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.replicate_secret_to_regions

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.replicate_secret_to_regions.replicate_secret_to_regions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.replicate_secret_to_regions_request.ReplicateSecretToRegionsRequest = {
            "secret_id": secret_id,
            "add_replica_regions": add_replica_regions,
        }
        if force_overwrite_replica_secret is not None:
            input_["force_overwrite_replica_secret"] = force_overwrite_replica_secret

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_secret(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
    ) -> "capo_secrets_manager.types.restore_secret_response.RestoreSecretResponse":
        """<p>Cancels the scheduled deletion of a secret by removing the <code>DeletedDate</code> time stamp. You can access a secret again after it has been restored.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:RestoreSecret</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret to restore.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To restore a previously deleted secret
            The following example shows how to restore a secret that you previously scheduled for deletion.

            >>> client.restore_secret(secret_id='MyTestDatabaseSecret')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.restore_secret_request.RestoreSecretRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.restore_secret_response.RestoreSecretResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.restore_secret

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.restore_secret.restore_secret(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.restore_secret_request.RestoreSecretRequest = {
            "secret_id": secret_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def rotate_secret(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        client_request_token: Optional[
            "capo_secrets_manager.types.client_request_token_type.ClientRequestTokenType"
        ] = None,
        rotation_lambda_arn: Optional[
            "capo_secrets_manager.types.rotation_lambda_arn_type.RotationLambdaARNType"
        ] = None,
        rotation_rules: Optional[
            "capo_secrets_manager.types.rotation_rules_type.RotationRulesType"
        ] = None,
        external_secret_rotation_metadata: Optional[
            "capo_secrets_manager.types.external_secret_rotation_metadata_type.ExternalSecretRotationMetadataType"
        ] = None,
        external_secret_rotation_role_arn: Optional[
            "capo_secrets_manager.types.role_arn_type.RoleARNType"
        ] = None,
        rotate_immediately: Optional[
            "capo_secrets_manager.types.boolean_type.BooleanType"
        ] = None,
    ) -> "capo_secrets_manager.types.rotate_secret_response.RotateSecretResponse":
        """<p>Configures and starts the asynchronous process of rotating the secret. For information about rotation, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html">Rotate secrets</a> in the <i>Secrets Manager User Guide</i>. If you include the configuration parameters, the operation sets the values for the secret and then immediately starts a rotation. If you don't include the configuration parameters, the operation starts a rotation with the values already stored in the secret. </p> <p>When rotation is successful, the <code>AWSPENDING</code> staging label might be attached to the same version as the <code>AWSCURRENT</code> version, or it might not be attached to any version. If the <code>AWSPENDING</code> staging label is present but not attached to the same version as <code>AWSCURRENT</code>, then any later invocation of <code>RotateSecret</code> assumes that a previous rotation request is still in progress and returns an error. When rotation is unsuccessful, the <code>AWSPENDING</code> staging label might be attached to an empty secret version. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot_rotation.html">Troubleshoot rotation</a> in the <i>Secrets Manager User Guide</i>.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:RotateSecret</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. You also need <code>lambda:InvokeFunction</code> permissions on the rotation function. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets-required-permissions-function.html"> Permissions for rotation</a>.</p>

        Args:
            secret_id: <p>The ARN or name of the secret to rotate.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>
            client_request_token: <p>A unique identifier for the new version of the secret. You only need to specify this value if you implement your own retry logic and you want to ensure that Secrets Manager doesn't attempt to create a secret version twice.</p> <note> <p>If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request. </p> </note> <p>If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a <code>ClientRequestToken</code> and include it in the request.</p> <p>This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type</a> value to ensure uniqueness of your versions within the specified secret. </p>
            rotation_lambda_arn: <p>For secrets that use a Lambda rotation function to rotate, the ARN of the Lambda rotation function. </p> <p>For secrets that use <i>managed rotation</i>, omit this field. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_managed.html">Managed rotation</a> in the <i>Secrets Manager User Guide</i>.</p>
            rotation_rules: <p>A structure that defines the rotation configuration for this secret.</p> <important> <p>When changing an existing rotation schedule and setting <code>RotateImmediately</code> to <code>false</code>:</p> <ul> <li> <p>If using <code>AutomaticallyAfterDays</code> or a <code>ScheduleExpression</code> with <code>rate()</code>, the previously scheduled rotation might still occur.</p> </li> <li> <p>To prevent unintended rotations, use a <code>ScheduleExpression</code> with <code>cron()</code> for granular control over rotation windows.</p> </li> </ul> </important>
            external_secret_rotation_metadata: <p>The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information about the required information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html">Using Secrets Manager managed external secrets</a> </p>
            external_secret_rotation_role_arn: <p>The Amazon Resource Name (ARN) of the role that allows Secrets Manager to rotate a secret held by a third-party partner. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-security.html">Security and permissions</a>.</p>
            rotate_immediately: <p>Specifies whether to rotate the secret immediately or wait until the next scheduled rotation window. The rotation schedule is defined in <a>RotateSecretRequest$RotationRules</a>.</p> <p>The default for <code>RotateImmediately</code> is <code>true</code>. If you don't specify this value, Secrets Manager rotates the secret immediately.</p> <p>If you set <code>RotateImmediately</code> to <code>false</code>, Secrets Manager tests the rotation configuration by running the <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html"> <code>testSecret</code> step</a> of the Lambda rotation function. This test creates an <code>AWSPENDING</code> version of the secret and then removes it.</p> <p>When changing an existing rotation schedule and setting <code>RotateImmediately</code> to <code>false</code>:</p> <ul> <li> <p>If using <code>AutomaticallyAfterDays</code> or a <code>ScheduleExpression</code> with <code>rate()</code>, the previously scheduled rotation might still occur.</p> </li> <li> <p>To prevent unintended rotations, use a <code>ScheduleExpression</code> with <code>cron()</code> for granular control over rotation windows.</p> </li> </ul> <p>Rotation is an asynchronous process. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html">How rotation works</a>.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To configure rotation for a secret
            The following example configures rotation for a secret using a cron expression. The first rotation happens immediately after the changes are stored in the secret. The rotation schedule is the first and 15th day of every month. The rotation window begins at 4:00 PM UTC and ends at 6:00 PM.

            >>> client.rotate_secret(secret_id='MyTestDatabaseSecret', rotation_lambda_arn='arn:aws:lambda:us-west-2:123456789012:function:MyTestDatabaseRotationLambda', rotation_rules={'ScheduleExpression': 'cron(0 16 1,15 * ? *)', 'Duration': '2h'})
            To request an immediate rotation for a secret
            The following example requests an immediate invocation of the secret's Lambda rotation function. It assumes that the specified secret already has rotation configured. The rotation function runs asynchronously in the background.

            >>> client.rotate_secret(secret_id='MyTestDatabaseSecret')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.rotate_secret_request.RotateSecretRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.rotate_secret_response.RotateSecretResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.rotate_secret

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.rotate_secret.rotate_secret(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.rotate_secret_request.RotateSecretRequest = {
            "secret_id": secret_id
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if rotation_lambda_arn is not None:
            input_["rotation_lambda_arn"] = rotation_lambda_arn
        if rotation_rules is not None:
            input_["rotation_rules"] = rotation_rules
        if external_secret_rotation_metadata is not None:
            input_["external_secret_rotation_metadata"] = (
                external_secret_rotation_metadata
            )
        if external_secret_rotation_role_arn is not None:
            input_["external_secret_rotation_role_arn"] = (
                external_secret_rotation_role_arn
            )
        if rotate_immediately is not None:
            input_["rotate_immediately"] = rotate_immediately

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_replication_to_replica(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
    ) -> "capo_secrets_manager.types.stop_replication_to_replica_response.StopReplicationToReplicaResponse":
        """<p>Removes the link between the replica secret and the primary secret and promotes the replica to a primary secret in the replica Region.</p> <p>You must call this operation from the Region in which you want to promote the replica to a primary secret.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:StopReplicationToReplica</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The name of the secret or the replica ARN. The replica ARN is the same as the original primary secret ARN expect the Region is changed to the replica Region. </p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.stop_replication_to_replica_request.StopReplicationToReplicaRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.stop_replication_to_replica_response.StopReplicationToReplicaResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.stop_replication_to_replica

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.stop_replication_to_replica.stop_replication_to_replica(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.stop_replication_to_replica_request.StopReplicationToReplicaRequest = {
            "secret_id": secret_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        tags: "capo_secrets_manager.types.tag_list_type.TagListType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
    ) -> None:
        """<p>Attaches tags to a secret. Tags consist of a key name and a value. Tags are part of the secret's metadata. They are not associated with specific versions of the secret. This operation appends tags to the existing list of tags.</p> <p>For tag quotas and naming restrictions, see <a href="https://docs.aws.amazon.com/general/latest/gr/arg.html#taged-reference-quotas">Service quotas for Tagging</a> in the <i>Amazon Web Services General Reference guide</i>.</p> <important> <p>If you use tags as part of your security strategy, then adding or removing a tag can change permissions. If successfully completing this operation would result in you losing your permissions for this secret, then the operation is blocked and returns an Access Denied error.</p> </important> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:TagResource</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The identifier for the secret to attach tags to. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>
            tags: <p>The tags to attach to the secret as a JSON text string argument. Each element in the list consists of a <code>Key</code> and a <code>Value</code>.</p> <p>For storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For more information, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html">Specifying parameter values for the Amazon Web Services CLI</a> in the Amazon Web Services CLI User Guide.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add tags to a secret
            The following example shows how to attach two tags each with a Key and Value to a secret. There is no output from this API. To see the result, use the DescribeSecret operation.

            >>> client.tag_resource(secret_id='MyExampleSecret', tags=[{'Key': 'FirstTag', 'Value': 'SomeValue'}, {'Key': 'SecondTag', 'Value': 'AnotherValue'}])
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_secrets_manager._operations.secretsmanager.tag_resource

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.tag_resource_request.TagResourceRequest = {
            "secret_id": secret_id,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        tag_keys: "capo_secrets_manager.types.tag_key_list_type.TagKeyListType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
    ) -> None:
        """<p>Removes specific tags from a secret.</p> <p>This operation is idempotent. If a requested tag is not attached to the secret, no error is returned and the secret metadata is unchanged.</p> <important> <p>If you use tags as part of your security strategy, then removing a tag can change permissions. If successfully completing this operation would result in you losing your permissions for this secret, then the operation is blocked and returns an Access Denied error.</p> </important> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:UntagResource</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>
            tag_keys: <p>A list of tag key names to remove from the secret. You don't specify the value. Both the key and its associated value are removed.</p> <p>This parameter requires a JSON text string argument.</p> <p>For storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For more information, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html">Specifying parameter values for the Amazon Web Services CLI</a> in the Amazon Web Services CLI User Guide.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove tags from a secret
            The following example shows how to remove two tags from a secret's metadata. For each, both the tag and the associated value are removed. There is no output from this API. To see the result, use the DescribeSecret operation.

            >>> client.untag_resource(secret_id='MyTestDatabaseSecret', tag_keys=['FirstTag', 'SecondTag'])
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_secrets_manager._operations.secretsmanager.untag_resource

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.untag_resource_request.UntagResourceRequest = {
            "secret_id": secret_id,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_secret(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        client_request_token: Optional[
            "capo_secrets_manager.types.client_request_token_type.ClientRequestTokenType"
        ] = None,
        description: Optional[
            "capo_secrets_manager.types.description_type.DescriptionType"
        ] = None,
        kms_key_id: Optional[
            "capo_secrets_manager.types.kms_key_id_type.KmsKeyIdType"
        ] = None,
        secret_binary: Optional[
            "capo_secrets_manager.types.secret_binary_type.SecretBinaryType"
        ] = None,
        secret_string: Optional[
            "capo_secrets_manager.types.secret_string_type.SecretStringType"
        ] = None,
        type: Optional[
            "capo_secrets_manager.types.medea_type_type.MedeaTypeType"
        ] = None,
    ) -> "capo_secrets_manager.types.update_secret_response.UpdateSecretResponse":
        """<p>Modifies the details of a secret, including metadata and the secret value. To change the secret value, you can also use <a>PutSecretValue</a>.</p> <p>To change the rotation configuration of a secret, use <a>RotateSecret</a> instead.</p> <p>To change a secret so that it is managed by another service, you need to recreate the secret in that service. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets Manager secrets managed by other Amazon Web Services services</a>.</p> <p>We recommend you avoid calling <code>UpdateSecret</code> at a sustained rate of more than once every 10 minutes. When you call <code>UpdateSecret</code> to update the secret value, Secrets Manager creates a new version of the secret. Secrets Manager removes outdated versions when there are more than 100, but it does not remove versions created less than 24 hours ago. If you update the secret value more than once every 10 minutes, you create more versions than Secrets Manager removes, and you will reach the quota for secret versions.</p> <p>If you include <code>SecretString</code> or <code>SecretBinary</code> to create a new secret version, Secrets Manager automatically moves the staging label <code>AWSCURRENT</code> to the new version. Then it attaches the label <code>AWSPREVIOUS</code> to the version that <code>AWSCURRENT</code> was removed from.</p> <p>If you call this operation with a <code>ClientRequestToken</code> that matches an existing version's <code>VersionId</code>, the operation results in an error. You can't modify an existing version, you can only create a new version. To remove a version, remove all staging labels from it. See <a>UpdateSecretVersionStage</a>.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters except <code>SecretBinary</code> or <code>SecretString</code> because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:UpdateSecret</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. If you use a customer managed key, you must also have <code>kms:GenerateDataKey</code>, <code>kms:Encrypt</code>, and <code>kms:Decrypt</code> permissions on the key. If you change the KMS key and you don't have <code>kms:Encrypt</code> permission to the new key, Secrets Manager does not re-encrypt existing secret versions with the new key. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html"> Secret encryption and decryption</a>.</p> <important> <p>When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. This is a concern if the command includes the value of a secret. Learn how to <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/security_cli-exposure-risks.html">Mitigate the risks of using command-line tools to store Secrets Manager secrets</a>.</p> </important>

        Args:
            secret_id: <p>The ARN or name of the secret.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>
            client_request_token: <p>If you include <code>SecretString</code> or <code>SecretBinary</code>, then Secrets Manager creates a new version for the secret, and this parameter specifies the unique identifier for the new version.</p> <note> <p>If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request. </p> </note> <p>If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a <code>ClientRequestToken</code> and include it in the request.</p> <p>This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type</a> value to ensure uniqueness of your versions within the specified secret. </p>
            description: <p>The description of the secret.</p>
            kms_key_id: <p>The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt new secret versions as well as any existing versions with the staging labels <code>AWSCURRENT</code>, <code>AWSPENDING</code>, or <code>AWSPREVIOUS</code>. If you don't have <code>kms:Encrypt</code> permission to the new key, Secrets Manager does not re-encrypt existing secret versions with the new key. For more information about versions and staging labels, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version">Concepts: Version</a>.</p> <p>A key alias is always prefixed by <code>alias/</code>, for example <code>alias/aws/secretsmanager</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html">About aliases</a>.</p> <p>If you set this to an empty string, Secrets Manager uses the Amazon Web Services managed key <code>aws/secretsmanager</code>. If this key doesn't already exist in your account, then Secrets Manager creates it for you automatically. All users and roles in the Amazon Web Services account automatically have access to use <code>aws/secretsmanager</code>. Creating <code>aws/secretsmanager</code> can result in a one-time significant delay in returning the result. </p> <important> <p>You can only use the Amazon Web Services managed key <code>aws/secretsmanager</code> if you call this operation using credentials from the same Amazon Web Services account that owns the secret. If the secret is in a different account, then you must use a customer managed key and provide the ARN of that KMS key in this field. The user making the call must have permissions to both the secret and the KMS key in their respective accounts.</p> </important>
            secret_binary: <p>The binary data to encrypt and store in the new version of the secret. We recommend that you store your binary data in a file and then pass the contents of the file as a parameter. </p> <p>Either <code>SecretBinary</code> or <code>SecretString</code> must have a value, but not both.</p> <p>You can't access this parameter in the Secrets Manager console.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>
            secret_string: <p>The text data to encrypt and store in the new version of the secret. We recommend you use a JSON structure of key/value pairs for your secret value. </p> <p>Either <code>SecretBinary</code> or <code>SecretString</code> must have a value, but not both. </p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>
            type: <p>The exact string that identifies the third-party partner that holds the external secret. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html">Managed external secret partners</a>.</p>

        Raises:
            capo_secrets_manager.errors.decryption_failure.DecryptionFailure: <p>Secrets Manager can't decrypt the protected secret text using the provided KMS key. </p>
            capo_secrets_manager.errors.encryption_failure.EncryptionFailure: <p>Secrets Manager can't encrypt the protected secret text using the provided KMS key. Check that the KMS key is available, enabled, and not in an invalid state. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">Key state: Effect on your KMS key</a>.</p>
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.limit_exceeded_exception.LimitExceededException: <p>The request failed because it would exceed one of the Secrets Manager quotas.</p>
            capo_secrets_manager.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>The resource policy has syntax errors.</p>
            capo_secrets_manager.errors.precondition_not_met_exception.PreconditionNotMetException: <p>The request failed because you did not complete all the prerequisite steps.</p>
            capo_secrets_manager.errors.resource_exists_exception.ResourceExistsException: <p>A resource with the ID you requested already exists.</p>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new version of the encrypted secret value
            The following example shows how to create a new version of the secret by updating the SecretString field. Alternatively, you can use the put-secret-value operation.

            >>> client.update_secret(secret_id='MyTestDatabaseSecret', secret_string='{JSON STRING WITH CREDENTIALS}')
            To update the description of a secret
            The following example shows how to modify the description of a secret.

            >>> client.update_secret(secret_id='MyTestDatabaseSecret', description='This is a new description for the secret.', client_request_token='EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE')
            To update the KMS key associated with a secret
            This example shows how to update the KMS customer managed key (CMK) used to encrypt the secret value. The KMS CMK must be in the same region as the secret.

            >>> client.update_secret(secret_id='MyTestDatabaseSecret', kms_key_id='arn:aws:kms:us-west-2:123456789012:key/EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.update_secret_request.UpdateSecretRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.update_secret_response.UpdateSecretResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.update_secret

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.update_secret.update_secret(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.update_secret_request.UpdateSecretRequest = {
            "secret_id": secret_id
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if description is not None:
            input_["description"] = description
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if secret_binary is not None:
            input_["secret_binary"] = secret_binary
        if secret_string is not None:
            input_["secret_string"] = secret_string
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_secret_version_stage(
        self,
        secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType",
        version_stage: "capo_secrets_manager.types.secret_version_stage_type.SecretVersionStageType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        remove_from_version_id: Optional[
            "capo_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
        ] = None,
        move_to_version_id: Optional[
            "capo_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
        ] = None,
    ) -> "capo_secrets_manager.types.update_secret_version_stage_response.UpdateSecretVersionStageResponse":
        """<p>Modifies the staging labels attached to a version of a secret. Secrets Manager uses staging labels to track a version as it progresses through the secret rotation process. Each staging label can be attached to only one version at a time. To add a staging label to a version when it is already attached to another version, Secrets Manager first removes it from the other version first and then attaches it to this one. For more information about versions and staging labels, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version">Concepts: Version</a>. </p> <p>The staging labels that you specify in the <code>VersionStage</code> parameter are added to the existing list of staging labels for the version. </p> <p>You can move the <code>AWSCURRENT</code> staging label to this version by including it in this call.</p> <note> <p>Whenever you move <code>AWSCURRENT</code>, Secrets Manager automatically moves the label <code>AWSPREVIOUS</code> to the version that <code>AWSCURRENT</code> was removed from.</p> </note> <p>If this action results in the last label being removed from a version, then the version is considered to be 'deprecated' and can be deleted by Secrets Manager.</p> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:UpdateSecretVersionStage</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or the name of the secret with the version and staging labelsto modify.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>
            version_stage: <p>The staging label to add to this version.</p>
            remove_from_version_id: <p>The ID of the version that the staging label is to be removed from. If the staging label you are trying to attach to one version is already attached to a different version, then you must include this parameter and specify the version that the label is to be removed from. If the label is attached and you either do not specify this parameter, or the version ID does not match, then the operation fails.</p>
            move_to_version_id: <p>The ID of the version to add the staging label to. To remove a label from a version, then do not specify this parameter.</p> <p>If the staging label is already attached to a different version of the secret, then you must also specify the <code>RemoveFromVersionId</code> parameter. </p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.limit_exceeded_exception.LimitExceededException: <p>The request failed because it would exceed one of the Secrets Manager quotas.</p>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add a staging label attached to a version of a secret
            The following example shows you how to add a staging label to a version of a secret. You can review the results by running the operation ListSecretVersionIds and viewing the VersionStages response field for the affected version.

            >>> client.update_secret_version_stage(secret_id='MyTestDatabaseSecret', version_stage='STAGINGLABEL1', move_to_version_id='EXAMPLE1-90ab-cdef-fedc-ba987SECRET1')
            To delete a staging label attached to a version of a secret
            The following example shows you how to delete a staging label that is attached to a version of a secret. You can review the results by running the operation ListSecretVersionIds and viewing the VersionStages response field for the affected version.

            >>> client.update_secret_version_stage(secret_id='MyTestDatabaseSecret', version_stage='STAGINGLABEL1', remove_from_version_id='EXAMPLE1-90ab-cdef-fedc-ba987SECRET1')
            To move a staging label from one version of a secret to another
            The following example shows you how to move a staging label that is attached to one version of a secret to a different version. You can review the results by running the operation ListSecretVersionIds and viewing the VersionStages response field for the affected version.

            >>> client.update_secret_version_stage(secret_id='MyTestDatabaseSecret', version_stage='AWSCURRENT', remove_from_version_id='EXAMPLE1-90ab-cdef-fedc-ba987SECRET1', move_to_version_id='EXAMPLE2-90ab-cdef-fedc-ba987SECRET2')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.update_secret_version_stage_request.UpdateSecretVersionStageRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.update_secret_version_stage_response.UpdateSecretVersionStageResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.update_secret_version_stage

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.update_secret_version_stage.update_secret_version_stage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.update_secret_version_stage_request.UpdateSecretVersionStageRequest = {
            "secret_id": secret_id,
            "version_stage": version_stage,
        }
        if remove_from_version_id is not None:
            input_["remove_from_version_id"] = remove_from_version_id
        if move_to_version_id is not None:
            input_["move_to_version_id"] = move_to_version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def validate_resource_policy(
        self,
        resource_policy: "capo_secrets_manager.types.non_empty_resource_policy_type.NonEmptyResourcePolicyType",
        *,
        config_overrides: Optional[SecretsManagerClientConfig] = None,
        secret_id: Optional[
            "capo_secrets_manager.types.secret_id_type.SecretIdType"
        ] = None,
    ) -> "capo_secrets_manager.types.validate_resource_policy_response.ValidateResourcePolicyResponse":
        r"""<p>Validates that a resource policy does not grant a wide range of principals access to your secret. A resource-based policy is optional for secrets.</p> <p>The API performs three checks when validating the policy:</p> <ul> <li> <p>Sends a call to <a href="https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/">Zelkova</a>, an automated reasoning engine, to ensure your resource policy does not allow broad access to your secret, for example policies that use a wildcard for the principal.</p> </li> <li> <p>Checks for correct syntax in a policy.</p> </li> <li> <p>Verifies the policy does not lock out a caller.</p> </li> </ul> <p>Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html">Logging Secrets Manager events with CloudTrail</a>.</p> <p> <b>Required permissions: </b> <code>secretsmanager:ValidateResourcePolicy</code> and <code>secretsmanager:PutResourcePolicy</code>. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions"> IAM policy actions for Secrets Manager</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control in Secrets Manager</a>. </p>

        Args:
            secret_id: <p>The ARN or name of the secret with the resource-based policy you want to validate.</p>
            resource_policy: <p>A JSON-formatted string that contains an Amazon Web Services resource-based policy. The policy in the string identifies who can access or manage this secret and its versions. For example policies, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html">Permissions policy examples</a>.</p>

        Raises:
            capo_secrets_manager.errors.internal_service_error.InternalServiceError: <p>An error occurred on the server side.</p>
            capo_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException: <p>The parameter name or value is invalid.</p>
            capo_secrets_manager.errors.invalid_request_exception.InvalidRequestException: <p>A parameter value is not valid for the current state of the resource.</p> <p>Possible causes:</p> <ul> <li> <p>The secret is scheduled for deletion.</p> </li> <li> <p>You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call. </p> </li> <li> <p>The secret is managed by another service, and you must use that service to update it. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p> </li> </ul>
            capo_secrets_manager.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>The resource policy has syntax errors.</p>
            capo_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Secrets Manager can't find the resource that you asked for.</p>
            capo_secrets_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To validate a resource-based policy to a secret
            The following example shows how to validate a resource-based policy to a secret.

            >>> client.validate_resource_policy(secret_id='MyTestDatabaseSecret', resource_policy='{\n"Version":"2012-10-17",\n"Statement":[{\n"Effect":"Allow",\n"Principal":{\n"AWS":"arn:aws:iam::123456789012:root"\n},\n"Action":"secretsmanager:GetSecretValue",\n"Resource":"*"\n}]\n}')
        """

        def _handler(
            req: "OperationRequest[capo_secrets_manager.types.validate_resource_policy_request.ValidateResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_secrets_manager.types.validate_resource_policy_response.ValidateResourcePolicyResponse"
        ]:
            import capo_secrets_manager._operations.secretsmanager.validate_resource_policy

            output, http_response = (
                capo_secrets_manager._operations.secretsmanager.validate_resource_policy.validate_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_secrets_manager.types.validate_resource_policy_request.ValidateResourcePolicyRequest = {
            "resource_policy": resource_policy
        }
        if secret_id is not None:
            input_["secret_id"] = secret_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
