"""Generated from Smithy shape ``com.amazonaws.lambdaweb#UpdateWebFunctionEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.auth_type
    import capo_lambda_web.types.auto_deployment_mode
    import capo_lambda_web.types.description
    import capo_lambda_web.types.endpoint_name
    import capo_lambda_web.types.function_name
    import capo_lambda_web.types.revision_weight_list
    import capo_lambda_web.types.scaling_config
    import capo_lambda_web.types.throttle_config


class UpdateWebFunctionEndpointRequest(TypedDict, closed=True):
    function_name: "capo_lambda_web.types.function_name.FunctionName"
    """<p>The name of the web function. You can specify the function name or the function ARN. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    endpoint_name: "capo_lambda_web.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint to update. You can specify the endpoint name or the endpoint ARN. The length constraint applies only to the full ARN. If you specify only the endpoint name, it is limited to 64 characters in length.</p>"""
    description: NotRequired["capo_lambda_web.types.description.Description"]
    """<p>A description of the endpoint.</p>"""
    auth_type: NotRequired["capo_lambda_web.types.auth_type.AuthType"]
    """<p>The authorization type for the endpoint.</p>"""
    auto_deployment_mode: NotRequired[
        "capo_lambda_web.types.auto_deployment_mode.AutoDeploymentMode"
    ]
    """<p>The auto-deployment mode for the endpoint.</p>"""
    revision_weights: NotRequired[
        "capo_lambda_web.types.revision_weight_list.RevisionWeightList"
    ]
    """<p>A list of revision weights that determine how traffic is distributed across revisions.</p>"""
    scaling_config: NotRequired["capo_lambda_web.types.scaling_config.ScalingConfig"]
    """<p>The scaling configuration for the endpoint. Omit this field to keep the current scaling configuration. To clear a previously set <code>maxEnvironments</code> value, specify an empty object.</p>"""
    throttle_config: NotRequired["capo_lambda_web.types.throttle_config.ThrottleConfig"]
    """<p>The throttling configuration for the endpoint. Omit this field to keep the current throttling configuration. To clear a previously set <code>rateLimit</code> value, specify an empty object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWebFunctionEndpointRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "auth_type" in value:
        import capo_lambda_web.types.auth_type

        out["authType"] = capo_lambda_web.types.auth_type.serialize_json(
            value["auth_type"]
        )
    if "auto_deployment_mode" in value:
        import capo_lambda_web.types.auto_deployment_mode

        out["autoDeploymentMode"] = (
            capo_lambda_web.types.auto_deployment_mode.serialize_json(
                value["auto_deployment_mode"]
            )
        )
    if "revision_weights" in value:
        import capo_lambda_web.types.revision_weight_list

        out["revisionWeights"] = (
            capo_lambda_web.types.revision_weight_list.serialize_json(
                value["revision_weights"]
            )
        )
    if "scaling_config" in value:
        import capo_lambda_web.types.scaling_config

        out["scalingConfig"] = capo_lambda_web.types.scaling_config.serialize_json(
            value["scaling_config"]
        )
    if "throttle_config" in value:
        import capo_lambda_web.types.throttle_config

        out["throttleConfig"] = capo_lambda_web.types.throttle_config.serialize_json(
            value["throttle_config"]
        )
    return out


def deserialize_json(data: dict) -> UpdateWebFunctionEndpointRequest:
    out: UpdateWebFunctionEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("authType") is not None:
        import capo_lambda_web.types.auth_type

        out["auth_type"] = capo_lambda_web.types.auth_type.deserialize_json(
            data["authType"]
        )
    if data.get("autoDeploymentMode") is not None:
        import capo_lambda_web.types.auto_deployment_mode

        out["auto_deployment_mode"] = (
            capo_lambda_web.types.auto_deployment_mode.deserialize_json(
                data["autoDeploymentMode"]
            )
        )
    if data.get("revisionWeights") is not None:
        import capo_lambda_web.types.revision_weight_list

        out["revision_weights"] = (
            capo_lambda_web.types.revision_weight_list.deserialize_json(
                data["revisionWeights"]
            )
        )
    if data.get("scalingConfig") is not None:
        import capo_lambda_web.types.scaling_config

        out["scaling_config"] = capo_lambda_web.types.scaling_config.deserialize_json(
            data["scalingConfig"]
        )
    if data.get("throttleConfig") is not None:
        import capo_lambda_web.types.throttle_config

        out["throttle_config"] = capo_lambda_web.types.throttle_config.deserialize_json(
            data["throttleConfig"]
        )
    return out
