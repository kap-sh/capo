"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#UpdateSubscriberRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.batch_configuration
    import capo_eventbridgev2.types.description
    import capo_eventbridgev2.types.filter_configuration
    import capo_eventbridgev2.types.log_configuration
    import capo_eventbridgev2.types.on_failure_configuration
    import capo_eventbridgev2.types.resume_position
    import capo_eventbridgev2.types.retry_policy
    import capo_eventbridgev2.types.subscriber_arn
    import capo_eventbridgev2.types.subscriber_state
    import capo_eventbridgev2.types.transformer
    import capo_eventbridgev2.types.update_invoke_configuration


class UpdateSubscriberRequest(TypedDict, closed=True):
    subscriber_arn: "capo_eventbridgev2.types.subscriber_arn.SubscriberArn"
    description: NotRequired["capo_eventbridgev2.types.description.Description"]
    state: NotRequired["capo_eventbridgev2.types.subscriber_state.SubscriberState"]
    resume_position: NotRequired[
        "capo_eventbridgev2.types.resume_position.ResumePosition"
    ]
    invoke_configuration: NotRequired[
        "capo_eventbridgev2.types.update_invoke_configuration.UpdateInvokeConfiguration"
    ]
    filter_configuration: NotRequired[
        "capo_eventbridgev2.types.filter_configuration.FilterConfiguration"
    ]
    batch_configuration: NotRequired[
        "capo_eventbridgev2.types.batch_configuration.BatchConfiguration"
    ]
    transformer: NotRequired["capo_eventbridgev2.types.transformer.Transformer"]
    """Not applicable to universal (aws-sdk) targets, whose input transformation is UniversalTargetParameters.Input; a Transformer on such a target is rejected."""
    retry_policy: NotRequired["capo_eventbridgev2.types.retry_policy.RetryPolicy"]
    on_failure_configuration: NotRequired[
        "capo_eventbridgev2.types.on_failure_configuration.OnFailureConfiguration"
    ]
    log_configuration: NotRequired[
        "capo_eventbridgev2.types.log_configuration.LogConfiguration"
    ]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateSubscriberRequest) -> dict:
    out: dict = {}
    out["SubscriberArn"] = value["subscriber_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import capo_eventbridgev2.types.subscriber_state

        out["State"] = capo_eventbridgev2.types.subscriber_state.serialize_cbor(
            value["state"]
        )
    if "resume_position" in value:
        import capo_eventbridgev2.types.resume_position

        out["ResumePosition"] = capo_eventbridgev2.types.resume_position.serialize_cbor(
            value["resume_position"]
        )
    if "invoke_configuration" in value:
        import capo_eventbridgev2.types.update_invoke_configuration

        out["InvokeConfiguration"] = (
            capo_eventbridgev2.types.update_invoke_configuration.serialize_cbor(
                value["invoke_configuration"]
            )
        )
    if "filter_configuration" in value:
        import capo_eventbridgev2.types.filter_configuration

        out["FilterConfiguration"] = (
            capo_eventbridgev2.types.filter_configuration.serialize_cbor(
                value["filter_configuration"]
            )
        )
    if "batch_configuration" in value:
        import capo_eventbridgev2.types.batch_configuration

        out["BatchConfiguration"] = (
            capo_eventbridgev2.types.batch_configuration.serialize_cbor(
                value["batch_configuration"]
            )
        )
    if "transformer" in value:
        import capo_eventbridgev2.types.transformer

        out["Transformer"] = capo_eventbridgev2.types.transformer.serialize_cbor(
            value["transformer"]
        )
    if "retry_policy" in value:
        import capo_eventbridgev2.types.retry_policy

        out["RetryPolicy"] = capo_eventbridgev2.types.retry_policy.serialize_cbor(
            value["retry_policy"]
        )
    if "on_failure_configuration" in value:
        import capo_eventbridgev2.types.on_failure_configuration

        out["OnFailureConfiguration"] = (
            capo_eventbridgev2.types.on_failure_configuration.serialize_cbor(
                value["on_failure_configuration"]
            )
        )
    if "log_configuration" in value:
        import capo_eventbridgev2.types.log_configuration

        out["LogConfiguration"] = (
            capo_eventbridgev2.types.log_configuration.serialize_cbor(
                value["log_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateSubscriberRequest:
    out: UpdateSubscriberRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubscriberArn") is not None:
        out["subscriber_arn"] = data["SubscriberArn"]
    else:
        out["subscriber_arn"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("State") is not None:
        import capo_eventbridgev2.types.subscriber_state

        out["state"] = capo_eventbridgev2.types.subscriber_state.deserialize_cbor(
            data["State"]
        )
    if data.get("ResumePosition") is not None:
        import capo_eventbridgev2.types.resume_position

        out["resume_position"] = (
            capo_eventbridgev2.types.resume_position.deserialize_cbor(
                data["ResumePosition"]
            )
        )
    if data.get("InvokeConfiguration") is not None:
        import capo_eventbridgev2.types.update_invoke_configuration

        out["invoke_configuration"] = (
            capo_eventbridgev2.types.update_invoke_configuration.deserialize_cbor(
                data["InvokeConfiguration"]
            )
        )
    if data.get("FilterConfiguration") is not None:
        import capo_eventbridgev2.types.filter_configuration

        out["filter_configuration"] = (
            capo_eventbridgev2.types.filter_configuration.deserialize_cbor(
                data["FilterConfiguration"]
            )
        )
    if data.get("BatchConfiguration") is not None:
        import capo_eventbridgev2.types.batch_configuration

        out["batch_configuration"] = (
            capo_eventbridgev2.types.batch_configuration.deserialize_cbor(
                data["BatchConfiguration"]
            )
        )
    if data.get("Transformer") is not None:
        import capo_eventbridgev2.types.transformer

        out["transformer"] = capo_eventbridgev2.types.transformer.deserialize_cbor(
            data["Transformer"]
        )
    if data.get("RetryPolicy") is not None:
        import capo_eventbridgev2.types.retry_policy

        out["retry_policy"] = capo_eventbridgev2.types.retry_policy.deserialize_cbor(
            data["RetryPolicy"]
        )
    if data.get("OnFailureConfiguration") is not None:
        import capo_eventbridgev2.types.on_failure_configuration

        out["on_failure_configuration"] = (
            capo_eventbridgev2.types.on_failure_configuration.deserialize_cbor(
                data["OnFailureConfiguration"]
            )
        )
    if data.get("LogConfiguration") is not None:
        import capo_eventbridgev2.types.log_configuration

        out["log_configuration"] = (
            capo_eventbridgev2.types.log_configuration.deserialize_cbor(
                data["LogConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateSubscriberRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "invoke_configuration" in value:
        import capo_eventbridgev2.types.update_invoke_configuration

        out["invoke_configuration"] = (
            capo_eventbridgev2.types.update_invoke_configuration.redact_sensitive(
                value["invoke_configuration"]
            )
        )
    if "filter_configuration" in value:
        import capo_eventbridgev2.types.filter_configuration

        out["filter_configuration"] = (
            capo_eventbridgev2.types.filter_configuration.redact_sensitive(
                value["filter_configuration"]
            )
        )
    if "transformer" in value:
        import capo_eventbridgev2.types.transformer

        out["transformer"] = capo_eventbridgev2.types.transformer.redact_sensitive(
            value["transformer"]
        )
    return out
