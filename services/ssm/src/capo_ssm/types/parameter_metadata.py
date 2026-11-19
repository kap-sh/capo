"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.allowed_pattern
    import capo_ssm.types.date_time
    import capo_ssm.types.parameter_data_type
    import capo_ssm.types.parameter_description
    import capo_ssm.types.parameter_key_id
    import capo_ssm.types.parameter_policy_list
    import capo_ssm.types.parameter_tier
    import capo_ssm.types.parameter_type
    import capo_ssm.types.ps_parameter_name
    import capo_ssm.types.ps_parameter_version
    import capo_ssm.types.string


class ParameterMetadata(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.ps_parameter_name.PSParameterName"]
    """<p>The parameter name.</p>"""
    arn: NotRequired["capo_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the parameter.</p>"""
    type: NotRequired["capo_ssm.types.parameter_type.ParameterType"]
    """<p>The type of parameter. Valid parameter types include the following: <code>String</code>, <code>StringList</code>, and <code>SecureString</code>.</p>"""
    key_id: NotRequired["capo_ssm.types.parameter_key_id.ParameterKeyId"]
    """<p>The alias of the Key Management Service (KMS) key used to encrypt the parameter. Applies to <code>SecureString</code> parameters only.</p>"""
    last_modified_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>Date the parameter was last changed or updated.</p>"""
    last_modified_user: NotRequired["capo_ssm.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the Amazon Web Services user who last changed the parameter.</p>"""
    description: NotRequired[
        "capo_ssm.types.parameter_description.ParameterDescription"
    ]
    """<p>Description of the parameter actions.</p>"""
    allowed_pattern: NotRequired["capo_ssm.types.allowed_pattern.AllowedPattern"]
    """<p>A parameter name can include only the following letters and symbols.</p> <p>a-zA-Z0-9_.-</p>"""
    version: "capo_ssm.types.ps_parameter_version.PSParameterVersion"
    """<p>The parameter version.</p>"""
    tier: NotRequired["capo_ssm.types.parameter_tier.ParameterTier"]
    """<p>The parameter tier.</p>"""
    policies: NotRequired["capo_ssm.types.parameter_policy_list.ParameterPolicyList"]
    """<p>A list of policies associated with a parameter.</p>"""
    data_type: NotRequired["capo_ssm.types.parameter_data_type.ParameterDataType"]
    """<p>The data type of the parameter, such as <code>text</code>, <code>aws:ec2:image</code>, or <code>json</code>. The default is <code>text</code>. For the list of data types, see the <code>DataType</code> parameter of <code>PutParameter</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "type" in value:
        import capo_ssm.types.parameter_type

        out["Type"] = capo_ssm.types.parameter_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "last_modified_date" in value:
        import capo_ssm.types.date_time

        out["LastModifiedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_modified_date"]
        )
    if "last_modified_user" in value:
        out["LastModifiedUser"] = value["last_modified_user"]
    if "description" in value:
        out["Description"] = value["description"]
    if "allowed_pattern" in value:
        out["AllowedPattern"] = value["allowed_pattern"]
    out["Version"] = value.get("version", 0)
    if "tier" in value:
        import capo_ssm.types.parameter_tier

        out["Tier"] = capo_ssm.types.parameter_tier.serialize_aws_json_1_1(
            value["tier"]
        )
    if "policies" in value:
        import capo_ssm.types.parameter_policy_list

        out["Policies"] = capo_ssm.types.parameter_policy_list.serialize_aws_json_1_1(
            value["policies"]
        )
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterMetadata:
    out: ParameterMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("Type") is not None:
        import capo_ssm.types.parameter_type

        out["type"] = capo_ssm.types.parameter_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("LastModifiedDate") is not None:
        import capo_ssm.types.date_time

        out["last_modified_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LastModifiedDate"]
        )
    if data.get("LastModifiedUser") is not None:
        out["last_modified_user"] = data["LastModifiedUser"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AllowedPattern") is not None:
        out["allowed_pattern"] = data["AllowedPattern"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if data.get("Tier") is not None:
        import capo_ssm.types.parameter_tier

        out["tier"] = capo_ssm.types.parameter_tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    if data.get("Policies") is not None:
        import capo_ssm.types.parameter_policy_list

        out["policies"] = capo_ssm.types.parameter_policy_list.deserialize_aws_json_1_1(
            data["Policies"]
        )
    if data.get("DataType") is not None:
        out["data_type"] = data["DataType"]
    return out
