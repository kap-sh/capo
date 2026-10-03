"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateFunctionEventInvokeConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.destination_config
    import capo_lambda.types.maximum_event_age_in_seconds
    import capo_lambda.types.maximum_retry_attempts
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.numeric_latest_published_or_alias_qualifier


class UpdateFunctionEventInvokeConfigRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function, version, or alias.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    qualifier: NotRequired[
        "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
    ]
    """<p>A version number or alias name.</p>"""
    maximum_retry_attempts: NotRequired[
        "capo_lambda.types.maximum_retry_attempts.MaximumRetryAttempts"
    ]
    """<p>The maximum number of times to retry when the function returns an error.</p>"""
    maximum_event_age_in_seconds: NotRequired[
        "capo_lambda.types.maximum_event_age_in_seconds.MaximumEventAgeInSeconds"
    ]
    """<p>The maximum age of a request that Lambda sends to a function for processing.</p>"""
    destination_config: NotRequired[
        "capo_lambda.types.destination_config.DestinationConfig"
    ]
    """<p>A destination for events after they have been sent to a function for processing.</p> <p class="title"> <b>Destinations</b> </p> <ul> <li> <p> <b>Function</b> - The Amazon Resource Name (ARN) of a Lambda function.</p> </li> <li> <p> <b>Queue</b> - The ARN of a standard SQS queue.</p> </li> <li> <p> <b>Bucket</b> - The ARN of an Amazon S3 bucket.</p> </li> <li> <p> <b>Topic</b> - The ARN of a standard SNS topic.</p> </li> <li> <p> <b>Event Bus</b> - The ARN of an Amazon EventBridge event bus.</p> </li> </ul> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFunctionEventInvokeConfigRequest) -> dict:
    out: dict = {}
    if "maximum_retry_attempts" in value:
        out["MaximumRetryAttempts"] = value["maximum_retry_attempts"]
    if "maximum_event_age_in_seconds" in value:
        out["MaximumEventAgeInSeconds"] = value["maximum_event_age_in_seconds"]
    if "destination_config" in value:
        import capo_lambda.types.destination_config

        out["DestinationConfig"] = capo_lambda.types.destination_config.serialize_json(
            value["destination_config"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFunctionEventInvokeConfigRequest:
    out: UpdateFunctionEventInvokeConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaximumRetryAttempts") is not None:
        out["maximum_retry_attempts"] = data["MaximumRetryAttempts"]
    if data.get("MaximumEventAgeInSeconds") is not None:
        out["maximum_event_age_in_seconds"] = data["MaximumEventAgeInSeconds"]
    if data.get("DestinationConfig") is not None:
        import capo_lambda.types.destination_config

        out["destination_config"] = (
            capo_lambda.types.destination_config.deserialize_json(
                data["DestinationConfig"]
            )
        )
    return out
