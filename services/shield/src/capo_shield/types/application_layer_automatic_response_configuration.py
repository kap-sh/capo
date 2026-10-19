"""Generated from Smithy shape ``com.amazonaws.shield#ApplicationLayerAutomaticResponseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_shield.errors import DeserializationError

if TYPE_CHECKING:
    import capo_shield.types.application_layer_automatic_response_status
    import capo_shield.types.response_action


class ApplicationLayerAutomaticResponseConfiguration(TypedDict, closed=True):
    status: "capo_shield.types.application_layer_automatic_response_status.ApplicationLayerAutomaticResponseStatus"
    """<p>Indicates whether automatic application layer DDoS mitigation is enabled for the protection. </p>"""
    action: "capo_shield.types.response_action.ResponseAction"
    """<p>Specifies the action setting that Shield Advanced should use in the WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ApplicationLayerAutomaticResponseConfiguration,
) -> dict:
    out: dict = {}
    import capo_shield.types.application_layer_automatic_response_status

    out["Status"] = (
        capo_shield.types.application_layer_automatic_response_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    import capo_shield.types.response_action

    out["Action"] = capo_shield.types.response_action.serialize_aws_json_1_1(
        value["action"]
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ApplicationLayerAutomaticResponseConfiguration:
    out: ApplicationLayerAutomaticResponseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_shield.types.application_layer_automatic_response_status

        out["status"] = (
            capo_shield.types.application_layer_automatic_response_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_shield.types.application_layer_automatic_response_status.ApplicationLayerAutomaticResponseStatus",
            "",
        )
    if data.get("Action") is not None:
        import capo_shield.types.response_action

        out["action"] = capo_shield.types.response_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError(
            "ApplicationLayerAutomaticResponseConfiguration.action required"
        )
    return out
