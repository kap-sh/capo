from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from capo_redshift_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_redshift_serverless.types.catalog_name_string
    import capo_redshift_serverless.types.create_namespace_request
    import capo_redshift_serverless.types.create_namespace_response
    import capo_redshift_serverless.types.db_password
    import capo_redshift_serverless.types.db_user
    import capo_redshift_serverless.types.delete_namespace_request
    import capo_redshift_serverless.types.delete_namespace_response
    import capo_redshift_serverless.types.get_namespace_request
    import capo_redshift_serverless.types.get_namespace_response
    import capo_redshift_serverless.types.iam_role_arn_list
    import capo_redshift_serverless.types.kms_key_id
    import capo_redshift_serverless.types.lakehouse_idc_registration
    import capo_redshift_serverless.types.lakehouse_registration
    import capo_redshift_serverless.types.list_namespaces_request
    import capo_redshift_serverless.types.list_namespaces_response
    import capo_redshift_serverless.types.log_destination_type
    import capo_redshift_serverless.types.log_export_list
    import capo_redshift_serverless.types.namespace
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.redshift_idc_application_arn
    import capo_redshift_serverless.types.s3_table_action
    import capo_redshift_serverless.types.s3_table_granularity
    import capo_redshift_serverless.types.s3_table_name_list
    import capo_redshift_serverless.types.tag_list
    import capo_redshift_serverless.types.update_lakehouse_configuration_request
    import capo_redshift_serverless.types.update_lakehouse_configuration_response
    import capo_redshift_serverless.types.update_namespace_request
    import capo_redshift_serverless.types.update_namespace_response
    from capo_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from capo_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class NamespaceResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def put(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        admin_username: Optional[
            "capo_redshift_serverless.types.db_user.DbUser"
        ] = None,
        admin_user_password: Optional[
            "capo_redshift_serverless.types.db_password.DbPassword"
        ] = None,
        db_name: Optional[str] = None,
        kms_key_id: Optional[str] = None,
        default_iam_role_arn: Optional[str] = None,
        iam_roles: Optional[
            "capo_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        log_exports: Optional[
            "capo_redshift_serverless.types.log_export_list.LogExportList"
        ] = None,
        tags: Optional["capo_redshift_serverless.types.tag_list.TagList"] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        redshift_idc_application_arn: Optional[
            "capo_redshift_serverless.types.redshift_idc_application_arn.RedshiftIdcApplicationArn"
        ] = None,
    ) -> "capo_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse":
        """<p>Creates a namespace in Amazon Redshift Serverless.</p>

        Args:
            namespace_name: <p>The name of the namespace.</p>
            admin_username: <p>The username of the administrator for the first database created in the namespace.</p>
            admin_user_password: <p>The password of the administrator for the first database created in the namespace.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p>
            db_name: <p>The name of the first database created in the namespace.</p>
            kms_key_id: <p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.</p>
            iam_roles: <p>A list of IAM roles to associate with the namespace.</p>
            log_exports: <p>The types of logs the namespace can export. Available export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>
            tags: <p>A list of tag instances.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>
            redshift_idc_application_arn: <p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_namespace

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.create_namespace.create_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.create_namespace_request

            return capo_redshift_serverless.types.create_namespace_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.create_namespace_response

            return capo_redshift_serverless.types.create_namespace_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateNamespace",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest = {
            "namespace_name": namespace_name
        }
        if admin_username is not None:
            input_["admin_username"] = admin_username
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if db_name is not None:
            input_["db_name"] = db_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if log_exports is not None:
            input_["log_exports"] = log_exports
        if tags is not None:
            input_["tags"] = tags
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )
        if redshift_idc_application_arn is not None:
            input_["redshift_idc_application_arn"] = redshift_idc_application_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_namespace_response.GetNamespaceResponse":
        """<p>Returns information about a namespace in Amazon Redshift Serverless.</p>

        Args:
            namespace_name: <p>The name of the namespace to retrieve information for.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.get_namespace_request.GetNamespaceRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.get_namespace_response.GetNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_namespace

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.get_namespace.get_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_redshift_serverless.types.get_namespace_response.GetNamespaceResponse",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.get_namespace_response

            return (
                capo_redshift_serverless.types.get_namespace_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetNamespace", redact_output=_redact_output),
        )
        input_: capo_redshift_serverless.types.get_namespace_request.GetNamespaceRequest = {
            "namespace_name": namespace_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        admin_user_password: Optional[
            "capo_redshift_serverless.types.db_password.DbPassword"
        ] = None,
        admin_username: Optional[
            "capo_redshift_serverless.types.db_user.DbUser"
        ] = None,
        kms_key_id: Optional[str] = None,
        default_iam_role_arn: Optional[str] = None,
        iam_roles: Optional[
            "capo_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        log_exports: Optional[
            "capo_redshift_serverless.types.log_export_list.LogExportList"
        ] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        log_destination_type: Optional[
            "capo_redshift_serverless.types.log_destination_type.LogDestinationType"
        ] = None,
        s3_table_action: Optional[
            "capo_redshift_serverless.types.s3_table_action.S3TableAction"
        ] = None,
        s3_table_names: Optional[
            "capo_redshift_serverless.types.s3_table_name_list.S3TableNameList"
        ] = None,
        s3_table_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        s3_table_granularity: Optional[
            "capo_redshift_serverless.types.s3_table_granularity.S3TableGranularity"
        ] = None,
    ) -> "capo_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse":
        """<p>Updates a namespace with the specified settings. Unless required, you can't update multiple parameters in one request. For example, you must specify both <code>adminUsername</code> and <code>adminUserPassword</code> to update either field, but you can't update both <code>kmsKeyId</code> and <code>logExports</code> in a single request.</p> <p>Similarly, an S3 Tables log-publishing update (a request where <code>logDestinationType</code> is <code>s3table</code>) cannot be combined with any other namespace configuration change and must be submitted as its own request.</p>

        Args:
            namespace_name: <p>The name of the namespace to update. You can't update the name of a namespace once it is created.</p>
            admin_user_password: <p>The password of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUsername</code>.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p> <p>If your admin user account is locked, this operation also unlocks your account and resets the failed-login counter. This option is available only when account lockout security is enabled for the namespace.</p>
            admin_username: <p>The username of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUserPassword</code>.</p>
            kms_key_id: <p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. This parameter must be updated together with <code>iamRoles</code>.</p>
            iam_roles: <p>A list of IAM roles to associate with the namespace. This parameter must be updated together with <code>defaultIamRoleArn</code>.</p>
            log_exports: <p>The types of logs the namespace can export. The export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>
            log_destination_type: <p>The destination for the log data. Valid values are <code>s3table</code> and <code>cloudwatch</code>.</p> <p>Set this to <code>s3table</code> to manage Amazon S3 Tables system-table publishing for the namespace.</p>
            s3_table_action: <p>Whether to enable or disable Amazon S3 Tables publishing. Valid values are <code>Enable</code> and <code>Disable</code>, matched case-insensitively.</p> <p>When omitted, defaults to <code>Enable</code>. Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>
            s3_table_names: <p>The system tables to publish (on enable) or to stop publishing (on disable). Each value is either a system table view name that begins with <code>sys_</code> or the keyword <code>all</code>.</p> <p>Omitting this parameter, passing an empty list, or including <code>all</code> each select every current and future system table. Each name must be 1-128 characters, and the list can contain up to 256 names.</p> <p>Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>
            s3_table_kms_key_id: <p>The identifier of the Key Management Service key used to encrypt the published Amazon S3 Tables data. When omitted, the data is encrypted with SSE-S3 (Amazon S3 managed keys).</p> <p>Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>
            s3_table_granularity: <p>The scope of the Amazon S3 Tables destination. Valid values are <code>namespace</code> and <code>account</code>, matched case-insensitively. <code>namespace</code> scopes the published tables to this namespace; <code>account</code> scopes them to the Amazon Web Services account.</p> <p>Required when enabling. Omitting this parameter or passing a blank value fails with <code>ValidationException</code>. Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_namespace

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.update_namespace.update_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.update_namespace_request

            return capo_redshift_serverless.types.update_namespace_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.update_namespace_response

            return capo_redshift_serverless.types.update_namespace_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateNamespace",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest = {
            "namespace_name": namespace_name
        }
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if admin_username is not None:
            input_["admin_username"] = admin_username
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if log_exports is not None:
            input_["log_exports"] = log_exports
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )
        if log_destination_type is not None:
            input_["log_destination_type"] = log_destination_type
        if s3_table_action is not None:
            input_["s3_table_action"] = s3_table_action
        if s3_table_names is not None:
            input_["s3_table_names"] = s3_table_names
        if s3_table_kms_key_id is not None:
            input_["s3_table_kms_key_id"] = s3_table_kms_key_id
        if s3_table_granularity is not None:
            input_["s3_table_granularity"] = s3_table_granularity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        final_snapshot_name: Optional[str] = None,
        final_snapshot_retention_period: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse":
        """<p>Deletes a namespace from Amazon Redshift Serverless. Before you delete the namespace, you can create a final snapshot that has all of the data within the namespace.</p>

        Args:
            namespace_name: <p>The name of the namespace to delete.</p>
            final_snapshot_name: <p>The name of the snapshot to be created before the namespace is deleted.</p>
            final_snapshot_retention_period: <p>How long to retain the final snapshot.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.delete_namespace_request.DeleteNamespaceRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_namespace

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.delete_namespace.delete_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.delete_namespace_response

            return capo_redshift_serverless.types.delete_namespace_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteNamespace", redact_output=_redact_output),
        )
        input_: capo_redshift_serverless.types.delete_namespace_request.DeleteNamespaceRequest = {
            "namespace_name": namespace_name
        }
        if final_snapshot_name is not None:
            input_["final_snapshot_name"] = final_snapshot_name
        if final_snapshot_retention_period is not None:
            input_["final_snapshot_retention_period"] = final_snapshot_retention_period

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse"
    ):
        """<p>Returns information about a list of specified namespaces.</p>

        Args:
            next_token: <p>If your initial <code>ListNamespaces</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListNamespaces</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.list_namespaces_request.ListNamespacesRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_namespaces

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.list_namespaces.list_namespaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.list_namespaces_response

            return capo_redshift_serverless.types.list_namespaces_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListNamespaces", redact_output=_redact_output),
        )
        input_: capo_redshift_serverless.types.list_namespaces_request.ListNamespacesRequest = {}
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

    def update_lakehouse_configuration(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        lakehouse_registration: Optional[
            "capo_redshift_serverless.types.lakehouse_registration.LakehouseRegistration"
        ] = None,
        catalog_name: Optional[
            "capo_redshift_serverless.types.catalog_name_string.CatalogNameString"
        ] = None,
        lakehouse_idc_registration: Optional[
            "capo_redshift_serverless.types.lakehouse_idc_registration.LakehouseIdcRegistration"
        ] = None,
        lakehouse_idc_application_arn: Optional[str] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.update_lakehouse_configuration_response.UpdateLakehouseConfigurationResponse":
        """<p>Modifies the lakehouse configuration for a namespace. This operation allows you to manage Amazon Redshift federated permissions and Amazon Web Services IAM Identity Center trusted identity propagation.</p>

        Args:
            namespace_name: <p>The name of the namespace whose lakehouse configuration you want to modify.</p>
            lakehouse_registration: <p>Specifies whether to register or deregister the namespace with Amazon Redshift federated permissions. Valid values are <code>Register</code> or <code>Deregister</code>.</p>
            catalog_name: <p>The name of the Glue Data Catalog that will be associated with the namespace enabled with Amazon Redshift federated permissions.</p> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p>
            lakehouse_idc_registration: <p>Modifies the Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions. Valid values are <code>Associate</code> or <code>Disassociate</code>.</p>
            lakehouse_idc_application_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions.</p>
            dry_run: <p>A boolean value that, if <code>true</code>, validates the request without actually updating the lakehouse configuration. Use this to check for errors before making changes.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.dry_run_exception.DryRunException: <p>This exception is thrown when the request was successful, but dry run was enabled so no action was taken.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.update_lakehouse_configuration_request.UpdateLakehouseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.update_lakehouse_configuration_response.UpdateLakehouseConfigurationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_lakehouse_configuration

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.update_lakehouse_configuration.update_lakehouse_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateLakehouseConfiguration")
        )
        input_: capo_redshift_serverless.types.update_lakehouse_configuration_request.UpdateLakehouseConfigurationRequest = {
            "namespace_name": namespace_name
        }
        if lakehouse_registration is not None:
            input_["lakehouse_registration"] = lakehouse_registration
        if catalog_name is not None:
            input_["catalog_name"] = catalog_name
        if lakehouse_idc_registration is not None:
            input_["lakehouse_idc_registration"] = lakehouse_idc_registration
        if lakehouse_idc_application_arn is not None:
            input_["lakehouse_idc_application_arn"] = lakehouse_idc_application_arn
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncNamespaceResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def put(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        admin_username: Optional[
            "capo_redshift_serverless.types.db_user.DbUser"
        ] = None,
        admin_user_password: Optional[
            "capo_redshift_serverless.types.db_password.DbPassword"
        ] = None,
        db_name: Optional[str] = None,
        kms_key_id: Optional[str] = None,
        default_iam_role_arn: Optional[str] = None,
        iam_roles: Optional[
            "capo_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        log_exports: Optional[
            "capo_redshift_serverless.types.log_export_list.LogExportList"
        ] = None,
        tags: Optional["capo_redshift_serverless.types.tag_list.TagList"] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        redshift_idc_application_arn: Optional[
            "capo_redshift_serverless.types.redshift_idc_application_arn.RedshiftIdcApplicationArn"
        ] = None,
    ) -> "capo_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse":
        """<p>Creates a namespace in Amazon Redshift Serverless.</p>

        Args:
            namespace_name: <p>The name of the namespace.</p>
            admin_username: <p>The username of the administrator for the first database created in the namespace.</p>
            admin_user_password: <p>The password of the administrator for the first database created in the namespace.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p>
            db_name: <p>The name of the first database created in the namespace.</p>
            kms_key_id: <p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.</p>
            iam_roles: <p>A list of IAM roles to associate with the namespace.</p>
            log_exports: <p>The types of logs the namespace can export. Available export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>
            tags: <p>A list of tag instances.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>
            redshift_idc_application_arn: <p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_namespace

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_namespace.async_create_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.create_namespace_request

            return capo_redshift_serverless.types.create_namespace_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.create_namespace_response

            return capo_redshift_serverless.types.create_namespace_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateNamespace",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest = {
            "namespace_name": namespace_name
        }
        if admin_username is not None:
            input_["admin_username"] = admin_username
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if db_name is not None:
            input_["db_name"] = db_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if log_exports is not None:
            input_["log_exports"] = log_exports
        if tags is not None:
            input_["tags"] = tags
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )
        if redshift_idc_application_arn is not None:
            input_["redshift_idc_application_arn"] = redshift_idc_application_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_namespace_response.GetNamespaceResponse":
        """<p>Returns information about a namespace in Amazon Redshift Serverless.</p>

        Args:
            namespace_name: <p>The name of the namespace to retrieve information for.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_namespace_request.GetNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_namespace_response.GetNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_namespace

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_namespace.async_get_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_redshift_serverless.types.get_namespace_response.GetNamespaceResponse",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.get_namespace_response

            return (
                capo_redshift_serverless.types.get_namespace_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetNamespace", redact_output=_redact_output),
        )
        input_: capo_redshift_serverless.types.get_namespace_request.GetNamespaceRequest = {
            "namespace_name": namespace_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        admin_user_password: Optional[
            "capo_redshift_serverless.types.db_password.DbPassword"
        ] = None,
        admin_username: Optional[
            "capo_redshift_serverless.types.db_user.DbUser"
        ] = None,
        kms_key_id: Optional[str] = None,
        default_iam_role_arn: Optional[str] = None,
        iam_roles: Optional[
            "capo_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        log_exports: Optional[
            "capo_redshift_serverless.types.log_export_list.LogExportList"
        ] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        log_destination_type: Optional[
            "capo_redshift_serverless.types.log_destination_type.LogDestinationType"
        ] = None,
        s3_table_action: Optional[
            "capo_redshift_serverless.types.s3_table_action.S3TableAction"
        ] = None,
        s3_table_names: Optional[
            "capo_redshift_serverless.types.s3_table_name_list.S3TableNameList"
        ] = None,
        s3_table_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        s3_table_granularity: Optional[
            "capo_redshift_serverless.types.s3_table_granularity.S3TableGranularity"
        ] = None,
    ) -> "capo_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse":
        """<p>Updates a namespace with the specified settings. Unless required, you can't update multiple parameters in one request. For example, you must specify both <code>adminUsername</code> and <code>adminUserPassword</code> to update either field, but you can't update both <code>kmsKeyId</code> and <code>logExports</code> in a single request.</p> <p>Similarly, an S3 Tables log-publishing update (a request where <code>logDestinationType</code> is <code>s3table</code>) cannot be combined with any other namespace configuration change and must be submitted as its own request.</p>

        Args:
            namespace_name: <p>The name of the namespace to update. You can't update the name of a namespace once it is created.</p>
            admin_user_password: <p>The password of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUsername</code>.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p> <p>If your admin user account is locked, this operation also unlocks your account and resets the failed-login counter. This option is available only when account lockout security is enabled for the namespace.</p>
            admin_username: <p>The username of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUserPassword</code>.</p>
            kms_key_id: <p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. This parameter must be updated together with <code>iamRoles</code>.</p>
            iam_roles: <p>A list of IAM roles to associate with the namespace. This parameter must be updated together with <code>defaultIamRoleArn</code>.</p>
            log_exports: <p>The types of logs the namespace can export. The export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>
            log_destination_type: <p>The destination for the log data. Valid values are <code>s3table</code> and <code>cloudwatch</code>.</p> <p>Set this to <code>s3table</code> to manage Amazon S3 Tables system-table publishing for the namespace.</p>
            s3_table_action: <p>Whether to enable or disable Amazon S3 Tables publishing. Valid values are <code>Enable</code> and <code>Disable</code>, matched case-insensitively.</p> <p>When omitted, defaults to <code>Enable</code>. Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>
            s3_table_names: <p>The system tables to publish (on enable) or to stop publishing (on disable). Each value is either a system table view name that begins with <code>sys_</code> or the keyword <code>all</code>.</p> <p>Omitting this parameter, passing an empty list, or including <code>all</code> each select every current and future system table. Each name must be 1-128 characters, and the list can contain up to 256 names.</p> <p>Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>
            s3_table_kms_key_id: <p>The identifier of the Key Management Service key used to encrypt the published Amazon S3 Tables data. When omitted, the data is encrypted with SSE-S3 (Amazon S3 managed keys).</p> <p>Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>
            s3_table_granularity: <p>The scope of the Amazon S3 Tables destination. Valid values are <code>namespace</code> and <code>account</code>, matched case-insensitively. <code>namespace</code> scopes the published tables to this namespace; <code>account</code> scopes them to the Amazon Web Services account.</p> <p>Required when enabling. Omitting this parameter or passing a blank value fails with <code>ValidationException</code>. Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_namespace

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_namespace.async_update_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.update_namespace_request

            return capo_redshift_serverless.types.update_namespace_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.update_namespace_response

            return capo_redshift_serverless.types.update_namespace_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateNamespace",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest = {
            "namespace_name": namespace_name
        }
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if admin_username is not None:
            input_["admin_username"] = admin_username
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if log_exports is not None:
            input_["log_exports"] = log_exports
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )
        if log_destination_type is not None:
            input_["log_destination_type"] = log_destination_type
        if s3_table_action is not None:
            input_["s3_table_action"] = s3_table_action
        if s3_table_names is not None:
            input_["s3_table_names"] = s3_table_names
        if s3_table_kms_key_id is not None:
            input_["s3_table_kms_key_id"] = s3_table_kms_key_id
        if s3_table_granularity is not None:
            input_["s3_table_granularity"] = s3_table_granularity

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        final_snapshot_name: Optional[str] = None,
        final_snapshot_retention_period: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse":
        """<p>Deletes a namespace from Amazon Redshift Serverless. Before you delete the namespace, you can create a final snapshot that has all of the data within the namespace.</p>

        Args:
            namespace_name: <p>The name of the namespace to delete.</p>
            final_snapshot_name: <p>The name of the snapshot to be created before the namespace is deleted.</p>
            final_snapshot_retention_period: <p>How long to retain the final snapshot.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_namespace_request.DeleteNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_namespace

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_namespace.async_delete_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.delete_namespace_response

            return capo_redshift_serverless.types.delete_namespace_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteNamespace", redact_output=_redact_output),
        )
        input_: capo_redshift_serverless.types.delete_namespace_request.DeleteNamespaceRequest = {
            "namespace_name": namespace_name
        }
        if final_snapshot_name is not None:
            input_["final_snapshot_name"] = final_snapshot_name
        if final_snapshot_retention_period is not None:
            input_["final_snapshot_retention_period"] = final_snapshot_retention_period

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse"
    ):
        """<p>Returns information about a list of specified namespaces.</p>

        Args:
            next_token: <p>If your initial <code>ListNamespaces</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListNamespaces</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_namespaces_request.ListNamespacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_namespaces

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_namespaces.async_list_namespaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse",
        ) -> dict[str, Any]:
            import capo_redshift_serverless.types.list_namespaces_response

            return capo_redshift_serverless.types.list_namespaces_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListNamespaces", redact_output=_redact_output),
        )
        input_: capo_redshift_serverless.types.list_namespaces_request.ListNamespacesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_lakehouse_configuration(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        lakehouse_registration: Optional[
            "capo_redshift_serverless.types.lakehouse_registration.LakehouseRegistration"
        ] = None,
        catalog_name: Optional[
            "capo_redshift_serverless.types.catalog_name_string.CatalogNameString"
        ] = None,
        lakehouse_idc_registration: Optional[
            "capo_redshift_serverless.types.lakehouse_idc_registration.LakehouseIdcRegistration"
        ] = None,
        lakehouse_idc_application_arn: Optional[str] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.update_lakehouse_configuration_response.UpdateLakehouseConfigurationResponse":
        """<p>Modifies the lakehouse configuration for a namespace. This operation allows you to manage Amazon Redshift federated permissions and Amazon Web Services IAM Identity Center trusted identity propagation.</p>

        Args:
            namespace_name: <p>The name of the namespace whose lakehouse configuration you want to modify.</p>
            lakehouse_registration: <p>Specifies whether to register or deregister the namespace with Amazon Redshift federated permissions. Valid values are <code>Register</code> or <code>Deregister</code>.</p>
            catalog_name: <p>The name of the Glue Data Catalog that will be associated with the namespace enabled with Amazon Redshift federated permissions.</p> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p>
            lakehouse_idc_registration: <p>Modifies the Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions. Valid values are <code>Associate</code> or <code>Disassociate</code>.</p>
            lakehouse_idc_application_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions.</p>
            dry_run: <p>A boolean value that, if <code>true</code>, validates the request without actually updating the lakehouse configuration. Use this to check for errors before making changes.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.dry_run_exception.DryRunException: <p>This exception is thrown when the request was successful, but dry run was enabled so no action was taken.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_lakehouse_configuration_request.UpdateLakehouseConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_lakehouse_configuration_response.UpdateLakehouseConfigurationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_lakehouse_configuration

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_lakehouse_configuration.async_update_lakehouse_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateLakehouseConfiguration")
        )
        input_: capo_redshift_serverless.types.update_lakehouse_configuration_request.UpdateLakehouseConfigurationRequest = {
            "namespace_name": namespace_name
        }
        if lakehouse_registration is not None:
            input_["lakehouse_registration"] = lakehouse_registration
        if catalog_name is not None:
            input_["catalog_name"] = catalog_name
        if lakehouse_idc_registration is not None:
            input_["lakehouse_idc_registration"] = lakehouse_idc_registration
        if lakehouse_idc_application_arn is not None:
            input_["lakehouse_idc_application_arn"] = lakehouse_idc_application_arn
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
