"""Generated from Smithy shape ``com.amazonaws.configservice#PutRemediationConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.remediation_configurations


class PutRemediationConfigurationsRequest(TypedDict, closed=True):
    remediation_configurations: (
        "capo_config_service.types.remediation_configurations.RemediationConfigurations"
    )
    """<p>A list of remediation configuration objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRemediationConfigurationsRequest) -> dict:
    out: dict = {}
    import capo_config_service.types.remediation_configurations

    out["RemediationConfigurations"] = (
        capo_config_service.types.remediation_configurations.serialize_aws_json_1_1(
            value["remediation_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRemediationConfigurationsRequest:
    out: PutRemediationConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("RemediationConfigurations") is not None:
        import capo_config_service.types.remediation_configurations

        out["remediation_configurations"] = (
            capo_config_service.types.remediation_configurations.deserialize_aws_json_1_1(
                data["RemediationConfigurations"]
            )
        )
    else:
        out["remediation_configurations"] = []
    return out
