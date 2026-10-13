"""Generated from Smithy shape ``com.amazonaws.ssm#Parameter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.parameter_data_type
    import capo_ssm.types.parameter_type
    import capo_ssm.types.ps_parameter_name
    import capo_ssm.types.ps_parameter_selector
    import capo_ssm.types.ps_parameter_value
    import capo_ssm.types.ps_parameter_version
    import capo_ssm.types.string


class Parameter(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.ps_parameter_name.PSParameterName"]
    """<p>The name of the parameter.</p>"""
    type: NotRequired["capo_ssm.types.parameter_type.ParameterType"]
    """<p>The type of parameter. Valid values include the following: <code>String</code>, <code>StringList</code>, and <code>SecureString</code>.</p> <note> <p>If type is <code>StringList</code>, the system returns a comma-separated string with no spaces between commas in the <code>Value</code> field.</p> </note>"""
    value: NotRequired["capo_ssm.types.ps_parameter_value.PSParameterValue"]
    """<p>The parameter value.</p> <note> <p>If type is <code>StringList</code>, the system returns a comma-separated string with no spaces between commas in the <code>Value</code> field.</p> </note>"""
    version: "capo_ssm.types.ps_parameter_version.PSParameterVersion"
    """<p>The parameter version.</p>"""
    selector: NotRequired["capo_ssm.types.ps_parameter_selector.PSParameterSelector"]
    """<p>Either the version number or the label used to retrieve the parameter value. Specify selectors by using one of the following formats:</p> <p>parameter_name:version</p> <p>parameter_name:label</p>"""
    source_result: NotRequired["capo_ssm.types.string.String"]
    """<p>Applies to parameters that reference information in other Amazon Web Services services. <code>SourceResult</code> is the raw result or response from the source.</p>"""
    last_modified_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>Date the parameter was last changed or updated and the parameter version was created.</p>"""
    arn: NotRequired["capo_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the parameter.</p>"""
    data_type: NotRequired["capo_ssm.types.parameter_data_type.ParameterDataType"]
    """<p>The data type of the parameter, such as <code>text</code> or <code>aws:ec2:image</code>. The default is <code>text</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Parameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_ssm.types.parameter_type

        out["Type"] = capo_ssm.types.parameter_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    out["Version"] = value.get("version", 0)
    if "selector" in value:
        out["Selector"] = value["selector"]
    if "source_result" in value:
        out["SourceResult"] = value["source_result"]
    if "last_modified_date" in value:
        import capo_ssm.types.date_time

        out["LastModifiedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_modified_date"]
        )
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_ssm.types.parameter_type

        out["type"] = capo_ssm.types.parameter_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if data.get("Selector") is not None:
        out["selector"] = data["Selector"]
    if data.get("SourceResult") is not None:
        out["source_result"] = data["SourceResult"]
    if data.get("LastModifiedDate") is not None:
        import capo_ssm.types.date_time

        out["last_modified_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LastModifiedDate"]
        )
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("DataType") is not None:
        out["data_type"] = data["DataType"]
    return out


def redact_sensitive(value: Parameter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
