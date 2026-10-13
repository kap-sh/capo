"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#StaticPolicyDefinitionItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.static_policy_description


class StaticPolicyDefinitionItem(TypedDict, closed=True):
    description: NotRequired[
        "capo_verifiedpermissions.types.static_policy_description.StaticPolicyDescription"
    ]
    """<p>A description of the static policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StaticPolicyDefinitionItem) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StaticPolicyDefinitionItem:
    out: StaticPolicyDefinitionItem = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: StaticPolicyDefinitionItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
