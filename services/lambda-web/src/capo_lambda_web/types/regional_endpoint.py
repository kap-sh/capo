"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RegionalEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.auth_type
    import capo_lambda_web.types.domain_name
    import capo_lambda_web.types.endpoint_state
    import capo_lambda_web.types.endpoint_update_status
    import capo_lambda_web.types.revision_weight_list
    import capo_lambda_web.types.scaling_config
    import capo_lambda_web.types.throttle_config


class RegionalEndpoint(TypedDict, closed=True):
    domain_name: NotRequired["capo_lambda_web.types.domain_name.DomainName"]
    """<p>The domain name of the regional endpoint.</p>"""
    auth_type: "capo_lambda_web.types.auth_type.AuthType"
    """<p>The authorization type for the regional endpoint.</p>"""
    revision_weights: "capo_lambda_web.types.revision_weight_list.RevisionWeightList"
    """<p>The revision weights for the regional endpoint.</p>"""
    scaling_config: NotRequired["capo_lambda_web.types.scaling_config.ScalingConfig"]
    """<p>The scaling configuration for the regional endpoint. This field is absent if the endpoint has no scaling configuration.</p>"""
    throttle_config: NotRequired["capo_lambda_web.types.throttle_config.ThrottleConfig"]
    """<p>The throttling configuration for the regional endpoint. This field is absent if the endpoint has no throttling configuration.</p>"""
    state: "capo_lambda_web.types.endpoint_state.EndpointState"
    """<p>The current state of the regional endpoint.</p>"""
    state_reason: "str"
    """<p>The reason for the current state of the regional endpoint.</p>"""
    update_status: NotRequired[
        "capo_lambda_web.types.endpoint_update_status.EndpointUpdateStatus"
    ]
    """<p>The status of the most recent update to the regional endpoint.</p>"""
    update_status_reason: NotRequired["str"]
    """<p>The reason for the current update status of the regional endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegionalEndpoint) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    import capo_lambda_web.types.auth_type

    out["authType"] = capo_lambda_web.types.auth_type.serialize_json(value["auth_type"])
    import capo_lambda_web.types.revision_weight_list

    out["revisionWeights"] = capo_lambda_web.types.revision_weight_list.serialize_json(
        value["revision_weights"]
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
    return out


def deserialize_json(data: dict) -> RegionalEndpoint:
    out: RegionalEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("authType") is not None:
        import capo_lambda_web.types.auth_type

        out["auth_type"] = capo_lambda_web.types.auth_type.deserialize_json(
            data["authType"]
        )
    else:
        raise DeserializationError("RegionalEndpoint.auth_type required")
    if data.get("revisionWeights") is not None:
        import capo_lambda_web.types.revision_weight_list

        out["revision_weights"] = (
            capo_lambda_web.types.revision_weight_list.deserialize_json(
                data["revisionWeights"]
            )
        )
    else:
        raise DeserializationError("RegionalEndpoint.revision_weights required")
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
        raise DeserializationError("RegionalEndpoint.state required")
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
    else:
        raise DeserializationError("RegionalEndpoint.state_reason required")
    if data.get("updateStatus") is not None:
        import capo_lambda_web.types.endpoint_update_status

        out["update_status"] = (
            capo_lambda_web.types.endpoint_update_status.deserialize_json(
                data["updateStatus"]
            )
        )
    if data.get("updateStatusReason") is not None:
        out["update_status_reason"] = data["updateStatusReason"]
    return out
