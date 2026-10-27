from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_elementalinference._auth._signers
import capo_elementalinference._auth._sigv4
from capo_elementalinference._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_elementalinference.types.associate_feed_request
    import capo_elementalinference.types.associate_feed_response
    import capo_elementalinference.types.associated_resource_name
    import capo_elementalinference.types.create_feed_request
    import capo_elementalinference.types.create_feed_response
    import capo_elementalinference.types.create_output_list
    import capo_elementalinference.types.create_schedule_action_request
    import capo_elementalinference.types.create_schedule_action_response
    import capo_elementalinference.types.delete_feed_policy_request
    import capo_elementalinference.types.delete_feed_request
    import capo_elementalinference.types.delete_feed_response
    import capo_elementalinference.types.delete_schedule_action_request
    import capo_elementalinference.types.delete_schedule_action_response
    import capo_elementalinference.types.disassociate_feed_request
    import capo_elementalinference.types.disassociate_feed_response
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.feed_summary
    import capo_elementalinference.types.get_feed_policy_request
    import capo_elementalinference.types.get_feed_policy_response
    import capo_elementalinference.types.get_feed_request
    import capo_elementalinference.types.get_feed_response
    import capo_elementalinference.types.iam_role_arn
    import capo_elementalinference.types.list_feeds_request
    import capo_elementalinference.types.list_feeds_response
    import capo_elementalinference.types.list_schedule_actions_request
    import capo_elementalinference.types.list_schedule_actions_response
    import capo_elementalinference.types.policy_document
    import capo_elementalinference.types.put_feed_policy_request
    import capo_elementalinference.types.put_feed_policy_response
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.schedule_action
    import capo_elementalinference.types.schedule_action_operations
    import capo_elementalinference.types.schedule_action_start_configuration
    import capo_elementalinference.types.tag_map
    import capo_elementalinference.types.update_feed_request
    import capo_elementalinference.types.update_feed_response
    import capo_elementalinference.types.update_output_list
    from capo_elementalinference._services.async_elemental_inference import (
        AsyncElementalInferenceClient,
        AsyncElementalInferenceClientConfig,
    )
    from capo_elementalinference._services.elemental_inference import (
        ElementalInferenceClient,
        ElementalInferenceClientConfig,
    )


