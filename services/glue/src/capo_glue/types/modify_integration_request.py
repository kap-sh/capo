"""Generated from Smithy shape ``com.amazonaws.glue#ModifyIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_config
    import capo_glue.types.integration_description
    import capo_glue.types.string128
    import capo_glue.types.string2048


class ModifyIntegrationRequest(TypedDict, closed=True):
    integration_identifier: "capo_glue.types.string128.String128"
    """<p>The Amazon Resource Name (ARN) for the integration.</p>"""
    description: NotRequired[
        "capo_glue.types.integration_description.IntegrationDescription"
    ]
    """<p>A description of the integration.</p>"""
    data_filter: NotRequired["capo_glue.types.string2048.String2048"]
    """<p>Selects source tables for the integration using Maxwell filter syntax.</p>"""
    integration_config: NotRequired[
        "capo_glue.types.integration_config.IntegrationConfig"
    ]
    """<p>The configuration settings for the integration. Currently, only the RefreshInterval can be modified. </p>"""
    integration_name: NotRequired["capo_glue.types.string128.String128"]
    """<p>A unique name for an integration in Glue.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyIntegrationRequest) -> dict:
    out: dict = {}
    out["IntegrationIdentifier"] = value["integration_identifier"]
    if "description" in value:
        out["Description"] = value["description"]
    if "data_filter" in value:
        out["DataFilter"] = value["data_filter"]
    if "integration_config" in value:
        import capo_glue.types.integration_config

        out["IntegrationConfig"] = (
            capo_glue.types.integration_config.serialize_aws_json_1_1(
                value["integration_config"]
            )
        )
    if "integration_name" in value:
        out["IntegrationName"] = value["integration_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyIntegrationRequest:
    out: ModifyIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("IntegrationIdentifier") is not None:
        out["integration_identifier"] = data["IntegrationIdentifier"]
    else:
        out["integration_identifier"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DataFilter") is not None:
        out["data_filter"] = data["DataFilter"]
    if data.get("IntegrationConfig") is not None:
        import capo_glue.types.integration_config

        out["integration_config"] = (
            capo_glue.types.integration_config.deserialize_aws_json_1_1(
                data["IntegrationConfig"]
            )
        )
    if data.get("IntegrationName") is not None:
        out["integration_name"] = data["IntegrationName"]
    return out
