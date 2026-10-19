"""Generated from Smithy shape ``com.amazonaws.kendra#CreateAccessControlConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.access_control_configuration_id


class CreateAccessControlConfigurationResponse(TypedDict, closed=True):
    id: "capo_kendra.types.access_control_configuration_id.AccessControlConfigurationId"
    """<p>The identifier of the access control configuration for your documents in an index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccessControlConfigurationResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccessControlConfigurationResponse:
    out: CreateAccessControlConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
