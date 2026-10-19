"""Generated from Smithy shape ``com.amazonaws.ssm#OpsResultAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_data_type_name


class OpsResultAttribute(TypedDict, closed=True):
    type_name: "capo_ssm.types.ops_data_type_name.OpsDataTypeName"
    """<p>Name of the data type. Valid value: <code>AWS:OpsItem</code>, <code>AWS:EC2InstanceInformation</code>, <code>AWS:OpsItemTrendline</code>, or <code>AWS:ComplianceSummary</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsResultAttribute) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsResultAttribute:
    out: OpsResultAttribute = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    else:
        out["type_name"] = ""
    return out
