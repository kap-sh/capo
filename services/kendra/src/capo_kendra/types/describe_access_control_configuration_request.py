"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeAccessControlConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.access_control_configuration_id
    import capo_kendra.types.index_id


class DescribeAccessControlConfigurationRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for an access control configuration.</p>"""
    id: "capo_kendra.types.access_control_configuration_id.AccessControlConfigurationId"
    """<p>The identifier of the access control configuration you want to get information on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccessControlConfigurationRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccessControlConfigurationRequest:
    out: DescribeAccessControlConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
