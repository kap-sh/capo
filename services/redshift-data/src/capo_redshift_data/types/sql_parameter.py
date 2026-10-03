"""Generated from Smithy shape ``com.amazonaws.redshiftdata#SqlParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_redshift_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_data.types.parameter_name
    import capo_redshift_data.types.parameter_value


class SqlParameter(TypedDict, closed=True):
    name: "capo_redshift_data.types.parameter_name.ParameterName"
    """<p>The name of the parameter.</p>"""
    value: "capo_redshift_data.types.parameter_value.ParameterValue"
    """<p>The value of the parameter. Amazon Redshift implicitly converts to the proper data type. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html">Data types</a> in the <i>Amazon Redshift Database Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlParameter:
    out: SqlParameter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SqlParameter.name required")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SqlParameter.value required")
    return out
