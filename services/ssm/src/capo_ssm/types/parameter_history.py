"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.allowed_pattern
    import capo_ssm.types.date_time
    import capo_ssm.types.parameter_data_type
    import capo_ssm.types.parameter_description
    import capo_ssm.types.parameter_key_id
    import capo_ssm.types.parameter_label_list
    import capo_ssm.types.parameter_policy_list
    import capo_ssm.types.parameter_tier
    import capo_ssm.types.parameter_type
    import capo_ssm.types.ps_parameter_name
    import capo_ssm.types.ps_parameter_value
    import capo_ssm.types.ps_parameter_version
    import capo_ssm.types.string


class ParameterHistory(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.ps_parameter_name.PSParameterName"]
    """<p>The name of the parameter.</p>"""
    type: NotRequired["capo_ssm.types.parameter_type.ParameterType"]
    """<p>The type of parameter used.</p>"""
    key_id: NotRequired["capo_ssm.types.parameter_key_id.ParameterKeyId"]
    """<p>The alias of the Key Management Service (KMS) key used to encrypt the parameter. Applies to <code>SecureString</code> parameters only</p>"""
    last_modified_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>Date the parameter was last changed or updated.</p>"""
    last_modified_user: NotRequired["capo_ssm.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the Amazon Web Services user who last changed the parameter.</p>"""
    description: NotRequired[
        "capo_ssm.types.parameter_description.ParameterDescription"
    ]
    """<p>Information about the parameter.</p>"""
    value: NotRequired["capo_ssm.types.ps_parameter_value.PSParameterValue"]
    """<p>The parameter value.</p>"""
    allowed_pattern: NotRequired["capo_ssm.types.allowed_pattern.AllowedPattern"]
    """<p>Parameter names can include the following letters and symbols.</p> <p>a-zA-Z0-9_.-</p>"""
    version: "capo_ssm.types.ps_parameter_version.PSParameterVersion"
    """<p>The parameter version.</p>"""
    labels: NotRequired["capo_ssm.types.parameter_label_list.ParameterLabelList"]
    """<p>Labels assigned to the parameter version.</p>"""
    tier: NotRequired["capo_ssm.types.parameter_tier.ParameterTier"]
    """<p>The parameter tier.</p>"""
    policies: NotRequired["capo_ssm.types.parameter_policy_list.ParameterPolicyList"]
    """<p>Information about the policies assigned to a parameter.</p> <p> <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html">Assigning parameter policies</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    data_type: NotRequired["capo_ssm.types.parameter_data_type.ParameterDataType"]
    """<p>The data type of the parameter, such as <code>text</code> or <code>aws:ec2:image</code>. The default is <code>text</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterHistory) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
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
    if "value" in value:
        out["Value"] = value["value"]
    if "allowed_pattern" in value:
        out["AllowedPattern"] = value["allowed_pattern"]
    out["Version"] = value.get("version", 0)
    if "labels" in value:
        import capo_ssm.types.parameter_label_list

        out["Labels"] = capo_ssm.types.parameter_label_list.serialize_aws_json_1_1(
            value["labels"]
        )
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


def deserialize_aws_json_1_1(data: dict) -> ParameterHistory:
    out: ParameterHistory = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("AllowedPattern") is not None:
        out["allowed_pattern"] = data["AllowedPattern"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if data.get("Labels") is not None:
        import capo_ssm.types.parameter_label_list

        out["labels"] = capo_ssm.types.parameter_label_list.deserialize_aws_json_1_1(
            data["Labels"]
        )
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
