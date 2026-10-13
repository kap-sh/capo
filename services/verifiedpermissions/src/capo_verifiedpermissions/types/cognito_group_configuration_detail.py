"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CognitoGroupConfigurationDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.group_entity_type


class CognitoGroupConfigurationDetail(TypedDict, closed=True):
    group_entity_type: NotRequired[
        "capo_verifiedpermissions.types.group_entity_type.GroupEntityType"
    ]
    """<p>The name of the schema entity type that's mapped to the user pool group. Defaults to <code>AWS::CognitoGroup</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CognitoGroupConfigurationDetail) -> dict:
    out: dict = {}
    if "group_entity_type" in value:
        out["groupEntityType"] = value["group_entity_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CognitoGroupConfigurationDetail:
    out: CognitoGroupConfigurationDetail = {}  # type: ignore[typeddict-item]
    if data.get("groupEntityType") is not None:
        out["group_entity_type"] = data["groupEntityType"]
    return out


def redact_sensitive(value: CognitoGroupConfigurationDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "group_entity_type" in value:
        out["group_entity_type"] = "*** Sensitive Data Redacted ***"
    return out