class FeedResource:
    def __init__(self, service: ElementalInferenceClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        outputs: "capo_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        access_role_arn: Optional[
            "capo_elementalinference.types.iam_role_arn.IamRoleArn"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "capo_elementalinference.types.create_feed_response.CreateFeedResponse":
        """<p>Creates a feed. The feed is the target for the live media stream that is being sent by the calling application. An example of a calling application is AWS Elemental MediaLive. </p> <p>The key contents of the feed is an array of outputs. Each output represents an Elemental Inference feature. After you create the feed, you must associate a resource with the feed. At that point, you will have a useable feed: resource - feed - output or outputs. </p>

        Args:
            name: <p>A user-friendly name for this feed.</p>
            access_role_arn: <p>The ARN of an IAM role that Elemental Inference assumes to access resources in your account on your behalf. For example, the smart crop feature uses this role to read graphics-compositing templates from your Amazon S3 bucket. You specify one access role for each feed. </p>
            outputs: <p>An array of outputs for this feed. Each output represents a specific Elemental Inference feature. For example, there is one output type for the smart crop feature. You must specify at least one output, but you can later add outputs using AssociateFeed, or add, modify, and delete outputs using UpdateFeed. </p>
            tags: <p>Optional tags. You can also add tags later, using TagResource.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_feed_request.CreateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_feed_response.CreateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_feed.create_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateFeed")
        )
        input_: capo_elementalinference.types.create_feed_request.CreateFeedRequest = {
            "name": name,
            "outputs": outputs,
        }
        if access_role_arn is not None:
            input_["access_role_arn"] = access_role_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_feed_response.GetFeedResponse":
        """<p>Retrieves information about the specified feed.</p>

        Args:
            id: <p>The ID of the feed to query.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_feed_request.GetFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_feed_response.GetFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_feed.get_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFeed")
        )
        input_: capo_elementalinference.types.get_feed_request.GetFeedRequest = {
            "id": id
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
        name: "capo_elementalinference.types.resource_name.ResourceName",
        id: "capo_elementalinference.types.feed_id.FeedId",
        outputs: "capo_elementalinference.types.update_output_list.UpdateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        access_role_arn: Optional[
            "capo_elementalinference.types.iam_role_arn.IamRoleArn"
        ] = None,
    ) -> "capo_elementalinference.types.update_feed_response.UpdateFeedResponse":
        """<p>Updates the name and/or outputs in a feed. </p> <p>UpdateFeed is a PUT operation, which means that the payload that you specify completely overwrites the existing payload. </p> <p>This means that if you want to touch the array of outputs, you must pass in the full new list. So you must omit outputs you want to delete, and include outputs you want to add or modify. </p> <p>If you want to patch the array of outputs to make selective additions, use AssociateFeed. </p>

        Args:
            name: <p>Required. You can specify the existing name (to leave it unchanged) or a new name. </p>
            access_role_arn: <p>The ARN of an IAM role that Elemental Inference assumes to access resources in your account on your behalf. You can specify the existing role (to leave it unchanged) or a new role. You specify one access role for each feed. </p>
            id: <p>The ID of the feed to update.</p>
            outputs: <p>Required. You can specify the existing array of outputs (to leave outputs unchanged) or you can specify a new array. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.update_feed_request.UpdateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.update_feed_response.UpdateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.update_feed.update_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateFeed")
        )
        input_: capo_elementalinference.types.update_feed_request.UpdateFeedRequest = {
            "name": name,
            "id": id,
            "outputs": outputs,
        }
        if access_role_arn is not None:
            input_["access_role_arn"] = access_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_feed_response.DeleteFeedResponse":
        """<p>Deletes the specified feed. You can delete the feed at any time. Elemental Inference doesn't block you from deleting a feed when the calling application is calling PutMedia or GetMetadata on that feed, although both these calls will start to fail. For more information about managing inactive feeds, see the Elemental Inference User Guide. </p>

        Args:
            id: <p>The ID of the feed.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_feed_request.DeleteFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_feed_response.DeleteFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_feed.delete_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFeed")
        )
        input_: capo_elementalinference.types.delete_feed_request.DeleteFeedRequest = {
            "id": id
        }

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
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_feeds_response.ListFeedsResponse":
        """<p>Displays a list of feeds that belong to this AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return per API request.</p> <p>For example, you submit a list request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 10 results per page. </p> <p>Valid Range: Minimum value of 1. Maximum value of 1000.</p>
            next_token: <p>The token that identifies the batch of results that you want to see.</p> <p>For example, you submit a ListFeeds request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFeeds request a second time and specify the NextToken value. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_feeds_request.ListFeedsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_feeds_response.ListFeedsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_feeds

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_feeds.list_feeds(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFeeds")
        )
        input_: capo_elementalinference.types.list_feeds_request.ListFeedsRequest = {}
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

    def associate_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "capo_elementalinference.types.associated_resource_name.AssociatedResourceName",
        outputs: "capo_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_elementalinference.types.associate_feed_response.AssociateFeedResponse":
        """<p>Associates a resource with the feed. The resource provides the input that Elemental Inference needs in order to perform an Elemental Inference feature, such as cropping video. You always provide the resource by associating it with a feed. You can associate only one resource with each feed. With an association, a specific source media is claiming ownership of the feed. </p> <p>AssociateFeed is a PATCH operation, which means that you can include only parameters that you want to change. Parameters that you don't include will not be affected by the operation. </p> <p>Specifically:</p> <ul> <li> <p>You can add more outputs to the existing outputs. New outputs will be appended.</p> </li> <li> <p>You can't modify an existing output (for example to change its name). Instead, use UpdateFeed. </p> </li> <li> <p>You can't delete an existing output. Instead, use UpdateFeed.</p> </li> </ul> <p>Also note that you can't change the feed name with AssociateFeed. Instead, use UpdateFeed. </p>

        Args:
            id: <p>The ID of the feed.</p>
            associated_resource_name: <p>An identifier for the resource. This name must not resemble an ARN.</p> <p>The resource is the source media that the feed will process. The name you assign should help you to later identify the source media that belongs to the feed. In this way, you will know which source media to push to the feed (using PutMedia). </p>
            outputs: <p>An array of one or more outputs that you want to add to this feed now, to supplement any outputs that you specified when you created or updated the feed. </p>
            dry_run: <p>Set to true if you want to do a dry run of the associate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions, quota limits exceeded, conflicting outputs, and so on. If the dry run fails, the action returns a 4xx error code. After you've fixed the errors, resubmit the request. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.associate_feed_request.AssociateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.associate_feed_response.AssociateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.associate_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.associate_feed.associate_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateFeed")
        )
        input_: capo_elementalinference.types.associate_feed_request.AssociateFeedRequest = {
            "id": id,
            "associated_resource_name": associated_resource_name,
            "outputs": outputs,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_schedule_action(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        action_name: "capo_elementalinference.types.resource_name.ResourceName",
        start_configuration: "capo_elementalinference.types.schedule_action_start_configuration.ScheduleActionStartConfiguration",
        operations: "capo_elementalinference.types.schedule_action_operations.ScheduleActionOperations",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.create_schedule_action_response.CreateScheduleActionResponse":
        """<p>Creates a schedule action on a feed. A schedule action applies configuration changes to the feed at a time that you specify, in the same way as an UpdateFeed request. </p> <p>Elemental Inference validates the targets of the action when you create it.</p>

        Args:
            id: <p>Specifies the ID of the feed that you want to add the schedule action to.</p>
            action_name: <p>A name for the schedule action. The name must be unique within the feed. You can reuse the name of an action that you deleted. </p>
            start_configuration: <p>Specifies when the action runs.</p>
            operations: <p>Specifies the list of configuration changes that you want to make to the feed. Elemental Inference applies all the operations in an action together, in the order that you specify them. If any operation fails, Elemental Inference doesn't apply any of them. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_schedule_action_request.CreateScheduleActionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_schedule_action_response.CreateScheduleActionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_schedule_action

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_schedule_action.create_schedule_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateScheduleAction")
        )
        input_: capo_elementalinference.types.create_schedule_action_request.CreateScheduleActionRequest = {
            "id": id,
            "action_name": action_name,
            "start_configuration": start_configuration,
            "operations": operations,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_feed_policy(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> None:
        """<p>Deletes the resource-based policy attached to the specified feed. After you delete the policy, the operation revokes the cross-account access that the policy granted. </p>

        Args:
            id: <p>The ID of the feed whose policy you want to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_feed_policy_request.DeleteFeedPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_elementalinference._operations.elemental_inference.delete_feed_policy

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_feed_policy.delete_feed_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFeedPolicy")
        )
        input_: capo_elementalinference.types.delete_feed_policy_request.DeleteFeedPolicyRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_schedule_action(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        action_name: "capo_elementalinference.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_schedule_action_response.DeleteScheduleActionResponse":
        """<p>Deletes a schedule action from a feed. A deleted action never runs.</p> <p>You can delete only an action whose status is PENDING. Deleting an action doesn't reverse changes that the action already made to the feed. When you delete or archive a feed, Elemental Inference deletes all the schedule actions on that feed. </p>

        Args:
            id: <p>The ID of the feed that holds the schedule action.</p>
            action_name: <p>The name of the schedule action that you want to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_schedule_action_request.DeleteScheduleActionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_schedule_action_response.DeleteScheduleActionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_schedule_action

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_schedule_action.delete_schedule_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteScheduleAction")
        )
        input_: capo_elementalinference.types.delete_schedule_action_request.DeleteScheduleActionRequest = {
            "id": id,
            "action_name": action_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "capo_elementalinference.types.associated_resource_name.AssociatedResourceName",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse":
        """<p>Releases the resource (the source media) that is associated with this feed. The outputs in the feed become DISABLED. </p>

        Args:
            id: <p>The ID of the feed where you want to release the resource.</p>
            associated_resource_name: <p>The name of the resource currently associated with the feed.</p>
            dry_run: <p>Set to true if you want to do a dry run of the disassociate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions. If the dry run fails, the action returns a 4xx error code. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.disassociate_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.disassociate_feed.disassociate_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateFeed")
        )
        input_: capo_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest = {
            "id": id,
            "associated_resource_name": associated_resource_name,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_feed_policy(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_feed_policy_response.GetFeedPolicyResponse":
        """<p>Retrieves the resource-based policy attached to the specified feed.</p>

        Args:
            id: <p>The ID of the feed whose policy you want to retrieve.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_feed_policy_request.GetFeedPolicyRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_feed_policy_response.GetFeedPolicyResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_feed_policy

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_feed_policy.get_feed_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFeedPolicy")
        )
        input_: capo_elementalinference.types.get_feed_policy_request.GetFeedPolicyRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_schedule_actions(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_schedule_actions_response.ListScheduleActionsResponse":
        """<p>Displays a list of the schedule actions on a feed, including the status of each action and, for a failed action, information about why it failed. </p> <p>Elemental Inference keeps an action whose status is COMPLETED or FAILED for about 48 hours after its scheduled time, and then deletes it automatically. </p>

        Args:
            id: <p>The ID of the feed that you want to query.</p>
            max_results: <p>The maximum number of results to return for each API request. If you don't specify MaxResults, Elemental Inference returns a maximum of 10 results for each page. </p>
            next_token: <p>The token that identifies the batch of results that you want to see. To see the next batch, submit the request a second time and specify the NextToken value that Elemental Inference returned. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_schedule_actions_request.ListScheduleActionsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_schedule_actions_response.ListScheduleActionsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_schedule_actions

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_schedule_actions.list_schedule_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListScheduleActions")
        )
        input_: capo_elementalinference.types.list_schedule_actions_request.ListScheduleActionsRequest = {
            "id": id
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

    def put_feed_policy(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        policy: "capo_elementalinference.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.put_feed_policy_response.PutFeedPolicyResponse":
        """<p>Attaches or replaces a resource-based policy on the specified feed. A resource-based policy grants cross-account access to the feed. </p>

        Args:
            id: <p>The ID of the feed to attach the policy to.</p>
            policy: <p>The resource-based policy document to attach to the feed.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.put_feed_policy_request.PutFeedPolicyRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.put_feed_policy_response.PutFeedPolicyResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.put_feed_policy

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.put_feed_policy.put_feed_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutFeedPolicy")
        )
        input_: capo_elementalinference.types.put_feed_policy_request.PutFeedPolicyRequest = {
            "id": id,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncFeedResource:
    def __init__(self, service: AsyncElementalInferenceClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        outputs: "capo_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        access_role_arn: Optional[
            "capo_elementalinference.types.iam_role_arn.IamRoleArn"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "capo_elementalinference.types.create_feed_response.CreateFeedResponse":
        """<p>Creates a feed. The feed is the target for the live media stream that is being sent by the calling application. An example of a calling application is AWS Elemental MediaLive. </p> <p>The key contents of the feed is an array of outputs. Each output represents an Elemental Inference feature. After you create the feed, you must associate a resource with the feed. At that point, you will have a useable feed: resource - feed - output or outputs. </p>

        Args:
            name: <p>A user-friendly name for this feed.</p>
            access_role_arn: <p>The ARN of an IAM role that Elemental Inference assumes to access resources in your account on your behalf. For example, the smart crop feature uses this role to read graphics-compositing templates from your Amazon S3 bucket. You specify one access role for each feed. </p>
            outputs: <p>An array of outputs for this feed. Each output represents a specific Elemental Inference feature. For example, there is one output type for the smart crop feature. You must specify at least one output, but you can later add outputs using AssociateFeed, or add, modify, and delete outputs using UpdateFeed. </p>
            tags: <p>Optional tags. You can also add tags later, using TagResource.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.create_feed_request.CreateFeedRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.create_feed_response.CreateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_feed

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.create_feed.async_create_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateFeed")
        )
        input_: capo_elementalinference.types.create_feed_request.CreateFeedRequest = {
            "name": name,
            "outputs": outputs,
        }
        if access_role_arn is not None:
            input_["access_role_arn"] = access_role_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_feed_response.GetFeedResponse":
        """<p>Retrieves information about the specified feed.</p>

        Args:
            id: <p>The ID of the feed to query.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.get_feed_request.GetFeedRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.get_feed_response.GetFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_feed

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.get_feed.async_get_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFeed")
        )
        input_: capo_elementalinference.types.get_feed_request.GetFeedRequest = {
            "id": id
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
        name: "capo_elementalinference.types.resource_name.ResourceName",
        id: "capo_elementalinference.types.feed_id.FeedId",
        outputs: "capo_elementalinference.types.update_output_list.UpdateOutputList",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        access_role_arn: Optional[
            "capo_elementalinference.types.iam_role_arn.IamRoleArn"
        ] = None,
    ) -> "capo_elementalinference.types.update_feed_response.UpdateFeedResponse":
        """<p>Updates the name and/or outputs in a feed. </p> <p>UpdateFeed is a PUT operation, which means that the payload that you specify completely overwrites the existing payload. </p> <p>This means that if you want to touch the array of outputs, you must pass in the full new list. So you must omit outputs you want to delete, and include outputs you want to add or modify. </p> <p>If you want to patch the array of outputs to make selective additions, use AssociateFeed. </p>

        Args:
            name: <p>Required. You can specify the existing name (to leave it unchanged) or a new name. </p>
            access_role_arn: <p>The ARN of an IAM role that Elemental Inference assumes to access resources in your account on your behalf. You can specify the existing role (to leave it unchanged) or a new role. You specify one access role for each feed. </p>
            id: <p>The ID of the feed to update.</p>
            outputs: <p>Required. You can specify the existing array of outputs (to leave outputs unchanged) or you can specify a new array. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.update_feed_request.UpdateFeedRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.update_feed_response.UpdateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_feed

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.update_feed.async_update_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateFeed")
        )
        input_: capo_elementalinference.types.update_feed_request.UpdateFeedRequest = {
            "name": name,
            "id": id,
            "outputs": outputs,
        }
        if access_role_arn is not None:
            input_["access_role_arn"] = access_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_feed_response.DeleteFeedResponse":
        """<p>Deletes the specified feed. You can delete the feed at any time. Elemental Inference doesn't block you from deleting a feed when the calling application is calling PutMedia or GetMetadata on that feed, although both these calls will start to fail. For more information about managing inactive feeds, see the Elemental Inference User Guide. </p>

        Args:
            id: <p>The ID of the feed.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.delete_feed_request.DeleteFeedRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.delete_feed_response.DeleteFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_feed

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.delete_feed.async_delete_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFeed")
        )
        input_: capo_elementalinference.types.delete_feed_request.DeleteFeedRequest = {
            "id": id
        }

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
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_feeds_response.ListFeedsResponse":
        """<p>Displays a list of feeds that belong to this AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return per API request.</p> <p>For example, you submit a list request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 10 results per page. </p> <p>Valid Range: Minimum value of 1. Maximum value of 1000.</p>
            next_token: <p>The token that identifies the batch of results that you want to see.</p> <p>For example, you submit a ListFeeds request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFeeds request a second time and specify the NextToken value. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.list_feeds_request.ListFeedsRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.list_feeds_response.ListFeedsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_feeds

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.list_feeds.async_list_feeds(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFeeds")
        )
        input_: capo_elementalinference.types.list_feeds_request.ListFeedsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "capo_elementalinference.types.associated_resource_name.AssociatedResourceName",
        outputs: "capo_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_elementalinference.types.associate_feed_response.AssociateFeedResponse":
        """<p>Associates a resource with the feed. The resource provides the input that Elemental Inference needs in order to perform an Elemental Inference feature, such as cropping video. You always provide the resource by associating it with a feed. You can associate only one resource with each feed. With an association, a specific source media is claiming ownership of the feed. </p> <p>AssociateFeed is a PATCH operation, which means that you can include only parameters that you want to change. Parameters that you don't include will not be affected by the operation. </p> <p>Specifically:</p> <ul> <li> <p>You can add more outputs to the existing outputs. New outputs will be appended.</p> </li> <li> <p>You can't modify an existing output (for example to change its name). Instead, use UpdateFeed. </p> </li> <li> <p>You can't delete an existing output. Instead, use UpdateFeed.</p> </li> </ul> <p>Also note that you can't change the feed name with AssociateFeed. Instead, use UpdateFeed. </p>

        Args:
            id: <p>The ID of the feed.</p>
            associated_resource_name: <p>An identifier for the resource. This name must not resemble an ARN.</p> <p>The resource is the source media that the feed will process. The name you assign should help you to later identify the source media that belongs to the feed. In this way, you will know which source media to push to the feed (using PutMedia). </p>
            outputs: <p>An array of one or more outputs that you want to add to this feed now, to supplement any outputs that you specified when you created or updated the feed. </p>
            dry_run: <p>Set to true if you want to do a dry run of the associate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions, quota limits exceeded, conflicting outputs, and so on. If the dry run fails, the action returns a 4xx error code. After you've fixed the errors, resubmit the request. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.associate_feed_request.AssociateFeedRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.associate_feed_response.AssociateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.associate_feed

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.associate_feed.async_associate_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateFeed")
        )
        input_: capo_elementalinference.types.associate_feed_request.AssociateFeedRequest = {
            "id": id,
            "associated_resource_name": associated_resource_name,
            "outputs": outputs,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_schedule_action(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        action_name: "capo_elementalinference.types.resource_name.ResourceName",
        start_configuration: "capo_elementalinference.types.schedule_action_start_configuration.ScheduleActionStartConfiguration",
        operations: "capo_elementalinference.types.schedule_action_operations.ScheduleActionOperations",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.create_schedule_action_response.CreateScheduleActionResponse":
        """<p>Creates a schedule action on a feed. A schedule action applies configuration changes to the feed at a time that you specify, in the same way as an UpdateFeed request. </p> <p>Elemental Inference validates the targets of the action when you create it.</p>

        Args:
            id: <p>Specifies the ID of the feed that you want to add the schedule action to.</p>
            action_name: <p>A name for the schedule action. The name must be unique within the feed. You can reuse the name of an action that you deleted. </p>
            start_configuration: <p>Specifies when the action runs.</p>
            operations: <p>Specifies the list of configuration changes that you want to make to the feed. Elemental Inference applies all the operations in an action together, in the order that you specify them. If any operation fails, Elemental Inference doesn't apply any of them. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.create_schedule_action_request.CreateScheduleActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.create_schedule_action_response.CreateScheduleActionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_schedule_action

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.create_schedule_action.async_create_schedule_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateScheduleAction")
        )
        input_: capo_elementalinference.types.create_schedule_action_request.CreateScheduleActionRequest = {
            "id": id,
            "action_name": action_name,
            "start_configuration": start_configuration,
            "operations": operations,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_feed_policy(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> None:
        """<p>Deletes the resource-based policy attached to the specified feed. After you delete the policy, the operation revokes the cross-account access that the policy granted. </p>

        Args:
            id: <p>The ID of the feed whose policy you want to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.delete_feed_policy_request.DeleteFeedPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_elementalinference._operations.elemental_inference.delete_feed_policy

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.delete_feed_policy.async_delete_feed_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFeedPolicy")
        )
        input_: capo_elementalinference.types.delete_feed_policy_request.DeleteFeedPolicyRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_schedule_action(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        action_name: "capo_elementalinference.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_schedule_action_response.DeleteScheduleActionResponse":
        """<p>Deletes a schedule action from a feed. A deleted action never runs.</p> <p>You can delete only an action whose status is PENDING. Deleting an action doesn't reverse changes that the action already made to the feed. When you delete or archive a feed, Elemental Inference deletes all the schedule actions on that feed. </p>

        Args:
            id: <p>The ID of the feed that holds the schedule action.</p>
            action_name: <p>The name of the schedule action that you want to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.delete_schedule_action_request.DeleteScheduleActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.delete_schedule_action_response.DeleteScheduleActionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_schedule_action

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.delete_schedule_action.async_delete_schedule_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteScheduleAction")
        )
        input_: capo_elementalinference.types.delete_schedule_action_request.DeleteScheduleActionRequest = {
            "id": id,
            "action_name": action_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "capo_elementalinference.types.associated_resource_name.AssociatedResourceName",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse":
        """<p>Releases the resource (the source media) that is associated with this feed. The outputs in the feed become DISABLED. </p>

        Args:
            id: <p>The ID of the feed where you want to release the resource.</p>
            associated_resource_name: <p>The name of the resource currently associated with the feed.</p>
            dry_run: <p>Set to true if you want to do a dry run of the disassociate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions. If the dry run fails, the action returns a 4xx error code. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.disassociate_feed

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.disassociate_feed.async_disassociate_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateFeed")
        )
        input_: capo_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest = {
            "id": id,
            "associated_resource_name": associated_resource_name,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_feed_policy(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_feed_policy_response.GetFeedPolicyResponse":
        """<p>Retrieves the resource-based policy attached to the specified feed.</p>

        Args:
            id: <p>The ID of the feed whose policy you want to retrieve.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.get_feed_policy_request.GetFeedPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.get_feed_policy_response.GetFeedPolicyResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_feed_policy

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.get_feed_policy.async_get_feed_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFeedPolicy")
        )
        input_: capo_elementalinference.types.get_feed_policy_request.GetFeedPolicyRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_schedule_actions(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_schedule_actions_response.ListScheduleActionsResponse":
        """<p>Displays a list of the schedule actions on a feed, including the status of each action and, for a failed action, information about why it failed. </p> <p>Elemental Inference keeps an action whose status is COMPLETED or FAILED for about 48 hours after its scheduled time, and then deletes it automatically. </p>

        Args:
            id: <p>The ID of the feed that you want to query.</p>
            max_results: <p>The maximum number of results to return for each API request. If you don't specify MaxResults, Elemental Inference returns a maximum of 10 results for each page. </p>
            next_token: <p>The token that identifies the batch of results that you want to see. To see the next batch, submit the request a second time and specify the NextToken value that Elemental Inference returned. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.list_schedule_actions_request.ListScheduleActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.list_schedule_actions_response.ListScheduleActionsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_schedule_actions

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.list_schedule_actions.async_list_schedule_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListScheduleActions")
        )
        input_: capo_elementalinference.types.list_schedule_actions_request.ListScheduleActionsRequest = {
            "id": id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_feed_policy(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        policy: "capo_elementalinference.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.put_feed_policy_response.PutFeedPolicyResponse":
        """<p>Attaches or replaces a resource-based policy on the specified feed. A resource-based policy grants cross-account access to the feed. </p>

        Args:
            id: <p>The ID of the feed to attach the policy to.</p>
            policy: <p>The resource-based policy document to attach to the feed.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.put_feed_policy_request.PutFeedPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.put_feed_policy_response.PutFeedPolicyResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.put_feed_policy

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.put_feed_policy.async_put_feed_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutFeedPolicy")
        )
        input_: capo_elementalinference.types.put_feed_policy_request.PutFeedPolicyRequest = {
            "id": id,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
