"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SsmParameterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.account_id
    import capo_imagebuilder.types.ssm_parameter_data_type
    import capo_imagebuilder.types.ssm_parameter_name


class SsmParameterConfiguration(TypedDict, closed=True):
    ami_account_id: NotRequired["capo_imagebuilder.types.account_id.AccountId"]
    """<p>Specify the account that will own the Parameter in a given Region. During distribution, this account must be specified in distribution settings as a target account for the Region.</p>"""
    parameter_name: "capo_imagebuilder.types.ssm_parameter_name.SsmParameterName"
    """<p>This is the name of the Parameter in the target Region or account. The image distribution creates the Parameter if it doesn't already exist. Otherwise, it updates the parameter.</p>"""
    data_type: NotRequired[
        "capo_imagebuilder.types.ssm_parameter_data_type.SsmParameterDataType"
    ]
    """<p>The type of value the parameter contains. We recommend the <code>aws:ec2:image</code> data type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsmParameterConfiguration) -> dict:
    out: dict = {}
    if "ami_account_id" in value:
        out["amiAccountId"] = value["ami_account_id"]
    out["parameterName"] = value["parameter_name"]
    if "data_type" in value:
        import capo_imagebuilder.types.ssm_parameter_data_type

        out["dataType"] = (
            capo_imagebuilder.types.ssm_parameter_data_type.serialize_json(
                value["data_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> SsmParameterConfiguration:
    out: SsmParameterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("amiAccountId") is not None:
        out["ami_account_id"] = data["amiAccountId"]
    if data.get("parameterName") is not None:
        out["parameter_name"] = data["parameterName"]
    else:
        out["parameter_name"] = ""
    if data.get("dataType") is not None:
        import capo_imagebuilder.types.ssm_parameter_data_type

        out["data_type"] = (
            capo_imagebuilder.types.ssm_parameter_data_type.deserialize_json(
                data["dataType"]
            )
        )
    return out
