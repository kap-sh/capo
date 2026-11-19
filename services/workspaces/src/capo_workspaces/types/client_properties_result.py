"""Generated from Smithy shape ``com.amazonaws.workspaces#ClientPropertiesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.client_properties
    import capo_workspaces.types.non_empty_string


class ClientPropertiesResult(TypedDict, closed=True):
    resource_id: NotRequired["capo_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The resource identifier, in the form of a directory ID.</p>"""
    client_properties: NotRequired[
        "capo_workspaces.types.client_properties.ClientProperties"
    ]
    """<p>Information about the Amazon WorkSpaces client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientPropertiesResult) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "client_properties" in value:
        import capo_workspaces.types.client_properties

        out["ClientProperties"] = (
            capo_workspaces.types.client_properties.serialize_aws_json_1_1(
                value["client_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientPropertiesResult:
    out: ClientPropertiesResult = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ClientProperties") is not None:
        import capo_workspaces.types.client_properties

        out["client_properties"] = (
            capo_workspaces.types.client_properties.deserialize_aws_json_1_1(
                data["ClientProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClientPropertiesResult) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "client_properties" in value:
        import capo_workspaces.types.client_properties

        out["ClientProperties"] = (
            capo_workspaces.types.client_properties.serialize_cbor(
                value["client_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ClientPropertiesResult:
    out: ClientPropertiesResult = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ClientProperties") is not None:
        import capo_workspaces.types.client_properties

        out["client_properties"] = (
            capo_workspaces.types.client_properties.deserialize_cbor(
                data["ClientProperties"]
            )
        )
    return out
