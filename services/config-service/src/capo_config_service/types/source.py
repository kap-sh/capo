"""Generated from Smithy shape ``com.amazonaws.configservice#Source``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.custom_policy_details
    import capo_config_service.types.owner
    import capo_config_service.types.source_details
    import capo_config_service.types.string_with_char_limit256


class Source(TypedDict, closed=True):
    owner: "capo_config_service.types.owner.Owner"
    """<p>Indicates whether Amazon Web Services or the customer owns and manages the Config rule.</p> <p>Config Managed Rules are predefined rules owned by Amazon Web Services. For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">Config Managed Rules</a> in the <i>Config developer guide</i>.</p> <p>Config Custom Rules are rules that you can develop either with Guard (<code>CUSTOM_POLICY</code>) or Lambda (<code>CUSTOM_LAMBDA</code>). For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html">Config Custom Rules </a> in the <i>Config developer guide</i>.</p>"""
    source_identifier: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>For Config Managed rules, a predefined identifier from a list. For example, <code>IAM_PASSWORD_POLICY</code> is a managed rule. To reference a managed rule, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html">List of Config Managed Rules</a>.</p> <p>For Config Custom Lambda rules, the identifier is the Amazon Resource Name (ARN) of the rule's Lambda function, such as <code>arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name</code>.</p> <p>For Config Custom Policy rules, this field will be ignored.</p>"""
    source_details: NotRequired[
        "capo_config_service.types.source_details.SourceDetails"
    ]
    """<p>Provides the source and the message types that cause Config to evaluate your Amazon Web Services resources against a rule. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.</p> <p>If the owner is set to <code>CUSTOM_POLICY</code>, the only acceptable values for the Config rule trigger message type are <code>ConfigurationItemChangeNotification</code> and <code>OversizedConfigurationItemChangeNotification</code>.</p>"""
    custom_policy_details: NotRequired[
        "capo_config_service.types.custom_policy_details.CustomPolicyDetails"
    ]
    """<p>Provides the runtime system, policy definition, and whether debug logging is enabled. Required when owner is set to <code>CUSTOM_POLICY</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Source) -> dict:
    out: dict = {}
    import capo_config_service.types.owner

    out["Owner"] = capo_config_service.types.owner.serialize_aws_json_1_1(
        value["owner"]
    )
    if "source_identifier" in value:
        out["SourceIdentifier"] = value["source_identifier"]
    if "source_details" in value:
        import capo_config_service.types.source_details

        out["SourceDetails"] = (
            capo_config_service.types.source_details.serialize_aws_json_1_1(
                value["source_details"]
            )
        )
    if "custom_policy_details" in value:
        import capo_config_service.types.custom_policy_details

        out["CustomPolicyDetails"] = (
            capo_config_service.types.custom_policy_details.serialize_aws_json_1_1(
                value["custom_policy_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Source:
    out: Source = {}  # type: ignore[typeddict-item]
    if data.get("Owner") is not None:
        import capo_config_service.types.owner

        out["owner"] = capo_config_service.types.owner.deserialize_aws_json_1_1(
            data["Owner"]
        )
    else:
        raise DeserializationError("Source.owner required")
    if data.get("SourceIdentifier") is not None:
        out["source_identifier"] = data["SourceIdentifier"]
    if data.get("SourceDetails") is not None:
        import capo_config_service.types.source_details

        out["source_details"] = (
            capo_config_service.types.source_details.deserialize_aws_json_1_1(
                data["SourceDetails"]
            )
        )
    if data.get("CustomPolicyDetails") is not None:
        import capo_config_service.types.custom_policy_details

        out["custom_policy_details"] = (
            capo_config_service.types.custom_policy_details.deserialize_aws_json_1_1(
                data["CustomPolicyDetails"]
            )
        )
    return out
