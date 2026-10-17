"""Generated from Smithy shape ``com.amazonaws.lambdaweb#CreateWebFunctionEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.auth_type
    import capo_lambda_web.types.auto_deployment_mode
    import capo_lambda_web.types.date_time
    import capo_lambda_web.types.description
    import capo_lambda_web.types.domain_name
    import capo_lambda_web.types.endpoint_arn
    import capo_lambda_web.types.endpoint_name
    import capo_lambda_web.types.endpoint_state
    import capo_lambda_web.types.endpoint_type
    import capo_lambda_web.types.endpoint_update_status
    import capo_lambda_web.types.function_arn
    import capo_lambda_web.types.region_list
    import capo_lambda_web.types.regional_endpoints
    import capo_lambda_web.types.revision_weight_list
    import capo_lambda_web.types.scaling_config
    import capo_lambda_web.types.throttle_config


class CreateWebFunctionEndpointResponse(TypedDict, closed=True):
    function_arn: "capo_lambda_web.types.function_arn.FunctionArn"
    """<p>The Amazon Resource Name (ARN) of the web function.</p>"""
    endpoint_arn: "capo_lambda_web.types.endpoint_arn.EndpointArn"
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""
    endpoint_name: "capo_lambda_web.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint.</p>"""
    description: NotRequired["capo_lambda_web.types.description.Description"]
    """<p>The description of the endpoint.</p>"""
    endpoint_type: "capo_lambda_web.types.endpoint_type.EndpointType"
    domain_name: "capo_lambda_web.types.domain_name.DomainName"
    """<p>The domain name assigned to the endpoint.</p>"""
    auth_type: "capo_lambda_web.types.auth_type.AuthType"
    auto_deployment_mode: (
        "capo_lambda_web.types.auto_deployment_mode.AutoDeploymentMode"
    )
    revision_weights: "capo_lambda_web.types.revision_weight_list.RevisionWeightList"
    """<p>The traffic distribution across revisions for the endpoint. Each entry maps a revision to a weight from 1 to 100.</p>"""
    regions: "capo_lambda_web.types.region_list.RegionList"
    """<p>The Regions configured for the endpoint.</p>"""
    scaling_config: NotRequired["capo_lambda_web.types.scaling_config.ScalingConfig"]
    throttle_config: NotRequired["capo_lambda_web.types.throttle_config.ThrottleConfig"]
    state: "capo_lambda_web.types.endpoint_state.EndpointState"
    """<p>The current state of the endpoint.</p>"""
    state_reason: "str"
    """<p>The reason for the current state of the endpoint.</p>"""
    update_status: NotRequired[
        "capo_lambda_web.types.endpoint_update_status.EndpointUpdateStatus"
    ]
    update_status_reason: NotRequired["str"]
    """<p>The reason for the endpoint's most recent update status.</p>"""
    regional_endpoints: "capo_lambda_web.types.regional_endpoints.RegionalEndpoints"
    """<p>The list of regional endpoint configurations.</p>"""
    created_at: "capo_lambda_web.types.date_time.DateTime"
    """<p>The date and time the endpoint was created.</p>"""
    updated_at: "capo_lambda_web.types.date_time.DateTime"
    """<p>The date and time the endpoint was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebFunctionEndpointResponse) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    out["endpointArn"] = value["endpoint_arn"]
    out["endpointName"] = value["endpoint_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_lambda_web.types.endpoint_type

    out["endpointType"] = capo_lambda_web.types.endpoint_type.serialize_json(
        value["endpoint_type"]
    )
    out["domainName"] = value["domain_name"]
    import capo_lambda_web.types.auth_type

    out["authType"] = capo_lambda_web.types.auth_type.serialize_json(value["auth_type"])
    import capo_lambda_web.types.auto_deployment_mode

    out["autoDeploymentMode"] = (
        capo_lambda_web.types.auto_deployment_mode.serialize_json(
            value["auto_deployment_mode"]
        )
    )
    import capo_lambda_web.types.revision_weight_list

    out["revisionWeights"] = capo_lambda_web.types.revision_weight_list.serialize_json(
        value["revision_weights"]
    )
    import capo_lambda_web.types.region_list

    out["regions"] = capo_lambda_web.types.region_list.serialize_json(value["regions"])
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
    import capo_lambda_web.types.endpoint_state

    out["state"] = capo_lambda_web.types.endpoint_state.serialize_json(value["state"])
    out["stateReason"] = value["state_reason"]
    if "update_status" in value:
        import capo_lambda_web.types.endpoint_update_status

        out["updateStatus"] = (
            capo_lambda_web.types.endpoint_update_status.serialize_json(
                value["update_status"]
            )
        )
    if "update_status_reason" in value:
        out["updateStatusReason"] = value["update_status_reason"]
    import capo_lambda_web.types.regional_endpoints

    out["regionalEndpoints"] = capo_lambda_web.types.regional_endpoints.serialize_json(
        value["regional_endpoints"]
    )
    import capo_lambda_web.types.date_time

    out["createdAt"] = capo_lambda_web.types.date_time.serialize_json(
        value["created_at"]
    )
    import capo_lambda_web.types.date_time

    out["updatedAt"] = capo_lambda_web.types.date_time.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateWebFunctionEndpointResponse:
    out: CreateWebFunctionEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("functionArn") is not None:
        out["function_arn"] = data["functionArn"]
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.function_arn required"
        )
    if data.get("endpointArn") is not None:
        out["endpoint_arn"] = data["endpointArn"]
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.endpoint_arn required"
        )
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.endpoint_name required"
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
            "CreateWebFunctionEndpointResponse.endpoint_type required"
        )
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.domain_name required"
        )
    if data.get("authType") is not None:
        import capo_lambda_web.types.auth_type

        out["auth_type"] = capo_lambda_web.types.auth_type.deserialize_json(
            data["authType"]
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.auth_type required"
        )
    if data.get("autoDeploymentMode") is not None:
        import capo_lambda_web.types.auto_deployment_mode

        out["auto_deployment_mode"] = (
            capo_lambda_web.types.auto_deployment_mode.deserialize_json(
                data["autoDeploymentMode"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.auto_deployment_mode required"
        )
    if data.get("revisionWeights") is not None:
        import capo_lambda_web.types.revision_weight_list

        out["revision_weights"] = (
            capo_lambda_web.types.revision_weight_list.deserialize_json(
                data["revisionWeights"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.revision_weights required"
        )
    if data.get("regions") is not None:
        import capo_lambda_web.types.region_list

        out["regions"] = capo_lambda_web.types.region_list.deserialize_json(
            data["regions"]
        )
    else:
        raise DeserializationError("CreateWebFunctionEndpointResponse.regions required")
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
    if data.get("state") is not None:
        import capo_lambda_web.types.endpoint_state

        out["state"] = capo_lambda_web.types.endpoint_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("CreateWebFunctionEndpointResponse.state required")
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.state_reason required"
        )
    if data.get("updateStatus") is not None:
        import capo_lambda_web.types.endpoint_update_status

        out["update_status"] = (
            capo_lambda_web.types.endpoint_update_status.deserialize_json(
                data["updateStatus"]
            )
        )
    if data.get("updateStatusReason") is not None:
        out["update_status_reason"] = data["updateStatusReason"]
    if data.get("regionalEndpoints") is not None:
        import capo_lambda_web.types.regional_endpoints

        out["regional_endpoints"] = (
            capo_lambda_web.types.regional_endpoints.deserialize_json(
                data["regionalEndpoints"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.regional_endpoints required"
        )
    if data.get("createdAt") is not None:
        import capo_lambda_web.types.date_time

        out["created_at"] = capo_lambda_web.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.created_at required"
        )
    if data.get("updatedAt") is not None:
        import capo_lambda_web.types.date_time

        out["updated_at"] = capo_lambda_web.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionEndpointResponse.updated_at required"
        )
    return out
