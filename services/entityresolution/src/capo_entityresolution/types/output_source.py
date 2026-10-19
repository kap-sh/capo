"""Generated from Smithy shape ``com.amazonaws.entityresolution#OutputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.customer_profiles_integration_config
    import capo_entityresolution.types.kms_arn
    import capo_entityresolution.types.optional_s3_path
    import capo_entityresolution.types.output_attributes


class OutputSource(TypedDict, closed=True):
    kms_arn: NotRequired["capo_entityresolution.types.kms_arn.KMSArn"]
    """<p>Customer KMS ARN for encryption at rest. If not provided, system will use an Entity Resolution managed KMS key.</p>"""
    output_s3_path: "capo_entityresolution.types.optional_s3_path.OptionalS3Path"
    """<p>The S3 path to which Entity Resolution will write the output table.</p>"""
    output: "capo_entityresolution.types.output_attributes.OutputAttributes"
    """<p>A list of <code>OutputAttribute</code> objects, each of which have the fields <code>Name</code> and <code>Hashed</code>. Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.</p>"""
    apply_normalization: NotRequired["bool"]
    """<p>Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an <code>AttributeType</code> of <code>PHONE_NUMBER</code>, and the data in the input table is in a format of 1234567890, Entity Resolution will normalize this field in the output to (123)-456-7890.</p>"""
    customer_profiles_integration_config: NotRequired[
        "capo_entityresolution.types.customer_profiles_integration_config.CustomerProfilesIntegrationConfig"
    ]
    """<p>Specifies the Customer Profiles integration configuration for sending matched output directly to Customer Profiles. When configured, Entity Resolution automatically creates and updates customer profiles based on match clusters, eliminating the need for manual Amazon S3 integration setup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputSource) -> dict:
    out: dict = {}
    if "kms_arn" in value:
        out["KMSArn"] = value["kms_arn"]
    out["outputS3Path"] = value.get("output_s3_path", "")
    import capo_entityresolution.types.output_attributes

    out["output"] = capo_entityresolution.types.output_attributes.serialize_json(
        value["output"]
    )
    if "apply_normalization" in value:
        out["applyNormalization"] = value["apply_normalization"]
    if "customer_profiles_integration_config" in value:
        import capo_entityresolution.types.customer_profiles_integration_config

        out["customerProfilesIntegrationConfig"] = (
            capo_entityresolution.types.customer_profiles_integration_config.serialize_json(
                value["customer_profiles_integration_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputSource:
    out: OutputSource = {}  # type: ignore[typeddict-item]
    if data.get("KMSArn") is not None:
        out["kms_arn"] = data["KMSArn"]
    if data.get("outputS3Path") is not None:
        out["output_s3_path"] = data["outputS3Path"]
    else:
        out["output_s3_path"] = ""
    if data.get("output") is not None:
        import capo_entityresolution.types.output_attributes

        out["output"] = capo_entityresolution.types.output_attributes.deserialize_json(
            data["output"]
        )
    else:
        out["output"] = []
    if data.get("applyNormalization") is not None:
        out["apply_normalization"] = data["applyNormalization"]
    if data.get("customerProfilesIntegrationConfig") is not None:
        import capo_entityresolution.types.customer_profiles_integration_config

        out["customer_profiles_integration_config"] = (
            capo_entityresolution.types.customer_profiles_integration_config.deserialize_json(
                data["customerProfilesIntegrationConfig"]
            )
        )
    return out
