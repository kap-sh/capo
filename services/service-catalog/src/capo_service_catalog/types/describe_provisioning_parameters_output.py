"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProvisioningParametersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.constraint_summaries
    import capo_service_catalog.types.provisioning_artifact_outputs
    import capo_service_catalog.types.provisioning_artifact_parameters
    import capo_service_catalog.types.provisioning_artifact_preferences
    import capo_service_catalog.types.tag_option_summaries
    import capo_service_catalog.types.usage_instructions


class DescribeProvisioningParametersOutput(TypedDict, closed=True):
    provisioning_artifact_parameters: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_parameters.ProvisioningArtifactParameters"
    ]
    """<p>Information about the parameters used to provision the product.</p>"""
    constraint_summaries: NotRequired[
        "capo_service_catalog.types.constraint_summaries.ConstraintSummaries"
    ]
    """<p>Information about the constraints used to provision the product.</p>"""
    usage_instructions: NotRequired[
        "capo_service_catalog.types.usage_instructions.UsageInstructions"
    ]
    """<p>Any additional metadata specifically related to the provisioning of the product. For example, see the <code>Version</code> field of the CloudFormation template.</p>"""
    tag_options: NotRequired[
        "capo_service_catalog.types.tag_option_summaries.TagOptionSummaries"
    ]
    """<p>Information about the TagOptions associated with the resource.</p>"""
    provisioning_artifact_preferences: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_preferences.ProvisioningArtifactPreferences"
    ]
    """<p>An object that contains information about preferences, such as Regions and accounts, for the provisioning artifact.</p>"""
    provisioning_artifact_outputs: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_outputs.ProvisioningArtifactOutputs"
    ]
    """<p>The output of the provisioning artifact.</p>"""
    provisioning_artifact_output_keys: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_outputs.ProvisioningArtifactOutputs"
    ]
    """<p>A list of the keys and descriptions of the outputs. These outputs can be referenced from a provisioned product launched from this provisioning artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProvisioningParametersOutput) -> dict:
    out: dict = {}
    if "provisioning_artifact_parameters" in value:
        import capo_service_catalog.types.provisioning_artifact_parameters

        out["ProvisioningArtifactParameters"] = (
            capo_service_catalog.types.provisioning_artifact_parameters.serialize_aws_json_1_1(
                value["provisioning_artifact_parameters"]
            )
        )
    if "constraint_summaries" in value:
        import capo_service_catalog.types.constraint_summaries

        out["ConstraintSummaries"] = (
            capo_service_catalog.types.constraint_summaries.serialize_aws_json_1_1(
                value["constraint_summaries"]
            )
        )
    if "usage_instructions" in value:
        import capo_service_catalog.types.usage_instructions

        out["UsageInstructions"] = (
            capo_service_catalog.types.usage_instructions.serialize_aws_json_1_1(
                value["usage_instructions"]
            )
        )
    if "tag_options" in value:
        import capo_service_catalog.types.tag_option_summaries

        out["TagOptions"] = (
            capo_service_catalog.types.tag_option_summaries.serialize_aws_json_1_1(
                value["tag_options"]
            )
        )
    if "provisioning_artifact_preferences" in value:
        import capo_service_catalog.types.provisioning_artifact_preferences

        out["ProvisioningArtifactPreferences"] = (
            capo_service_catalog.types.provisioning_artifact_preferences.serialize_aws_json_1_1(
                value["provisioning_artifact_preferences"]
            )
        )
    if "provisioning_artifact_outputs" in value:
        import capo_service_catalog.types.provisioning_artifact_outputs

        out["ProvisioningArtifactOutputs"] = (
            capo_service_catalog.types.provisioning_artifact_outputs.serialize_aws_json_1_1(
                value["provisioning_artifact_outputs"]
            )
        )
    if "provisioning_artifact_output_keys" in value:
        import capo_service_catalog.types.provisioning_artifact_outputs

        out["ProvisioningArtifactOutputKeys"] = (
            capo_service_catalog.types.provisioning_artifact_outputs.serialize_aws_json_1_1(
                value["provisioning_artifact_output_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProvisioningParametersOutput:
    out: DescribeProvisioningParametersOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisioningArtifactParameters") is not None:
        import capo_service_catalog.types.provisioning_artifact_parameters

        out["provisioning_artifact_parameters"] = (
            capo_service_catalog.types.provisioning_artifact_parameters.deserialize_aws_json_1_1(
                data["ProvisioningArtifactParameters"]
            )
        )
    if data.get("ConstraintSummaries") is not None:
        import capo_service_catalog.types.constraint_summaries

        out["constraint_summaries"] = (
            capo_service_catalog.types.constraint_summaries.deserialize_aws_json_1_1(
                data["ConstraintSummaries"]
            )
        )
    if data.get("UsageInstructions") is not None:
        import capo_service_catalog.types.usage_instructions

        out["usage_instructions"] = (
            capo_service_catalog.types.usage_instructions.deserialize_aws_json_1_1(
                data["UsageInstructions"]
            )
        )
    if data.get("TagOptions") is not None:
        import capo_service_catalog.types.tag_option_summaries

        out["tag_options"] = (
            capo_service_catalog.types.tag_option_summaries.deserialize_aws_json_1_1(
                data["TagOptions"]
            )
        )
    if data.get("ProvisioningArtifactPreferences") is not None:
        import capo_service_catalog.types.provisioning_artifact_preferences

        out["provisioning_artifact_preferences"] = (
            capo_service_catalog.types.provisioning_artifact_preferences.deserialize_aws_json_1_1(
                data["ProvisioningArtifactPreferences"]
            )
        )
    if data.get("ProvisioningArtifactOutputs") is not None:
        import capo_service_catalog.types.provisioning_artifact_outputs

        out["provisioning_artifact_outputs"] = (
            capo_service_catalog.types.provisioning_artifact_outputs.deserialize_aws_json_1_1(
                data["ProvisioningArtifactOutputs"]
            )
        )
    if data.get("ProvisioningArtifactOutputKeys") is not None:
        import capo_service_catalog.types.provisioning_artifact_outputs

        out["provisioning_artifact_output_keys"] = (
            capo_service_catalog.types.provisioning_artifact_outputs.deserialize_aws_json_1_1(
                data["ProvisioningArtifactOutputKeys"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProvisioningParametersOutput) -> dict:
    out: dict = {}
    if "provisioning_artifact_parameters" in value:
        import capo_service_catalog.types.provisioning_artifact_parameters

        out["ProvisioningArtifactParameters"] = (
            capo_service_catalog.types.provisioning_artifact_parameters.serialize_cbor(
                value["provisioning_artifact_parameters"]
            )
        )
    if "constraint_summaries" in value:
        import capo_service_catalog.types.constraint_summaries

        out["ConstraintSummaries"] = (
            capo_service_catalog.types.constraint_summaries.serialize_cbor(
                value["constraint_summaries"]
            )
        )
    if "usage_instructions" in value:
        import capo_service_catalog.types.usage_instructions

        out["UsageInstructions"] = (
            capo_service_catalog.types.usage_instructions.serialize_cbor(
                value["usage_instructions"]
            )
        )
    if "tag_options" in value:
        import capo_service_catalog.types.tag_option_summaries

        out["TagOptions"] = (
            capo_service_catalog.types.tag_option_summaries.serialize_cbor(
                value["tag_options"]
            )
        )
    if "provisioning_artifact_preferences" in value:
        import capo_service_catalog.types.provisioning_artifact_preferences

        out["ProvisioningArtifactPreferences"] = (
            capo_service_catalog.types.provisioning_artifact_preferences.serialize_cbor(
                value["provisioning_artifact_preferences"]
            )
        )
    if "provisioning_artifact_outputs" in value:
        import capo_service_catalog.types.provisioning_artifact_outputs

        out["ProvisioningArtifactOutputs"] = (
            capo_service_catalog.types.provisioning_artifact_outputs.serialize_cbor(
                value["provisioning_artifact_outputs"]
            )
        )
    if "provisioning_artifact_output_keys" in value:
        import capo_service_catalog.types.provisioning_artifact_outputs

        out["ProvisioningArtifactOutputKeys"] = (
            capo_service_catalog.types.provisioning_artifact_outputs.serialize_cbor(
                value["provisioning_artifact_output_keys"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeProvisioningParametersOutput:
    out: DescribeProvisioningParametersOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisioningArtifactParameters") is not None:
        import capo_service_catalog.types.provisioning_artifact_parameters

        out["provisioning_artifact_parameters"] = (
            capo_service_catalog.types.provisioning_artifact_parameters.deserialize_cbor(
                data["ProvisioningArtifactParameters"]
            )
        )
    if data.get("ConstraintSummaries") is not None:
        import capo_service_catalog.types.constraint_summaries

        out["constraint_summaries"] = (
            capo_service_catalog.types.constraint_summaries.deserialize_cbor(
                data["ConstraintSummaries"]
            )
        )
    if data.get("UsageInstructions") is not None:
        import capo_service_catalog.types.usage_instructions

        out["usage_instructions"] = (
            capo_service_catalog.types.usage_instructions.deserialize_cbor(
                data["UsageInstructions"]
            )
        )
    if data.get("TagOptions") is not None:
        import capo_service_catalog.types.tag_option_summaries

        out["tag_options"] = (
            capo_service_catalog.types.tag_option_summaries.deserialize_cbor(
                data["TagOptions"]
            )
        )
    if data.get("ProvisioningArtifactPreferences") is not None:
        import capo_service_catalog.types.provisioning_artifact_preferences

        out["provisioning_artifact_preferences"] = (
            capo_service_catalog.types.provisioning_artifact_preferences.deserialize_cbor(
                data["ProvisioningArtifactPreferences"]
            )
        )
    if data.get("ProvisioningArtifactOutputs") is not None:
        import capo_service_catalog.types.provisioning_artifact_outputs

        out["provisioning_artifact_outputs"] = (
            capo_service_catalog.types.provisioning_artifact_outputs.deserialize_cbor(
                data["ProvisioningArtifactOutputs"]
            )
        )
    if data.get("ProvisioningArtifactOutputKeys") is not None:
        import capo_service_catalog.types.provisioning_artifact_outputs

        out["provisioning_artifact_output_keys"] = (
            capo_service_catalog.types.provisioning_artifact_outputs.deserialize_cbor(
                data["ProvisioningArtifactOutputKeys"]
            )
        )
    return out
