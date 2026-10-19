"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CognitoGroupConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.group_entity_type


class CognitoGroupConfiguration(TypedDict, closed=True):
    group_entity_type: (
        "capo_verifiedpermissions.types.group_entity_type.GroupEntityType"
    )
    """<p>The name of the schema entity type that's mapped to the user pool group. Defaults to <code>AWS::CognitoGroup</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CognitoGroupConfiguration) -> dict:
    out: dict = {}
    out["groupEntityType"] = value["group_entity_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CognitoGroupConfiguration:
    out: CognitoGroupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("groupEntityType") is not None:
        out["group_entity_type"] = data["groupEntityType"]
    else:
        out["group_entity_type"] = ""
    return out


def redact_sensitive(value: CognitoGroupConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "group_entity_type" in value:
        out["group_entity_type"] = "*** Sensitive Data Redacted ***"
    return out
