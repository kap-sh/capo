"""Generated from Smithy shape ``com.amazonaws.lambdaweb#CreateWebFunctionEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.auth_type
    import capo_lambda_web.types.auto_deployment_mode
    import capo_lambda_web.types.description
    import capo_lambda_web.types.endpoint_name
    import capo_lambda_web.types.endpoint_type
    import capo_lambda_web.types.function_name
    import capo_lambda_web.types.region_list
    import capo_lambda_web.types.revision_weight_list
    import capo_lambda_web.types.scaling_config
    import capo_lambda_web.types.throttle_config


class CreateWebFunctionEndpointRequest(TypedDict, closed=True):
    function_name: "capo_lambda_web.types.function_name.FunctionName"
    """<p>The name of the web function to create the endpoint for. You can specify the function name or the function ARN. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    endpoint_name: "capo_lambda_web.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint to create. The name can contain letters, numbers, hyphens (-), and underscores (_), and can't begin or end with a hyphen or an underscore. The length constraint applies only to the full ARN. If you specify only the endpoint name, it is limited to 64 characters in length.</p>"""
    description: NotRequired["capo_lambda_web.types.description.Description"]
    """<p>A description of the endpoint.</p>"""
    endpoint_type: "capo_lambda_web.types.endpoint_type.EndpointType"
    """<p>The type of endpoint to create. Determines how traffic is served and routed across Regions.</p>"""
    auth_type: "capo_lambda_web.types.auth_type.AuthType"
    """<p>The authorization type for the endpoint.</p>"""
    auto_deployment_mode: NotRequired[
        "capo_lambda_web.types.auto_deployment_mode.AutoDeploymentMode"
    ]
    """<p>The auto-deployment mode for the endpoint. Controls whether the endpoint automatically serves the newest revision. If you don't specify a value, the default is <code>Disabled</code>, and this default is returned in the response.</p>"""
    revision_weights: NotRequired[
        "capo_lambda_web.types.revision_weight_list.RevisionWeightList"
    ]
    """<p>A list of revision weights that determine how traffic is distributed across revisions. Up to two revisions can be specified for canary or blue-green deployments.</p>"""
    regions: NotRequired["capo_lambda_web.types.region_list.RegionList"]
    """<p>The list of Regions for the endpoint. Required when the endpoint type is <code>MultiRegion</code> or <code>PerRegion</code>: specify at least one Region other than the Region where you create the endpoint (the home Region). The home Region is added automatically if you don't include it; specifying only the home Region isn't allowed. When the endpoint type is <code>HomeRegion</code>, omit this field or specify only the home Region.</p>"""
    scaling_config: NotRequired["capo_lambda_web.types.scaling_config.ScalingConfig"]
    """<p>The scaling configuration for the endpoint. There is no default value. If you don't specify a scaling configuration, it is absent from the response.</p>"""
    throttle_config: NotRequired["capo_lambda_web.types.throttle_config.ThrottleConfig"]
    """<p>The throttling configuration for the endpoint. There is no default value. If you don't specify a throttling configuration, it is absent from the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebFunctionEndpointRequest) -> dict:
    out: dict = {}
    out["endpointName"] = value["endpoint_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_lambda_web.types.endpoint_type

    out["endpointType"] = capo_lambda_web.types.endpoint_type.serialize_json(
        value["endpoint_type"]
    )
    import capo_lambda_web.types.auth_type

    out["authType"] = capo_lambda_web.types.auth_type.serialize_json(value["auth_type"])
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
    if "regions" in value:
        import capo_lambda_web.types.region_list

        out["regions"] = capo_lambda_web.types.region_list.serialize_json(
            value["regions"]
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


def deserialize_json(data: dict) -> CreateWebFunctionEndpointRequest:
    out: CreateWebFunctionEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointRequest.endpoint_name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("endpointType") is not None:
        import capo_lambda_web.types.endpoint_type

        out["endpoint_type"] = capo_lambda_web.types.endpoint_type.deserialize_json(
            data["endpointType"]
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointRequest.endpoint_type required"
        )
    if data.get("authType") is not None:
        import capo_lambda_web.types.auth_type

        out["auth_type"] = capo_lambda_web.types.auth_type.deserialize_json(
            data["authType"]
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointRequest.auth_type required"
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
    if data.get("regions") is not None:
        import capo_lambda_web.types.region_list

        out["regions"] = capo_lambda_web.types.region_list.deserialize_json(
            data["regions"]
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
