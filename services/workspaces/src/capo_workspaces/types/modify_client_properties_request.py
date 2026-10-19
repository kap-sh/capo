"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyClientPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.client_properties
    import capo_workspaces.types.non_empty_string


class ModifyClientPropertiesRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.non_empty_string.NonEmptyString"
    """<p>The resource identifiers, in the form of directory IDs.</p>"""
    client_properties: "capo_workspaces.types.client_properties.ClientProperties"
    """<p>Information about the Amazon WorkSpaces client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyClientPropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_workspaces.types.client_properties

    out["ClientProperties"] = (
        capo_workspaces.types.client_properties.serialize_aws_json_1_1(
            value["client_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyClientPropertiesRequest:
    out: ModifyClientPropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ClientProperties") is not None:
        import capo_workspaces.types.client_properties

        out["client_properties"] = (
            capo_workspaces.types.client_properties.deserialize_aws_json_1_1(
                data["ClientProperties"]
            )
        )
    else:
        raise DeserializationError(
            "ModifyClientPropertiesRequest.client_properties required"
        )
    return out
