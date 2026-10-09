"""Generated from Smithy shape ``com.amazonaws.finspacedata#AWSHabaneroPublicAPI``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_finspace_data._auth._signers
import capo_finspace_data._auth._sigv4
from capo_finspace_data._auth._identity import Credentials
from capo_finspace_data._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_finspace_data._auth._zapros_handler import AuthMiddleware
from capo_finspace_data._pagination import resolve_path as _resolve_path
from capo_finspace_data._services._aws_config import aws_config
from capo_finspace_data._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_finspace_data.types.alias_string
    import capo_finspace_data.types.api_access
    import capo_finspace_data.types.application_permission_list
    import capo_finspace_data.types.associate_user_to_permission_group_request
    import capo_finspace_data.types.associate_user_to_permission_group_response
    import capo_finspace_data.types.boolean
    import capo_finspace_data.types.change_type
    import capo_finspace_data.types.changeset_id
    import capo_finspace_data.types.changeset_summary
    import capo_finspace_data.types.client_token
    import capo_finspace_data.types.create_changeset_request
    import capo_finspace_data.types.create_changeset_response
    import capo_finspace_data.types.create_data_view_request
    import capo_finspace_data.types.create_data_view_response
    import capo_finspace_data.types.create_dataset_request
    import capo_finspace_data.types.create_dataset_response
    import capo_finspace_data.types.create_permission_group_request
    import capo_finspace_data.types.create_permission_group_response
    import capo_finspace_data.types.create_user_request
    import capo_finspace_data.types.create_user_response
    import capo_finspace_data.types.data_view_destination_type_params
    import capo_finspace_data.types.data_view_id
    import capo_finspace_data.types.data_view_summary
    import capo_finspace_data.types.dataset
    import capo_finspace_data.types.dataset_description
    import capo_finspace_data.types.dataset_id
    import capo_finspace_data.types.dataset_kind
    import capo_finspace_data.types.dataset_owner_info
    import capo_finspace_data.types.dataset_title
    import capo_finspace_data.types.delete_dataset_request
    import capo_finspace_data.types.delete_dataset_response
    import capo_finspace_data.types.delete_permission_group_request
    import capo_finspace_data.types.delete_permission_group_response
    import capo_finspace_data.types.disable_user_request
    import capo_finspace_data.types.disable_user_response
    import capo_finspace_data.types.disassociate_user_from_permission_group_request
    import capo_finspace_data.types.disassociate_user_from_permission_group_response
    import capo_finspace_data.types.email
    import capo_finspace_data.types.enable_user_request
    import capo_finspace_data.types.enable_user_response
    import capo_finspace_data.types.first_name
    import capo_finspace_data.types.format_params
    import capo_finspace_data.types.get_changeset_request
    import capo_finspace_data.types.get_changeset_response
    import capo_finspace_data.types.get_data_view_request
    import capo_finspace_data.types.get_data_view_response
    import capo_finspace_data.types.get_dataset_request
    import capo_finspace_data.types.get_dataset_response
    import capo_finspace_data.types.get_external_data_view_access_details_request
    import capo_finspace_data.types.get_external_data_view_access_details_response
    import capo_finspace_data.types.get_permission_group_request
    import capo_finspace_data.types.get_permission_group_response
    import capo_finspace_data.types.get_programmatic_access_credentials_request
    import capo_finspace_data.types.get_programmatic_access_credentials_response
    import capo_finspace_data.types.get_user_request
    import capo_finspace_data.types.get_user_response
    import capo_finspace_data.types.get_working_location_request
    import capo_finspace_data.types.get_working_location_response
    import capo_finspace_data.types.id_type
    import capo_finspace_data.types.last_name
    import capo_finspace_data.types.list_changesets_request
    import capo_finspace_data.types.list_changesets_response
    import capo_finspace_data.types.list_data_views_request
    import capo_finspace_data.types.list_data_views_response
    import capo_finspace_data.types.list_datasets_request
    import capo_finspace_data.types.list_datasets_response
    import capo_finspace_data.types.list_permission_groups_by_user_request
    import capo_finspace_data.types.list_permission_groups_by_user_response
    import capo_finspace_data.types.list_permission_groups_request
    import capo_finspace_data.types.list_permission_groups_response
    import capo_finspace_data.types.list_users_by_permission_group_request
    import capo_finspace_data.types.list_users_by_permission_group_response
    import capo_finspace_data.types.list_users_request
    import capo_finspace_data.types.list_users_response
    import capo_finspace_data.types.location_type
    import capo_finspace_data.types.pagination_token
    import capo_finspace_data.types.partition_column_list
    import capo_finspace_data.types.permission_group
    import capo_finspace_data.types.permission_group_description
    import capo_finspace_data.types.permission_group_id
    import capo_finspace_data.types.permission_group_name
    import capo_finspace_data.types.permission_group_params
    import capo_finspace_data.types.reset_user_password_request
    import capo_finspace_data.types.reset_user_password_response
    import capo_finspace_data.types.result_limit
    import capo_finspace_data.types.role_arn
    import capo_finspace_data.types.schema_union
    import capo_finspace_data.types.session_duration
    import capo_finspace_data.types.sort_column_list
    import capo_finspace_data.types.source_params
    import capo_finspace_data.types.string_value_length1to255
    import capo_finspace_data.types.timestamp_epoch
    import capo_finspace_data.types.update_changeset_request
    import capo_finspace_data.types.update_changeset_response
    import capo_finspace_data.types.update_dataset_request
    import capo_finspace_data.types.update_dataset_response
    import capo_finspace_data.types.update_permission_group_request
    import capo_finspace_data.types.update_permission_group_response
    import capo_finspace_data.types.update_user_request
    import capo_finspace_data.types.update_user_response
    import capo_finspace_data.types.user
    import capo_finspace_data.types.user_id
    import capo_finspace_data.types.user_type


class finspacedataClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class finspacedataClient:
    """A client for the ``finspacedata`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
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
        anonymous: bool | None = None,
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
        self._config = finspacedataClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[finspacedataClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: finspacedataClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def associate_user_to_permission_group(
        self,
        permission_group_id: "capo_finspace_data.types.permission_group_id.PermissionGroupId",
        user_id: "capo_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.associate_user_to_permission_group_response.AssociateUserToPermissionGroupResponse":
        """<p>Adds a user to a permission group to grant permissions for actions a user can perform in FinSpace.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group.</p>
            user_id: <p>The unique identifier for the user.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.associate_user_to_permission_group_request.AssociateUserToPermissionGroupRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.associate_user_to_permission_group_response.AssociateUserToPermissionGroupResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.associate_user_to_permission_group

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.associate_user_to_permission_group.associate_user_to_permission_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.associate_user_to_permission_group_request.AssociateUserToPermissionGroupRequest = {
            "permission_group_id": permission_group_id,
            "user_id": user_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_changeset(
        self,
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        change_type: "capo_finspace_data.types.change_type.ChangeType",
        source_params: "capo_finspace_data.types.source_params.SourceParams",
        format_params: "capo_finspace_data.types.format_params.FormatParams",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.create_changeset_response.CreateChangesetResponse":
        """<p>Creates a new Changeset in a FinSpace Dataset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_id: <p>The unique identifier for the FinSpace Dataset where the Changeset will be created. </p>
            change_type: <p>The option to indicate how a Changeset will be applied to a Dataset.</p> <ul> <li> <p> <code>REPLACE</code> – Changeset will be considered as a replacement to all prior loaded Changesets.</p> </li> <li> <p> <code>APPEND</code> – Changeset will be considered as an addition to the end of all prior loaded Changesets.</p> </li> <li> <p> <code>MODIFY</code> – Changeset is considered as a replacement to a specific prior ingested Changeset.</p> </li> </ul>
            source_params: <p>Options that define the location of the data being ingested (<code>s3SourcePath</code>) and the source of the changeset (<code>sourceType</code>).</p> <p>Both <code>s3SourcePath</code> and <code>sourceType</code> are required attributes.</p> <p>Here is an example of how you could specify the <code>sourceParams</code>:</p> <p> <code> "sourceParams": { "s3SourcePath": "s3://finspace-landing-us-east-2-bk7gcfvitndqa6ebnvys4d/scratch/wr5hh8pwkpqqkxa4sxrmcw/ingestion/equity.csv", "sourceType": "S3" } </code> </p> <p>The S3 path that you specify must allow the FinSpace role access. To do that, you first need to configure the IAM policy on S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html#access-s3-buckets">Loading data from an Amazon S3 Bucket using the FinSpace API</a> section.</p>
            format_params: <p>Options that define the structure of the source file(s) including the format type (<code>formatType</code>), header row (<code>withHeader</code>), data separation character (<code>separator</code>) and the type of compression (<code>compression</code>). </p> <p> <code>formatType</code> is a required attribute and can have the following values: </p> <ul> <li> <p> <code>PARQUET</code> – Parquet source file format.</p> </li> <li> <p> <code>CSV</code> – CSV source file format.</p> </li> <li> <p> <code>JSON</code> – JSON source file format.</p> </li> <li> <p> <code>XML</code> – XML source file format.</p> </li> </ul> <p>Here is an example of how you could specify the <code>formatParams</code>:</p> <p> <code> "formatParams": { "formatType": "CSV", "withHeader": "true", "separator": ",", "compression":"None" } </code> </p> <p>Note that if you only provide <code>formatType</code> as <code>CSV</code>, the rest of the attributes will automatically default to CSV values as following:</p> <p> <code> { "withHeader": "true", "separator": "," } </code> </p> <p> For more information about supported file formats, see <a href="https://docs.aws.amazon.com/finspace/latest/userguide/supported-data-types.html">Supported Data Types and File Formats</a> in the FinSpace User Guide.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.limit_exceeded_exception.LimitExceededException: <p>A limit has exceeded.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.create_changeset_request.CreateChangesetRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.create_changeset_response.CreateChangesetResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.create_changeset

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.create_changeset.create_changeset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.create_changeset_request.CreateChangesetRequest = {
            "dataset_id": dataset_id,
            "change_type": change_type,
            "source_params": source_params,
            "format_params": format_params,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_dataset(
        self,
        dataset_title: "capo_finspace_data.types.dataset_title.DatasetTitle",
        kind: "capo_finspace_data.types.dataset_kind.DatasetKind",
        permission_group_params: "capo_finspace_data.types.permission_group_params.PermissionGroupParams",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
        dataset_description: Optional[
            "capo_finspace_data.types.dataset_description.DatasetDescription"
        ] = None,
        owner_info: Optional[
            "capo_finspace_data.types.dataset_owner_info.DatasetOwnerInfo"
        ] = None,
        alias: Optional["capo_finspace_data.types.alias_string.AliasString"] = None,
        schema_definition: Optional[
            "capo_finspace_data.types.schema_union.SchemaUnion"
        ] = None,
    ) -> "capo_finspace_data.types.create_dataset_response.CreateDatasetResponse":
        """<p>Creates a new FinSpace Dataset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_title: <p>Display title for a FinSpace Dataset.</p>
            kind: <p>The format in which Dataset data is structured.</p> <ul> <li> <p> <code>TABULAR</code> – Data is structured in a tabular format.</p> </li> <li> <p> <code>NON_TABULAR</code> – Data is structured in a non-tabular format.</p> </li> </ul>
            dataset_description: <p>Description of a Dataset.</p>
            owner_info: <p>Contact information for a Dataset owner.</p>
            permission_group_params: <p>Permission group parameters for Dataset permissions.</p>
            alias: <p>The unique resource identifier for a Dataset.</p>
            schema_definition: <p>Definition for a schema on a tabular Dataset.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.limit_exceeded_exception.LimitExceededException: <p>A limit has exceeded.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.create_dataset_request.CreateDatasetRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.create_dataset

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.create_dataset.create_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.create_dataset_request.CreateDatasetRequest = {
            "dataset_title": dataset_title,
            "kind": kind,
            "permission_group_params": permission_group_params,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if dataset_description is not None:
            input_["dataset_description"] = dataset_description
        if owner_info is not None:
            input_["owner_info"] = owner_info
        if alias is not None:
            input_["alias"] = alias
        if schema_definition is not None:
            input_["schema_definition"] = schema_definition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_view(
        self,
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        destination_type_params: "capo_finspace_data.types.data_view_destination_type_params.DataViewDestinationTypeParams",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
        auto_update: Optional["capo_finspace_data.types.boolean.Boolean"] = None,
        sort_columns: Optional[
            "capo_finspace_data.types.sort_column_list.SortColumnList"
        ] = None,
        partition_columns: Optional[
            "capo_finspace_data.types.partition_column_list.PartitionColumnList"
        ] = None,
        as_of_timestamp: Optional[
            "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
        ] = None,
    ) -> "capo_finspace_data.types.create_data_view_response.CreateDataViewResponse":
        """<p>Creates a Dataview for a Dataset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_id: <p>The unique Dataset identifier that is used to create a Dataview.</p>
            auto_update: <p>Flag to indicate Dataview should be updated automatically.</p>
            sort_columns: <p>Columns to be used for sorting the data.</p>
            partition_columns: <p>Ordered set of column names used to partition data.</p>
            as_of_timestamp: <p>Beginning time to use for the Dataview. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>
            destination_type_params: <p>Options that define the destination type for the Dataview.</p>

        Raises:
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.limit_exceeded_exception.LimitExceededException: <p>A limit has exceeded.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.create_data_view_request.CreateDataViewRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.create_data_view_response.CreateDataViewResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.create_data_view

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.create_data_view.create_data_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.create_data_view_request.CreateDataViewRequest = {
            "dataset_id": dataset_id,
            "destination_type_params": destination_type_params,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if auto_update is not None:
            input_["auto_update"] = auto_update
        if sort_columns is not None:
            input_["sort_columns"] = sort_columns
        if partition_columns is not None:
            input_["partition_columns"] = partition_columns
        if as_of_timestamp is not None:
            input_["as_of_timestamp"] = as_of_timestamp

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_permission_group(
        self,
        name: "capo_finspace_data.types.permission_group_name.PermissionGroupName",
        application_permissions: "capo_finspace_data.types.application_permission_list.ApplicationPermissionList",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        description: Optional[
            "capo_finspace_data.types.permission_group_description.PermissionGroupDescription"
        ] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.create_permission_group_response.CreatePermissionGroupResponse":
        """<p>Creates a group of permissions for various actions that a user can perform in FinSpace.</p>

        Args:
            name: <p>The name of the permission group.</p>
            description: <p>A brief description for the permission group.</p>
            application_permissions: <p>The option to indicate FinSpace application permissions that are granted to a specific group.</p> <important> <p>When assigning application permissions, be aware that the permission <code>ManageUsersAndGroups</code> allows users to grant themselves or others access to any functionality in their FinSpace environment's application. It should only be granted to trusted users.</p> </important> <ul> <li> <p> <code>CreateDataset</code> – Group members can create new datasets.</p> </li> <li> <p> <code>ManageClusters</code> – Group members can manage Apache Spark clusters from FinSpace notebooks.</p> </li> <li> <p> <code>ManageUsersAndGroups</code> – Group members can manage users and permission groups. This is a privileged permission that allows users to grant themselves or others access to any functionality in the application. It should only be granted to trusted users.</p> </li> <li> <p> <code>ManageAttributeSets</code> – Group members can manage attribute sets.</p> </li> <li> <p> <code>ViewAuditData</code> – Group members can view audit data.</p> </li> <li> <p> <code>AccessNotebooks</code> – Group members will have access to FinSpace notebooks.</p> </li> <li> <p> <code>GetTemporaryCredentials</code> – Group members can get temporary API credentials.</p> </li> </ul>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.limit_exceeded_exception.LimitExceededException: <p>A limit has exceeded.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.create_permission_group_request.CreatePermissionGroupRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.create_permission_group_response.CreatePermissionGroupResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.create_permission_group

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.create_permission_group.create_permission_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.create_permission_group_request.CreatePermissionGroupRequest = {
            "name": name,
            "application_permissions": application_permissions,
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_user(
        self,
        email_address: "capo_finspace_data.types.email.Email",
        type: "capo_finspace_data.types.user_type.UserType",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        first_name: Optional["capo_finspace_data.types.first_name.FirstName"] = None,
        last_name: Optional["capo_finspace_data.types.last_name.LastName"] = None,
        api_access: Optional["capo_finspace_data.types.api_access.ApiAccess"] = None,
        api_access_principal_arn: Optional[
            "capo_finspace_data.types.role_arn.RoleArn"
        ] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.create_user_response.CreateUserResponse":
        """<p>Creates a new user in FinSpace.</p>

        Args:
            email_address: <p>The email address of the user that you want to register. The email address serves as a uniquer identifier for each user and cannot be changed after it's created.</p>
            type: <p>The option to indicate the type of user. Use one of the following options to specify this parameter:</p> <ul> <li> <p> <code>SUPER_USER</code> – A user with permission to all the functionality and data in FinSpace.</p> </li> <li> <p> <code>APP_USER</code> – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.</p> </li> </ul>
            first_name: <p>The first name of the user that you want to register.</p>
            last_name: <p>The last name of the user that you want to register.</p>
            api_access: <p>The option to indicate whether the user can use the <code>GetProgrammaticAccessCredentials</code> API to obtain credentials that can then be used to access other FinSpace Data API operations.</p> <ul> <li> <p> <code>ENABLED</code> – The user has permissions to use the APIs.</p> </li> <li> <p> <code>DISABLED</code> – The user does not have permissions to use any APIs.</p> </li> </ul>
            api_access_principal_arn: <p>The ARN identifier of an AWS user or role that is allowed to call the <code>GetProgrammaticAccessCredentials</code> API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.limit_exceeded_exception.LimitExceededException: <p>A limit has exceeded.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.create_user_response.CreateUserResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.create_user

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.create_user_request.CreateUserRequest = {
            "email_address": email_address,
            "type": type,
        }
        if first_name is not None:
            input_["first_name"] = first_name
        if last_name is not None:
            input_["last_name"] = last_name
        if api_access is not None:
            input_["api_access"] = api_access
        if api_access_principal_arn is not None:
            input_["api_access_principal_arn"] = api_access_principal_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_dataset(
        self,
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.delete_dataset_response.DeleteDatasetResponse":
        """<p>Deletes a FinSpace Dataset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_id: <p>The unique identifier of the Dataset to be deleted.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.limit_exceeded_exception.LimitExceededException: <p>A limit has exceeded.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.delete_dataset_response.DeleteDatasetResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.delete_dataset

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.delete_dataset.delete_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.delete_dataset_request.DeleteDatasetRequest = {
            "dataset_id": dataset_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_permission_group(
        self,
        permission_group_id: "capo_finspace_data.types.permission_group_id.PermissionGroupId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.delete_permission_group_response.DeletePermissionGroupResponse":
        """<p>Deletes a permission group. This action is irreversible.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group that you want to delete.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.limit_exceeded_exception.LimitExceededException: <p>A limit has exceeded.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.delete_permission_group_request.DeletePermissionGroupRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.delete_permission_group_response.DeletePermissionGroupResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.delete_permission_group

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.delete_permission_group.delete_permission_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.delete_permission_group_request.DeletePermissionGroupRequest = {
            "permission_group_id": permission_group_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_user(
        self,
        user_id: "capo_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.disable_user_response.DisableUserResponse":
        """<p>Denies access to the FinSpace web application and API for the specified user.</p>

        Args:
            user_id: <p>The unique identifier for the user that you want to deactivate.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.disable_user_request.DisableUserRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.disable_user_response.DisableUserResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.disable_user

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.disable_user.disable_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.disable_user_request.DisableUserRequest = {
            "user_id": user_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_user_from_permission_group(
        self,
        permission_group_id: "capo_finspace_data.types.permission_group_id.PermissionGroupId",
        user_id: "capo_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.disassociate_user_from_permission_group_response.DisassociateUserFromPermissionGroupResponse":
        """<p>Removes a user from a permission group.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group.</p>
            user_id: <p>The unique identifier for the user.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.disassociate_user_from_permission_group_request.DisassociateUserFromPermissionGroupRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.disassociate_user_from_permission_group_response.DisassociateUserFromPermissionGroupResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.disassociate_user_from_permission_group

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.disassociate_user_from_permission_group.disassociate_user_from_permission_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.disassociate_user_from_permission_group_request.DisassociateUserFromPermissionGroupRequest = {
            "permission_group_id": permission_group_id,
            "user_id": user_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_user(
        self,
        user_id: "capo_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.enable_user_response.EnableUserResponse":
        """<p> Allows the specified user to access the FinSpace web application and API.</p>

        Args:
            user_id: <p>The unique identifier for the user that you want to activate.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.limit_exceeded_exception.LimitExceededException: <p>A limit has exceeded.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.enable_user_request.EnableUserRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.enable_user_response.EnableUserResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.enable_user

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.enable_user.enable_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.enable_user_request.EnableUserRequest = {
            "user_id": user_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_changeset(
        self,
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        changeset_id: "capo_finspace_data.types.changeset_id.ChangesetId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
    ) -> "capo_finspace_data.types.get_changeset_response.GetChangesetResponse":
        """<p>Get information about a Changeset.</p>

        Args:
            dataset_id: <p>The unique identifier for the FinSpace Dataset where the Changeset is created.</p>
            changeset_id: <p>The unique identifier of the Changeset for which to get data.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.get_changeset_request.GetChangesetRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.get_changeset_response.GetChangesetResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.get_changeset

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.get_changeset.get_changeset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.get_changeset_request.GetChangesetRequest = {
            "dataset_id": dataset_id,
            "changeset_id": changeset_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_dataset(
        self,
        dataset_id: "capo_finspace_data.types.string_value_length1to255.StringValueLength1to255",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
    ) -> "capo_finspace_data.types.get_dataset_response.GetDatasetResponse":
        """<p>Returns information about a Dataset.</p>

        Args:
            dataset_id: <p>The unique identifier for a Dataset.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.get_dataset_request.GetDatasetRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.get_dataset_response.GetDatasetResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.get_dataset

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.get_dataset.get_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.get_dataset_request.GetDatasetRequest = {
            "dataset_id": dataset_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_view(
        self,
        data_view_id: "capo_finspace_data.types.data_view_id.DataViewId",
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
    ) -> "capo_finspace_data.types.get_data_view_response.GetDataViewResponse":
        """<p>Gets information about a Dataview.</p>

        Args:
            data_view_id: <p>The unique identifier for the Dataview.</p>
            dataset_id: <p>The unique identifier for the Dataset used in the Dataview.</p>

        Raises:
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.get_data_view_request.GetDataViewRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.get_data_view_response.GetDataViewResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.get_data_view

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.get_data_view.get_data_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.get_data_view_request.GetDataViewRequest = {
            "data_view_id": data_view_id,
            "dataset_id": dataset_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_external_data_view_access_details(
        self,
        data_view_id: "capo_finspace_data.types.data_view_id.DataViewId",
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
    ) -> "capo_finspace_data.types.get_external_data_view_access_details_response.GetExternalDataViewAccessDetailsResponse":
        """<p>Returns the credentials to access the external Dataview from an S3 location. To call this API:</p> <ul> <li> <p>You must retrieve the programmatic credentials.</p> </li> <li> <p>You must be a member of a FinSpace user group, where the dataset that you want to access has <code>Read Dataset Data</code> permissions.</p> </li> </ul>

        Args:
            data_view_id: <p>The unique identifier for the Dataview that you want to access.</p>
            dataset_id: <p>The unique identifier for the Dataset.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.get_external_data_view_access_details_request.GetExternalDataViewAccessDetailsRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.get_external_data_view_access_details_response.GetExternalDataViewAccessDetailsResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.get_external_data_view_access_details

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.get_external_data_view_access_details.get_external_data_view_access_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.get_external_data_view_access_details_request.GetExternalDataViewAccessDetailsRequest = {
            "data_view_id": data_view_id,
            "dataset_id": dataset_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_permission_group(
        self,
        permission_group_id: "capo_finspace_data.types.permission_group_id.PermissionGroupId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
    ) -> "capo_finspace_data.types.get_permission_group_response.GetPermissionGroupResponse":
        """<p>Retrieves the details of a specific permission group.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.get_permission_group_request.GetPermissionGroupRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.get_permission_group_response.GetPermissionGroupResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.get_permission_group

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.get_permission_group.get_permission_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.get_permission_group_request.GetPermissionGroupRequest = {
            "permission_group_id": permission_group_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_programmatic_access_credentials(
        self,
        environment_id: "capo_finspace_data.types.id_type.IdType",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        duration_in_minutes: Optional[
            "capo_finspace_data.types.session_duration.SessionDuration"
        ] = None,
    ) -> "capo_finspace_data.types.get_programmatic_access_credentials_response.GetProgrammaticAccessCredentialsResponse":
        """<p>Request programmatic credentials to use with FinSpace SDK. For more information, see <a href="https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html#accessing-credentials">Step 2. Access credentials programmatically using IAM access key id and secret access key</a>.</p>

        Args:
            duration_in_minutes: <p>The time duration in which the credentials remain valid. </p>
            environment_id: <p>The FinSpace environment identifier.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.get_programmatic_access_credentials_request.GetProgrammaticAccessCredentialsRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.get_programmatic_access_credentials_response.GetProgrammaticAccessCredentialsResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.get_programmatic_access_credentials

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.get_programmatic_access_credentials.get_programmatic_access_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.get_programmatic_access_credentials_request.GetProgrammaticAccessCredentialsRequest = {
            "environment_id": environment_id
        }
        if duration_in_minutes is not None:
            input_["duration_in_minutes"] = duration_in_minutes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_user(
        self,
        user_id: "capo_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
    ) -> "capo_finspace_data.types.get_user_response.GetUserResponse":
        """<p>Retrieves details for a specific user.</p>

        Args:
            user_id: <p>The unique identifier of the user to get data for.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.get_user_request.GetUserRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.get_user_response.GetUserResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.get_user

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.get_user.get_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.get_user_request.GetUserRequest = {
            "user_id": user_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_working_location(
        self,
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        location_type: Optional[
            "capo_finspace_data.types.location_type.locationType"
        ] = None,
    ) -> "capo_finspace_data.types.get_working_location_response.GetWorkingLocationResponse":
        """<p>A temporary Amazon S3 location, where you can copy your files from a source location to stage or use as a scratch space in FinSpace notebook.</p>

        Args:
            location_type: <p>Specify the type of the working location.</p> <ul> <li> <p> <code>SAGEMAKER</code> – Use the Amazon S3 location as a temporary location to store data content when working with FinSpace Notebooks that run on SageMaker studio.</p> </li> <li> <p> <code>INGESTION</code> – Use the Amazon S3 location as a staging location to copy your data content and then use the location with the Changeset creation operation.</p> </li> </ul>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.get_working_location_request.GetWorkingLocationRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.get_working_location_response.GetWorkingLocationResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.get_working_location

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.get_working_location.get_working_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.get_working_location_request.GetWorkingLocationRequest = {}
        if location_type is not None:
            input_["location_type"] = location_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_changesets(
        self,
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        max_results: Optional[
            "capo_finspace_data.types.result_limit.ResultLimit"
        ] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_finspace_data.types.list_changesets_response.ListChangesetsResponse":
        """<p>Lists the FinSpace Changesets for a Dataset.</p>

        Args:
            dataset_id: <p>The unique identifier for the FinSpace Dataset to which the Changeset belongs.</p>
            max_results: <p>The maximum number of results per page.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.list_changesets_request.ListChangesetsRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.list_changesets_response.ListChangesetsResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.list_changesets

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.list_changesets.list_changesets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.list_changesets_request.ListChangesetsRequest = {
            "dataset_id": dataset_id
        }
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

    def iter_list_changesets(
        self,
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        max_results: Optional[
            "capo_finspace_data.types.result_limit.ResultLimit"
        ] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_finspace_data.types.changeset_summary.ChangesetSummary]":
        _token = next_token
        while True:
            _response = self.list_changesets(
                dataset_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("changesets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_datasets(
        self,
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_finspace_data.types.result_limit.ResultLimit"
        ] = None,
    ) -> "capo_finspace_data.types.list_datasets_response.ListDatasetsResponse":
        """<p>Lists all of the active Datasets that a user has access to.</p>

        Args:
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>

        Raises:
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.list_datasets_request.ListDatasetsRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.list_datasets

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.list_datasets.list_datasets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.list_datasets_request.ListDatasetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_datasets(
        self,
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_finspace_data.types.result_limit.ResultLimit"
        ] = None,
    ) -> "Iterator[capo_finspace_data.types.dataset.Dataset]":
        _token = next_token
        while True:
            _response = self.list_datasets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("datasets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_views(
        self,
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_finspace_data.types.result_limit.ResultLimit"
        ] = None,
    ) -> "capo_finspace_data.types.list_data_views_response.ListDataViewsResponse":
        """<p>Lists all available Dataviews for a Dataset.</p>

        Args:
            dataset_id: <p>The unique identifier of the Dataset for which to retrieve Dataviews.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>

        Raises:
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.list_data_views_request.ListDataViewsRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.list_data_views_response.ListDataViewsResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.list_data_views

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.list_data_views.list_data_views(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.list_data_views_request.ListDataViewsRequest = {
            "dataset_id": dataset_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_data_views(
        self,
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_finspace_data.types.result_limit.ResultLimit"
        ] = None,
    ) -> "Iterator[capo_finspace_data.types.data_view_summary.DataViewSummary]":
        _token = next_token
        while True:
            _response = self.list_data_views(
                dataset_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_permission_groups(
        self,
        max_results: "capo_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_finspace_data.types.list_permission_groups_response.ListPermissionGroupsResponse":
        """<p>Lists all available permission groups in FinSpace.</p>

        Args:
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.list_permission_groups_request.ListPermissionGroupsRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.list_permission_groups_response.ListPermissionGroupsResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.list_permission_groups

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.list_permission_groups.list_permission_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.list_permission_groups_request.ListPermissionGroupsRequest = {
            "max_results": max_results
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_permission_groups(
        self,
        max_results: "capo_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_finspace_data.types.permission_group.PermissionGroup]":
        _token = next_token
        while True:
            _response = self.list_permission_groups(
                max_results,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("permission_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_permission_groups_by_user(
        self,
        user_id: "capo_finspace_data.types.user_id.UserId",
        max_results: "capo_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_finspace_data.types.list_permission_groups_by_user_response.ListPermissionGroupsByUserResponse":
        """<p>Lists all the permission groups that are associated with a specific user.</p>

        Args:
            user_id: <p>The unique identifier for the user.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.list_permission_groups_by_user_request.ListPermissionGroupsByUserRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.list_permission_groups_by_user_response.ListPermissionGroupsByUserResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.list_permission_groups_by_user

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.list_permission_groups_by_user.list_permission_groups_by_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.list_permission_groups_by_user_request.ListPermissionGroupsByUserRequest = {
            "user_id": user_id,
            "max_results": max_results,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_users(
        self,
        max_results: "capo_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_finspace_data.types.list_users_response.ListUsersResponse":
        """<p>Lists all available users in FinSpace.</p>

        Args:
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.list_users_request.ListUsersRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.list_users_response.ListUsersResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.list_users

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.list_users.list_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.list_users_request.ListUsersRequest = {
            "max_results": max_results
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_users(
        self,
        max_results: "capo_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_finspace_data.types.user.User]":
        _token = next_token
        while True:
            _response = self.list_users(
                max_results,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_users_by_permission_group(
        self,
        permission_group_id: "capo_finspace_data.types.permission_group_id.PermissionGroupId",
        max_results: "capo_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        next_token: Optional[
            "capo_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_finspace_data.types.list_users_by_permission_group_response.ListUsersByPermissionGroupResponse":
        """<p>Lists details of all the users in a specific permission group.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.list_users_by_permission_group_request.ListUsersByPermissionGroupRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.list_users_by_permission_group_response.ListUsersByPermissionGroupResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.list_users_by_permission_group

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.list_users_by_permission_group.list_users_by_permission_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.list_users_by_permission_group_request.ListUsersByPermissionGroupRequest = {
            "permission_group_id": permission_group_id,
            "max_results": max_results,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reset_user_password(
        self,
        user_id: "capo_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.reset_user_password_response.ResetUserPasswordResponse":
        """<p>Resets the password for a specified user ID and generates a temporary one. Only a superuser can reset password for other users. Resetting the password immediately invalidates the previous password associated with the user.</p>

        Args:
            user_id: <p>The unique identifier of the user that a temporary password is requested for.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.reset_user_password_request.ResetUserPasswordRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.reset_user_password_response.ResetUserPasswordResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.reset_user_password

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.reset_user_password.reset_user_password(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.reset_user_password_request.ResetUserPasswordRequest = {
            "user_id": user_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_changeset(
        self,
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        changeset_id: "capo_finspace_data.types.changeset_id.ChangesetId",
        source_params: "capo_finspace_data.types.source_params.SourceParams",
        format_params: "capo_finspace_data.types.format_params.FormatParams",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.update_changeset_response.UpdateChangesetResponse":
        """<p>Updates a FinSpace Changeset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_id: <p>The unique identifier for the FinSpace Dataset in which the Changeset is created.</p>
            changeset_id: <p>The unique identifier for the Changeset to update.</p>
            source_params: <p>Options that define the location of the data being ingested (<code>s3SourcePath</code>) and the source of the changeset (<code>sourceType</code>).</p> <p>Both <code>s3SourcePath</code> and <code>sourceType</code> are required attributes.</p> <p>Here is an example of how you could specify the <code>sourceParams</code>:</p> <p> <code> "sourceParams": { "s3SourcePath": "s3://finspace-landing-us-east-2-bk7gcfvitndqa6ebnvys4d/scratch/wr5hh8pwkpqqkxa4sxrmcw/ingestion/equity.csv", "sourceType": "S3" } </code> </p> <p>The S3 path that you specify must allow the FinSpace role access. To do that, you first need to configure the IAM policy on S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html#access-s3-buckets">Loading data from an Amazon S3 Bucket using the FinSpace API</a>section.</p>
            format_params: <p>Options that define the structure of the source file(s) including the format type (<code>formatType</code>), header row (<code>withHeader</code>), data separation character (<code>separator</code>) and the type of compression (<code>compression</code>). </p> <p> <code>formatType</code> is a required attribute and can have the following values: </p> <ul> <li> <p> <code>PARQUET</code> – Parquet source file format.</p> </li> <li> <p> <code>CSV</code> – CSV source file format.</p> </li> <li> <p> <code>JSON</code> – JSON source file format.</p> </li> <li> <p> <code>XML</code> – XML source file format.</p> </li> </ul> <p>Here is an example of how you could specify the <code>formatParams</code>:</p> <p> <code> "formatParams": { "formatType": "CSV", "withHeader": "true", "separator": ",", "compression":"None" } </code> </p> <p>Note that if you only provide <code>formatType</code> as <code>CSV</code>, the rest of the attributes will automatically default to CSV values as following:</p> <p> <code> { "withHeader": "true", "separator": "," } </code> </p> <p> For more information about supported file formats, see <a href="https://docs.aws.amazon.com/finspace/latest/userguide/supported-data-types.html">Supported Data Types and File Formats</a> in the FinSpace User Guide.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.update_changeset_request.UpdateChangesetRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.update_changeset_response.UpdateChangesetResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.update_changeset

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.update_changeset.update_changeset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.update_changeset_request.UpdateChangesetRequest = {
            "dataset_id": dataset_id,
            "changeset_id": changeset_id,
            "source_params": source_params,
            "format_params": format_params,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_dataset(
        self,
        dataset_id: "capo_finspace_data.types.dataset_id.DatasetId",
        dataset_title: "capo_finspace_data.types.dataset_title.DatasetTitle",
        kind: "capo_finspace_data.types.dataset_kind.DatasetKind",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
        dataset_description: Optional[
            "capo_finspace_data.types.dataset_description.DatasetDescription"
        ] = None,
        alias: Optional["capo_finspace_data.types.alias_string.AliasString"] = None,
        schema_definition: Optional[
            "capo_finspace_data.types.schema_union.SchemaUnion"
        ] = None,
    ) -> "capo_finspace_data.types.update_dataset_response.UpdateDatasetResponse":
        """<p>Updates a FinSpace Dataset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_id: <p>The unique identifier for the Dataset to update.</p>
            dataset_title: <p>A display title for the Dataset.</p>
            kind: <p>The format in which the Dataset data is structured.</p> <ul> <li> <p> <code>TABULAR</code> – Data is structured in a tabular format.</p> </li> <li> <p> <code>NON_TABULAR</code> – Data is structured in a non-tabular format.</p> </li> </ul>
            dataset_description: <p>A description for the Dataset.</p>
            alias: <p>The unique resource identifier for a Dataset.</p>
            schema_definition: <p>Definition for a schema on a tabular Dataset.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.update_dataset_request.UpdateDatasetRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.update_dataset_response.UpdateDatasetResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.update_dataset

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.update_dataset.update_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.update_dataset_request.UpdateDatasetRequest = {
            "dataset_id": dataset_id,
            "dataset_title": dataset_title,
            "kind": kind,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if dataset_description is not None:
            input_["dataset_description"] = dataset_description
        if alias is not None:
            input_["alias"] = alias
        if schema_definition is not None:
            input_["schema_definition"] = schema_definition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_permission_group(
        self,
        permission_group_id: "capo_finspace_data.types.permission_group_id.PermissionGroupId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        name: Optional[
            "capo_finspace_data.types.permission_group_name.PermissionGroupName"
        ] = None,
        description: Optional[
            "capo_finspace_data.types.permission_group_description.PermissionGroupDescription"
        ] = None,
        application_permissions: Optional[
            "capo_finspace_data.types.application_permission_list.ApplicationPermissionList"
        ] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.update_permission_group_response.UpdatePermissionGroupResponse":
        """<p>Modifies the details of a permission group. You cannot modify a <code>permissionGroupID</code>.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group to update.</p>
            name: <p>The name of the permission group.</p>
            description: <p>A brief description for the permission group.</p>
            application_permissions: <p>The permissions that are granted to a specific group for accessing the FinSpace application.</p> <important> <p>When assigning application permissions, be aware that the permission <code>ManageUsersAndGroups</code> allows users to grant themselves or others access to any functionality in their FinSpace environment's application. It should only be granted to trusted users.</p> </important> <ul> <li> <p> <code>CreateDataset</code> – Group members can create new datasets.</p> </li> <li> <p> <code>ManageClusters</code> – Group members can manage Apache Spark clusters from FinSpace notebooks.</p> </li> <li> <p> <code>ManageUsersAndGroups</code> – Group members can manage users and permission groups. This is a privileged permission that allows users to grant themselves or others access to any functionality in the application. It should only be granted to trusted users.</p> </li> <li> <p> <code>ManageAttributeSets</code> – Group members can manage attribute sets.</p> </li> <li> <p> <code>ViewAuditData</code> – Group members can view audit data.</p> </li> <li> <p> <code>AccessNotebooks</code> – Group members will have access to FinSpace notebooks.</p> </li> <li> <p> <code>GetTemporaryCredentials</code> – Group members can get temporary API credentials.</p> </li> </ul>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.update_permission_group_request.UpdatePermissionGroupRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.update_permission_group_response.UpdatePermissionGroupResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.update_permission_group

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.update_permission_group.update_permission_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.update_permission_group_request.UpdatePermissionGroupRequest = {
            "permission_group_id": permission_group_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if application_permissions is not None:
            input_["application_permissions"] = application_permissions
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_user(
        self,
        user_id: "capo_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[finspacedataClientConfig] = None,
        type: Optional["capo_finspace_data.types.user_type.UserType"] = None,
        first_name: Optional["capo_finspace_data.types.first_name.FirstName"] = None,
        last_name: Optional["capo_finspace_data.types.last_name.LastName"] = None,
        api_access: Optional["capo_finspace_data.types.api_access.ApiAccess"] = None,
        api_access_principal_arn: Optional[
            "capo_finspace_data.types.role_arn.RoleArn"
        ] = None,
        client_token: Optional[
            "capo_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_finspace_data.types.update_user_response.UpdateUserResponse":
        """<p>Modifies the details of the specified user. You cannot update the <code>userId</code> for a user.</p>

        Args:
            user_id: <p>The unique identifier for the user that you want to update.</p>
            type: <p>The option to indicate the type of user.</p> <ul> <li> <p> <code>SUPER_USER</code>– A user with permission to all the functionality and data in FinSpace.</p> </li> <li> <p> <code>APP_USER</code> – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.</p> </li> </ul>
            first_name: <p>The first name of the user.</p>
            last_name: <p>The last name of the user.</p>
            api_access: <p>The option to indicate whether the user can use the <code>GetProgrammaticAccessCredentials</code> API to obtain credentials that can then be used to access other FinSpace Data API operations.</p> <ul> <li> <p> <code>ENABLED</code> – The user has permissions to use the APIs.</p> </li> <li> <p> <code>DISABLED</code> – The user does not have permissions to use any APIs.</p> </li> </ul>
            api_access_principal_arn: <p>The ARN identifier of an AWS user or role that is allowed to call the <code>GetProgrammaticAccessCredentials</code> API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace_data.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource.</p>
            capo_finspace_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace_data.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace_data.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "capo_finspace_data.types.update_user_response.UpdateUserResponse"
        ]:
            import capo_finspace_data._operations.aws_habanero_public_api.update_user

            output, http_response = (
                capo_finspace_data._operations.aws_habanero_public_api.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace_data.types.update_user_request.UpdateUserRequest = {
            "user_id": user_id
        }
        if type is not None:
            input_["type"] = type
        if first_name is not None:
            input_["first_name"] = first_name
        if last_name is not None:
            input_["last_name"] = last_name
        if api_access is not None:
            input_["api_access"] = api_access
        if api_access_principal_arn is not None:
            input_["api_access_principal_arn"] = api_access_principal_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

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
