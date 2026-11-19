"""Generated from Smithy shape ``com.amazonaws.appstream#EntitlementAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string


class EntitlementAttribute(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>A supported AWS IAM SAML <code>PrincipalTag</code> attribute that is matched to the associated value when a user identity federates into a WorkSpaces Applications SAML application.</p> <p>The following are valid values:</p> <ul> <li> <p>roles</p> </li> <li> <p>department </p> </li> <li> <p>organization </p> </li> <li> <p>groups </p> </li> <li> <p>title </p> </li> <li> <p>costCenter </p> </li> <li> <p>userType</p> </li> </ul> <p> </p>"""
    value: NotRequired["capo_appstream.types.string.String"]
    """<p>A value that is matched to a supported SAML attribute name when a user identity federates into a WorkSpaces Applications SAML application. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementAttribute) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntitlementAttribute:
    out: EntitlementAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntitlementAttribute) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> EntitlementAttribute:
    out: EntitlementAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
