"""Generated from Smithy shape ``com.amazonaws.ssm#GetParameterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.ps_parameter_name


class GetParameterRequest(TypedDict, closed=True):
    name: "capo_ssm.types.ps_parameter_name.PSParameterName"
    """<p>The name or Amazon Resource Name (ARN) of the parameter that you want to query. For parameters shared with you from another account, you must use the full ARN.</p> <p>To query by parameter label, use <code>"Name": "name:label"</code>. To query by parameter version, use <code>"Name": "name:version"</code>.</p> <p>For more information about shared parameters, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html">Working with shared parameters</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    with_decryption: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Return decrypted values for secure string parameters. This flag is ignored for <code>String</code> and <code>StringList</code> parameter types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParameterRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "with_decryption" in value:
        out["WithDecryption"] = value["with_decryption"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParameterRequest:
    out: GetParameterRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetParameterRequest.name required")
    if data.get("WithDecryption") is not None:
        out["with_decryption"] = data["WithDecryption"]
    return out
