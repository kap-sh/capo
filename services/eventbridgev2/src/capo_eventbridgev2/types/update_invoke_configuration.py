"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#UpdateInvokeConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_v2_parameters
    import capo_eventbridgev2.types.http_parameters
    import capo_eventbridgev2.types.kinesis_parameters
    import capo_eventbridgev2.types.lambda_parameters
    import capo_eventbridgev2.types.role_arn
    import capo_eventbridgev2.types.sns_parameters
    import capo_eventbridgev2.types.sqs_parameters
    import capo_eventbridgev2.types.step_functions_parameters
    import capo_eventbridgev2.types.universal_target_parameters


class UpdateInvokeConfiguration(TypedDict, closed=True):
    role_arn: "capo_eventbridgev2.types.role_arn.RoleArn"
    """IAM role the service assumes to invoke the target. Must belong to the calling account."""
    lambda_parameters: NotRequired[
        "capo_eventbridgev2.types.lambda_parameters.LambdaParameters"
    ]
    sqs_parameters: NotRequired["capo_eventbridgev2.types.sqs_parameters.SqsParameters"]
    sns_parameters: NotRequired["capo_eventbridgev2.types.sns_parameters.SnsParameters"]
    kinesis_parameters: NotRequired[
        "capo_eventbridgev2.types.kinesis_parameters.KinesisParameters"
    ]
    step_functions_parameters: NotRequired[
        "capo_eventbridgev2.types.step_functions_parameters.StepFunctionsParameters"
    ]
    http_parameters: NotRequired[
        "capo_eventbridgev2.types.http_parameters.HttpParameters"
    ]
    universal_target_parameters: NotRequired[
        "capo_eventbridgev2.types.universal_target_parameters.UniversalTargetParameters"
    ]
    event_bus_v2_parameters: NotRequired[
        "capo_eventbridgev2.types.event_bus_v2_parameters.EventBusV2Parameters"
    ]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateInvokeConfiguration) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    if "lambda_parameters" in value:
        import capo_eventbridgev2.types.lambda_parameters

        out["LambdaParameters"] = (
            capo_eventbridgev2.types.lambda_parameters.serialize_cbor(
                value["lambda_parameters"]
            )
        )
    if "sqs_parameters" in value:
        import capo_eventbridgev2.types.sqs_parameters

        out["SqsParameters"] = capo_eventbridgev2.types.sqs_parameters.serialize_cbor(
            value["sqs_parameters"]
        )
    if "sns_parameters" in value:
        import capo_eventbridgev2.types.sns_parameters

        out["SnsParameters"] = capo_eventbridgev2.types.sns_parameters.serialize_cbor(
            value["sns_parameters"]
        )
    if "kinesis_parameters" in value:
        import capo_eventbridgev2.types.kinesis_parameters

        out["KinesisParameters"] = (
            capo_eventbridgev2.types.kinesis_parameters.serialize_cbor(
                value["kinesis_parameters"]
            )
        )
    if "step_functions_parameters" in value:
        import capo_eventbridgev2.types.step_functions_parameters

        out["StepFunctionsParameters"] = (
            capo_eventbridgev2.types.step_functions_parameters.serialize_cbor(
                value["step_functions_parameters"]
            )
        )
    if "http_parameters" in value:
        import capo_eventbridgev2.types.http_parameters

        out["HttpParameters"] = capo_eventbridgev2.types.http_parameters.serialize_cbor(
            value["http_parameters"]
        )
    if "universal_target_parameters" in value:
        import capo_eventbridgev2.types.universal_target_parameters

        out["UniversalTargetParameters"] = (
            capo_eventbridgev2.types.universal_target_parameters.serialize_cbor(
                value["universal_target_parameters"]
            )
        )
    if "event_bus_v2_parameters" in value:
        import capo_eventbridgev2.types.event_bus_v2_parameters

        out["EventBusV2Parameters"] = (
            capo_eventbridgev2.types.event_bus_v2_parameters.serialize_cbor(
                value["event_bus_v2_parameters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateInvokeConfiguration:
    out: UpdateInvokeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("LambdaParameters") is not None:
        import capo_eventbridgev2.types.lambda_parameters

        out["lambda_parameters"] = (
            capo_eventbridgev2.types.lambda_parameters.deserialize_cbor(
                data["LambdaParameters"]
            )
        )
    if data.get("SqsParameters") is not None:
        import capo_eventbridgev2.types.sqs_parameters

        out["sqs_parameters"] = (
            capo_eventbridgev2.types.sqs_parameters.deserialize_cbor(
                data["SqsParameters"]
            )
        )
    if data.get("SnsParameters") is not None:
        import capo_eventbridgev2.types.sns_parameters

        out["sns_parameters"] = (
            capo_eventbridgev2.types.sns_parameters.deserialize_cbor(
                data["SnsParameters"]
            )
        )
    if data.get("KinesisParameters") is not None:
        import capo_eventbridgev2.types.kinesis_parameters

        out["kinesis_parameters"] = (
            capo_eventbridgev2.types.kinesis_parameters.deserialize_cbor(
                data["KinesisParameters"]
            )
        )
    if data.get("StepFunctionsParameters") is not None:
        import capo_eventbridgev2.types.step_functions_parameters

        out["step_functions_parameters"] = (
            capo_eventbridgev2.types.step_functions_parameters.deserialize_cbor(
                data["StepFunctionsParameters"]
            )
        )
    if data.get("HttpParameters") is not None:
        import capo_eventbridgev2.types.http_parameters

        out["http_parameters"] = (
            capo_eventbridgev2.types.http_parameters.deserialize_cbor(
                data["HttpParameters"]
            )
        )
    if data.get("UniversalTargetParameters") is not None:
        import capo_eventbridgev2.types.universal_target_parameters

        out["universal_target_parameters"] = (
            capo_eventbridgev2.types.universal_target_parameters.deserialize_cbor(
                data["UniversalTargetParameters"]
            )
        )
    if data.get("EventBusV2Parameters") is not None:
        import capo_eventbridgev2.types.event_bus_v2_parameters

        out["event_bus_v2_parameters"] = (
            capo_eventbridgev2.types.event_bus_v2_parameters.deserialize_cbor(
                data["EventBusV2Parameters"]
            )
        )
    return out


def redact_sensitive(value: UpdateInvokeConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "lambda_parameters" in value:
        out["lambda_parameters"] = "*** Sensitive Data Redacted ***"
    if "sqs_parameters" in value:
        out["sqs_parameters"] = "*** Sensitive Data Redacted ***"
    if "sns_parameters" in value:
        out["sns_parameters"] = "*** Sensitive Data Redacted ***"
    if "kinesis_parameters" in value:
        out["kinesis_parameters"] = "*** Sensitive Data Redacted ***"
    if "step_functions_parameters" in value:
        out["step_functions_parameters"] = "*** Sensitive Data Redacted ***"
    if "http_parameters" in value:
        out["http_parameters"] = "*** Sensitive Data Redacted ***"
    if "universal_target_parameters" in value:
        out["universal_target_parameters"] = "*** Sensitive Data Redacted ***"
    if "event_bus_v2_parameters" in value:
        out["event_bus_v2_parameters"] = "*** Sensitive Data Redacted ***"
    return out
