"""Generated from Smithy shape ``com.amazonaws.wafv2#ChallengeJavascriptSdkInjection``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.associated_resource_type
    import capo_wafv2.types.challenge_javascript_sdk_injection_config

ChallengeJavascriptSdkInjection: TypeAlias = dict[
    "capo_wafv2.types.associated_resource_type.AssociatedResourceType",
    "capo_wafv2.types.challenge_javascript_sdk_injection_config.ChallengeJavascriptSdkInjectionConfig",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ChallengeJavascriptSdkInjection) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_wafv2.types.associated_resource_type
        import capo_wafv2.types.challenge_javascript_sdk_injection_config

        out[capo_wafv2.types.associated_resource_type.serialize_aws_json_1_1(key)] = (
            capo_wafv2.types.challenge_javascript_sdk_injection_config.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChallengeJavascriptSdkInjection:
    out: ChallengeJavascriptSdkInjection = {}
    for key, value in data.items():
        import capo_wafv2.types.associated_resource_type

        if value is None:
            continue
        import capo_wafv2.types.challenge_javascript_sdk_injection_config

        out[capo_wafv2.types.associated_resource_type.deserialize_aws_json_1_1(key)] = (
            capo_wafv2.types.challenge_javascript_sdk_injection_config.deserialize_aws_json_1_1(
                value
            )
        )
    return out
