"""Generated from Smithy shape ``com.amazonaws.textract#Textract``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_textract._auth._signers
import capo_textract._auth._sigv4
from capo_textract._auth._identity import Credentials
from capo_textract._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_textract._auth._zapros_handler import AuthMiddleware
from capo_textract._pagination import resolve_path as _resolve_path
from capo_textract._services._aws_config import aws_config
from capo_textract._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_textract.types.adapter_description
    import capo_textract.types.adapter_id
    import capo_textract.types.adapter_name
    import capo_textract.types.adapter_overview
    import capo_textract.types.adapter_version
    import capo_textract.types.adapter_version_dataset_config
    import capo_textract.types.adapter_version_overview
    import capo_textract.types.adapters_config
    import capo_textract.types.amazon_resource_name
    import capo_textract.types.analyze_document_request
    import capo_textract.types.analyze_document_response
    import capo_textract.types.analyze_expense_request
    import capo_textract.types.analyze_expense_response
    import capo_textract.types.analyze_id_request
    import capo_textract.types.analyze_id_response
    import capo_textract.types.auto_update
    import capo_textract.types.client_request_token
    import capo_textract.types.create_adapter_request
    import capo_textract.types.create_adapter_response
    import capo_textract.types.create_adapter_version_request
    import capo_textract.types.create_adapter_version_response
    import capo_textract.types.date_time
    import capo_textract.types.delete_adapter_request
    import capo_textract.types.delete_adapter_response
    import capo_textract.types.delete_adapter_version_request
    import capo_textract.types.delete_adapter_version_response
    import capo_textract.types.detect_document_text_request
    import capo_textract.types.detect_document_text_response
    import capo_textract.types.document
    import capo_textract.types.document_location
    import capo_textract.types.document_pages
    import capo_textract.types.feature_types
    import capo_textract.types.get_adapter_request
    import capo_textract.types.get_adapter_response
    import capo_textract.types.get_adapter_version_request
    import capo_textract.types.get_adapter_version_response
    import capo_textract.types.get_document_analysis_request
    import capo_textract.types.get_document_analysis_response
    import capo_textract.types.get_document_text_detection_request
    import capo_textract.types.get_document_text_detection_response
    import capo_textract.types.get_expense_analysis_request
    import capo_textract.types.get_expense_analysis_response
    import capo_textract.types.get_lending_analysis_request
    import capo_textract.types.get_lending_analysis_response
    import capo_textract.types.get_lending_analysis_summary_request
    import capo_textract.types.get_lending_analysis_summary_response
    import capo_textract.types.human_loop_config
    import capo_textract.types.job_id
    import capo_textract.types.job_tag
    import capo_textract.types.kms_key_id
    import capo_textract.types.list_adapter_versions_request
    import capo_textract.types.list_adapter_versions_response
    import capo_textract.types.list_adapters_request
    import capo_textract.types.list_adapters_response
    import capo_textract.types.list_tags_for_resource_request
    import capo_textract.types.list_tags_for_resource_response
    import capo_textract.types.max_results
    import capo_textract.types.notification_channel
    import capo_textract.types.output_config
    import capo_textract.types.pagination_token
    import capo_textract.types.queries_config
    import capo_textract.types.start_document_analysis_request
    import capo_textract.types.start_document_analysis_response
    import capo_textract.types.start_document_text_detection_request
    import capo_textract.types.start_document_text_detection_response
    import capo_textract.types.start_expense_analysis_request
    import capo_textract.types.start_expense_analysis_response
    import capo_textract.types.start_lending_analysis_request
    import capo_textract.types.start_lending_analysis_response
    import capo_textract.types.tag_key_list
    import capo_textract.types.tag_map
    import capo_textract.types.tag_resource_request
    import capo_textract.types.tag_resource_response
    import capo_textract.types.untag_resource_request
    import capo_textract.types.untag_resource_response
    import capo_textract.types.update_adapter_request
    import capo_textract.types.update_adapter_response


class TextractClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class TextractClient:
    """A client for the ``Textract`` service.

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
        self._config = TextractClientConfig(
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
        self, config_overrides: Optional[TextractClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: TextractClientConfig = config_overrides or {}
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

    def analyze_document(
        self,
        document: "capo_textract.types.document.Document",
        feature_types: "capo_textract.types.feature_types.FeatureTypes",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        human_loop_config: Optional[
            "capo_textract.types.human_loop_config.HumanLoopConfig"
        ] = None,
        queries_config: Optional[
            "capo_textract.types.queries_config.QueriesConfig"
        ] = None,
        adapters_config: Optional[
            "capo_textract.types.adapters_config.AdaptersConfig"
        ] = None,
    ) -> "capo_textract.types.analyze_document_response.AnalyzeDocumentResponse":
        """<p>Analyzes an input document for relationships between detected items. </p> <p>The types of information returned are as follows: </p> <ul> <li> <p>Form data (key-value pairs). The related information is returned in two <a>Block</a> objects, each of type <code>KEY_VALUE_SET</code>: a KEY <code>Block</code> object and a VALUE <code>Block</code> object. For example, <i>Name: Ana Silva Carolina</i> contains a key and value. <i>Name:</i> is the key. <i>Ana Silva Carolina</i> is the value.</p> </li> <li> <p>Table and table cell data. A TABLE <code>Block</code> object contains information about a detected table. A CELL <code>Block</code> object is returned for each cell in a table.</p> </li> <li> <p>Lines and words of text. A LINE <code>Block</code> object contains one or more WORD <code>Block</code> objects. All lines and words that are detected in the document are returned (including text that doesn't have a relationship with the value of <code>FeatureTypes</code>). </p> </li> <li> <p>Signatures. A SIGNATURE <code>Block</code> object contains the location information of a signature in a document. If used in conjunction with forms or tables, a signature can be given a Key-Value pairing or be detected in the cell of a table.</p> </li> <li> <p>Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.</p> </li> <li> <p>Query Result. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.</p> </li> </ul> <p>Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT <code>Block</code> object contains information about a selection element, including the selection status.</p> <p>You can choose which type of analysis to perform by specifying the <code>FeatureTypes</code> list. </p> <p>The output is returned in a list of <code>Block</code> objects.</p> <p> <code>AnalyzeDocument</code> is a synchronous operation. To analyze documents asynchronously, use <a>StartDocumentAnalysis</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html">Document Text Analysis</a>.</p>

        Args:
            document: <p>The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can't pass image bytes. The document must be an image in JPEG, PNG, PDF, or TIFF format.</p> <p>If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes that are passed using the <code>Bytes</code> field. </p>
            feature_types: <p>A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. Add SIGNATURES to return the locations of detected signatures. Add LAYOUT to the list to return information about the layout of the document. All lines and words detected in the document are included in the response (including text that isn't related to the value of <code>FeatureTypes</code>). </p>
            human_loop_config: <p>Sets the configuration for the human in the loop workflow for analyzing documents.</p> <note> <p>Amazon Textract uses Amazon Augmented AI (A2I) to run the human review workflows that you specify in <code>HumanLoopConfig</code>. A2I entered maintenance mode in July 2026 and no longer accepts new customers. If your account is not an existing A2I customer, requests fail with an <code>InvalidParameterException</code>. For more information, see <a href="https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/">AWS service availability</a>. If you're an existing A2I customer but receive this error, contact AWS Support and request assistance from the A2I team.</p> </note>
            queries_config: <p>Contains Queries and the alias for those Queries, as determined by the input. </p>
            adapters_config: <p>Specifies the adapter to be used when analyzing a document.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.bad_document_exception.BadDocumentException: <p>Amazon Textract isn't able to read the document. For more information on the document limits in Amazon Textract, see <a href="https://docs.aws.amazon.com/textract/latest/dg/limits.html">Hard limits</a>.</p>
            capo_textract.errors.document_too_large_exception.DocumentTooLargeException: <p>The document can't be processed because it's too large. The maximum document size for synchronous operations 10 MB. The maximum document size for asynchronous operations is 500 MB for PDF files.</p>
            capo_textract.errors.human_loop_quota_exceeded_exception.HumanLoopQuotaExceededException: <p>Indicates you have exceeded the maximum number of active human in the loop workflows available</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.unsupported_document_exception.UnsupportedDocumentException: <p>The format of the input document isn't supported. Documents for operations can be in PNG, JPEG, PDF, or TIFF format.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.analyze_document_request.AnalyzeDocumentRequest]",
        ) -> OperationResponse[
            "capo_textract.types.analyze_document_response.AnalyzeDocumentResponse"
        ]:
            import capo_textract._operations.textract.analyze_document

            output, http_response = (
                capo_textract._operations.textract.analyze_document.analyze_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.analyze_document_request.AnalyzeDocumentRequest = {
            "document": document,
            "feature_types": feature_types,
        }
        if human_loop_config is not None:
            input_["human_loop_config"] = human_loop_config
        if queries_config is not None:
            input_["queries_config"] = queries_config
        if adapters_config is not None:
            input_["adapters_config"] = adapters_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def analyze_expense(
        self,
        document: "capo_textract.types.document.Document",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.analyze_expense_response.AnalyzeExpenseResponse":
        """<p> <code>AnalyzeExpense</code> synchronously analyzes an input document for financially related relationships between text.</p> <p>Information is returned as <code>ExpenseDocuments</code> and seperated as follows:</p> <ul> <li> <p> <code>LineItemGroups</code>- A data set containing <code>LineItems</code> which store information about the lines of text, such as an item purchased and its price on a receipt.</p> </li> <li> <p> <code>SummaryFields</code>- Contains all other information a receipt, such as header information or the vendors name.</p> </li> </ul>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.bad_document_exception.BadDocumentException: <p>Amazon Textract isn't able to read the document. For more information on the document limits in Amazon Textract, see <a href="https://docs.aws.amazon.com/textract/latest/dg/limits.html">Hard limits</a>.</p>
            capo_textract.errors.document_too_large_exception.DocumentTooLargeException: <p>The document can't be processed because it's too large. The maximum document size for synchronous operations 10 MB. The maximum document size for asynchronous operations is 500 MB for PDF files.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.unsupported_document_exception.UnsupportedDocumentException: <p>The format of the input document isn't supported. Documents for operations can be in PNG, JPEG, PDF, or TIFF format.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.analyze_expense_request.AnalyzeExpenseRequest]",
        ) -> OperationResponse[
            "capo_textract.types.analyze_expense_response.AnalyzeExpenseResponse"
        ]:
            import capo_textract._operations.textract.analyze_expense

            output, http_response = (
                capo_textract._operations.textract.analyze_expense.analyze_expense(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.analyze_expense_request.AnalyzeExpenseRequest = {
            "document": document
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def analyze_id(
        self,
        document_pages: "capo_textract.types.document_pages.DocumentPages",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.analyze_id_response.AnalyzeIDResponse":
        """<p>Analyzes identity documents for relevant information. This information is extracted and returned as <code>IdentityDocumentFields</code>, which records both the normalized field and value of the extracted text. Unlike other Amazon Textract operations, <code>AnalyzeID</code> doesn't return any Geometry data.</p>

        Args:
            document_pages: <p>The document being passed to AnalyzeID.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.bad_document_exception.BadDocumentException: <p>Amazon Textract isn't able to read the document. For more information on the document limits in Amazon Textract, see <a href="https://docs.aws.amazon.com/textract/latest/dg/limits.html">Hard limits</a>.</p>
            capo_textract.errors.document_too_large_exception.DocumentTooLargeException: <p>The document can't be processed because it's too large. The maximum document size for synchronous operations 10 MB. The maximum document size for asynchronous operations is 500 MB for PDF files.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.unsupported_document_exception.UnsupportedDocumentException: <p>The format of the input document isn't supported. Documents for operations can be in PNG, JPEG, PDF, or TIFF format.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.analyze_id_request.AnalyzeIDRequest]",
        ) -> OperationResponse[
            "capo_textract.types.analyze_id_response.AnalyzeIDResponse"
        ]:
            import capo_textract._operations.textract.analyze_id

            output, http_response = (
                capo_textract._operations.textract.analyze_id.analyze_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.analyze_id_request.AnalyzeIDRequest = {
            "document_pages": document_pages
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_adapter(
        self,
        adapter_name: "capo_textract.types.adapter_name.AdapterName",
        feature_types: "capo_textract.types.feature_types.FeatureTypes",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        client_request_token: Optional[
            "capo_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        description: Optional[
            "capo_textract.types.adapter_description.AdapterDescription"
        ] = None,
        auto_update: Optional["capo_textract.types.auto_update.AutoUpdate"] = None,
        tags: Optional["capo_textract.types.tag_map.TagMap"] = None,
    ) -> "capo_textract.types.create_adapter_response.CreateAdapterResponse":
        """<p>Creates an adapter, which can be fine-tuned for enhanced performance on user provided documents. Takes an AdapterName and FeatureType. Currently the only supported feature type is <code>QUERIES</code>. You can also provide a Description, Tags, and a ClientRequestToken. You can choose whether or not the adapter should be AutoUpdated with the AutoUpdate argument. By default, AutoUpdate is set to DISABLED.</p>

        Args:
            adapter_name: <p>The name to be assigned to the adapter being created.</p>
            client_request_token: <p>Idempotent token is used to recognize the request. If the same token is used with multiple CreateAdapter requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.</p>
            description: <p>The description to be assigned to the adapter being created.</p>
            feature_types: <p>The type of feature that the adapter is being trained on. Currrenly, supported feature types are: <code>QUERIES</code> </p>
            auto_update: <p>Controls whether or not the adapter should automatically update.</p>
            tags: <p>A list of tags to be added to the adapter.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_textract.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation. </p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Textract service limit was exceeded. For example, if you start too many asynchronous jobs concurrently, calls to start operations (<code>StartDocumentTextDetection</code>, for example) raise a LimitExceededException exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Textract service limit. </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Returned when a request cannot be completed as it would exceed a maximum service quota.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.create_adapter_request.CreateAdapterRequest]",
        ) -> OperationResponse[
            "capo_textract.types.create_adapter_response.CreateAdapterResponse"
        ]:
            import capo_textract._operations.textract.create_adapter

            output, http_response = (
                capo_textract._operations.textract.create_adapter.create_adapter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.create_adapter_request.CreateAdapterRequest = {
            "adapter_name": adapter_name,
            "feature_types": feature_types,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if description is not None:
            input_["description"] = description
        if auto_update is not None:
            input_["auto_update"] = auto_update
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_adapter_version(
        self,
        adapter_id: "capo_textract.types.adapter_id.AdapterId",
        dataset_config: "capo_textract.types.adapter_version_dataset_config.AdapterVersionDatasetConfig",
        output_config: "capo_textract.types.output_config.OutputConfig",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        client_request_token: Optional[
            "capo_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        kms_key_id: Optional["capo_textract.types.kms_key_id.KMSKeyId"] = None,
        tags: Optional["capo_textract.types.tag_map.TagMap"] = None,
    ) -> "capo_textract.types.create_adapter_version_response.CreateAdapterVersionResponse":
        """<p>Creates a new version of an adapter. Operates on a provided AdapterId and a specified dataset provided via the DatasetConfig argument. Requires that you specify an Amazon S3 bucket with the OutputConfig argument. You can provide an optional KMSKeyId, an optional ClientRequestToken, and optional tags.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter that will receive a new version.</p>
            client_request_token: <p>Idempotent token is used to recognize the request. If the same token is used with multiple CreateAdapterVersion requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.</p>
            dataset_config: <p>Specifies a dataset used to train a new adapter version. Takes a ManifestS3Object as the value.</p>
            kms_key_id: <p>The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt your documents.</p>
            tags: <p>A set of tags (key-value pairs) that you want to attach to the adapter version. </p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_textract.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation. </p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_kms_key_exception.InvalidKMSKeyException: <p> Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key was entered incorrectly. </p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Textract service limit was exceeded. For example, if you start too many asynchronous jobs concurrently, calls to start operations (<code>StartDocumentTextDetection</code>, for example) raise a LimitExceededException exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Textract service limit. </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.resource_not_found_exception.ResourceNotFoundException: <p> Returned when an operation tried to access a nonexistent resource. </p>
            capo_textract.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Returned when a request cannot be completed as it would exceed a maximum service quota.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.create_adapter_version_request.CreateAdapterVersionRequest]",
        ) -> OperationResponse[
            "capo_textract.types.create_adapter_version_response.CreateAdapterVersionResponse"
        ]:
            import capo_textract._operations.textract.create_adapter_version

            output, http_response = (
                capo_textract._operations.textract.create_adapter_version.create_adapter_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.create_adapter_version_request.CreateAdapterVersionRequest = {
            "adapter_id": adapter_id,
            "dataset_config": dataset_config,
            "output_config": output_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_adapter(
        self,
        adapter_id: "capo_textract.types.adapter_id.AdapterId",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.delete_adapter_response.DeleteAdapterResponse":
        """<p>Deletes an Amazon Textract adapter. Takes an AdapterId and deletes the adapter specified by the ID.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter to be deleted.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.resource_not_found_exception.ResourceNotFoundException: <p> Returned when an operation tried to access a nonexistent resource. </p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.delete_adapter_request.DeleteAdapterRequest]",
        ) -> OperationResponse[
            "capo_textract.types.delete_adapter_response.DeleteAdapterResponse"
        ]:
            import capo_textract._operations.textract.delete_adapter

            output, http_response = (
                capo_textract._operations.textract.delete_adapter.delete_adapter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.delete_adapter_request.DeleteAdapterRequest = {
            "adapter_id": adapter_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_adapter_version(
        self,
        adapter_id: "capo_textract.types.adapter_id.AdapterId",
        adapter_version: "capo_textract.types.adapter_version.AdapterVersion",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.delete_adapter_version_response.DeleteAdapterVersionResponse":
        """<p>Deletes an Amazon Textract adapter version. Requires that you specify both an AdapterId and a AdapterVersion. Deletes the adapter version specified by the AdapterId and the AdapterVersion.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter version that will be deleted.</p>
            adapter_version: <p>Specifies the adapter version to be deleted.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.resource_not_found_exception.ResourceNotFoundException: <p> Returned when an operation tried to access a nonexistent resource. </p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.delete_adapter_version_request.DeleteAdapterVersionRequest]",
        ) -> OperationResponse[
            "capo_textract.types.delete_adapter_version_response.DeleteAdapterVersionResponse"
        ]:
            import capo_textract._operations.textract.delete_adapter_version

            output, http_response = (
                capo_textract._operations.textract.delete_adapter_version.delete_adapter_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.delete_adapter_version_request.DeleteAdapterVersionRequest = {
            "adapter_id": adapter_id,
            "adapter_version": adapter_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_document_text(
        self,
        document: "capo_textract.types.document.Document",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.detect_document_text_response.DetectDocumentTextResponse":
        """<p>Detects text in the input document. Amazon Textract can detect lines of text and the words that make up a line of text. The input document must be in one of the following image formats: JPEG, PNG, PDF, or TIFF. <code>DetectDocumentText</code> returns the detected text in an array of <a>Block</a> objects. </p> <p>Each document page has as an associated <code>Block</code> of type PAGE. Each PAGE <code>Block</code> object is the parent of LINE <code>Block</code> objects that represent the lines of detected text on a page. A LINE <code>Block</code> object is a parent for each word that makes up the line. Words are represented by <code>Block</code> objects of type WORD.</p> <p> <code>DetectDocumentText</code> is a synchronous operation. To analyze documents asynchronously, use <a>StartDocumentTextDetection</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html">Document Text Detection</a>.</p>

        Args:
            document: <p>The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can't pass image bytes. The document must be an image in JPEG or PNG format.</p> <p>If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes that are passed using the <code>Bytes</code> field. </p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.bad_document_exception.BadDocumentException: <p>Amazon Textract isn't able to read the document. For more information on the document limits in Amazon Textract, see <a href="https://docs.aws.amazon.com/textract/latest/dg/limits.html">Hard limits</a>.</p>
            capo_textract.errors.document_too_large_exception.DocumentTooLargeException: <p>The document can't be processed because it's too large. The maximum document size for synchronous operations 10 MB. The maximum document size for asynchronous operations is 500 MB for PDF files.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.unsupported_document_exception.UnsupportedDocumentException: <p>The format of the input document isn't supported. Documents for operations can be in PNG, JPEG, PDF, or TIFF format.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.detect_document_text_request.DetectDocumentTextRequest]",
        ) -> OperationResponse[
            "capo_textract.types.detect_document_text_response.DetectDocumentTextResponse"
        ]:
            import capo_textract._operations.textract.detect_document_text

            output, http_response = (
                capo_textract._operations.textract.detect_document_text.detect_document_text(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.detect_document_text_request.DetectDocumentTextRequest = {
            "document": document
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_adapter(
        self,
        adapter_id: "capo_textract.types.adapter_id.AdapterId",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.get_adapter_response.GetAdapterResponse":
        """<p>Gets configuration information for an adapter specified by an AdapterId, returning information on AdapterName, Description, CreationTime, AutoUpdate status, and FeatureTypes.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.resource_not_found_exception.ResourceNotFoundException: <p> Returned when an operation tried to access a nonexistent resource. </p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.get_adapter_request.GetAdapterRequest]",
        ) -> OperationResponse[
            "capo_textract.types.get_adapter_response.GetAdapterResponse"
        ]:
            import capo_textract._operations.textract.get_adapter

            output, http_response = (
                capo_textract._operations.textract.get_adapter.get_adapter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.get_adapter_request.GetAdapterRequest = {
            "adapter_id": adapter_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_adapter_version(
        self,
        adapter_id: "capo_textract.types.adapter_id.AdapterId",
        adapter_version: "capo_textract.types.adapter_version.AdapterVersion",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.get_adapter_version_response.GetAdapterVersionResponse":
        """<p>Gets configuration information for the specified adapter version, including: AdapterId, AdapterVersion, FeatureTypes, Status, StatusMessage, DatasetConfig, KMSKeyId, OutputConfig, Tags and EvaluationMetrics.</p>

        Args:
            adapter_id: <p>A string specifying a unique ID for the adapter version you want to retrieve information for.</p>
            adapter_version: <p>A string specifying the adapter version you want to retrieve information for.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.resource_not_found_exception.ResourceNotFoundException: <p> Returned when an operation tried to access a nonexistent resource. </p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.get_adapter_version_request.GetAdapterVersionRequest]",
        ) -> OperationResponse[
            "capo_textract.types.get_adapter_version_response.GetAdapterVersionResponse"
        ]:
            import capo_textract._operations.textract.get_adapter_version

            output, http_response = (
                capo_textract._operations.textract.get_adapter_version.get_adapter_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.get_adapter_version_request.GetAdapterVersionRequest = {
            "adapter_id": adapter_id,
            "adapter_version": adapter_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_document_analysis(
        self,
        job_id: "capo_textract.types.job_id.JobId",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        max_results: Optional["capo_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "capo_textract.types.get_document_analysis_response.GetDocumentAnalysisResponse"
    ):
        """<p>Gets the results for an Amazon Textract asynchronous operation that analyzes text in a document.</p> <p>You start asynchronous text analysis by calling <a>StartDocumentAnalysis</a>, which returns a job identifier (<code>JobId</code>). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that's registered in the initial call to <code>StartDocumentAnalysis</code>. To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <code>GetDocumentAnalysis</code>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartDocumentAnalysis</code>.</p> <p> <code>GetDocumentAnalysis</code> returns an array of <a>Block</a> objects. The following types of information are returned: </p> <ul> <li> <p>Form data (key-value pairs). The related information is returned in two <a>Block</a> objects, each of type <code>KEY_VALUE_SET</code>: a KEY <code>Block</code> object and a VALUE <code>Block</code> object. For example, <i>Name: Ana Silva Carolina</i> contains a key and value. <i>Name:</i> is the key. <i>Ana Silva Carolina</i> is the value.</p> </li> <li> <p>Table and table cell data. A TABLE <code>Block</code> object contains information about a detected table. A CELL <code>Block</code> object is returned for each cell in a table.</p> </li> <li> <p>Lines and words of text. A LINE <code>Block</code> object contains one or more WORD <code>Block</code> objects. All lines and words that are detected in the document are returned (including text that doesn't have a relationship with the value of the <code>StartDocumentAnalysis</code> <code>FeatureTypes</code> input parameter). </p> </li> <li> <p>Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.</p> </li> <li> <p>Query Results. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.</p> </li> </ul> <note> <p>While processing a document with queries, look out for <code>INVALID_REQUEST_PARAMETERS</code> output. This indicates that either the per page query limit has been exceeded or that the operation is trying to query a page in the document which doesn’t exist. </p> </note> <p>Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT <code>Block</code> object contains information about a selection element, including the selection status.</p> <p>Use the <code>MaxResults</code> parameter to limit the number of blocks that are returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetDocumentAnalysis</code>, and populate the <code>NextToken</code> request parameter with the token value that's returned from the previous call to <code>GetDocumentAnalysis</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html">Document Text Analysis</a>.</p>

        Args:
            job_id: <p>A unique identifier for the text-detection job. The <code>JobId</code> is returned from <code>StartDocumentAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value that you can specify is 1,000. If you specify a value greater than 1,000, a maximum of 1,000 results is returned. The default value is 1,000.</p>
            next_token: <p>If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_job_id_exception.InvalidJobIdException: <p>An invalid job identifier was passed to an asynchronous analysis operation.</p>
            capo_textract.errors.invalid_kms_key_exception.InvalidKMSKeyException: <p> Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key was entered incorrectly. </p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.get_document_analysis_request.GetDocumentAnalysisRequest]",
        ) -> OperationResponse[
            "capo_textract.types.get_document_analysis_response.GetDocumentAnalysisResponse"
        ]:
            import capo_textract._operations.textract.get_document_analysis

            output, http_response = (
                capo_textract._operations.textract.get_document_analysis.get_document_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.get_document_analysis_request.GetDocumentAnalysisRequest = {
            "job_id": job_id
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

    def get_document_text_detection(
        self,
        job_id: "capo_textract.types.job_id.JobId",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        max_results: Optional["capo_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_textract.types.get_document_text_detection_response.GetDocumentTextDetectionResponse":
        """<p>Gets the results for an Amazon Textract asynchronous operation that detects text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.</p> <p>You start asynchronous text detection by calling <a>StartDocumentTextDetection</a>, which returns a job identifier (<code>JobId</code>). When the text detection operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that's registered in the initial call to <code>StartDocumentTextDetection</code>. To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <code>GetDocumentTextDetection</code>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartDocumentTextDetection</code>.</p> <p> <code>GetDocumentTextDetection</code> returns an array of <a>Block</a> objects. </p> <p>Each document page has as an associated <code>Block</code> of type PAGE. Each PAGE <code>Block</code> object is the parent of LINE <code>Block</code> objects that represent the lines of detected text on a page. A LINE <code>Block</code> object is a parent for each word that makes up the line. Words are represented by <code>Block</code> objects of type WORD.</p> <p>Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetDocumentTextDetection</code>, and populate the <code>NextToken</code> request parameter with the token value that's returned from the previous call to <code>GetDocumentTextDetection</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html">Document Text Detection</a>.</p>

        Args:
            job_id: <p>A unique identifier for the text detection job. The <code>JobId</code> is returned from <code>StartDocumentTextDetection</code>. A <code>JobId</code> value is only valid for 7 days.</p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value you can specify is 1,000. If you specify a value greater than 1,000, a maximum of 1,000 results is returned. The default value is 1,000.</p>
            next_token: <p>If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_job_id_exception.InvalidJobIdException: <p>An invalid job identifier was passed to an asynchronous analysis operation.</p>
            capo_textract.errors.invalid_kms_key_exception.InvalidKMSKeyException: <p> Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key was entered incorrectly. </p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.get_document_text_detection_request.GetDocumentTextDetectionRequest]",
        ) -> OperationResponse[
            "capo_textract.types.get_document_text_detection_response.GetDocumentTextDetectionResponse"
        ]:
            import capo_textract._operations.textract.get_document_text_detection

            output, http_response = (
                capo_textract._operations.textract.get_document_text_detection.get_document_text_detection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.get_document_text_detection_request.GetDocumentTextDetectionRequest = {
            "job_id": job_id
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

    def get_expense_analysis(
        self,
        job_id: "capo_textract.types.job_id.JobId",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        max_results: Optional["capo_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_textract.types.get_expense_analysis_response.GetExpenseAnalysisResponse":
        """<p>Gets the results for an Amazon Textract asynchronous operation that analyzes invoices and receipts. Amazon Textract finds contact information, items purchased, and vendor name, from input invoices and receipts.</p> <p>You start asynchronous invoice/receipt analysis by calling <a>StartExpenseAnalysis</a>, which returns a job identifier (<code>JobId</code>). Upon completion of the invoice/receipt analysis, Amazon Textract publishes the completion status to the Amazon Simple Notification Service (Amazon SNS) topic. This topic must be registered in the initial call to <code>StartExpenseAnalysis</code>. To get the results of the invoice/receipt analysis operation, first ensure that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <code>GetExpenseAnalysis</code>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartExpenseAnalysis</code>.</p> <p>Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetExpenseAnalysis</code>, and populate the <code>NextToken</code> request parameter with the token value that's returned from the previous call to <code>GetExpenseAnalysis</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/invoices-receipts.html">Analyzing Invoices and Receipts</a>.</p>

        Args:
            job_id: <p>A unique identifier for the text detection job. The <code>JobId</code> is returned from <code>StartExpenseAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value you can specify is 20. If you specify a value greater than 20, a maximum of 20 results is returned. The default value is 20.</p>
            next_token: <p>If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_job_id_exception.InvalidJobIdException: <p>An invalid job identifier was passed to an asynchronous analysis operation.</p>
            capo_textract.errors.invalid_kms_key_exception.InvalidKMSKeyException: <p> Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key was entered incorrectly. </p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.get_expense_analysis_request.GetExpenseAnalysisRequest]",
        ) -> OperationResponse[
            "capo_textract.types.get_expense_analysis_response.GetExpenseAnalysisResponse"
        ]:
            import capo_textract._operations.textract.get_expense_analysis

            output, http_response = (
                capo_textract._operations.textract.get_expense_analysis.get_expense_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.get_expense_analysis_request.GetExpenseAnalysisRequest = {
            "job_id": job_id
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

    def get_lending_analysis(
        self,
        job_id: "capo_textract.types.job_id.JobId",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        max_results: Optional["capo_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_textract.types.get_lending_analysis_response.GetLendingAnalysisResponse":
        """<p>Gets the results for an Amazon Textract asynchronous operation that analyzes text in a lending document. </p> <p>You start asynchronous text analysis by calling <code>StartLendingAnalysis</code>, which returns a job identifier (<code>JobId</code>). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that's registered in the initial call to <code>StartLendingAnalysis</code>. </p> <p>To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call GetLendingAnalysis, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartLendingAnalysis</code>.</p>

        Args:
            job_id: <p>A unique identifier for the lending or text-detection job. The <code>JobId</code> is returned from <code>StartLendingAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value that you can specify is 30. If you specify a value greater than 30, a maximum of 30 results is returned. The default value is 30.</p>
            next_token: <p>If the previous response was incomplete, Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of lending results.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_job_id_exception.InvalidJobIdException: <p>An invalid job identifier was passed to an asynchronous analysis operation.</p>
            capo_textract.errors.invalid_kms_key_exception.InvalidKMSKeyException: <p> Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key was entered incorrectly. </p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.get_lending_analysis_request.GetLendingAnalysisRequest]",
        ) -> OperationResponse[
            "capo_textract.types.get_lending_analysis_response.GetLendingAnalysisResponse"
        ]:
            import capo_textract._operations.textract.get_lending_analysis

            output, http_response = (
                capo_textract._operations.textract.get_lending_analysis.get_lending_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.get_lending_analysis_request.GetLendingAnalysisRequest = {
            "job_id": job_id
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

    def get_lending_analysis_summary(
        self,
        job_id: "capo_textract.types.job_id.JobId",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.get_lending_analysis_summary_response.GetLendingAnalysisSummaryResponse":
        """<p>Gets summarized results for the <code>StartLendingAnalysis</code> operation, which analyzes text in a lending document. The returned summary consists of information about documents grouped together by a common document type. Information like detected signatures, page numbers, and split documents is returned with respect to the type of grouped document. </p> <p>You start asynchronous text analysis by calling <code>StartLendingAnalysis</code>, which returns a job identifier (<code>JobId</code>). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that's registered in the initial call to <code>StartLendingAnalysis</code>. </p> <p>To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call <code>GetLendingAnalysisSummary</code>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartLendingAnalysis</code>.</p>

        Args:
            job_id: <p> A unique identifier for the lending or text-detection job. The <code>JobId</code> is returned from StartLendingAnalysis. A <code>JobId</code> value is only valid for 7 days.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_job_id_exception.InvalidJobIdException: <p>An invalid job identifier was passed to an asynchronous analysis operation.</p>
            capo_textract.errors.invalid_kms_key_exception.InvalidKMSKeyException: <p> Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key was entered incorrectly. </p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.get_lending_analysis_summary_request.GetLendingAnalysisSummaryRequest]",
        ) -> OperationResponse[
            "capo_textract.types.get_lending_analysis_summary_response.GetLendingAnalysisSummaryResponse"
        ]:
            import capo_textract._operations.textract.get_lending_analysis_summary

            output, http_response = (
                capo_textract._operations.textract.get_lending_analysis_summary.get_lending_analysis_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.get_lending_analysis_summary_request.GetLendingAnalysisSummaryRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_adapters(
        self,
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        after_creation_time: Optional["capo_textract.types.date_time.DateTime"] = None,
        before_creation_time: Optional["capo_textract.types.date_time.DateTime"] = None,
        max_results: Optional["capo_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_textract.types.list_adapters_response.ListAdaptersResponse":
        """<p>Lists all adapters that match the specified filtration criteria.</p>

        Args:
            after_creation_time: <p>Specifies the lower bound for the ListAdapters operation. Ensures ListAdapters returns only adapters created after the specified creation time.</p>
            before_creation_time: <p>Specifies the upper bound for the ListAdapters operation. Ensures ListAdapters returns only adapters created before the specified creation time.</p>
            max_results: <p>The maximum number of results to return when listing adapters.</p>
            next_token: <p>Identifies the next page of results to return when listing adapters.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.list_adapters_request.ListAdaptersRequest]",
        ) -> OperationResponse[
            "capo_textract.types.list_adapters_response.ListAdaptersResponse"
        ]:
            import capo_textract._operations.textract.list_adapters

            output, http_response = (
                capo_textract._operations.textract.list_adapters.list_adapters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.list_adapters_request.ListAdaptersRequest = {}
        if after_creation_time is not None:
            input_["after_creation_time"] = after_creation_time
        if before_creation_time is not None:
            input_["before_creation_time"] = before_creation_time
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

    def iter_list_adapters(
        self,
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        after_creation_time: Optional["capo_textract.types.date_time.DateTime"] = None,
        before_creation_time: Optional["capo_textract.types.date_time.DateTime"] = None,
        max_results: Optional["capo_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_textract.types.adapter_overview.AdapterOverview]":
        _token = next_token
        while True:
            _response = self.list_adapters(
                config_overrides=config_overrides,
                after_creation_time=after_creation_time,
                before_creation_time=before_creation_time,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("adapters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_adapter_versions(
        self,
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        adapter_id: Optional["capo_textract.types.adapter_id.AdapterId"] = None,
        after_creation_time: Optional["capo_textract.types.date_time.DateTime"] = None,
        before_creation_time: Optional["capo_textract.types.date_time.DateTime"] = None,
        max_results: Optional["capo_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "capo_textract.types.list_adapter_versions_response.ListAdapterVersionsResponse"
    ):
        """<p>List all version of an adapter that meet the specified filtration criteria.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter to match for when listing adapter versions.</p>
            after_creation_time: <p>Specifies the lower bound for the ListAdapterVersions operation. Ensures ListAdapterVersions returns only adapter versions created after the specified creation time.</p>
            before_creation_time: <p>Specifies the upper bound for the ListAdapterVersions operation. Ensures ListAdapterVersions returns only adapter versions created after the specified creation time.</p>
            max_results: <p>The maximum number of results to return when listing adapter versions.</p>
            next_token: <p>Identifies the next page of results to return when listing adapter versions.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.resource_not_found_exception.ResourceNotFoundException: <p> Returned when an operation tried to access a nonexistent resource. </p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.list_adapter_versions_request.ListAdapterVersionsRequest]",
        ) -> OperationResponse[
            "capo_textract.types.list_adapter_versions_response.ListAdapterVersionsResponse"
        ]:
            import capo_textract._operations.textract.list_adapter_versions

            output, http_response = (
                capo_textract._operations.textract.list_adapter_versions.list_adapter_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.list_adapter_versions_request.ListAdapterVersionsRequest = {}
        if adapter_id is not None:
            input_["adapter_id"] = adapter_id
        if after_creation_time is not None:
            input_["after_creation_time"] = after_creation_time
        if before_creation_time is not None:
            input_["before_creation_time"] = before_creation_time
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

    def iter_list_adapter_versions(
        self,
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        adapter_id: Optional["capo_textract.types.adapter_id.AdapterId"] = None,
        after_creation_time: Optional["capo_textract.types.date_time.DateTime"] = None,
        before_creation_time: Optional["capo_textract.types.date_time.DateTime"] = None,
        max_results: Optional["capo_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "Iterator[capo_textract.types.adapter_version_overview.AdapterVersionOverview]"
    ):
        _token = next_token
        while True:
            _response = self.list_adapter_versions(
                config_overrides=config_overrides,
                adapter_id=adapter_id,
                after_creation_time=after_creation_time,
                before_creation_time=before_creation_time,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("adapter_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_textract.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags for an Amazon Textract resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that specifies the resource to list tags for.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.resource_not_found_exception.ResourceNotFoundException: <p> Returned when an operation tried to access a nonexistent resource. </p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_textract.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_textract._operations.textract.list_tags_for_resource

            output, http_response = (
                capo_textract._operations.textract.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_document_analysis(
        self,
        document_location: "capo_textract.types.document_location.DocumentLocation",
        feature_types: "capo_textract.types.feature_types.FeatureTypes",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        client_request_token: Optional[
            "capo_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        job_tag: Optional["capo_textract.types.job_tag.JobTag"] = None,
        notification_channel: Optional[
            "capo_textract.types.notification_channel.NotificationChannel"
        ] = None,
        output_config: Optional[
            "capo_textract.types.output_config.OutputConfig"
        ] = None,
        kms_key_id: Optional["capo_textract.types.kms_key_id.KMSKeyId"] = None,
        queries_config: Optional[
            "capo_textract.types.queries_config.QueriesConfig"
        ] = None,
        adapters_config: Optional[
            "capo_textract.types.adapters_config.AdaptersConfig"
        ] = None,
    ) -> "capo_textract.types.start_document_analysis_response.StartDocumentAnalysisResponse":
        """<p>Starts the asynchronous analysis of an input document for relationships between detected items such as key-value pairs, tables, and selection elements.</p> <p> <code>StartDocumentAnalysis</code> can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use <a>DocumentLocation</a> to specify the bucket name and file name of the document. </p> <p> <code>StartDocumentAnalysis</code> returns a job identifier (<code>JobId</code>) that you use to get the results of the operation. When text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in <code>NotificationChannel</code>. To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetDocumentAnalysis</a>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartDocumentAnalysis</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html">Document Text Analysis</a>.</p>

        Args:
            document_location: <p>The location of the document to be processed.</p>
            feature_types: <p>A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. To perform both types of analysis, add TABLES and FORMS to <code>FeatureTypes</code>. All lines and words detected in the document are included in the response (including text that isn't related to the value of <code>FeatureTypes</code>). </p>
            client_request_token: <p>The idempotent token that you use to identify the start request. If you use the same token with multiple <code>StartDocumentAnalysis</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentally started more than once. For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/api-async.html">Calling Amazon Textract Asynchronous Operations</a>.</p>
            job_tag: <p>An identifier that you specify that's included in the completion notification published to the Amazon SNS topic. For example, you can use <code>JobTag</code> to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).</p>
            notification_channel: <p>The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to. </p>
            output_config: <p>Sets if the output will go to a customer defined bucket. By default, Amazon Textract will save the results internally to be accessed by the GetDocumentAnalysis operation.</p>
            kms_key_id: <p>The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side,using SSE-S3.</p>
            adapters_config: <p>Specifies the adapter to be used when analyzing a document.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.bad_document_exception.BadDocumentException: <p>Amazon Textract isn't able to read the document. For more information on the document limits in Amazon Textract, see <a href="https://docs.aws.amazon.com/textract/latest/dg/limits.html">Hard limits</a>.</p>
            capo_textract.errors.document_too_large_exception.DocumentTooLargeException: <p>The document can't be processed because it's too large. The maximum document size for synchronous operations 10 MB. The maximum document size for asynchronous operations is 500 MB for PDF files.</p>
            capo_textract.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation. </p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_kms_key_exception.InvalidKMSKeyException: <p> Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key was entered incorrectly. </p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Textract service limit was exceeded. For example, if you start too many asynchronous jobs concurrently, calls to start operations (<code>StartDocumentTextDetection</code>, for example) raise a LimitExceededException exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Textract service limit. </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.unsupported_document_exception.UnsupportedDocumentException: <p>The format of the input document isn't supported. Documents for operations can be in PNG, JPEG, PDF, or TIFF format.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.start_document_analysis_request.StartDocumentAnalysisRequest]",
        ) -> OperationResponse[
            "capo_textract.types.start_document_analysis_response.StartDocumentAnalysisResponse"
        ]:
            import capo_textract._operations.textract.start_document_analysis

            output, http_response = (
                capo_textract._operations.textract.start_document_analysis.start_document_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.start_document_analysis_request.StartDocumentAnalysisRequest = {
            "document_location": document_location,
            "feature_types": feature_types,
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if output_config is not None:
            input_["output_config"] = output_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if queries_config is not None:
            input_["queries_config"] = queries_config
        if adapters_config is not None:
            input_["adapters_config"] = adapters_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_document_text_detection(
        self,
        document_location: "capo_textract.types.document_location.DocumentLocation",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        client_request_token: Optional[
            "capo_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        job_tag: Optional["capo_textract.types.job_tag.JobTag"] = None,
        notification_channel: Optional[
            "capo_textract.types.notification_channel.NotificationChannel"
        ] = None,
        output_config: Optional[
            "capo_textract.types.output_config.OutputConfig"
        ] = None,
        kms_key_id: Optional["capo_textract.types.kms_key_id.KMSKeyId"] = None,
    ) -> "capo_textract.types.start_document_text_detection_response.StartDocumentTextDetectionResponse":
        """<p>Starts the asynchronous detection of text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.</p> <p> <code>StartDocumentTextDetection</code> can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use <a>DocumentLocation</a> to specify the bucket name and file name of the document. </p> <p> <code>StartDocumentTextDetection</code> returns a job identifier (<code>JobId</code>) that you use to get the results of the operation. When text detection is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in <code>NotificationChannel</code>. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetDocumentTextDetection</a>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartDocumentTextDetection</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html">Document Text Detection</a>.</p>

        Args:
            document_location: <p>The location of the document to be processed.</p>
            client_request_token: <p>The idempotent token that's used to identify the start request. If you use the same token with multiple <code>StartDocumentTextDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentally started more than once. For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/api-async.html">Calling Amazon Textract Asynchronous Operations</a>.</p>
            job_tag: <p>An identifier that you specify that's included in the completion notification published to the Amazon SNS topic. For example, you can use <code>JobTag</code> to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).</p>
            notification_channel: <p>The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to. </p>
            output_config: <p>Sets if the output will go to a customer defined bucket. By default Amazon Textract will save the results internally to be accessed with the GetDocumentTextDetection operation.</p>
            kms_key_id: <p>The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side,using SSE-S3.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.bad_document_exception.BadDocumentException: <p>Amazon Textract isn't able to read the document. For more information on the document limits in Amazon Textract, see <a href="https://docs.aws.amazon.com/textract/latest/dg/limits.html">Hard limits</a>.</p>
            capo_textract.errors.document_too_large_exception.DocumentTooLargeException: <p>The document can't be processed because it's too large. The maximum document size for synchronous operations 10 MB. The maximum document size for asynchronous operations is 500 MB for PDF files.</p>
            capo_textract.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation. </p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_kms_key_exception.InvalidKMSKeyException: <p> Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key was entered incorrectly. </p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Textract service limit was exceeded. For example, if you start too many asynchronous jobs concurrently, calls to start operations (<code>StartDocumentTextDetection</code>, for example) raise a LimitExceededException exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Textract service limit. </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.unsupported_document_exception.UnsupportedDocumentException: <p>The format of the input document isn't supported. Documents for operations can be in PNG, JPEG, PDF, or TIFF format.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.start_document_text_detection_request.StartDocumentTextDetectionRequest]",
        ) -> OperationResponse[
            "capo_textract.types.start_document_text_detection_response.StartDocumentTextDetectionResponse"
        ]:
            import capo_textract._operations.textract.start_document_text_detection

            output, http_response = (
                capo_textract._operations.textract.start_document_text_detection.start_document_text_detection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.start_document_text_detection_request.StartDocumentTextDetectionRequest = {
            "document_location": document_location
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if output_config is not None:
            input_["output_config"] = output_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_expense_analysis(
        self,
        document_location: "capo_textract.types.document_location.DocumentLocation",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        client_request_token: Optional[
            "capo_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        job_tag: Optional["capo_textract.types.job_tag.JobTag"] = None,
        notification_channel: Optional[
            "capo_textract.types.notification_channel.NotificationChannel"
        ] = None,
        output_config: Optional[
            "capo_textract.types.output_config.OutputConfig"
        ] = None,
        kms_key_id: Optional["capo_textract.types.kms_key_id.KMSKeyId"] = None,
    ) -> "capo_textract.types.start_expense_analysis_response.StartExpenseAnalysisResponse":
        """<p>Starts the asynchronous analysis of invoices or receipts for data like contact information, items purchased, and vendor names.</p> <p> <code>StartExpenseAnalysis</code> can analyze text in documents that are in JPEG, PNG, and PDF format. The documents must be stored in an Amazon S3 bucket. Use the <a>DocumentLocation</a> parameter to specify the name of your S3 bucket and the name of the document in that bucket. </p> <p> <code>StartExpenseAnalysis</code> returns a job identifier (<code>JobId</code>) that you will provide to <code>GetExpenseAnalysis</code> to retrieve the results of the operation. When the analysis of the input invoices/receipts is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you provide to the <code>NotificationChannel</code>. To obtain the results of the invoice and receipt analysis operation, ensure that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetExpenseAnalysis</a>, and pass the job identifier (<code>JobId</code>) that was returned by your call to <code>StartExpenseAnalysis</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/invoice-receipts.html">Analyzing Invoices and Receipts</a>.</p>

        Args:
            document_location: <p>The location of the document to be processed.</p>
            client_request_token: <p>The idempotent token that's used to identify the start request. If you use the same token with multiple <code>StartDocumentTextDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentally started more than once. For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/api-async.html">Calling Amazon Textract Asynchronous Operations</a> </p>
            job_tag: <p>An identifier you specify that's included in the completion notification published to the Amazon SNS topic. For example, you can use <code>JobTag</code> to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).</p>
            notification_channel: <p>The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to. </p>
            output_config: <p>Sets if the output will go to a customer defined bucket. By default, Amazon Textract will save the results internally to be accessed by the <code>GetExpenseAnalysis</code> operation.</p>
            kms_key_id: <p>The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side,using SSE-S3.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.bad_document_exception.BadDocumentException: <p>Amazon Textract isn't able to read the document. For more information on the document limits in Amazon Textract, see <a href="https://docs.aws.amazon.com/textract/latest/dg/limits.html">Hard limits</a>.</p>
            capo_textract.errors.document_too_large_exception.DocumentTooLargeException: <p>The document can't be processed because it's too large. The maximum document size for synchronous operations 10 MB. The maximum document size for asynchronous operations is 500 MB for PDF files.</p>
            capo_textract.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation. </p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_kms_key_exception.InvalidKMSKeyException: <p> Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key was entered incorrectly. </p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Textract service limit was exceeded. For example, if you start too many asynchronous jobs concurrently, calls to start operations (<code>StartDocumentTextDetection</code>, for example) raise a LimitExceededException exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Textract service limit. </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.unsupported_document_exception.UnsupportedDocumentException: <p>The format of the input document isn't supported. Documents for operations can be in PNG, JPEG, PDF, or TIFF format.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.start_expense_analysis_request.StartExpenseAnalysisRequest]",
        ) -> OperationResponse[
            "capo_textract.types.start_expense_analysis_response.StartExpenseAnalysisResponse"
        ]:
            import capo_textract._operations.textract.start_expense_analysis

            output, http_response = (
                capo_textract._operations.textract.start_expense_analysis.start_expense_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.start_expense_analysis_request.StartExpenseAnalysisRequest = {
            "document_location": document_location
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if output_config is not None:
            input_["output_config"] = output_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_lending_analysis(
        self,
        document_location: "capo_textract.types.document_location.DocumentLocation",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        client_request_token: Optional[
            "capo_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        job_tag: Optional["capo_textract.types.job_tag.JobTag"] = None,
        notification_channel: Optional[
            "capo_textract.types.notification_channel.NotificationChannel"
        ] = None,
        output_config: Optional[
            "capo_textract.types.output_config.OutputConfig"
        ] = None,
        kms_key_id: Optional["capo_textract.types.kms_key_id.KMSKeyId"] = None,
    ) -> "capo_textract.types.start_lending_analysis_response.StartLendingAnalysisResponse":
        """<p>Starts the classification and analysis of an input document. <code>StartLendingAnalysis</code> initiates the classification and analysis of a packet of lending documents. <code>StartLendingAnalysis</code> operates on a document file located in an Amazon S3 bucket.</p> <p> <code>StartLendingAnalysis</code> can analyze text in documents that are in one of the following formats: JPEG, PNG, TIFF, PDF. Use <code>DocumentLocation</code> to specify the bucket name and the file name of the document. </p> <p> <code>StartLendingAnalysis</code> returns a job identifier (<code>JobId</code>) that you use to get the results of the operation. When the text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in <code>NotificationChannel</code>. To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If the status is SUCCEEDED you can call either <code>GetLendingAnalysis</code> or <code>GetLendingAnalysisSummary</code> and provide the <code>JobId</code> to obtain the results of the analysis.</p> <p>If using <code>OutputConfig</code> to specify an Amazon S3 bucket, the output will be contained within the specified prefix in a directory labeled with the job-id. In the directory there are 3 sub-directories: </p> <ul> <li> <p>detailedResponse (contains the GetLendingAnalysis response)</p> </li> <li> <p>summaryResponse (for the GetLendingAnalysisSummary response)</p> </li> <li> <p>splitDocuments (documents split across logical boundaries)</p> </li> </ul>

        Args:
            client_request_token: <p>The idempotent token that you use to identify the start request. If you use the same token with multiple <code>StartLendingAnalysis</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentally started more than once. For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/api-sync.html">Calling Amazon Textract Asynchronous Operations</a>.</p>
            job_tag: <p>An identifier that you specify to be included in the completion notification published to the Amazon SNS topic. For example, you can use <code>JobTag</code> to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).</p>
            kms_key_id: <p>The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side, using SSE-S3. </p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.bad_document_exception.BadDocumentException: <p>Amazon Textract isn't able to read the document. For more information on the document limits in Amazon Textract, see <a href="https://docs.aws.amazon.com/textract/latest/dg/limits.html">Hard limits</a>.</p>
            capo_textract.errors.document_too_large_exception.DocumentTooLargeException: <p>The document can't be processed because it's too large. The maximum document size for synchronous operations 10 MB. The maximum document size for asynchronous operations is 500 MB for PDF files.</p>
            capo_textract.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation. </p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_kms_key_exception.InvalidKMSKeyException: <p> Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key was entered incorrectly. </p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Textract is unable to access the S3 object that's specified in the request. for more information, <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html">Configure Access to Amazon S3</a> For troubleshooting information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html">Troubleshooting Amazon S3</a> </p>
            capo_textract.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Textract service limit was exceeded. For example, if you start too many asynchronous jobs concurrently, calls to start operations (<code>StartDocumentTextDetection</code>, for example) raise a LimitExceededException exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Textract service limit. </p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.unsupported_document_exception.UnsupportedDocumentException: <p>The format of the input document isn't supported. Documents for operations can be in PNG, JPEG, PDF, or TIFF format.</p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.start_lending_analysis_request.StartLendingAnalysisRequest]",
        ) -> OperationResponse[
            "capo_textract.types.start_lending_analysis_response.StartLendingAnalysisResponse"
        ]:
            import capo_textract._operations.textract.start_lending_analysis

            output, http_response = (
                capo_textract._operations.textract.start_lending_analysis.start_lending_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.start_lending_analysis_request.StartLendingAnalysisRequest = {
            "document_location": document_location
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if output_config is not None:
            input_["output_config"] = output_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_textract.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_textract.types.tag_map.TagMap",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that specifies the resource to be tagged.</p>
            tags: <p>A set of tags (key-value pairs) that you want to assign to the resource.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.resource_not_found_exception.ResourceNotFoundException: <p> Returned when an operation tried to access a nonexistent resource. </p>
            capo_textract.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Returned when a request cannot be completed as it would exceed a maximum service quota.</p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_textract.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_textract._operations.textract.tag_resource

            output, http_response = (
                capo_textract._operations.textract.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
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
        resource_arn: "capo_textract.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_textract.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
    ) -> "capo_textract.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes any tags with the specified keys from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that specifies the resource to be untagged.</p>
            tag_keys: <p>Specifies the tags to be removed from the resource specified by the ResourceARN.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.resource_not_found_exception.ResourceNotFoundException: <p> Returned when an operation tried to access a nonexistent resource. </p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_textract.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_textract._operations.textract.untag_resource

            output, http_response = (
                capo_textract._operations.textract.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_adapter(
        self,
        adapter_id: "capo_textract.types.adapter_id.AdapterId",
        *,
        config_overrides: Optional[TextractClientConfig] = None,
        description: Optional[
            "capo_textract.types.adapter_description.AdapterDescription"
        ] = None,
        adapter_name: Optional["capo_textract.types.adapter_name.AdapterName"] = None,
        auto_update: Optional["capo_textract.types.auto_update.AutoUpdate"] = None,
    ) -> "capo_textract.types.update_adapter_response.UpdateAdapterResponse":
        """<p>Update the configuration for an adapter. FeatureTypes configurations cannot be updated. At least one new parameter must be specified as an argument.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter that will be updated.</p>
            description: <p>The new description to be applied to the adapter.</p>
            adapter_name: <p>The new name to be applied to the adapter.</p>
            auto_update: <p>The new auto-update status to be applied to the adapter.</p>

        Raises:
            capo_textract.errors.access_denied_exception.AccessDeniedException: <p>You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.</p>
            capo_textract.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_textract.errors.internal_server_error.InternalServerError: <p>Amazon Textract experienced a service issue. Try your call again.</p>
            capo_textract.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter violated a constraint. For example, in synchronous operations, an <code>InvalidParameterException</code> exception occurs when neither of the <code>S3Object</code> or <code>Bytes</code> values are supplied in the <code>Document</code> request parameter. Validate your parameter before calling the API operation again.</p>
            capo_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.</p>
            capo_textract.errors.resource_not_found_exception.ResourceNotFoundException: <p> Returned when an operation tried to access a nonexistent resource. </p>
            capo_textract.errors.throttling_exception.ThrottlingException: <p>Amazon Textract is temporarily unable to process the request. Try your call again.</p>
            capo_textract.errors.validation_exception.ValidationException: <p> Indicates that a request was not valid. Check request for proper formatting. </p>
            capo_textract.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_textract.types.update_adapter_request.UpdateAdapterRequest]",
        ) -> OperationResponse[
            "capo_textract.types.update_adapter_response.UpdateAdapterResponse"
        ]:
            import capo_textract._operations.textract.update_adapter

            output, http_response = (
                capo_textract._operations.textract.update_adapter.update_adapter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_textract.types.update_adapter_request.UpdateAdapterRequest = {
            "adapter_id": adapter_id
        }
        if description is not None:
            input_["description"] = description
        if adapter_name is not None:
            input_["adapter_name"] = adapter_name
        if auto_update is not None:
            input_["auto_update"] = auto_update

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
