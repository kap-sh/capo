"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#AmazonPersonalizeRuntime``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_personalize_runtime._auth._signers
import capo_personalize_runtime._auth._sigv4
from capo_personalize_runtime._auth._identity import Credentials
from capo_personalize_runtime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_personalize_runtime._auth._zapros_handler import AuthMiddleware
from capo_personalize_runtime._services._aws_config import aws_config
from capo_personalize_runtime._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_personalize_runtime.types.arn
    import capo_personalize_runtime.types.context
    import capo_personalize_runtime.types.filter_values
    import capo_personalize_runtime.types.get_action_recommendations_request
    import capo_personalize_runtime.types.get_action_recommendations_response
    import capo_personalize_runtime.types.get_personalized_ranking_request
    import capo_personalize_runtime.types.get_personalized_ranking_response
    import capo_personalize_runtime.types.get_recommendations_request
    import capo_personalize_runtime.types.get_recommendations_response
    import capo_personalize_runtime.types.input_list
    import capo_personalize_runtime.types.item_id
    import capo_personalize_runtime.types.metadata_columns
    import capo_personalize_runtime.types.num_results
    import capo_personalize_runtime.types.promotion_list
    import capo_personalize_runtime.types.user_id


class PersonalizeRuntimeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class PersonalizeRuntimeClient:
    """A client for the ``PersonalizeRuntime`` service.

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
        self._config = PersonalizeRuntimeClientConfig(
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
        self, config_overrides: Optional[PersonalizeRuntimeClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PersonalizeRuntimeClientConfig = config_overrides or {}
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

    def get_action_recommendations(
        self,
        *,
        config_overrides: Optional[PersonalizeRuntimeClientConfig] = None,
        campaign_arn: Optional["capo_personalize_runtime.types.arn.Arn"] = None,
        user_id: Optional["capo_personalize_runtime.types.user_id.UserID"] = None,
        num_results: Optional[
            "capo_personalize_runtime.types.num_results.NumResults"
        ] = None,
        filter_arn: Optional["capo_personalize_runtime.types.arn.Arn"] = None,
        filter_values: Optional[
            "capo_personalize_runtime.types.filter_values.FilterValues"
        ] = None,
    ) -> "capo_personalize_runtime.types.get_action_recommendations_response.GetActionRecommendationsResponse":
        """<p>Returns a list of recommended actions in sorted in descending order by prediction score. Use the <code>GetActionRecommendations</code> API if you have a custom campaign that deploys a solution version trained with a PERSONALIZED_ACTIONS recipe. </p> <p>For more information about PERSONALIZED_ACTIONS recipes, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/nexts-best-action-recipes.html">PERSONALIZED_ACTIONS recipes</a>. For more information about getting action recommendations, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/get-action-recommendations.html">Getting action recommendations</a>.</p>

        Args:
            campaign_arn: <p>The Amazon Resource Name (ARN) of the campaign to use for getting action recommendations. This campaign must deploy a solution version trained with a PERSONALIZED_ACTIONS recipe.</p>
            user_id: <p>The user ID of the user to provide action recommendations for.</p>
            num_results: <p>The number of results to return. The default is 5. The maximum is 100.</p>
            filter_arn: <p>The ARN of the filter to apply to the returned recommendations. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering Recommendations</a>.</p> <p>When using this parameter, be sure the filter resource is <code>ACTIVE</code>.</p>
            filter_values: <p>The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma. </p> <p>For filter expressions that use an <code>INCLUDE</code> element to include actions, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an <code>EXCLUDE</code> element to exclude actions, you can omit the <code>filter-values</code>. In this case, Amazon Personalize doesn't use that portion of the expression to filter recommendations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering recommendations and user segments</a>.</p>

        Raises:
            capo_personalize_runtime.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_personalize_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_personalize_runtime.types.get_action_recommendations_request.GetActionRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_personalize_runtime.types.get_action_recommendations_response.GetActionRecommendationsResponse"
        ]:
            import capo_personalize_runtime._operations.amazon_personalize_runtime.get_action_recommendations

            output, http_response = (
                capo_personalize_runtime._operations.amazon_personalize_runtime.get_action_recommendations.get_action_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize_runtime.types.get_action_recommendations_request.GetActionRecommendationsRequest = {}
        if campaign_arn is not None:
            input_["campaign_arn"] = campaign_arn
        if user_id is not None:
            input_["user_id"] = user_id
        if num_results is not None:
            input_["num_results"] = num_results
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
        if filter_values is not None:
            input_["filter_values"] = filter_values

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_personalized_ranking(
        self,
        campaign_arn: "capo_personalize_runtime.types.arn.Arn",
        input_list: "capo_personalize_runtime.types.input_list.InputList",
        user_id: "capo_personalize_runtime.types.user_id.UserID",
        *,
        config_overrides: Optional[PersonalizeRuntimeClientConfig] = None,
        context: Optional["capo_personalize_runtime.types.context.Context"] = None,
        filter_arn: Optional["capo_personalize_runtime.types.arn.Arn"] = None,
        filter_values: Optional[
            "capo_personalize_runtime.types.filter_values.FilterValues"
        ] = None,
        metadata_columns: Optional[
            "capo_personalize_runtime.types.metadata_columns.MetadataColumns"
        ] = None,
    ) -> "capo_personalize_runtime.types.get_personalized_ranking_response.GetPersonalizedRankingResponse":
        """<p>Re-ranks a list of recommended items for the given user. The first item in the list is deemed the most likely item to be of interest to the user.</p> <note> <p>The solution backing the campaign must have been created using a recipe of type PERSONALIZED_RANKING.</p> </note>

        Args:
            campaign_arn: <p>The Amazon Resource Name (ARN) of the campaign to use for generating the personalized ranking.</p>
            input_list: <p>A list of items (by <code>itemId</code>) to rank. If an item was not included in the training dataset, the item is appended to the end of the reranked list. If you are including metadata in recommendations, the maximum is 50. Otherwise, the maximum is 500.</p>
            user_id: <p>The user for which you want the campaign to provide a personalized ranking.</p>
            context: <p>The contextual metadata to use when getting recommendations. Contextual metadata includes any interaction information that might be relevant when getting a user's recommendations, such as the user's current location or device type.</p>
            filter_arn: <p>The Amazon Resource Name (ARN) of a filter you created to include items or exclude items from recommendations for a given user. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering Recommendations</a>.</p>
            filter_values: <p>The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma. </p> <p>For filter expressions that use an <code>INCLUDE</code> element to include items, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an <code>EXCLUDE</code> element to exclude items, you can omit the <code>filter-values</code>.In this case, Amazon Personalize doesn't use that portion of the expression to filter recommendations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering Recommendations</a>.</p>
            metadata_columns: <p>If you enabled metadata in recommendations when you created or updated the campaign, specify metadata columns from your Items dataset to include in the personalized ranking. The map key is <code>ITEMS</code> and the value is a list of column names from your Items dataset. The maximum number of columns you can provide is 10.</p> <p> For information about enabling metadata for a campaign, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata">Enabling metadata in recommendations for a campaign</a>. </p>

        Raises:
            capo_personalize_runtime.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_personalize_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_personalize_runtime.types.get_personalized_ranking_request.GetPersonalizedRankingRequest]",
        ) -> OperationResponse[
            "capo_personalize_runtime.types.get_personalized_ranking_response.GetPersonalizedRankingResponse"
        ]:
            import capo_personalize_runtime._operations.amazon_personalize_runtime.get_personalized_ranking

            output, http_response = (
                capo_personalize_runtime._operations.amazon_personalize_runtime.get_personalized_ranking.get_personalized_ranking(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize_runtime.types.get_personalized_ranking_request.GetPersonalizedRankingRequest = {
            "campaign_arn": campaign_arn,
            "input_list": input_list,
            "user_id": user_id,
        }
        if context is not None:
            input_["context"] = context
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
        if filter_values is not None:
            input_["filter_values"] = filter_values
        if metadata_columns is not None:
            input_["metadata_columns"] = metadata_columns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recommendations(
        self,
        *,
        config_overrides: Optional[PersonalizeRuntimeClientConfig] = None,
        campaign_arn: Optional["capo_personalize_runtime.types.arn.Arn"] = None,
        item_id: Optional["capo_personalize_runtime.types.item_id.ItemID"] = None,
        user_id: Optional["capo_personalize_runtime.types.user_id.UserID"] = None,
        num_results: Optional[
            "capo_personalize_runtime.types.num_results.NumResults"
        ] = None,
        context: Optional["capo_personalize_runtime.types.context.Context"] = None,
        filter_arn: Optional["capo_personalize_runtime.types.arn.Arn"] = None,
        filter_values: Optional[
            "capo_personalize_runtime.types.filter_values.FilterValues"
        ] = None,
        recommender_arn: Optional["capo_personalize_runtime.types.arn.Arn"] = None,
        promotions: Optional[
            "capo_personalize_runtime.types.promotion_list.PromotionList"
        ] = None,
        metadata_columns: Optional[
            "capo_personalize_runtime.types.metadata_columns.MetadataColumns"
        ] = None,
    ) -> "capo_personalize_runtime.types.get_recommendations_response.GetRecommendationsResponse":
        """<p>Returns a list of recommended items. For campaigns, the campaign's Amazon Resource Name (ARN) is required and the required user and item input depends on the recipe type used to create the solution backing the campaign as follows:</p> <ul> <li> <p>USER_PERSONALIZATION - <code>userId</code> required, <code>itemId</code> not used</p> </li> <li> <p>RELATED_ITEMS - <code>itemId</code> required, <code>userId</code> not used</p> </li> </ul> <note> <p>Campaigns that are backed by a solution created using a recipe of type PERSONALIZED_RANKING use the API.</p> </note> <p> For recommenders, the recommender's ARN is required and the required item and user input depends on the use case (domain-based recipe) backing the recommender. For information on use case requirements see <a href="https://docs.aws.amazon.com/personalize/latest/dg/domain-use-cases.html">Choosing recommender use cases</a>. </p>

        Args:
            campaign_arn: <p>The Amazon Resource Name (ARN) of the campaign to use for getting recommendations.</p>
            item_id: <p>The item ID to provide recommendations for.</p> <p>Required for <code>RELATED_ITEMS</code> recipe type.</p>
            user_id: <p>The user ID to provide recommendations for.</p> <p>Required for <code>USER_PERSONALIZATION</code> recipe type.</p>
            num_results: <p>The number of results to return. The default is 25. If you are including metadata in recommendations, the maximum is 50. Otherwise, the maximum is 500.</p>
            context: <p>The contextual metadata to use when getting recommendations. Contextual metadata includes any interaction information that might be relevant when getting a user's recommendations, such as the user's current location or device type.</p>
            filter_arn: <p>The ARN of the filter to apply to the returned recommendations. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering Recommendations</a>.</p> <p>When using this parameter, be sure the filter resource is <code>ACTIVE</code>.</p>
            filter_values: <p>The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma. </p> <p>For filter expressions that use an <code>INCLUDE</code> element to include items, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an <code>EXCLUDE</code> element to exclude items, you can omit the <code>filter-values</code>.In this case, Amazon Personalize doesn't use that portion of the expression to filter recommendations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering recommendations and user segments</a>.</p>
            recommender_arn: <p>The Amazon Resource Name (ARN) of the recommender to use to get recommendations. Provide a recommender ARN if you created a Domain dataset group with a recommender for a domain use case.</p>
            promotions: <p>The promotions to apply to the recommendation request. A promotion defines additional business rules that apply to a configurable subset of recommended items.</p>
            metadata_columns: <p>If you enabled metadata in recommendations when you created or updated the campaign or recommender, specify the metadata columns from your Items dataset to include in item recommendations. The map key is <code>ITEMS</code> and the value is a list of column names from your Items dataset. The maximum number of columns you can provide is 10.</p> <p> For information about enabling metadata for a campaign, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata">Enabling metadata in recommendations for a campaign</a>. For information about enabling metadata for a recommender, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/creating-recommenders.html#create-recommender-return-metadata">Enabling metadata in recommendations for a recommender</a>. </p>

        Raises:
            capo_personalize_runtime.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_personalize_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_personalize_runtime.types.get_recommendations_request.GetRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_personalize_runtime.types.get_recommendations_response.GetRecommendationsResponse"
        ]:
            import capo_personalize_runtime._operations.amazon_personalize_runtime.get_recommendations

            output, http_response = (
                capo_personalize_runtime._operations.amazon_personalize_runtime.get_recommendations.get_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize_runtime.types.get_recommendations_request.GetRecommendationsRequest = {}
        if campaign_arn is not None:
            input_["campaign_arn"] = campaign_arn
        if item_id is not None:
            input_["item_id"] = item_id
        if user_id is not None:
            input_["user_id"] = user_id
        if num_results is not None:
            input_["num_results"] = num_results
        if context is not None:
            input_["context"] = context
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
        if filter_values is not None:
            input_["filter_values"] = filter_values
        if recommender_arn is not None:
            input_["recommender_arn"] = recommender_arn
        if promotions is not None:
            input_["promotions"] = promotions
        if metadata_columns is not None:
            input_["metadata_columns"] = metadata_columns

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
