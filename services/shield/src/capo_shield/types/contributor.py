"""Generated from Smithy shape ``com.amazonaws.shield#Contributor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.long
    import capo_shield.types.string


class Contributor(TypedDict, closed=True):
    name: NotRequired["capo_shield.types.string.String"]
    """<p>The name of the contributor. The type of name that you'll find here depends on the <code>AttackPropertyIdentifier</code> setting in the <code>AttackProperty</code> where this contributor is defined. For example, if the <code>AttackPropertyIdentifier</code> is <code>SOURCE_COUNTRY</code>, the <code>Name</code> could be <code>United States</code>.</p>"""
    value: "capo_shield.types.long.Long"
    """<p>The contribution of this contributor expressed in <a>Protection</a> units. For example <code>10,000</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Contributor) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["Value"] = value.get("value", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Contributor:
    out: Contributor = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Contributor) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["Value"] = value.get("value", 0)
    return out


def deserialize_cbor(data: dict) -> Contributor:
    out: Contributor = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    return out
