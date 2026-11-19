"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Feedback``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_insights.types.feedback_key
    import capo_application_insights.types.feedback_value

Feedback: TypeAlias = dict[
    "capo_application_insights.types.feedback_key.FeedbackKey",
    "capo_application_insights.types.feedback_value.FeedbackValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Feedback) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_application_insights.types.feedback_key
        import capo_application_insights.types.feedback_value

        out[
            capo_application_insights.types.feedback_key.serialize_aws_json_1_1(key)
        ] = capo_application_insights.types.feedback_value.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> Feedback:
    out: Feedback = {}
    for key, value in data.items():
        import capo_application_insights.types.feedback_key

        if value is None:
            continue
        import capo_application_insights.types.feedback_value

        out[
            capo_application_insights.types.feedback_key.deserialize_aws_json_1_1(key)
        ] = capo_application_insights.types.feedback_value.deserialize_aws_json_1_1(
            value
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: Feedback) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_application_insights.types.feedback_key
        import capo_application_insights.types.feedback_value

        out[capo_application_insights.types.feedback_key.serialize_cbor(key)] = (
            capo_application_insights.types.feedback_value.serialize_cbor(value)
        )
    return out


def deserialize_cbor(data: dict) -> Feedback:
    out: Feedback = {}
    for key, value in data.items():
        import capo_application_insights.types.feedback_key

        if value is None:
            continue
        import capo_application_insights.types.feedback_value

        out[capo_application_insights.types.feedback_key.deserialize_cbor(key)] = (
            capo_application_insights.types.feedback_value.deserialize_cbor(value)
        )
    return out
