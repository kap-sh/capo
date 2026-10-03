"""Generated from Smithy shape ``com.amazonaws.ssm#GetParametersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.parameter_name_list


class GetParametersRequest(TypedDict, closed=True):
    names: "capo_ssm.types.parameter_name_list.ParameterNameList"
    """<p>The names or Amazon Resource Names (ARNs) of the parameters that you want to query. For parameters shared with you from another account, you must use the full ARNs.</p> <p>To query by parameter label, use <code>"Name": "name:label"</code>. To query by parameter version, use <code>"Name": "name:version"</code>.</p> <note> <p>The results for <code>GetParameters</code> requests are listed in alphabetical order in query responses.</p> </note> <p>For information about shared parameters, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html">Working with shared parameters</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    with_decryption: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Return decrypted secure string value. Return decrypted values for secure string parameters. This flag is ignored for <code>String</code> and <code>StringList</code> parameter types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParametersRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.parameter_name_list

    out["Names"] = capo_ssm.types.parameter_name_list.serialize_aws_json_1_1(
        value["names"]
    )
    if "with_decryption" in value:
        out["WithDecryption"] = value["with_decryption"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParametersRequest:
    out: GetParametersRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_ssm.types.parameter_name_list

        out["names"] = capo_ssm.types.parameter_name_list.deserialize_aws_json_1_1(
            data["Names"]
        )
    else:
        raise DeserializationError("GetParametersRequest.names required")
    if data.get("WithDecryption") is not None:
        out["with_decryption"] = data["WithDecryption"]
    return out
