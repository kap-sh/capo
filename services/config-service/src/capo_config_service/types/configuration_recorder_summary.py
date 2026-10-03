"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.provider
    import capo_config_service.types.recorder_name
    import capo_config_service.types.recording_scope
    import capo_config_service.types.service_principal


class ConfigurationRecorderSummary(TypedDict, closed=True):
    arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the configuration recorder.</p>"""
    name: "capo_config_service.types.recorder_name.RecorderName"
    """<p>The name of the configuration recorder.</p>"""
    service_principal: NotRequired[
        "capo_config_service.types.service_principal.ServicePrincipal"
    ]
    """<p>For service-linked configuration recorders, indicates which Amazon Web Services service the configuration recorder is linked to.</p>"""
    recording_scope: "capo_config_service.types.recording_scope.RecordingScope"
    """<p>Indicates whether the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html">ConfigurationItems</a> in scope for the configuration recorder are recorded for free (<code>INTERNAL</code>) or if you are charged a service fee for recording (<code>PAID</code>).</p>"""
    provider: NotRequired["capo_config_service.types.provider.Provider"]
    """<p>For service-linked configuration recorders that record resources from a third-party cloud service provider, indicates the cloud service provider. Currently, <code>AZURE</code> is supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "service_principal" in value:
        out["servicePrincipal"] = value["service_principal"]
    import capo_config_service.types.recording_scope

    out["recordingScope"] = (
        capo_config_service.types.recording_scope.serialize_aws_json_1_1(
            value["recording_scope"]
        )
    )
    if "provider" in value:
        import capo_config_service.types.provider

        out["provider"] = capo_config_service.types.provider.serialize_aws_json_1_1(
            value["provider"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationRecorderSummary:
    out: ConfigurationRecorderSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ConfigurationRecorderSummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfigurationRecorderSummary.name required")
    if data.get("servicePrincipal") is not None:
        out["service_principal"] = data["servicePrincipal"]
    if data.get("recordingScope") is not None:
        import capo_config_service.types.recording_scope

        out["recording_scope"] = (
            capo_config_service.types.recording_scope.deserialize_aws_json_1_1(
                data["recordingScope"]
            )
        )
    else:
        raise DeserializationError(
            "ConfigurationRecorderSummary.recording_scope required"
        )
    if data.get("provider") is not None:
        import capo_config_service.types.provider

        out["provider"] = capo_config_service.types.provider.deserialize_aws_json_1_1(
            data["provider"]
        )
    return out
