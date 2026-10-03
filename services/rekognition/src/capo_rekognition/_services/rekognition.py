"""Generated from Smithy shape ``com.amazonaws.rekognition#RekognitionService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_rekognition._auth._signers
import capo_rekognition._auth._sigv4
from capo_rekognition._auth._identity import Credentials
from capo_rekognition._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_rekognition._auth._zapros_handler import AuthMiddleware
from capo_rekognition._pagination import resolve_path as _resolve_path
from capo_rekognition._services._aws_config import aws_config
from capo_rekognition._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_rekognition.types.associate_faces_request
    import capo_rekognition.types.associate_faces_response
    import capo_rekognition.types.attributes
    import capo_rekognition.types.celebrity_recognition_sort_by
    import capo_rekognition.types.client_request_token
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.compare_faces_request
    import capo_rekognition.types.compare_faces_response
    import capo_rekognition.types.content_moderation_aggregate_by
    import capo_rekognition.types.content_moderation_sort_by
    import capo_rekognition.types.copy_project_version_request
    import capo_rekognition.types.copy_project_version_response
    import capo_rekognition.types.create_collection_request
    import capo_rekognition.types.create_collection_response
    import capo_rekognition.types.create_dataset_request
    import capo_rekognition.types.create_dataset_response
    import capo_rekognition.types.create_face_liveness_session_request
    import capo_rekognition.types.create_face_liveness_session_request_settings
    import capo_rekognition.types.create_face_liveness_session_response
    import capo_rekognition.types.create_project_request
    import capo_rekognition.types.create_project_response
    import capo_rekognition.types.create_project_version_request
    import capo_rekognition.types.create_project_version_response
    import capo_rekognition.types.create_stream_processor_request
    import capo_rekognition.types.create_stream_processor_response
    import capo_rekognition.types.create_user_request
    import capo_rekognition.types.create_user_response
    import capo_rekognition.types.customization_feature
    import capo_rekognition.types.customization_feature_config
    import capo_rekognition.types.customization_features
    import capo_rekognition.types.dataset_arn
    import capo_rekognition.types.dataset_changes
    import capo_rekognition.types.dataset_entry
    import capo_rekognition.types.dataset_label_description
    import capo_rekognition.types.dataset_labels
    import capo_rekognition.types.dataset_source
    import capo_rekognition.types.dataset_type
    import capo_rekognition.types.delete_collection_request
    import capo_rekognition.types.delete_collection_response
    import capo_rekognition.types.delete_dataset_request
    import capo_rekognition.types.delete_dataset_response
    import capo_rekognition.types.delete_faces_request
    import capo_rekognition.types.delete_faces_response
    import capo_rekognition.types.delete_project_policy_request
    import capo_rekognition.types.delete_project_policy_response
    import capo_rekognition.types.delete_project_request
    import capo_rekognition.types.delete_project_response
    import capo_rekognition.types.delete_project_version_request
    import capo_rekognition.types.delete_project_version_response
    import capo_rekognition.types.delete_stream_processor_request
    import capo_rekognition.types.delete_stream_processor_response
    import capo_rekognition.types.delete_user_request
    import capo_rekognition.types.delete_user_response
    import capo_rekognition.types.describe_collection_request
    import capo_rekognition.types.describe_collection_response
    import capo_rekognition.types.describe_dataset_request
    import capo_rekognition.types.describe_dataset_response
    import capo_rekognition.types.describe_project_versions_request
    import capo_rekognition.types.describe_project_versions_response
    import capo_rekognition.types.describe_projects_request
    import capo_rekognition.types.describe_projects_response
    import capo_rekognition.types.describe_stream_processor_request
    import capo_rekognition.types.describe_stream_processor_response
    import capo_rekognition.types.detect_custom_labels_request
    import capo_rekognition.types.detect_custom_labels_response
    import capo_rekognition.types.detect_faces_request
    import capo_rekognition.types.detect_faces_response
    import capo_rekognition.types.detect_labels_feature_list
    import capo_rekognition.types.detect_labels_request
    import capo_rekognition.types.detect_labels_response
    import capo_rekognition.types.detect_labels_settings
    import capo_rekognition.types.detect_moderation_labels_request
    import capo_rekognition.types.detect_moderation_labels_response
    import capo_rekognition.types.detect_protective_equipment_request
    import capo_rekognition.types.detect_protective_equipment_response
    import capo_rekognition.types.detect_text_filters
    import capo_rekognition.types.detect_text_request
    import capo_rekognition.types.detect_text_response
    import capo_rekognition.types.disassociate_faces_request
    import capo_rekognition.types.disassociate_faces_response
    import capo_rekognition.types.distribute_dataset_entries_request
    import capo_rekognition.types.distribute_dataset_entries_response
    import capo_rekognition.types.distribute_dataset_metadata_list
    import capo_rekognition.types.extended_pagination_token
    import capo_rekognition.types.external_image_id
    import capo_rekognition.types.face
    import capo_rekognition.types.face_attributes
    import capo_rekognition.types.face_id
    import capo_rekognition.types.face_id_list
    import capo_rekognition.types.face_search_sort_by
    import capo_rekognition.types.get_celebrity_info_request
    import capo_rekognition.types.get_celebrity_info_response
    import capo_rekognition.types.get_celebrity_recognition_request
    import capo_rekognition.types.get_celebrity_recognition_response
    import capo_rekognition.types.get_content_moderation_request
    import capo_rekognition.types.get_content_moderation_response
    import capo_rekognition.types.get_face_detection_request
    import capo_rekognition.types.get_face_detection_response
    import capo_rekognition.types.get_face_liveness_session_results_request
    import capo_rekognition.types.get_face_liveness_session_results_response
    import capo_rekognition.types.get_face_search_request
    import capo_rekognition.types.get_face_search_response
    import capo_rekognition.types.get_label_detection_request
    import capo_rekognition.types.get_label_detection_response
    import capo_rekognition.types.get_media_analysis_job_request
    import capo_rekognition.types.get_media_analysis_job_response
    import capo_rekognition.types.get_person_tracking_request
    import capo_rekognition.types.get_person_tracking_response
    import capo_rekognition.types.get_segment_detection_request
    import capo_rekognition.types.get_segment_detection_response
    import capo_rekognition.types.get_text_detection_request
    import capo_rekognition.types.get_text_detection_response
    import capo_rekognition.types.has_errors
    import capo_rekognition.types.human_loop_config
    import capo_rekognition.types.image
    import capo_rekognition.types.index_faces_request
    import capo_rekognition.types.index_faces_response
    import capo_rekognition.types.inference_units
    import capo_rekognition.types.is_labeled
    import capo_rekognition.types.job_id
    import capo_rekognition.types.job_tag
    import capo_rekognition.types.kms_key_id
    import capo_rekognition.types.label_detection_aggregate_by
    import capo_rekognition.types.label_detection_feature_list
    import capo_rekognition.types.label_detection_settings
    import capo_rekognition.types.label_detection_sort_by
    import capo_rekognition.types.list_collections_request
    import capo_rekognition.types.list_collections_response
    import capo_rekognition.types.list_dataset_entries_page_size
    import capo_rekognition.types.list_dataset_entries_request
    import capo_rekognition.types.list_dataset_entries_response
    import capo_rekognition.types.list_dataset_labels_page_size
    import capo_rekognition.types.list_dataset_labels_request
    import capo_rekognition.types.list_dataset_labels_response
    import capo_rekognition.types.list_faces_request
    import capo_rekognition.types.list_faces_response
    import capo_rekognition.types.list_media_analysis_jobs_page_size
    import capo_rekognition.types.list_media_analysis_jobs_request
    import capo_rekognition.types.list_media_analysis_jobs_response
    import capo_rekognition.types.list_project_policies_page_size
    import capo_rekognition.types.list_project_policies_request
    import capo_rekognition.types.list_project_policies_response
    import capo_rekognition.types.list_stream_processors_request
    import capo_rekognition.types.list_stream_processors_response
    import capo_rekognition.types.list_tags_for_resource_request
    import capo_rekognition.types.list_tags_for_resource_response
    import capo_rekognition.types.list_users_request
    import capo_rekognition.types.list_users_response
    import capo_rekognition.types.liveness_session_id
    import capo_rekognition.types.max_faces
    import capo_rekognition.types.max_faces_to_index
    import capo_rekognition.types.max_results
    import capo_rekognition.types.max_user_results
    import capo_rekognition.types.media_analysis_input
    import capo_rekognition.types.media_analysis_job_id
    import capo_rekognition.types.media_analysis_job_name
    import capo_rekognition.types.media_analysis_operations_config
    import capo_rekognition.types.media_analysis_output_config
    import capo_rekognition.types.notification_channel
    import capo_rekognition.types.output_config
    import capo_rekognition.types.page_size
    import capo_rekognition.types.pagination_token
    import capo_rekognition.types.percent
    import capo_rekognition.types.person_tracking_sort_by
    import capo_rekognition.types.project_arn
    import capo_rekognition.types.project_auto_update
    import capo_rekognition.types.project_description
    import capo_rekognition.types.project_name
    import capo_rekognition.types.project_names
    import capo_rekognition.types.project_policy
    import capo_rekognition.types.project_policy_document
    import capo_rekognition.types.project_policy_name
    import capo_rekognition.types.project_policy_revision_id
    import capo_rekognition.types.project_version_arn
    import capo_rekognition.types.project_version_description
    import capo_rekognition.types.project_version_id
    import capo_rekognition.types.project_versions_page_size
    import capo_rekognition.types.projects_page_size
    import capo_rekognition.types.protective_equipment_summarization_attributes
    import capo_rekognition.types.put_project_policy_request
    import capo_rekognition.types.put_project_policy_response
    import capo_rekognition.types.quality_filter
    import capo_rekognition.types.query_string
    import capo_rekognition.types.recognize_celebrities_request
    import capo_rekognition.types.recognize_celebrities_response
    import capo_rekognition.types.regions_of_interest
    import capo_rekognition.types.rekognition_unique_id
    import capo_rekognition.types.resource_arn
    import capo_rekognition.types.role_arn
    import capo_rekognition.types.search_faces_by_image_request
    import capo_rekognition.types.search_faces_by_image_response
    import capo_rekognition.types.search_faces_request
    import capo_rekognition.types.search_faces_response
    import capo_rekognition.types.search_users_by_image_request
    import capo_rekognition.types.search_users_by_image_response
    import capo_rekognition.types.search_users_request
    import capo_rekognition.types.search_users_response
    import capo_rekognition.types.segment_types
    import capo_rekognition.types.start_celebrity_recognition_request
    import capo_rekognition.types.start_celebrity_recognition_response
    import capo_rekognition.types.start_content_moderation_request
    import capo_rekognition.types.start_content_moderation_response
    import capo_rekognition.types.start_face_detection_request
    import capo_rekognition.types.start_face_detection_response
    import capo_rekognition.types.start_face_search_request
    import capo_rekognition.types.start_face_search_response
    import capo_rekognition.types.start_label_detection_request
    import capo_rekognition.types.start_label_detection_response
    import capo_rekognition.types.start_media_analysis_job_request
    import capo_rekognition.types.start_media_analysis_job_response
    import capo_rekognition.types.start_person_tracking_request
    import capo_rekognition.types.start_person_tracking_response
    import capo_rekognition.types.start_project_version_request
    import capo_rekognition.types.start_project_version_response
    import capo_rekognition.types.start_segment_detection_filters
    import capo_rekognition.types.start_segment_detection_request
    import capo_rekognition.types.start_segment_detection_response
    import capo_rekognition.types.start_stream_processor_request
    import capo_rekognition.types.start_stream_processor_response
    import capo_rekognition.types.start_text_detection_filters
    import capo_rekognition.types.start_text_detection_request
    import capo_rekognition.types.start_text_detection_response
    import capo_rekognition.types.stop_project_version_request
    import capo_rekognition.types.stop_project_version_response
    import capo_rekognition.types.stop_stream_processor_request
    import capo_rekognition.types.stop_stream_processor_response
    import capo_rekognition.types.stream_processing_start_selector
    import capo_rekognition.types.stream_processing_stop_selector
    import capo_rekognition.types.stream_processor_data_sharing_preference
    import capo_rekognition.types.stream_processor_input
    import capo_rekognition.types.stream_processor_name
    import capo_rekognition.types.stream_processor_notification_channel
    import capo_rekognition.types.stream_processor_output
    import capo_rekognition.types.stream_processor_parameters_to_delete
    import capo_rekognition.types.stream_processor_settings
    import capo_rekognition.types.stream_processor_settings_for_update
    import capo_rekognition.types.tag_key_list
    import capo_rekognition.types.tag_map
    import capo_rekognition.types.tag_resource_request
    import capo_rekognition.types.tag_resource_response
    import capo_rekognition.types.testing_data
    import capo_rekognition.types.training_data
    import capo_rekognition.types.u_integer
    import capo_rekognition.types.untag_resource_request
    import capo_rekognition.types.untag_resource_response
    import capo_rekognition.types.update_dataset_entries_request
    import capo_rekognition.types.update_dataset_entries_response
    import capo_rekognition.types.update_stream_processor_request
    import capo_rekognition.types.update_stream_processor_response
    import capo_rekognition.types.user
    import capo_rekognition.types.user_face_id_list
    import capo_rekognition.types.user_id
    import capo_rekognition.types.version_description
    import capo_rekognition.types.version_name
    import capo_rekognition.types.version_names
    import capo_rekognition.types.video


class RekognitionClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class RekognitionClient:
    """A client for the ``Rekognition`` service.

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
        self._config = RekognitionClientConfig(
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
        self, config_overrides: Optional[RekognitionClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: RekognitionClientConfig = config_overrides or {}
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

    def associate_faces(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        user_id: "capo_rekognition.types.user_id.UserId",
        face_ids: "capo_rekognition.types.user_face_id_list.UserFaceIdList",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        user_match_threshold: Optional["capo_rekognition.types.percent.Percent"] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_rekognition.types.associate_faces_response.AssociateFacesResponse":
        """<p>Associates one or more faces with an existing UserID. Takes an array of <code>FaceIds</code>. Each <code>FaceId</code> that are present in the <code>FaceIds</code> list is associated with the provided UserID. The number of FaceIds that can be used as input in a single request is limited to 100.</p> <p>Note that the total number of faces that can be associated with a single <code>UserID</code> is also limited to 100. Once a <code>UserID</code> has 100 faces associated with it, no additional faces can be added. If more API calls are made after the limit is reached, a <code>ServiceQuotaExceededException</code> will result.</p> <p>The <code>UserMatchThreshold</code> parameter specifies the minimum user match confidence required for the face to be associated with a UserID that has at least one <code>FaceID</code> already associated. This ensures that the <code>FaceIds</code> are associated with the right UserID. The value ranges from 0-100 and default value is 75. </p> <p>If successful, an array of <code>AssociatedFace</code> objects containing the associated <code>FaceIds</code> is returned. If a given face is already associated with the given <code>UserID</code>, it will be ignored and will not be returned in the response. If a given face is already associated to a different <code>UserID</code>, isn't found in the collection, doesn’t meet the <code>UserMatchThreshold</code>, or there are already 100 faces associated with the <code>UserID</code>, it will be returned as part of an array of <code>UnsuccessfulFaceAssociations.</code> </p> <p>The <code>UserStatus</code> reflects the status of an operation which updates a UserID representation with a list of given faces. The <code>UserStatus</code> can be: </p> <ul> <li> <p>ACTIVE - All associations or disassociations of FaceID(s) for a UserID are complete.</p> </li> <li> <p>CREATED - A UserID has been created, but has no FaceID(s) associated with it.</p> </li> <li> <p>UPDATING - A UserID is being updated and there are current associations or disassociations of FaceID(s) taking place.</p> </li> </ul>

        Args:
            collection_id: <p>The ID of an existing collection containing the UserID.</p>
            user_id: <p>The ID for the existing UserID.</p>
            face_ids: <p>An array of FaceIDs to associate with the UserID.</p>
            user_match_threshold: <p>An optional value specifying the minimum confidence in the UserID match to return. The default value is 75.</p>
            client_request_token: <p>Idempotent token used to identify the request to <code>AssociateFaces</code>. If you use the same token with multiple <code>AssociateFaces</code> requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.conflict_exception.ConflictException: <p> A User with the same Id already exists within the collection, or the update or deletion of the User caused an inconsistent state. ** </p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p></p> <p>The size of the collection exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            AssociateFaces
            This operation associates one or more faces with an existing UserID.

            >>> client.associate_faces(collection_id='MyCollection', user_id='DemoUser', face_ids=['f5817d37-94f6-4335-bfee-6cf79a3d806e', '851cb847-dccc-4fea-9309-9f4805967855', '35ebbb41-7f67-4263-908d-dd0ecba05ab9'], user_match_threshold=70, client_request_token='550e8400-e29b-41d4-a716-446655440002')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.associate_faces_request.AssociateFacesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.associate_faces_response.AssociateFacesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.associate_faces

            output, http_response = (
                capo_rekognition._operations.rekognition_service.associate_faces.associate_faces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.associate_faces_request.AssociateFacesRequest = {
            "collection_id": collection_id,
            "user_id": user_id,
            "face_ids": face_ids,
        }
        if user_match_threshold is not None:
            input_["user_match_threshold"] = user_match_threshold
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def compare_faces(
        self,
        source_image: "capo_rekognition.types.image.Image",
        target_image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        similarity_threshold: Optional["capo_rekognition.types.percent.Percent"] = None,
        quality_filter: Optional[
            "capo_rekognition.types.quality_filter.QualityFilter"
        ] = None,
    ) -> "capo_rekognition.types.compare_faces_response.CompareFacesResponse":
        """<p>Compares a face in the <i>source</i> input image with each of the 100 largest faces detected in the <i>target</i> input image. </p> <p> If the source image contains multiple faces, the service detects the largest face and compares it with each face detected in the target image. </p> <note> <p>CompareFaces uses machine learning algorithms, which are probabilistic. A false negative is an incorrect prediction that a face in the target image has a low similarity confidence score when compared to the face in the source image. To reduce the probability of false negatives, we recommend that you compare the target image against multiple source images. If you plan to use <code>CompareFaces</code> to make a decision that impacts an individual's rights, privacy, or access to services, we recommend that you pass the result to a human for review and further validation before taking action.</p> </note> <p>You pass the input and target images either as base64-encoded image bytes or as references to images in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn't supported. The image must be formatted as a PNG or JPEG file. </p> <p>In response, the operation returns an array of face matches ordered by similarity score in descending order. For each face match, the response provides a bounding box of the face, facial landmarks, pose details (pitch, roll, and yaw), quality (brightness and sharpness), and confidence value (indicating the level of confidence that the bounding box contains a face). The response also provides a similarity score, which indicates how closely the faces match. </p> <note> <p>By default, only faces with a similarity score of greater than or equal to 80% are returned in the response. You can change this value by specifying the <code>SimilarityThreshold</code> parameter.</p> </note> <p> <code>CompareFaces</code> also returns an array of faces that don't match the source image. For each face, it returns a bounding box, confidence value, landmarks, pose details, and quality. The response also returns information about the face in the source image, including the bounding box of the face and confidence value.</p> <p>The <code>QualityFilter</code> input parameter allows you to filter out detected faces that don’t meet a required quality bar. The quality bar is based on a variety of common use cases. Use <code>QualityFilter</code> to set the quality bar by specifying <code>LOW</code>, <code>MEDIUM</code>, or <code>HIGH</code>. If you do not want to filter detected faces, specify <code>NONE</code>. The default value is <code>NONE</code>. </p> <p>If the image doesn't contain Exif metadata, <code>CompareFaces</code> returns orientation information for the source and target images. Use these values to display the images with the correct image orientation.</p> <p>If no faces are detected in the source or target images, <code>CompareFaces</code> returns an <code>InvalidParameterException</code> error. </p> <note> <p> This is a stateless API operation. That is, data returned by this operation doesn't persist.</p> </note> <p>For an example, see Comparing Faces in Images in the Amazon Rekognition Developer Guide.</p> <p>This operation requires permissions to perform the <code>rekognition:CompareFaces</code> action.</p>

        Args:
            source_image: <p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>
            target_image: <p>The target image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>
            similarity_threshold: <p>The minimum level of confidence in the face matches that a match must meet to be included in the <code>FaceMatches</code> array.</p>
            quality_filter: <p>A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren't compared. If you specify <code>AUTO</code>, Amazon Rekognition chooses the quality bar. If you specify <code>LOW</code>, <code>MEDIUM</code>, or <code>HIGH</code>, filtering removes all faces that don’t meet the chosen quality bar. The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object that's misidentified as a face, a face that's too blurry, or a face with a pose that's too extreme to use. If you specify <code>NONE</code>, no filtering is performed. The default value is <code>NONE</code>. </p> <p>To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To compare two images
            This operation compares the largest face detected in the source image with each face detected in the target image.

            >>> client.compare_faces(source_image={'S3Object': {'Bucket': 'mybucket', 'Name': 'mysourceimage'}}, target_image={'S3Object': {'Bucket': 'mybucket', 'Name': 'mytargetimage'}}, similarity_threshold=90)
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.compare_faces_request.CompareFacesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.compare_faces_response.CompareFacesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.compare_faces

            output, http_response = (
                capo_rekognition._operations.rekognition_service.compare_faces.compare_faces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.compare_faces_request.CompareFacesRequest = {
            "source_image": source_image,
            "target_image": target_image,
        }
        if similarity_threshold is not None:
            input_["similarity_threshold"] = similarity_threshold
        if quality_filter is not None:
            input_["quality_filter"] = quality_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def copy_project_version(
        self,
        source_project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        source_project_version_arn: "capo_rekognition.types.project_version_arn.ProjectVersionArn",
        destination_project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        version_name: "capo_rekognition.types.version_name.VersionName",
        output_config: "capo_rekognition.types.output_config.OutputConfig",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        tags: Optional["capo_rekognition.types.tag_map.TagMap"] = None,
        kms_key_id: Optional["capo_rekognition.types.kms_key_id.KmsKeyId"] = None,
    ) -> "capo_rekognition.types.copy_project_version_response.CopyProjectVersionResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Copies a version of an Amazon Rekognition Custom Labels model from a source project to a destination project. The source and destination projects can be in different AWS accounts but must be in the same AWS Region. You can't copy a model to another AWS service. </p> <p>To copy a model version to a different AWS account, you need to create a resource-based policy known as a <i>project policy</i>. You attach the project policy to the source project by calling <a>PutProjectPolicy</a>. The project policy gives permission to copy the model version from a trusting AWS account to a trusted account.</p> <p>For more information creating and attaching a project policy, see Attaching a project policy (SDK) in the <i>Amazon Rekognition Custom Labels Developer Guide</i>. </p> <p>If you are copying a model version to a project in the same AWS account, you don't need to create a project policy.</p> <note> <p>Copying project versions is supported only for Custom Labels models. </p> <p>To copy a model, the destination project, source project, and source model version must already exist.</p> </note> <p>Copying a model version takes a while to complete. To get the current status, call <a>DescribeProjectVersions</a> and check the value of <code>Status</code> in the <a>ProjectVersionDescription</a> object. The copy operation has finished when the value of <code>Status</code> is <code>COPYING_COMPLETED</code>.</p> <p>This operation requires permissions to perform the <code>rekognition:CopyProjectVersion</code> action.</p>

        Args:
            source_project_arn: <p>The ARN of the source project in the trusting AWS account.</p>
            source_project_version_arn: <p>The ARN of the model version in the source project that you want to copy to a destination project.</p>
            destination_project_arn: <p>The ARN of the project in the trusted AWS account that you want to copy the model version to. </p>
            version_name: <p>A name for the version of the model that's copied to the destination project.</p>
            output_config: <p>The S3 bucket and folder location where the training output for the source model version is placed.</p>
            tags: <p>The key-value tags to assign to the model version. </p>
            kms_key_id: <p>The identifier for your AWS Key Management Service key (AWS KMS key). You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt training results and manifest files written to the output Amazon S3 bucket (<code>OutputConfig</code>).</p> <p>If you choose to use your own KMS key, you need the following permissions on the KMS key.</p> <ul> <li> <p>kms:CreateGrant</p> </li> <li> <p>kms:DescribeKey</p> </li> <li> <p>kms:GenerateDataKey</p> </li> <li> <p>kms:Decrypt</p> </li> </ul> <p>If you don't specify a value for <code>KmsKeyId</code>, images copied into the service are encrypted using a key that AWS owns and manages.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p></p> <p>The size of the collection exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CopyProjectVersion
            Copies a version of an Amazon Rekognition Custom Labels model from a source project to a destination project.

            >>> client.copy_project_version(source_project_arn='arn:aws:rekognition:us-east-1:111122223333:project/SourceProject/16565123456', source_project_version_arn='arn:aws:rekognition:us-east-1:111122223333:project/SourceProject/version/model_1/1656611123456', destination_project_arn='arn:aws:rekognition:us-east-1:555555555555:project/DestinationProject/1656705098765', version_name='DestinationVersionName_cross_account', output_config={'S3Bucket': 'bucket-name', 'S3KeyPrefix': 'path_to_folder'}, tags={'key1': 'val1'}, kms_key_id='arn:1234abcd-12ab-34cd-56ef-1234567890ab')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.copy_project_version_request.CopyProjectVersionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.copy_project_version_response.CopyProjectVersionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.copy_project_version

            output, http_response = (
                capo_rekognition._operations.rekognition_service.copy_project_version.copy_project_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.copy_project_version_request.CopyProjectVersionRequest = {
            "source_project_arn": source_project_arn,
            "source_project_version_arn": source_project_version_arn,
            "destination_project_arn": destination_project_arn,
            "version_name": version_name,
            "output_config": output_config,
        }
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_collection(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        tags: Optional["capo_rekognition.types.tag_map.TagMap"] = None,
    ) -> "capo_rekognition.types.create_collection_response.CreateCollectionResponse":
        """<p>Creates a collection in an AWS Region. You can add faces to the collection using the <a>IndexFaces</a> operation. </p> <p>For example, you might create collections, one for each of your application users. A user can then index faces using the <code>IndexFaces</code> operation and persist results in a specific collection. Then, a user can search the collection for faces in the user-specific container. </p> <p>When you create a collection, it is associated with the latest version of the face model version.</p> <note> <p>Collection names are case-sensitive.</p> </note> <p>This operation requires permissions to perform the <code>rekognition:CreateCollection</code> action. If you want to tag your collection, you also require permission to perform the <code>rekognition:TagResource</code> operation.</p>

        Args:
            collection_id: <p>ID for the collection that you are creating.</p>
            tags: <p> A set of tags (key-value pairs) that you want to attach to the collection. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>A resource with the specified ID already exists.</p>
            capo_rekognition.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p></p> <p>The size of the collection exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a collection
            This operation creates a Rekognition collection for storing image data.

            >>> client.create_collection(collection_id='myphotos')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.create_collection_request.CreateCollectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.create_collection_response.CreateCollectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.create_collection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.create_collection.create_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.create_collection_request.CreateCollectionRequest = {
            "collection_id": collection_id
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_dataset(
        self,
        dataset_type: "capo_rekognition.types.dataset_type.DatasetType",
        project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        dataset_source: Optional[
            "capo_rekognition.types.dataset_source.DatasetSource"
        ] = None,
        tags: Optional["capo_rekognition.types.tag_map.TagMap"] = None,
    ) -> "capo_rekognition.types.create_dataset_response.CreateDatasetResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Creates a new Amazon Rekognition Custom Labels dataset. You can create a dataset by using an Amazon Sagemaker format manifest file or by copying an existing Amazon Rekognition Custom Labels dataset.</p> <p>To create a training dataset for a project, specify <code>TRAIN</code> for the value of <code>DatasetType</code>. To create the test dataset for a project, specify <code>TEST</code> for the value of <code>DatasetType</code>. </p> <p>The response from <code>CreateDataset</code> is the Amazon Resource Name (ARN) for the dataset. Creating a dataset takes a while to complete. Use <a>DescribeDataset</a> to check the current status. The dataset created successfully if the value of <code>Status</code> is <code>CREATE_COMPLETE</code>. </p> <p>To check if any non-terminal errors occurred, call <a>ListDatasetEntries</a> and check for the presence of <code>errors</code> lists in the JSON Lines.</p> <p>Dataset creation fails if a terminal error occurs (<code>Status</code> = <code>CREATE_FAILED</code>). Currently, you can't access the terminal error information. </p> <p>For more information, see Creating dataset in the <i>Amazon Rekognition Custom Labels Developer Guide</i>.</p> <p>This operation requires permissions to perform the <code>rekognition:CreateDataset</code> action. If you want to copy an existing dataset, you also require permission to perform the <code>rekognition:ListDatasetEntries</code> action.</p>

        Args:
            dataset_source: <p> The source files for the dataset. You can specify the ARN of an existing dataset or specify the Amazon S3 bucket location of an Amazon Sagemaker format manifest file. If you don't specify <code>datasetSource</code>, an empty dataset is created. To add labeled images to the dataset, You can use the console or call <a>UpdateDatasetEntries</a>. </p>
            dataset_type: <p> The type of the dataset. Specify <code>TRAIN</code> to create a training dataset. Specify <code>TEST</code> to create a test dataset. </p>
            project_arn: <p> The ARN of the Amazon Rekognition Custom Labels project to which you want to asssign the dataset. </p>
            tags: <p>A set of tags (key-value pairs) that you want to attach to the dataset.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>A resource with the specified ID already exists.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an Amazon Rekognition Custom Labels dataset
            Creates an Amazon Rekognition Custom Labels dataset with a manifest file stored in an Amazon S3 bucket.

            >>> client.create_dataset(dataset_source={'GroundTruthManifest': {'S3Object': {'Bucket': 'my-bucket', 'Name': 'datasets/flowers_training/manifests/output/output.manifest'}}}, dataset_type='TRAIN', project_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-project/1690474772815')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.create_dataset_request.CreateDatasetRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.create_dataset

            output, http_response = (
                capo_rekognition._operations.rekognition_service.create_dataset.create_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.create_dataset_request.CreateDatasetRequest = {
            "dataset_type": dataset_type,
            "project_arn": project_arn,
        }
        if dataset_source is not None:
            input_["dataset_source"] = dataset_source
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_face_liveness_session(
        self,
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        kms_key_id: Optional["capo_rekognition.types.kms_key_id.KmsKeyId"] = None,
        settings: Optional[
            "capo_rekognition.types.create_face_liveness_session_request_settings.CreateFaceLivenessSessionRequestSettings"
        ] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_rekognition.types.create_face_liveness_session_response.CreateFaceLivenessSessionResponse":
        """<p>This API operation initiates a Face Liveness session. It returns a <code>SessionId</code>, which you can use to start streaming Face Liveness video and get the results for a Face Liveness session. </p> <p>You can use the <code>OutputConfig</code> option in the Settings parameter to provide an Amazon S3 bucket location. The Amazon S3 bucket stores reference images and audit images. If no Amazon S3 bucket is defined, raw bytes are sent instead. </p> <p>You can use <code>AuditImagesLimit</code> to limit the number of audit images returned when <code>GetFaceLivenessSessionResults</code> is called. This number is between 0 and 4. By default, it is set to 0. The limit is best effort and based on the duration of the selfie-video. </p> <p>You can use the <code>ChallengePreferences</code> option in the <code>Settings</code> parameter to choose between the 'FaceMovementAndLightChallenge' or FaceMovementChallenge' settings. See the <a href="https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-shared-responsibility-model.html">Shared Responsibility</a> page for details on guidance for which setting to choose between these two settings depending on your use case and preferences. This parameter is optional and if no parameter is provided, then the 'FaceMovementAndLightChallenge' settings is applied by default.</p>

        Args:
            kms_key_id: <p> The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt audit images and reference images.</p>
            settings: <p>A session settings object. It contains settings for the operation to be performed. For Face Liveness, it accepts <code>OutputConfig</code> and <code>AuditImagesLimit</code>.</p>
            client_request_token: <p>Idempotent token is used to recognize the Face Liveness request. If the same token is used with multiple <code>CreateFaceLivenessSession</code> requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.create_face_liveness_session_request.CreateFaceLivenessSessionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.create_face_liveness_session_response.CreateFaceLivenessSessionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.create_face_liveness_session

            output, http_response = (
                capo_rekognition._operations.rekognition_service.create_face_liveness_session.create_face_liveness_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.create_face_liveness_session_request.CreateFaceLivenessSessionRequest = {}
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if settings is not None:
            input_["settings"] = settings
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_project(
        self,
        project_name: "capo_rekognition.types.project_name.ProjectName",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        feature: Optional[
            "capo_rekognition.types.customization_feature.CustomizationFeature"
        ] = None,
        auto_update: Optional[
            "capo_rekognition.types.project_auto_update.ProjectAutoUpdate"
        ] = None,
        tags: Optional["capo_rekognition.types.tag_map.TagMap"] = None,
    ) -> "capo_rekognition.types.create_project_response.CreateProjectResponse":
        """<p>Creates a new Amazon Rekognition project. A project is a group of resources (datasets, model versions) that you use to create and manage a Amazon Rekognition Custom Labels Model or custom adapter. You can specify a feature to create the project with, if no feature is specified then Custom Labels is used by default. For adapters, you can also choose whether or not to have the project auto update by using the AutoUpdate argument. This operation requires permissions to perform the <code>rekognition:CreateProject</code> action.</p>

        Args:
            project_name: <p>The name of the project to create.</p>
            feature: <p>Specifies feature that is being customized. If no value is provided CUSTOM_LABELS is used as a default.</p>
            auto_update: <p>Specifies whether automatic retraining should be attempted for the versions of the project. Automatic retraining is done as a best effort. Required argument for Content Moderation. Applicable only to adapters.</p>
            tags: <p>A set of tags (key-value pairs) that you want to attach to the project.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an Amazon Rekognition Custom Labels project
            Creates an Amazon Rekognition Custom Labels project.

            >>> client.create_project(project_name='my-project')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.create_project_request.CreateProjectRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.create_project_response.CreateProjectResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.create_project

            output, http_response = (
                capo_rekognition._operations.rekognition_service.create_project.create_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.create_project_request.CreateProjectRequest = {
            "project_name": project_name
        }
        if feature is not None:
            input_["feature"] = feature
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

    def create_project_version(
        self,
        project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        version_name: "capo_rekognition.types.version_name.VersionName",
        output_config: "capo_rekognition.types.output_config.OutputConfig",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        training_data: Optional[
            "capo_rekognition.types.training_data.TrainingData"
        ] = None,
        testing_data: Optional[
            "capo_rekognition.types.testing_data.TestingData"
        ] = None,
        tags: Optional["capo_rekognition.types.tag_map.TagMap"] = None,
        kms_key_id: Optional["capo_rekognition.types.kms_key_id.KmsKeyId"] = None,
        version_description: Optional[
            "capo_rekognition.types.version_description.VersionDescription"
        ] = None,
        feature_config: Optional[
            "capo_rekognition.types.customization_feature_config.CustomizationFeatureConfig"
        ] = None,
    ) -> "capo_rekognition.types.create_project_version_response.CreateProjectVersionResponse":
        """<p>Creates a new version of Amazon Rekognition project (like a Custom Labels model or a custom adapter) and begins training. Models and adapters are managed as part of a Rekognition project. The response from <code>CreateProjectVersion</code> is an Amazon Resource Name (ARN) for the project version. </p> <p>The FeatureConfig operation argument allows you to configure specific model or adapter settings. You can provide a description to the project version by using the VersionDescription argment. Training can take a while to complete. You can get the current status by calling <a>DescribeProjectVersions</a>. Training completed successfully if the value of the <code>Status</code> field is <code>TRAINING_COMPLETED</code>. Once training has successfully completed, call <a>DescribeProjectVersions</a> to get the training results and evaluate the model.</p> <p>This operation requires permissions to perform the <code>rekognition:CreateProjectVersion</code> action.</p> <note> <p> <i>The following applies only to projects with Amazon Rekognition Custom Labels as the chosen feature:</i> </p> <p>You can train a model in a project that doesn't have associated datasets by specifying manifest files in the <code>TrainingData</code> and <code>TestingData</code> fields. </p> <p>If you open the console after training a model with manifest files, Amazon Rekognition Custom Labels creates the datasets for you using the most recent manifest files. You can no longer train a model version for the project by specifying manifest files. </p> <p>Instead of training with a project without associated datasets, we recommend that you use the manifest files to create training and test datasets for the project.</p> </note> <p></p>

        Args:
            project_arn: <p>The ARN of the Amazon Rekognition project that will manage the project version you want to train.</p>
            version_name: <p>A name for the version of the project version. This value must be unique.</p>
            output_config: <p>The Amazon S3 bucket location to store the results of training. The bucket can be any S3 bucket in your AWS account. You need <code>s3:PutObject</code> permission on the bucket. </p>
            training_data: <p>Specifies an external manifest that the services uses to train the project version. If you specify <code>TrainingData</code> you must also specify <code>TestingData</code>. The project must not have any associated datasets. </p>
            testing_data: <p>Specifies an external manifest that the service uses to test the project version. If you specify <code>TestingData</code> you must also specify <code>TrainingData</code>. The project must not have any associated datasets.</p>
            tags: <p> A set of tags (key-value pairs) that you want to attach to the project version. </p>
            kms_key_id: <p>The identifier for your AWS Key Management Service key (AWS KMS key). You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt training images, test images, and manifest files copied into the service for the project version. Your source images are unaffected. The key is also used to encrypt training results and manifest files written to the output Amazon S3 bucket (<code>OutputConfig</code>).</p> <p>If you choose to use your own KMS key, you need the following permissions on the KMS key.</p> <ul> <li> <p>kms:CreateGrant</p> </li> <li> <p>kms:DescribeKey</p> </li> <li> <p>kms:GenerateDataKey</p> </li> <li> <p>kms:Decrypt</p> </li> </ul> <p>If you don't specify a value for <code>KmsKeyId</code>, images copied into the service are encrypted using a key that AWS owns and manages.</p>
            version_description: <p>A description applied to the project version being created.</p>
            feature_config: <p>Feature-specific configuration of the training job. If the job configuration does not match the feature type associated with the project, an InvalidParameterException is returned.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p></p> <p>The size of the collection exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To train an Amazon Rekognition Custom Labels model
            Trains a version of an Amazon Rekognition Custom Labels model.

            >>> client.create_project_version(project_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-project/1690474772815', version_name='1', output_config={'S3Bucket': 'output_bucket', 'S3KeyPrefix': 'output_folder'})
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.create_project_version_request.CreateProjectVersionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.create_project_version_response.CreateProjectVersionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.create_project_version

            output, http_response = (
                capo_rekognition._operations.rekognition_service.create_project_version.create_project_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.create_project_version_request.CreateProjectVersionRequest = {
            "project_arn": project_arn,
            "version_name": version_name,
            "output_config": output_config,
        }
        if training_data is not None:
            input_["training_data"] = training_data
        if testing_data is not None:
            input_["testing_data"] = testing_data
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if version_description is not None:
            input_["version_description"] = version_description
        if feature_config is not None:
            input_["feature_config"] = feature_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_stream_processor(
        self,
        input: "capo_rekognition.types.stream_processor_input.StreamProcessorInput",
        output: "capo_rekognition.types.stream_processor_output.StreamProcessorOutput",
        name: "capo_rekognition.types.stream_processor_name.StreamProcessorName",
        settings: "capo_rekognition.types.stream_processor_settings.StreamProcessorSettings",
        role_arn: "capo_rekognition.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        tags: Optional["capo_rekognition.types.tag_map.TagMap"] = None,
        notification_channel: Optional[
            "capo_rekognition.types.stream_processor_notification_channel.StreamProcessorNotificationChannel"
        ] = None,
        kms_key_id: Optional["capo_rekognition.types.kms_key_id.KmsKeyId"] = None,
        regions_of_interest: Optional[
            "capo_rekognition.types.regions_of_interest.RegionsOfInterest"
        ] = None,
        data_sharing_preference: Optional[
            "capo_rekognition.types.stream_processor_data_sharing_preference.StreamProcessorDataSharingPreference"
        ] = None,
    ) -> "capo_rekognition.types.create_stream_processor_response.CreateStreamProcessorResponse":
        """<important> <p>Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html">Rekognition feature availability changes</a>.</p> <p> <b>This change does not impact the availability of other Amazon Rekognition features.</b> </p> </important> <p>Creates an Amazon Rekognition stream processor that you can use to detect and recognize faces or to detect labels in a streaming video.</p> <p>Amazon Rekognition Video is a consumer of live video from Amazon Kinesis Video Streams. There are two different settings for stream processors in Amazon Rekognition: detecting faces and detecting labels.</p> <ul> <li> <p>If you are creating a stream processor for detecting faces, you provide as input a Kinesis video stream (<code>Input</code>) and a Kinesis data stream (<code>Output</code>) stream for receiving the output. You must use the <code>FaceSearch</code> option in <code>Settings</code>, specifying the collection that contains the faces you want to recognize. After you have finished analyzing a streaming video, use <a>StopStreamProcessor</a> to stop processing.</p> </li> <li> <p>If you are creating a stream processor to detect labels, you provide as input a Kinesis video stream (<code>Input</code>), Amazon S3 bucket information (<code>Output</code>), and an Amazon SNS topic ARN (<code>NotificationChannel</code>). You can also provide a KMS key ID to encrypt the data sent to your Amazon S3 bucket. You specify what you want to detect by using the <code>ConnectedHome</code> option in settings, and selecting one of the following: <code>PERSON</code>, <code>PET</code>, <code>PACKAGE</code>, <code>ALL</code> You can also specify where in the frame you want Amazon Rekognition to monitor with <code>RegionsOfInterest</code>. When you run the <a>StartStreamProcessor</a> operation on a label detection stream processor, you input start and stop information to determine the length of the processing time.</p> </li> </ul> <p> Use <code>Name</code> to assign an identifier for the stream processor. You use <code>Name</code> to manage the stream processor. For example, you can start processing the source video by calling <a>StartStreamProcessor</a> with the <code>Name</code> field. </p> <p>This operation requires permissions to perform the <code>rekognition:CreateStreamProcessor</code> action. If you want to tag your stream processor, you also require permission to perform the <code>rekognition:TagResource</code> operation.</p>

        Args:
            input: <p>Kinesis video stream stream that provides the source streaming video. If you are using the AWS CLI, the parameter name is <code>StreamProcessorInput</code>. This is required for both face search and label detection stream processors.</p>
            output: <p>Kinesis data stream stream or Amazon S3 bucket location to which Amazon Rekognition Video puts the analysis results. If you are using the AWS CLI, the parameter name is <code>StreamProcessorOutput</code>. This must be a <a>S3Destination</a> of an Amazon S3 bucket that you own for a label detection stream processor or a Kinesis data stream ARN for a face search stream processor.</p>
            name: <p>An identifier you assign to the stream processor. You can use <code>Name</code> to manage the stream processor. For example, you can get the current status of the stream processor by calling <a>DescribeStreamProcessor</a>. <code>Name</code> is idempotent. This is required for both face search and label detection stream processors. </p>
            settings: <p>Input parameters used in a streaming video analyzed by a stream processor. You can use <code>FaceSearch</code> to recognize faces in a streaming video, or you can use <code>ConnectedHome</code> to detect labels.</p>
            role_arn: <p>The Amazon Resource Number (ARN) of the IAM role that allows access to the stream processor. The IAM role provides Rekognition read permissions for a Kinesis stream. It also provides write permissions to an Amazon S3 bucket and Amazon Simple Notification Service topic for a label detection stream processor. This is required for both face search and label detection stream processors.</p>
            tags: <p> A set of tags (key-value pairs) that you want to attach to the stream processor. </p>
            kms_key_id: <p> The identifier for your AWS Key Management Service key (AWS KMS key). This is an optional parameter for label detection stream processors and should not be used to create a face search stream processor. You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt results and data published to your Amazon S3 bucket, which includes image frames and hero images. Your source images are unaffected. </p> <p> </p>
            regions_of_interest: <p> Specifies locations in the frames where Amazon Rekognition checks for objects or people. You can specify up to 10 regions of interest, and each region has either a polygon or a bounding box. This is an optional parameter for label detection stream processors and should not be used to create a face search stream processor. </p>
            data_sharing_preference: <p> Shows whether you are sharing data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p></p> <p>The size of the collection exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.create_stream_processor_request.CreateStreamProcessorRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.create_stream_processor_response.CreateStreamProcessorResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.create_stream_processor

            output, http_response = (
                capo_rekognition._operations.rekognition_service.create_stream_processor.create_stream_processor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.create_stream_processor_request.CreateStreamProcessorRequest = {
            "input": input,
            "output": output,
            "name": name,
            "settings": settings,
            "role_arn": role_arn,
        }
        if tags is not None:
            input_["tags"] = tags
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if regions_of_interest is not None:
            input_["regions_of_interest"] = regions_of_interest
        if data_sharing_preference is not None:
            input_["data_sharing_preference"] = data_sharing_preference

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_user(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        user_id: "capo_rekognition.types.user_id.UserId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_rekognition.types.create_user_response.CreateUserResponse":
        """<p>Creates a new User within a collection specified by <code>CollectionId</code>. Takes <code>UserId</code> as a parameter, which is a user provided ID which should be unique within the collection. The provided <code>UserId</code> will alias the system generated UUID to make the <code>UserId</code> more user friendly. </p> <p>Uses a <code>ClientToken</code>, an idempotency token that ensures a call to <code>CreateUser</code> completes only once. If the value is not supplied, the AWS SDK generates an idempotency token for the requests. This prevents retries after a network error results from making multiple <code>CreateUser</code> calls. </p>

        Args:
            collection_id: <p>The ID of an existing collection to which the new UserID needs to be created.</p>
            user_id: <p>ID for the UserID to be created. This ID needs to be unique within the collection.</p>
            client_request_token: <p>Idempotent token used to identify the request to <code>CreateUser</code>. If you use the same token with multiple <code>CreateUser</code> requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.conflict_exception.ConflictException: <p> A User with the same Id already exists within the collection, or the update or deletion of the User caused an inconsistent state. ** </p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p></p> <p>The size of the collection exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateUser
            Creates a new User within a collection specified by CollectionId.

            >>> client.create_user(collection_id='MyCollection', user_id='DemoUser')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.create_user_response.CreateUserResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.create_user

            output, http_response = (
                capo_rekognition._operations.rekognition_service.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.create_user_request.CreateUserRequest = {
            "collection_id": collection_id,
            "user_id": user_id,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_collection(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.delete_collection_response.DeleteCollectionResponse":
        """<p>Deletes the specified collection. Note that this operation removes all faces in the collection. For an example, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/delete-collection-procedure.html">Deleting a collection</a>.</p> <p>This operation requires permissions to perform the <code>rekognition:DeleteCollection</code> action.</p>

        Args:
            collection_id: <p>ID of the collection to delete.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a collection
            This operation deletes a Rekognition collection.

            >>> client.delete_collection(collection_id='myphotos')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.delete_collection_request.DeleteCollectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.delete_collection_response.DeleteCollectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.delete_collection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.delete_collection.delete_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.delete_collection_request.DeleteCollectionRequest = {
            "collection_id": collection_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_dataset(
        self,
        dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.delete_dataset_response.DeleteDatasetResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Deletes an existing Amazon Rekognition Custom Labels dataset. Deleting a dataset might take while. Use <a>DescribeDataset</a> to check the current status. The dataset is still deleting if the value of <code>Status</code> is <code>DELETE_IN_PROGRESS</code>. If you try to access the dataset after it is deleted, you get a <code>ResourceNotFoundException</code> exception. </p> <p>You can't delete a dataset while it is creating (<code>Status</code> = <code>CREATE_IN_PROGRESS</code>) or if the dataset is updating (<code>Status</code> = <code>UPDATE_IN_PROGRESS</code>).</p> <p>This operation requires permissions to perform the <code>rekognition:DeleteDataset</code> action.</p>

        Args:
            dataset_arn: <p> The ARN of the Amazon Rekognition Custom Labels dataset that you want to delete. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an Amazon Rekognition Custom Labels dataset
            Deletes an Amazon Rekognition Custom Labels dataset.

            >>> client.delete_dataset(dataset_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-project/dataset/test/1690556733321')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.delete_dataset_response.DeleteDatasetResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.delete_dataset

            output, http_response = (
                capo_rekognition._operations.rekognition_service.delete_dataset.delete_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.delete_dataset_request.DeleteDatasetRequest = {
            "dataset_arn": dataset_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_faces(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        face_ids: "capo_rekognition.types.face_id_list.FaceIdList",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.delete_faces_response.DeleteFacesResponse":
        """<p>Deletes faces from a collection. You specify a collection ID and an array of face IDs to remove from the collection.</p> <p>This operation requires permissions to perform the <code>rekognition:DeleteFaces</code> action.</p>

        Args:
            collection_id: <p>Collection from which to remove the specific faces.</p>
            face_ids: <p>An array of face IDs to delete.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a face
            This operation deletes one or more faces from a Rekognition collection.

            >>> client.delete_faces(collection_id='myphotos', face_ids=['ff43d742-0c13-5d16-a3e8-03d3f58e980b'])
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.delete_faces_request.DeleteFacesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.delete_faces_response.DeleteFacesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.delete_faces

            output, http_response = (
                capo_rekognition._operations.rekognition_service.delete_faces.delete_faces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.delete_faces_request.DeleteFacesRequest = {
            "collection_id": collection_id,
            "face_ids": face_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_project(
        self,
        project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.delete_project_response.DeleteProjectResponse":
        """<p>Deletes a Amazon Rekognition project. To delete a project you must first delete all models or adapters associated with the project. To delete a model or adapter, see <a>DeleteProjectVersion</a>.</p> <p> <code>DeleteProject</code> is an asynchronous operation. To check if the project is deleted, call <a>DescribeProjects</a>. The project is deleted when the project no longer appears in the response. Be aware that deleting a given project will also delete any <code>ProjectPolicies</code> associated with that project.</p> <p>This operation requires permissions to perform the <code>rekognition:DeleteProject</code> action. </p>

        Args:
            project_arn: <p>The Amazon Resource Name (ARN) of the project that you want to delete.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an Amazon Rekognition Custom Labels project
            Deletes an Amazon Rekognition Custom Labels projects.

            >>> client.delete_project(project_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-project/1690405809285')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.delete_project_request.DeleteProjectRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.delete_project_response.DeleteProjectResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.delete_project

            output, http_response = (
                capo_rekognition._operations.rekognition_service.delete_project.delete_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.delete_project_request.DeleteProjectRequest = {
            "project_arn": project_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_project_policy(
        self,
        project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        policy_name: "capo_rekognition.types.project_policy_name.ProjectPolicyName",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        policy_revision_id: Optional[
            "capo_rekognition.types.project_policy_revision_id.ProjectPolicyRevisionId"
        ] = None,
    ) -> "capo_rekognition.types.delete_project_policy_response.DeleteProjectPolicyResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Deletes an existing project policy.</p> <p>To get a list of project policies attached to a project, call <a>ListProjectPolicies</a>. To attach a project policy to a project, call <a>PutProjectPolicy</a>.</p> <p>This operation requires permissions to perform the <code>rekognition:DeleteProjectPolicy</code> action.</p>

        Args:
            project_arn: <p>The Amazon Resource Name (ARN) of the project that the project policy you want to delete is attached to.</p>
            policy_name: <p>The name of the policy that you want to delete.</p>
            policy_revision_id: <p>The ID of the project policy revision that you want to delete.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_policy_revision_id_exception.InvalidPolicyRevisionIdException: <p>The supplied revision id for the project policy is invalid.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteProjectPolicy
            This operation deletes a revision of an existing project policy from an Amazon Rekognition Custom Labels project.

            >>> client.delete_project_policy(project_arn='arn:aws:rekognition:us-east-1:111122223333:project/SourceProject/1656557123456', policy_name='testPolicy1', policy_revision_id='3b274c25e9203a56a99e00e3ff205fbc')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.delete_project_policy_request.DeleteProjectPolicyRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.delete_project_policy_response.DeleteProjectPolicyResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.delete_project_policy

            output, http_response = (
                capo_rekognition._operations.rekognition_service.delete_project_policy.delete_project_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.delete_project_policy_request.DeleteProjectPolicyRequest = {
            "project_arn": project_arn,
            "policy_name": policy_name,
        }
        if policy_revision_id is not None:
            input_["policy_revision_id"] = policy_revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_project_version(
        self,
        project_version_arn: "capo_rekognition.types.project_version_arn.ProjectVersionArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.delete_project_version_response.DeleteProjectVersionResponse":
        """<p>Deletes a Rekognition project model or project version, like a Amazon Rekognition Custom Labels model or a custom adapter.</p> <p>You can't delete a project version if it is running or if it is training. To check the status of a project version, use the Status field returned from <a>DescribeProjectVersions</a>. To stop a project version call <a>StopProjectVersion</a>. If the project version is training, wait until it finishes.</p> <p>This operation requires permissions to perform the <code>rekognition:DeleteProjectVersion</code> action. </p>

        Args:
            project_version_arn: <p>The Amazon Resource Name (ARN) of the project version that you want to delete.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an Amazon Rekognition Custom Labels model
            Deletes a version of an Amazon Rekognition Custom Labels model.

            >>> client.delete_project_version(project_version_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-project/version/1/1690556751958')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.delete_project_version_request.DeleteProjectVersionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.delete_project_version_response.DeleteProjectVersionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.delete_project_version

            output, http_response = (
                capo_rekognition._operations.rekognition_service.delete_project_version.delete_project_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.delete_project_version_request.DeleteProjectVersionRequest = {
            "project_version_arn": project_version_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_stream_processor(
        self,
        name: "capo_rekognition.types.stream_processor_name.StreamProcessorName",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.delete_stream_processor_response.DeleteStreamProcessorResponse":
        """<important> <p>Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html">Rekognition feature availability changes</a>.</p> <p> <b>This change does not impact the availability of other Amazon Rekognition features.</b> </p> </important> <p>Deletes the stream processor identified by <code>Name</code>. You assign the value for <code>Name</code> when you create the stream processor with <a>CreateStreamProcessor</a>. You might not be able to use the same name for a stream processor for a few seconds after calling <code>DeleteStreamProcessor</code>.</p>

        Args:
            name: <p>The name of the stream processor you want to delete.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.delete_stream_processor_request.DeleteStreamProcessorRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.delete_stream_processor_response.DeleteStreamProcessorResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.delete_stream_processor

            output, http_response = (
                capo_rekognition._operations.rekognition_service.delete_stream_processor.delete_stream_processor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.delete_stream_processor_request.DeleteStreamProcessorRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_user(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        user_id: "capo_rekognition.types.user_id.UserId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_rekognition.types.delete_user_response.DeleteUserResponse":
        """<p>Deletes the specified UserID within the collection. Faces that are associated with the UserID are disassociated from the UserID before deleting the specified UserID. If the specified <code>Collection</code> or <code>UserID</code> is already deleted or not found, a <code>ResourceNotFoundException</code> will be thrown. If the action is successful with a 200 response, an empty HTTP body is returned. </p>

        Args:
            collection_id: <p>The ID of an existing collection from which the UserID needs to be deleted. </p>
            user_id: <p>ID for the UserID to be deleted. </p>
            client_request_token: <p>Idempotent token used to identify the request to <code>DeleteUser</code>. If you use the same token with multiple <code>DeleteUser </code>requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.conflict_exception.ConflictException: <p> A User with the same Id already exists within the collection, or the update or deletion of the User caused an inconsistent state. ** </p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteUser
            Deletes the specified UserID within the collection.

            >>> client.delete_user(collection_id='MyCollection', user_id='DemoUser', client_request_token='550e8400-e29b-41d4-a716-446655440001')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.delete_user_response.DeleteUserResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.delete_user

            output, http_response = (
                capo_rekognition._operations.rekognition_service.delete_user.delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.delete_user_request.DeleteUserRequest = {
            "collection_id": collection_id,
            "user_id": user_id,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_collection(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> (
        "capo_rekognition.types.describe_collection_response.DescribeCollectionResponse"
    ):
        """<p>Describes the specified collection. You can use <code>DescribeCollection</code> to get information, such as the number of faces indexed into a collection and the version of the model used by the collection for face detection.</p> <p>For more information, see Describing a Collection in the Amazon Rekognition Developer Guide.</p>

        Args:
            collection_id: <p>The ID of the collection to describe.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.describe_collection_request.DescribeCollectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.describe_collection_response.DescribeCollectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.describe_collection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.describe_collection.describe_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.describe_collection_request.DescribeCollectionRequest = {
            "collection_id": collection_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_dataset(
        self,
        dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.describe_dataset_response.DescribeDatasetResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p> Describes an Amazon Rekognition Custom Labels dataset. You can get information such as the current status of a dataset and statistics about the images and labels in a dataset. </p> <p>This operation requires permissions to perform the <code>rekognition:DescribeDataset</code> action.</p>

        Args:
            dataset_arn: <p> The Amazon Resource Name (ARN) of the dataset that you want to describe. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.describe_dataset_request.DescribeDatasetRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.describe_dataset_response.DescribeDatasetResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.describe_dataset

            output, http_response = (
                capo_rekognition._operations.rekognition_service.describe_dataset.describe_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.describe_dataset_request.DescribeDatasetRequest = {
            "dataset_arn": dataset_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_projects(
        self,
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.projects_page_size.ProjectsPageSize"
        ] = None,
        project_names: Optional[
            "capo_rekognition.types.project_names.ProjectNames"
        ] = None,
        features: Optional[
            "capo_rekognition.types.customization_features.CustomizationFeatures"
        ] = None,
    ) -> "capo_rekognition.types.describe_projects_response.DescribeProjectsResponse":
        """<p>Gets information about your Rekognition projects.</p> <p>This operation requires permissions to perform the <code>rekognition:DescribeProjects</code> action.</p>

        Args:
            next_token: <p>If the previous response was incomplete (because there is more results to retrieve), Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. </p>
            project_names: <p>A list of the projects that you want Rekognition to describe. If you don't specify a value, the response includes descriptions for all the projects in your AWS account.</p>
            features: <p>Specifies the type of customization to filter projects by. If no value is specified, CUSTOM_LABELS is used as a default.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.describe_projects_request.DescribeProjectsRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.describe_projects_response.DescribeProjectsResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.describe_projects

            output, http_response = (
                capo_rekognition._operations.rekognition_service.describe_projects.describe_projects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.describe_projects_request.DescribeProjectsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if project_names is not None:
            input_["project_names"] = project_names
        if features is not None:
            input_["features"] = features

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_projects(
        self,
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.projects_page_size.ProjectsPageSize"
        ] = None,
        project_names: Optional[
            "capo_rekognition.types.project_names.ProjectNames"
        ] = None,
        features: Optional[
            "capo_rekognition.types.customization_features.CustomizationFeatures"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.project_description.ProjectDescription]":
        _token = next_token
        while True:
            _response = self.describe_projects(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                project_names=project_names,
                features=features,
            )
            _page = _resolve_path(_response, ("project_descriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_project_versions(
        self,
        project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        version_names: Optional[
            "capo_rekognition.types.version_names.VersionNames"
        ] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.project_versions_page_size.ProjectVersionsPageSize"
        ] = None,
    ) -> "capo_rekognition.types.describe_project_versions_response.DescribeProjectVersionsResponse":
        """<p>Lists and describes the versions of an Amazon Rekognition project. You can specify up to 10 model or adapter versions in <code>ProjectVersionArns</code>. If you don't specify a value, descriptions for all model/adapter versions in the project are returned.</p> <p>This operation requires permissions to perform the <code>rekognition:DescribeProjectVersions</code> action.</p>

        Args:
            project_arn: <p>The Amazon Resource Name (ARN) of the project that contains the model/adapter you want to describe.</p>
            version_names: <p>A list of model or project version names that you want to describe. You can add up to 10 model or project version names to the list. If you don't specify a value, all project version descriptions are returned. A version name is part of a project version ARN. For example, <code>my-model.2020-01-21T09.10.15</code> is the version name in the following ARN. <code>arn:aws:rekognition:us-east-1:123456789012:project/getting-started/version/<i>my-model.2020-01-21T09.10.15</i>/1234567890123</code>.</p>
            next_token: <p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.describe_project_versions_request.DescribeProjectVersionsRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.describe_project_versions_response.DescribeProjectVersionsResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.describe_project_versions

            output, http_response = (
                capo_rekognition._operations.rekognition_service.describe_project_versions.describe_project_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.describe_project_versions_request.DescribeProjectVersionsRequest = {
            "project_arn": project_arn
        }
        if version_names is not None:
            input_["version_names"] = version_names
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

    def iter_describe_project_versions(
        self,
        project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        version_names: Optional[
            "capo_rekognition.types.version_names.VersionNames"
        ] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.project_versions_page_size.ProjectVersionsPageSize"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.project_version_description.ProjectVersionDescription]":
        _token = next_token
        while True:
            _response = self.describe_project_versions(
                project_arn,
                config_overrides=config_overrides,
                version_names=version_names,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("project_version_descriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_stream_processor(
        self,
        name: "capo_rekognition.types.stream_processor_name.StreamProcessorName",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.describe_stream_processor_response.DescribeStreamProcessorResponse":
        """<important> <p>Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html">Rekognition feature availability changes</a>.</p> <p> <b>This change does not impact the availability of other Amazon Rekognition features.</b> </p> </important> <p>Provides information about a stream processor created by <a>CreateStreamProcessor</a>. You can get information about the input and output streams, the input parameters for the face recognition being performed, and the current status of the stream processor.</p>

        Args:
            name: <p>Name of the stream processor for which you want information.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.describe_stream_processor_request.DescribeStreamProcessorRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.describe_stream_processor_response.DescribeStreamProcessorResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.describe_stream_processor

            output, http_response = (
                capo_rekognition._operations.rekognition_service.describe_stream_processor.describe_stream_processor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.describe_stream_processor_request.DescribeStreamProcessorRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_custom_labels(
        self,
        project_version_arn: "capo_rekognition.types.project_version_arn.ProjectVersionArn",
        image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.u_integer.UInteger"] = None,
        min_confidence: Optional["capo_rekognition.types.percent.Percent"] = None,
    ) -> "capo_rekognition.types.detect_custom_labels_response.DetectCustomLabelsResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Detects custom labels in a supplied image by using an Amazon Rekognition Custom Labels model. </p> <p>You specify which version of a model version to use by using the <code>ProjectVersionArn</code> input parameter. </p> <p>You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. </p> <p> For each object that the model version detects on an image, the API returns a (<code>CustomLabel</code>) object in an array (<code>CustomLabels</code>). Each <code>CustomLabel</code> object provides the label name (<code>Name</code>), the level of confidence that the image contains the object (<code>Confidence</code>), and object location information, if it exists, for the label on the image (<code>Geometry</code>). </p> <p>To filter labels that are returned, specify a value for <code>MinConfidence</code>. <code>DetectCustomLabelsLabels</code> only returns labels with a confidence that's higher than the specified value. The value of <code>MinConfidence</code> maps to the assumed threshold values created during training. For more information, see <i>Assumed threshold</i> in the Amazon Rekognition Custom Labels Developer Guide. Amazon Rekognition Custom Labels metrics expresses an assumed threshold as a floating point value between 0-1. The range of <code>MinConfidence</code> normalizes the threshold value to a percentage value (0-100). Confidence responses from <code>DetectCustomLabels</code> are also returned as a percentage. You can use <code>MinConfidence</code> to change the precision and recall or your model. For more information, see <i>Analyzing an image</i> in the Amazon Rekognition Custom Labels Developer Guide. </p> <p>If you don't specify a value for <code>MinConfidence</code>, <code>DetectCustomLabels</code> returns labels based on the assumed threshold of each label.</p> <p>This is a stateless API operation. That is, the operation does not persist any data.</p> <p>This operation requires permissions to perform the <code>rekognition:DetectCustomLabels</code> action. </p> <p>For more information, see <i>Analyzing an image</i> in the Amazon Rekognition Custom Labels Developer Guide. </p>

        Args:
            project_version_arn: <p>The ARN of the model version that you want to use. Only models associated with Custom Labels projects accepted by the operation. If a provided ARN refers to a model version associated with a project for a different feature type, then an InvalidParameterException is returned.</p>
            max_results: <p>Maximum number of results you want the service to return in the response. The service returns the specified number of highest confidence labels ranked from highest confidence to lowest.</p>
            min_confidence: <p>Specifies the minimum confidence level for the labels to return. <code>DetectCustomLabels</code> doesn't return any labels with a confidence value that's lower than this specified value. If you specify a value of 0, <code>DetectCustomLabels</code> returns all labels, regardless of the assumed threshold applied to each label. If you don't specify a value for <code>MinConfidence</code>, <code>DetectCustomLabels</code> returns labels based on the assumed threshold of each label.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource isn't ready. For example, this exception occurs when you call <code>DetectCustomLabels</code> with a model version that isn't deployed. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To detect custom labels in an image with an Amazon Rekognition Custom Labels model
            Detects custom labels in an image with an Amazon Rekognition Custom Labels model

            >>> client.detect_custom_labels(project_version_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-project/version/my-project.2023-07-31T11.49.37/1690829378219', image={'S3Object': {'Bucket': 'custom-labels-console-us-east-1-1111111111', 'Name': 'assets/flowers_1_test_dataset/camellia4.jpg'}}, max_results=100, min_confidence=50)
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.detect_custom_labels_request.DetectCustomLabelsRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.detect_custom_labels_response.DetectCustomLabelsResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.detect_custom_labels

            output, http_response = (
                capo_rekognition._operations.rekognition_service.detect_custom_labels.detect_custom_labels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.detect_custom_labels_request.DetectCustomLabelsRequest = {
            "project_version_arn": project_version_arn,
            "image": image,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if min_confidence is not None:
            input_["min_confidence"] = min_confidence

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_faces(
        self,
        image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        attributes: Optional["capo_rekognition.types.attributes.Attributes"] = None,
    ) -> "capo_rekognition.types.detect_faces_response.DetectFacesResponse":
        """<p>Detects faces within an image that is provided as input.</p> <p> <code>DetectFaces</code> detects the 100 largest faces in the image. For each face detected, the operation returns face details. These details include a bounding box of the face, a confidence value (that the bounding box contains a face), and a fixed set of attributes such as facial landmarks (for example, coordinates of eye and mouth), pose, presence of facial occlusion, and so on.</p> <p>The face-detection algorithm is most effective on frontal faces. For non-frontal or obscured faces, the algorithm might not detect the faces or might detect faces with lower confidence. </p> <p>You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. </p> <note> <p>This is a stateless API operation. That is, the operation does not persist any data.</p> </note> <p>This operation requires permissions to perform the <code>rekognition:DetectFaces</code> action. </p>

        Args:
            image: <p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>
            attributes: <p>An array of facial attributes you want to be returned. A <code>DEFAULT</code> subset of facial attributes - <code>BoundingBox</code>, <code>Confidence</code>, <code>Pose</code>, <code>Quality</code>, and <code>Landmarks</code> - will always be returned. You can request for specific facial attributes (in addition to the default list) - by using [<code>"DEFAULT", "FACE_OCCLUDED"</code>] or just [<code>"FACE_OCCLUDED"</code>]. You can request for all facial attributes by using [<code>"ALL"]</code>. Requesting more attributes may increase response time.</p> <p>If you provide both, <code>["ALL", "DEFAULT"]</code>, the service uses a logical "AND" operator to determine which attributes to return (in this case, all attributes). </p> <p>Note that while the FaceOccluded and EyeDirection attributes are supported when using <code>DetectFaces</code>, they aren't supported when analyzing videos with <code>StartFaceDetection</code> and <code>GetFaceDetection</code>.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To detect faces in an image
            This operation detects faces in an image stored in an AWS S3 bucket.

            >>> client.detect_faces(image={'S3Object': {'Bucket': 'mybucket', 'Name': 'myphoto'}})
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.detect_faces_request.DetectFacesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.detect_faces_response.DetectFacesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.detect_faces

            output, http_response = (
                capo_rekognition._operations.rekognition_service.detect_faces.detect_faces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.detect_faces_request.DetectFacesRequest = {
            "image": image
        }
        if attributes is not None:
            input_["attributes"] = attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_labels(
        self,
        image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_labels: Optional["capo_rekognition.types.u_integer.UInteger"] = None,
        min_confidence: Optional["capo_rekognition.types.percent.Percent"] = None,
        features: Optional[
            "capo_rekognition.types.detect_labels_feature_list.DetectLabelsFeatureList"
        ] = None,
        settings: Optional[
            "capo_rekognition.types.detect_labels_settings.DetectLabelsSettings"
        ] = None,
    ) -> "capo_rekognition.types.detect_labels_response.DetectLabelsResponse":
        """<p>Detects instances of real-world entities within an image (JPEG or PNG) provided as input. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; and concepts like landscape, evening, and nature. </p> <p>For an example, see Analyzing images stored in an Amazon S3 bucket in the Amazon Rekognition Developer Guide.</p> <p>You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. </p> <p> <b>Optional Parameters</b> </p> <p>You can specify one or both of the <code>GENERAL_LABELS</code> and <code>IMAGE_PROPERTIES</code> feature types when calling the DetectLabels API. Including <code>GENERAL_LABELS</code> will ensure the response includes the labels detected in the input image, while including <code>IMAGE_PROPERTIES </code>will ensure the response includes information about the image quality and color.</p> <p>When using <code>GENERAL_LABELS</code> and/or <code>IMAGE_PROPERTIES</code> you can provide filtering criteria to the Settings parameter. You can filter with sets of individual labels or with label categories. You can specify inclusive filters, exclusive filters, or a combination of inclusive and exclusive filters. For more information on filtering see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html">Detecting Labels in an Image</a>.</p> <p>When getting labels, you can specify <code>MinConfidence</code> to control the confidence threshold for the labels returned. The default is 55%. You can also add the <code>MaxLabels</code> parameter to limit the number of labels returned. The default and upper limit is 1000 labels. These arguments are only valid when supplying GENERAL_LABELS as a feature type.</p> <p> <b>Response Elements</b> </p> <p> For each object, scene, and concept the API returns one or more labels. The API returns the following types of information about labels:</p> <ul> <li> <p> Name - The name of the detected label. </p> </li> <li> <p> Confidence - The level of confidence in the label assigned to a detected object. </p> </li> <li> <p> Parents - The ancestor labels for a detected label. DetectLabels returns a hierarchical taxonomy of detected labels. For example, a detected car might be assigned the label car. The label car has two parent labels: Vehicle (its parent) and Transportation (its grandparent). The response includes the all ancestors for a label, where every ancestor is a unique label. In the previous example, Car, Vehicle, and Transportation are returned as unique labels in the response. </p> </li> <li> <p> Aliases - Possible Aliases for the label. </p> </li> <li> <p> Categories - The label categories that the detected label belongs to. </p> </li> <li> <p> BoundingBox — Bounding boxes are described for all instances of detected common object labels, returned in an array of Instance objects. An Instance object contains a BoundingBox object, describing the location of the label on the input image. It also includes the confidence for the accuracy of the detected bounding box. </p> </li> </ul> <p> The API returns the following information regarding the image, as part of the ImageProperties structure:</p> <ul> <li> <p>Quality - Information about the Sharpness, Brightness, and Contrast of the input image, scored between 0 to 100. Image quality is returned for the entire image, as well as the background and the foreground. </p> </li> <li> <p>Dominant Color - An array of the dominant colors in the image. </p> </li> <li> <p>Foreground - Information about the sharpness, brightness, and dominant colors of the input image’s foreground. </p> </li> <li> <p>Background - Information about the sharpness, brightness, and dominant colors of the input image’s background.</p> </li> </ul> <p>The list of returned labels will include at least one label for every detected object, along with information about that label. In the following example, suppose the input image has a lighthouse, the sea, and a rock. The response includes all three labels, one for each object, as well as the confidence in the label:</p> <p> <code>{Name: lighthouse, Confidence: 98.4629}</code> </p> <p> <code>{Name: rock,Confidence: 79.2097}</code> </p> <p> <code> {Name: sea,Confidence: 75.061}</code> </p> <p>The list of labels can include multiple labels for the same object. For example, if the input image shows a flower (for example, a tulip), the operation might return the following three labels. </p> <p> <code>{Name: flower,Confidence: 99.0562}</code> </p> <p> <code>{Name: plant,Confidence: 99.0562}</code> </p> <p> <code>{Name: tulip,Confidence: 99.0562}</code> </p> <p>In this example, the detection algorithm more precisely identifies the flower as a tulip.</p> <note> <p>If the object detected is a person, the operation doesn't provide the same facial details that the <a>DetectFaces</a> operation provides.</p> </note> <p>This is a stateless API operation that doesn't return any data.</p> <p>This operation requires permissions to perform the <code>rekognition:DetectLabels</code> action. </p>

        Args:
            image: <p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. Images stored in an S3 Bucket do not need to be base64-encoded.</p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>
            max_labels: <p>Maximum number of labels you want the service to return in the response. The service returns the specified number of highest confidence labels. Only valid when GENERAL_LABELS is specified as a feature type in the Feature input parameter.</p>
            min_confidence: <p>Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with confidence lower than this specified value.</p> <p>If <code>MinConfidence</code> is not specified, the operation returns labels with a confidence values greater than or equal to 55 percent. Only valid when GENERAL_LABELS is specified as a feature type in the Feature input parameter.</p>
            features: <p>A list of the types of analysis to perform. Specifying GENERAL_LABELS uses the label detection feature, while specifying IMAGE_PROPERTIES returns information regarding image color and quality. If no option is specified GENERAL_LABELS is used by default.</p>
            settings: <p>A list of the filters to be applied to returned detected labels and image properties. Specified filters can be inclusive, exclusive, or a combination of both. Filters can be used for individual labels or label categories. The exact label names or label categories must be supplied. For a full list of labels and label categories, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/labels.html">Detecting labels</a>.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To detect labels
            This operation detects labels in the supplied image

            >>> client.detect_labels(image={'S3Object': {'Bucket': 'mybucket', 'Name': 'myphoto'}}, max_labels=123, min_confidence=70)
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.detect_labels_request.DetectLabelsRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.detect_labels_response.DetectLabelsResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.detect_labels

            output, http_response = (
                capo_rekognition._operations.rekognition_service.detect_labels.detect_labels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.detect_labels_request.DetectLabelsRequest = {
            "image": image
        }
        if max_labels is not None:
            input_["max_labels"] = max_labels
        if min_confidence is not None:
            input_["min_confidence"] = min_confidence
        if features is not None:
            input_["features"] = features
        if settings is not None:
            input_["settings"] = settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_moderation_labels(
        self,
        image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        min_confidence: Optional["capo_rekognition.types.percent.Percent"] = None,
        human_loop_config: Optional[
            "capo_rekognition.types.human_loop_config.HumanLoopConfig"
        ] = None,
        project_version: Optional[
            "capo_rekognition.types.project_version_id.ProjectVersionId"
        ] = None,
    ) -> "capo_rekognition.types.detect_moderation_labels_response.DetectModerationLabelsResponse":
        """<p>Detects unsafe content in a specified JPEG or PNG format image. Use <code>DetectModerationLabels</code> to moderate images depending on your requirements. For example, you might want to filter images that contain nudity, but not images containing suggestive content.</p> <p>To filter images, use the labels returned by <code>DetectModerationLabels</code> to determine which types of content are appropriate.</p> <p>For information about moderation labels, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.</p> <p>You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. </p> <p>You can specify an adapter to use when retrieving label predictions by providing a <code>ProjectVersionArn</code> to the <code>ProjectVersion</code> argument.</p>

        Args:
            image: <p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>
            min_confidence: <p>Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with a confidence level lower than this specified value.</p> <p>If you don't specify <code>MinConfidence</code>, the operation returns labels with confidence values greater than or equal to 50 percent.</p>
            human_loop_config: <p>Sets up the configuration for human evaluation, including the FlowDefinition the image will be sent to.</p>
            project_version: <p>Identifier for the custom adapter. Expects the ProjectVersionArn as a value. Use the CreateProject or CreateProjectVersion APIs to create a custom adapter.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.human_loop_quota_exceeded_exception.HumanLoopQuotaExceededException: <p>The number of in-progress human reviews you have has exceeded the number allowed.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource isn't ready. For example, this exception occurs when you call <code>DetectCustomLabels</code> with a model version that isn't deployed. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.detect_moderation_labels_request.DetectModerationLabelsRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.detect_moderation_labels_response.DetectModerationLabelsResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.detect_moderation_labels

            output, http_response = (
                capo_rekognition._operations.rekognition_service.detect_moderation_labels.detect_moderation_labels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.detect_moderation_labels_request.DetectModerationLabelsRequest = {
            "image": image
        }
        if min_confidence is not None:
            input_["min_confidence"] = min_confidence
        if human_loop_config is not None:
            input_["human_loop_config"] = human_loop_config
        if project_version is not None:
            input_["project_version"] = project_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_protective_equipment(
        self,
        image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        summarization_attributes: Optional[
            "capo_rekognition.types.protective_equipment_summarization_attributes.ProtectiveEquipmentSummarizationAttributes"
        ] = None,
    ) -> "capo_rekognition.types.detect_protective_equipment_response.DetectProtectiveEquipmentResponse":
        """<p>Detects Personal Protective Equipment (PPE) worn by people detected in an image. Amazon Rekognition can detect the following types of PPE.</p> <ul> <li> <p>Face cover</p> </li> <li> <p>Hand cover</p> </li> <li> <p>Head cover</p> </li> </ul> <p>You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. The image must be either a PNG or JPG formatted file. </p> <p> <code>DetectProtectiveEquipment</code> detects PPE worn by up to 15 persons detected in an image.</p> <p>For each person detected in the image the API returns an array of body parts (face, head, left-hand, right-hand). For each body part, an array of detected items of PPE is returned, including an indicator of whether or not the PPE covers the body part. The API returns the confidence it has in each detection (person, PPE, body part and body part coverage). It also returns a bounding box (<a>BoundingBox</a>) for each detected person and each detected item of PPE. </p> <p>You can optionally request a summary of detected PPE items with the <code>SummarizationAttributes</code> input parameter. The summary provides the following information. </p> <ul> <li> <p>The persons detected as wearing all of the types of PPE that you specify.</p> </li> <li> <p>The persons detected as not wearing all of the types PPE that you specify.</p> </li> <li> <p>The persons detected where PPE adornment could not be determined. </p> </li> </ul> <p>This is a stateless API operation. That is, the operation does not persist any data.</p> <p>This operation requires permissions to perform the <code>rekognition:DetectProtectiveEquipment</code> action. </p>

        Args:
            image: <p>The image in which you want to detect PPE on detected persons. The image can be passed as image bytes or you can reference an image stored in an Amazon S3 bucket. </p>
            summarization_attributes: <p>An array of PPE types that you want to summarize.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.detect_protective_equipment_request.DetectProtectiveEquipmentRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.detect_protective_equipment_response.DetectProtectiveEquipmentResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.detect_protective_equipment

            output, http_response = (
                capo_rekognition._operations.rekognition_service.detect_protective_equipment.detect_protective_equipment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.detect_protective_equipment_request.DetectProtectiveEquipmentRequest = {
            "image": image
        }
        if summarization_attributes is not None:
            input_["summarization_attributes"] = summarization_attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_text(
        self,
        image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        filters: Optional[
            "capo_rekognition.types.detect_text_filters.DetectTextFilters"
        ] = None,
    ) -> "capo_rekognition.types.detect_text_response.DetectTextResponse":
        """<p>Detects text in the input image and converts it into machine-readable text.</p> <p>Pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, you must pass it as a reference to an image in an Amazon S3 bucket. For the AWS CLI, passing image bytes is not supported. The image must be either a .png or .jpeg formatted file. </p> <p>The <code>DetectText</code> operation returns text in an array of <a>TextDetection</a> elements, <code>TextDetections</code>. Each <code>TextDetection</code> element provides information about a single word or line of text that was detected in the image. </p> <p>A word is one or more script characters that are not separated by spaces. <code>DetectText</code> can detect up to 100 words in an image.</p> <p>A line is a string of equally spaced words. A line isn't necessarily a complete sentence. For example, a driver's license number is detected as a line. A line ends when there is no aligned text after it. Also, a line ends when there is a large gap between words, relative to the length of the words. This means, depending on the gap between words, Amazon Rekognition may detect multiple lines in text aligned in the same direction. Periods don't represent the end of a line. If a sentence spans multiple lines, the <code>DetectText</code> operation returns multiple lines.</p> <p>To determine whether a <code>TextDetection</code> element is a line of text or a word, use the <code>TextDetection</code> object <code>Type</code> field. </p> <p>To be detected, text must be within +/- 90 degrees orientation of the horizontal axis.</p> <p>For more information, see Detecting text in the Amazon Rekognition Developer Guide.</p>

        Args:
            image: <p>The input image as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Rekognition operations, you can't pass image bytes. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>
            filters: <p>Optional parameters that let you set the criteria that the text must meet to be included in your response.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.detect_text_request.DetectTextRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.detect_text_response.DetectTextResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.detect_text

            output, http_response = (
                capo_rekognition._operations.rekognition_service.detect_text.detect_text(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.detect_text_request.DetectTextRequest = {
            "image": image
        }
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_faces(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        user_id: "capo_rekognition.types.user_id.UserId",
        face_ids: "capo_rekognition.types.user_face_id_list.UserFaceIdList",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_rekognition.types.disassociate_faces_response.DisassociateFacesResponse":
        """<p>Removes the association between a <code>Face</code> supplied in an array of <code>FaceIds</code> and the User. If the User is not present already, then a <code>ResourceNotFound</code> exception is thrown. If successful, an array of faces that are disassociated from the User is returned. If a given face is already disassociated from the given UserID, it will be ignored and not be returned in the response. If a given face is already associated with a different User or not found in the collection it will be returned as part of <code>UnsuccessfulDisassociations</code>. You can remove 1 - 100 face IDs from a user at one time.</p>

        Args:
            collection_id: <p>The ID of an existing collection containing the UserID.</p>
            user_id: <p>ID for the existing UserID.</p>
            client_request_token: <p>Idempotent token used to identify the request to <code>DisassociateFaces</code>. If you use the same token with multiple <code>DisassociateFaces</code> requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>
            face_ids: <p>An array of face IDs to disassociate from the UserID. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.conflict_exception.ConflictException: <p> A User with the same Id already exists within the collection, or the update or deletion of the User caused an inconsistent state. ** </p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DisassociateFaces
            Removes the association between a Face supplied in an array of FaceIds and the User.

            >>> client.disassociate_faces(collection_id='MyCollection', user_id='DemoUser', face_ids=['f5817d37-94f6-4335-bfee-6cf79a3d806e', 'c92265d4-5f9c-43af-a58e-12be0ce02bc3'], client_request_token='550e8400-e29b-41d4-a716-446655440003')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.disassociate_faces_request.DisassociateFacesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.disassociate_faces_response.DisassociateFacesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.disassociate_faces

            output, http_response = (
                capo_rekognition._operations.rekognition_service.disassociate_faces.disassociate_faces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.disassociate_faces_request.DisassociateFacesRequest = {
            "collection_id": collection_id,
            "user_id": user_id,
            "face_ids": face_ids,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def distribute_dataset_entries(
        self,
        datasets: "capo_rekognition.types.distribute_dataset_metadata_list.DistributeDatasetMetadataList",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.distribute_dataset_entries_response.DistributeDatasetEntriesResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Distributes the entries (images) in a training dataset across the training dataset and the test dataset for a project. <code>DistributeDatasetEntries</code> moves 20% of the training dataset images to the test dataset. An entry is a JSON Line that describes an image. </p> <p>You supply the Amazon Resource Names (ARN) of a project's training dataset and test dataset. The training dataset must contain the images that you want to split. The test dataset must be empty. The datasets must belong to the same project. To create training and test datasets for a project, call <a>CreateDataset</a>.</p> <p>Distributing a dataset takes a while to complete. To check the status call <code>DescribeDataset</code>. The operation is complete when the <code>Status</code> field for the training dataset and the test dataset is <code>UPDATE_COMPLETE</code>. If the dataset split fails, the value of <code>Status</code> is <code>UPDATE_FAILED</code>.</p> <p>This operation requires permissions to perform the <code>rekognition:DistributeDatasetEntries</code> action.</p>

        Args:
            datasets: <p>The ARNS for the training dataset and test dataset that you want to use. The datasets must belong to the same project. The test dataset must be empty. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource isn't ready. For example, this exception occurs when you call <code>DetectCustomLabels</code> with a model version that isn't deployed. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To distribute an Amazon Rekognition Custom Labels dataset
            Distributes an Amazon Rekognition Custom Labels training dataset to a test dataset.

            >>> client.distribute_dataset_entries(datasets=[{'Arn': 'arn:aws:rekognition:us-east-1:111122223333:project/my-proj-2/dataset/train/1690564858106'}, {'Arn': 'arn:aws:rekognition:us-east-1:111122223333:project/my-proj-2/dataset/test/1690564858106'}])
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.distribute_dataset_entries_request.DistributeDatasetEntriesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.distribute_dataset_entries_response.DistributeDatasetEntriesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.distribute_dataset_entries

            output, http_response = (
                capo_rekognition._operations.rekognition_service.distribute_dataset_entries.distribute_dataset_entries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.distribute_dataset_entries_request.DistributeDatasetEntriesRequest = {
            "datasets": datasets
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_celebrity_info(
        self,
        id: "capo_rekognition.types.rekognition_unique_id.RekognitionUniqueId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.get_celebrity_info_response.GetCelebrityInfoResponse":
        """<p>Gets the name and additional information about a celebrity based on their Amazon Rekognition ID. The additional information is returned as an array of URLs. If there is no additional information about the celebrity, this list is empty.</p> <p>For more information, see Getting information about a celebrity in the Amazon Rekognition Developer Guide.</p> <p>This operation requires permissions to perform the <code>rekognition:GetCelebrityInfo</code> action. </p>

        Args:
            id: <p>The ID for the celebrity. You get the celebrity ID from a call to the <a>RecognizeCelebrities</a> operation, which recognizes celebrities in an image. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_celebrity_info_request.GetCelebrityInfoRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_celebrity_info_response.GetCelebrityInfoResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_celebrity_info

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_celebrity_info.get_celebrity_info(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_celebrity_info_request.GetCelebrityInfoRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_celebrity_recognition(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_rekognition.types.celebrity_recognition_sort_by.CelebrityRecognitionSortBy"
        ] = None,
    ) -> "capo_rekognition.types.get_celebrity_recognition_response.GetCelebrityRecognitionResponse":
        """<p>Gets the celebrity recognition results for a Amazon Rekognition Video analysis started by <a>StartCelebrityRecognition</a>.</p> <p>Celebrity recognition in a video is an asynchronous operation. Analysis is started by a call to <a>StartCelebrityRecognition</a> which returns a job identifier (<code>JobId</code>). </p> <p>When the celebrity recognition operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to <code>StartCelebrityRecognition</code>. To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <code>GetCelebrityDetection</code> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartCelebrityDetection</code>. </p> <p>For more information, see Working With Stored Videos in the Amazon Rekognition Developer Guide.</p> <p> <code>GetCelebrityRecognition</code> returns detected celebrities and the time(s) they are detected in an array (<code>Celebrities</code>) of <a>CelebrityRecognition</a> objects. Each <code>CelebrityRecognition</code> contains information about the celebrity in a <a>CelebrityDetail</a> object and the time, <code>Timestamp</code>, the celebrity was detected. This <a>CelebrityDetail</a> object stores information about the detected celebrity's face attributes, a face bounding box, known gender, the celebrity's name, and a confidence estimate.</p> <note> <p> <code>GetCelebrityRecognition</code> only returns the default facial attributes (<code>BoundingBox</code>, <code>Confidence</code>, <code>Landmarks</code>, <code>Pose</code>, and <code>Quality</code>). The <code>BoundingBox</code> field only applies to the detected face instance. The other facial attributes listed in the <code>Face</code> object of the following response syntax are not returned. For more information, see FaceDetail in the Amazon Rekognition Developer Guide. </p> </note> <p>By default, the <code>Celebrities</code> array is sorted by time (milliseconds from the start of the video). You can also sort the array by celebrity by specifying the value <code>ID</code> in the <code>SortBy</code> input parameter.</p> <p>The <code>CelebrityDetail</code> object includes the celebrity identifer and additional information urls. If you don't store the additional information urls, you can get them later by calling <a>GetCelebrityInfo</a> with the celebrity identifer.</p> <p>No information is returned for faces not recognized as celebrities.</p> <p>Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetCelebrityDetection</code> and populate the <code>NextToken</code> request parameter with the token value returned from the previous call to <code>GetCelebrityRecognition</code>.</p>

        Args:
            job_id: <p>Job identifier for the required celebrity recognition analysis. You can get the job identifer from a call to <code>StartCelebrityRecognition</code>.</p>
            max_results: <p>Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.</p>
            next_token: <p>If the previous response was incomplete (because there is more recognized celebrities to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of celebrities. </p>
            sort_by: <p>Sort to use for celebrities returned in <code>Celebrities</code> field. Specify <code>ID</code> to sort by the celebrity identifier, specify <code>TIMESTAMP</code> to sort by the time the celebrity was recognized.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_celebrity_recognition_request.GetCelebrityRecognitionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_celebrity_recognition_response.GetCelebrityRecognitionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_celebrity_recognition

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_celebrity_recognition.get_celebrity_recognition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_celebrity_recognition_request.GetCelebrityRecognitionRequest = {
            "job_id": job_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_celebrity_recognition(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_rekognition.types.celebrity_recognition_sort_by.CelebrityRecognitionSortBy"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.get_celebrity_recognition_response.GetCelebrityRecognitionResponse]":
        _token = next_token
        while True:
            _response = self.get_celebrity_recognition(
                job_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_content_moderation(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_rekognition.types.content_moderation_sort_by.ContentModerationSortBy"
        ] = None,
        aggregate_by: Optional[
            "capo_rekognition.types.content_moderation_aggregate_by.ContentModerationAggregateBy"
        ] = None,
    ) -> "capo_rekognition.types.get_content_moderation_response.GetContentModerationResponse":
        """<p>Gets the inappropriate, unwanted, or offensive content analysis results for a Amazon Rekognition Video analysis started by <a>StartContentModeration</a>. For a list of moderation labels in Amazon Rekognition, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api">Using the image and video moderation APIs</a>.</p> <p>Amazon Rekognition Video inappropriate or offensive content detection in a stored video is an asynchronous operation. You start analysis by calling <a>StartContentModeration</a> which returns a job identifier (<code>JobId</code>). When analysis finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to <code>StartContentModeration</code>. To get the results of the content analysis, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <code>GetContentModeration</code> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartContentModeration</code>. </p> <p>For more information, see Working with Stored Videos in the Amazon Rekognition Devlopers Guide.</p> <p> <code>GetContentModeration</code> returns detected inappropriate, unwanted, or offensive content moderation labels, and the time they are detected, in an array, <code>ModerationLabels</code>, of <a>ContentModerationDetection</a> objects. </p> <p>By default, the moderated labels are returned sorted by time, in milliseconds from the start of the video. You can also sort them by moderated label by specifying <code>NAME</code> for the <code>SortBy</code> input parameter. </p> <p>Since video analysis can return a large number of results, use the <code>MaxResults</code> parameter to limit the number of labels returned in a single call to <code>GetContentModeration</code>. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetContentModeration</code> and populate the <code>NextToken</code> request parameter with the value of <code>NextToken</code> returned from the previous call to <code>GetContentModeration</code>.</p> <p>For more information, see moderating content in the Amazon Rekognition Developer Guide.</p>

        Args:
            job_id: <p>The identifier for the inappropriate, unwanted, or offensive content moderation job. Use <code>JobId</code> to identify the job in a subsequent call to <code>GetContentModeration</code>.</p>
            max_results: <p>Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of content moderation labels.</p>
            sort_by: <p>Sort to use for elements in the <code>ModerationLabelDetections</code> array. Use <code>TIMESTAMP</code> to sort array elements by the time labels are detected. Use <code>NAME</code> to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by <code>TIMESTAMP</code>.</p>
            aggregate_by: <p>Defines how to aggregate results of the StartContentModeration request. Default aggregation option is TIMESTAMPS. SEGMENTS mode aggregates moderation labels over time.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_content_moderation_request.GetContentModerationRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_content_moderation_response.GetContentModerationResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_content_moderation

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_content_moderation.get_content_moderation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_content_moderation_request.GetContentModerationRequest = {
            "job_id": job_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if aggregate_by is not None:
            input_["aggregate_by"] = aggregate_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_content_moderation(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_rekognition.types.content_moderation_sort_by.ContentModerationSortBy"
        ] = None,
        aggregate_by: Optional[
            "capo_rekognition.types.content_moderation_aggregate_by.ContentModerationAggregateBy"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.get_content_moderation_response.GetContentModerationResponse]":
        _token = next_token
        while True:
            _response = self.get_content_moderation(
                job_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                aggregate_by=aggregate_by,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_face_detection(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_rekognition.types.get_face_detection_response.GetFaceDetectionResponse":
        """<p>Gets face detection results for a Amazon Rekognition Video analysis started by <a>StartFaceDetection</a>.</p> <p>Face detection with Amazon Rekognition Video is an asynchronous operation. You start face detection by calling <a>StartFaceDetection</a> which returns a job identifier (<code>JobId</code>). When the face detection operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to <code>StartFaceDetection</code>. To get the results of the face detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetFaceDetection</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartFaceDetection</code>.</p> <p> <code>GetFaceDetection</code> returns an array of detected faces (<code>Faces</code>) sorted by the time the faces were detected. </p> <p>Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetFaceDetection</code> and populate the <code>NextToken</code> request parameter with the token value returned from the previous call to <code>GetFaceDetection</code>.</p> <p>Note that for the <code>GetFaceDetection</code> operation, the returned values for <code>FaceOccluded</code> and <code>EyeDirection</code> will always be "null".</p>

        Args:
            job_id: <p>Unique identifier for the face detection job. The <code>JobId</code> is returned from <code>StartFaceDetection</code>.</p>
            max_results: <p>Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.</p>
            next_token: <p>If the previous response was incomplete (because there are more faces to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of faces.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_face_detection_request.GetFaceDetectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_face_detection_response.GetFaceDetectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_face_detection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_face_detection.get_face_detection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_face_detection_request.GetFaceDetectionRequest = {
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

    def iter_get_face_detection(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.get_face_detection_response.GetFaceDetectionResponse]":
        _token = next_token
        while True:
            _response = self.get_face_detection(
                job_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_face_liveness_session_results(
        self,
        session_id: "capo_rekognition.types.liveness_session_id.LivenessSessionId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.get_face_liveness_session_results_response.GetFaceLivenessSessionResultsResponse":
        """<p>Retrieves the results of a specific Face Liveness session. It requires the <code>sessionId</code> as input, which was created using <code>CreateFaceLivenessSession</code>. Returns the corresponding Face Liveness confidence score, a reference image that includes a face bounding box, and audit images that also contain face bounding boxes. The Face Liveness confidence score ranges from 0 to 100. </p> <p>The number of audit images returned by <code>GetFaceLivenessSessionResults</code> is defined by the <code>AuditImagesLimit</code> paramater when calling <code>CreateFaceLivenessSession</code>. Reference images are always returned when possible.</p> <p>For a session that has completed, the response can also include a <code>Feedback</code> list describing conditions that were detected in the selfie-video, such as low lighting or an obstructed face, and <code>Metadata</code> about the client that streamed the session.</p>

        Args:
            session_id: <p>A unique 128-bit UUID. This is used to uniquely identify the session and also acts as an idempotency token for all operations associated with the session.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.session_not_found_exception.SessionNotFoundException: <p>Occurs when a given sessionId is not found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_face_liveness_session_results_request.GetFaceLivenessSessionResultsRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_face_liveness_session_results_response.GetFaceLivenessSessionResultsResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_face_liveness_session_results

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_face_liveness_session_results.get_face_liveness_session_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_face_liveness_session_results_request.GetFaceLivenessSessionResultsRequest = {
            "session_id": session_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_face_search(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_rekognition.types.face_search_sort_by.FaceSearchSortBy"
        ] = None,
    ) -> "capo_rekognition.types.get_face_search_response.GetFaceSearchResponse":
        """<p>Gets the face search results for Amazon Rekognition Video face search started by <a>StartFaceSearch</a>. The search returns faces in a collection that match the faces of persons detected in a video. It also includes the time(s) that faces are matched in the video.</p> <p>Face search in a video is an asynchronous operation. You start face search by calling to <a>StartFaceSearch</a> which returns a job identifier (<code>JobId</code>). When the search operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to <code>StartFaceSearch</code>. To get the search results, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <code>GetFaceSearch</code> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartFaceSearch</code>.</p> <p>For more information, see Searching Faces in a Collection in the Amazon Rekognition Developer Guide.</p> <p>The search results are retured in an array, <code>Persons</code>, of <a>PersonMatch</a> objects. Each<code>PersonMatch</code> element contains details about the matching faces in the input collection, person information (facial attributes, bounding boxes, and person identifer) for the matched person, and the time the person was matched in the video.</p> <note> <p> <code>GetFaceSearch</code> only returns the default facial attributes (<code>BoundingBox</code>, <code>Confidence</code>, <code>Landmarks</code>, <code>Pose</code>, and <code>Quality</code>). The other facial attributes listed in the <code>Face</code> object of the following response syntax are not returned. For more information, see FaceDetail in the Amazon Rekognition Developer Guide. </p> </note> <p>By default, the <code>Persons</code> array is sorted by the time, in milliseconds from the start of the video, persons are matched. You can also sort by persons by specifying <code>INDEX</code> for the <code>SORTBY</code> input parameter.</p>

        Args:
            job_id: <p>The job identifer for the search request. You get the job identifier from an initial call to <code>StartFaceSearch</code>.</p>
            max_results: <p>Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.</p>
            next_token: <p>If the previous response was incomplete (because there is more search results to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of search results. </p>
            sort_by: <p>Sort to use for grouping faces in the response. Use <code>TIMESTAMP</code> to group faces by the time that they are recognized. Use <code>INDEX</code> to sort by recognized faces. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_face_search_request.GetFaceSearchRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_face_search_response.GetFaceSearchResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_face_search

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_face_search.get_face_search(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_face_search_request.GetFaceSearchRequest = {
            "job_id": job_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_face_search(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_rekognition.types.face_search_sort_by.FaceSearchSortBy"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.get_face_search_response.GetFaceSearchResponse]":
        _token = next_token
        while True:
            _response = self.get_face_search(
                job_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_label_detection(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_rekognition.types.label_detection_sort_by.LabelDetectionSortBy"
        ] = None,
        aggregate_by: Optional[
            "capo_rekognition.types.label_detection_aggregate_by.LabelDetectionAggregateBy"
        ] = None,
    ) -> (
        "capo_rekognition.types.get_label_detection_response.GetLabelDetectionResponse"
    ):
        """<p>Gets the label detection results of a Amazon Rekognition Video analysis started by <a>StartLabelDetection</a>. </p> <p>The label detection operation is started by a call to <a>StartLabelDetection</a> which returns a job identifier (<code>JobId</code>). When the label detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to <code>StartlabelDetection</code>. </p> <p>To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetLabelDetection</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartLabelDetection</code>.</p> <p> <code>GetLabelDetection</code> returns an array of detected labels (<code>Labels</code>) sorted by the time the labels were detected. You can also sort by the label name by specifying <code>NAME</code> for the <code>SortBy</code> input parameter. If there is no <code>NAME</code> specified, the default sort is by timestamp.</p> <p>You can select how results are aggregated by using the <code>AggregateBy</code> input parameter. The default aggregation method is <code>TIMESTAMPS</code>. You can also aggregate by <code>SEGMENTS</code>, which aggregates all instances of labels detected in a given segment. </p> <p>The returned Labels array may include the following attributes:</p> <ul> <li> <p>Name - The name of the detected label.</p> </li> <li> <p>Confidence - The level of confidence in the label assigned to a detected object. </p> </li> <li> <p>Parents - The ancestor labels for a detected label. GetLabelDetection returns a hierarchical taxonomy of detected labels. For example, a detected car might be assigned the label car. The label car has two parent labels: Vehicle (its parent) and Transportation (its grandparent). The response includes the all ancestors for a label, where every ancestor is a unique label. In the previous example, Car, Vehicle, and Transportation are returned as unique labels in the response. </p> </li> <li> <p> Aliases - Possible Aliases for the label. </p> </li> <li> <p>Categories - The label categories that the detected label belongs to.</p> </li> <li> <p>BoundingBox — Bounding boxes are described for all instances of detected common object labels, returned in an array of Instance objects. An Instance object contains a BoundingBox object, describing the location of the label on the input image. It also includes the confidence for the accuracy of the detected bounding box.</p> </li> <li> <p>Timestamp - Time, in milliseconds from the start of the video, that the label was detected. For aggregation by <code>SEGMENTS</code>, the <code>StartTimestampMillis</code>, <code>EndTimestampMillis</code>, and <code>DurationMillis</code> structures are what define a segment. Although the “Timestamp” structure is still returned with each label, its value is set to be the same as <code>StartTimestampMillis</code>.</p> </li> </ul> <p>Timestamp and Bounding box information are returned for detected Instances, only if aggregation is done by <code>TIMESTAMPS</code>. If aggregating by <code>SEGMENTS</code>, information about detected instances isn’t returned. </p> <p>The version of the label model used for the detection is also returned.</p> <p> <b>Note <code>DominantColors</code> isn't returned for <code>Instances</code>, although it is shown as part of the response in the sample seen below.</b> </p> <p>Use <code>MaxResults</code> parameter to limit the number of labels returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetlabelDetection</code> and populate the <code>NextToken</code> request parameter with the token value returned from the previous call to <code>GetLabelDetection</code>.</p> <p>If you are retrieving results while using the Amazon Simple Notification Service, note that you will receive an "ERROR" notification if the job encounters an issue.</p>

        Args:
            job_id: <p>Job identifier for the label detection operation for which you want results returned. You get the job identifer from an initial call to <code>StartlabelDetection</code>.</p>
            max_results: <p>Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.</p>
            next_token: <p>If the previous response was incomplete (because there are more labels to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of labels. </p>
            sort_by: <p>Sort to use for elements in the <code>Labels</code> array. Use <code>TIMESTAMP</code> to sort array elements by the time labels are detected. Use <code>NAME</code> to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by <code>TIMESTAMP</code>.</p>
            aggregate_by: <p>Defines how to aggregate the returned results. Results can be aggregated by timestamps or segments.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_label_detection_request.GetLabelDetectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_label_detection_response.GetLabelDetectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_label_detection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_label_detection.get_label_detection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_label_detection_request.GetLabelDetectionRequest = {
            "job_id": job_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if aggregate_by is not None:
            input_["aggregate_by"] = aggregate_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_label_detection(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_rekognition.types.label_detection_sort_by.LabelDetectionSortBy"
        ] = None,
        aggregate_by: Optional[
            "capo_rekognition.types.label_detection_aggregate_by.LabelDetectionAggregateBy"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.get_label_detection_response.GetLabelDetectionResponse]":
        _token = next_token
        while True:
            _response = self.get_label_detection(
                job_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                aggregate_by=aggregate_by,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_media_analysis_job(
        self,
        job_id: "capo_rekognition.types.media_analysis_job_id.MediaAnalysisJobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.get_media_analysis_job_response.GetMediaAnalysisJobResponse":
        """<important> <p>Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html">Rekognition feature availability changes</a>.</p> <p> <b>This change does not impact the availability of other Amazon Rekognition features.</b> </p> </important> <p>Retrieves the results for a given media analysis job. Takes a <code>JobId</code> returned by StartMediaAnalysisJob.</p>

        Args:
            job_id: <p>Unique identifier for the media analysis job for which you want to retrieve results.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_media_analysis_job_request.GetMediaAnalysisJobRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_media_analysis_job_response.GetMediaAnalysisJobResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_media_analysis_job

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_media_analysis_job.get_media_analysis_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_media_analysis_job_request.GetMediaAnalysisJobRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_person_tracking(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_rekognition.types.person_tracking_sort_by.PersonTrackingSortBy"
        ] = None,
    ) -> (
        "capo_rekognition.types.get_person_tracking_response.GetPersonTrackingResponse"
    ):
        """<note> <p> <i>End of support notice:</i> On October 31, 2025, AWS will discontinue support for Amazon Rekognition People Pathing. After October 31, 2025, you will no longer be able to use the Rekognition People Pathing capability. For more information, visit this <a href="https://aws.amazon.com/blogs/machine-learning/transitioning-from-amazon-rekognition-people-pathing-exploring-other-alternatives/">blog post</a>.</p> </note> <p>Gets the path tracking results of a Amazon Rekognition Video analysis started by <a>StartPersonTracking</a>.</p> <p>The person path tracking operation is started by a call to <code>StartPersonTracking</code> which returns a job identifier (<code>JobId</code>). When the operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to <code>StartPersonTracking</code>.</p> <p>To get the results of the person path tracking operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetPersonTracking</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartPersonTracking</code>.</p> <p> <code>GetPersonTracking</code> returns an array, <code>Persons</code>, of tracked persons and the time(s) their paths were tracked in the video. </p> <note> <p> <code>GetPersonTracking</code> only returns the default facial attributes (<code>BoundingBox</code>, <code>Confidence</code>, <code>Landmarks</code>, <code>Pose</code>, and <code>Quality</code>). The other facial attributes listed in the <code>Face</code> object of the following response syntax are not returned. </p> <p>For more information, see FaceDetail in the Amazon Rekognition Developer Guide.</p> </note> <p>By default, the array is sorted by the time(s) a person's path is tracked in the video. You can sort by tracked persons by specifying <code>INDEX</code> for the <code>SortBy</code> input parameter.</p> <p>Use the <code>MaxResults</code> parameter to limit the number of items returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetPersonTracking</code> and populate the <code>NextToken</code> request parameter with the token value returned from the previous call to <code>GetPersonTracking</code>.</p>

        Args:
            job_id: <p>The identifier for a job that tracks persons in a video. You get the <code>JobId</code> from a call to <code>StartPersonTracking</code>. </p>
            max_results: <p>Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.</p>
            next_token: <p>If the previous response was incomplete (because there are more persons to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of persons. </p>
            sort_by: <p>Sort to use for elements in the <code>Persons</code> array. Use <code>TIMESTAMP</code> to sort array elements by the time persons are detected. Use <code>INDEX</code> to sort by the tracked persons. If you sort by <code>INDEX</code>, the array elements for each person are sorted by detection confidence. The default sort is by <code>TIMESTAMP</code>.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_person_tracking_request.GetPersonTrackingRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_person_tracking_response.GetPersonTrackingResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_person_tracking

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_person_tracking.get_person_tracking(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_person_tracking_request.GetPersonTrackingRequest = {
            "job_id": job_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_person_tracking(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_rekognition.types.person_tracking_sort_by.PersonTrackingSortBy"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.get_person_tracking_response.GetPersonTrackingResponse]":
        _token = next_token
        while True:
            _response = self.get_person_tracking(
                job_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_segment_detection(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_rekognition.types.get_segment_detection_response.GetSegmentDetectionResponse":
        """<p>Gets the segment detection results of a Amazon Rekognition Video analysis started by <a>StartSegmentDetection</a>.</p> <p>Segment detection with Amazon Rekognition Video is an asynchronous operation. You start segment detection by calling <a>StartSegmentDetection</a> which returns a job identifier (<code>JobId</code>). When the segment detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to <code>StartSegmentDetection</code>. To get the results of the segment detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. if so, call <code>GetSegmentDetection</code> and pass the job identifier (<code>JobId</code>) from the initial call of <code>StartSegmentDetection</code>.</p> <p> <code>GetSegmentDetection</code> returns detected segments in an array (<code>Segments</code>) of <a>SegmentDetection</a> objects. <code>Segments</code> is sorted by the segment types specified in the <code>SegmentTypes</code> input parameter of <code>StartSegmentDetection</code>. Each element of the array includes the detected segment, the precentage confidence in the acuracy of the detected segment, the type of the segment, and the frame in which the segment was detected.</p> <p>Use <code>SelectedSegmentTypes</code> to find out the type of segment detection requested in the call to <code>StartSegmentDetection</code>.</p> <p>Use the <code>MaxResults</code> parameter to limit the number of segment detections returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetSegmentDetection</code> and populate the <code>NextToken</code> request parameter with the token value returned from the previous call to <code>GetSegmentDetection</code>.</p> <p>For more information, see Detecting video segments in stored video in the Amazon Rekognition Developer Guide.</p>

        Args:
            job_id: <p>Job identifier for the text detection operation for which you want results returned. You get the job identifer from an initial call to <code>StartSegmentDetection</code>.</p>
            max_results: <p>Maximum number of results to return per paginated call. The largest value you can specify is 1000.</p>
            next_token: <p>If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of text.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_segment_detection_request.GetSegmentDetectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_segment_detection_response.GetSegmentDetectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_segment_detection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_segment_detection.get_segment_detection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_segment_detection_request.GetSegmentDetectionRequest = {
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

    def iter_get_segment_detection(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.get_segment_detection_response.GetSegmentDetectionResponse]":
        _token = next_token
        while True:
            _response = self.get_segment_detection(
                job_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_text_detection(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_rekognition.types.get_text_detection_response.GetTextDetectionResponse":
        """<p>Gets the text detection results of a Amazon Rekognition Video analysis started by <a>StartTextDetection</a>.</p> <p>Text detection with Amazon Rekognition Video is an asynchronous operation. You start text detection by calling <a>StartTextDetection</a> which returns a job identifier (<code>JobId</code>) When the text detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to <code>StartTextDetection</code>. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. if so, call <code>GetTextDetection</code> and pass the job identifier (<code>JobId</code>) from the initial call of <code>StartLabelDetection</code>.</p> <p> <code>GetTextDetection</code> returns an array of detected text (<code>TextDetections</code>) sorted by the time the text was detected, up to 100 words per frame of video.</p> <p>Each element of the array includes the detected text, the precentage confidence in the acuracy of the detected text, the time the text was detected, bounding box information for where the text was located, and unique identifiers for words and their lines.</p> <p>Use MaxResults parameter to limit the number of text detections returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetTextDetection</code> and populate the <code>NextToken</code> request parameter with the token value returned from the previous call to <code>GetTextDetection</code>.</p>

        Args:
            job_id: <p>Job identifier for the text detection operation for which you want results returned. You get the job identifer from an initial call to <code>StartTextDetection</code>.</p>
            max_results: <p>Maximum number of results to return per paginated call. The largest value you can specify is 1000.</p>
            next_token: <p>If the previous response was incomplete (because there are more labels to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of text.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.get_text_detection_request.GetTextDetectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.get_text_detection_response.GetTextDetectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.get_text_detection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.get_text_detection.get_text_detection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.get_text_detection_request.GetTextDetectionRequest = {
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

    def iter_get_text_detection(
        self,
        job_id: "capo_rekognition.types.job_id.JobId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.get_text_detection_response.GetTextDetectionResponse]":
        _token = next_token
        while True:
            _response = self.get_text_detection(
                job_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def index_faces(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        external_image_id: Optional[
            "capo_rekognition.types.external_image_id.ExternalImageId"
        ] = None,
        detection_attributes: Optional[
            "capo_rekognition.types.attributes.Attributes"
        ] = None,
        max_faces: Optional[
            "capo_rekognition.types.max_faces_to_index.MaxFacesToIndex"
        ] = None,
        quality_filter: Optional[
            "capo_rekognition.types.quality_filter.QualityFilter"
        ] = None,
    ) -> "capo_rekognition.types.index_faces_response.IndexFacesResponse":
        """<p>Detects faces in the input image and adds them to the specified collection. </p> <p>Amazon Rekognition doesn't save the actual faces that are detected. Instead, the underlying detection algorithm first detects the faces in the input image. For each face, the algorithm extracts facial features into a feature vector, and stores it in the backend database. Amazon Rekognition uses feature vectors when it performs face match and search operations using the <a>SearchFaces</a> and <a>SearchFacesByImage</a> operations.</p> <p>For more information, see Adding faces to a collection in the Amazon Rekognition Developer Guide.</p> <p>To get the number of faces in a collection, call <a>DescribeCollection</a>. </p> <p>If you're using version 1.0 of the face detection model, <code>IndexFaces</code> indexes the 15 largest faces in the input image. Later versions of the face detection model index the 100 largest faces in the input image. </p> <p>If you're using version 4 or later of the face model, image orientation information is not returned in the <code>OrientationCorrection</code> field. </p> <p>To determine which version of the model you're using, call <a>DescribeCollection</a> and supply the collection ID. You can also get the model version from the value of <code>FaceModelVersion</code> in the response from <code>IndexFaces</code> </p> <p>For more information, see Model Versioning in the Amazon Rekognition Developer Guide.</p> <p>If you provide the optional <code>ExternalImageId</code> for the input image you provided, Amazon Rekognition associates this ID with all faces that it detects. When you call the <a>ListFaces</a> operation, the response returns the external ID. You can use this external image ID to create a client-side index to associate the faces with each image. You can then use the index to find all faces in an image.</p> <p>You can specify the maximum number of faces to index with the <code>MaxFaces</code> input parameter. This is useful when you want to index the largest faces in an image and don't want to index smaller faces, such as those belonging to people standing in the background.</p> <p>The <code>QualityFilter</code> input parameter allows you to filter out detected faces that don’t meet a required quality bar. The quality bar is based on a variety of common use cases. By default, <code>IndexFaces</code> chooses the quality bar that's used to filter faces. You can also explicitly choose the quality bar. Use <code>QualityFilter</code>, to set the quality bar by specifying <code>LOW</code>, <code>MEDIUM</code>, or <code>HIGH</code>. If you do not want to filter detected faces, specify <code>NONE</code>. </p> <note> <p>To use quality filtering, you need a collection associated with version 3 of the face model or higher. To get the version of the face model associated with a collection, call <a>DescribeCollection</a>. </p> </note> <p>Information about faces detected in an image, but not indexed, is returned in an array of <a>UnindexedFace</a> objects, <code>UnindexedFaces</code>. Faces aren't indexed for reasons such as:</p> <ul> <li> <p>The number of faces detected exceeds the value of the <code>MaxFaces</code> request parameter.</p> </li> <li> <p>The face is too small compared to the image dimensions.</p> </li> <li> <p>The face is too blurry.</p> </li> <li> <p>The image is too dark.</p> </li> <li> <p>The face has an extreme pose.</p> </li> <li> <p>The face doesn’t have enough detail to be suitable for face search.</p> </li> </ul> <p>In response, the <code>IndexFaces</code> operation returns an array of metadata for all detected faces, <code>FaceRecords</code>. This includes: </p> <ul> <li> <p>The bounding box, <code>BoundingBox</code>, of the detected face. </p> </li> <li> <p>A confidence value, <code>Confidence</code>, which indicates the confidence that the bounding box contains a face.</p> </li> <li> <p>A face ID, <code>FaceId</code>, assigned by the service for each face that's detected and stored.</p> </li> <li> <p>An image ID, <code>ImageId</code>, assigned by the service for the input image.</p> </li> </ul> <p>If you request <code>ALL</code> or specific facial attributes (e.g., <code>FACE_OCCLUDED</code>) by using the detectionAttributes parameter, Amazon Rekognition returns detailed facial attributes, such as facial landmarks (for example, location of eye and mouth), facial occlusion, and other facial attributes.</p> <p>If you provide the same image, specify the same collection, and use the same external ID in the <code>IndexFaces</code> operation, Amazon Rekognition doesn't save duplicate face metadata.</p> <p></p> <p>The input image is passed either as base64-encoded image bytes, or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn't supported. The image must be formatted as a PNG or JPEG file. </p> <p>This operation requires permissions to perform the <code>rekognition:IndexFaces</code> action.</p>

        Args:
            collection_id: <p>The ID of an existing collection to which you want to add the faces that are detected in the input images.</p>
            image: <p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes isn't supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>
            external_image_id: <p>The ID you want to assign to all the faces detected in the image.</p>
            detection_attributes: <p>An array of facial attributes you want to be returned. A <code>DEFAULT</code> subset of facial attributes - <code>BoundingBox</code>, <code>Confidence</code>, <code>Pose</code>, <code>Quality</code>, and <code>Landmarks</code> - will always be returned. You can request for specific facial attributes (in addition to the default list) - by using <code>["DEFAULT", "FACE_OCCLUDED"]</code> or just <code>["FACE_OCCLUDED"]</code>. You can request for all facial attributes by using <code>["ALL"]</code>. Requesting more attributes may increase response time.</p> <p>If you provide both, <code>["ALL", "DEFAULT"]</code>, the service uses a logical AND operator to determine which attributes to return (in this case, all attributes). </p>
            max_faces: <p>The maximum number of faces to index. The value of <code>MaxFaces</code> must be greater than or equal to 1. <code>IndexFaces</code> returns no more than 100 detected faces in an image, even if you specify a larger value for <code>MaxFaces</code>.</p> <p>If <code>IndexFaces</code> detects more faces than the value of <code>MaxFaces</code>, the faces with the lowest quality are filtered out first. If there are still more faces than the value of <code>MaxFaces</code>, the faces with the smallest bounding boxes are filtered out (up to the number that's needed to satisfy the value of <code>MaxFaces</code>). Information about the unindexed faces is available in the <code>UnindexedFaces</code> array. </p> <p>The faces that are returned by <code>IndexFaces</code> are sorted by the largest face bounding box size to the smallest size, in descending order.</p> <p> <code>MaxFaces</code> can be used with a collection associated with any version of the face model.</p>
            quality_filter: <p>A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren't indexed. If you specify <code>AUTO</code>, Amazon Rekognition chooses the quality bar. If you specify <code>LOW</code>, <code>MEDIUM</code>, or <code>HIGH</code>, filtering removes all faces that don’t meet the chosen quality bar. The default value is <code>AUTO</code>. The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object that's misidentified as a face, a face that's too blurry, or a face with a pose that's too extreme to use. If you specify <code>NONE</code>, no filtering is performed. </p> <p>To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p></p> <p>The size of the collection exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add a face to a collection
            This operation detects faces in an image and adds them to the specified Rekognition collection.

            >>> client.index_faces(collection_id='myphotos', image={'S3Object': {'Bucket': 'mybucket', 'Name': 'myphoto'}}, external_image_id='myphotoid', detection_attributes=[])
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.index_faces_request.IndexFacesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.index_faces_response.IndexFacesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.index_faces

            output, http_response = (
                capo_rekognition._operations.rekognition_service.index_faces.index_faces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.index_faces_request.IndexFacesRequest = {
            "collection_id": collection_id,
            "image": image,
        }
        if external_image_id is not None:
            input_["external_image_id"] = external_image_id
        if detection_attributes is not None:
            input_["detection_attributes"] = detection_attributes
        if max_faces is not None:
            input_["max_faces"] = max_faces
        if quality_filter is not None:
            input_["quality_filter"] = quality_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_collections(
        self,
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_rekognition.types.page_size.PageSize"] = None,
    ) -> "capo_rekognition.types.list_collections_response.ListCollectionsResponse":
        """<p>Returns list of collection IDs in your account. If the result is truncated, the response also provides a <code>NextToken</code> that you can use in the subsequent request to fetch the next set of collection IDs.</p> <p>For an example, see Listing collections in the Amazon Rekognition Developer Guide.</p> <p>This operation requires permissions to perform the <code>rekognition:ListCollections</code> action.</p>

        Args:
            next_token: <p>Pagination token from the previous response.</p>
            max_results: <p>Maximum number of collection IDs to return. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the collections
            This operation returns a list of Rekognition collections.

            >>> client.list_collections()
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.list_collections_request.ListCollectionsRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.list_collections_response.ListCollectionsResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.list_collections

            output, http_response = (
                capo_rekognition._operations.rekognition_service.list_collections.list_collections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.list_collections_request.ListCollectionsRequest = {}
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

    def iter_list_collections(
        self,
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_rekognition.types.page_size.PageSize"] = None,
    ) -> "Iterator[capo_rekognition.types.collection_id.CollectionId]":
        _token = next_token
        while True:
            _response = self.list_collections(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("collection_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_dataset_entries(
        self,
        dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        contains_labels: Optional[
            "capo_rekognition.types.dataset_labels.DatasetLabels"
        ] = None,
        labeled: Optional["capo_rekognition.types.is_labeled.IsLabeled"] = None,
        source_ref_contains: Optional[
            "capo_rekognition.types.query_string.QueryString"
        ] = None,
        has_errors: Optional["capo_rekognition.types.has_errors.HasErrors"] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.list_dataset_entries_page_size.ListDatasetEntriesPageSize"
        ] = None,
    ) -> "capo_rekognition.types.list_dataset_entries_response.ListDatasetEntriesResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p> Lists the entries (images) within a dataset. An entry is a JSON Line that contains the information for a single image, including the image location, assigned labels, and object location bounding boxes. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-manifest-files.html">Creating a manifest file</a>.</p> <p>JSON Lines in the response include information about non-terminal errors found in the dataset. Non terminal errors are reported in <code>errors</code> lists within each JSON Line. The same information is reported in the training and testing validation result manifests that Amazon Rekognition Custom Labels creates during model training. </p> <p>You can filter the response in variety of ways, such as choosing which labels to return and returning JSON Lines created after a specific date. </p> <p>This operation requires permissions to perform the <code>rekognition:ListDatasetEntries</code> action.</p>

        Args:
            dataset_arn: <p> The Amazon Resource Name (ARN) for the dataset that you want to use. </p>
            contains_labels: <p>Specifies a label filter for the response. The response includes an entry only if one or more of the labels in <code>ContainsLabels</code> exist in the entry. </p>
            labeled: <p> Specify <code>true</code> to get only the JSON Lines where the image is labeled. Specify <code>false</code> to get only the JSON Lines where the image isn't labeled. If you don't specify <code>Labeled</code>, <code>ListDatasetEntries</code> returns JSON Lines for labeled and unlabeled images. </p>
            source_ref_contains: <p>If specified, <code>ListDatasetEntries</code> only returns JSON Lines where the value of <code>SourceRefContains</code> is part of the <code>source-ref</code> field. The <code>source-ref</code> field contains the Amazon S3 location of the image. You can use <code>SouceRefContains</code> for tasks such as getting the JSON Line for a single image, or gettting JSON Lines for all images within a specific folder.</p>
            has_errors: <p>Specifies an error filter for the response. Specify <code>True</code> to only include entries that have errors. </p>
            next_token: <p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource isn't ready. For example, this exception occurs when you call <code>DetectCustomLabels</code> with a model version that isn't deployed. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the entries in an Amazon Rekognition Custom Labels dataset
            Lists the JSON line entries in an Amazon Rekognition Custom Labels dataset.

            >>> client.list_dataset_entries(dataset_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-proj-2/dataset/train/1690564858106', contains_labels=['camellia'], labeled=True, source_ref_contains='camellia4.jpg', has_errors=True, next_token='', max_results=100)
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.list_dataset_entries_request.ListDatasetEntriesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.list_dataset_entries_response.ListDatasetEntriesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.list_dataset_entries

            output, http_response = (
                capo_rekognition._operations.rekognition_service.list_dataset_entries.list_dataset_entries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.list_dataset_entries_request.ListDatasetEntriesRequest = {
            "dataset_arn": dataset_arn
        }
        if contains_labels is not None:
            input_["contains_labels"] = contains_labels
        if labeled is not None:
            input_["labeled"] = labeled
        if source_ref_contains is not None:
            input_["source_ref_contains"] = source_ref_contains
        if has_errors is not None:
            input_["has_errors"] = has_errors
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

    def iter_list_dataset_entries(
        self,
        dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        contains_labels: Optional[
            "capo_rekognition.types.dataset_labels.DatasetLabels"
        ] = None,
        labeled: Optional["capo_rekognition.types.is_labeled.IsLabeled"] = None,
        source_ref_contains: Optional[
            "capo_rekognition.types.query_string.QueryString"
        ] = None,
        has_errors: Optional["capo_rekognition.types.has_errors.HasErrors"] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.list_dataset_entries_page_size.ListDatasetEntriesPageSize"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.dataset_entry.DatasetEntry]":
        _token = next_token
        while True:
            _response = self.list_dataset_entries(
                dataset_arn,
                config_overrides=config_overrides,
                contains_labels=contains_labels,
                labeled=labeled,
                source_ref_contains=source_ref_contains,
                has_errors=has_errors,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dataset_entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_dataset_labels(
        self,
        dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.list_dataset_labels_page_size.ListDatasetLabelsPageSize"
        ] = None,
    ) -> (
        "capo_rekognition.types.list_dataset_labels_response.ListDatasetLabelsResponse"
    ):
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Lists the labels in a dataset. Amazon Rekognition Custom Labels uses labels to describe images. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-labeling-images.html">Labeling images</a>. </p> <p> Lists the labels in a dataset. Amazon Rekognition Custom Labels uses labels to describe images. For more information, see Labeling images in the <i>Amazon Rekognition Custom Labels Developer Guide</i>. </p>

        Args:
            dataset_arn: <p> The Amazon Resource Name (ARN) of the dataset that you want to use. </p>
            next_token: <p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource isn't ready. For example, this exception occurs when you call <code>DetectCustomLabels</code> with a model version that isn't deployed. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the entries in an Amazon Rekognition Custom Labels dataset
            Lists the JSON line entries in an Amazon Rekognition Custom Labels dataset.

            >>> client.list_dataset_labels(dataset_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-proj-2/dataset/train/1690564858106', next_token='', max_results=100)
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.list_dataset_labels_request.ListDatasetLabelsRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.list_dataset_labels_response.ListDatasetLabelsResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.list_dataset_labels

            output, http_response = (
                capo_rekognition._operations.rekognition_service.list_dataset_labels.list_dataset_labels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.list_dataset_labels_request.ListDatasetLabelsRequest = {
            "dataset_arn": dataset_arn
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

    def iter_list_dataset_labels(
        self,
        dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.list_dataset_labels_page_size.ListDatasetLabelsPageSize"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.dataset_label_description.DatasetLabelDescription]":
        _token = next_token
        while True:
            _response = self.list_dataset_labels(
                dataset_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dataset_label_descriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_faces(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_rekognition.types.page_size.PageSize"] = None,
        user_id: Optional["capo_rekognition.types.user_id.UserId"] = None,
        face_ids: Optional["capo_rekognition.types.face_id_list.FaceIdList"] = None,
    ) -> "capo_rekognition.types.list_faces_response.ListFacesResponse":
        """<p>Returns metadata for faces in the specified collection. This metadata includes information such as the bounding box coordinates, the confidence (that the bounding box contains a face), and face ID. For an example, see Listing Faces in a Collection in the Amazon Rekognition Developer Guide.</p> <p>This operation requires permissions to perform the <code>rekognition:ListFaces</code> action.</p>

        Args:
            collection_id: <p>ID of the collection from which to list the faces.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of faces.</p>
            max_results: <p>Maximum number of faces to return.</p>
            user_id: <p>An array of user IDs to filter results with when listing faces in a collection.</p>
            face_ids: <p>An array of face IDs to filter results with when listing faces in a collection.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the faces in a collection
            This operation lists the faces in a Rekognition collection.

            >>> client.list_faces(collection_id='myphotos', max_results=20)
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.list_faces_request.ListFacesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.list_faces_response.ListFacesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.list_faces

            output, http_response = (
                capo_rekognition._operations.rekognition_service.list_faces.list_faces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.list_faces_request.ListFacesRequest = {
            "collection_id": collection_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if user_id is not None:
            input_["user_id"] = user_id
        if face_ids is not None:
            input_["face_ids"] = face_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_faces(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_rekognition.types.page_size.PageSize"] = None,
        user_id: Optional["capo_rekognition.types.user_id.UserId"] = None,
        face_ids: Optional["capo_rekognition.types.face_id_list.FaceIdList"] = None,
    ) -> "Iterator[capo_rekognition.types.face.Face]":
        _token = next_token
        while True:
            _response = self.list_faces(
                collection_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                user_id=user_id,
                face_ids=face_ids,
            )
            _page = _resolve_path(_response, ("faces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_media_analysis_jobs(
        self,
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.list_media_analysis_jobs_page_size.ListMediaAnalysisJobsPageSize"
        ] = None,
    ) -> "capo_rekognition.types.list_media_analysis_jobs_response.ListMediaAnalysisJobsResponse":
        """<important> <p>Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html">Rekognition feature availability changes</a>.</p> <p> <b>This change does not impact the availability of other Amazon Rekognition features.</b> </p> </important> <p>Returns a list of media analysis jobs. Results are sorted by <code>CreationTimestamp</code> in descending order.</p>

        Args:
            next_token: <p>Pagination token, if the previous response was incomplete.</p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value user can specify is 100. If user specifies a value greater than 100, an <code>InvalidParameterException</code> error occurs. The default value is 100.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.list_media_analysis_jobs_request.ListMediaAnalysisJobsRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.list_media_analysis_jobs_response.ListMediaAnalysisJobsResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.list_media_analysis_jobs

            output, http_response = (
                capo_rekognition._operations.rekognition_service.list_media_analysis_jobs.list_media_analysis_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.list_media_analysis_jobs_request.ListMediaAnalysisJobsRequest = {}
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

    def iter_list_media_analysis_jobs(
        self,
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.list_media_analysis_jobs_page_size.ListMediaAnalysisJobsPageSize"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.list_media_analysis_jobs_response.ListMediaAnalysisJobsResponse]":
        _token = next_token
        while True:
            _response = self.list_media_analysis_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_project_policies(
        self,
        project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.list_project_policies_page_size.ListProjectPoliciesPageSize"
        ] = None,
    ) -> "capo_rekognition.types.list_project_policies_response.ListProjectPoliciesResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Gets a list of the project policies attached to a project.</p> <p>To attach a project policy to a project, call <a>PutProjectPolicy</a>. To remove a project policy from a project, call <a>DeleteProjectPolicy</a>.</p> <p>This operation requires permissions to perform the <code>rekognition:ListProjectPolicies</code> action.</p>

        Args:
            project_arn: <p>The ARN of the project for which you want to list the project policies.</p>
            next_token: <p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value you can specify is 5. If you specify a value greater than 5, a ValidationException error occurs. The default value is 5. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.list_project_policies_request.ListProjectPoliciesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.list_project_policies_response.ListProjectPoliciesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.list_project_policies

            output, http_response = (
                capo_rekognition._operations.rekognition_service.list_project_policies.list_project_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.list_project_policies_request.ListProjectPoliciesRequest = {
            "project_arn": project_arn
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

    def iter_list_project_policies(
        self,
        project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
        ] = None,
        max_results: Optional[
            "capo_rekognition.types.list_project_policies_page_size.ListProjectPoliciesPageSize"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.project_policy.ProjectPolicy]":
        _token = next_token
        while True:
            _response = self.list_project_policies(
                project_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("project_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stream_processors(
        self,
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
    ) -> "capo_rekognition.types.list_stream_processors_response.ListStreamProcessorsResponse":
        """<important> <p>Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html">Rekognition feature availability changes</a>.</p> <p> <b>This change does not impact the availability of other Amazon Rekognition features.</b> </p> </important> <p>Gets a list of stream processors that you have created with <a>CreateStreamProcessor</a>. </p>

        Args:
            next_token: <p>If the previous response was incomplete (because there are more stream processors to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of stream processors. </p>
            max_results: <p>Maximum number of stream processors you want Amazon Rekognition Video to return in the response. The default is 1000. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.list_stream_processors_request.ListStreamProcessorsRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.list_stream_processors_response.ListStreamProcessorsResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.list_stream_processors

            output, http_response = (
                capo_rekognition._operations.rekognition_service.list_stream_processors.list_stream_processors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.list_stream_processors_request.ListStreamProcessorsRequest = {}
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

    def iter_list_stream_processors(
        self,
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_rekognition.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_rekognition.types.list_stream_processors_response.ListStreamProcessorsResponse]":
        _token = next_token
        while True:
            _response = self.list_stream_processors(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_rekognition.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Returns a list of tags in an Amazon Rekognition collection, stream processor, or Custom Labels model. </p> <p>This operation requires permissions to perform the <code>rekognition:ListTagsForResource</code> action. </p>

        Args:
            resource_arn: <p> Amazon Resource Name (ARN) of the model, collection, or stream processor that contains the tags that you want a list of. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.list_tags_for_resource

            output, http_response = (
                capo_rekognition._operations.rekognition_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_users(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional[
            "capo_rekognition.types.max_user_results.MaxUserResults"
        ] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_rekognition.types.list_users_response.ListUsersResponse":
        """<p>Returns metadata of the User such as <code>UserID</code> in the specified collection. Anonymous User (to reserve faces without any identity) is not returned as part of this request. The results are sorted by system generated primary key ID. If the response is truncated, <code>NextToken</code> is returned in the response that can be used in the subsequent request to retrieve the next set of identities.</p>

        Args:
            collection_id: <p>The ID of an existing collection.</p>
            max_results: <p>Maximum number of UsersID to return. </p>
            next_token: <p>Pagingation token to receive the next set of UsersID.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Pagination token in the request is not valid.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListUsers
            Returns metadata of the User such as UserID in the specified collection.

            >>> client.list_users(collection_id='MyCollection')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.list_users_request.ListUsersRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.list_users_response.ListUsersResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.list_users

            output, http_response = (
                capo_rekognition._operations.rekognition_service.list_users.list_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.list_users_request.ListUsersRequest = {
            "collection_id": collection_id
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

    def iter_list_users(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_results: Optional[
            "capo_rekognition.types.max_user_results.MaxUserResults"
        ] = None,
        next_token: Optional[
            "capo_rekognition.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_rekognition.types.user.User]":
        _token = next_token
        while True:
            _response = self.list_users(
                collection_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_project_policy(
        self,
        project_arn: "capo_rekognition.types.project_arn.ProjectArn",
        policy_name: "capo_rekognition.types.project_policy_name.ProjectPolicyName",
        policy_document: "capo_rekognition.types.project_policy_document.ProjectPolicyDocument",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        policy_revision_id: Optional[
            "capo_rekognition.types.project_policy_revision_id.ProjectPolicyRevisionId"
        ] = None,
    ) -> "capo_rekognition.types.put_project_policy_response.PutProjectPolicyResponse":
        r"""<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Attaches a project policy to a Amazon Rekognition Custom Labels project in a trusting AWS account. A project policy specifies that a trusted AWS account can copy a model version from a trusting AWS account to a project in the trusted AWS account. To copy a model version you use the <a>CopyProjectVersion</a> operation. Only applies to Custom Labels projects.</p> <p>For more information about the format of a project policy document, see Attaching a project policy (SDK) in the <i>Amazon Rekognition Custom Labels Developer Guide</i>. </p> <p>The response from <code>PutProjectPolicy</code> is a revision ID for the project policy. You can attach multiple project policies to a project. You can also update an existing project policy by specifying the policy revision ID of the existing policy.</p> <p>To remove a project policy from a project, call <a>DeleteProjectPolicy</a>. To get a list of project policies attached to a project, call <a>ListProjectPolicies</a>. </p> <p>You copy a model version by calling <a>CopyProjectVersion</a>.</p> <p>This operation requires permissions to perform the <code>rekognition:PutProjectPolicy</code> action.</p>

        Args:
            project_arn: <p>The Amazon Resource Name (ARN) of the project that the project policy is attached to.</p>
            policy_name: <p>A name for the policy.</p>
            policy_revision_id: <p>The revision ID for the Project Policy. Each time you modify a policy, Amazon Rekognition Custom Labels generates and assigns a new <code>PolicyRevisionId</code> and then deletes the previous version of the policy.</p>
            policy_document: <p>A resource policy to add to the model. The policy is a JSON structure that contains one or more statements that define the policy. The policy must follow the IAM syntax. For more information about the contents of a JSON policy document, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html">IAM JSON policy reference</a>. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_policy_revision_id_exception.InvalidPolicyRevisionIdException: <p>The supplied revision id for the project policy is invalid.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>The format of the project policy document that you supplied to <code>PutProjectPolicy</code> is incorrect. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>A resource with the specified ID already exists.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p></p> <p>The size of the collection exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            PutProjectPolicy
            This operation attaches a project policy to a Amazon Rekognition Custom Labels project in a trusting AWS account.

            >>> client.put_project_policy(project_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-sdk-project/1656557051929', policy_name='SamplePolicy', policy_revision_id='0123456789abcdef', policy_document='\'{"Version":"2012-10-17","Statement":[{"Effect":"ALLOW","Principal":{"AWS":"principal"},"Action":"rekognition:CopyProjectVersion","Resource":"arn:aws:rekognition:us-east-1:123456789012:project/my-sdk-project/version/DestinationVersionName/1627045542080"}]}\'')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.put_project_policy_request.PutProjectPolicyRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.put_project_policy_response.PutProjectPolicyResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.put_project_policy

            output, http_response = (
                capo_rekognition._operations.rekognition_service.put_project_policy.put_project_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.put_project_policy_request.PutProjectPolicyRequest = {
            "project_arn": project_arn,
            "policy_name": policy_name,
            "policy_document": policy_document,
        }
        if policy_revision_id is not None:
            input_["policy_revision_id"] = policy_revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def recognize_celebrities(
        self,
        image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.recognize_celebrities_response.RecognizeCelebritiesResponse":
        """<p>Returns an array of celebrities recognized in the input image. For more information, see Recognizing celebrities in the Amazon Rekognition Developer Guide. </p> <p> <code>RecognizeCelebrities</code> returns the 64 largest faces in the image. It lists the recognized celebrities in the <code>CelebrityFaces</code> array and any unrecognized faces in the <code>UnrecognizedFaces</code> array. <code>RecognizeCelebrities</code> doesn't return celebrities whose faces aren't among the largest 64 faces in the image.</p> <p>For each celebrity recognized, <code>RecognizeCelebrities</code> returns a <code>Celebrity</code> object. The <code>Celebrity</code> object contains the celebrity name, ID, URL links to additional information, match confidence, and a <code>ComparedFace</code> object that you can use to locate the celebrity's face on the image.</p> <p>Amazon Rekognition doesn't retain information about which images a celebrity has been recognized in. Your application must store this information and use the <code>Celebrity</code> ID property as a unique identifier for the celebrity. If you don't store the celebrity name or additional information URLs returned by <code>RecognizeCelebrities</code>, you will need the ID to identify the celebrity in a call to the <a>GetCelebrityInfo</a> operation.</p> <p>You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. </p> <p>For an example, see Recognizing celebrities in an image in the Amazon Rekognition Developer Guide.</p> <p>This operation requires permissions to perform the <code>rekognition:RecognizeCelebrities</code> operation.</p>

        Args:
            image: <p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.recognize_celebrities_request.RecognizeCelebritiesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.recognize_celebrities_response.RecognizeCelebritiesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.recognize_celebrities

            output, http_response = (
                capo_rekognition._operations.rekognition_service.recognize_celebrities.recognize_celebrities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.recognize_celebrities_request.RecognizeCelebritiesRequest = {
            "image": image
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_faces(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        face_id: "capo_rekognition.types.face_id.FaceId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_faces: Optional["capo_rekognition.types.max_faces.MaxFaces"] = None,
        face_match_threshold: Optional["capo_rekognition.types.percent.Percent"] = None,
    ) -> "capo_rekognition.types.search_faces_response.SearchFacesResponse":
        """<p>For a given input face ID, searches for matching faces in the collection the face belongs to. You get a face ID when you add a face to the collection using the <a>IndexFaces</a> operation. The operation compares the features of the input face with faces in the specified collection. </p> <note> <p>You can also search faces without indexing faces by using the <code>SearchFacesByImage</code> operation.</p> </note> <p> The operation response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match that is found. Along with the metadata, the response also includes a <code>confidence</code> value for each face match, indicating the confidence that the specific face matches the input face. </p> <p>For an example, see Searching for a face using its face ID in the Amazon Rekognition Developer Guide.</p> <p>This operation requires permissions to perform the <code>rekognition:SearchFaces</code> action.</p>

        Args:
            collection_id: <p>ID of the collection the face belongs to.</p>
            face_id: <p>ID of a face to find matches for in the collection.</p>
            max_faces: <p>Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.</p>
            face_match_threshold: <p>Optional value specifying the minimum confidence in the face match to return. For example, don't return any matches where confidence in matches is less than 70%. The default value is 80%. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a face
            This operation searches for matching faces in the collection the supplied face belongs to.

            >>> client.search_faces(collection_id='myphotos', face_id='70008e50-75e4-55d0-8e80-363fb73b3a14', max_faces=10, face_match_threshold=90)
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.search_faces_request.SearchFacesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.search_faces_response.SearchFacesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.search_faces

            output, http_response = (
                capo_rekognition._operations.rekognition_service.search_faces.search_faces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.search_faces_request.SearchFacesRequest = {
            "collection_id": collection_id,
            "face_id": face_id,
        }
        if max_faces is not None:
            input_["max_faces"] = max_faces
        if face_match_threshold is not None:
            input_["face_match_threshold"] = face_match_threshold

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_faces_by_image(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_faces: Optional["capo_rekognition.types.max_faces.MaxFaces"] = None,
        face_match_threshold: Optional["capo_rekognition.types.percent.Percent"] = None,
        quality_filter: Optional[
            "capo_rekognition.types.quality_filter.QualityFilter"
        ] = None,
    ) -> "capo_rekognition.types.search_faces_by_image_response.SearchFacesByImageResponse":
        """<p>For a given input image, first detects the largest face in the image, and then searches the specified collection for matching faces. The operation compares the features of the input face with faces in the specified collection. </p> <note> <p>To search for all faces in an input image, you might first call the <a>IndexFaces</a> operation, and then use the face IDs returned in subsequent calls to the <a>SearchFaces</a> operation. </p> <p> You can also call the <code>DetectFaces</code> operation and use the bounding boxes in the response to make face crops, which then you can pass in to the <code>SearchFacesByImage</code> operation. </p> </note> <p>You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. </p> <p> The response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match found. Along with the metadata, the response also includes a <code>similarity</code> indicating how similar the face is to the input face. In the response, the operation also returns the bounding box (and a confidence level that the bounding box contains a face) of the face that Amazon Rekognition used for the input image. </p> <p>If no faces are detected in the input image, <code>SearchFacesByImage</code> returns an <code>InvalidParameterException</code> error. </p> <p>For an example, Searching for a Face Using an Image in the Amazon Rekognition Developer Guide.</p> <p>The <code>QualityFilter</code> input parameter allows you to filter out detected faces that don’t meet a required quality bar. The quality bar is based on a variety of common use cases. Use <code>QualityFilter</code> to set the quality bar for filtering by specifying <code>LOW</code>, <code>MEDIUM</code>, or <code>HIGH</code>. If you do not want to filter detected faces, specify <code>NONE</code>. The default value is <code>NONE</code>.</p> <note> <p>To use quality filtering, you need a collection associated with version 3 of the face model or higher. To get the version of the face model associated with a collection, call <a>DescribeCollection</a>. </p> </note> <p>This operation requires permissions to perform the <code>rekognition:SearchFacesByImage</code> action.</p>

        Args:
            collection_id: <p>ID of the collection to search.</p>
            image: <p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>
            max_faces: <p>Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.</p>
            face_match_threshold: <p>(Optional) Specifies the minimum confidence in the face match to return. For example, don't return any matches where confidence in matches is less than 70%. The default value is 80%.</p>
            quality_filter: <p>A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren't searched for in the collection. If you specify <code>AUTO</code>, Amazon Rekognition chooses the quality bar. If you specify <code>LOW</code>, <code>MEDIUM</code>, or <code>HIGH</code>, filtering removes all faces that don’t meet the chosen quality bar. The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object that's misidentified as a face, a face that's too blurry, or a face with a pose that's too extreme to use. If you specify <code>NONE</code>, no filtering is performed. The default value is <code>NONE</code>. </p> <p>To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To search for faces matching a supplied image
            This operation searches for faces in a Rekognition collection that match the largest face in an S3 bucket stored image.

            >>> client.search_faces_by_image(collection_id='myphotos', image={'S3Object': {'Bucket': 'mybucket', 'Name': 'myphoto'}}, max_faces=5, face_match_threshold=95)
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.search_faces_by_image_request.SearchFacesByImageRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.search_faces_by_image_response.SearchFacesByImageResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.search_faces_by_image

            output, http_response = (
                capo_rekognition._operations.rekognition_service.search_faces_by_image.search_faces_by_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.search_faces_by_image_request.SearchFacesByImageRequest = {
            "collection_id": collection_id,
            "image": image,
        }
        if max_faces is not None:
            input_["max_faces"] = max_faces
        if face_match_threshold is not None:
            input_["face_match_threshold"] = face_match_threshold
        if quality_filter is not None:
            input_["quality_filter"] = quality_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_users(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        user_id: Optional["capo_rekognition.types.user_id.UserId"] = None,
        face_id: Optional["capo_rekognition.types.face_id.FaceId"] = None,
        user_match_threshold: Optional["capo_rekognition.types.percent.Percent"] = None,
        max_users: Optional[
            "capo_rekognition.types.max_user_results.MaxUserResults"
        ] = None,
    ) -> "capo_rekognition.types.search_users_response.SearchUsersResponse":
        """<p>Searches for UserIDs within a collection based on a <code>FaceId</code> or <code>UserId</code>. This API can be used to find the closest UserID (with a highest similarity) to associate a face. The request must be provided with either <code>FaceId</code> or <code>UserId</code>. The operation returns an array of UserID that match the <code>FaceId</code> or <code>UserId</code>, ordered by similarity score with the highest similarity first. </p>

        Args:
            collection_id: <p>The ID of an existing collection containing the UserID, used with a UserId or FaceId. If a FaceId is provided, UserId isn’t required to be present in the Collection.</p>
            user_id: <p>ID for the existing User.</p>
            face_id: <p>ID for the existing face.</p>
            user_match_threshold: <p>Optional value that specifies the minimum confidence in the matched UserID to return. Default value of 80.</p>
            max_users: <p>Maximum number of identities to return.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SearchUsers
            Searches for UserIDs within a collection based on a FaceId or UserId.

            >>> client.search_users(collection_id='MyCollection', user_id='DemoUser', max_users=2, user_match_threshold=70)
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.search_users_request.SearchUsersRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.search_users_response.SearchUsersResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.search_users

            output, http_response = (
                capo_rekognition._operations.rekognition_service.search_users.search_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.search_users_request.SearchUsersRequest = {
            "collection_id": collection_id
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if face_id is not None:
            input_["face_id"] = face_id
        if user_match_threshold is not None:
            input_["user_match_threshold"] = user_match_threshold
        if max_users is not None:
            input_["max_users"] = max_users

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_users_by_image(
        self,
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        image: "capo_rekognition.types.image.Image",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        user_match_threshold: Optional["capo_rekognition.types.percent.Percent"] = None,
        max_users: Optional[
            "capo_rekognition.types.max_user_results.MaxUserResults"
        ] = None,
        quality_filter: Optional[
            "capo_rekognition.types.quality_filter.QualityFilter"
        ] = None,
    ) -> "capo_rekognition.types.search_users_by_image_response.SearchUsersByImageResponse":
        """<p>Searches for UserIDs using a supplied image. It first detects the largest face in the image, and then searches a specified collection for matching UserIDs. </p> <p>The operation returns an array of UserIDs that match the face in the supplied image, ordered by similarity score with the highest similarity first. It also returns a bounding box for the face found in the input image. </p> <p>Information about faces detected in the supplied image, but not used for the search, is returned in an array of <code>UnsearchedFace</code> objects. If no valid face is detected in the image, the response will contain an empty <code>UserMatches</code> list and no <code>SearchedFace</code> object. </p>

        Args:
            collection_id: <p>The ID of an existing collection containing the UserID.</p>
            user_match_threshold: <p>Specifies the minimum confidence in the UserID match to return. Default value is 80.</p>
            max_users: <p>Maximum number of UserIDs to return.</p>
            quality_filter: <p>A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren't searched for in the collection. The default value is NONE.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.image_too_large_exception.ImageTooLargeException: <p>The input image size exceeds the allowed limit. If you are calling DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException: <p>The provided image format is not supported. </p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SearchUsersByImage
            Searches for UserIDs using a supplied image.

            >>> client.search_users_by_image(collection_id='MyCollection', image={'S3Object': {'Bucket': 'bucket', 'Name': 'input.jpg'}}, max_users=2, user_match_threshold=70, quality_filter='MEDIUM')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.search_users_by_image_request.SearchUsersByImageRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.search_users_by_image_response.SearchUsersByImageResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.search_users_by_image

            output, http_response = (
                capo_rekognition._operations.rekognition_service.search_users_by_image.search_users_by_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.search_users_by_image_request.SearchUsersByImageRequest = {
            "collection_id": collection_id,
            "image": image,
        }
        if user_match_threshold is not None:
            input_["user_match_threshold"] = user_match_threshold
        if max_users is not None:
            input_["max_users"] = max_users
        if quality_filter is not None:
            input_["quality_filter"] = quality_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_celebrity_recognition(
        self,
        video: "capo_rekognition.types.video.Video",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
        notification_channel: Optional[
            "capo_rekognition.types.notification_channel.NotificationChannel"
        ] = None,
        job_tag: Optional["capo_rekognition.types.job_tag.JobTag"] = None,
    ) -> "capo_rekognition.types.start_celebrity_recognition_response.StartCelebrityRecognitionResponse":
        """<p>Starts asynchronous recognition of celebrities in a stored video.</p> <p>Amazon Rekognition Video can detect celebrities in a video must be stored in an Amazon S3 bucket. Use <a>Video</a> to specify the bucket name and the filename of the video. <code>StartCelebrityRecognition</code> returns a job identifier (<code>JobId</code>) which you use to get the results of the analysis. When celebrity recognition analysis is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in <code>NotificationChannel</code>. To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetCelebrityRecognition</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartCelebrityRecognition</code>. </p> <p>For more information, see Recognizing celebrities in the Amazon Rekognition Developer Guide.</p>

        Args:
            video: <p>The video in which you want to recognize celebrities. The video must be stored in an Amazon S3 bucket.</p>
            client_request_token: <p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartCelebrityRecognition</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>
            notification_channel: <p>The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status of the celebrity recognition analysis to. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy.</p>
            job_tag: <p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.video_too_large_exception.VideoTooLargeException: <p>The file size or duration of the supplied media is too large. The maximum file size is 10GB. The maximum duration is 6 hours. </p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_celebrity_recognition_request.StartCelebrityRecognitionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_celebrity_recognition_response.StartCelebrityRecognitionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_celebrity_recognition

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_celebrity_recognition.start_celebrity_recognition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_celebrity_recognition_request.StartCelebrityRecognitionRequest = {
            "video": video
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if job_tag is not None:
            input_["job_tag"] = job_tag

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_content_moderation(
        self,
        video: "capo_rekognition.types.video.Video",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        min_confidence: Optional["capo_rekognition.types.percent.Percent"] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
        notification_channel: Optional[
            "capo_rekognition.types.notification_channel.NotificationChannel"
        ] = None,
        job_tag: Optional["capo_rekognition.types.job_tag.JobTag"] = None,
    ) -> "capo_rekognition.types.start_content_moderation_response.StartContentModerationResponse":
        """<p> Starts asynchronous detection of inappropriate, unwanted, or offensive content in a stored video. For a list of moderation labels in Amazon Rekognition, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api">Using the image and video moderation APIs</a>.</p> <p>Amazon Rekognition Video can moderate content in a video stored in an Amazon S3 bucket. Use <a>Video</a> to specify the bucket name and the filename of the video. <code>StartContentModeration</code> returns a job identifier (<code>JobId</code>) which you use to get the results of the analysis. When content analysis is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in <code>NotificationChannel</code>.</p> <p>To get the results of the content analysis, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetContentModeration</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartContentModeration</code>. </p> <p>For more information, see Moderating content in the Amazon Rekognition Developer Guide.</p>

        Args:
            video: <p>The video in which you want to detect inappropriate, unwanted, or offensive content. The video must be stored in an Amazon S3 bucket.</p>
            min_confidence: <p>Specifies the minimum confidence that Amazon Rekognition must have in order to return a moderated content label. Confidence represents how certain Amazon Rekognition is that the moderated content is correctly identified. 0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition doesn't return any moderated content labels with a confidence level lower than this specified value. If you don't specify <code>MinConfidence</code>, <code>GetContentModeration</code> returns labels with confidence values greater than or equal to 50 percent.</p>
            client_request_token: <p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartContentModeration</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>
            notification_channel: <p>The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status of the content analysis to. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy to access the topic.</p>
            job_tag: <p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.video_too_large_exception.VideoTooLargeException: <p>The file size or duration of the supplied media is too large. The maximum file size is 10GB. The maximum duration is 6 hours. </p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_content_moderation_request.StartContentModerationRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_content_moderation_response.StartContentModerationResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_content_moderation

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_content_moderation.start_content_moderation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_content_moderation_request.StartContentModerationRequest = {
            "video": video
        }
        if min_confidence is not None:
            input_["min_confidence"] = min_confidence
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if job_tag is not None:
            input_["job_tag"] = job_tag

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_face_detection(
        self,
        video: "capo_rekognition.types.video.Video",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
        notification_channel: Optional[
            "capo_rekognition.types.notification_channel.NotificationChannel"
        ] = None,
        face_attributes: Optional[
            "capo_rekognition.types.face_attributes.FaceAttributes"
        ] = None,
        job_tag: Optional["capo_rekognition.types.job_tag.JobTag"] = None,
    ) -> "capo_rekognition.types.start_face_detection_response.StartFaceDetectionResponse":
        """<p>Starts asynchronous detection of faces in a stored video.</p> <p>Amazon Rekognition Video can detect faces in a video stored in an Amazon S3 bucket. Use <a>Video</a> to specify the bucket name and the filename of the video. <code>StartFaceDetection</code> returns a job identifier (<code>JobId</code>) that you use to get the results of the operation. When face detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in <code>NotificationChannel</code>. To get the results of the face detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetFaceDetection</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartFaceDetection</code>.</p> <p>For more information, see Detecting faces in a stored video in the Amazon Rekognition Developer Guide.</p>

        Args:
            video: <p>The video in which you want to detect faces. The video must be stored in an Amazon S3 bucket.</p>
            client_request_token: <p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartFaceDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>
            notification_channel: <p>The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the face detection operation. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy.</p>
            face_attributes: <p>The face attributes you want returned.</p> <p> <code>DEFAULT</code> - The following subset of facial attributes are returned: BoundingBox, Confidence, Pose, Quality and Landmarks. </p> <p> <code>ALL</code> - All facial attributes are returned.</p>
            job_tag: <p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.video_too_large_exception.VideoTooLargeException: <p>The file size or duration of the supplied media is too large. The maximum file size is 10GB. The maximum duration is 6 hours. </p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_face_detection_request.StartFaceDetectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_face_detection_response.StartFaceDetectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_face_detection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_face_detection.start_face_detection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_face_detection_request.StartFaceDetectionRequest = {
            "video": video
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if face_attributes is not None:
            input_["face_attributes"] = face_attributes
        if job_tag is not None:
            input_["job_tag"] = job_tag

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_face_search(
        self,
        video: "capo_rekognition.types.video.Video",
        collection_id: "capo_rekognition.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
        face_match_threshold: Optional["capo_rekognition.types.percent.Percent"] = None,
        notification_channel: Optional[
            "capo_rekognition.types.notification_channel.NotificationChannel"
        ] = None,
        job_tag: Optional["capo_rekognition.types.job_tag.JobTag"] = None,
    ) -> "capo_rekognition.types.start_face_search_response.StartFaceSearchResponse":
        """<p>Starts the asynchronous search for faces in a collection that match the faces of persons detected in a stored video.</p> <p>The video must be stored in an Amazon S3 bucket. Use <a>Video</a> to specify the bucket name and the filename of the video. <code>StartFaceSearch</code> returns a job identifier (<code>JobId</code>) which you use to get the search results once the search has completed. When searching is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in <code>NotificationChannel</code>. To get the search results, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetFaceSearch</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartFaceSearch</code>. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/procedure-person-search-videos.html">Searching stored videos for faces</a>. </p>

        Args:
            video: <p>The video you want to search. The video must be stored in an Amazon S3 bucket. </p>
            client_request_token: <p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartFaceSearch</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>
            face_match_threshold: <p>The minimum confidence in the person match to return. For example, don't return any matches where confidence in matches is less than 70%. The default value is 80%.</p>
            collection_id: <p>ID of the collection that contains the faces you want to search for.</p>
            notification_channel: <p>The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the search. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy to access the topic.</p>
            job_tag: <p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.video_too_large_exception.VideoTooLargeException: <p>The file size or duration of the supplied media is too large. The maximum file size is 10GB. The maximum duration is 6 hours. </p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_face_search_request.StartFaceSearchRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_face_search_response.StartFaceSearchResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_face_search

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_face_search.start_face_search(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_face_search_request.StartFaceSearchRequest = {
            "video": video,
            "collection_id": collection_id,
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if face_match_threshold is not None:
            input_["face_match_threshold"] = face_match_threshold
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if job_tag is not None:
            input_["job_tag"] = job_tag

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_label_detection(
        self,
        video: "capo_rekognition.types.video.Video",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
        min_confidence: Optional["capo_rekognition.types.percent.Percent"] = None,
        notification_channel: Optional[
            "capo_rekognition.types.notification_channel.NotificationChannel"
        ] = None,
        job_tag: Optional["capo_rekognition.types.job_tag.JobTag"] = None,
        features: Optional[
            "capo_rekognition.types.label_detection_feature_list.LabelDetectionFeatureList"
        ] = None,
        settings: Optional[
            "capo_rekognition.types.label_detection_settings.LabelDetectionSettings"
        ] = None,
    ) -> "capo_rekognition.types.start_label_detection_response.StartLabelDetectionResponse":
        """<p>Starts asynchronous detection of labels in a stored video.</p> <p>Amazon Rekognition Video can detect labels in a video. Labels are instances of real-world entities. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; concepts like landscape, evening, and nature; and activities like a person getting out of a car or a person skiing.</p> <p>The video must be stored in an Amazon S3 bucket. Use <a>Video</a> to specify the bucket name and the filename of the video. <code>StartLabelDetection</code> returns a job identifier (<code>JobId</code>) which you use to get the results of the operation. When label detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in <code>NotificationChannel</code>.</p> <p>To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetLabelDetection</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartLabelDetection</code>.</p> <p> <i>Optional Parameters</i> </p> <p> <code>StartLabelDetection</code> has the <code>GENERAL_LABELS</code> Feature applied by default. This feature allows you to provide filtering criteria to the <code>Settings</code> parameter. You can filter with sets of individual labels or with label categories. You can specify inclusive filters, exclusive filters, or a combination of inclusive and exclusive filters. For more information on filtering, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/labels-detecting-labels-video.html">Detecting labels in a video</a>.</p> <p>You can specify <code>MinConfidence</code> to control the confidence threshold for the labels returned. The default is 50.</p>

        Args:
            video: <p>The video in which you want to detect labels. The video must be stored in an Amazon S3 bucket.</p>
            client_request_token: <p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartLabelDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>
            min_confidence: <p>Specifies the minimum confidence that Amazon Rekognition Video must have in order to return a detected label. Confidence represents how certain Amazon Rekognition is that a label is correctly identified.0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition Video doesn't return any labels with a confidence level lower than this specified value.</p> <p>If you don't specify <code>MinConfidence</code>, the operation returns labels and bounding boxes (if detected) with confidence values greater than or equal to 50 percent.</p>
            notification_channel: <p>The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion status of the label detection operation to. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy.</p>
            job_tag: <p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>
            features: <p>The features to return after video analysis. You can specify that GENERAL_LABELS are returned.</p>
            settings: <p>The settings for a StartLabelDetection request.Contains the specified parameters for the label detection request of an asynchronous label analysis operation. Settings can include filters for GENERAL_LABELS.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.video_too_large_exception.VideoTooLargeException: <p>The file size or duration of the supplied media is too large. The maximum file size is 10GB. The maximum duration is 6 hours. </p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_label_detection_request.StartLabelDetectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_label_detection_response.StartLabelDetectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_label_detection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_label_detection.start_label_detection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_label_detection_request.StartLabelDetectionRequest = {
            "video": video
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if min_confidence is not None:
            input_["min_confidence"] = min_confidence
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if features is not None:
            input_["features"] = features
        if settings is not None:
            input_["settings"] = settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_media_analysis_job(
        self,
        operations_config: "capo_rekognition.types.media_analysis_operations_config.MediaAnalysisOperationsConfig",
        input: "capo_rekognition.types.media_analysis_input.MediaAnalysisInput",
        output_config: "capo_rekognition.types.media_analysis_output_config.MediaAnalysisOutputConfig",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
        job_name: Optional[
            "capo_rekognition.types.media_analysis_job_name.MediaAnalysisJobName"
        ] = None,
        kms_key_id: Optional["capo_rekognition.types.kms_key_id.KmsKeyId"] = None,
    ) -> "capo_rekognition.types.start_media_analysis_job_response.StartMediaAnalysisJobResponse":
        """<important> <p>Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html">Rekognition feature availability changes</a>.</p> <p> <b>This change does not impact the availability of other Amazon Rekognition features.</b> </p> </important> <p>Initiates a new media analysis job. Accepts a manifest file in an Amazon S3 bucket. The output is a manifest file and a summary of the manifest stored in the Amazon S3 bucket.</p>

        Args:
            client_request_token: <p>Idempotency token used to prevent the accidental creation of duplicate versions. If you use the same token with multiple <code>StartMediaAnalysisJobRequest</code> requests, the same response is returned. Use <code>ClientRequestToken</code> to prevent the same request from being processed more than once.</p>
            job_name: <p>The name of the job. Does not have to be unique.</p>
            operations_config: <p>Configuration options for the media analysis job to be created.</p>
            input: <p>Input data to be analyzed by the job.</p>
            output_config: <p>The Amazon S3 bucket location to store the results.</p>
            kms_key_id: <p>The identifier of customer managed AWS KMS key (name or ARN). The key is used to encrypt images copied into the service. The key is also used to encrypt results and manifest files written to the output Amazon S3 bucket.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_manifest_exception.InvalidManifestException: <p>Indicates that a provided manifest file is empty or larger than the allowed limit.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource isn't ready. For example, this exception occurs when you call <code>DetectCustomLabels</code> with a model version that isn't deployed. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            StartMediaAnalysisJob
            Initiates a new media analysis job.

            >>> client.start_media_analysis_job(job_name='job-name', operations_config={'DetectModerationLabels': {'MinConfidence': 50, 'ProjectVersion': 'arn:aws:rekognition:us-east-1:111122223333:project/my-project/version/1/1690556751958'}}, input={'S3Object': {'Bucket': 'input-bucket', 'Name': 'input-manifest.json'}}, output_config={'S3Bucket': 'output-bucket', 'S3KeyPrefix': 'output-location'})
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_media_analysis_job_request.StartMediaAnalysisJobRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_media_analysis_job_response.StartMediaAnalysisJobResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_media_analysis_job

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_media_analysis_job.start_media_analysis_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_media_analysis_job_request.StartMediaAnalysisJobRequest = {
            "operations_config": operations_config,
            "input": input,
            "output_config": output_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if job_name is not None:
            input_["job_name"] = job_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_person_tracking(
        self,
        video: "capo_rekognition.types.video.Video",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
        notification_channel: Optional[
            "capo_rekognition.types.notification_channel.NotificationChannel"
        ] = None,
        job_tag: Optional["capo_rekognition.types.job_tag.JobTag"] = None,
    ) -> "capo_rekognition.types.start_person_tracking_response.StartPersonTrackingResponse":
        """<note> <p> <i>End of support notice:</i> On October 31, 2025, AWS will discontinue support for Amazon Rekognition People Pathing. After October 31, 2025, you will no longer be able to use the Rekognition People Pathing capability. For more information, visit this <a href="https://aws.amazon.com/blogs/machine-learning/transitioning-from-amazon-rekognition-people-pathing-exploring-other-alternatives/">blog post</a>.</p> </note> <p>Starts the asynchronous tracking of a person's path in a stored video.</p> <p>Amazon Rekognition Video can track the path of people in a video stored in an Amazon S3 bucket. Use <a>Video</a> to specify the bucket name and the filename of the video. <code>StartPersonTracking</code> returns a job identifier (<code>JobId</code>) which you use to get the results of the operation. When label detection is finished, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic that you specify in <code>NotificationChannel</code>. </p> <p>To get the results of the person detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetPersonTracking</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartPersonTracking</code>.</p>

        Args:
            video: <p>The video in which you want to detect people. The video must be stored in an Amazon S3 bucket.</p>
            client_request_token: <p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartPersonTracking</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>
            notification_channel: <p>The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion status of the people detection operation to. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy.</p>
            job_tag: <p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.video_too_large_exception.VideoTooLargeException: <p>The file size or duration of the supplied media is too large. The maximum file size is 10GB. The maximum duration is 6 hours. </p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_person_tracking_request.StartPersonTrackingRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_person_tracking_response.StartPersonTrackingResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_person_tracking

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_person_tracking.start_person_tracking(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_person_tracking_request.StartPersonTrackingRequest = {
            "video": video
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if job_tag is not None:
            input_["job_tag"] = job_tag

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_project_version(
        self,
        project_version_arn: "capo_rekognition.types.project_version_arn.ProjectVersionArn",
        min_inference_units: "capo_rekognition.types.inference_units.InferenceUnits",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        max_inference_units: Optional[
            "capo_rekognition.types.inference_units.InferenceUnits"
        ] = None,
    ) -> "capo_rekognition.types.start_project_version_response.StartProjectVersionResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Starts the running of the version of a model. Starting a model takes a while to complete. To check the current state of the model, use <a>DescribeProjectVersions</a>. </p> <p>Once the model is running, you can detect custom labels in new images by calling <a>DetectCustomLabels</a>.</p> <note> <p>You are charged for the amount of time that the model is running. To stop a running model, call <a>StopProjectVersion</a>.</p> </note> <p>This operation requires permissions to perform the <code>rekognition:StartProjectVersion</code> action.</p>

        Args:
            project_version_arn: <p>The Amazon Resource Name(ARN) of the model version that you want to start.</p>
            min_inference_units: <p>The minimum number of inference units to use. A single inference unit represents 1 hour of processing. </p> <p>Use a higher number to increase the TPS throughput of your model. You are charged for the number of inference units that you use. </p>
            max_inference_units: <p>The maximum number of inference units to use for auto-scaling the model. If you don't specify a value, Amazon Rekognition Custom Labels doesn't auto-scale the model.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To start an Amazon Rekognition Custom Labels model
            Starts a version of an Amazon Rekognition Custom Labels model.

            >>> client.start_project_version(project_version_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-project/version/1/1690556751958', min_inference_units=1, max_inference_units=1)
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_project_version_request.StartProjectVersionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_project_version_response.StartProjectVersionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_project_version

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_project_version.start_project_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_project_version_request.StartProjectVersionRequest = {
            "project_version_arn": project_version_arn,
            "min_inference_units": min_inference_units,
        }
        if max_inference_units is not None:
            input_["max_inference_units"] = max_inference_units

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_segment_detection(
        self,
        video: "capo_rekognition.types.video.Video",
        segment_types: "capo_rekognition.types.segment_types.SegmentTypes",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
        notification_channel: Optional[
            "capo_rekognition.types.notification_channel.NotificationChannel"
        ] = None,
        job_tag: Optional["capo_rekognition.types.job_tag.JobTag"] = None,
        filters: Optional[
            "capo_rekognition.types.start_segment_detection_filters.StartSegmentDetectionFilters"
        ] = None,
    ) -> "capo_rekognition.types.start_segment_detection_response.StartSegmentDetectionResponse":
        """<p>Starts asynchronous detection of segment detection in a stored video.</p> <p>Amazon Rekognition Video can detect segments in a video stored in an Amazon S3 bucket. Use <a>Video</a> to specify the bucket name and the filename of the video. <code>StartSegmentDetection</code> returns a job identifier (<code>JobId</code>) which you use to get the results of the operation. When segment detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in <code>NotificationChannel</code>.</p> <p>You can use the <code>Filters</code> (<a>StartSegmentDetectionFilters</a>) input parameter to specify the minimum detection confidence returned in the response. Within <code>Filters</code>, use <code>ShotFilter</code> (<a>StartShotDetectionFilter</a>) to filter detected shots. Use <code>TechnicalCueFilter</code> (<a>StartTechnicalCueDetectionFilter</a>) to filter technical cues. </p> <p>To get the results of the segment detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. if so, call <a>GetSegmentDetection</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartSegmentDetection</code>. </p> <p>For more information, see Detecting video segments in stored video in the Amazon Rekognition Developer Guide.</p>

        Args:
            client_request_token: <p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartSegmentDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>
            notification_channel: <p>The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the segment detection operation. Note that the Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy to access the topic.</p>
            job_tag: <p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>
            filters: <p>Filters for technical cue or shot detection.</p>
            segment_types: <p>An array of segment types to detect in the video. Valid values are TECHNICAL_CUE and SHOT.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.video_too_large_exception.VideoTooLargeException: <p>The file size or duration of the supplied media is too large. The maximum file size is 10GB. The maximum duration is 6 hours. </p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_segment_detection_request.StartSegmentDetectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_segment_detection_response.StartSegmentDetectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_segment_detection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_segment_detection.start_segment_detection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_segment_detection_request.StartSegmentDetectionRequest = {
            "video": video,
            "segment_types": segment_types,
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_stream_processor(
        self,
        name: "capo_rekognition.types.stream_processor_name.StreamProcessorName",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        start_selector: Optional[
            "capo_rekognition.types.stream_processing_start_selector.StreamProcessingStartSelector"
        ] = None,
        stop_selector: Optional[
            "capo_rekognition.types.stream_processing_stop_selector.StreamProcessingStopSelector"
        ] = None,
    ) -> "capo_rekognition.types.start_stream_processor_response.StartStreamProcessorResponse":
        """<important> <p>Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html">Rekognition feature availability changes</a>.</p> <p> <b>This change does not impact the availability of other Amazon Rekognition features.</b> </p> </important> <p>Starts processing a stream processor. You create a stream processor by calling <a>CreateStreamProcessor</a>. To tell <code>StartStreamProcessor</code> which stream processor to start, use the value of the <code>Name</code> field specified in the call to <code>CreateStreamProcessor</code>.</p> <p>If you are using a label detection stream processor to detect labels, you need to provide a <code>Start selector</code> and a <code>Stop selector</code> to determine the length of the stream processing time.</p>

        Args:
            name: <p>The name of the stream processor to start processing.</p>
            start_selector: <p> Specifies the starting point in the Kinesis stream to start processing. You can use the producer timestamp or the fragment number. If you use the producer timestamp, you must put the time in milliseconds. For more information about fragment numbers, see <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_Fragment.html">Fragment</a>. </p> <p>This is a required parameter for label detection stream processors and should not be used to start a face search stream processor.</p>
            stop_selector: <p> Specifies when to stop processing the stream. You can specify a maximum amount of time to process the video. </p> <p>This is a required parameter for label detection stream processors and should not be used to start a face search stream processor.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_stream_processor_request.StartStreamProcessorRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_stream_processor_response.StartStreamProcessorResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_stream_processor

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_stream_processor.start_stream_processor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_stream_processor_request.StartStreamProcessorRequest = {
            "name": name
        }
        if start_selector is not None:
            input_["start_selector"] = start_selector
        if stop_selector is not None:
            input_["stop_selector"] = stop_selector

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_text_detection(
        self,
        video: "capo_rekognition.types.video.Video",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        client_request_token: Optional[
            "capo_rekognition.types.client_request_token.ClientRequestToken"
        ] = None,
        notification_channel: Optional[
            "capo_rekognition.types.notification_channel.NotificationChannel"
        ] = None,
        job_tag: Optional["capo_rekognition.types.job_tag.JobTag"] = None,
        filters: Optional[
            "capo_rekognition.types.start_text_detection_filters.StartTextDetectionFilters"
        ] = None,
    ) -> "capo_rekognition.types.start_text_detection_response.StartTextDetectionResponse":
        """<p>Starts asynchronous detection of text in a stored video.</p> <p>Amazon Rekognition Video can detect text in a video stored in an Amazon S3 bucket. Use <a>Video</a> to specify the bucket name and the filename of the video. <code>StartTextDetection</code> returns a job identifier (<code>JobId</code>) which you use to get the results of the operation. When text detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in <code>NotificationChannel</code>.</p> <p>To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. if so, call <a>GetTextDetection</a> and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartTextDetection</code>. </p>

        Args:
            client_request_token: <p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartTextDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentaly started more than once.</p>
            job_tag: <p>An identifier returned in the completion status published by your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>
            filters: <p>Optional parameters that let you set criteria the text must meet to be included in your response.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A <code>ClientRequestToken</code> input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException: <p>Amazon Rekognition is unable to access the S3 object specified in the request.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.video_too_large_exception.VideoTooLargeException: <p>The file size or duration of the supplied media is too large. The maximum file size is 10GB. The maximum duration is 6 hours. </p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.start_text_detection_request.StartTextDetectionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.start_text_detection_response.StartTextDetectionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.start_text_detection

            output, http_response = (
                capo_rekognition._operations.rekognition_service.start_text_detection.start_text_detection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.start_text_detection_request.StartTextDetectionRequest = {
            "video": video
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_project_version(
        self,
        project_version_arn: "capo_rekognition.types.project_version_arn.ProjectVersionArn",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.stop_project_version_response.StopProjectVersionResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Stops a running model. The operation might take a while to complete. To check the current status, call <a>DescribeProjectVersions</a>. Only applies to Custom Labels projects.</p> <p>This operation requires permissions to perform the <code>rekognition:StopProjectVersion</code> action.</p>

        Args:
            project_version_arn: <p>The Amazon Resource Name (ARN) of the model version that you want to stop.</p> <p>This operation requires permissions to perform the <code>rekognition:StopProjectVersion</code> action.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To stop an Amazon Rekognition Custom Labels model.
            Stops a version of an Amazon Rekognition Custom Labels model.

            >>> client.stop_project_version(project_version_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-project/version/1/1690556751958')
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.stop_project_version_request.StopProjectVersionRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.stop_project_version_response.StopProjectVersionResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.stop_project_version

            output, http_response = (
                capo_rekognition._operations.rekognition_service.stop_project_version.stop_project_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.stop_project_version_request.StopProjectVersionRequest = {
            "project_version_arn": project_version_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_stream_processor(
        self,
        name: "capo_rekognition.types.stream_processor_name.StreamProcessorName",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.stop_stream_processor_response.StopStreamProcessorResponse":
        """<important> <p>Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html">Rekognition feature availability changes</a>.</p> <p> <b>This change does not impact the availability of other Amazon Rekognition features.</b> </p> </important> <p>Stops a running stream processor that was created by <a>CreateStreamProcessor</a>.</p>

        Args:
            name: <p>The name of a stream processor created by <a>CreateStreamProcessor</a>.</p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.stop_stream_processor_request.StopStreamProcessorRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.stop_stream_processor_response.StopStreamProcessorResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.stop_stream_processor

            output, http_response = (
                capo_rekognition._operations.rekognition_service.stop_stream_processor.stop_stream_processor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.stop_stream_processor_request.StopStreamProcessorRequest = {
            "name": name
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
        resource_arn: "capo_rekognition.types.resource_arn.ResourceArn",
        tags: "capo_rekognition.types.tag_map.TagMap",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.tag_resource_response.TagResourceResponse":
        """<p> Adds one or more key-value tags to an Amazon Rekognition collection, stream processor, or Custom Labels model. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging AWS Resources</a>. </p> <p>This operation requires permissions to perform the <code>rekognition:TagResource</code> action. </p>

        Args:
            resource_arn: <p> Amazon Resource Name (ARN) of the model, collection, or stream processor that you want to assign the tags to. </p>
            tags: <p> The key-value tags to assign to the resource. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p></p> <p>The size of the collection exceeds the allowed limit. For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer Guide. </p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.tag_resource

            output, http_response = (
                capo_rekognition._operations.rekognition_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_rekognition.types.resource_arn.ResourceArn",
        tag_keys: "capo_rekognition.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes one or more tags from an Amazon Rekognition collection, stream processor, or Custom Labels model. </p> <p>This operation requires permissions to perform the <code>rekognition:UntagResource</code> action. </p>

        Args:
            resource_arn: <p> Amazon Resource Name (ARN) of the model, collection, or stream processor that you want to remove the tags from. </p>
            tag_keys: <p> A list of the tags that you want to remove. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.untag_resource

            output, http_response = (
                capo_rekognition._operations.rekognition_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.untag_resource_request.UntagResourceRequest = {
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

    def update_dataset_entries(
        self,
        dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn",
        changes: "capo_rekognition.types.dataset_changes.DatasetChanges",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
    ) -> "capo_rekognition.types.update_dataset_entries_response.UpdateDatasetEntriesResponse":
        """<note> <p>This operation applies only to Amazon Rekognition Custom Labels.</p> </note> <p>Adds or updates one or more entries (images) in a dataset. An entry is a JSON Line which contains the information for a single image, including the image location, assigned labels, and object location bounding boxes. For more information, see Image-Level labels in manifest files and Object localization in manifest files in the <i>Amazon Rekognition Custom Labels Developer Guide</i>. </p> <p>If the <code>source-ref</code> field in the JSON line references an existing image, the existing image in the dataset is updated. If <code>source-ref</code> field doesn't reference an existing image, the image is added as a new image to the dataset. </p> <p>You specify the changes that you want to make in the <code>Changes</code> input parameter. There isn't a limit to the number JSON Lines that you can change, but the size of <code>Changes</code> must be less than 5MB.</p> <p> <code>UpdateDatasetEntries</code> returns immediatly, but the dataset update might take a while to complete. Use <a>DescribeDataset</a> to check the current status. The dataset updated successfully if the value of <code>Status</code> is <code>UPDATE_COMPLETE</code>. </p> <p>To check if any non-terminal errors occured, call <a>ListDatasetEntries</a> and check for the presence of <code>errors</code> lists in the JSON Lines.</p> <p>Dataset update fails if a terminal error occurs (<code>Status</code> = <code>UPDATE_FAILED</code>). Currently, you can't access the terminal error information from the Amazon Rekognition Custom Labels SDK. </p> <p>This operation requires permissions to perform the <code>rekognition:UpdateDatasetEntries</code> action.</p>

        Args:
            dataset_arn: <p> The Amazon Resource Name (ARN) of the dataset that you want to update. </p>
            changes: <p> The changes that you want to make to the dataset. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: <code>StartLabelDetection</code>) will raise a <code>LimitExceededException</code> exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit. </p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To-add dataset entries to an Amazon Rekognition Custom Labels dataset
            Adds dataset entries to an Amazon Rekognition Custom Labels dataset.

            >>> client.update_dataset_entries(dataset_arn='arn:aws:rekognition:us-east-1:111122223333:project/my-proj-2/dataset/train/1690564858106', changes={'GroundTruth': '{"source-ref":"s3://custom-labels-console-us-east-1-111111111/assets/flowers_1_test_dataset/mediterranean_spurge4.jpg","mediterranean_spurge":1,"mediterranean_spurge-metadata":{"confidence":1,"job-name":"labeling-job/mediterranean_spurge","class-name":"mediterranean_spurge","human-annotated":"yes","creation-date":"2021-07-11T03:33:42.025Z","type":"groundtruth/image-classification"},"with_leaves":1,"with_leaves-metadata":{"confidence":1,"job-name":"labeling-job/with_leaves","class-name":"with_leaves","human-annotated":"yes","creation-date":"2021-07-11T03:33:42.025Z","type":"groundtruth/image-classification"}}'})
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.update_dataset_entries_request.UpdateDatasetEntriesRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.update_dataset_entries_response.UpdateDatasetEntriesResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.update_dataset_entries

            output, http_response = (
                capo_rekognition._operations.rekognition_service.update_dataset_entries.update_dataset_entries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.update_dataset_entries_request.UpdateDatasetEntriesRequest = {
            "dataset_arn": dataset_arn,
            "changes": changes,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_stream_processor(
        self,
        name: "capo_rekognition.types.stream_processor_name.StreamProcessorName",
        *,
        config_overrides: Optional[RekognitionClientConfig] = None,
        settings_for_update: Optional[
            "capo_rekognition.types.stream_processor_settings_for_update.StreamProcessorSettingsForUpdate"
        ] = None,
        regions_of_interest_for_update: Optional[
            "capo_rekognition.types.regions_of_interest.RegionsOfInterest"
        ] = None,
        data_sharing_preference_for_update: Optional[
            "capo_rekognition.types.stream_processor_data_sharing_preference.StreamProcessorDataSharingPreference"
        ] = None,
        parameters_to_delete: Optional[
            "capo_rekognition.types.stream_processor_parameters_to_delete.StreamProcessorParametersToDelete"
        ] = None,
    ) -> "capo_rekognition.types.update_stream_processor_response.UpdateStreamProcessorResponse":
        """<important> <p>Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html">Rekognition feature availability changes</a>.</p> <p> <b>This change does not impact the availability of other Amazon Rekognition features.</b> </p> </important> <p> Allows you to update a stream processor. You can change some settings and regions of interest and delete certain parameters. </p>

        Args:
            name: <p> Name of the stream processor that you want to update. </p>
            settings_for_update: <p> The stream processor settings that you want to update. Label detection settings can be updated to detect different labels with a different minimum confidence. </p>
            regions_of_interest_for_update: <p> Specifies locations in the frames where Amazon Rekognition checks for objects or people. This is an optional parameter for label detection stream processors. </p>
            data_sharing_preference_for_update: <p> Shows whether you are sharing data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams. </p>
            parameters_to_delete: <p> A list of parameters you want to delete from the stream processor. </p>

        Raises:
            capo_rekognition.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to perform the action.</p>
            capo_rekognition.errors.internal_server_error.InternalServerError: <p>Amazon Rekognition experienced a service issue. Try your call again.</p>
            capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException: <p>Input parameter violated a constraint. Validate your parameter before calling the API operation again.</p>
            capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.</p>
            capo_rekognition.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is already being used.</p>
            capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request cannot be found.</p>
            capo_rekognition.errors.throttling_exception.ThrottlingException: <p>Amazon Rekognition is temporarily unable to process the request. Try your call again.</p>
            capo_rekognition.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rekognition.types.update_stream_processor_request.UpdateStreamProcessorRequest]",
        ) -> OperationResponse[
            "capo_rekognition.types.update_stream_processor_response.UpdateStreamProcessorResponse"
        ]:
            import capo_rekognition._operations.rekognition_service.update_stream_processor

            output, http_response = (
                capo_rekognition._operations.rekognition_service.update_stream_processor.update_stream_processor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rekognition.types.update_stream_processor_request.UpdateStreamProcessorRequest = {
            "name": name
        }
        if settings_for_update is not None:
            input_["settings_for_update"] = settings_for_update
        if regions_of_interest_for_update is not None:
            input_["regions_of_interest_for_update"] = regions_of_interest_for_update
        if data_sharing_preference_for_update is not None:
            input_["data_sharing_preference_for_update"] = (
                data_sharing_preference_for_update
            )
        if parameters_to_delete is not None:
            input_["parameters_to_delete"] = parameters_to_delete

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
