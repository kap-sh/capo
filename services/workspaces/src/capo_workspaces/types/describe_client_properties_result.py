"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeClientPropertiesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.client_properties_list


class DescribeClientPropertiesResult(TypedDict, closed=True):
    client_properties_list: NotRequired[
        "capo_workspaces.types.client_properties_list.ClientPropertiesList"
    ]
    """<p>Information about the specified Amazon WorkSpaces clients.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClientPropertiesResult) -> dict:
    out: dict = {}
    if "client_properties_list" in value:
        import capo_workspaces.types.client_properties_list

        out["ClientPropertiesList"] = (
            capo_workspaces.types.client_properties_list.serialize_aws_json_1_1(
                value["client_properties_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClientPropertiesResult:
    out: DescribeClientPropertiesResult = {}  # type: ignore[typeddict-item]
    if data.get("ClientPropertiesList") is not None:
        import capo_workspaces.types.client_properties_list

        out["client_properties_list"] = (
            capo_workspaces.types.client_properties_list.deserialize_aws_json_1_1(
                data["ClientPropertiesList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeClientPropertiesResult) -> dict:
    out: dict = {}
    if "client_properties_list" in value:
        import capo_workspaces.types.client_properties_list

        out["ClientPropertiesList"] = (
            capo_workspaces.types.client_properties_list.serialize_cbor(
                value["client_properties_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeClientPropertiesResult:
    out: DescribeClientPropertiesResult = {}  # type: ignore[typeddict-item]
    if data.get("ClientPropertiesList") is not None:
        import capo_workspaces.types.client_properties_list

        out["client_properties_list"] = (
            capo_workspaces.types.client_properties_list.deserialize_cbor(
                data["ClientPropertiesList"]
            )
        )
    return out
