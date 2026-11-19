"""Generated from Smithy shape ``com.amazonaws.snowball#LambdaResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.event_trigger_definition_list
    import capo_snowball.types.resource_arn


class LambdaResource(TypedDict, closed=True):
    lambda_arn: NotRequired["capo_snowball.types.resource_arn.ResourceARN"]
    """<p>An Amazon Resource Name (ARN) that represents an Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.</p>"""
    event_triggers: NotRequired[
        "capo_snowball.types.event_trigger_definition_list.EventTriggerDefinitionList"
    ]
    """<p>The array of ARNs for <a>S3Resource</a> objects to trigger the <a>LambdaResource</a> objects associated with this job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaResource) -> dict:
    out: dict = {}
    if "lambda_arn" in value:
        out["LambdaArn"] = value["lambda_arn"]
    if "event_triggers" in value:
        import capo_snowball.types.event_trigger_definition_list

        out["EventTriggers"] = (
            capo_snowball.types.event_trigger_definition_list.serialize_aws_json_1_1(
                value["event_triggers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaResource:
    out: LambdaResource = {}  # type: ignore[typeddict-item]
    if data.get("LambdaArn") is not None:
        out["lambda_arn"] = data["LambdaArn"]
    if data.get("EventTriggers") is not None:
        import capo_snowball.types.event_trigger_definition_list

        out["event_triggers"] = (
            capo_snowball.types.event_trigger_definition_list.deserialize_aws_json_1_1(
                data["EventTriggers"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaResource) -> dict:
    out: dict = {}
    if "lambda_arn" in value:
        out["LambdaArn"] = value["lambda_arn"]
    if "event_triggers" in value:
        import capo_snowball.types.event_trigger_definition_list

        out["EventTriggers"] = (
            capo_snowball.types.event_trigger_definition_list.serialize_cbor(
                value["event_triggers"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LambdaResource:
    out: LambdaResource = {}  # type: ignore[typeddict-item]
    if data.get("LambdaArn") is not None:
        out["lambda_arn"] = data["LambdaArn"]
    if data.get("EventTriggers") is not None:
        import capo_snowball.types.event_trigger_definition_list

        out["event_triggers"] = (
            capo_snowball.types.event_trigger_definition_list.deserialize_cbor(
                data["EventTriggers"]
            )
        )
    return out
