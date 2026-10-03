"""Generated from Smithy shape ``com.amazonaws.codepipeline#WebhookDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_name
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.webhook_auth_configuration
    import capo_codepipeline.types.webhook_authentication_type
    import capo_codepipeline.types.webhook_filters
    import capo_codepipeline.types.webhook_name


class WebhookDefinition(TypedDict, closed=True):
    name: "capo_codepipeline.types.webhook_name.WebhookName"
    """<p>The name of the webhook.</p>"""
    target_pipeline: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline you want to connect to the webhook.</p>"""
    target_action: "capo_codepipeline.types.action_name.ActionName"
    """<p>The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.</p>"""
    filters: "capo_codepipeline.types.webhook_filters.WebhookFilters"
    """<p>A list of rules applied to the body/payload sent in the POST request to a webhook URL. All defined rules must pass for the request to be accepted and the pipeline started.</p>"""
    authentication: (
        "capo_codepipeline.types.webhook_authentication_type.WebhookAuthenticationType"
    )
    """<p>Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.</p> <important> <p>When creating CodePipeline webhooks, do not use your own credentials or reuse the same secret token across multiple webhooks. For optimal security, generate a unique secret token for each webhook you create. The secret token is an arbitrary string that you provide, which GitHub uses to compute and sign the webhook payloads sent to CodePipeline, for protecting the integrity and authenticity of the webhook payloads. Using your own credentials or reusing the same token across multiple webhooks can lead to security vulnerabilities.</p> </important> <note> <p>If a secret token was provided, it will be redacted in the response.</p> </note> <ul> <li> <p>For information about the authentication scheme implemented by GITHUB_HMAC, see <a href="https://developer.github.com/webhooks/securing/">Securing your webhooks</a> on the GitHub Developer website.</p> </li> <li> <p> IP rejects webhooks trigger requests unless they originate from an IP address in the IP range whitelisted in the authentication configuration.</p> </li> <li> <p> UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.</p> </li> </ul>"""
    authentication_configuration: (
        "capo_codepipeline.types.webhook_auth_configuration.WebhookAuthConfiguration"
    )
    """<p>Properties that configure the authentication applied to incoming webhook trigger requests. The required properties depend on the authentication type. For GITHUB_HMAC, only the <code>SecretToken </code>property must be set. For IP, only the <code>AllowedIPRange </code>property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["targetPipeline"] = value["target_pipeline"]
    out["targetAction"] = value["target_action"]
    import capo_codepipeline.types.webhook_filters

    out["filters"] = capo_codepipeline.types.webhook_filters.serialize_aws_json_1_1(
        value["filters"]
    )
    import capo_codepipeline.types.webhook_authentication_type

    out["authentication"] = (
        capo_codepipeline.types.webhook_authentication_type.serialize_aws_json_1_1(
            value["authentication"]
        )
    )
    import capo_codepipeline.types.webhook_auth_configuration

    out["authenticationConfiguration"] = (
        capo_codepipeline.types.webhook_auth_configuration.serialize_aws_json_1_1(
            value["authentication_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> WebhookDefinition:
    out: WebhookDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("WebhookDefinition.name required")
    if data.get("targetPipeline") is not None:
        out["target_pipeline"] = data["targetPipeline"]
    else:
        raise DeserializationError("WebhookDefinition.target_pipeline required")
    if data.get("targetAction") is not None:
        out["target_action"] = data["targetAction"]
    else:
        raise DeserializationError("WebhookDefinition.target_action required")
    if data.get("filters") is not None:
        import capo_codepipeline.types.webhook_filters

        out["filters"] = (
            capo_codepipeline.types.webhook_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    else:
        raise DeserializationError("WebhookDefinition.filters required")
    if data.get("authentication") is not None:
        import capo_codepipeline.types.webhook_authentication_type

        out["authentication"] = (
            capo_codepipeline.types.webhook_authentication_type.deserialize_aws_json_1_1(
                data["authentication"]
            )
        )
    else:
        raise DeserializationError("WebhookDefinition.authentication required")
    if data.get("authenticationConfiguration") is not None:
        import capo_codepipeline.types.webhook_auth_configuration

        out["authentication_configuration"] = (
            capo_codepipeline.types.webhook_auth_configuration.deserialize_aws_json_1_1(
                data["authenticationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "WebhookDefinition.authentication_configuration required"
        )
    return out
