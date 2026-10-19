"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreateABTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ab_test_description
    import capo_bedrock_agentcore.types.ab_test_evaluation_config
    import capo_bedrock_agentcore.types.ab_test_name
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.gateway_arn
    import capo_bedrock_agentcore.types.gateway_filter
    import capo_bedrock_agentcore.types.role_arn
    import capo_bedrock_agentcore.types.tags_map
    import capo_bedrock_agentcore.types.variant_list


class CreateABTestRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore.types.ab_test_name.ABTestName"
    """<p>The name of the A/B test. Must be unique within your account.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.ab_test_description.ABTestDescription"
    ]
    """<p>The description of the A/B test.</p>"""
    gateway_arn: "capo_bedrock_agentcore.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway to use for traffic splitting.</p>"""
    variants: "capo_bedrock_agentcore.types.variant_list.VariantList"
    """<p>The list of variants for the A/B test. Must contain exactly two variants: a control (C) and a treatment (T1), each with a configuration bundle or target reference and a traffic weight.</p>"""
    gateway_filter: NotRequired[
        "capo_bedrock_agentcore.types.gateway_filter.GatewayFilter"
    ]
    """<p>Optional filter to restrict which gateway target paths are included in the A/B test.</p>"""
    evaluation_config: (
        "capo_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig"
    )
    """<p>The evaluation configuration specifying which online evaluation configurations to use for measuring variant performance.</p>"""
    role_arn: "capo_bedrock_agentcore.types.role_arn.RoleArn"
    """<p>The IAM role ARN that grants permissions for the A/B test to access gateway and evaluation resources.</p>"""
    enable_on_create: NotRequired["bool"]
    """<p>Whether to enable the A/B test immediately upon creation. If true, traffic splitting begins automatically.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""
    tags: NotRequired["capo_bedrock_agentcore.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to associate with the A/B test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateABTestRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["gatewayArn"] = value["gateway_arn"]
    import capo_bedrock_agentcore.types.variant_list

    out["variants"] = capo_bedrock_agentcore.types.variant_list.serialize_json(
        value["variants"]
    )
    if "gateway_filter" in value:
        import capo_bedrock_agentcore.types.gateway_filter

        out["gatewayFilter"] = (
            capo_bedrock_agentcore.types.gateway_filter.serialize_json(
                value["gateway_filter"]
            )
        )
    import capo_bedrock_agentcore.types.ab_test_evaluation_config

    out["evaluationConfig"] = (
        capo_bedrock_agentcore.types.ab_test_evaluation_config.serialize_json(
            value["evaluation_config"]
        )
    )
    out["roleArn"] = value["role_arn"]
    if "enable_on_create" in value:
        out["enableOnCreate"] = value["enable_on_create"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_bedrock_agentcore.types.tags_map

        out["tags"] = capo_bedrock_agentcore.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateABTestRequest:
    out: CreateABTestRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        out["gateway_arn"] = ""
    if data.get("variants") is not None:
        import capo_bedrock_agentcore.types.variant_list

        out["variants"] = capo_bedrock_agentcore.types.variant_list.deserialize_json(
            data["variants"]
        )
    else:
        out["variants"] = []
    if data.get("gatewayFilter") is not None:
        import capo_bedrock_agentcore.types.gateway_filter

        out["gateway_filter"] = (
            capo_bedrock_agentcore.types.gateway_filter.deserialize_json(
                data["gatewayFilter"]
            )
        )
    if data.get("evaluationConfig") is not None:
        import capo_bedrock_agentcore.types.ab_test_evaluation_config

        out["evaluation_config"] = (
            capo_bedrock_agentcore.types.ab_test_evaluation_config.deserialize_json(
                data["evaluationConfig"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["evaluation_config"] = (
            capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("enableOnCreate") is not None:
        out["enable_on_create"] = data["enableOnCreate"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore.types.tags_map

        out["tags"] = capo_bedrock_agentcore.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
